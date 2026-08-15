"""Zhou original full-MCFSTW Z0-Z6 formula replay.

Timestamp: 2026-08-15 12:33 +08:00

Identity:
- NZ-SCCM comparison values are externally persisted reduced-object diagnostics.
- This script computes only Zhou's ORIGINAL full-MCFSTW formula side.
- Internal web steel is retained in the Zhou section; no reduced-D_EI shortcut is used.
- No test/comparator load is used to select m or alter a parameter.
"""

from math import pi, sqrt

ES = 206000.0
NU_S = 0.30
NU_C = 0.20

# case, ns, ls, h, ts, fy, fcu, a, b, current NZ A/500+local-cap D32, old transferred comparator
CASES = [
    ("Z0", 30, 200.0, 130.0, 4.0, 355.0, 40.0, 6000.0, 6000.0, 36.61933000, 33.429123359711),
    ("Z1", 30, 200.0, 100.0, 4.0, 235.0, 40.0, 6000.0, 6000.0, 23.19047000, 22.208147192292),
    ("Z2", 30, 200.0, 130.0, 4.0, 460.0, 40.0, 6000.0, 6000.0, 40.20807000, 36.858841504351),
    ("Z3", 30, 200.0, 130.0, 4.0, 355.0, 60.0, 6000.0, 6000.0, 45.02278000, 41.158145428775),
    ("Z4", 40, 200.0, 200.0, 4.0, 355.0, 40.0, 6000.0, 8000.0, 66.88685000, 62.043026001061),
    ("Z5", 10, 200.0, 130.0, 4.0, 355.0, 40.0, 3000.0, 2000.0, 13.17757000, 13.097600000000),
    ("Z6", 60, 200.0, 130.0, 4.0, 355.0, 40.0, 9000.0, 12000.0, 37.50942609, 44.740402775200),
]


def Ec_from_source(fcu):
    # Zhou/project source replay used in the preceding Table-5.1 staging.
    if abs(fcu - 40.0) < 1e-12:
        return 32500.0
    return 1.0e5 / (34.7 / fcu + 2.2)


def zhou_original(case):
    name, ns, ls, h, ts, fy, fcu, a, b, nz_pu, old_transfer = case
    Ec = Ec_from_source(fcu)
    Gs = ES / (2.0 * (1.0 + NU_S))
    Gc = Ec / (2.0 * (1.0 + NU_C))
    fc = 0.76 * fcu
    tc = h - 2.0 * ts

    # Original MCFSTW section: ls is web-centreline spacing.
    Ac = ns * (ls - ts) * tc
    Ag = b * h
    As = Ag - Ac
    Psteel = fy * As / 1.0e6
    Pconc = fc * Ac / 1.0e6
    Pyth = Psteel + Pconc

    # Zhou original bending stiffnesses.
    void_I = ns * (ls - ts) * tc**3 / 12.0
    Dy_s = ES / b * (b * h**3 / 12.0 - void_I)
    Dy_c = Ec / b * void_I
    Dy = Dy_s + Dy_c
    Dx = ES * (h**3 - tc**3) / 12.0 + Ec * tc**3 / 12.0

    # Zhou original free torsion chain, Eqs. 4-33--4-36.
    A0 = (b - ts) * (h - ts)
    s = 2.0 * ((b - ts) + (h - ts))
    integral_ds_over_t = s / ts
    ratio = tc / (b - 2.0 * ts)
    beta_shape = (1.0 / 3.0) * (1.0 - 0.63 * ratio + 0.052 * ratio**5)
    steel_tors = 4.0 * Gs * A0**2 / integral_ds_over_t
    concrete_tors = Gc * beta_shape * (b - 2.0 * ts) * tc**3
    Dt = (steel_tors + concrete_tors) / b
    Dxy = Dt / 2.0

    Dmu = NU_S * Dy_s + NU_C * Dy_c
    H = Dxy + Dmu

    # Zhou Eq. 5-79. Retain all m candidates and choose the theoretical minimum.
    candidates = []
    for m in range(1, 51):
        Ncr = pi**2 * (
            Dx * a**2 / (m**2 * b**4)
            + 2.0 * H / b**2
            + Dy * m**2 / a**2
        )
        Pcr = Ncr * b / 1.0e6
        candidates.append((m, Pcr))
    m_star, Pcr = min(candidates, key=lambda item: item[1])

    lam = sqrt(Pyth / Pcr)
    if lam <= 1.0:
        Phi = 0.454 + 0.192 * lam + 0.416 * lam**2
    else:
        Phi = -0.140 + 1.387 * lam - 0.186 * lam**2
    if lam <= 0.55:
        phi = 1.0
    else:
        phi = 1.0 / (Phi + sqrt(Phi**2 - lam**2))
    Pu = phi * Pyth

    return {
        "case": name, "ns": ns, "ls": ls, "h": h, "ts": ts,
        "fy": fy, "fcu": fcu, "a": a, "b": b,
        "Ec": Ec, "Gs": Gs, "Gc": Gc, "fc_prime": fc, "tc": tc,
        "Ac": Ac, "Ag": Ag, "As": As,
        "Psteel": Psteel, "Pconc": Pconc, "Pyth": Pyth,
        "Dx": Dx, "Dy_s": Dy_s, "Dy_c": Dy_c, "Dy": Dy,
        "A0": A0, "perimeter": s, "integral_ds_over_t": integral_ds_over_t,
        "beta_shape": beta_shape, "steel_tors": steel_tors,
        "concrete_tors": concrete_tors, "Dt": Dt, "Dxy": Dxy,
        "Dmu": Dmu, "H": H,
        "m_candidates": candidates, "m_star": m_star, "Pcr": Pcr,
        "lambda": lam, "Phi": Phi, "phi": phi, "Pu_Zhou_original": Pu,
        "Pu_Zhou_old_transferred": old_transfer,
        "zhou_original_shift_pct": (Pu - old_transfer) / old_transfer * 100.0,
        "NZ_D32": nz_pu,
        "NZ_minus_Zhou_original_pct": (nz_pu - Pu) / Pu * 100.0,
    }


def main():
    results = [zhou_original(c) for c in CASES]
    print("case,Pyth_MN,m_star,Pcr_MN,lambda_n,Phi_N,phi_N,Pu_Zhou_original_MN,NZ_D32_MN,NZ_minus_Zhou_pct")
    for r in results:
        print(
            f"{r['case']},{r['Pyth']:.12f},{r['m_star']},{r['Pcr']:.12f},"
            f"{r['lambda']:.12f},{r['Phi']:.12f},{r['phi']:.12f},"
            f"{r['Pu_Zhou_original']:.12f},{r['NZ_D32']:.12f},{r['NZ_minus_Zhou_original_pct']:.12f}"
        )
    print("\n# complete m=1..50 Eq.5-79 candidates")
    for r in results:
        print(r['case'] + ":" + ",".join(f"m{m}={p:.12f}" for m, p in r['m_candidates']))
    mape_all = sum(abs(r['NZ_minus_Zhou_original_pct']) for r in results) / len(results)
    mape_0_5 = sum(abs(r['NZ_minus_Zhou_original_pct']) for r in results[:6]) / 6.0
    mean_signed = sum(r['NZ_minus_Zhou_original_pct'] for r in results) / len(results)
    print(f"\nMAPE_Z0_Z6={mape_all:.12f}%")
    print(f"MAPE_Z0_Z5={mape_0_5:.12f}%")
    print(f"MEAN_SIGNED_Z0_Z6={mean_signed:.12f}%")


if __name__ == "__main__":
    main()
