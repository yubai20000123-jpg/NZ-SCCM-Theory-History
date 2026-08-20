"""
NC-M6 exact thickness integration engine V5
Zero formal spatial quadrature. No Case21 inputs are hard-coded.

Purpose:
1) preserve the frozen NC-M6 tension decimal coefficients exactly as decimal rationals;
2) provide the quadratic-extension pair algebra Z=A+B*R, R**2=Q;
3) provide the Euler rationalization map for R=sqrt(Q2*zeta**2+Q1*zeta+Q0);
4) integrate the resulting rational function exactly with SymPy ratint when instantiated.

This engine does NOT evaluate the remaining 2D relative GKZ/Aomoto periods.
"""
from __future__ import annotations
import sympy as sp
from dataclasses import dataclass

zeta, omega = sp.symbols("zeta omega")
Q0, Q1, Q2 = sp.symbols("Q0 Q1 Q2", nonzero=True)
Q = Q2*zeta**2 + Q1*zeta + Q0

r = sp.symbols("r")
T1 = r
chi = (r - sp.Rational(7,10))/sp.Rational(4,5)
T2 = (
    sp.Rational(7,10)
    + sp.Rational(4,5)*chi
    - sp.Rational(194,100)*chi**3
    + sp.Rational(204777777778,100000000000)*chi**4
    - sp.Rational(646666666667,1000000000000)*chi**5
)
T3 = 1 - sp.Rational(7,90)*(r-1)
psi = (r-9)/2
T4 = (
    sp.Rational(377777777778,10**12)
    - sp.Rational(155555555556,10**12)*psi
    + sp.Rational(155555555556,10**12)*psi**3
    - sp.Rational(777777777778,10**13)*psi**4
)
T5 = sp.Rational(3,10)
T_BRANCHES = tuple(sp.expand(T) for T in (T1,T2,T3,T4,T5))

@dataclass(frozen=True)
class Pair:
    a: sp.Expr
    b: sp.Expr

def p_add(x: Pair, y: Pair) -> Pair:
    return Pair(x.a+y.a, x.b+y.b)

def p_sub(x: Pair, y: Pair) -> Pair:
    return Pair(x.a-y.a, x.b-y.b)

def p_mul(x: Pair, y: Pair) -> Pair:
    return Pair(x.a*y.a + x.b*y.b*Q, x.a*y.b + x.b*y.a)

def p_scale(x: Pair, c: sp.Expr) -> Pair:
    return Pair(c*x.a, c*x.b)

def p_pow(x: Pair, n: int) -> Pair:
    out = Pair(sp.Integer(1), sp.Integer(0))
    base = x
    while n:
        if n & 1:
            out = p_mul(out, base)
        n >>= 1
        if n:
            base = p_mul(base, base)
    return out

def poly_in_pair(poly: sp.Expr, x: Pair, symbol=r) -> Pair:
    P = sp.Poly(sp.expand(poly), symbol)
    out = Pair(sp.Integer(0), sp.Integer(0))
    for k in range(P.degree(), -1, -1):
        out = p_add(p_mul(out, x), Pair(P.nth(k), 0))
    return out

def compression_pair(c: Pair, kappa: sp.Expr) -> Pair:
    d0 = 1 + (kappa-2)*c.a + c.a**2 + c.b**2*Q
    d1 = c.b*(kappa-2 + 2*c.a)
    den = d0**2 - d1**2*Q
    return Pair(
        sp.factor(kappa*(c.a*d0 - c.b*d1*Q)/den),
        sp.factor(kappa*(c.b*d0 - c.a*d1)/den),
    )

def euler_map():
    den = 2*sp.sqrt(Q2)*omega + Q1
    z = (omega**2-Q0)/den
    Rw = (
        sp.sqrt(Q2)*omega**2 + Q1*omega + sp.sqrt(Q2)*Q0
    )/den
    dz = sp.diff(z, omega)
    return z, Rw, dz

def euler_rationalize(kernel: Pair) -> sp.Expr:
    z, Rw, dz = euler_map()
    expr = (kernel.a.subs(zeta,z) + kernel.b.subs(zeta,z)*Rw)*dz
    return sp.together(expr)

def exact_rational_primitive(kernel: Pair) -> sp.Expr:
    rat = euler_rationalize(kernel)
    return sp.integrals.rationaltools.ratint(rat, omega)

def validate_euler_identity():
    z, Rw, dz = euler_map()
    identity = sp.factor(Rw**2 - (Q2*z**2 + Q1*z + Q0))
    return sp.simplify(identity) == 0

if __name__ == "__main__":
    print("T degrees:", [sp.Poly(T,r).degree() for T in T_BRANCHES])
    print("Euler identity:", validate_euler_identity())
