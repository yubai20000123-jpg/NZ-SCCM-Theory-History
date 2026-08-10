"""
NZ-SCCM Case21 invariant / exact-moment audit V1.

Purpose
-------
1. Verify the closed-form I1 and I2 identities against the frozen Case21
   normalized Nguyen second-order kinematics.
2. Provide a transparent exact monomial moment functional for fields written as
       sum c[a,b,h] * sin(X)^a * sin(Y)^b * zeta^h.
3. Verify several hand-calculation checksums used in the accompanying report.

This file performs symbolic algebra only.  It is NOT a spatial quadrature,
material-point grid, element integration, or production material model.
"""
from __future__ import annotations

import sympy as sp


# -----------------------------------------------------------------------------
# Symbols
# -----------------------------------------------------------------------------
D, nu = sp.symbols("D nu")
M, B = sp.symbols("M B")       # M=C_m(q), B=C_b(q)
Mq, Bq = sp.symbols("M_q B_q")
u, v, z = sp.symbols("u v z")  # u=sin X, v=sin Y, z=zeta


# -----------------------------------------------------------------------------
# Compact invariant blocks
# -----------------------------------------------------------------------------
H = u**2 + v**2 - 2*u**2*v**2
K = nu*u**2 - v**2 + (1-nu)*u**2*v**2
W = u*v*z

I1 = (nu-1)*D + M*H + 2*B*W
I2 = (
    -nu*D**2
    + D*M*K
    + B*D*(nu-1)*W
    + B*M*W*(2-u**2-v**2)
    + B**2*z**2*(u**2+v**2-1)
)

I1q = Mq*H + 2*Bq*W
I2q = (
    D*Mq*K
    + Bq*D*(nu-1)*W
    + (Bq*M+B*Mq)*W*(2-u**2-v**2)
    + 2*B*Bq*z**2*(u**2+v**2-1)
)

Xyy = -D + M*u**2*(1-v**2) + B*W
Gq = sp.expand(I1*I1q - I2q)  # X:X_q


# -----------------------------------------------------------------------------
# Direct verification from original e_x,e_y,g_xy
# -----------------------------------------------------------------------------
# Use independent cx,cy symbols first, then impose cx^2=1-u^2,
# cy^2=1-v^2.  On X,Y in [0,pi], u,v are nonnegative.
cx, cy = sp.symbols("c_x c_y")
ex = nu*D + M*cx**2*v**2 + B*u*v*z
ey = -D + M*u**2*cy**2 + B*u*v*z
hxy = M*u*cx*v*cy - B*cx*cy*z  # g_xy / 2

I1_direct = sp.expand(ex + ey)
I2_direct = sp.expand(ex*ey - hxy**2)

subs_trig = {cx**2: 1-u**2, cy**2: 1-v**2}

assert sp.expand(I1_direct.subs(subs_trig) - I1) == 0
assert sp.expand(I2_direct.subs(subs_trig) - I2) == 0


# -----------------------------------------------------------------------------
# Exact analytic monomial moments
# -----------------------------------------------------------------------------
def S(n: int):
    """Integral_0^pi sin(X)^n dX, exact."""
    n = int(n)
    return sp.sqrt(sp.pi) * sp.gamma(sp.Rational(n+1, 2)) / sp.gamma(sp.Rational(n+2, 2))


def Z(h: int):
    """Integral_-1^1 zeta^h dzeta, exact."""
    h = int(h)
    return sp.Integer(0) if h % 2 else sp.Rational(2, h+1)


def exact_moment(expr):
    """
    Exact integral over X,Y in [0,pi], zeta in [-1,1] for an expression
    polynomial in u=sin X, v=sin Y, z=zeta.
    """
    poly = sp.Poly(sp.expand(expr), u, v, z)
    out = sp.Integer(0)
    for (a, b, h), coeff in poly.terms():
        out += coeff * S(a) * S(b) * Z(h)
    return sp.simplify(out)


# -----------------------------------------------------------------------------
# Hand-calculation checksums
# -----------------------------------------------------------------------------
checks = {
    "JPA00": exact_moment(1),
    "JPB00": exact_moment(Xyy),
    "JqA00": exact_moment(I1q),
    "JqB00": exact_moment(Gq),
    "M_I1": exact_moment(I1),
    "M_I2": exact_moment(I2),
}

expected = {
    "JPA00": 2*sp.pi**2,
    "JPB00": sp.pi**2*(-2*D + M/sp.Integer(2)),
    "JqA00": sp.pi**2*Mq,
    "JqB00": sp.pi**2*(Mq*((nu-1)*D/sp.Integer(2) + 5*M/sp.Integer(8))
                          + sp.Rational(2, 3)*B*Bq),
    "M_I1": sp.pi**2*(2*(nu-1)*D + M),
    "M_I2": -sp.pi**2*D*(4*nu*D + (1-nu)*M)/sp.Integer(2),
}

for key in checks:
    assert sp.simplify(checks[key] - expected[key]) == 0, key


if __name__ == "__main__":
    print("I1 =", sp.factor(I1))
    print("I2 =", sp.factor(I2))
    print("All exact-moment checks passed.")
    for key, value in checks.items():
        print(f"{key} = {sp.factor(value)}")
