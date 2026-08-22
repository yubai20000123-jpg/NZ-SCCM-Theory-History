"""Z6 TC-R1 direct endpoint calculation.

Purpose
-------
Finite s=0 post-crack continuation test for the project-defined NC TC-R1 map.
This is NOT a load-stepping algorithm and does not use spatial quadrature.

Formal objects:
- Marguerre-Airy Ppb(q), Nx(q), Ny(q) at s=0;
- NC T5 tension;
- Nguyen/MCFT current compression-softening reduction gamma(lambda_t);
- Saenz current softened compression branch;
- source-style bounded postcrush continuation;
- plane-stress steel face radial cap;
- longitudinal web elastic-perfectly-plastic clip.

The terminal event solved here is the web compression-yield complementarity kink.
The result is an endpoint candidate only; general-s final certification remains open.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.optimize import root

# Z6 frozen structural/material data
B = 12000.0
TC = 122.0
TS = 4.0
RHO_W = 0.02
FC = 30.4
E0 = 32500.0
EPS0 = 0.0018712490394580678
NU_C = 0.18
ES = 206000.0
FY = 355.0
NU_S = 0.30
Q0 = 0.004
PCR_MN = 39.2880147150
C_MN = 86071.5974582
G = 7.4692093263e6
KX = 6.876056916767441e6
RHO_T = 0.10
GAMMA2 = 10.0

P8 = np.array([
    0.0, 1.0, -1.75097804029, 1.13048200179, -0.0846335376902,
    -0.0337140826189, 0.00762023069439, -0.000634513017411,
    0.0000201154758756,
])
Q8 = np.array([
    1.0, -1.83488765925, 1.61630171237, -1.05371536507,
    0.738658387222, -0.206491596446, 0.0293277836449,
    -0.00217520309897, 0.0000670515862521,
])

KAPPA = E0 * EPS0 / FC
XCR = RHO_T / KAPPA


def poly_asc(a: np.ndarray, x: float) -> float:
    return float(sum(float(ai) * x**i for i, ai in enumerate(a)))


def t5(r: float) -> float:
    return poly_asc(P8, r) / poly_asc(Q8, r)


def softened_peak(lambda_t: float) -> tuple[float, float, float]:
    """Return gamma_c, signed sigma_cp, signed eps_cp."""
    gamma = min(1.0, 1.0 / (0.8 + 0.34 * max(lambda_t, 0.0)))
    sigp = -gamma * FC
    if gamma >= 1.0 - 1.0e-14:
        epsp = -EPS0 * (3.0 * gamma - 2.0)
    else:
        epsp = -EPS0 * (0.35*gamma + 2.25*gamma**2 - 1.6*gamma**3)
    elastic_limit = 2.0 * sigp / E0
    if epsp > elastic_limit:
        epsp = elastic_limit
    return gamma, sigp, epsp


def saenz(eps: float, epsp: float, sigp: float) -> float:
    esp = sigp / epsp
    rr = eps / epsp
    den = 1.0 + (E0 / esp - 2.0) * rr + rr * rr
    return E0 * eps / den


def postcrush(eps: float, epsp: float, sigp: float) -> float:
    if abs(eps) < abs(GAMMA2 * epsp):
        return sigp - 0.9 * sigp * (eps - epsp) / (epsp * (GAMMA2 - 1.0))
    return 0.1 * sigp


def concrete_tc(lambda_t: float, lambda_c: float) -> tuple[float, float, float]:
    sig_t = RHO_T * FC * t5(lambda_t / XCR)
    gamma, sigp, epsp = softened_peak(lambda_t)
    epsc = EPS0 * lambda_c
    if abs(epsc) <= abs(epsp):
        sig_c = saenz(epsc, epsp, sigp)
    else:
        sig_c = postcrush(epsc, epsp, sigp)
    return sig_t, sig_c, gamma


def steel_face(ex: float, ey: float) -> tuple[float, float, float, float]:
    fac = ES / (1.0 - NU_S**2)
    sx = fac * (ex + NU_S * ey)
    sy = fac * (ey + NU_S * ex)
    vm = math.sqrt(sx*sx - sx*sy + sy*sy)
    scale = 1.0 if vm <= FY else FY / vm
    return scale*sx, scale*sy, vm, scale


def ppb_mn(q: float) -> float:
    return PCR_MN * q / (q + Q0) + C_MN * q * (q + 2.0 * Q0)


def normal_residual(lambda_t: float, lambda_c: float, q: float, web_mode: str) -> np.ndarray:
    ex = EPS0 * (lambda_t - NU_C * lambda_c)
    ey = EPS0 * (lambda_c - NU_C * lambda_t)
    sx_c, sy_c, _ = concrete_tc(lambda_t, lambda_c)
    sx_s, sy_s, _, _ = steel_face(ex, ey)
    if web_mode == "elastic":
        sy_w = ES * ey
    elif web_mode == "cap":
        sy_w = -FY
    else:
        raise ValueError(web_mode)

    nx = (1.0-RHO_W)*TC*sx_c + 2.0*TS*sx_s
    ny = (1.0-RHO_W)*TC*sy_c + 2.0*TS*sy_s + RHO_W*TC*sy_w
    qq = q*(q + 2.0*Q0)
    nx_d = KX * qq
    ny_d = -(ppb_mn(q)*1.0e6/B + G*qq)
    return np.array([nx-nx_d, ny-ny_d], dtype=float)


def endpoint_residual(z: np.ndarray) -> np.ndarray:
    lt, lc, q = map(float, z)
    ex = EPS0 * (lt - NU_C*lc)
    ey = EPS0 * (lc - NU_C*lt)
    r = normal_residual(lt, lc, q, "cap")
    return np.array([r[0], r[1], ES*ey + FY], dtype=float)


def jacobian_2(fun, x: np.ndarray, rel: float = 1.0e-6) -> np.ndarray:
    f0 = np.asarray(fun(x), dtype=float)
    out = np.zeros((len(f0), len(x)), dtype=float)
    for j in range(len(x)):
        h = rel * max(1.0, abs(float(x[j])))
        xp = x.copy(); xm = x.copy()
        xp[j] += h; xm[j] -= h
        out[:,j] = (np.asarray(fun(xp))-np.asarray(fun(xm))) / (2.0*h)
    return out


def branch_direction(lt: float, lc: float, q: float, web_mode: str) -> tuple[float, float]:
    lam = np.array([lt, lc], dtype=float)
    J = jacobian_2(lambda L: normal_residual(float(L[0]), float(L[1]), q, web_mode), lam)
    hq = 1.0e-7
    dR_dq = (normal_residual(lt, lc, q+hq, web_mode)
             - normal_residual(lt, lc, q-hq, web_mode)) / (2.0*hq)
    dlam_dq = -np.linalg.solve(J, dR_dq)
    grad_yield = np.array([-ES*EPS0*NU_C, ES*EPS0], dtype=float)
    dh_dq = float(grad_yield @ dlam_dq)
    return float(np.linalg.det(J)), dh_dq


def main() -> None:
    sol = root(endpoint_residual, np.array([0.725, -0.790, 0.01203]), tol=1.0e-12)
    if not sol.success:
        raise RuntimeError(sol.message)
    lt, lc, q = map(float, sol.x)
    ex = EPS0*(lt-NU_C*lc)
    ey = EPS0*(lc-NU_C*lt)
    sx_c, sy_c, gamma = concrete_tc(lt, lc)
    sx_s, sy_s, vm, scale = steel_face(ex, ey)
    nx_res = normal_residual(lt, lc, q, "cap")
    det_el, dh_el = branch_direction(lt, lc, q, "elastic")
    det_cap, dh_cap = branch_direction(lt, lc, q, "cap")

    print("Z6 TC-R1 s=0 direct endpoint candidate")
    print(f"lambda_t = {lt:.15g}")
    print(f"lambda_c = {lc:.15g}")
    print(f"q = {q:.15g}")
    print(f"P = {ppb_mn(q):.12f} MN")
    print(f"gamma_c = {gamma:.12f}")
    print(f"concrete sx,sy = {sx_c:.9f}, {sy_c:.9f} MPa")
    print(f"steel face sx,sy = {sx_s:.9f}, {sy_s:.9f} MPa")
    print(f"steel trial VM = {vm:.9f} MPa; radial scale = {scale:.12f}")
    print(f"web ey = {ey:.15g}; web sy = {-FY:.9f} MPa")
    print(f"equilibrium residual = {nx_res}")
    print(f"elastic-web det = {det_el:.9e}; d(yield)/dq = {dh_el:.9e}")
    print(f"capped-web  det = {det_cap:.9e}; d(yield)/dq = {dh_cap:.9e}")
    print("Interpretation: elastic branch reaches the web-yield surface as q increases,")
    print("while the capped continuation points immediately back across that surface.")
    print("This is a terminal complementarity kink for the s=0 finite system.")
    print("GENERAL-s FORMAL CERTIFICATE REMAINS OPEN; do not label this final Z6 Pu.")


if __name__ == "__main__":
    main()
