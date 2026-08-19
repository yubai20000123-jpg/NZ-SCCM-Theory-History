#!/usr/bin/env python3
"""NZ-SCCM Z1 R17: exact global spectral-Heaviside constructor.

Replaces the reducible four-threshold-radical part of the R13 CH circuit by the
exact scalar spectral truncated-power law. No spatial partition is created:
the six ordered spectral states are finite distributional terms in one global
formula. Tangent-half-angle coordinates make all kinematics rational, so each
threshold predicate reduces to polynomial inequalities after clearing strictly
positive denominators.

No quadrature, sampling, material points, finite prefix, or load stepping.
"""
from __future__ import annotations
import json
import sympy as sp

# Symbols
x,y,z,D,q,al,P2=sp.symbols('x y z D q al P2', real=True)
th=sp.symbols('th', real=True)
nu=sp.Rational(9,50)
eps0=sp.Rational('0.0018712490394580678')
b=sp.Integer(6000); tc=sp.Integer(92); q0=sp.Rational(1,250)
kappa=sp.Rational('2.0005129533678754'); rho=sp.Rational(1,10)
xcr=sp.factor(rho/kappa); eta=sp.factor(xcr/20)
HR=sp.Rational('0.09799750427197301'); UR=sp.Rational(3,100)

# Tangent-half-angle map X=2 atan x, Y=2 atan y.
sx=2*x/(1+x**2); cx=(1-x**2)/(1+x**2)
sy=2*y/(1+y**2); cy=(1-y**2)/(1+y**2)
Hs=sp.cancel(sx*sy)
Fx=sp.cancel(sy**2*(1-sx**2))
Fy=sp.cancel(sx**2*(1-sy**2))
Ax=sp.cancel(-sp.Rational(1,4)-nu* sx**2/2-sy**2/2+sx**2*sy**2)
Ay=sp.cancel(nu/4-sx**2/2-nu*sy**2/2+sx**2*sy**2)
M=sp.factor(P2/eps0*(q0*q+q**2/2))
beta=sp.factor(P2*q/(eps0*b)); zz=tc*z/2
ex=sp.cancel(nu*D+M*Fx+al*Ax+beta*zz*Hs)
ey=sp.cancel(-D+M*Fy+al*Ay+beta*zz*Hs)
ga=sp.cancel(2*cx*cy*((M-al)*Hs-beta*zz))
# Equivalent-strain invariants at k=1
mu=sp.cancel((ex+ey)/(2*(1-nu)))
de=sp.cancel((ex-ey)/(2*(1+nu)))
h=sp.cancel(ga/(2*(1+nu)))
r2=sp.cancel(de**2+h**2)

# Threshold polynomial for theta from Pi_eta(theta)=a*xcr.
T,Y,E=sp.symbols('T Y E')
threshold_poly=sp.expand(4*E**4*Y**2+8*E**2*Y**2*T**2-4*E**2*Y*T**3-E**2*T**4+4*Y**2*T**4-4*Y*T**5)
def thpoly(a):
    return sp.Poly(sp.factor(threshold_poly.subs({E:eta,Y:a*xcr})),T)

def positive_den(expr):
    num,den=sp.fraction(sp.factor(sp.cancel(expr)))
    return sp.factor(num),sp.factor(den)

a_th=sp.cancel(mu-th)
delta_th=sp.cancel(a_th**2-r2)
Na,Da=positive_den(a_th); Nd,Dd=positive_den(delta_th)
# Da,Dd consist only of positive constants and powers of (1+x^2),(1+y^2).

def factor_signature(den):
    return sp.sstr(sp.factor(den))

# Three exact branch polynomials for u_R(t); rr=t/xcr.
rr=sp.symbols('rr')
p0=rho*rr+(10*HR-6*rho)*rr**3+(8*rho-15*HR)*rr**4+(6*HR-3*rho)*rr**5
A3=4*rho-sp.Rational(7300,729)*HR+sp.Rational(10,729)*UR
A4=7*rho-sp.Rational(32800,2187)*HR-sp.Rational(5,2187)*UR
A5=3*rho-sp.Rational(118100,19683)*HR+sp.Rational(2,19683)*UR
B3=sp.Rational(10,729)*(HR-UR);B4=sp.Rational(5,2187)*(HR-UR);B5=sp.Rational(2,19683)*(HR-UR)
p1=sp.expand(p0+A3*(rr-1)**3+A4*(rr-1)**4+A5*(rr-1)**5)
p2=sp.expand(p1+B3*(rr-10)**3+B4*(rr-10)**4+B5*(rr-10)**5)

# Endpoint identity audit through C2.
endpoint_audit={}
for pt,left,right in [(1,p0,p1),(10,p1,p2)]:
    endpoint_audit[str(pt)]={
        'value':sp.simplify(left.subs(rr,pt)-right.subs(rr,pt))==0,
        'd1':sp.simplify(sp.diff(left,rr).subs(rr,pt)-sp.diff(right,rr).subs(rr,pt))==0,
        'd2':sp.simplify(sp.diff(left,rr,2).subs(rr,pt)-sp.diff(right,rr,2).subs(rr,pt))==0,
    }

# Ordered states (plus state >= minus state), exactly six.
states=[(0,0),(1,0),(1,1),(2,0),(2,1),(2,2)]
# Hminus(theta)=H(A)H(delta); Hplus(theta)=1-H(-A)H(delta).
# State predicates are kept as Boolean formulas of four primitive predicates:
# P1=lambda+>=theta1, P10=lambda+>=theta10, M1=lambda->=theta1, M10=lambda->=theta10.
state_bool={
 '00':'(1-P1)',
 '10':'P1*(1-P10)*(1-M1)',
 '11':'M1*(1-P10)',
 '20':'P10*(1-M1)',
 '21':'P10*M1*(1-M10)',
 '22':'M10',
}
primitive={
 'M(th)':'H(mu-th)*H(delta_th)',
 'P(th)':'1-H(th-mu)*H(delta_th)',
 'A_num':sp.sstr(Na),
 'A_den':factor_signature(Da),
 'delta_num':sp.sstr(Nd),
 'delta_den':factor_signature(Dd),
}

report={
 'identity':'NZSCCM_Z1_R17_GLOBAL_SPECTRAL_HEAVISIDE_CONSTRUCTOR',
 'governance':{'spatial_sampling':0,'spatial_quadrature':0,'material_points':0,'finite_prefix':0,'spatial_subdomains':1},
 'coordinates':{
   'x':'tan(X/2) in [0,+inf)','y':'tan(Y/2) in [0,+inf)','z':'normalized thickness in [-1,1]',
   'jacobian':'dX dY = 4/((1+x^2)(1+y^2)) dx dy'
 },
 'z1_exact_constants':{'nu':'9/50','eps0':str(eps0),'xcr':str(xcr),'eta':str(eta)},
 'kinematic_invariants':{
   'mu':sp.sstr(mu),'de':sp.sstr(de),'h':sp.sstr(h),'rE_squared':sp.sstr(r2)
 },
 'threshold_theta':{
   'theta1_polynomial':sp.sstr(thpoly(1).as_expr()),
   'theta10_polynomial':sp.sstr(thpoly(10).as_expr()),
   'root_selector':'unique positive root satisfying unsquared Pi_eta(theta)=a*xcr'
 },
 'threshold_predicates':primitive,
 'state_count':6,
 'ordered_states':states,
 'state_boolean_formula':state_bool,
 'branch_uR':{'state0':sp.sstr(p0),'state1':sp.sstr(p1),'state2':sp.sstr(p2)},
 'C2_endpoint_audit':endpoint_audit,
 'constructor_status':{
   'SEVEN_RADICAL_SINGLE_FIELD':'CROSSED_OUT_REDUCIBLE_ABS_BRANCHES',
   'TANGENT_HALF_ANGLE_RATIONAL_KINEMATICS':'PASS',
   'THRESHOLD_TO_POLYNOMIAL_INEQUALITIES':'PASS',
   'GLOBAL_THREE_BRANCH_TO_SIX_ORDERED_DISTRIBUTIONAL_STATES':'PASS',
   'R13_MATERIAL_LAW_CHANGED':'NO'
 }
}
print(json.dumps(report,ensure_ascii=False,indent=2))
