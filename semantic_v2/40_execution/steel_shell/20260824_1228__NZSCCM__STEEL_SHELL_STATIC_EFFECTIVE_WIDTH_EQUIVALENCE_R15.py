"""R15: steel-shell local-buckling cap vs effective-width/resultant audit.

Keeps the full 2D Marguerre-Airy structural demand and the axial y-normal
Ny-My terminal unchanged. Shows that a static widthwise effective-width
reduction of one external face is exactly equivalent, on the present Ny-My
cut, to a scalar compressive face force/stress cap.
"""
from __future__ import annotations

FY = 355.0
TS = 4.0

UHPC = [
    ("T120", 1600.0, 0.001631860743, 0.0025, 355.0, 12.252164525, 12.6378, -3.051444673, "primary"),
    ("T360", 1600.0, 0.001406053484, 0.0025, 301.87133, 11.133264739, 10.9688, 1.499386794, "primary"),
    ("BH005", 250.0, 3.103538185e-5, 0.0025, 355.0, 2.422372923, 2.3558, 2.825915759, "primary"),
    ("BH010", 500.0, 0.0001188132600, 0.0025, 355.0, 4.462040087, 4.3043, 3.664709396, "primary"),
    ("BH020", 1000.0, 0.0004977063181, 0.0025, 355.0, 8.155351621, 8.0076, 1.845142374, "primary"),
    ("BH032", 1600.0, 0.001420886996, 0.0025, 295.42, 11.163055965, 10.9905, 1.570046536, "primary"),
    ("BH050", 2500.0, 0.005045738449, 0.0025, 250.07, 13.650448214, 12.2198, 11.707623808, "lower_confidence"),
]

NC = [
    ("Z0", 6000.0, 0.003428230723, 0.004, 37.825706787, 36.9455, 2.382),
    ("Z1", 6000.0, 0.004996679885, 0.004, 24.714128548, 23.7214, 4.185),
    ("Z2", 6000.0, 0.004321772846, 0.004, 42.959011131, 41.2134, 4.236),
    ("Z3", 6000.0, 0.004613406152, 0.004, 46.495651955, 44.3203, 4.908),
    ("Z4", 8000.0, 0.002445428167, 0.004, 70.265718566, 69.3399, 1.335),
    ("Z5", 2000.0, 0.000258841897, 0.004, 14.118193577, 14.6816, -3.838),
    ("Z6", 12000.0, 0.013807412938, 0.004, 56.379421090, 49.4868, 13.928),
]


def eta_from_face_cap(fcs: float, fy: float = FY) -> float:
    return fcs / fy


def static_equivalence_force(fcs: float, ts: float = TS, fy: float = FY) -> tuple[float, float]:
    eta = eta_from_face_cap(fcs, fy)
    return fcs * ts, eta * fy * ts


def rho_sun_2022(lam: float) -> float:
    # Sun Lipeng Eq. (3.25), one-side-constrained flat plate.
    if lam <= 0.500:
        return 1.0
    if lam <= 1.348:
        return 0.66 / lam**0.6
    return 0.64 / lam**0.5


def rho_bridge_1998_as_reported_by_yun(lam: float) -> float:
    # Yun thesis Eq. (5-13).
    a = lam**(-1.2)
    return a * (1.0 - 0.25 * a)


def main() -> None:
    print("R15 static effective-width equivalence audit")
    print("UHPC: case gross_b/t q_u Ainc_mm Atot/t eta_cap face_loss_pct error_pct role")
    for case, b, q, q0, fcs, pu, comp, err, role in UHPC:
        eta = eta_from_face_cap(fcs)
        n1, n2 = static_equivalence_force(fcs)
        assert abs(n1 - n2) < 1e-12
        print(f"{case:6s} {b/TS:9.3f} {q:.12g} {b*q:10.6f} {b*(q+q0)/TS:10.6f} {eta:10.7f} {100*(1-eta):10.5f} {err:10.5f} {role}")
    print("NC: case gross_b/t q_u Ainc_mm Atot/t eta_terminal error_vs_Zhou_pct")
    for case, b, q, q0, pu, zhou, err in NC:
        print(f"{case:3s} {b/TS:9.3f} {q:.12g} {b*q:10.6f} {b*(q+q0)/TS:10.6f} {1.0:10.7f} {err:10.5f}")
    print("STATIC_IDENTITY: be/b=eta -> fcs=eta*fy on one external face")
    print("A richer terminal requires source-closed local subpanel geometry plus a progressive effective-width/effective-area relation.")


if __name__ == "__main__":
    main()
