"""NZ-SCCM Z6 rectangular-Airy derivation and fixed-state compiler-gate checks.

Timestamp: 2026-08-17 13:37 +08:00

This file reproduces the exact rectangular Airy coefficients, their isotropic
elastic benchmark, and arithmetic gates from the saved direct-R10 / N48
fixed-state audit ledger.  It is NOT the Gauss audit executor and therefore
must not be presented as a formal structural integration solver.

Formal structural spatial sampling/quadrature remains zero.
"""
import math

# Real Z6
A = 9000.0
b = 12000.0
ell = 9000.0
k = b / ell
nu = 0.18
eps0 = 0.0018712490394580678
q0 = (A / 500.0) / b
rho_w = 0.02

# Rectangular Airy direction derived from elastic harmonic equilibrium.
b0 = -(1.0 + nu * k * k) / 4.0
b20 = (nu * k * k - 1.0) / 4.0
b22 = 1.0 / 4.0
c02 = (nu - k * k) / 4.0
c22 = k * k / 4.0
d22 = -k / 2.0

expected = (-0.33, -0.17, 0.25, -0.3994444444444444,
            0.4444444444444444, -0.6666666666666666)
actual = (b0, b20, b22, c02, c22, d22)
for x, y in zip(actual, expected):
    assert abs(x - y) < 1e-14, (x, y)

# k=1 degeneration must recover the qualified Case21 square vector.
def airy(k_, nu_):
    return (
        -(1.0 + nu_ * k_ * k_) / 4.0,
        (nu_ * k_ * k_ - 1.0) / 4.0,
        1.0 / 4.0,
        (nu_ - k_ * k_) / 4.0,
        k_ * k_ / 4.0,
        -k_ / 2.0,
    )

sq = airy(1.0, 0.18)
assert all(abs(x-y) < 1e-14 for x, y in zip(
    sq, (-0.295, -0.205, 0.25, -0.205, 0.25, -0.5)))

# Direct-R10 audit peak ledger (external oracle only).
D = 1.30722165
q = 0.02144304
lam = 0.84614161
M = math.pi**2 / eps0 * (q0*q + 0.5*q*q)
P_direct = 43.45654
Pc_eff_direct = 20.23789
Pc_full_direct = Pc_eff_direct / (1.0-rho_w)

# Broad fixed-N48 same-state formal concrete result.
Pc_full_n48 = 18.5008
compiler_gap_pct = (Pc_full_n48/Pc_full_direct - 1.0) * 100.0
assert compiler_gap_pct < -10.0

# External comparator only, never used in compiler selection.
P_zhou = 49.672436
model_gap_pct = (P_direct/P_zhou - 1.0) * 100.0

# High-grid direct audit ledger.
conv = [
    ("32x32x14_face6", 43.46840),
    ("40x40x16_face8", 43.43295),
    ("48x48x20_face8", 43.47339),
    ("56x56x22_face10", 43.45191),
    ("64x64x24_face10", 43.45118),
    ("72x72x28_face12", 43.46148),
    ("80x80x30_face12", 43.45654),
]

if __name__ == "__main__":
    print("REAL Z6: a,b,ell,k,q0 =", A, b, ell, k, q0)
    print("rectangular Airy coefficients =", actual)
    print("square degeneration =", sq)
    print("peak D,q,lambda,M =", D, q, lam, M)
    print("direct-R10 audit convergence:")
    for row in conv:
        print("  ", row)
    print("Pc_full_direct ~=", Pc_full_direct, "MN")
    print("Pc_full_N48   ~=", Pc_full_n48, "MN")
    print("same-state N48 compiler gap (%) =", compiler_gap_pct)
    print("direct R10 vs Zhou fitted formula gap (%) =", model_gap_pct)
    print("FORMAL Z6 Pu RELEASED = NO")
    print("NEXT = Z6_CONVERGENT_SERIES_FINITE_MOMENT_MATERIAL_COMPILER")
