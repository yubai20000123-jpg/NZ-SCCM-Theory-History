#!/usr/bin/env python3
"""R17 exact spectral branch annihilator constructor.

Builds one full R10 fixed-spline-state Syy branch in the irreducible smooth
three-radical field (rE,g+,g-) and asks ore_algebra for an exact scalar
annihilator in the tangent-half-angle variable x. This is the analytic half of
the Oaku semialgebraic constructor; threshold Heavisides are handled separately.

No spatial quadrature/sampling/material points/prefixes.
"""
from time import time
from sage.all import QQ, PolynomialRing
from ore_algebra import OreAlgebra

T0=time()
Cpoly=PolynomialRing(QQ,names=('y','z','tt','p2'))
y,z,tt,p2=Cpoly.gens(); C=Cpoly.fraction_field()
Rx=PolynomialRing(C,'x'); x=Rx.gen(); F=Rx.fraction_field()
D=QQ(1); Q=QQ(1)/100; AL=QQ(1)
nu=QQ(9)/50
eps0=QQ('0.0018712490394580678'); b=QQ(6000); tc=QQ(92); qimp=QQ(1)/250
kappa=QQ('2.0005129533678754'); rho=QQ(1)/10
xcr=rho/kappa; eta=xcr/20
HR=QQ('0.09799750427197301'); UR=QQ(3)/100
acc=QQ('0.1072329249362415')
Cpoly=PolynomialRing(QQ,names=('y','z','tt','p2','atp'))
y,z,tt,p2,atp=Cpoly.gens(); C=Cpoly.fraction_field(); Rx=PolynomialRing(C,'x'); x=Rx.gen(); F=Rx.fraction_field()
def ff(v): return F(v)
y,z,tt,p2,atp=map(ff,(y,z,tt,p2,atp)); x=F(x)
sx=2*x/(1+x*x); cx=(1-x*x)/(1+x*x)
sy=2*y/(1+y*y); cy=(1-y*y)/(1+y*y)
Hs=sx*sy; Fx=sy**2*(1-sx**2); Fy=sx**2*(1-sy**2)
Ax=-QQ(1)/4-nu*sx**2/2-sy**2/2+sx**2*sy**2
Ay=nu/4-sx**2/2-nu*sy**2/2+sx**2*sy**2
q=tt*Q; al=tt*AL
M=p2/eps0*(qimp*q+q*q/2); beta=p2*q/(eps0*b); zz=tc*z/2
ex=nu*D+M*Fx+al*Ax+beta*zz*Hs
ey=-D+M*Fy+al*Ay+beta*zz*Hs
ga=2*cx*cy*((M-al)*Hs-beta*zz)
mu=(ex+ey)/(2*(1-nu)); de=(ex-ey)/(2*(1+nu)); hh=ga/(2*(1+nu))
R0=de**2+hh**2
Pr=PolynomialRing(F,'RR'); RR=Pr.gen(); K1=F.extension(RR**2-R0,names=('rE',)); rE=K1.gen()
mu=K1(mu);de=K1(de);hh=K1(hh);eta1=K1(eta)
Pgp=PolynomialRing(K1,'GGp'); GGp=Pgp.gen(); K2=K1.extension(GGp**2-((mu+rE)**2+eta1**2),names=('gp',)); gp=K2.gen()
mu=K2(mu);de=K2(de);hh=K2(hh);rE=K2(rE);eta2=K2(eta)
Pgm=PolynomialRing(K2,'GGm'); GGm=Pgm.gen(); K3=K2.extension(GGm**2-((mu-rE)**2+eta2**2),names=('gm',)); gm=K3.gen()
mu=K3(mu);de=K3(de);hh=K3(hh);rE=K3(rE);gp=K3(gp);gm=K3(gm)
kappa3=K3(kappa);rho3=K3(rho);xcr3=K3(xcr);acc3=K3(acc);at3=K3(atp);eta3=K3(eta)
def proj(lam,g,sign=1):
    z0=lam if sign==1 else -lam
    return z0**2*(g+z0)/(2*(z0**2+eta3**2))
def Cfun(c): return kappa3*c/(1+(kappa3-2)*c+c*c)
rrvar=PolynomialRing(QQ,'rr').gen()
p0=rho*rrvar+(10*HR-6*rho)*rrvar**3+(8*rho-15*HR)*rrvar**4+(6*HR-3*rho)*rrvar**5
A3=4*rho-QQ(7300)/729*HR+QQ(10)/729*UR
A4=7*rho-QQ(32800)/2187*HR-QQ(5)/2187*UR
A5=3*rho-QQ(118100)/19683*HR+QQ(2)/19683*UR
B3=QQ(10)/729*(HR-UR); B4=QQ(5)/2187*(HR-UR); B5=QQ(2)/19683*(HR-UR)
p1=p0+A3*(rrvar-1)**3+A4*(rrvar-1)**4+A5*(rrvar-1)**5
p2b=p1+B3*(rrvar-10)**3+B4*(rrvar-10)**4+B5*(rrvar-10)**5
branches=[p0,p1,p2b]
def evalpoly(poly,t):
    out=K3(0)
    for i in range(poly.degree()+1): out+=K3(poly[i])*(t/xcr3)**i
    return out
def stress_for_state(ip,im):
    lp=mu+rE; lm=mu-rE
    tp=proj(lp,gp,1); tm=proj(lm,gm,1)
    cp=proj(lp,gp,-1); cm=proj(lm,gm,-1)
    Cp=Cfun(cp); Cm=Cfun(cm)
    up=evalpoly(branches[ip],tp); um=evalpoly(branches[im],tm)
    Tp=up/rho3; Tm=um/rho3
    Up=kappa3*lp-Cp+kappa3*cp+up-kappa3*tp
    Um=kappa3*lm-Cm+kappa3*cm+um-kappa3*tm
    spv=Up-acc3*Cp**2*Cm+Cp*Tm-rho3*at3*Tp*Tm**8
    smv=Um-acc3*Cm**2*Cp+Cm*Tp-rho3*at3*Tm*Tp**8
    return (spv+smv)/2+de*(smv-spv)/(2*rE)
Syy=stress_for_state(0,0)
print('NZSCCM_R17_SPECTRAL_BRANCH_FIELD_BUILT seconds=',time()-T0)
A=OreAlgebra(Rx,'Dx'); Dx=A.gen()
L=(Rx.gen()*Dx-1).annihilator_of_composition(Syy)
print('NZSCCM_R17_STATE=00')
print('ANN_ORDER=',L.order())
print('ANN_DEGREE=',L.degree())
print('ANNIHILATOR=',L)
print('TOTAL_SECONDS=',time()-T0)
print('NZSCCM_R17_SPECTRAL_BRANCH_ANNIHILATOR_PASS')