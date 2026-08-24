"""R16 deterministic local-subpanel Yun elastic-preyield gate.

This reproducer does not calculate Pu and does not use any comparator.
It evaluates the absolute minimum elastic local-buckling stress in the
current one-side-constrained Yun analytical family:

    k_cr,min = 32/3
    sigma_cr,min = k_cr,min*pi^2*Es/[12(1-nu^2)]*(ts/Bs)^2

If sigma_cr,min > fy, no local aspect ratio in this elastic family can
produce local buckling before steel yield.

Geometry provenance:
- Z0-Z6: Bs=200 mm is primary-source closed from Zhou Table 5.3.
- T120/T360: current project geometry contract; independent causal
  native-CAE provenance remains partial.
- BH: Bs=0.225B is current working geometry and remains source-open.
"""

from __future__ import annotations
from dataclasses import dataclass
from math import pi, sqrt

ES = 206000.0
NU = 0.30
FY = 355.0
TS = 4.0
KCR_MIN = 32.0 / 3.0


@dataclass(frozen=True)
class LocalCase:
    family: str
    case: str
    Bs: float
    provenance: str


CASES = [
    LocalCase("Z", "Z0-Z6", 200.0, "PRIMARY_SOURCE_CLOSED_ZHOU_TABLE_5_3"),
    LocalCase("UHPC-T", "T120", 120.0, "CURRENT_PROJECT_CONTRACT_PROVENANCE_PARTIAL"),
    LocalCase("UHPC-T", "T360", 360.0, "CURRENT_PROJECT_CONTRACT_PROVENANCE_PARTIAL"),
    LocalCase("UHPC-BH", "BH005", 56.25, "CURRENT_WORKING_Bs_0P225B_SOURCE_OPEN"),
    LocalCase("UHPC-BH", "BH010", 112.5, "CURRENT_WORKING_Bs_0P225B_SOURCE_OPEN"),
    LocalCase("UHPC-BH", "BH020", 225.0, "CURRENT_WORKING_Bs_0P225B_SOURCE_OPEN"),
    LocalCase("UHPC-BH", "BH032", 360.0, "CURRENT_WORKING_Bs_0P225B_SOURCE_OPEN"),
    LocalCase("UHPC-BH", "BH050", 562.5, "CURRENT_WORKING_Bs_0P225B_SOURCE_OPEN"),
]


def sigma_cr_min(Bs: float) -> float:
    return (
        KCR_MIN
        * pi**2
        * ES
        / (12.0 * (1.0 - NU**2))
        * (TS / Bs) ** 2
    )


def transition_Bs_over_ts() -> float:
    coefficient = KCR_MIN * pi**2 * ES / (12.0 * (1.0 - NU**2))
    return sqrt(coefficient / FY)


def main() -> None:
    threshold = transition_Bs_over_ts()
    print(f"Es_MPa={ES:.12g}")
    print(f"nu={NU:.12g}")
    print(f"fy_MPa={FY:.12g}")
    print(f"kcr_min={KCR_MIN:.15g}")
    print(f"transition_Bs_over_ts={threshold:.12f}")
    print(
        "family,case,Bs_mm,ts_mm,Bs_over_ts,sigma_cr_min_MPa,"
        "sigma_cr_min_over_fy,elastic_local_before_yield_possible,geometry_provenance"
    )
    for c in CASES:
        sig = sigma_cr_min(c.Bs)
        possible = sig <= FY
        print(
            f"{c.family},{c.case},{c.Bs:.8f},{TS:.8f},{c.Bs/TS:.8f},"
            f"{sig:.12f},{sig/FY:.12f},{str(possible).upper()},{c.provenance}"
        )


if __name__ == "__main__":
    main()
