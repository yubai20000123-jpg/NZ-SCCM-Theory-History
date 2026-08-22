"""NZ-SCCM Z0-Z6 finite NC-TC source-transition reproduction.

Identity
--------
- Structural backbone: frozen Marguerre-Airy explicit theory.
- NC axis current backbones: Saenz compression + T5 tension.
- 2D source boundary: Nguyen Eqs. (3.18)-(3.19) TC failure envelope.
- External steel faces: plane-stress elastic trial + von-Mises radial cap.
- Equivalent longitudinal web: y-only elastic-perfectly-plastic clip.
- Formal structural spatial sampling/quadrature: ZERO.
- Material points / load path / history state machine: ZERO/OFF.

This script solves a finite 3-unknown algebraic system (lambda_x, lambda_y, q)
at the s=0 Airy endpoint. The returned values are SOURCE TRANSITION/CRACKING
loads, NOT final post-crack ultimate capacities.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Tuple

import numpy as np
from scipy.optimize import root


# -----------------------------------------------------------------------------
# Frozen common data
# -----------------------------------------------------------------------------
RHO_T = 0.10              # ft/fc project tensile input for Z family
NU_C = 0.18
NU_S = 0.30
E_S = 206000.0            # MPa
T_S = 4.0                 # mm / external face
RHO_W = 0.02
Q0 = 0.004

# T5(r) = P8/Q8; coefficients in ascending powers.
P8 = np.array([
    0.0,
    1.0,
    -1.75097804029,
    1.13048200179,
    -0.0846335376902,
    -0.0337140826189,
    0.00762023069439,
    -0.000634513017411,
    0.0000201154758756,
])

Q8 = np.array([
    1.0,
    -1.83488765925,
    1.61630171237,
    -1.05371536507,
    0.738658387222,
    -0.206491596446,
    0.0293277836449,
    -0.00217520309897,
    0.0000670515862521,
])


def polyval_ascending(a: np.ndarray, x: float) -> float:
    return float(sum(ai * x**i for i, ai in enumerate(a)))


def t5(r: float) -> float:
    return polyval_ascending(P8, r) / polyval_ascending(Q8, r)


def saenz(c: float, kappa: float) -> float:
    return kappa * c / (1.0 + (kappa - 2.0) * c + c * c)


@dataclass(frozen=True)
class Case:
    b: float
    tc: float
    Ec: float
    fc: float
    eps0: float
    fy: float
    Pcr_MN: float
    C_MN: float
    q_1D: float
    Pu_1D_MN: float


CASES: Dict[str, Case] = {
    "Z0": Case(6000., 122., 32500., 30.4, 0.0018712490394580678, 355., 78.30671, 43035.79873, 0.00342823, 37.82571),
    "Z1": Case(6000.,  92., 32500., 30.4, 0.0018712490394580678, 235., 40.35021, 35478.23714, 0.00499668, 24.71413),
    "Z2": Case(6000., 122., 32500., 30.4, 0.0018712490394580678, 460., 78.30671, 43035.79873, 0.00432177, 42.95901),
    "Z3": Case(6000., 122., 35992.801439712057, 45.6, 0.0025344898708809867, 355., 81.78821, 46121.44731, 0.00461430, 46.49489),
    "Z4": Case(8000., 192., 32500., 30.4, 0.0018712490394580678, 355., 179.75477, 80875.42965, 0.00244543, 70.26572),
    "Z5": Case(2000., 122., 32500., 30.4, 0.0018712490394580678, 355., 231.78841, 14345.26624, 0.000258842, 14.11819),
    "Z6": Case(12000.,122., 32500., 30.4, 0.0018712490394580678, 355., 39.2880147150, 86071.5974582, 0.0138074129378, 56.37942109),
}

# Deterministic material-coordinate seeds for the first origin-connected
# ascending-compression TC source transition. They are not load steps.
SEEDS: Dict[str, Tuple[str, float, float, float]] = {
    "Z0": ("B", 0.0310131, -0.4594515, 0.002007625),
    "Z1": ("B", 0.0345810, -0.3438529, 0.002653116),
    "Z2": ("B", 0.0310131, -0.4594515, 0.002007625),
    "Z3": ("B", 0.0317598, -0.4323697, 0.003023358),
    "Z4": ("A", 0.0259798, -0.5292564, 0.001755102),
    "Z5": ("A", 0.0226245, -0.5557318, 0.000194053),
    "Z6": ("B", 0.0400238, -0.2121687, 0.004014855),
}


def extensional_G_Kx(c: Case) -> Tuple[float, float]:
    A11 = ((1.0 - RHO_W) * c.tc * c.Ec / (1.0 - NU_C**2)
           + 2.0 * T_S * E_S / (1.0 - NU_S**2))
    A22 = A11 + RHO_W * c.tc * E_S
    A12 = ((1.0 - RHO_W) * c.tc * NU_C * c.Ec / (1.0 - NU_C**2)
           + 2.0 * T_S * NU_S * E_S / (1.0 - NU_S**2))
    delta_A = A11 * A22 - A12 * A12
    # current Z cases have alpha=beta=pi/b, hence alpha^2 b^2=beta^2 b^2=pi^2
    G = math.pi**2 * delta_A / (8.0 * A11)
    Kx = math.pi**2 * delta_A / (8.0 * A22)
    return G, Kx


def Ppb_MN(q: float, c: Case) -> float:
    return c.Pcr_MN * q / (q + Q0) + c.C_MN * q * (q + 2.0 * Q0)


def steel_face(ex: float, ey: float, fy: float) -> Tuple[float, float]:
    fac = E_S / (1.0 - NU_S**2)
    sx_tr = fac * (ex + NU_S * ey)
    sy_tr = fac * (ey + NU_S * ex)
    vm = math.sqrt(sx_tr*sx_tr - sx_tr*sy_tr + sy_tr*sy_tr)
    scale = 1.0 if vm <= fy else fy / vm
    return scale * sx_tr, scale * sy_tr


def section_state(lx: float, ly: float, c: Case) -> Tuple[float, float, float, float]:
    """Return Nx, Ny, p/fc, t/ft for a TC state."""
    kappa = c.Ec * c.eps0 / c.fc
    xcr = RHO_T / kappa

    # Current axis backbones. No historical c*(1-tau) cross-softening is used.
    sx_c = RHO_T * c.fc * t5(lx / xcr)
    sy_c = -c.fc * saenz(-ly, kappa)

    # Bonded physical strains shared by concrete and steel faces/web.
    ex = c.eps0 * (lx - NU_C * ly)
    ey = c.eps0 * (ly - NU_C * lx)

    sx_s, sy_s = steel_face(ex, ey, c.fy)
    sy_w = float(np.clip(E_S * ey, -c.fy, c.fy))

    Nx = (1.0 - RHO_W) * c.tc * sx_c + 2.0 * T_S * sx_s
    Ny = ((1.0 - RHO_W) * c.tc * sy_c
          + 2.0 * T_S * sy_s
          + RHO_W * c.tc * sy_w)

    return Nx, Ny, (-sy_c / c.fc), (sx_c / (RHO_T * c.fc))


def residual(z: np.ndarray, c: Case, segment: str) -> np.ndarray:
    lx, ly, q = map(float, z)
    Nx, Ny, pfc, tft = section_state(lx, ly, c)
    G, Kx = extensional_G_Kx(c)
    Q = q * (q + 2.0 * Q0)

    Nx_d = Kx * Q
    Ny_d = -(Ppb_MN(q, c) * 1.0e6 / c.b + G * Q)

    if segment == "A":
        gate = pfc + tft / 3.0 - 1.0
    elif segment == "B":
        gate = pfc / 2.0 + tft - 1.0
    else:
        raise ValueError(segment)

    return np.array([Nx - Nx_d, Ny - Ny_d, gate], dtype=float)


def solve_transition(name: str) -> dict:
    c = CASES[name]
    segment, lx0, ly0, q0 = SEEDS[name]
    sol = root(lambda z: residual(z, c, segment), np.array([lx0, ly0, q0]), tol=1e-12)
    if not sol.success:
        raise RuntimeError(f"{name}: nonlinear root failed: {sol.message}")

    lx, ly, q = map(float, sol.x)
    Nx, Ny, pfc, tft = section_state(lx, ly, c)

    # Source-branch and origin-connected ascending-compression checks.
    if not (lx >= 0.0 and ly < 0.0 and -ly <= 1.0 + 1e-8 and q > 0.0):
        raise RuntimeError(f"{name}: root is not on the admitted origin-connected TC branch")
    if segment == "A" and not (pfc >= 0.8 - 1e-7 and tft <= 0.6 + 1e-7):
        raise RuntimeError(f"{name}: A-segment condition failed")
    if segment == "B" and not (pfc <= 0.8 + 1e-7 and tft >= 0.6 - 1e-7):
        raise RuntimeError(f"{name}: B-segment condition failed")

    Pu = Ppb_MN(q, c)
    return {
        "case": name,
        "segment": segment,
        "q": q,
        "P_transition_MN": Pu,
        "lambda_x": lx,
        "lambda_y": ly,
        "p_over_fc": pfc,
        "t_over_ft": tft,
        "reduction_vs_1D_pct": 100.0 * (Pu / c.Pu_1D_MN - 1.0),
        "residual_inf": float(np.max(np.abs(sol.fun))),
    }


def main() -> None:
    print("Z0-Z6 NC TC SOURCE TRANSITION — finite s=0 compatible system")
    print("formal spatial sampling/quadrature = 0")
    print("material points/load path/history state = 0/OFF")
    print()
    print("case seg q Ptrans_MN lambda_x lambda_y p/fc t/ft delta_vs_1D_% residual_inf")
    for name in CASES:
        r = solve_transition(name)
        print(
            f"{r['case']:>3s} {r['segment']:>1s} "
            f"{r['q']:.12g} {r['P_transition_MN']:.9f} "
            f"{r['lambda_x']:.9f} {r['lambda_y']:.9f} "
            f"{r['p_over_fc']:.9f} {r['t_over_ft']:.9f} "
            f"{r['reduction_vs_1D_pct']:.5f} {r['residual_inf']:.3e}"
        )

    print()
    print("IMPORTANT: these are Nguyen TC cracking/state-transition loads, not final post-crack Pu.")
    print("A later Z6 A-segment mathematical intersection must not be promoted without a source-closed post-crack continuation.")


if __name__ == "__main__":
    main()
