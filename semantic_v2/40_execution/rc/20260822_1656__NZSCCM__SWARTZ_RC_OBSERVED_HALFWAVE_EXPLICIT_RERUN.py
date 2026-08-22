from __future__ import annotations

"""Observed-halfwave-conditioned rerun of the current explicit Swartz RC path.

Purpose
-------
Change only the representative half-wave length ell according to the frozen
source waveform classification, regenerate all ell-dependent structural
coefficients, and solve the same current finite explicit 1D section equations.

This script is a structural waveform diagnostic. Experimental failure loads are
used only after theoretical roots are frozen. They never enter root selection,
coefficient generation, or material parameters.

Formal architecture retained:
    ONE_CONTINUOUS_COMPLETE_HALFWAVE
    N_formal_spatial_sampling = 0
    N_formal_spatial_quadrature = 0
    N_material_points = 0
    RITZ_ORDER = NONE
    LOAD_PATH_TRACKING = 0
"""

import math
import numpy as np
from scipy.optimize import root

B = 1220.0
A_PHYS = 2440.0
NU = 0.18
ES = 200000.0
FY = 530.0
Q0 = 1.0 / 400.0

# Frozen selected Swartz inputs. Pf is comparator-only.
CASES = {
    1:  dict(t=25.40, fc=22.81, E0=21730.0, eps0=0.00210, p=0.0020, ell_obs=2440.0, Pf=490.1940220017071),
    2:  dict(t=25.40, fc=22.27, E0=23194.0, eps0=0.00192, p=0.0020, ell_obs=2440.0, Pf=506.6524419781709),
    9:  dict(t=31.75, fc=15.02, E0=15480.0, eps0=0.00194, p=0.0020, ell_obs=2440.0, Pf=625.8647812671522),
    10: dict(t=31.75, fc=15.54, E0=17656.0, eps0=0.00176, p=0.0020, ell_obs=2440.0, Pf=696.1466827882682),
    19: dict(t=19.23, fc=20.20, E0=21482.0, eps0=0.00188, p=0.0050, ell_obs=1220.0, Pf=377.6540151356164),
    20: dict(t=18.97, fc=20.76, E0=20977.0, eps0=0.00198, p=0.0050, ell_obs=1220.0, Pf=372.76097135882986),
    21: dict(t=19.30, fc=21.23, E0=20321.0, eps0=0.00209, p=0.0075, ell_obs=1220.0, Pf=368.3127497435694),
    22: dict(t=19.25, fc=21.03, E0=21237.0, eps0=0.00198, p=0.0075, ell_obs=1220.0, Pf=355.85772922084),
}


def structural_coefficients(c: dict, ell: float) -> dict:
    t, E0, p = c["t"], c["E0"], c["p"]
    ax = ay = p * t
    te = t - ax - ay
    den = 1.0 - NU**2

    A11 = E0 / den * te + ES * ax
    A22 = E0 / den * te + ES * ay
    A12 = NU * E0 / den * te
    D = E0 * t**3 / (12.0 * den)
    D12 = NU * D
    H = D

    alpha = math.pi / B
    beta = math.pi / ell
    Pcr = B * (D * alpha**4 + 2.0 * H * alpha**2 * beta**2 + D * beta**4) / beta**2 / 1000.0

    DeltaA = A11 * A22 - A12**2
    Kx = B**2 * alpha**2 * DeltaA / (8.0 * A22)
    Ky = B**2 * beta**2 * DeltaA / (8.0 * A11)
    G = Ky
    C = B / 2.0 * (Ky + Kx * alpha**2 / beta**2) / 1000.0
    J = B * (D * beta**2 + D12 * alpha**2)

    return dict(A11=A11, A22=A22, A12=A12, D=D, D12=D12, H=H,
                alpha=alpha, beta=beta, Pcr=Pcr, C=C, G=G, J=J)


def section_capacity(c: dict, neutral_axis_c: float) -> tuple[float, float]:
    t, fc, eps0, p = c["t"], c["fc"], c["eps0"], c["p"]
    ys = t / 2.0
    ax = ay = p * t
    cc = neutral_axis_c

    if cc <= t:
        Nc = (2.0 / 3.0) * fc * cc
        Mc = Nc * t / 2.0 - 0.25 * fc * cc**2
    else:
        Nc = fc * (t - t**3 / (3.0 * cc**2))
        first_moment = fc * (t**2 / 2.0 - t**4 / (4.0 * cc**2))
        Mc = Nc * t / 2.0 - first_moment

    sigc_bar = fc * (1.0 - (ys / cc)**2) if ys < cc else 0.0
    eps_s = eps0 * (1.0 - ys / cc)
    sig_s = float(np.clip(ES * eps_s, -FY, FY))

    Nu = Nc - (ax + ay) * sigc_bar + ay * sig_s
    Mu = Mc  # all selected bars are mid-plane bars
    return Nu, Mu


def solve_case(c: dict, ell: float) -> dict:
    co = structural_coefficients(c, ell)

    def equations(x):
        q, cc = x
        Ppb = co["Pcr"] * q / (q + Q0) + co["C"] * q * (q + 2.0 * Q0)
        nd = Ppb * 1000.0 / B - co["G"] * q * (q + 2.0 * Q0)  # s=1
        md = co["J"] * q
        Nu, Mu = section_capacity(c, cc)
        return np.array([nd - Nu, md - Mu], dtype=float)

    candidates = []
    for qg in (1e-4, 5e-4, 1e-3, 2e-3, 4e-3, 8e-3, 1.5e-2):
        for cg in (0.3*c["t"], 0.7*c["t"], 1.2*c["t"], 2.0*c["t"], 4.0*c["t"]):
            sol = root(equations, [qg, cg])
            if not sol.success:
                continue
            q, cc = map(float, sol.x)
            if q <= 0.0 or cc <= 0.0:
                continue
            if np.linalg.norm(equations([q, cc])) > 1e-5:
                continue
            P = co["Pcr"] * q / (q + Q0) + co["C"] * q * (q + 2.0 * Q0)
            if P > 0.0:
                candidates.append((P, q, cc))

    if not candidates:
        raise RuntimeError("no admissible positive finite root")

    # Current explicit rule: smallest positive capacity root. No comparator enters selection.
    P, q, cc = min(candidates, key=lambda r: r[0])
    return dict(P=P, q=q, c=cc, **co)


def main() -> None:
    print("case,ell_obs,baseline_m2_kN,observed_wave_kN,change_pct,error_vs_Pf_pct")
    for case, c in CASES.items():
        base = solve_case(c, 1220.0)
        obs = solve_case(c, c["ell_obs"])
        change = (obs["P"] / base["P"] - 1.0) * 100.0
        err = (obs["P"] / c["Pf"] - 1.0) * 100.0
        print(f"{case},{c['ell_obs']:.1f},{base['P']:.9f},{obs['P']:.9f},{change:.6f},{err:.6f}")


if __name__ == "__main__":
    main()
