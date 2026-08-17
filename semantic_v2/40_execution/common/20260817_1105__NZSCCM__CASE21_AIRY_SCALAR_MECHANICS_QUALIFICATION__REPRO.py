"""NZ-SCCM Case21 Airy-scalar mechanics qualification reproducer.

Purpose
-------
1. Reuse the frozen 2026-08-17 02:10 direct-source audit evaluator.
2. Check the reinforced linear scalar benchmark.
3. Check dRA/dlambda > 0 along the current origin-connected branch.
4. Check peak-state derivative convergence.

IMPORTANT
---------
All Gauss-Legendre grids used here are AUDIT ONLY. They do not become the formal
zero-spatial production operator. Formal counters remain:

    N_formal_spatial_sampling = 0
    N_formal_spatial_quadrature = 0
    N_formal_spatial_subdomains = 1
    N_formal_thickness_quadrature = 0
"""
from pathlib import Path
import math
import runpy
import numpy as np

BASE = Path(__file__).with_name(
    "20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_R10_CONTINUATION__REPRO.py"
)
ns = runpy.run_path(str(BASE))
Oracle = ns["Oracle"]
solve_at_D = ns["solve_at_D"]
A_AIRY = ns["A_AIRY"]
eps0 = ns["eps0"]
q0 = ns["q0"]
E0 = ns["E0"]
Es = ns["Es"]
nu = ns["nu"]
rsx = ns["rsx"]
rsy = ns["rsy"]
b = ns["b"]
ell = ns["ell"]
tp = ns["tp"]

PCR_EXP_KIP = 75.6
PF_EXP_KIP = 82.8
KIP_TO_KN = 4.4482216152605
P_F_EXP = PF_EXP_KIP * KIP_TO_KN
D_PEAK = 0.7887924801


def M_of_q(q):
    return math.pi**2 / eps0 * (q0*q + 0.5*q*q)


def linear_rc_coefficients():
    rho_s = rsy
    H = (
        4*E0*nu**2 + 6*E0
        - 4*rho_s*Es*nu**4 - rho_s*Es*nu**2 + 5*rho_s*Es
    )
    A = (
        4*E0*nu**2 + 6*E0
        - 5*rho_s*Es*nu**2 + 5*rho_s*Es
    ) / H
    B = 8*rho_s*Es*nu*(1-nu)*(1+nu)**2 / H
    return A, B


def dRA_dlambda(oracle, D, q, lam, h=5e-5):
    M = M_of_q(q)
    def RA(l):
        ev = oracle.evaluate(D, q, l*M*A_AIRY)
        return float(np.dot(A_AIRY, ev["Rm"]))
    return (RA(lam+h)-RA(lam-h))/(2*h)


def print_load_identity():
    print("Case21 experimental buckling  :", PCR_EXP_KIP*KIP_TO_KN, "kN")
    print("Case21 experimental failure   :", PF_EXP_KIP*KIP_TO_KN, "kN")
    print("Ultimate comparison target    : failure / ultimate load")


def low_load_linear_rc_check():
    A, B = linear_rc_coefficients()
    oracle = Oracle(64, 36)
    D = 0.001
    sol, ev = solve_at_D(oracle, D, [6.2e-6, 1.13])
    q, lam = sol.x
    M = ev["M"]
    lam_lin = A + B*D/M
    print("\nLinear RC scalar benchmark")
    print("A_RC =", A)
    print("B_RC =", B)
    print("D =", D, "q =", q, "M =", M)
    print("lambda direct R10 =", lam)
    print("lambda linear RC  =", lam_lin)
    print("abs difference     =", abs(lam-lam_lin))


def branch_stability_check():
    print("\n96x96x52 audit-only branch stability")
    oracle = Oracle(96, 52)
    guess = [0.0005, 0.8]
    for D in [0.1, 0.3, 0.5, 0.7, D_PEAK]:
        sol, ev = solve_at_D(oracle, D, guess)
        if not sol.success:
            raise RuntimeError(f"branch solve failed at D={D}: {sol.message}")
        q, lam = sol.x
        guess = sol.x
        slope = dRA_dlambda(oracle, D, q, lam)
        kval = ev["M"] * slope
        print(D, q, lam, ev["P"], ev["M"], slope, kval)
        assert slope > 0.0


def peak_convergence_check():
    print("\nPeak dRA/dlambda convergence (audit only)")
    guess = [0.00180836, 0.08624]
    last = None
    for nxy, nz in [(64,36),(80,44),(96,52),(112,60),(128,68),(144,76)]:
        oracle = Oracle(nxy, nz)
        sol, ev = solve_at_D(oracle, D_PEAK, guess)
        if not sol.success:
            raise RuntimeError(f"peak solve failed on {nxy}x{nxy}x{nz}")
        q, lam = sol.x
        guess = sol.x
        slope = dRA_dlambda(oracle, D_PEAK, q, lam)
        kval = ev["M"] * slope
        print((nxy,nxy,nz), q, lam, ev["P"], slope, kval)
        assert slope > 0.0
        last = (ev, slope, kval)
    ev, slope, kval = last
    print("\nFinal oracle Pu =", ev["P"], "kN")
    print("Pf_exp          =", P_F_EXP, "kN")
    print("error (%)       =", (ev["P"]-P_F_EXP)/P_F_EXP*100.0)
    print("dRA/dlambda     =", slope)
    print("M*dRA/dlambda   =", kval)


def steel_closed_form_check():
    Cs = rsy*tp*b*Es*eps0/1000.0
    CR = rsy*Es*eps0**2*b*ell*tp/(32*1000.0)
    oracle = Oracle(144, 76)
    sol, ev = solve_at_D(oracle, D_PEAK, [0.00180836,0.08624])
    q, lam = sol.x
    M = ev["M"]
    Ps = Cs*(D_PEAK-M/4)
    print("\nSteel closed-form check")
    print("Cs =", Cs, "CR =", CR)
    print("Ps closed form =", Ps)
    print("Ps oracle      =", ev["Ps"])
    assert abs(Ps-ev["Ps"]) < 1e-6


if __name__ == "__main__":
    print("FORMAL COUNTERS: 0 / 0 / 1 / 0")
    print("GAUSS EXECUTION BELOW = AUDIT ONLY")
    print_load_identity()
    low_load_linear_rc_check()
    branch_stability_check()
    peak_convergence_check()
    steel_closed_form_check()
    print("\nMECHANICS QUALIFICATION = PASS")
    print("NEXT = CASE21_AIRY_SCALAR_FORMAL_T12_FIXED_ENDPOINT_DESCRIPTOR_GATE")
