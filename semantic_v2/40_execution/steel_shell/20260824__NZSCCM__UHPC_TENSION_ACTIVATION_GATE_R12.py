"""R12: exact UHPC tensile-resultant activation gate after R11.

Purpose
-------
Determine whether a Hiew-2024 UHPC tensile branch is actually activated at any
of the seven current controlling R11 steel-shell UHPC Ny-My roots.

Important: this gate intentionally does not select SL-2.0, HL-2.0 or SL-HL-2.0.
The activation test occurs before any tensile parameter is needed.  If the complete
UHPC core is in compression at the controlling root, every admissible Hiew tensile
law contributes exactly zero resultant there.

Formal identities
-----------------
- Full 2D Marguerre-Airy structural front is frozen.
- y-normal terminal remains Ny-My.
- R11 FHWA compression diagram is unchanged.
- Formal spatial quadrature = 0.
- Thickness quadrature = 0.
- Material points = 0.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import sqrt

FC = 141.1
EC = 43400.0
ALPHA_U = 0.85
SIGP = ALPHA_U * FC
EPS_CU = 0.0035
ES = 206000.0
FY = 355.0
TC = 42.0
TS = 4.0
H = TC / 2.0
KAPPA_T = EPS_CU / TC


@dataclass(frozen=True)
class Case:
    rho: float
    fcs: float
    q: float
    kappa: float
    Ny: float
    My: float
    Pu: float
    comparator: float


CASES = {
    "T120": Case(0.05506, 355.0, 0.001532358582617, 4.979774776415e-05,
                 7312.106945, 17140.851028, 11.786054390, 12.6378),
    "T360": Case(0.01982, 301.87133, 0.001313428140621, 5.145272562064e-05,
                 6614.264322, 14385.364186, 10.650152679, 10.9688),
    "BH005": Case(0.12685714, 355.0, 0.000028827861831, 2.758413669254e-05,
                  9007.365071, 1945.102321, 2.252035579, 2.3558),
    "BH010": Case(0.06342857, 355.0, 0.000109610295040, 3.239444538014e-05,
                  8259.160764, 3561.896148, 4.130932213, 4.3043),
    "BH020": Case(0.03171429, 355.0, 0.000462148890429, 4.119300500595e-05,
                  7651.896017, 7365.729016, 7.663407953, 8.0076),
    "BH032": Case(0.01982143, 295.42, 0.001324938066331, 5.086216663831e-05,
                  6630.111828, 13102.180044, 10.667983706, 10.9905),
    "BH050": Case(0.01268571, 250.07, 0.004675216555654, 6.855138326101e-05,
                  5103.410893, 29458.539517, 13.256120907, 12.2198),
}


def integrate_clipped(a: float, b: float, E: float, lo: float, hi: float,
                      kappa: float, density: float = 1.0):
    """Exact N,M primitive of clip(E*(EPS_CU-kappa*y),lo,hi)."""
    cuts = [a, b]
    if abs(kappa) > 1e-16:
        for sth in (lo, hi):
            y = (EPS_CU - sth / E) / kappa
            if a < y < b:
                cuts.append(y)
    cuts = sorted(set(cuts))
    N = M = 0.0
    for u, v in zip(cuts[:-1], cuts[1:]):
        mid = 0.5 * (u + v)
        trial = E * (EPS_CU - kappa * mid)
        if trial <= lo:
            A, B = lo, 0.0
        elif trial >= hi:
            A, B = hi, 0.0
        else:
            A, B = E * EPS_CU, -E * kappa
        A *= density
        B *= density
        d1 = v - u
        d2 = v * v - u * u
        d3 = v ** 3 - u ** 3
        n = A * d1 + 0.5 * B * d2
        first_y = 0.5 * A * d2 + (B / 3.0) * d3
        N += n
        M += H * n - first_y
    return N, M


def r11_section(kappa: float, c: Case):
    """R11 compression-only section; exact and zero thickness quadrature."""
    parts = [
        (-TS, 0.0, ES, -FY, c.fcs, 1.0),
        (0.0, TC, EC, 0.0, SIGP, 1.0 - c.rho),
        (0.0, TC, ES, -FY, FY, c.rho),
        (TC, TC + TS, ES, -FY, c.fcs, 1.0),
    ]
    N = M = 0.0
    for a, b, E, lo, hi, d in parts:
        n, m = integrate_clipped(a, b, E, lo, hi, kappa, d)
        N += n
        M += m
    return N, M


def main():
    print("R12 UHPC tensile-resultant activation gate")
    print("formal spatial quadrature = 0")
    print("thickness quadrature = 0")
    print("material points = 0")
    print(f"kappa_tension_onset = {KAPPA_T:.15g} 1/mm")
    print("case kappa ratio eps_bottom Ny_root Ny_onset My_root My_onset Pu error_pct active")

    errors = []
    for name, c in CASES.items():
        eps_bottom = EPS_CU - c.kappa * TC
        N_on, M_on = r11_section(KAPPA_T, c)
        active = not (c.kappa < KAPPA_T and eps_bottom > 0.0)
        error = 100.0 * (c.Pu / c.comparator - 1.0)
        if name != "BH050":
            errors.append(error)

        # Exact activation gate: all controlling roots must precede first UHPC tension.
        assert c.kappa < KAPPA_T
        assert eps_bottom > 0.0
        assert c.Ny > N_on
        assert M_on > c.My
        assert active is False

        print(
            f"{name:6s} {c.kappa:.12g} {c.kappa/KAPPA_T:.9f} "
            f"{eps_bottom:.12g} {c.Ny:.6f} {N_on:.6f} "
            f"{c.My:.6f} {M_on:.6f} {c.Pu:.9f} {error:.6f} {active}"
        )

    mean = sum(errors) / len(errors)
    mae = sum(abs(x) for x in errors) / len(errors)
    rmse = sqrt(sum(x*x for x in errors) / len(errors))
    print(f"primary6_mean_signed_pct = {mean:.9f}")
    print(f"primary6_MAE_pct = {mae:.9f}")
    print(f"primary6_RMSE_pct = {rmse:.9f}")
    print("R12 roots = R11 roots: PASS")


if __name__ == "__main__":
    main()
