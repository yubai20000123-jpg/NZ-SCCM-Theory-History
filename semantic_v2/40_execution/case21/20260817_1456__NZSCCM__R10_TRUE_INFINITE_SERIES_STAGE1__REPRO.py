"""NZ-SCCM R10 true-infinite-series Stage-I reproduction.

Timestamp: 2026-08-17 14:56 +08:00

No structural spatial sampling or quadrature is performed here.
This script reproduces the source-level symbolic reductions, recurrence constants,
quadratic-field ODE degree checks, tension-knot factorization and Z6 material
landmarks used in the Stage-I derivation.
"""
import math
import sympy as sp

KAPPA = 2.0005129533678754
RHO = 0.1
ETA = 0.0024993589726987125
HVAL = 0.09799750427197301
URVAL = 0.03
A_TENSION = RHO / KAPPA
LZ6, UZ6 = -1.75, 1.45
C0, HW = (LZ6 + UZ6) / 2, (UZ6 - LZ6) / 2
A0REC = C0 * C0 + ETA * ETA + HW * HW / 2


def t_coord(x):
    q = x * x + ETA * ETA
    return 0.5 * x * x / math.sqrt(q) + 0.5 * x * x * x / q


def tprime(x):
    """Deterministic landmark diagnostic only; not part of the formal theory."""
    hh = 1e-7
    return (t_coord(x + hh) - t_coord(x - hh)) / (2 * hh)


def bisect_root(target, lo=0.0, hi=1.0, it=100):
    flo = t_coord(lo) - target
    fhi = t_coord(hi) - target
    assert flo * fhi <= 0
    for _ in range(it):
        mid = (lo + hi) / 2
        fm = t_coord(mid) - target
        if flo * fm <= 0:
            hi = mid
            fhi = fm
        else:
            lo = mid
            flo = fm
    return (lo + hi) / 2


# ---------------------------------------------------------------------------
# 1. Exact c/t decomposition into universal sqrt and rational kernels.
# ---------------------------------------------------------------------------
l, e = sp.symbols("lambda eta", positive=True)
q = l * l + e * e
f = 1 / sp.sqrt(q)
t_direct = l * l * (sp.sqrt(q) + l) / (2 * q)
c_direct = l * l * (sp.sqrt(q) - l) / (2 * q)
t_reduced = l * l * f / 2 + l**3 / (2 * q)
c_reduced = l * l * f / 2 - l**3 / (2 * q)
assert sp.simplify(t_direct - t_reduced) == 0
assert sp.simplify(c_direct - c_reduced) == 0


# ---------------------------------------------------------------------------
# 2. Quadratic-field ODE-degree generator.
# Any source branch A(lambda)+B(lambda)/sqrt(q) obeys a first-order rational ODE.
# ---------------------------------------------------------------------------
K, rho, H, UR = sp.symbols("K rho H UR", nonzero=True)
A_c = -l**3 / (2 * q)
B_c = l**2 / 2
D0 = 1 + (K - 2) * A_c + A_c * A_c + B_c * B_c / q
D1 = (K - 2) * B_c + 2 * A_c * B_c
den = sp.cancel(D0 * D0 - D1 * D1 / q)
AC = sp.cancel(K * (A_c * D0 - B_c * D1 / q) / den)
BC = sp.cancel(K * (B_c * D0 - A_c * D1) / den)


def ode_degrees(A, B):
    S = sp.cancel(sp.diff(B, l) / B - l / q)
    R = sp.cancel(sp.diff(A, l) - S * A)
    _, dS = sp.fraction(S)
    _, dR = sp.fraction(R)
    common = sp.lcm(dS, dR)
    out = []
    for expr in (common, sp.cancel(-common * S), sp.cancel(common * R)):
        num, deno = sp.fraction(sp.cancel(expr))
        assert sp.degree(deno, l) == 0
        out.append(sp.degree(num, l))
    return tuple(out)


assert ode_degrees(AC, BC) == (17, 16, 14)


# ---------------------------------------------------------------------------
# 3. Tension branch reductions and ODE degrees.
# ---------------------------------------------------------------------------
ff = sp.symbols("f")
At = l**3 / (2 * q)
Bt = l**2 / 2
rt = (At + Bt * ff) / (rho / K)
low = (
    rho * rt
    + (10 * H - 6 * rho) * rt**3
    + (8 * rho - 15 * H) * rt**4
    + (6 * H - 3 * rho) * rt**5
)
ss = (rt - 1) / 9
mid = H + (UR - H) * (10 * ss**3 - 15 * ss**4 + 6 * ss**5)
high = UR


def quad_reduce(expr):
    poly = sp.Poly(sp.expand(expr), ff)
    A = sp.S.Zero
    B = sp.S.Zero
    for (m,), coef in poly.terms():
        if m % 2 == 0:
            A += coef / q ** (m // 2)
        else:
            B += coef / q ** ((m - 1) // 2)
    return sp.cancel(A), sp.cancel(B)


Al, Bl = quad_reduce(low / rho)
Am, Bm = quad_reduce(mid / rho)
assert ode_degrees(Al, Bl) == (25, 24, 23)
assert ode_degrees(Am, Bm) == (25, 24, 24)


# ---------------------------------------------------------------------------
# 4. Exact cubic-contact factors at r=1 and r=10.
# ---------------------------------------------------------------------------
r = sp.symbols("r")
low_r = (
    rho * r
    + (10 * H - 6 * rho) * r**3
    + (8 * rho - 15 * H) * r**4
    + (6 * H - 3 * rho) * r**5
)
s_r = (r - 1) / 9
mid_r = H + (UR - H) * (10 * s_r**3 - 15 * s_r**4 + 6 * s_r**5)
high_r = UR
fac1 = sp.factor(mid_r - low_r)
fac10 = sp.factor(high_r - mid_r)
assert sp.rem(sp.Poly(mid_r - low_r, r), sp.Poly((r - 1) ** 3, r)) == 0
assert sp.rem(sp.Poly(high_r - mid_r, r), sp.Poly((r - 10) ** 3, r)) == 0


# ---------------------------------------------------------------------------
# 5. Z6 recurrence constants and material landmarks.
# ---------------------------------------------------------------------------
lam1 = bisect_root(A_TENSION, 0.0, 0.2)
lam10 = bisect_root(10 * A_TENSION, 0.2, 0.8)
x1 = (lam1 - C0) / HW
x10 = (lam10 - C0) / HW
th1 = math.acos(x1)
th10 = math.acos(x10)
geom_ratio = (4 - KAPPA) / 4


def bernstein_rho(z):
    import cmath

    w1 = z + cmath.sqrt(z * z - 1)
    w2 = z - cmath.sqrt(z * z - 1)
    return max(abs(w1), abs(w2))


zplus = (1j * ETA - C0) / HW
rho_eta = bernstein_rho(zplus)


if __name__ == "__main__":
    print("R10 TRUE-INFINITE STAGE-I")
    print("FORMAL STRUCTURAL SPATIAL SAMPLING/QUADRATURE = 0")
    print("Z6 material interval =", (LZ6, UZ6), "c0=", C0, "h=", HW)
    print("sqrt recurrence constants:")
    print("  h^2/4 =", HW * HW / 4)
    print("  h*c0  =", HW * C0)
    print("  A0     =", A0REC)
    print("compression geometric ratio upper bound =", geom_ratio)
    print("C ODE degrees =", (17, 16, 14))
    print("T low ODE degrees =", (25, 24, 23))
    print("T mid ODE degrees =", (25, 24, 24))
    print("lambda1, theta1 =", lam1, th1)
    print("lambda10, theta10 =", lam10, th10)
    print("tprime landmarks ~", tprime(lam1), tprime(lam10))
    print("rho_eta =", rho_eta)
    print("mid-low factor =", fac1)
    print("high-mid factor =", fac10)
    print("PASS: source sequence laws derived; no Pu solved in Stage-I")
