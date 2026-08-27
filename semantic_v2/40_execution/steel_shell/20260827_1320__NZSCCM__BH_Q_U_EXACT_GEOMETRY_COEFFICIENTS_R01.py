from __future__ import annotations

"""Exact finite-harmonic geometry backend for the BH q-U repair.

No spatial quadrature, material points, or fitted coefficients are used.
Frequencies are stored as rational multiples of pi/B, so harmonic collisions are
merged exactly before endpoint evaluation.

BH normalized geometry:
  global representative halfwave: B x B
  local Lx/B = 9/40 = 0.225
  local Ly/B = 2/9
  TOP (4 PBL stations): central full cell x/B in [31/80,49/80]
  BOTTOM (5 PBL stations): central left/right cells x/B in [11/40,1/2]
                                or [1/2,29/40]
  longitudinal local cell containing y/B=1/2: y/B in [4/9,6/9]

The bottom left/right cells are mirror images: h_gamma changes sign while the
normal h-coefficients and Airy energies are identical.
"""

from collections import defaultdict
from fractions import Fraction as F
import cmath
import math

NU = 0.30


def add(a,b,scale=1.0):
    out=defaultdict(complex); out.update(a)
    for k,v in b.items(): out[k]+=scale*v
    return {k:v for k,v in out.items() if abs(v)>1e-14}


def mul(a,b):
    out=defaultdict(complex)
    for (ax,ay),ca in a.items():
        for (bx,by),cb in b.items(): out[(ax+bx,ay+by)] += ca*cb
    return {k:v for k,v in out.items() if abs(v)>1e-13}


def deriv(f,dx=0,dy=0):
    return {(a,b):c*(1j*math.pi*float(a))**dx*(1j*math.pi*float(b))**dy
            for (a,b),c in f.items()}


def scale(f,s): return {k:s*v for k,v in f.items()}


def sin_mode(r,axis):
    if axis=='x': return {(r,F(0)):1/(2j),(-r,F(0)):-1/(2j)}
    return {(F(0),r):1/(2j),(F(0),-r):-1/(2j)}


def cos_shift(r,x0,axis):
    ph=cmath.exp(-1j*math.pi*float(r*x0))
    if axis=='x': return {(r,F(0)):.5*ph,(-r,F(0)):.5*ph.conjugate()}
    return {(F(0),r):.5*ph,(F(0),-r):.5*ph.conjugate()}


def one_minus_cos(r,x0,axis):
    return add({(F(0),F(0)):1+0j},cos_shift(r,x0,axis),-1)


def avg_exp(freq,x0,Lx,y0,Ly):
    a,b=freq
    def av(r,z0,L):
        if r==0: return 1+0j
        w=math.pi*float(r)
        return cmath.exp(1j*w*float(z0+L/2))*math.sin(w*float(L)/2)/(w*float(L)/2)
    return av(a,x0,Lx)*av(b,y0,Ly)


def avg_product(f,g,x0,Lx,y0,Ly):
    return sum(c*avg_exp(k,x0,Lx,y0,Ly) for k,c in mul(f,g).items())


def psi(): return mul(sin_mode(F(1),'x'),sin_mode(F(1),'y'))


def phi(x0,y0):
    # kx/pi = 80/9, ky/pi = 9 for all self-similar BH cases.
    return mul(one_minus_cos(F(80,9),x0,'x'),one_minus_cos(F(9),y0,'y'))


def source_ll(p):
    K=add(mul(deriv(p,2,0),deriv(p,0,2)),mul(deriv(p,1,1),deriv(p,1,1)),-1)
    return scale(K,-1)  # frozen R02 sign convention


def source_gl(ps,p):
    C=add(mul(deriv(ps,2,0),deriv(p,0,2)),mul(deriv(p,2,0),deriv(ps,0,2)))
    C=add(C,mul(deriv(ps,1,1),deriv(p,1,1)),-2)
    return scale(C,-1)


def stress_from_source(S):
    sx={}; sy={}; tau={}
    for (a,b),c in S.items():
        aa=math.pi*float(a); bb=math.pi*float(b)
        den=(aa*aa+bb*bb)**2
        if den<1e-30: continue
        FF=c/den
        sx[(a,b)]=-bb*bb*FF
        sy[(a,b)]=-aa*aa*FF
        tau[(a,b)]=aa*bb*FF
    return sx,sy,tau


def inner(s1,s2,nu,x0,Lx,y0,Ly):
    sx1,sy1,t1=s1; sx2,sy2,t2=s2
    v=avg_product(sx1,sx2,x0,Lx,y0,Ly)+avg_product(sy1,sy2,x0,Lx,y0,Ly)
    v-=nu*(avg_product(sx1,sy2,x0,Lx,y0,Ly)+avg_product(sy1,sx2,x0,Lx,y0,Ly))
    v+=2*(1+nu)*avg_product(t1,t2,x0,Lx,y0,Ly)
    return v.real


def dimensionless_coefficients(pattern):
    Lx=F(9,40); Ly=F(2,9); y0=F(4,9)
    x0={'TOP4':F(31,80),'BOTTOM5_LEFT':F(11,40),'BOTTOM5_RIGHT':F(1,2)}[pattern]
    ps=psi(); p=phi(x0,y0)
    hx=avg_product(deriv(ps,1,0),deriv(p,1,0),x0,Lx,y0,Ly).real
    hy=avg_product(deriv(ps,0,1),deriv(p,0,1),x0,Lx,y0,Ly).real
    hg=(avg_product(deriv(ps,1,0),deriv(p,0,1),x0,Lx,y0,Ly)
        +avg_product(deriv(ps,0,1),deriv(p,1,0),x0,Lx,y0,Ly)).real
    sll=stress_from_source(source_ll(p)); sgl=stress_from_source(source_gl(ps,p))
    KA=.5*inner(sll,sll,NU,x0,Lx,y0,Ly)
    Kd=.5*inner(sll,sgl,NU,x0,Lx,y0,Ly)
    KDD=.5*inner(sgl,sgl,NU,x0,Lx,y0,Ly)
    return dict(B2_hx=hx,B2_hy=hy,B2_hgamma=hg,
                B4_KA=KA,B4_KdDelta=Kd,B4_KDeltaDelta=KDD)


def dimensional_coefficients(B,pattern):
    d=dimensionless_coefficients(pattern)
    return dict(hx=d['B2_hx']/B**2,hy=d['B2_hy']/B**2,hgamma=d['B2_hgamma']/B**2,
                KA=d['B4_KA']/B**4,KdDelta=d['B4_KdDelta']/B**4,
                KDeltaDelta=d['B4_KDeltaDelta']/B**4)


if __name__=='__main__':
    for p in ('TOP4','BOTTOM5_LEFT','BOTTOM5_RIGHT'):
        print(p,dimensionless_coefficients(p))
    for B in (1600.0,2500.0):
        print('B=',B)
        for p in ('TOP4','BOTTOM5_LEFT','BOTTOM5_RIGHT'):
            print(p,dimensional_coefficients(B,p))
