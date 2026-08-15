"""Exact symbolic reproduction of the NZ-SCCM classical elastic postbuckling limit gate.

No spatial numerical sampling or quadrature is used.
SymPy performs analytic differentiation, trigonometric reduction and exact integration.
"""
import sympy as sp

x,y,b,ell,A,A0,E,t,nu,N,Dp = sp.symbols(
    'x y b ell A A0 E t nu N Dp', positive=True
)
alpha=sp.pi/b
beta=sp.pi/ell
phi=sp.sin(alpha*x)*sp.sin(beta*y)
w0=A0*phi
wa=A*phi
wt=(A0+A)*phi
S=A*(A+2*A0)

def detcurv(w):
    return sp.diff(w,x,2)*sp.diff(w,y,2)-sp.diff(w,x,y)**2

def lap(f):
    return sp.diff(f,x,2)+sp.diff(f,y,2)

def bracket(F,w):
    return (sp.diff(F,y,2)*sp.diff(w,x,2)
            +sp.diff(F,x,2)*sp.diff(w,y,2)
            -2*sp.diff(F,x,y)*sp.diff(w,x,y))

source=sp.trigsimp(sp.expand_trig(detcurv(wt)-detcurv(w0)))
source_expected=-S*alpha**2*beta**2/2*(sp.cos(2*alpha*x)+sp.cos(2*beta*y))
assert sp.simplify(source-source_expected)==0

C20=E*t*S*beta**2/(32*alpha**2)
C02=E*t*S*alpha**2/(32*beta**2)
Fp=C20*sp.cos(2*alpha*x)+C02*sp.cos(2*beta*y)
assert sp.simplify(lap(lap(Fp)) + E*t*source)==0

Fh=-N*x**2/2
F=Fh+Fp
Ny=sp.simplify(sp.diff(F,x,2))
Nx=sp.simplify(sp.diff(F,y,2))

I0=sp.integrate(sp.integrate(phi**2,(x,0,b)),(y,0,ell))
I20=sp.integrate(sp.integrate(phi**2*sp.cos(2*alpha*x),(x,0,b)),(y,0,ell))
I02=sp.integrate(sp.integrate(phi**2*sp.cos(2*beta*y),(x,0,b)),(y,0,ell))
assert sp.simplify(I0-b*ell/4)==0
assert sp.simplify(I20+b*ell/8)==0
assert sp.simplify(I02+b*ell/8)==0

lhs=Dp*lap(lap(wa))
rhs=bracket(F,wt)
GL=sp.integrate(sp.integrate(phi*lhs,(x,0,b)),(y,0,ell))
GR=sp.integrate(sp.integrate(phi*rhs,(x,0,b)),(y,0,ell))
Nsol=sp.factor(sp.solve(sp.Eq(GL,GR),N)[0])
Ncr=Dp*(alpha**2+beta**2)**2/beta**2
Nexpected=sp.simplify(Ncr*A/(A+A0) + E*t*S/16*(beta**2+alpha**4/beta**2))
assert sp.simplify(Nsol-Nexpected)==0

chi=sp.symbols('chi', positive=True)
kcr=sp.simplify((1+chi**2)**2/chi**2)
kp=sp.simplify(sp.Rational(3,4)*(chi**2+chi**-2))

# Square representative halfwave chi=1, perfect plate.
ratio_square_perfect=sp.simplify(1+sp.Rational(3,8)*(1-nu**2)*(A/t)**2)

dN_dA=sp.simplify(sp.diff(Nexpected,A))

print('compatibility_source =', source_expected)
print('C20 =', C20)
print('C02 =', C02)
print('Ny =', Ny)
print('Nx =', Nx)
print('I0,I20,I02 =', I0,I20,I02)
print('Ncr =', sp.factor(Ncr))
print('N(A,A0) =', sp.factor(Nexpected))
print('kcr(chi) =', kcr)
print('kp(chi) =', kp)
print('square perfect sigma/sigma_cr =', ratio_square_perfect)
print('dN/dA =', sp.factor(dN_dA))
print('formal spatial sampling/quadrature = 0')
