from __future__ import annotations

# Symbolic audit only: proves that the exact GL augmentation of the frozen R02
# condensed energy remains a cubic stationarity equation in U and degenerates
# exactly to the frozen depressed cubic when GL coefficients vanish.

import sympy as sp

U,a,W,W0 = sp.symbols('U a W W0')
ex,ey,gamma = sp.symbols('ex ey gamma')
cx,cy,hx,hy,hg = sp.symbols('cx cy hx hy hg')
t,Q,nu,G,Kb,E = sp.symbols('t Q nu G Kb E')
KA,Kd,Kgg = sp.symbols('KA Kd Kgg')

d = U**2-a**2
Delta = W*U-W0*a
mx = ex-cx*d-hx*Delta
my = ey-cy*d-hy*Delta
mg = gamma-hg*Delta

Pi = (
    sp.Rational(1,2)*Kb*(U-a)**2
    +sp.Rational(1,2)*t*Q*(mx**2+my**2+2*nu*mx*my)
    +sp.Rational(1,2)*t*G*mg**2
    +t*E*(KA*d**2+2*Kd*d*Delta+Kgg*Delta**2)
)

RU = sp.expand(sp.diff(Pi,U))
poly = sp.Poly(RU,U)
assert poly.degree() == 3
B3,B2,B1,B0 = [sp.factor(c) for c in poly.all_coeffs()]

Ccc = Q*(cx**2+2*nu*cx*cy+cy**2)
Cch = Q*(cx*hx+nu*cx*hy+nu*cy*hx+cy*hy)
Chh = Q*(hx**2+2*nu*hx*hy+hy**2)+G*hg**2
Lc = Q*(cx*(ex+nu*ey)+cy*(ey+nu*ex))
Lh = Q*(hx*(ex+nu*ey)+hy*(ey+nu*ex))+G*gamma*hg

B3_expected = 2*t*(2*E*KA+Ccc)
B2_expected = 3*W*t*(2*E*Kd+Cch)
B1_expected = (Kb-B3_expected*a**2
               -2*a*W0*t*(2*E*Kd+Cch)
               +W**2*t*(2*E*Kgg+Chh)
               -2*t*Lc)
B0_expected = (-a*Kb
               -a**2*W*t*(2*E*Kd+Cch)
               -a*W*W0*t*(2*E*Kgg+Chh)
               -W*t*Lh)

for actual,expected in ((B3,B3_expected),(B2,B2_expected),(B1,B1_expected),(B0,B0_expected)):
    assert sp.simplify(actual-expected) == 0

# Frozen R02 degeneration.
subs_off = {hx:0,hy:0,hg:0,Kd:0,Kgg:0,gamma:0}
B3_old = sp.simplify(B3_expected.subs(subs_off))
B2_old = sp.simplify(B2_expected.subs(subs_off))
B1_old = sp.simplify(B1_expected.subs(subs_off))
B0_old = sp.simplify(B0_expected.subs(subs_off))

assert B2_old == 0
assert sp.simplify(B3_old-(4*t*E*KA+2*t*Ccc.subs(subs_off))) == 0
assert sp.simplify(B1_old-(Kb-B3_old*a**2-2*t*Lc.subs(subs_off))) == 0
assert sp.simplify(B0_old+Kb*a) == 0

if __name__ == '__main__':
    print('R02_GL_CUBIC_DEGREE =',poly.degree())
    print('B3 =',B3_expected)
    print('B2 =',B2_expected)
    print('B1 =',B1_expected)
    print('B0 =',B0_expected)
    print('GL_OFF_R02_DEGENERATION = PASS')
