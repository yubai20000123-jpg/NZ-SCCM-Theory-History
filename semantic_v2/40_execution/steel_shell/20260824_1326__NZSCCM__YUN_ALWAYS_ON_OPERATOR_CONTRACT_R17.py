"""NZ-SCCM R17 — always-on Yun steel-shell operator contract.

This file is an architecture contract/reproducer scaffold, not a Pu solver.
It supersedes use of sigma_cr/fy as a Yun activation switch.

Frozen rule:
    YUN_ACTIVE = True for every steel-shell case.

Case parameters determine the Yun response; they do not decide whether Yun
exists in the equations.
"""

from __future__ import annotations
from dataclasses import dataclass
from math import pi

YUN_ACTIVE = True
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
TC_CC_TT = False


@dataclass(frozen=True)
class YunGeometry:
    Bs: float
    ts: float
    ell_local: float
    A0: float
    Es: float
    nu: float
    fy: float

    @property
    def r(self) -> float:
        return self.ell_local / self.Bs


def kcr_yun(r: float) -> float:
    """Yun Ch.2 exact one-side-constrained elastic coefficient."""
    return 4.0 * (3.0 * r**4 + 2.0 * r**2 + 3.0) / (3.0 * r**2)


def kp_yun(r: float) -> float:
    """Yun Ch.2 exact large-deflection membrane coefficient."""
    num = (
        272.0 * r**16
        + 2856.0 * r**14
        + 11273.0 * r**12
        + 23146.0 * r**10
        + 31506.0 * r**8
        + 23146.0 * r**6
        + 11273.0 * r**4
        + 2856.0 * r**2
        + 272.0
    )
    den = r**2 * (r**2 + 1.0) ** 2 * (r**2 + 4.0) ** 2 * (4.0 * r**2 + 1.0) ** 2
    return num / den


def ideal_ep_stress_tangent(eps: float, Es: float, fy: float) -> tuple[float, float]:
    """Minimal current steel law retained until a fuller source-closed law is adopted."""
    trial = Es * eps
    if trial > fy:
        return fy, 0.0
    if trial < -fy:
        return -fy, 0.0
    return trial, Es


def yun_local_strain(
    eps_global_face: float,
    A: float,
    A0: float,
    wg_y: float,
    dwg_y: float,
    phi_y: float,
) -> float:
    """Executed 2026-08-18 Yun/Karman local steel strain coupling."""
    return (
        eps_global_face
        + A * (wg_y + dwg_y) * phi_y
        + A0 * dwg_y * phi_y
        + (A0 * A + 0.5 * A * A) * phi_y * phi_y
    )


def yun_residual_prefactors(g: YunGeometry) -> tuple[float, float, float]:
    """Return C_sigma, kcr, H used by the continuous local amplitude row."""
    r = g.r
    kcr = kcr_yun(r)
    kp = kp_yun(r)
    C_sigma = pi**2 * g.Es * g.ts**2 / (12.0 * (1.0 - g.nu**2) * g.Bs**2)
    H = kp * (1.0 - g.nu**2) / g.ts**2
    return C_sigma, kcr, H


def yun_local_amplitude_residual(A: float, mean_compression_stress: float, g: YunGeometry) -> float:
    """Always-on local Yun row R_Ai; no sigma_cr/fy activity switch."""
    C_sigma, kcr, H = yun_residual_prefactors(g)
    return (
        C_sigma
        * (kcr * A + H * (2.0 * g.A0 * A + A * A) * (A + g.A0))
        - mean_compression_stress * (A + g.A0)
    )


def condensed_tangent(Kgg, KgA, KAA, KAg):
    """Symbolic contract only: Kgg_cond = Kgg - KgA inv(KAA) KAg.

    Actual implementation must use the project's exact finite algebra backend,
    not a spatial material-point discretization.
    """
    return (Kgg, KgA, KAA, KAg)


ARCHITECTURE = {
    "YUN_STEEL_SHELL_MODULE": "ALWAYS_ON",
    "SIGMA_CR_OVER_FY": "DIAGNOSTIC_ONLY",
    "YUN_LOCAL_AIRY_REDISTRIBUTION": "ACTIVE",
    "CURRENT_STEEL_STRESS_TANGENT": "ACTIVE",
    "YUN_TO_CURRENT_STIFFNESS": "ACTIVE",
    "YUN_LOCAL_ROWS_IN_GLOBAL_EQUILIBRIUM": "ACTIVE",
    "STATIC_FACE_CAP_AS_COMPLETE_STEEL_MODULE": "RETIRED_FROM_TARGET",
    "PRE_YUN_Pcr_C_G_Jy_GLOBAL_FREEZE": "RETIRED_FROM_TARGET",
    "NY_MY_TERMINAL": "RETAIN",
    "TC_CC_TT": "OFF_MAINLINE",
    "FORMAL_SPATIAL_QUADRATURE": 0,
    "MATERIAL_POINTS": 0,
}


if __name__ == "__main__":
    assert YUN_ACTIVE is True
    assert kcr_yun(1.0) == 32.0 / 3.0
    assert abs(kp_yun(1.0) - 42.64) < 1e-12
    print("R17_YUN_ALWAYS_ON_OPERATOR_CONTRACT = PASS")
    for k, v in ARCHITECTURE.items():
        print(f"{k} = {v}")
