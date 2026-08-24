from __future__ import annotations
from dataclasses import dataclass
from math import pi, sqrt, cos, acos, copysign
import numpy as np

# SSNC-R03
# Scope: pre-first-yield elastic-material PBL postbuckling current tangent/resultant operator.
# Global Marguerre-Airy structure and the fixed global ultimate-state criterion remain unchanged.
# No effective width/area reduction is used.
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH_PRODUCTION = False
GLOBAL_AIRY_CHANGED = False
ULTIMATE_STATE_CHANGED = False
Pu_CALCULATED_IN_R03 = False
ELASTIC_POSTBUCKLING_CURRENT_TANGENT_CLOSED = True
POST_FIRST_YIELD_2D_PLASTIC_TANGENT_CLOSED = False
SHEAR_POSTBUCKLING_CLOSED = False


def _kp_num(r: float) -> float:
    return (272*r**16 + 2856*r**14 + 11273*r**12 + 23146*r**10
            + 31506*r**8 + 23146*r**6 + 11273*r**4 + 2856*r**2 + 272)


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
    def kx(self) -> float:
        return 2.0*pi/self.Lx

    @property
    def ky(self) -> float:
        return 2.0*pi/self.Ly

    @property
    def Q(self) -> float:
        return self.E/(1.0-self.nu**2)

    @property
    def G(self) -> float:
        return self.E/(2.0*(1.0+self.nu))

    @property
    def D(self) -> float:
        return self.E*self.t**3/(12.0*(1.0-self.nu**2))

    @property
    def cx(self) -> float:
        return 3.0*self.kx**2/8.0

    @property
    def cy(self) -> float:
        return 3.0*self.ky**2/8.0

    @property
    def Kb(self) -> float:
        return self.D*(0.75*(self.kx**4+self.ky**4) + 0.5*self.kx**2*self.ky**2)

    @property
    def KA(self) -> float:
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


def amplitude_coefficients(cell: PBLCell, ex: float, ey: float):
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


def mean_compression_stress(cell: PBLCell, U: float, ex: float, ey: float, gamma: float):
    """Full-area mean membrane stresses; normal compression is positive."""
    Delta = U*U-cell.A0**2
    mx = ex-cell.cx*Delta
    my = ey-cell.cy*Delta
    return np.array([
        cell.Q*(mx+cell.nu*my),
        cell.Q*(my+cell.nu*mx),
        cell.G*gamma,
    ], dtype=float)


def elastic_membrane_matrix(cell: PBLCell):
    return cell.t*np.array([
        [cell.Q, cell.nu*cell.Q, 0.0],
        [cell.nu*cell.Q, cell.Q, 0.0],
        [0.0, 0.0, cell.G],
    ], dtype=float)


def gross_bending_matrix(cell: PBLCell):
    D = cell.D
    return np.array([
        [D, cell.nu*D, 0.0],
        [cell.nu*D, D, 0.0],
        [0.0, 0.0, 0.5*(1.0-cell.nu)*D],
    ], dtype=float)


def amplitude_tangent_data(cell: PBLCell, U: float, ex: float, ey: float):
    """Exact Hessian data at the selected smooth stationary amplitude root."""
    B3, B1, _ = amplitude_coefficients(cell, ex, ey)
    kUU = 3.0*B3*U*U+B1
    h = -2.0*cell.t*cell.Q*U*np.array([
        cell.cx+cell.nu*cell.cy,
        cell.cy+cell.nu*cell.cx,
        0.0,
    ])
    if kUU <= 1e-12:
        raise RuntimeError(f"Selected amplitude root is not a stable smooth minimum: Pi_UU={kUU}")
    dU_de = -h/kUU
    return kUU, h, dU_de


def condensed_membrane_tangent(cell: PBLCell, U: float, ex: float, ey: float):
    """
    Exact pre-first-yield plate-level tangent after eliminating local amplitude U:

        A_pb = Pi_ee - Pi_eU * Pi_UU^{-1} * Pi_Ue.

    This is a Schur complement of the same R02 condensed potential, not an
    effective-width/effective-area reduction and not a change of the steel base E.
    """
    A0 = elastic_membrane_matrix(cell)
    if abs(U) <= 1e-15 and abs(cell.A0) <= 1e-15:
        return A0, np.inf, np.zeros(3), np.zeros(3)
    kUU, h, dU_de = amplitude_tangent_data(cell, U, ex, ey)
    A = A0-np.outer(h, h)/kUU
    return A, kUU, h, dU_de


def face_current_resultant_tangent(cell: PBLCell, e0, kappa, z: float):
    """
    One full steel face referred to the existing section reference surface.

    e_face = e0 + z*kappa
    N_face = N(e_face, U(e_face))
    M_face = z*N_face + D_skin*kappa

    Before first material yield, D_skin keeps the steel material E. Postbuckling
    loss of section bending stiffness enters exactly through z^2*A_pb.
    """
    e0 = np.asarray(e0, dtype=float)
    kappa = np.asarray(kappa, dtype=float)
    ef = e0+z*kappa
    U, roots = solve_total_amplitude(cell, ef[0], ef[1], ef[2])
    N = cell.t*mean_compression_stress(cell, U, *ef)
    Dskin = gross_bending_matrix(cell)
    M = z*N+Dskin@kappa
    A, kUU, h, dU_de = condensed_membrane_tangent(cell, U, ef[0], ef[1])
    K = np.block([
        [A, z*A],
        [z*A, z*z*A+Dskin],
    ])
    return {
        "U": U,
        "roots": roots,
        "face_strain": ef,
        "N": N,
        "M": M,
        "resultants": np.r_[N, M],
        "A": A,
        "Dskin": Dskin,
        "K": K,
        "Pi_UU": kUU,
        "h": h,
        "dU_de": dU_de,
    }


def two_face_current_operator(top: PBLCell, bottom: PBLCell, e0, kappa,
                              ztop: float, zbot: float):
    rt = face_current_resultant_tangent(top, e0, kappa, ztop)
    rb = face_current_resultant_tangent(bottom, e0, kappa, zbot)
    return {
        "top": rt,
        "bottom": rb,
        "resultants": rt["resultants"]+rb["resultants"],
        "K": rt["K"]+rb["K"],
    }


def reduced_y_uniaxial_solution(cell: PBLCell, ey: float):
    """
    Exact sigma_x=0 reduction of the same R02 PBL mode.

    Because R02 already proved the uniaxial kcr/kp identities with Yun, the
    derivative below is the tangent of that same Yun-coefficient-consistent
    reduced branch. It is a new derivative, not a claim that Yun published it.
    """
    B3 = 4.0*cell.t*cell.E*cell.KA+2.0*cell.t*cell.E*cell.cy**2
    B1 = cell.Kb-2.0*cell.t*cell.E*cell.cy*ey-B3*cell.A0**2
    B0 = -cell.Kb*cell.A0
    roots = cubic_real_roots(B3, B1, B0)
    admissible = [max(0.0, u) for u in roots if u >= -1e-11]
    if not admissible:
        raise RuntimeError("No uniaxial reduced root")

    def energy_red(U):
        Delta = U*U-cell.A0**2
        sy = cell.E*(ey-cell.cy*Delta)
        return (0.5*cell.Kb*(U-cell.A0)**2
                +cell.t*cell.E*cell.KA*Delta*Delta
                +0.5*cell.t*sy*sy/cell.E)

    U = min(admissible, key=energy_red)
    Delta = U*U-cell.A0**2
    ex = -cell.nu*ey+(cell.cx+cell.nu*cell.cy)*Delta
    sy = cell.E*(ey-cell.cy*Delta)

    if abs(U) <= 1e-15 and abs(cell.A0) <= 1e-15:
        Et = cell.E
    else:
        R_U = (cell.Kb
               +4.0*cell.t*cell.E*cell.KA*(3.0*U*U-cell.A0**2)
               -2.0*cell.t*cell.E*cell.cy
               *(ey-cell.cy*(3.0*U*U-cell.A0**2)))
        dU_dey = 2.0*cell.t*cell.E*cell.cy*U/R_U
        Et = cell.E*(1.0-2.0*cell.cy*U*dU_dey)
    return U, ex, sy, Et


def finite_difference_jacobian(fun, q, steps):
    q = np.asarray(q, dtype=float)
    f0 = np.asarray(fun(q), dtype=float)
    J = np.zeros((f0.size, q.size))
    for j, h in enumerate(steps):
        qp = q.copy(); qm = q.copy()
        qp[j] += h; qm[j] -= h
        J[:, j] = (np.asarray(fun(qp))-np.asarray(fun(qm)))/(2.0*h)
    return J


def run_gate():
    err = {}

    # 1. Exact pre-buckling degeneration to full elastic A and own-skin D.
    cp = PBLCell(200.0, 200.0, 4.0, 206000.0, 0.30, 355.0, 0.0)
    epre = np.array([1e-7, 2e-7, 3e-7])
    Upre, _ = solve_total_amplitude(cp, *epre)
    Apre, *_ = condensed_membrane_tangent(cp, Upre, epre[0], epre[1])
    rpre = face_current_resultant_tangent(cp, epre, np.zeros(3), 0.0)
    err["small_deflection_A_abs"] = float(np.max(np.abs(Apre-elastic_membrane_matrix(cp))))
    err["full_skin_D_preyield_abs"] = float(np.max(np.abs(rpre["Dskin"]-gross_bending_matrix(cp))))

    # 2. x<->y symmetry and actual postbuckling orthotropy/an\-isotropy.
    cxy = PBLCell(360.0, 240.0, 4.0, 206000.0, 0.30, 355.0, 0.0)
    cyx = PBLCell(240.0, 360.0, 4.0, 206000.0, 0.30, 355.0, 0.0)
    ex, ey = 0.0004625, 0.000925
    Uxy, _ = solve_total_amplitude(cxy, ex, ey)
    Uyx, _ = solve_total_amplitude(cyx, ey, ex)
    Axy, *_ = condensed_membrane_tangent(cxy, Uxy, ex, ey)
    Ayx, *_ = condensed_membrane_tangent(cyx, Uyx, ey, ex)
    P = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    err["xy_U_abs"] = abs(Uxy-Uyx)
    err["xy_A_abs"] = float(np.max(np.abs(Ayx-P@Axy@P.T)))
    err["postbuckling_anisotropy_ratio"] = float(
        abs(Axy[0, 0]-Axy[1, 1])/max(abs(Axy[0, 0]), abs(Axy[1, 1])))

    # 3. Exact A_pb versus derivative of full-area N.
    def Nofe(v):
        U, _ = solve_total_amplitude(cxy, v[0], v[1], v[2])
        return cxy.t*mean_compression_stress(cxy, U, *v)

    Jfd = finite_difference_jacobian(Nofe, np.array([ex, ey, 0.0]), [1e-9]*3)
    err["A_tangent_fd_rel"] = float(np.max(
        np.abs(Jfd-Axy)/np.maximum(1.0, np.abs(Axy))))

    # 4. Uniaxial stress-free transverse reduction: direct derivative equals
    #    Schur condensation of the biaxial A_pb.
    cu = PBLCell(360.0, 360.0, 4.0, 206000.0, 0.30, 355.0, 0.0)
    Uy, exy, sy, Et_direct = reduced_y_uniaxial_solution(cu, 0.0014)
    Ufull, _ = solve_total_amplitude(cu, exy, 0.0014, 0.0)
    Afull, *_ = condensed_membrane_tangent(cu, Ufull, exy, 0.0014)
    Et_cond = (Afull[1, 1]-Afull[1, 0]*Afull[0, 1]/Afull[0, 0])/cu.t
    err["uniaxial_U_abs"] = abs(Uy-Ufull)
    err["uniaxial_tangent_abs_MPa"] = abs(Et_direct-Et_cond)
    err["uniaxial_tangent_ratio_E"] = float(Et_cond/cu.E)
    err["uniaxial_mean_stress_MPa"] = float(sy)

    # 5. Two-face current 6x6 tangent and lever-arm bending degradation.
    z = 50.0
    e0 = np.array([ex, ey, 0.0])
    kap = np.zeros(3)
    two = two_face_current_operator(cxy, cxy, e0, kap, z, -z)
    K = two["K"]
    err["two_face_K_sym_abs"] = float(np.max(np.abs(K-K.T)))

    Ael = elastic_membrane_matrix(cxy)
    Dskin = gross_bending_matrix(cxy)
    Del = 2.0*z*z*Ael+2.0*Dskin
    Dcur = K[3:, 3:]
    err["Dx_current_over_elastic"] = float(Dcur[0, 0]/Del[0, 0])
    err["Dy_current_over_elastic"] = float(Dcur[1, 1]/Del[1, 1])

    # 6. Entire [N,M] 6x6 derivative versus finite difference.
    q = np.r_[e0, kap]

    def Rofq(v):
        return two_face_current_operator(cxy, cxy, v[:3], v[3:], z, -z)["resultants"]

    J6 = finite_difference_jacobian(
        Rofq, q, [1e-9, 1e-9, 1e-9, 1e-11, 1e-11, 1e-11])
    err["K6_fd_rel"] = float(np.max(
        np.abs(J6-K)/np.maximum(1.0, np.abs(K))))

    assert err["small_deflection_A_abs"] < 1e-9
    assert err["full_skin_D_preyield_abs"] < 1e-9
    assert err["xy_U_abs"] < 1e-11
    assert err["xy_A_abs"] < 1e-6
    assert err["postbuckling_anisotropy_ratio"] > 0.05
    assert err["A_tangent_fd_rel"] < 1e-6
    assert err["uniaxial_U_abs"] < 1e-11
    assert err["uniaxial_tangent_abs_MPa"] < 1e-7
    assert err["uniaxial_tangent_ratio_E"] < 0.999
    assert err["two_face_K_sym_abs"] < 1e-7
    assert err["Dx_current_over_elastic"] < 0.999
    assert err["Dy_current_over_elastic"] < 0.999
    assert err["K6_fd_rel"] < 1e-5

    print("SSNC_R03_CURRENT_6X6_TANGENT_GATE = PASS")
    print("ELASTIC_POSTBUCKLING_CURRENT_TANGENT = CLOSED")
    print("POST_FIRST_YIELD_2D_PLASTIC_TANGENT = OPEN")
    print("GLOBAL_AIRY_CHANGED = False")
    print("ULTIMATE_STATE_CHANGED = False")
    print("EFFECTIVE_WIDTH_PRODUCTION = False")
    print("Pu_CALCULATED_IN_R03 = False")
    for k, v in err.items():
        print(f"{k} = {v:.12e}")


if __name__ == "__main__":
    run_gate()
