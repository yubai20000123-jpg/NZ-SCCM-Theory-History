#!/usr/bin/env python3
"""Generate an OpenXM/Asir Oaku script for one actual compactified R17 primitive mask.

This stays on the active R17 spectral-Heaviside route. It uses the exact R18
bounded compactification and the exact R17 threshold predicates. The first
constructor target is the primitive minus-threshold mask M(chi)=H(Achi)H(Dchi)
for the same nonuniform symbolic constructor slice used by the R17 smooth-branch
annihilator probe: D=1, q=tt/100, alpha=tt, while v,z,tt,p2,chi remain exact
parameters. No spatial sampling, quadrature, cells, material points, or finite
prefixes are introduced.
"""
from __future__ import annotations
import pathlib
import sympy as sp

u,v,z,tt,p2,cc=sp.symbols('u v z tt p2 cc', real=True)
D,q,al,P2,chi=sp.symbols('D q al P2 chi', real=True)
nu0=sp.Rational(9,50)
eps0=sp.Rational('0.0018712490394580678')
b=sp.Integer(6000); tc=sp.Integer(92); q0=sp.Rational(1,250)
kappa=sp.Rational('2.0005129533678754'); rho=sp.Rational(1,10)
xcr=sp.factor(rho/kappa)

x=sp.cancel(u/(1-u)); y=sp.cancel(v/(1-v))
sx=sp.cancel(2*x/(1+x**2)); cx=sp.cancel((1-x**2)/(1+x**2))
sy=sp.cancel(2*y/(1+y**2)); cy=sp.cancel((1-y**2)/(1+y**2))
Hs=sp.cancel(sx*sy); Fx=sp.cancel(sy**2*(1-sx**2)); Fy=sp.cancel(sx**2*(1-sy**2))
Ax=sp.cancel(-sp.Rational(1,4)-nu0*sx**2/2-sy**2/2+sx**2*sy**2)
Ay=sp.cancel(nu0/4-sx**2/2-nu0*sy**2/2+sx**2*sy**2)
M=sp.factor(P2/eps0*(q0*q+q**2/2)); beta=sp.factor(P2*q/(eps0*b)); zz=tc*z/2
ex=sp.cancel(nu0*D+M*Fx+al*Ax+beta*zz*Hs)
ey=sp.cancel(-D+M*Fy+al*Ay+beta*zz*Hs)
ga=sp.cancel(2*cx*cy*((M-al)*Hs-beta*zz))
mu=sp.cancel((ex+ey)/(2*(1-nu0))); de=sp.cancel((ex-ey)/(2*(1+nu0))); h=sp.cancel(ga/(2*(1+nu0)))
r2=sp.cancel(de**2+h**2)
Achi=sp.cancel(mu/xcr-chi); Dchi=sp.cancel(Achi**2-r2/xcr**2)
NA,_=sp.fraction(sp.factor(Achi)); ND,_=sp.fraction(sp.factor(Dchi))
subs={D:sp.Integer(1),q:tt*sp.Rational(1,100),al:tt,P2:p2,chi:cc}
NA=sp.expand(NA.subs(subs)); ND=sp.expand(ND.subs(subs))

def asir(expr):
    return sp.sstr(expr).replace('**','^')

rr=f'''import("nn_ndbf.rr")$
import("nk_restriction.rr")$
print("NZSCCM_R18_ACTUAL_R17_MASK_OAKU_START")$
print("A_TERMS={len(sp.Poly(NA,u,v,z,tt,p2,cc).terms())}")$
print("D_TERMS={len(sp.Poly(ND,u,v,z,tt,p2,cc).terms())}")$
A={asir(NA)}$
B={asir(ND)}$
print("BUILD_HEAVISIDE_ANN_START")$
IH=ndbf.ann_n([A,B])$
IH0=map(subst,map(subst,IH,s0,0),s1,0)$
print("BUILD_HEAVISIDE_ANN_PASS")$
print(IH0)$
print("INTEGRATE_U_START")$
J=nk_restriction.ost_integration_ideal(IH0,[u,v,z,tt,p2,cc],[du,dv,dz,dtt,dp2,dcc],[1,0,0,0,0,0],[0],[1])$
print("INTEGRATE_U_PASS")$
print(J)$
print("NZSCCM_R18_ACTUAL_R17_MASK_OAKU_PASS")$
end$
'''
out=pathlib.Path('semantic_v2/40_execution/combined/20260819__NZSCCM__Z1__R18_ACTUAL_MASK_OAKU.rr')
out.write_text(rr,encoding='utf-8')
print(out)
