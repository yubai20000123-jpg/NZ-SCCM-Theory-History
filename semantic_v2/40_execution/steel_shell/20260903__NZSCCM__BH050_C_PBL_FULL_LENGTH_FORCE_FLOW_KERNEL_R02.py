#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NZ-SCCM / BH050 C-PBL full-length force-flow kernel R02

Identity
--------
Diagnostic / theory-development implementation. It does NOT modify R14 production
and does NOT report a source-grade Pu(C_P).

The code mirrors the accompanying R02 technical ledger. The primary result of R02
is an exact mechanics statement: with common steel/core end displacement and a
prescribed geometric-shortening field g(y), the phase-average axial-force partition is
independent of the longitudinal connector stiffness C_P. C_P controls slip, interface
shear, local force oscillation, and therefore can affect the condensed tangent / terminal
only after the current C1 steel operator is coupled back consistently.

No spatial quadrature is used in the executed sweep; all expressions are closed form.
"""

from __future__ import annotations
import csv
import math
from pathlib import Path

# 1. BH050 source-locked raw inputs used by this diagnostic
B = 2500.0
L_PHYS = 5000.0
TC = 42.0
TS = 4.0
AW = 1332.0
ES = 206000.0
EC = 43400.0
L_CELL = L_PHYS / 9.0
LX = 562.5
A0_LOCAL = 0.3515625

# Frozen R02/R06 amplitudes: forcing-scale audit only, NOT latest C1 amplitudes.
U_UP_R02 = 0.16926688579226457
U_LO_R02 = 2.9398459144778792

# Current C1 diagnostic force level: cross-ledger scale comparison only.
N_TOTAL_C1 = -5194.45
N_WEB_C1 = -162.60

# 2. Section-design elastic baseline (per unit width)
RHO_W = AW / (B * TC)
K_C_PER_W = EC * (1.0 - RHO_W) * TC
K_S_FACE_PER_W = ES * TS
K_S_FACES_PER_W = 2.0 * K_S_FACE_PER_W
K_WEB_PER_W = ES * AW / B
K_TOTAL_PER_W = K_C_PER_W + K_S_FACES_PER_W + K_WEB_PER_W

ETA_C_SEC = K_C_PER_W / K_TOTAL_PER_W
ETA_S_SEC = K_S_FACES_PER_W / K_TOTAL_PER_W
ETA_W_SEC = K_WEB_PER_W / K_TOTAL_PER_W

# 3. R02 geometric-shortening forcing scale
KY = 2.0 * math.pi / L_CELL
CY = 3.0 * KY * KY / 8.0
D_UP = U_UP_R02 * U_UP_R02 - A0_LOCAL * A0_LOCAL
D_LO = U_LO_R02 * U_LO_R02 - A0_LOCAL * A0_LOCAL
G_BAR_UP = CY * D_UP
G_BAR_LO = CY * D_LO
G0 = 0.5 * (G_BAR_UP + G_BAR_LO)

# 4. Full-width steel-faces <-> UHPC partial-interaction reference.
#    Web/PBL axial path remains separate in this first audit.
K_S = K_S_FACES_PER_W * B
K_C = K_C_PER_W * B
K_EQ = K_S * K_C / (K_S + K_C)
C0 = K_EQ / L_CELL
N_CELL_HARMONIC = 4
N_FULL_HARMONIC = N_CELL_HARMONIC * 9


def exact_harmonic(lambda_cell: float) -> dict[str, float]:
    """Closed-form full-length result for repeated BH050 R02 forcing.

    lambda_cell = k_P L_cell^2/K_eq = C_P L_cell/K_eq = C_P/C0.
    The same field over L_phys is harmonic n=36 with Lambda_full=81 Lambda_cell.
    """
    den = N_CELL_HARMONIC**2 * math.pi**2 + lambda_cell
    eta = 0.0 if lambda_cell == 0.0 else lambda_cell / den
    relief = N_CELL_HARMONIC**2 * math.pi**2 / den
    cp = lambda_cell * C0
    kp = cp / L_CELL
    ell = math.inf if lambda_cell == 0.0 else L_CELL / math.sqrt(lambda_cell)
    smax = G0 * N_CELL_HARMONIC * math.pi * L_CELL / den
    tmax = kp * smax
    dns_amp = K_EQ * G0 * eta
    lam_full = lambda_cell * (L_PHYS / L_CELL) ** 2
    eta_full = 0.0 if lam_full == 0.0 else lam_full / (
        N_FULL_HARMONIC**2 * math.pi**2 + lam_full
    )
    return {
        "Lambda_cell": lambda_cell,
        "Lambda_full": lam_full,
        "C_P_N_per_mm": cp,
        "eta": eta,
        "slip_relief": relief,
        "transfer_length_mm": ell,
        "s_max_mm": smax,
        "t_max_N_per_mm": tmax,
        "delta_Ns_amp_N": dns_amp,
        "delta_Ns_amp_per_width_N_per_mm": dns_amp / B,
        "eta_full_check": eta_full,
    }


def mean_partition_for_fixed_total(n_total: float, n_web: float, g0: float) -> dict[str, float]:
    """Exact mean-force partition under common end displacement.

    This result contains NO C_P because the connector term integrates out of the
    phase-average constitutive relations when s(0)=s(L)=0.
    """
    n_phase = n_total - n_web
    ebar = (n_phase - K_S_FACES_PER_W * g0) / (K_S_FACES_PER_W + K_C_PER_W)
    ns = K_S_FACES_PER_W * (ebar + g0)
    nc = K_C_PER_W * ebar
    return {
        "e_bar": ebar,
        "N_steel_faces_N_per_mm": ns,
        "N_UHPC_N_per_mm": nc,
        "N_web_N_per_mm": n_web,
        "N_total_check_N_per_mm": ns + nc + n_web,
        "eta_UHPC_total": nc / n_total,
        "eta_steel_faces_total": ns / n_total,
        "eta_web_total": n_web / n_total,
    }


def exact_line_element_matrices(Ks: float, Kc: float, kp: float, Le: float):
    """Exact 2-node line-element integral identities, retained as an audit utility.

    This is NOT used in the formal harmonic sweep and therefore does not introduce
    numerical spatial quadrature/discretization into the executed R02 result.
    """
    ks = Ks / Le
    kc = Kc / Le
    cp = kp * Le / 6.0
    Ks_e = [
        [ ks, -ks, 0.0, 0.0],
        [-ks,  ks, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
    ]
    Kc_e = [
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0,  kc, -kc],
        [0.0, 0.0, -kc,  kc],
    ]
    Kp_e = [
        [2*cp, cp, -2*cp, -cp],
        [cp, 2*cp, -cp, -2*cp],
        [-2*cp, -cp, 2*cp, cp],
        [-cp, -2*cp, cp, 2*cp],
    ]
    return Ks_e, Kc_e, Kp_e


def run_sweep(out_csv: Path) -> None:
    lambdas = [0.0, 0.1, 1.0, 5.0, 10.0, 20.0, 40.0, 80.0,
               16.0*math.pi**2, 200.0, 500.0, 1000.0]
    rows = [exact_harmonic(x) for x in lambdas]
    fields = list(rows[0].keys())
    with out_csv.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    assert all(abs(r["eta"] - r["eta_full_check"]) < 2e-15 for r in rows)
    assert abs(ETA_C_SEC + ETA_S_SEC + ETA_W_SEC - 1.0) < 1e-14

    mp = mean_partition_for_fixed_total(N_TOTAL_C1, N_WEB_C1, G0)
    assert abs(mp["N_total_check_N_per_mm"] - N_TOTAL_C1) < 1e-9

    print("BH050 R02 full-length C_P force-flow diagnostic")
    print("rho_w =", RHO_W)
    print("section elastic shares: UHPC, steel faces, web =",
          ETA_C_SEC, ETA_S_SEC, ETA_W_SEC)
    print("Kc_per_width, Ks_faces_per_width, Kw_per_width =",
          K_C_PER_W, K_S_FACES_PER_W, K_WEB_PER_W)
    print("gbar upper/lower, G0 =", G_BAR_UP, G_BAR_LO, G0)
    print("Ks_total, Kc_total, Keq_total, C0 =", K_S, K_C, K_EQ, C0)
    print("mean partition cross-ledger audit (independent of C_P):")
    for k, v in mp.items():
        print(" ", k, "=", v)
    print("CSV:", out_csv)
    print("\nLambda  C_P(MN/mm) eta  ell(mm) smax(mm) tmax(kN/mm) dNs/B(N/mm)")
    for r in rows:
        ell = r["transfer_length_mm"]
        ell_s = "inf" if math.isinf(ell) else f"{ell:.6f}"
        print(f'{r["Lambda_cell"]:10.5f} {r["C_P_N_per_mm"]/1e6:12.6f} '
              f'{r["eta"]:9.6f} {ell_s:>11} {r["s_max_mm"]:10.6f} '
              f'{r["t_max_N_per_mm"]/1000:12.6f} '
              f'{r["delta_Ns_amp_per_width_N_per_mm"]:12.6f}')


if __name__ == "__main__":
    run_sweep(Path("/mnt/data/NZSCCM_BH050_C_PBL_full_length_CP_sweep_R02.csv"))
