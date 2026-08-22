"""NZ-SCCM Z6 TC-R2 direct finite solver.

Formal scope
------------
This file contains NO spatial/thickness quadrature, NO material points, NO load
steps and NO history state machine. It solves two finite uniform-section roots:

1. exactly symmetric s=0 TC-R2 endpoint at longitudinal-web compression yield;
2. the s->0+ asymmetric second-face-yield limit, where curvature tends to zero,
   the web is still elastic and the two face elastic trials are exactly at von-Mises
   yield.

Neither root uses Zhou, Winter, FEM or experiment values.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.optimize import root

# Frozen Z6 data
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
ALPHA1 = 10.0
ALPHA2 = 0.30
GAMMA2 = 10.0

KAPPA = E0 * EPS0 / FC
XCR = RHO_T / KAPPA


def ppb_mn(q: float) -> float:
    return PCR_MN * q / (q + Q0) + C_MN * q * (q + 2.0 * Q0)


def foster_tension(lambda_t: float) -> float:
    """Finite Foster/Nguyen project tension law used by TC-R2."""
    r = lambda_t / XCR
    ft = RHO_T * FC
    if r <= 1.0:
        return ft * r
    if r < ALPHA1:
        gamma_t = ALPHA2 + (1.0 - ALPHA2) * (ALPHA1 - r) / (ALPHA1 - 1.0)
        return gamma_t * ft
    return ALPHA2 * ft


def base_compression(lambda_c: float) -> float:
    """Fixed-peak Saenz + bounded postpeak NC backbone."""
    eps = EPS0 * lambda_c
    epsp = -EPS0
    sigp = -FC
    if abs(eps) <= abs(epsp):
        esp = sigp / epsp
        r = eps / epsp
        den = 1.0 + (E0 / esp - 2.0) * r + r * r
        return E0 * eps / den
    if abs(eps) < GAMMA2 * abs(epsp):
        return sigp - 0.9 * sigp * (eps - epsp) / (epsp * (GAMMA2 - 1.0))
    return 0.1 * sigp


def gamma_soft(lambda_t: float) -> float:
    return min(1.0, 1.0 / (0.8 + 0.34 * max(lambda_t, 0.0)))


def concrete_tc_r2(lambda_t: float, lambda_c: float) -> tuple[float, float, float]:
    sx = foster_tension(lambda_t)
    gamma = gamma_soft(lambda_t)
    sy = gamma * base_compression(lambda_c)
    return sx, sy, gamma


def steel_trial(ex: float, ey: float) -> tuple[float, float, float]:
    fac = ES / (1.0 - NU_S**2)
    sx = fac * (ex + NU_S * ey)
    sy = fac * (ey + NU_S * ex)
    vm = math.sqrt(sx * sx - sx * sy + sy * sy)
    return sx, sy, vm


def steel_radial_cap(ex: float, ey: float) -> tuple[float, float, float, float]:
    sx, sy, vm = steel_trial(ex, ey)
    scale = 1.0 if vm <= FY else FY / vm
    return scale * sx, scale * sy, vm, scale


def physical_strain(lambda_t: float, lambda_c: float) -> tuple[float, float]:
    ex = EPS0 * (lambda_t - NU_C * lambda_c)
    ey = EPS0 * (lambda_c - NU_C * lambda_t)
    return ex, ey


def demands(q: float) -> tuple[float, float]:
    qq = q * (q + 2.0 * Q0)
    nx = KX * qq
    ny = -(ppb_mn(q) * 1.0e6 / B + G * qq)
    return nx, ny


def symmetric_web_yield_residual(z: np.ndarray) -> np.ndarray:
    """s=0: both faces use current radial cap; web at compression yield."""
    lt, lc, q = map(float, z)
    ex, ey = physical_strain(lt, lc)
    sx_c, sy_c, _ = concrete_tc_r2(lt, lc)
    sx_s, sy_s, _, _ = steel_radial_cap(ex, ey)
    sy_w = -FY

    nx = (1.0 - RHO_W) * TC * sx_c + 2.0 * TS * sx_s
    ny = ((1.0 - RHO_W) * TC * sy_c
          + 2.0 * TS * sy_s
          + RHO_W * TC * sy_w)
    nxd, nyd = demands(q)
    return np.array([nx - nxd, ny - nyd, ES * ey + FY], dtype=float)


def s0plus_face_yield_limit_residual(z: np.ndarray) -> np.ndarray:
    """s->0+: uniform limiting state, web elastic, faces just reach VM yield."""
    lt, lc, q = map(float, z)
    ex, ey = physical_strain(lt, lc)
    sx_c, sy_c, _ = concrete_tc_r2(lt, lc)
    sx_s, sy_s, vm = steel_trial(ex, ey)  # scale=1 exactly at event
    sy_w = ES * ey

    nx = (1.0 - RHO_W) * TC * sx_c + 2.0 * TS * sx_s
    ny = ((1.0 - RHO_W) * TC * sy_c
          + 2.0 * TS * sy_s
          + RHO_W * TC * sy_w)
    nxd, nyd = demands(q)
    return np.array([nx - nxd, ny - nyd, vm - FY], dtype=float)


def solve() -> None:
    s0 = root(symmetric_web_yield_residual,
              np.array([0.724, -0.791, 0.01202]), tol=1.0e-12)
    if not s0.success:
        raise RuntimeError(f"s=0 root failed: {s0.message}")

    lim = root(s0plus_face_yield_limit_residual,
               np.array([0.5364, -0.6330, 0.01164]), tol=1.0e-12)
    if not lim.success:
        raise RuntimeError(f"s->0+ limit root failed: {lim.message}")

    lt0, lc0, q0 = map(float, s0.x)
    ex0, ey0 = physical_strain(lt0, lc0)
    sxc0, syc0, gam0 = concrete_tc_r2(lt0, lc0)
    sxs0, sys0, vm0, sc0 = steel_radial_cap(ex0, ey0)

    ltl, lcl, ql = map(float, lim.x)
    exl, eyl = physical_strain(ltl, lcl)
    sxsl, sysl, vml = steel_trial(exl, eyl)

    print("Z6 TC-R2 direct finite roots")
    print("formal spatial/thickness quadrature = 0")
    print("material points/load steps/history = 0")
    print()
    print("[A] symmetric s=0 web-yield endpoint")
    print(f"lambda_t = {lt0:.12f}")
    print(f"lambda_c = {lc0:.12f}")
    print(f"q = {q0:.12f}")
    print(f"P = {ppb_mn(q0):.12f} MN")
    print(f"gamma_c = {gam0:.12f}")
    print(f"concrete sx,sy = {sxc0:.9f}, {syc0:.9f} MPa")
    print(f"face sx,sy = {sxs0:.9f}, {sys0:.9f} MPa")
    print(f"face trial VM = {vm0:.9f} MPa; radial scale = {sc0:.12f}")
    print(f"web ey = {ey0:.15g}; web sy = {-FY:.9f} MPa")
    print(f"residual_inf = {np.max(np.abs(symmetric_web_yield_residual(s0.x))):.3e}")
    print()
    print("[B] asymmetric s->0+ second-face-yield limit")
    print(f"lambda_t = {ltl:.12f}")
    print(f"lambda_c = {lcl:.12f}")
    print(f"q = {ql:.12f}")
    print(f"P = {ppb_mn(ql):.12f} MN")
    print(f"face elastic trial sx,sy = {sxsl:.9f}, {sysl:.9f} MPa")
    print(f"face elastic trial VM = {vml:.12f} MPa")
    print(f"web elastic sy = {ES * eyl:.9f} MPa")
    print(f"residual_inf = {np.max(np.abs(s0plus_face_yield_limit_residual(lim.x))):.3e}")
    print()
    print("IMPORTANT: A and B are direct endpoint/local-limit candidates.")
    print("The full global minimum over 0<s<=1 is not certified by this file.")


if __name__ == "__main__":
    solve()
