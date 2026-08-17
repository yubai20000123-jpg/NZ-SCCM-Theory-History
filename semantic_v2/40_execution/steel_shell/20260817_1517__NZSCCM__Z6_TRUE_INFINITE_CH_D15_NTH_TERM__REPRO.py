"""NZ-SCCM true-infinite R10 Stage-II CH/D15 nth-term audit.

Timestamp: 2026-08-17 15:17 +08:00

Formal spatial quadrature = 0.  The script builds the corrected Z6(a=24000)
complete-halfwave normalized matrix field in Fourier-zeta coefficient algebra,
then verifies that direct matrix Chebyshev recurrence equals the exact 2x2
Cayley-Hamilton p/q recurrence.  All displayed J_n values use closed Fourier
and thickness moments; no spatial sampling points are created.
"""
import math
from collections import defaultdict

TOL = 1e-13

# ---------------------------------------------------------------------------
# Sparse Fourier-zeta algebra: key = (kx,ky,kzeta).
# ---------------------------------------------------------------------------
def clean(a):
    return {k: v for k, v in a.items() if abs(v) > TOL}


def add(a, b, s=1.0):
    d = defaultdict(complex)
    for k, v in a.items():
        d[k] += v
    for k, v in b.items():
        d[k] += s * v
    return clean(d)


def scale(a, s):
    return clean({k: s * v for k, v in a.items()})


def mul(a, b):
    d = defaultdict(complex)
    for (i, j, k), v in a.items():
        for (p, q, r), w in b.items():
            d[(i + p, j + q, k + r)] += v * w
    return clean(d)


def const(x):
    return {(0, 0, 0): complex(x)} if x else {}


def zeta():
    return {(0, 0, 1): 1 + 0j}


def ex(n):
    return {(n, 0, 0): 1 + 0j}


def ey(n):
    return {(0, n, 0): 1 + 0j}


def sinx(n=1):
    return add(scale(ex(n), 1 / (2j)), scale(ex(-n), -1 / (2j)))


def cosx(n=1):
    return add(scale(ex(n), 0.5), scale(ex(-n), 0.5))


def siny(n=1):
    return add(scale(ey(n), 1 / (2j)), scale(ey(-n), -1 / (2j)))


def cosy(n=1):
    return add(scale(ey(n), 0.5), scale(ey(-n), 0.5))


# Exact one-dimensional endpoint moments.
def Ipi(n):
    if n == 0:
        return math.pi
    return (((-1) ** n) - 1) / (1j * n)


def Iz(k):
    return 0.0 if k % 2 else 2.0 / (k + 1)


def d15(F):
    return sum(
        v * Ipi(i) * Ipi(j) * Iz(k)
        for (i, j, k), v in F.items()
    ).real


# ---------------------------------------------------------------------------
# 2x2 field algebra.
# ---------------------------------------------------------------------------
I = [[const(1), {}], [{}, const(1)]]


def matadd(A, B, s=1.0):
    return [[add(A[i][j], B[i][j], s) for j in range(2)] for i in range(2)]


def matscale(A, s):
    return [[scale(A[i][j], s) for j in range(2)] for i in range(2)]


def matmul(A, B):
    C = [[{} for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = add(C[i][j], mul(A[i][k], B[k][j]))
    return C


def ch_matrix(p, q, E):
    return [
        [add(p if i == j else {}, mul(q, E[i][j])) for j in range(2)]
        for i in range(2)
    ]


def max_field_error(A, B):
    err = 0.0
    for i in range(2):
        for j in range(2):
            keys = set(A[i][j]) | set(B[i][j])
            for key in keys:
                err = max(err, abs(A[i][j].get(key, 0) - B[i][j].get(key, 0)))
    return err


# ---------------------------------------------------------------------------
# Corrected Z6(a=24000), one complete 12000-mm halfwave, Airy scalar state.
# ---------------------------------------------------------------------------
def z6_ehat():
    D = 1.36180798
    qamp = 0.026485404
    lamA = 0.786915819
    eps0 = 0.0018712490394580678
    nu = 0.18
    q0 = 0.004
    tc = 122.0
    b = 12000.0
    c0 = -0.15
    h = 1.6

    M = math.pi**2 / eps0 * (q0 * qamp + 0.5 * qamp * qamp)
    B = math.pi**2 / (2 * eps0) * (tc / b) * qamp

    CX, CY = cosx(2), cosy(2)
    SX, SY = sinx(2), siny(2)
    CXC = mul(CX, CY)
    SXS = mul(SX, SY)
    sxs = mul(sinx(), siny())
    cxc = mul(cosx(), cosy())

    bx = const(1)
    bx = add(bx, CX)
    bx = add(bx, CY, -1)
    bx = add(bx, CXC, -1)
    bx = add(bx, const(lamA * (1 + nu)), -1)
    bx = add(bx, scale(CX, lamA * (1 - nu)), -1)
    bx = add(bx, scale(CXC, lamA))

    by = const(1)
    by = add(by, CX, -1)
    by = add(by, CY)
    by = add(by, CXC, -1)
    by = add(by, scale(CY, lamA * (1 - nu)), -1)
    by = add(by, scale(CXC, lamA))

    exx = add(const(nu * D), scale(bx, M / 4))
    exx = add(exx, scale(mul(sxs, zeta()), B))
    eyy = add(const(-D), scale(by, M / 4))
    eyy = add(eyy, scale(mul(sxs, zeta()), B))
    gam = scale(SXS, M / 2 * (1 - lamA))
    gam = add(gam, scale(mul(cxc, zeta()), -2 * B))

    den = 1 - nu * nu
    X11 = scale(add(exx, scale(eyy, nu)), 1 / den)
    X22 = scale(add(scale(exx, nu), eyy), 1 / den)
    X12 = scale(gam, 1 / (2 * (1 + nu)))

    E = [
        [scale(add(X11, const(-c0)), 1 / h), scale(X12, 1 / h)],
        [scale(X12, 1 / h), scale(add(X22, const(-c0)), 1 / h)],
    ]
    return E, M, B


def main():
    E, M, B = z6_ehat()
    tau = add(E[0][0], E[1][1])
    delta = add(mul(E[0][0], E[1][1]), mul(E[0][1], E[1][0]), -1)

    # Direct matrix recurrence and CH p/q recurrence.
    Tm1, Tn = I, E
    pm1, pn = const(1), {}
    qm1, qn = {}, const(1)

    rows = [(0, d15(Tm1[1][1]), 0.0), (1, d15(Tn[1][1]), 0.0)]

    for n in range(1, 8):
        Tnext = matadd(matscale(matmul(E, Tn), 2), Tm1, -1)

        pnext = add(scale(mul(delta, qn), -2), pm1, -1)
        qnext = add(scale(pn, 2), scale(mul(tau, qn), 2))
        qnext = add(qnext, qm1, -1)

        Tch = ch_matrix(pnext, qnext, E)
        err = max_field_error(Tnext, Tch)
        assert err < 1e-11, (n + 1, err)

        rows.append((n + 1, d15(Tnext[1][1]), err))

        Tm1, Tn = Tn, Tnext
        pm1, pn = pn, pnext
        qm1, qn = qn, qnext

    print("FORMAL SPATIAL QUADRATURE = 0")
    print("Z6 M,B =", M, B)
    print("n,J22_exact,max_direct_vs_CH_coefficient_error")
    for row in rows:
        print("%d,%.15g,%.6g" % row)
    print("PASS")


if __name__ == "__main__":
    main()
