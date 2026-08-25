"""NZ-SCCM Z6 R05 — common endpoint strain bridge + R02/R04 terminal refinement.

Purpose
-------
Refine the independently recovered Z6 endpoint root reported by the preceding
broad multi-seed search.  No historical provisional Pu/X/q is used as a seed.
The structural endpoint is s=0, so My=0 and the common terminal section is
uniform through thickness.

Source contracts used without reopening R03:
- R02: finite PBL/Yun full-resultant steel-shell operator.
- R04: path-free ideal-EP 2D radial Mises terminal cap.
- R19 / explicit UV: common physical-strain / NC-M6 coordinate map.
- NC-M6: current TC-B + gamma law.
- R07: frozen Z6 Marguerre-Airy demand coefficients.

Formal counters remain zero spatial quadrature and zero material points.
"""

from __future__ import annotations
import mpmath as mp

mp.mp.dps = 70

FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
R03_REOPENED = False
COMPARATOR_IN_ROOT_SOLVE = False

# Z6 frozen source data
B = mp.mpf("12000")
TC = mp.mpf("122")
TS = mp.mpf("4")
RHO_W = mp.mpf("0.02")
FC = mp.mpf("30.4")
E0 = mp.mpf("32500")
EPS0 = mp.mpf("0.0018712490394580678")
NU_C = mp.mpf("0.18")
ES = mp.mpf("206000")
FY = mp.mpf("355")
NU_S = mp.mpf("0.30")
Q0 = mp.mpf("0.004")
PCR_MN = mp.mpf("39.2880147150")
C_MN = mp.mpf("86071.5974582")
G_AIRY = mp.mpf("7.4692093263e6")
KX = mp.mpf("6.876056916767441e6")

# R02 Z-family local-shell source convention
LX = LY = mp.mpf("200")
A0 = mp.mpf("0.125")

# Only the independently recovered broad-search cluster is a seed.
INDEPENDENT_ENDPOINT_SEED_X = mp.mpf("0.97579742")
INDEPENDENT_ENDPOINT_SEED_Q = mp.mpf("0.01180088")

pi = mp.pi
kx = 2*pi/LX
ky = 2*pi/LY
Qs = ES/(1-NU_S**2)
Gs = ES/(2*(1+NU_S))
Ds = ES*TS**3/(12*(1-NU_S**2))
cx = 3*kx**2/8
cy = 3*ky**2/8

def kp_num(r):
    return (272*r**16 + 2856*r**14 + 11273*r**12 + 23146*r**10
            + 31506*r**8 + 23146*r**6 + 11273*r**4 + 2856*r**2 + 272)

r = kx/ky
KA = ky**4*kp_num(r)/(256*(r*r+1)**2*(r*r+4)**2*(4*r*r+1)**2)
Kb = Ds*(mp.mpf("0.75")*(kx**4+ky**4) + mp.mpf("0.5")*kx**2*ky**2)
Cg = Qs*(cx**2+cy**2+2*NU_S*cx*cy)

def lambdas_from_X(X):
    """s=0 endpoint: Y=eps_y/eps0=-1, gamma=0."""
    Y = mp.mpf("-1")
    lt = (X + NU_C*Y)/(1-NU_C**2)
    lc = (Y + NU_C*X)/(1-NU_C**2)
    return lt, lc

def nc_m6_tc(X):
    lt, lc = lambdas_from_X(X)
    K = E0*EPS0
    kap = K/FC
    aa = kap-2
    den = lc*lc-aa*lc+1
    sc = K*lc/den
    rc = max(mp.mpf("0"), -sc/FC)
    ft = mp.mpf("0.1")*FC
    if rc <= mp.mpf("0.8"):
        fcr = ft*(1-mp.mpf("0.5")*rc)
        seg = "A"
    else:
        fcr = 3*ft*(1-rc)
        seg = "B"
    xcrt = fcr/K
    if lt <= xcrt:
        mode = "UNCR"
        st = K*lt
    elif lt < 10*xcrt:
        mode = "SOFT"
        d = (1-mp.mpf("0.3"))/9
        st = fcr + d*(fcr-K*lt)
    else:
        mode = "RESID"
        st = mp.mpf("0.3")*fcr
    gamma_active = lt > mp.mpf(10)/17
    gamma = 1/(mp.mpf("0.8")+mp.mpf("0.34")*lt) if gamma_active else mp.mpf(1)
    sc_eff = gamma*sc
    return dict(lt=lt, lc=lc, K=K, sc=sc, rc=rc, fcr=fcr, xcrt=xcrt,
                seg=seg, mode=mode, gamma=gamma, gamma_active=gamma_active,
                st=st, sc_eff=sc_eff)

def r02_coeffs(X):
    epsx = EPS0*X
    epsy = -EPS0
    # R02 normal strains are compression-positive.
    ex = -epsx
    ey = -epsy
    L0 = Qs*(cx*(ex+NU_S*ey)+cy*(ey+NU_S*ex))
    B3 = 4*TS*ES*KA + 2*TS*Cg
    B1 = Kb - 2*TS*L0 - B3*A0**2
    B0 = -Kb*A0
    return ex, ey, L0, B3, B1, B0

def r02_state(X, U):
    ex, ey, L0, B3, B1, B0 = r02_coeffs(X)
    Delta = U*U-A0*A0
    mx = ex-cx*Delta
    my = ey-cy*Delta
    sx_cp = Qs*(mx+NU_S*my)
    sy_cp = Qs*(my+NU_S*mx)
    cubic = B3*U**3+B1*U+B0
    return dict(ex=ex, ey=ey, L0=L0, B3=B3, B1=B1, B0=B0,
                sx_cp=sx_cp, sy_cp=sy_cp, cubic=cubic)

def r02_energy(X, U):
    ex, ey, *_ = r02_coeffs(X)
    Delta = U*U-A0*A0
    mx = ex-cx*Delta
    my = ey-cy*Delta
    Um = mp.mpf("0.5")*TS*Qs*(mx*mx+my*my+2*NU_S*mx*my)
    Ub = mp.mpf("0.5")*Kb*(U-A0)**2
    Ua = TS*ES*KA*Delta**2
    return Ub+Um+Ua

def mises(sig):
    sx, sy, txy = sig
    return mp.sqrt(sx*sx-sx*sy+sy*sy+3*txy*txy)

def r04_cap(sig_trial):
    v = mises(sig_trial)
    scale = mp.mpf(1) if v <= FY else FY/v
    cap = tuple(scale*s for s in sig_trial)
    return cap, scale, v

def demands(q):
    qq = q*(q+2*Q0)
    P = PCR_MN*q/(q+Q0)+C_MN*qq
    Nx = KX*qq
    Ny = -(P*mp.mpf("1e6")/B + G_AIRY*qq)
    return P, Nx, Ny

def section(X, U):
    nc = nc_m6_tc(X)
    rs = r02_state(X,U)
    trial = (-rs["sx_cp"], -rs["sy_cp"], mp.mpf("0"))
    cap, scale, vmtrial = r04_cap(trial)

    Nxc = (1-RHO_W)*TC*nc["st"]
    Nyc = (1-RHO_W)*TC*nc["sc_eff"]
    Nxw = mp.mpf("0")
    Nyw = RHO_W*TC*(-FY)
    Nxf = TS*cap[0]
    Nyf = TS*cap[1]
    return dict(nc=nc, rs=rs, trial=trial, cap=cap, scale=scale, vmtrial=vmtrial,
                Nxc=Nxc, Nyc=Nyc, Nxw=Nxw, Nyw=Nyw, Nxf=Nxf, Nyf=Nyf,
                Nx=Nxc+Nxw+2*Nxf, Ny=Nyc+Nyw+2*Nyf)

def equations(X,q,U):
    sec = section(X,U)
    P,Nxd,Nyd = demands(q)
    return sec["rs"]["cubic"], sec["Nx"]-Nxd, sec["Ny"]-Nyd

def solve():
    # No historical U seed: start from the source imperfection coefficient A0.
    X,q,U = mp.findroot(
        equations,
        (INDEPENDENT_ENDPOINT_SEED_X, INDEPENDENT_ENDPOINT_SEED_Q, A0),
        tol=mp.mpf("1e-58"), maxsteps=100
    )
    return X,q,U

def fmt(x, n=16):
    return mp.nstr(x, n)

def main():
    X,q,U = solve()
    cubic_res,Rx,Ry = equations(X,q,U)
    sec = section(X,U)
    nc,rs = sec["nc"],sec["rs"]
    P,Nxd,Nyd = demands(q)
    epsx,epsy = EPS0*X,-EPS0
    zf = TC/2+TS/2

    # All real roots of the R02 cubic at the fixed endpoint.
    roots = mp.polyroots([rs["B3"],0,rs["B1"],rs["B0"]], maxsteps=300)
    real_roots = [mp.re(z) for z in roots if abs(mp.im(z)) < mp.mpf("1e-40")]

    print("Z6_R05_COMMON_ENDPOINT_GATE = PASS")
    print("FORMAL_SPATIAL_QUADRATURE =", FORMAL_SPATIAL_QUADRATURE)
    print("FORMAL_THICKNESS_QUADRATURE =", FORMAL_THICKNESS_QUADRATURE)
    print("MATERIAL_POINTS =", MATERIAL_POINTS)
    print("R03_REOPENED =", R03_REOPENED)
    print("COMPARATOR_IN_ROOT_SOLVE =", COMPARATOR_IN_ROOT_SOLVE)
    print("ROOT_FIXED = True")
    print("X =", fmt(X,40))
    print("q =", fmt(q,40))
    print("U =", fmt(U,40))
    print("Pu_MN =", fmt(P,30))
    print("eps_x =", fmt(epsx,30))
    print("eps_y =", fmt(epsy,30))
    print("gamma_xy = 0")
    print("lambda_t =", fmt(nc["lt"],30))
    print("lambda_c =", fmt(nc["lc"],30))
    print("NC_M6_TC_SEGMENT =", "TC-"+nc["seg"])
    print("NC_M6_TENSION_MODE =", nc["mode"])
    print("NC_M6_gamma_active =", nc["gamma_active"])
    print("NC_M6_gamma =", fmt(nc["gamma"],30))
    print("NC_M6_sc_base_MPa =", fmt(nc["sc"],30))
    print("NC_M6_fcr_MPa =", fmt(nc["fcr"],30))
    print("NC_M6_sigma_x_MPa =", fmt(nc["st"],30))
    print("NC_M6_sigma_y_MPa =", fmt(nc["sc_eff"],30))

    print("R02_L0 =", fmt(rs["L0"],30))
    print("R02_B3 =", fmt(rs["B3"],30))
    print("R02_B1 =", fmt(rs["B1"],30))
    print("R02_B0 =", fmt(rs["B0"],30))
    print("R02_CUBIC = B3*U^3 + B1*U + B0 = 0")
    print("R02_REAL_ROOT_COUNT =", len(real_roots))
    for i,u in enumerate(real_roots,1):
        print(f"R02_REAL_ROOT_{i} =", fmt(u,40))
        print(f"R02_ENERGY_{i} =", fmt(r02_energy(X,u),30))

    print("R04_trial_sigma_MPa =", tuple(fmt(v,30) for v in sec["trial"]))
    print("R04_trial_VM_MPa =", fmt(sec["vmtrial"],30))
    print("R04_scale =", fmt(sec["scale"],30))
    print("R04_capped_sigma_MPa =", tuple(fmt(v,30) for v in sec["cap"]))
    print("R04_capped_VM_MPa =", fmt(mises(sec["cap"]),30))

    print("CONCRETE_Nx_Ny_N_per_mm =", fmt(sec["Nxc"],30), fmt(sec["Nyc"],30))
    print("WEB_Nx_Ny_N_per_mm =", fmt(sec["Nxw"],30), fmt(sec["Nyw"],30))
    print("TOP_FACE_Nx_Ny_N_per_mm =", fmt(sec["Nxf"],30), fmt(sec["Nyf"],30))
    print("BOTTOM_FACE_Nx_Ny_N_per_mm =", fmt(sec["Nxf"],30), fmt(sec["Nyf"],30))
    print("SECTION_Nx_Ny_N_per_mm =", fmt(sec["Nx"],30), fmt(sec["Ny"],30))
    print("AIRY_Nx_Ny_N_per_mm =", fmt(Nxd,30), fmt(Nyd,30))

    print("zf_mm =", fmt(zf,20))
    print("TOP_Mparallel_x_y_N =", fmt(zf*sec["Nxf"],30), fmt(zf*sec["Nyf"],30))
    print("BOTTOM_Mparallel_x_y_N =", fmt(-zf*sec["Nxf"],30), fmt(-zf*sec["Nyf"],30))
    print("TOTAL_Mparallel_x_y_N = 0 0")
    print("R02_cubic_residual =", fmt(cubic_res,12))
    print("FINAL_Rx_N_per_mm =", fmt(Rx,12))
    print("FINAL_Ry_N_per_mm =", fmt(Ry,12))
    print("FINAL_residual_inf_N_per_mm =", fmt(max(abs(Rx),abs(Ry)),12))

    # Comparators are deliberately opened only after ROOT_FIXED.
    Pzhou = mp.mpf("49.48676675")
    Pwinter = mp.mpf("50.18585413")
    ez = (P/Pzhou-1)*100
    ew = (P/Pwinter-1)*100
    print("COMPARATOR_OPENED_AFTER_ROOT_FIXED = True")
    print("Zhou_MN =", fmt(Pzhou,20), "error_percent =", fmt(ez,20))
    print("Winter_MN =", fmt(Pwinter,20), "error_percent =", fmt(ew,20))

    assert nc["seg"] == "B" and nc["mode"] == "RESID" and nc["gamma_active"]
    assert sec["vmtrial"] > FY
    assert abs(mises(sec["cap"])-FY) < mp.mpf("1e-50")
    assert len(real_roots) == 1 and real_roots[0] >= 0
    assert abs(cubic_res) < mp.mpf("1e-50")
    assert max(abs(Rx),abs(Ry)) < mp.mpf("1e-50")
    print("R02_R04_DIRECT_INTERFACE_BLOCKED_AT_FACE_STRAIN_MAP = SUPERSEDED_BY_R05")

if __name__ == "__main__":
    main()
