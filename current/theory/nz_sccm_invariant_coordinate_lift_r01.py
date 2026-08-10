"""Exact symbolic checks for NZ-SCCM invariant-coordinate lift R01.

No spatial quadrature is used.  The script verifies:
1) I1 is affine in z;
2) z -> s=I1 inverse/Jacobian;
3) I2 becomes quadratic in s exactly;
4) Saenz-type rational primitive differentiates exactly.
"""
from __future__ import annotations
import sympy as sp

u,v,z,D,M,B,nu,s,kappa,a = sp.symbols(
    "u v z D M B nu s kappa a", positive=True
)

H = u**2 + v**2 - 2*u**2*v**2
K = nu*u**2 - v**2 + (1-nu)*u**2*v**2
W = u*v*z

I1 = (nu-1)*D + M*H + 2*B*W
I2 = (
    -nu*D**2 + D*M*K + B*D*(nu-1)*W
    + B*M*W*(2-u**2-v**2)
    + B**2*z**2*(u**2+v**2-1)
)

abase = (nu-1)*D + M*H
z_of_s = (s-abase)/(2*B*u*v)

I2_s_expected = (
    -nu*D**2 + D*M*K
    + D*(nu-1)*(s-abase)/2
    + M*(2-u**2-v**2)*(s-abase)/2
    + (u**2+v**2-1)*(s-abase)**2/(4*u**2*v**2)
)

assert sp.simplify(I1.subs(z,z_of_s)-s) == 0
assert sp.simplify(I2.subs(z,z_of_s)-I2_s_expected) == 0
assert sp.simplify(sp.diff(I1,z)-2*B*u*v) == 0
assert sp.Poly(sp.together(I2_s_expected),s).degree() == 2

# Saenz-type rational primitive check
Delta = 4-a**2
R = kappa*s/(1+a*s+s**2)
primitive = (
    kappa*sp.log(s**2+a*s+1)/2
    - kappa*a/sp.sqrt(Delta)*sp.atan((2*s+a)/sp.sqrt(Delta))
)
assert sp.simplify(sp.diff(primitive,s)-R) == 0

print("PASS: exact invariant-coordinate identities")
