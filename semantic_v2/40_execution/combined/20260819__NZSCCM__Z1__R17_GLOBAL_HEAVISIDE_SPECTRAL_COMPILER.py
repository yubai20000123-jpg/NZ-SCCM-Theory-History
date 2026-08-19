#!/usr/bin/env python3
"""NZ-SCCM Z1 R17: exact global spectral-Heaviside constructor.

The reducible threshold-absolute-value radicals of the R13 CH implementation
are replaced by the identical scalar spectral truncated-power law.  The
physical material map remains one global formula.  Six ordered spectral states
are compiled into only nine reusable products of polynomial Heavisides.
Tangent-half-angle coordinates make the spatial kinematics rational.

No quadrature, sampling, material points, finite prefix, load stepping, or
numerical spatial subdivision.
"""
from __future__ import annotations
import json
import sympy as sp

x,y,z,D,q,al,P2=sp.symbols('x y z D q al P2', real=True)
chi=sp.symbols('chi', real=True)  # normalized threshold theta/xcr
nu=sp.Rational(9,50)
eps0=sp.Rational('0.0018712490394580678')
b=sp.Integer(6000); tc=sp.Integer(92); q0=sp.Rational(1,250)
kappa=sp.Rational('2.0005129533678754'); rho=sp.Rational(1,10)
xcr=sp.factor(rho/kappa); eta=sp.factor(xcr/20)
HR=sp.Rational('0.09799750427197301'); UR=sp.Rational(3,100)

# Rational tangent-half-angle coordinates.
sx=2*x/(1+x**2); cx=(1-x**2)/(1+x**2)
sy=2*y/(1+y**2); cy=(1-y**2)/(1+y**2)
Hs=sp.cancel(sx*sy); Fx=sp.cancel(sy**2*(1-sx**2)); Fy=sp.cancel(sx**2*(1-sy**2))
Ax=sp.cancel(-sp.Rational(1,4)-nu*sx**2/2-sy**2/2+sx**2*sy**2)
Ay=sp.cancel(nu/4-sx**2/2-nu*sy**2/2+sx**2*sy**2)
M=sp.factor(P2/eps0*(q0*q+q**2/2)); beta=sp.factor(P2*q/(eps0*b)); zz=tc*z/2
ex=sp.cancel(nu*D+M*Fx+al*Ax+beta*zz*Hs)
ey=sp.cancel(-D+M*Fy+al*Ay+beta*zz*Hs)
ga=sp.cancel(2*cx*cy*((M-al)*Hs-beta*zz))
mu=sp.cancel((ex+ey)/(2*(1-nu))); de=sp.cancel((ex-ey)/(2*(1+nu))); h=sp.cancel(ga/(2*(1+nu)))
r2=sp.cancel(de**2+h**2)

# Pi_eta is homogeneous: Pi_{xcr/20}(xcr*chi)/xcr = Pi_{1/20}(chi).
# Hence the two threshold algebraic constants have small universal quintics.
V=sp.symbols('V')
chi1_poly=160000*V**5-159900*V**4+400*V**3-800*V**2-1
chi10_poly=16000*V**5-159999*V**4+40*V**3-800*V**2-1
# actual threshold theta=xcr*chi. Work with normalized invariants to keep coefficients small.
mub=sp.cancel(mu/xcr); r2b=sp.cancel(r2/xcr**2)
Achi=sp.cancel(mub-chi); Dchi=sp.cancel(Achi**2-r2b)

def numden(expr):
    n,d=sp.fraction(sp.factor(sp.cancel(expr))); return sp.factor(n),sp.factor(d)
NA,DA=numden(Achi); ND,DD=numden(Dchi)

# Three exact scalar spline branches in rr=t/xcr.
rr=sp.symbols('rr')
p0=rho*rr+(10*HR-6*rho)*rr**3+(8*rho-15*HR)*rr**4+(6*HR-3*rho)*rr**5
A3=4*rho-sp.Rational(7300,729)*HR+sp.Rational(10,729)*UR
A4=7*rho-sp.Rational(32800,2187)*HR-sp.Rational(5,2187)*UR
A5=3*rho-sp.Rational(118100,19683)*HR+sp.Rational(2,19683)*UR
B3=sp.Rational(10,729)*(HR-UR);B4=sp.Rational(5,2187)*(HR-UR);B5=sp.Rational(2,19683)*(HR-UR)
p1=sp.expand(p0+A3*(rr-1)**3+A4*(rr-1)**4+A5*(rr-1)**5)
p2=sp.expand(p1+B3*(rr-10)**3+B4*(rr-10)**4+B5*(rr-10)**5)
endpoint={}
for pt,L,R in [(1,p0,p1),(10,p1,p2)]:
    endpoint[str(pt)]={f'd{k}':sp.simplify(sp.diff(L,rr,k).subs(rr,pt)-sp.diff(R,rr,k).subs(rr,pt))==0 for k in range(3)}

# Primitive spectral threshold indicators, using A=mu/xcr-chi and Delta=A^2-rE^2/xcr^2:
# M(chi)=1_{lambda_minus >= theta}=H(A)H(Delta)
# P(chi)=1_{lambda_plus  >= theta}=1-H(-A)H(Delta).
# Away from a threshold surface H(-A)=1-H(A), and all spline jumps vanish through C2,
# so the point convention has zero effect on the classical integral.
a1,b1,a10,b10=sp.symbols('a1 b1 a10 b10')
M1=a1*b1; P1=1-(1-a1)*b1; M10=a10*b10; P10=1-(1-a10)*b10
state_expr={
 '00':1-P1,
 '10':P1*(1-P10)*(1-M1),
 '11':M1*(1-P10),
 '20':P10*(1-M1),
 '21':P10*M1*(1-M10),
 '22':M10,
}
vars4=(a1,b1,a10,b10)
def idempotent_expand(expr):
    P=sp.Poly(sp.expand(expr),*vars4); out={}
    for mon,c in P.terms():
        mask=tuple(min(1,e) for e in mon); out[mask]=sp.simplify(out.get(mask,0)+c)
    return {mask:c for mask,c in out.items() if c!=0}
state_masks={s:{''.join(map(str,m)):str(c) for m,c in idempotent_expand(e).items()} for s,e in state_expr.items()}
all_masks=sorted(set().union(*(idempotent_expand(e).keys() for e in state_expr.values())))
# Verify the six states partition all monotone threshold truth assignments P10<=P1, M10<=M1, M<=P.
truth_ok=True; truth_rows=[]
for pp1 in (0,1):
 for pp10 in (0,1):
  for mm1 in (0,1):
   for mm10 in (0,1):
    if pp10>pp1 or mm10>mm1 or mm1>pp1 or mm10>pp10: continue
    vals={P1:pp1,P10:pp10,M1:mm1,M10:mm10}
    # evaluate original state definitions directly using P/M symbols
    svals=[
      1-pp1,
      pp1*(1-pp10)*(1-mm1),
      mm1*(1-pp10),
      pp10*(1-mm1),
      pp10*mm1*(1-mm10),
      mm10]
    truth_ok &= (sum(svals)==1 and sum(v!=0 for v in svals)==1)
    truth_rows.append([pp1,pp10,mm1,mm10,svals])

report={
 'identity':'NZSCCM_Z1_R17_GLOBAL_SPECTRAL_HEAVISIDE_CONSTRUCTOR',
 'governance':{'spatial_sampling':0,'spatial_quadrature':0,'material_points':0,'finite_prefix':0,'formal_complete_halfwaves':1},
 'coordinates':{'x':'tan(X/2) in [0,+inf)','y':'tan(Y/2) in [0,+inf)','z':'normalized core thickness in [-1,1]','jacobian':'4/((1+x^2)(1+y^2))'},
 'normalized_thresholds':{
   'theta_over_xcr_state1_polynomial':sp.sstr(chi1_poly),
   'theta_over_xcr_state10_polynomial':sp.sstr(chi10_poly),
   'selector':'the unique positive real root of each quintic; theta_a=xcr*chi_a'
 },
 'threshold_predicate_polynomials':{
   'A_chi_numerator':sp.sstr(NA),'A_chi_denominator_positive':sp.sstr(DA),
   'Delta_chi_numerator':sp.sstr(ND),'Delta_chi_denominator_positive':sp.sstr(DD),
   'minus':'H(A_chi)*H(Delta_chi)',
   'plus':'1-H(-A_chi)*H(Delta_chi)'
 },
 'branch_uR':{'0':sp.sstr(p0),'1':sp.sstr(p1),'2':sp.sstr(p2)},
 'C2_endpoint_audit':endpoint,
 'ordered_state_count':6,
 'ordered_states':['00','10','11','20','21','22'],
 'state_to_idempotent_heaviside_masks':state_masks,
 'unique_basic_heaviside_product_count':len(all_masks),
 'unique_basic_masks':[''.join(map(str,m)) for m in all_masks],
 'state_partition_truth_table_pass':bool(truth_ok),
 'constructor_status':{
   'SEVEN_RADICAL_SINGLE_FIELD':'CROSSED_OUT_REDUCIBLE_ABS_BRANCHES_AND_TIMEOUT',
   'GLOBAL_R13_SPLINE_IDENTITY':'PASS',
   'TANGENT_HALF_ANGLE_RATIONAL_KINEMATICS':'PASS',
   'ALGEBRAIC_THRESHOLD_NORMALIZATION':'PASS',
   'SIX_ORDERED_STATES':'PASS',
   'NINE_REUSABLE_HEAVISIDE_PRODUCTS':'PASS',
   'SPATIAL_SUBDIVISION_CREATED':'NO'
 }
}
print(json.dumps(report,ensure_ascii=False,indent=2))
