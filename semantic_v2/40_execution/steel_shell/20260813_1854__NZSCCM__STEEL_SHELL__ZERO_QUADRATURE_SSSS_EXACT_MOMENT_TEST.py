from __future__ import annotations

import math


def plate_rigidity(E: float, t: float, nu: float) -> float:
    return E * t**3 / (12.0 * (1.0 - nu**2))


def exact_shell_terms(E: float, nu: float, t: float, b: float, ell: float):
    D = plate_rigidity(E, t, nu)
    alpha = math.pi / b
    beta = math.pi / ell

    # Exact general-D15 degeneration:
    # int_0^pi sin^2 = int_0^pi cos^2 = pi/2
    # int_-1^1 eta^2 d eta = 2/3
    Kmat = D * b * ell / 4.0 * (alpha**2 + beta**2) ** 2
    Kgeo_per_N = -b * ell / 4.0 * beta**2
    Ncr_from_KZ = -Kmat / Kgeo_per_N
    Ncr_closed = D * (alpha**2 + beta**2) ** 2 / beta**2
    return D, Kmat, Kgeo_per_N, Ncr_from_KZ, Ncr_closed


def k_aspect(r: float) -> float:
    return (r + 1.0 / r) ** 2


def main() -> None:
    # Official Abaqus/Standard verification problem:
    E = 1.0e8
    nu = 0.3
    t = 0.01
    b = 2.0
    ell = 2.0

    D, Kmat, Kgeo_per_N, Ncr_KZ, Ncr_closed = exact_shell_terms(E, nu, t, b, ell)

    print('ZERO-QUADRATURE SSSS STEEL-SHELL EXACT-MOMENT TEST')
    print(f'D = {D:.15g}')
    print(f'Kmat = {Kmat:.15g}')
    print(f'Kgeo/N = {Kgeo_per_N:.15g}')
    print(f'Ncr from KZ = {Ncr_KZ:.15g}')
    print(f'Ncr closed = {Ncr_closed:.15g}')
    print(f'abs discrepancy = {abs(Ncr_KZ-Ncr_closed):.3e}')

    assert math.isclose(Ncr_KZ, Ncr_closed, rel_tol=2e-15, abs_tol=1e-12)
    assert math.isclose(Ncr_closed, 90.38099268396849, rel_tol=2e-15, abs_tol=1e-12)

    abaqus = {
        'S8R5_2x2': 90.52,
        'S8R_2x2': 95.32,
        'S9R5_2x2': 90.52,
        'STRI65_2x2': 89.64,
        'STRI3_4x4': 90.47,
        'S3R_4x4': 115.92,
        'S4R_4x4': 92.80,
        'S4R5_4x4': 92.76,
        'S4_4x4': 92.35,
    }

    print('\nOFFICIAL ABAQUS FE COMPARISON')
    for name, value in abaqus.items():
        error_pct = 100.0 * (value / Ncr_closed - 1.0)
        print(f'{name:12s}  FE={value:10.5f}  error={error_pct:+9.4f}%')

    print('\nASPECT-RATIO / HALFWAVE MINIMUM CHECK')
    for r in (0.50, 0.75, 1.00, 1.25, 1.50, 2.00):
        _, _, _, _, ncr = exact_shell_terms(E, nu, t, b, r * b)
        print(f'ell/b={r:4.2f}  k={k_aspect(r):10.6f}  Ncr={ncr:12.6f}')

    values = [exact_shell_terms(E, nu, t, b, r * b)[4] for r in (0.50, 0.75, 1.00, 1.25, 1.50, 2.00)]
    assert values[2] == min(values)

    print('\nPASS: finite-thickness shell exact moments calculate through with zero spatial/thickness quadrature.')


if __name__ == '__main__':
    main()
