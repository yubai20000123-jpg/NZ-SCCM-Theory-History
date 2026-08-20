"""
NC-M6 universal parametric coefficient compiler V6
No material decimal constants are hard-coded.

Core idea:
- material curve coefficients are supplied as parameters;
- all expanded coefficients are generated from a universal rule;
- geometry/material derived parameters are computed symbolically;
- the exact-thickness quadratic-extension algebra is unchanged.

This file is intended as a universal compiler, not a Case-specific material database.
"""
from __future__ import annotations
from dataclasses import dataclass
import sympy as sp

r = sp.symbols("r")
zeta, omega = sp.symbols("zeta omega")
Q0, Q1, Q2 = sp.symbols("Q0 Q1 Q2")
Q = Q2*zeta**2 + Q1*zeta + Q0

@dataclass(frozen=True)
class LocalPolynomialSegment:
    """
    T(r) = sum_{n=0}^N c_n * xi^n, xi=(r-a)/h.
    a: left/shift coordinate
    h: normalization width/scale
    coeffs: (c_0,...,c_N)
    """
    a: sp.Expr
    h: sp.Expr
    coeffs: tuple[sp.Expr, ...]

def local_to_global_coefficients(seg: LocalPolynomialSegment) -> tuple[sp.Expr, ...]:
    """
    Universal coefficient rule:
      T(r)=sum_n c_n ((r-a)/h)^n = sum_m t_m r^m
      t_m = sum_{n=m}^N c_n * C(n,m) * (-a)^(n-m) / h^n.
    Returns (t_0,...,t_N).
    """
    N = len(seg.coeffs) - 1
    out = []
    for m in range(N + 1):
        tm = sp.Add(*[
            seg.coeffs[n] * sp.binomial(n, m) * (-seg.a)**(n-m) / seg.h**n
            for n in range(m, N + 1)
        ])
        out.append(sp.factor(tm))
    return tuple(out)

def segment_polynomial(seg: LocalPolynomialSegment) -> sp.Expr:
    t = local_to_global_coefficients(seg)
    return sp.expand(sum(t[m]*r**m for m in range(len(t))))

def derived_material_parameters(E0, fc, ft, eps_c0):
    kappa = sp.factor(E0*eps_c0/fc)
    rho = sp.factor(ft/fc)
    xcr = sp.factor(ft/(E0*eps_c0))
    return {"kappa": kappa, "rho": rho, "xcr": xcr}

@dataclass(frozen=True)
class Pair:
    """A+B*R in the quadratic extension R^2=Q."""
    a: sp.Expr
    b: sp.Expr

def p_add(x: Pair, y: Pair) -> Pair:
    return Pair(sp.expand(x.a+y.a), sp.expand(x.b+y.b))

def p_mul(x: Pair, y: Pair) -> Pair:
    return Pair(sp.expand(x.a*y.a + x.b*y.b*Q),
                sp.expand(x.a*y.b + x.b*y.a))

def p_pow(x: Pair, n: int) -> Pair:
    out = Pair(sp.Integer(1), sp.Integer(0))
    for _ in range(n):
        out = p_mul(out, x)
    return out

def polynomial_in_pair(global_coeffs: tuple[sp.Expr, ...], x: Pair) -> Pair:
    out = Pair(sp.Integer(0), sp.Integer(0))
    for m, tm in enumerate(global_coeffs):
        pm = p_pow(x, m)
        out = p_add(out, Pair(tm*pm.a, tm*pm.b))
    return out

def compression_pair(c: Pair, kappa: sp.Expr) -> Pair:
    d0 = 1 + (kappa-2)*c.a + c.a**2 + c.b**2*Q
    d1 = c.b*(kappa-2 + 2*c.a)
    den = sp.expand(d0**2 - d1**2*Q)
    return Pair(
        sp.factor(kappa*(c.a*d0 - c.b*d1*Q)/den),
        sp.factor(kappa*(c.b*d0 - c.a*d1)/den),
    )

def euler_map():
    den = 2*sp.sqrt(Q2)*omega + Q1
    z = (omega**2-Q0)/den
    Rw = (sp.sqrt(Q2)*omega**2 + Q1*omega + sp.sqrt(Q2)*Q0)/den
    dz = sp.diff(z, omega)
    return z, Rw, dz

def euler_rationalize(kernel: Pair) -> sp.Expr:
    z, Rw, dz = euler_map()
    expr = (kernel.a.subs(zeta,z) + kernel.b.subs(zeta,z)*Rw)*dz
    return sp.together(expr)

if __name__ == "__main__":
    a, h = sp.symbols("a h", nonzero=True)
    c0, c1, c2, c3, c4, c5 = sp.symbols("c0:6")
    seg = LocalPolynomialSegment(a, h, (c0,c1,c2,c3,c4,c5))
    print("Universal global coefficients:")
    for i, ti in enumerate(local_to_global_coefficients(seg)):
        print(f"t_{i} =", ti)
