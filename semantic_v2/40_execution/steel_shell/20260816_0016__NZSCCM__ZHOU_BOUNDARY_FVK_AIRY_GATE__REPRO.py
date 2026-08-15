"""NZ-SCCM Zhou-boundary classical FvK/Airy gate reproducer.

No structural spatial numerical quadrature/sampling is used.
All integrations in this file are exact SymPy integrations or closed formulas.
This file does NOT calculate a nonlinear-material Z6 Pu.
"""
import sympy as sp

# -----------------------------------------------------------------------------
# 1. Exact side-free biharmonic correction
# -----------------------------------------------------------------------------
z, s, chi, nu = sp.symbols('z s chi nu', positive=True, real=True)
den = z + sp.sinh(z)*sp.cosh(z)
G = 1 - (z*sp.cosh(z)+sp.sinh(z))/den*sp.cosh(s) \
      + sp.sinh(z)/den*s*sp.sinh(s)
Gp = sp.diff(G, s)
Gpp = sp.simplify(sp.diff(G, s, 2))

assert sp.simplify(G.subs(s, z)) == 0
assert sp.simplify(G.subs(s, -z)) == 0
assert sp.simplify(Gp.subs(s, z)) == 0
assert sp.simplify(Gp.subs(s, -z)) == 0

G0 = sp.simplify(G.subs(s, 0))
Gpp0 = sp.simplify(Gpp.subs(s, 0))
Gppz = sp.simplify(Gpp.subs(s, z))

# Exact integrated side-correction diagnostic.  This is a closed formula;
# no numerical spatial quadrature is used.
J_closed = sp.simplify(
    2*(
        z**3 + z**2*sp.sinh(2*z)
        + z*sp.Rational(1,4)*(sp.cosh(2*z)-1)**2
        - z*sp.Rational(1,2)*sp.cosh(2*z) + z*sp.Rational(1,2)
        + sp.Rational(1,2)*sp.sinh(2*z)
        - sp.Rational(1,4)*sp.sinh(4*z)
    )/(z+sp.Rational(1,2)*sp.sinh(2*z))**2
)

# Optional exact symbolic cross-check of the closed J expression.
J_symbolic = sp.simplify(sp.integrate(G**2 + Gpp**2 + 2*Gp**2, (s, -z, z)))
assert sp.simplify(sp.trigsimp(J_symbolic-J_closed)) == 0

# -----------------------------------------------------------------------------
# 2. Loaded-end ux=0 compatibility residual after side traction correction
# -----------------------------------------------------------------------------
# Normalize by 4*alpha^2*C02 and remove the one spatial constant that can be
# supplied by the mean axial resultant N:
# H(X) = -chi^2*(G + nu*G'') + nu*chi^4*cos(2X)
X = sp.symbols('X', real=True)
H = -chi**2*(G + nu*Gpp) + nu*chi**4*sp.cos(2*X)

# x=0 -> X=0, s=-z; x=b/2 -> X=pi/2, s=0.
H_side = sp.simplify(H.subs({X:0, s:-z}))
H_center = sp.simplify(H.subs({X:sp.pi/2, s:0}))

# -----------------------------------------------------------------------------
# 3. Exact finite Ritz diagnostic satisfying the essential loaded-end u=0 BC
# -----------------------------------------------------------------------------
r0, r2, s2 = sp.symbols('r0 r2 s2', real=True)
Y = sp.symbols('Y', real=True)

# Set alpha=1 and beta=chi for dimensionless exact energy integration.
ex = sp.Rational(1,4)*((1-r0)+(1-r2)*sp.cos(2*X))*sp.sin(Y)**2
ey = chi**2*sp.Rational(1,4)*(1+(1-s2)*sp.cos(2*Y))*sp.sin(X)**2
gxy = chi*sp.Rational(1,4)*(
    (1-(r2+s2)/2)*sp.sin(2*X)-r0*(X-sp.pi/2)
)*sp.sin(2*Y)

energy_density = (
    ex**2 + ey**2 + 2*nu*ex*ey + (1-nu)*sp.Rational(1,2)*gxy**2
)
I = sp.simplify(sp.integrate(sp.integrate(
    sp.expand_trig(energy_density), (X,0,sp.pi)), (Y,0,sp.pi)))

stationarity = [sp.diff(I,v) for v in (r0,r2,s2)]
ritz_sol = sp.solve(stationarity, (r0,r2,s2), dict=True, simplify=False)[0]
Imin = sp.simplify(I.subs(ritz_sol))
# For a perfect plate, kp = 96 Imin / [(1-nu^2) chi^2 pi^2].
kp_trial = sp.simplify(96*Imin/((1-nu**2)*chi**2*sp.pi**2))


def eval_case(chi_value, nu_value):
    zz = sp.pi*sp.Rational(chi_value) if isinstance(chi_value, int) else sp.pi*chi_value
    vals = {chi:chi_value, nu:nu_value, z:zz}
    return {
        'chi': float(sp.N(chi_value,16)),
        'nu': float(sp.N(nu_value,16)),
        'z': float(sp.N(zz,16)),
        'G0': float(sp.N(G0.subs(z,zz),16)),
        'Gpp0': float(sp.N(Gpp0.subs(z,zz),16)),
        'Gpp_side': float(sp.N(Gppz.subs(z,zz),16)),
        'J': float(sp.N(J_closed.subs(z,zz),16)),
        'H_side': float(sp.N(H_side.subs(vals),16)),
        'H_center': float(sp.N(H_center.subs(vals),16)),
        'H_difference': float(sp.N((H_side-H_center).subs(vals),16)),
        'r0': float(sp.N(ritz_sol[r0].subs({chi:chi_value,nu:nu_value}),16)),
        'r2': float(sp.N(ritz_sol[r2].subs({chi:chi_value,nu:nu_value}),16)),
        's2': float(sp.N(ritz_sol[s2].subs({chi:chi_value,nu:nu_value}),16)),
        'kp_trial_positive': float(sp.N(kp_trial.subs({chi:chi_value,nu:nu_value}),16)),
    }


if __name__ == '__main__':
    print('SIDE_FREE_BIHARMONIC_BOUNDARY_CHECK = PASS')
    print('G(z)=', sp.simplify(G.subs(s,z)), 'Gprime(z)=', sp.simplify(Gp.subs(s,z)))
    print('J symbolic closed-form check = PASS')
    for ch,nv in [
        (sp.Integer(1), sp.Rational(18,100)),
        (sp.Rational(4,3), sp.Rational(18,100)),
        (sp.Rational(4,3), sp.Rational(3,10)),
    ]:
        print(eval_case(ch,nv))
    print('Expected original-Z6 nu=.18 H side-center difference > 0 -> loaded-end residual is nonconstant.')
    print('EXACT_ZHOU_MIXED_BOUNDARY_AIRY_CLOSURE = OPEN')
    print('ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS')
    print('NEW_Z6_Pu = NOT_CALCULATED')
