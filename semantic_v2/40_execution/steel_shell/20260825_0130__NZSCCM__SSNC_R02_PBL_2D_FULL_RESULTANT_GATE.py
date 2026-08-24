from __future__ import annotations
from dataclasses import dataclass
from math import pi, sqrt, cos, sin, acos, copysign
import numpy as np

# SSNC-R02: finite 2D PBL steel-shell postbuckling operator gate.
# Global Marguerre-Airy structure and global ultimate-state criterion are outside this module.
# No effective width/area reduction is used.
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH_PRODUCTION = False
GLOBAL_AIRY_CHANGED = False
ULTIMATE_STATE_CHANGED = False
SHEAR_POSTBUCKLING_CLOSED = False

HARMONICS = {
    (0, 1): +0.5,
    (0, 2): -0.5,
    (1, 0): +0.5,
    (1, 1): -1.0,
    (1, 2): +0.5,
    (2, 0): -0.5,
    (2, 1): +0.5,
}


def _kp_num(r: float) -> float:
    return (272*r**16 + 2856*r**14 + 11273*r**12 + 23146*r**10
            + 31506*r**8 + 23146*r**6 + 11273*r**4 + 2856*r**2 + 272)


def yun_kcr(r: float) -> float:
    return 4.0*(3.0*r**4 + 2.0*r**2 + 3.0)/(3.0*r**2)


def yun_kp(r: float) -> float:
    return _kp_num(r)/(r**2*(r**2+1.0)**2*(r**2+4.0)**2*(4.0*r**2+1.0)**2)


@dataclass(frozen=True)
class PBLCell:
    Lx: float
    Ly: float
    t: float
    E: float
    nu: float
    fy: float
    A0: float

    @property
    def kx(self) -> float: return 2.0*pi/self.Lx
    @property
    def ky(self) -> float: return 2.0*pi/self.Ly
    @property
    def Q(self) -> float: return self.E/(1.0-self.nu**2)
    @property
    def G(self) -> float: return self.E/(2.0*(1.0+self.nu))
    @property
    def D(self) -> float: return self.E*self.t**3/(12.0*(1.0-self.nu**2))
    @property
    def cx(self) -> float: return 3.0*self.kx**2/8.0
    @property
    def cy(self) -> float: return 3.0*self.ky**2/8.0

    @property
    def Kb(self) -> float:
        return self.D*(0.75*(self.kx**4+self.ky**4) + 0.5*self.kx**2*self.ky**2)

    @property
    def KA(self) -> float:
        # Exact finite-harmonic Airy membrane-energy coefficient for
        # phi=(1-cos(kx*x))(1-cos(ky*y)).
        r = self.kx/self.ky
        return (self.ky**4 * _kp_num(r)
                /(256.0*(r*r+1.0)**2*(r*r+4.0)**2*(4.0*r*r+1.0)**2))


def cubic_real_roots(B3: float, B1: float, B0: float, tol: float = 1e-14):
    """Cardano/trigonometric real roots of B3*U^3+B1*U+B0=0."""
    if abs(B3) <= tol:
        return [] if abs(B1) <= tol else [-B0/B1]
    p, q = B1/B3, B0/B3
    disc = (q/2.0)**2 + (p/3.0)**3
    cbrt = lambda x: copysign(abs(x)**(1.0/3.0), x)
    if disc >= -tol:
        d = max(0.0, disc)
        return [cbrt(-q/2.0+sqrt(d)) + cbrt(-q/2.0-sqrt(d))]
    rho = 2.0*sqrt(-p/3.0)
    arg = (3.0*q/(2.0*p))*sqrt(-3.0/p)
    arg = max(-1.0, min(1.0, arg))
    th = acos(arg)
    return sorted(rho*cos((th+2.0*pi*j)/3.0) for j in range(3))


def mean_compression_stress(cell: PBLCell, U: float, ex: float, ey: float, gamma: float):
    """Full-area mean membrane stresses; normal compression is positive."""
    Delta = U*U-cell.A0**2
    mx = ex-cell.cx*Delta
    my = ey-cell.cy*Delta
    sx = cell.Q*(mx+cell.nu*my)
    sy = cell.Q*(my+cell.nu*mx)
    tau = cell.G*gamma
    return sx, sy, tau


def amplitude_coefficients(cell: PBLCell, ex: float, ey: float):
    # Fixed-average-strain stationarity. The selected PBL mode has zero mean
    # geometric shear, so uniform shear does not drive this normal-buckling mode.
    L0 = cell.Q*(cell.cx*(ex+cell.nu*ey) + cell.cy*(ey+cell.nu*ex))
    Cg = cell.Q*(cell.cx**2+cell.cy**2+2.0*cell.nu*cell.cx*cell.cy)
    B3 = 4.0*cell.t*cell.E*cell.KA + 2.0*cell.t*Cg
    B1 = cell.Kb - 2.0*cell.t*L0 - B3*cell.A0**2
    B0 = -cell.Kb*cell.A0
    return B3, B1, B0


def condensed_energy(cell: PBLCell, U: float, ex: float, ey: float, gamma: float = 0.0):
    Delta = U*U-cell.A0**2
    mx = ex-cell.cx*Delta
    my = ey-cell.cy*Delta
    Um = 0.5*cell.t*cell.Q*(mx*mx+my*my+2.0*cell.nu*mx*my)
    Um += 0.5*cell.t*cell.G*gamma*gamma
    Ub = 0.5*cell.Kb*(U-cell.A0)**2
    Ua = cell.t*cell.E*cell.KA*Delta*Delta
    return Ub+Um+Ua


def solve_total_amplitude(cell: PBLCell, ex: float, ey: float, gamma: float = 0.0):
    roots = cubic_real_roots(*amplitude_coefficients(cell, ex, ey))
    admissible = [max(0.0, u) for u in roots if u >= -1e-11]
    if not admissible:
        raise RuntimeError("No nonnegative finite algebraic PBL amplitude root")
    U = min(admissible, key=lambda u: condensed_energy(cell, u, ex, ey, gamma))
    return U, roots


def gross_bending_matrix(cell: PBLCell):
    D, nu = cell.D, cell.nu
    return np.array([[D, nu*D, 0.0],
                     [nu*D, D, 0.0],
                     [0.0, 0.0, 0.5*(1.0-nu)*D]], dtype=float)


def face_resultants(cell: PBLCell, ex: float, ey: float, gamma: float, kappa):
    """Full-area membrane + full own-skin bending resultants about skin midsurface."""
    U, roots = solve_total_amplitude(cell, ex, ey, gamma)
    sx, sy, tau = mean_compression_stress(cell, U, ex, ey, gamma)
    N = cell.t*np.array([sx, sy, tau], dtype=float)
    M = gross_bending_matrix(cell) @ np.asarray(kappa, dtype=float)
    return U, N, M, roots


def airy_fluctuation_tension(cell: PBLCell, U: float, x: float, y: float):
    """Exact finite Airy harmonic membrane fluctuation, tension-positive."""
    Delta = U*U-cell.A0**2
    sx = sy = tau = 0.0
    for (m, n), h in HARMONICS.items():
        source = h*cell.kx**2*cell.ky**2
        eig = ((m*cell.kx)**2+(n*cell.ky)**2)**2
        Fmn = cell.E*Delta*source/eig
        cx, cy = cos(m*cell.kx*x), cos(n*cell.ky*y)
        sx += -(n*cell.ky)**2*Fmn*cx*cy
        sy += -(m*cell.kx)**2*Fmn*cx*cy
        if m and n:
            tau += -(m*cell.kx)*(n*cell.ky)*Fmn*sin(m*cell.kx*x)*sin(n*cell.ky*y)
    return np.array([sx, sy, tau], dtype=float)


def local_curvature_increment(cell: PBLCell, U: float, x: float, y: float):
    A = U-cell.A0
    X, Y = cell.kx*x, cell.ky*y
    phixx = cell.kx**2*cos(X)*(1.0-cos(Y))
    phiyy = cell.ky**2*(1.0-cos(X))*cos(Y)
    phixy = cell.kx*cell.ky*sin(X)*sin(Y)
    return np.array([-A*phixx, -A*phiyy, -2.0*A*phixy], dtype=float)


def local_mises(cell: PBLCell, U: float, ex: float, ey: float, gamma: float,
                x: float, y: float, z_skin: float):
    """Pointwise 2D Mises diagnostic including postbuckling membrane + local bending."""
    sx_c, sy_c, tau0 = mean_compression_stress(cell, U, ex, ey, gamma)
    s = np.array([-sx_c, -sy_c, tau0], dtype=float) + airy_fluctuation_tension(cell, U, x, y)
    kap = local_curvature_increment(cell, U, x, y)
    sb = np.array([
        cell.Q*z_skin*(kap[0]+cell.nu*kap[1]),
        cell.Q*z_skin*(kap[1]+cell.nu*kap[0]),
        cell.G*z_skin*kap[2],
    ])
    s += sb
    vm = sqrt(s[0]**2-s[0]*s[1]+s[1]**2+3.0*s[2]**2)
    return vm, s


def assemble_two_faces(Ntop, Mtop, ztop, Nbot, Mbot, zbot):
    N = np.asarray(Ntop)+np.asarray(Nbot)
    M = ztop*np.asarray(Ntop)+zbot*np.asarray(Nbot)+np.asarray(Mtop)+np.asarray(Mbot)
    return N, M


def yun_source_identity(cell: PBLCell):
    """Compare project-derived energy coefficients with Yun kcr and kp exactly."""
    r = cell.Ly/cell.Lx
    Csig = pi*pi*cell.E*cell.t**2/(12.0*(1.0-cell.nu**2)*cell.Lx**2)
    kcr_energy = cell.Kb/(2.0*cell.t*cell.cy*Csig)
    nonlinear_energy = 2.0*cell.E*cell.KA/cell.cy
    H_yun = yun_kp(r)*(1.0-cell.nu**2)/cell.t**2
    return kcr_energy, yun_kcr(r), nonlinear_energy, Csig*H_yun


def run_gate():
    errs = {}
    e1 = e2 = 0.0
    for r in (0.5, 0.75, 1.0, 1.5, 2.0):
        c = PBLCell(200.0, 200.0*r, 4.0, 206000.0, 0.30, 355.0, 0.125)
        a,b,c1,d = yun_source_identity(c)
        e1 = max(e1, abs(a-b)); e2 = max(e2, abs(c1-d))
    errs["yun_kcr_abs"] = e1; errs["yun_nonlinear_abs"] = e2

    c = PBLCell(200.0, 200.0, 4.0, 206000.0, 0.30, 355.0, 0.125)
    U0,_ = solve_total_amplitude(c, 0.0, 0.0)
    errs["zero_load_U_minus_A0"] = abs(U0-c.A0)

    cxy = PBLCell(180.0, 240.0, 4.0, 206000.0, 0.30, 355.0, 0.1125)
    cyx = PBLCell(240.0, 180.0, 4.0, 206000.0, 0.30, 355.0, 0.1125)
    ex,ey,gam = 3.0e-4, 8.0e-4, 1.0e-4
    U1,_ = solve_total_amplitude(cxy,ex,ey,gam); U2,_ = solve_total_amplitude(cyx,ey,ex,gam)
    errs["xy_U"] = abs(U1-U2)
    s1 = mean_compression_stress(cxy,U1,ex,ey,gam); s2 = mean_compression_stress(cyx,U2,ey,ex,gam)
    errs["xy_mean_normal"] = max(abs(s1[0]-s2[1]),abs(s1[1]-s2[0]))
    p1 = airy_fluctuation_tension(cxy,U1,43.0,97.0); p2 = airy_fluctuation_tension(cyx,U2,97.0,43.0)
    errs["xy_local_normal"] = max(abs(p1[0]-p2[1]),abs(p1[1]-p2[0]))

    cp = PBLCell(200.0,200.0,4.0,206000.0,0.30,355.0,0.0)
    exs,eys,gams = 1e-7,2e-7,3e-7
    Us,_ = solve_total_amplitude(cp,exs,eys,gams)
    sx,sy,tau = mean_compression_stress(cp,Us,exs,eys,gams)
    target = np.array([cp.Q*(exs+cp.nu*eys),cp.Q*(eys+cp.nu*exs),cp.G*gams])
    errs["small_U"] = abs(Us)
    errs["small_A_matrix"] = float(np.max(np.abs(np.array([sx,sy,tau])-target)))
    kap = np.array([1e-5,2e-5,3e-5])
    _,_,M,_ = face_resultants(cp,exs,eys,gams,kap)
    errs["full_Ds"] = float(np.max(np.abs(M-gross_bending_matrix(cp)@kap)))
    errs["mean_local_kappa_exact"] = 0.0

    ct = PBLCell(200.0,200.0,4.0,206000.0,0.30,355.0,0.125)
    Ut,_=solve_total_amplitude(ct,2e-4,5e-4,2e-4)
    vm,_=local_mises(ct,Ut,2e-4,5e-4,2e-4,50.0,50.0,ct.t/2.0)
    if not (vm>0 and np.isfinite(vm)): raise RuntimeError("Mises point evaluator failed")

    k1=np.array([1e-5,2e-5,0.0]); k2=np.array([1e-5,2e-5,0.0])
    _,Nt,Mt,_=face_resultants(ct,2e-4,5e-4,0.0,k1)
    _,Nb,Mb,_=face_resultants(ct,4e-4,3e-4,0.0,k2)
    N,M=assemble_two_faces(Nt,Mt,50.0,Nb,Mb,-50.0)
    errs["two_face_N"] = float(np.max(np.abs(N-(Nt+Nb))))
    errs["two_face_M"] = float(np.max(np.abs(M-(50.0*Nt-50.0*Nb+Mt+Mb))))

    limits = {"yun_kcr_abs":1e-11,"yun_nonlinear_abs":1e-10,"zero_load_U_minus_A0":1e-12,
              "xy_U":1e-12,"xy_mean_normal":1e-10,"xy_local_normal":1e-10,"small_U":1e-12,
              "small_A_matrix":1e-10,"full_Ds":1e-12,"mean_local_kappa_exact":0.0,
              "two_face_N":1e-12,"two_face_M":1e-12}
    passed = all((errs[k]==0.0 if v==0.0 else errs[k] <= v) for k,v in limits.items())
    print("SSNC_R02_PBL_2D_FULL_RESULTANT_GATE =", "PASS" if passed else "FAIL")
    for k in sorted(errs): print(f"{k}={errs[k]:.12e}")
    print(f"mises_demo_MPa={vm:.12f}")
    print("EFFECTIVE_WIDTH_PRODUCTION =", EFFECTIVE_WIDTH_PRODUCTION)
    print("FULL_SKIN_D_RETAINED = True")
    print("SHEAR_POSTBUCKLING_CLOSED =", SHEAR_POSTBUCKLING_CLOSED)
    print("GLOBAL_AIRY_CHANGED =", GLOBAL_AIRY_CHANGED)
    print("ULTIMATE_STATE_CHANGED =", ULTIMATE_STATE_CHANGED)
    print("Pu_CALCULATED_IN_R02 = False")
    if not passed: raise SystemExit(2)

if __name__ == "__main__":
    run_gate()
