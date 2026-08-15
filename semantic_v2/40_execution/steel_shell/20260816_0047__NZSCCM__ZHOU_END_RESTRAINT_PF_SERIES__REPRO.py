"""NZ-SCCM 20260816_0047 PF end-restraint exact-moment reproducer.

This script performs NO spatial numerical integration and NO spatial sampling.
It uses only:
- coefficient-space complex root solving for sin(2 lambda)+2 lambda=0;
- closed analytical cosine/hyperbolic moments;
- finite linear algebra in coefficient space.

It reproduces the roots, N=6 PF coefficients, omitted exact moments, and
finite-panel center factors recorded in the corresponding JSON artifact.
"""

import mpmath as mp

mp.mp.dps = 60
PI = mp.pi

ROOT_GUESSES = [
    2.1 + 1.1j,
    5.35 + 1.55j,
    8.54 + 1.78j,
    11.70 + 1.93j,
    14.85 + 2.05j,
    18.00 + 2.14j,
]


def even_roots(nmax=6):
    roots = []
    for g in ROOT_GUESSES[:nmax]:
        lam = mp.findroot(lambda z: mp.sin(2*z) + 2*z, g)
        roots.append(lam)
    return roots


def sinc_unscaled(q):
    """sin(q)/q, analytic limit 1 at q=0."""
    if abs(q) < mp.mpf("1e-40"):
        return mp.mpf(1)
    return mp.sin(q)/q


def dsinc_unscaled(q):
    """d[sin(q)/q]/dq, analytic limit 0 at q=0."""
    if abs(q) < mp.mpf("1e-30"):
        return -q/3 + q**3/30
    return (q*mp.cos(q) - mp.sin(q))/q**2


def Icos(lam, k):
    """Exact integral int_-1^1 cos(lam t) cos(k pi t) dt."""
    kp = k*PI
    return sinc_unscaled(lam-kp) + sinc_unscaled(lam+kp)


def dIcos_dlambda(lam, k):
    kp = k*PI
    return dsinc_unscaled(lam-kp) + dsinc_unscaled(lam+kp)


def F_moment(lam, k):
    # F=sin(lam)cos(lam t)-t cos(lam)sin(lam t)
    # int t sin(lam t) cos(k pi t) dt = -dI/dlam
    return mp.sin(lam)*Icos(lam, k) + mp.cos(lam)*dIcos_dlambda(lam, k)


def B_moment(lam, k, nu):
    # B=(1+nu)lam^2 F + 2 nu lam cos(lam) cos(lam t)
    return ((1+nu)*lam**2*F_moment(lam, k)
            + 2*nu*lam*mp.cos(lam)*Icos(lam, k))


def C_hyperbolic(z, k):
    """Exact int_-1^1 cosh(z t) cos(k pi t) dt."""
    r = k*PI
    return 2*((-1)**k)*z*mp.sinh(z)/(z**2+r**2)


def T_hyperbolic(z, k):
    """Exact int_-1^1 z t sinh(z t) cos(k pi t) dt."""
    r = k*PI
    den = z**2 + r**2
    num_deriv = (mp.sinh(z) + z*mp.cosh(z))*den - 2*z**2*mp.sinh(z)
    dC = 2*((-1)**k)*num_deriv/den**2
    return z*dC


def H_moment(k, chi, nu):
    """Exact cosine moment of the inherited 00:16 end residual H(t)."""
    z = PI*chi
    den = z + mp.sinh(z)*mp.cosh(z)
    Az = (z*mp.cosh(z) + mp.sinh(z))/den
    Bz = mp.sinh(z)/den
    Cg = -Az*(1+nu) + 2*nu*Bz

    const_moment = mp.mpf(2) if k == 0 else mp.mpf(0)
    cos_pi_moment = mp.mpf(1) if k == 1 else mp.mpf(0)

    return (-chi**2*(const_moment
                      + Cg*C_hyperbolic(z, k)
                      + Bz*(1+nu)*T_hyperbolic(z, k))
            - nu*chi**4*cos_pi_moment)


def solve_coefficients(roots, N, chi, nu):
    """Solve 2N exact cosine moment equations for N complex amplitudes."""
    M = mp.matrix(2*N, 2*N)
    rhs = mp.matrix(2*N, 1)

    for k in range(2*N):
        rhs[k] = -H_moment(k, chi, nu)
        for j in range(N):
            mb = B_moment(roots[j], k, nu)
            # Re[(u+i v)(p+i q)] = u p - v q
            M[k, 2*j] = mp.re(mb)
            M[k, 2*j+1] = -mp.im(mb)

    sol = mp.lu_solve(M, rhs)
    return [mp.mpc(sol[2*j], sol[2*j+1]) for j in range(N)]


def residual_moment(k, roots, coeffs, chi, nu):
    r = H_moment(k, chi, nu)
    for lam, a in zip(roots[:len(coeffs)], coeffs):
        r += mp.re(a*B_moment(lam, k, nu))
    return r


def convergence(roots, N, chi, nu, kmax=24):
    coeffs = solve_coefficients(roots, N, chi, nu)
    vals = [abs(residual_moment(k, roots, coeffs, chi, nu))
            for k in range(kmax+1)]
    enforced = max(vals[:2*N])
    omitted = max(vals[2*N:]) if 2*N <= kmax else mp.mpf(0)
    Hmax = max(abs(H_moment(k, chi, nu)) for k in range(kmax+1))
    return coeffs, enforced, omitted, omitted/Hmax, Hmax


def center_factors(roots, physical_a_over_b):
    # Y_n(a/2)=1/cosh(lambda_n*a/b)
    return [1/mp.cosh(lam*physical_a_over_b) for lam in roots]


def show_complex(label, values):
    print(label)
    for i, z in enumerate(values, 1):
        print(i, mp.nstr(mp.re(z), 18), mp.nstr(mp.im(z), 18))


def main():
    roots = even_roots(6)
    show_complex("EVEN ROOTS", roots)

    cases = [
        ("original_Z6_nu018", mp.mpf(4)/3, mp.mpf("0.18")),
        ("original_Z6_nu030", mp.mpf(4)/3, mp.mpf("0.30")),
        ("AR2_nu018", mp.mpf(1), mp.mpf("0.18")),
        ("AR2_nu030", mp.mpf(1), mp.mpf("0.30")),
    ]

    for name, chi, nu in cases:
        coeffs = solve_coefficients(roots, 6, chi, nu)
        show_complex("COEFFS " + name, coeffs)

    for name, chi in [("original_Z6", mp.mpf(4)/3), ("AR2", mp.mpf(1))]:
        print("CONVERGENCE", name, "nu=.18")
        for N in range(2, 7):
            _, enf, omit, ratio, hmax = convergence(
                roots, N, chi, mp.mpf("0.18"), 24
            )
            print(N,
                  "enforced=", mp.nstr(enf, 8),
                  "omitted=", mp.nstr(omit, 14),
                  "ratio=", mp.nstr(ratio, 14),
                  "Hmax=", mp.nstr(hmax, 14))

    print("CENTER FACTORS original Z6 a/b=.75")
    for i, y in enumerate(center_factors(roots, mp.mpf("0.75")), 1):
        print(i, mp.nstr(abs(y), 16), mp.nstr(y, 18))

    print("CENTER FACTORS AR2 a/b=2")
    for i, y in enumerate(center_factors(roots, mp.mpf("2")), 1):
        print(i, mp.nstr(abs(y), 16), mp.nstr(y, 18))

    print("FORMAL SPATIAL SAMPLING = 0")
    print("FORMAL SPATIAL QUADRATURE = 0")
    print("FORMAL SPATIAL SUBDOMAINS = 1")


if __name__ == "__main__":
    main()
