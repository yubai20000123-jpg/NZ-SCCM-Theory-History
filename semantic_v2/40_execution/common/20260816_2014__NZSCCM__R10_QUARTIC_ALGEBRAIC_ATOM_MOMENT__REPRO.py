"""NZ-SCCM fixed algebraic atom -> scalar quartic / special-function moment gate.

Formal structural spatial/thickness numerical integration remains ZERO.
The mpmath quadrature below is audit-only for a 1D special-function identity and is
NOT a structural production integral.  The generic 2x2 thickness probe calls SymPy
symbolic integrate only and accepts unevaluated output as an implementation boundary.
"""
import sympy as sp
import mpmath as mp

RHO = sp.Rational(1,10)

# -----------------------------------------------------------------------------
# 1. Smooth split algebraic reduction
# -----------------------------------------------------------------------------
x, eta = sp.symbols('x eta', real=True, nonzero=True)
R = sp.sqrt(x*x + eta*eta)
pi_p = x*x*(R+x)/(2*(x*x+eta*eta))
pi_m = x*x*(R-x)/(2*(x*x+eta*eta))
ID_SUM = sp.simplify(pi_p + pi_m - x*x/R)
ID_DIFF = sp.simplify(pi_p - pi_m - x**3/(x*x+eta*eta))

# -----------------------------------------------------------------------------
# 2. Universal dimensionless spline-knot thresholds
# eta = a/20, x=a*u, t/a = tau(u)
# -----------------------------------------------------------------------------
u, m = sp.symbols('u m', positive=True, real=True)
tau = u*u*(sp.sqrt(u*u+sp.Rational(1,400))+u)/(2*(u*u+sp.Rational(1,400)))
P_KNOT = sp.expand(160000*m*u**5 + (100-160000*m**2)*u**4 + 400*m*u**3 - 800*m**2*u**2 - m**2)

mp.mp.dps = 80
def tau_mp(uu):
    uu=mp.mpf(uu)
    return uu*uu*(mp.sqrt(uu*uu+mp.mpf(1)/400)+uu)/(2*(uu*uu+mp.mpf(1)/400))
U1 = mp.findroot(lambda uu: tau_mp(uu)-1, 1)
U10 = mp.findroot(lambda uu: tau_mp(uu)-10, 10)

# -----------------------------------------------------------------------------
# 3. One-scalar quartic representation of sqrt(E^2+eta^2 I)
# For E^2 - T E + D I = 0, s = tr sqrt(E^2+eta^2 I)
# -----------------------------------------------------------------------------
T,D,s = sp.symbols('T D s', real=True)
ee = sp.symbols('ee', positive=True, real=True)
p = T**2 - 2*D + 2*ee**2
q = D**2 + ee**2*(T**2-2*D) + ee**4
P_S = sp.expand(s**4 - 2*p*s**2 + T**2*(T**2-4*D))
DET_DISC_ID = sp.factor(p**2 - 4*q - T**2*(T**2-4*D))
a = (s**2-T**2)/(2*s)
b = T/s
COEFF_E_RES = sp.simplify(2*a*b + b*b*T - T)
COEFF_I_RES = sp.factor(a*a - b*b*D - (ee**2-D))
COEFF_I_MOD = sp.simplify(COEFF_I_RES - P_S/(4*s**2))

Tp,Dp = sp.symbols('Tp Dp', real=True)
pp = sp.diff(p,T)*Tp + sp.diff(p,D)*Dp
rr = sp.diff(T**2*(T**2-4*D),T)*Tp + sp.diff(T**2*(T**2-4*D),D)*Dp
S_DERIV = sp.factor((pp*s**2-sp.Rational(1,2)*rr)/(2*s*(s**2-p)))

tau_s,delta,sk=sp.symbols('tau delta sk', real=True)
KNOT_QUARTIC = sp.expand(sk**4-2*(tau_s**2-2*delta)*sk**2+tau_s**2*(tau_s**2-4*delta))
KNOT_QUARTIC_FACTORED = sp.factor(KNOT_QUARTIC)

# -----------------------------------------------------------------------------
# 4. Exact affine-thickness recurrence J_n = int y^n/sqrt(y^2+eta^2) dy
# -----------------------------------------------------------------------------
y = sp.symbols('y', real=True)
R_y = sp.sqrt(y*y+ee*ee)
J = {0: sp.asinh(y/ee), 1: R_y}
REC_RES = {}
for n in range(2,7):
    J[n] = sp.simplify(y**(n-1)*R_y/sp.Integer(n) - sp.Rational(n-1,n)*ee**2*J[n-2])
    REC_RES[n] = sp.simplify(sp.diff(J[n],y) - y**n/R_y)

# -----------------------------------------------------------------------------
# 5. Exact one-harmonic D15/Appell-F1 prototype
# -----------------------------------------------------------------------------
def I_quad(n,A,B,e):
    f=lambda X: mp.sin(X)**(2*n)/mp.sqrt((A+B*mp.sin(X)**2)**2+e**2)
    # audit only, not production
    return mp.quad(f,[0,mp.pi/2,mp.pi])

def I_appell(n,A,B,e):
    alpha=mp.mpf(n)+mp.mpf('0.5')
    gamma=mp.mpf(n)+1
    z1=-B/(A+1j*e)
    z2=-B/(A-1j*e)
    return mp.beta(alpha,mp.mpf('0.5'))/mp.sqrt(A*A+e*e)*mp.appellf1(
        alpha,mp.mpf('0.5'),mp.mpf('0.5'),gamma,z1,z2)

APPELL_ERR={}
for n in (0,1,2):
    A=mp.mpf('0.3'); B=mp.mpf('0.7'); ev=mp.mpf('0.05')
    v1=I_quad(n,A,B,ev); v2=I_appell(n,A,B,ev)
    APPELL_ERR[n]=abs(v1-v2)

# -----------------------------------------------------------------------------
# 6. Generic non-commuting affine 2x2 thickness CAS probe
# -----------------------------------------------------------------------------
z=sp.symbols('z', real=True)
eta0=sp.Rational(1,20)
E=sp.Matrix([
    [sp.Rational(1,5)+z/sp.Integer(3), sp.Rational(1,7)+z/sp.Integer(5)],
    [sp.Rational(1,7)+z/sp.Integer(5), -sp.Rational(1,4)+2*z/sp.Integer(7)]
])
A2=sp.expand(E*E)+eta0**2*sp.eye(2)
pz=sp.factor(sp.trace(A2)); qz=sp.factor(A2.det())
sz=sp.sqrt(pz+2*sp.sqrt(qz))
CAS_GENERIC=sp.integrate(sz,(z,-1,1),risch=False)
CAS_UNEVALUATED = bool(CAS_GENERIC.has(sp.Integral))

print('FORMAL STRUCTURAL COUNTERS: sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0')
print('SMOOTH_SPLIT_SUM_RESIDUAL =', ID_SUM)
print('SMOOTH_SPLIT_DIFF_RESIDUAL =', ID_DIFF)
print('KNOT_POLYNOMIAL =', P_KNOT)
print('u1 =', mp.nstr(U1,70))
print('u10 =', mp.nstr(U10,70))
print('tau(u1)-1 =', mp.nstr(tau_mp(U1)-1,10))
print('tau(u10)-10 =', mp.nstr(tau_mp(U10)-10,10))
print('TRACE_SQRT_QUARTIC =', P_S)
print('DET_DISCRIMINANT_RESIDUAL =', DET_DISC_ID)
print('MATRIX_SQRT_E_COEFF_RESIDUAL =', COEFF_E_RES)
print('MATRIX_SQRT_I_COEFF_MINUS_QUARTIC =', COEFF_I_MOD)
print('QUARTIC_ATOM_FORMAL_DERIVATIVE =', S_DERIV)
print('KNOT_QUARTIC_FACTORIZATION =', KNOT_QUARTIC_FACTORED)
print('FIXED_ALGEBRAIC_FIELD_DEGREE_UPPER_BOUND = 64')
print('AFFINE_THICKNESS_RECURRENCE_RESIDUALS =', REC_RES)
print('APPELL_F1_AUDIT_ERRORS =', {k: mp.nstr(v,12) for k,v in APPELL_ERR.items()})
print('GENERIC_2X2_p(z) =', pz)
print('GENERIC_2X2_q_degree =', sp.Poly(qz,z).degree())
print('GENERIC_2X2_DIRECT_CAS_UNEVALUATED =', CAS_UNEVALUATED)
print('GENERIC_2X2_DIRECT_CAS_RESULT =', CAS_GENERIC)
print('NEW_Pu = NOT_RUN')
