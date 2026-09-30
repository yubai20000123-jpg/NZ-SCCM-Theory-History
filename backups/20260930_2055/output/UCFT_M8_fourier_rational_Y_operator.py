#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UCFT M8 production analytic-Y operator.

Finite trigonometric fields are retained in Fourier form for conditioning.
Active boundaries still use t=tan(Y/2) polynomial roots. On each active interval,
material primitives are composed exactly in the finite Fourier algebra. Terms that
require division by global curvature sin(Y) or sin^2(Y) are integrated by the
same tan-half-angle rational primitive, harmonic by harmonic. This is algebraically
identical to one giant P(t)/Q(t) integral but avoids catastrophic coefficient
cancellation for C/S/B high harmonics.

No Y Gauss points are introduced. Only fixed-X analytic/rational Y integration is
performed; X remains the sole deterministic integral in the production hierarchy.
"""
import math, cmath
from dataclasses import dataclass
from math import comb
import numpy as np
import mpmath as mp

import UCFT_M8_rational_Y_primitive_mp as ry
import UCFT_M8_generalized_UHPC_trig_active_set as aset

mp.mp.dps=55

@dataclass
class FS:
    c: dict
    def __post_init__(self):
        out={}
        for k,v in self.c.items():
            z=complex(v)
            if abs(z)>1e-40: out[int(k)]=z
        self.c=out
    @staticmethod
    def const(x): return FS({0:complex(x)})
    @staticmethod
    def from_trig(a0=0.0,cos_coeff=None,sin_coeff=None):
        c={0:complex(a0)}
        for k,a in (cos_coeff or {}).items():
            k=int(k);a=complex(a);c[k]=c.get(k,0)+a/2;c[-k]=c.get(-k,0)+a/2
        for k,b in (sin_coeff or {}).items():
            k=int(k);b=complex(b);c[k]=c.get(k,0)+b/(2j);c[-k]=c.get(-k,0)-b/(2j)
        return FS(c)
    def __add__(self,o):
        o=o if isinstance(o,FS) else FS.const(o);c=dict(self.c)
        for k,v in o.c.items():c[k]=c.get(k,0)+v
        return FS(c)
    __radd__=__add__
    def __neg__(self):return FS({k:-v for k,v in self.c.items()})
    def __sub__(self,o):return self+(-(o if isinstance(o,FS) else FS.const(o)))
    def __rsub__(self,o):return (o if isinstance(o,FS) else FS.const(o))-self
    def __mul__(self,o):
        o=o if isinstance(o,FS) else FS.const(o);c={}
        for k,a in self.c.items():
            for l,b in o.c.items():c[k+l]=c.get(k+l,0)+a*b
        return FS(c)
    __rmul__=__mul__
    def pow(self,n):
        n=int(n);out=FS.const(1);base=self
        while n:
            if n&1:out=out*base
            n//=2
            if n:base=base*base
        return out
    def eval(self,Y):return sum(v*cmath.exp(1j*k*Y) for k,v in self.c.items()).real
    def maxk(self):return max([0]+[abs(k) for k in self.c])

def poly_compose(poly, e):
    out=FS.const(0)
    for a in poly.coef[::-1]:out=out*e+float(a)
    return out

def odd_divdiff(poly, em, d, h_over_denom_power=1):
    h=float(h_over_denom_power); out=FS.const(0)
    epows=[FS.const(1)];dpows=[FS.const(1)]
    deg=len(poly.coef)-1
    for _ in range(deg): epows.append(epows[-1]*em); dpows.append(dpows[-1]*d)
    for n,a in enumerate(poly.coef):
        if abs(a)<1e-30:continue
        for j in range(1,n+1,2):
            out += 2*float(a)*comb(n,j)*epows[n-j]*dpows[j-1]*h
    return out

def same_branch_M(Fpoly,Hpoly,em,d,h):
    maxdeg=max(len(Fpoly.coef),len(Hpoly.coef))-1
    ep=[FS.const(1)];dp=[FS.const(1)]
    for _ in range(maxdeg+1):ep.append(ep[-1]*em);dp.append(dp[-1]*d)
    out=FS.const(0)
    for j in range(3,maxdeg+1,2):
        term=FS.const(0)
        for n,a in enumerate(Hpoly.coef):
            if n>=j and abs(a)>1e-30: term += 2*float(a)*comb(n,j)*ep[n-j]
        for n,a in enumerate(Fpoly.coef):
            if n>=j and abs(a)>1e-30: term -= 2*float(a)*comb(n,j)*ep[n-j+1]
        out += term*dp[j-2]*(h*h)
    return out

_basis_cache={}
def _A1_primitive(k,Y):
    k=abs(int(k))
    if k==0: return math.log(math.tan(Y/2.0))
    if k%2==0:
        n=k//2;v=math.log(math.tan(Y/2.0))
        for j in range(1,n+1):
            m=2*j-1;v += 2.0*math.cos(m*Y)/m
        return v
    n=(k-1)//2;v=math.log(math.sin(Y))
    for j in range(1,n+1):
        m=2*j;v += 2.0*math.cos(m*Y)/m
    return v

def _B1_primitive(k,Y):
    sign=1
    if k<0: sign=-1;k=-k
    k=int(k)
    if k==0:return 0.0
    if k%2==0:
        n=k//2;v=0.0
        for j in range(1,n+1):
            m=2*j-1; v += 2.0*math.sin(m*Y)/m
    else:
        n=(k-1)//2;v=Y
        for j in range(1,n+1):
            m=2*j; v += 2.0*math.sin(m*Y)/m
    return sign*v

def _C2_primitive(k,Y):
    k=abs(int(k));cot=math.cos(Y)/math.sin(Y)
    if k==0:return -cot
    return -cot*math.cos(k*Y) - 0.5*k*(_B1_primitive(k+1,Y)+_B1_primitive(k-1,Y))

def _D2_primitive(k,Y):
    sign=1
    if k<0:sign=-1;k=-k
    k=int(k)
    if k==0:return 0.0
    cot=math.cos(Y)/math.sin(Y)
    v=-cot*math.sin(k*Y)+0.5*k*(_A1_primitive(k+1,Y)+_A1_primitive(abs(k-1),Y))
    return sign*v

def basis_integral(k,r,Y0,Y1):
    key=(int(k),int(r),round(float(Y0),13),round(float(Y1),13))
    if key in _basis_cache:return _basis_cache[key]
    k=int(k);r=int(r)
    if r==0:
        if k==0:v=complex(Y1-Y0)
        else:v=(cmath.exp(1j*k*Y1)-cmath.exp(1j*k*Y0))/(1j*k)
    else:
        eps=2e-13
        if Y0<=eps or Y1>=math.pi-eps:
            raise ArithmeticError('singular rational basis interval reaches sinY=0 endpoint')
        if r==1:
            re=_A1_primitive(k,Y1)-_A1_primitive(k,Y0)
            im=_B1_primitive(k,Y1)-_B1_primitive(k,Y0)
        elif r==2:
            re=_C2_primitive(k,Y1)-_C2_primitive(k,Y0)
            im=_D2_primitive(k,Y1)-_D2_primitive(k,Y0)
        else:raise ValueError('r must be 0,1,2')
        v=complex(re,im)
    _basis_cache[key]=v;return v

def integrate_fs(fs,Y0,Y1,weight=None,sin_power=0,scale=1.0):
    if weight is not None:fs=fs*weight
    val=0j
    for k,c in fs.c.items(): val += c*basis_integral(k,sin_power,Y0,Y1)
    val*=scale
    if abs(val.imag)>5e-9*max(1.0,abs(val.real)):
        raise ArithmeticError(f'non-real integral residual {val}')
    return float(val.real)

def active_cuts_for_faces(a0,cc,ss,chi0,h,thresholds):
    spp=dict(ss or {});spm=dict(ss or {})
    spp[1]=spp.get(1,0.0)+h*chi0;spm[1]=spm.get(1,0.0)-h*chi0
    cuts=[0.0,math.pi]
    for th in thresholds:
        cuts += aset.material_boundary_roots(a0,cc,spp,float(th))
        cuts += aset.material_boundary_roots(a0,cc,spm,float(th))
    cuts.sort();u=[]
    for y in cuts:
        if not u or abs(y-u[-1])>2e-7:u.append(y)
    return u

def generalized_y_moments(law,a0,cc,ss,chi0,t_c,weights):
    h=.5*t_c
    em=FS.from_trig(a0,cc,ss); chi=FS.from_trig(0,{}, {1:chi0}); d=h*chi
    ep=em+d;en=em-d
    cuts=active_cuts_for_faces(a0,cc,ss,chi0,h,law.thresholds)
    out={f'{kind}_{name}':0.0 for kind in ('N','M') for name in weights}
    for yl,yr in zip(cuts[:-1],cuts[1:]):
        ym=.5*(yl+yr); epp=ep.eval(ym);enn=en.eval(ym)
        ip=law.branch_index(epp);im=law.branch_index(enn)
        if ip==im:
            Nfs=odd_divdiff(law.F_branch[ip],em,d,h)
            Mfs=same_branch_M(law.F_branch[ip],law.H_branch[ip],em,d,h)
            for name,w in weights.items():
                out['N_'+name]+=integrate_fs(Nfs,yl,yr,w,0)
                out['M_'+name]+=integrate_fs(Mfs,yl,yr,w,0)
        else:
            Fd=poly_compose(law.F_branch[ip],ep)-poly_compose(law.F_branch[im],en)
            Hd=poly_compose(law.H_branch[ip],ep)-poly_compose(law.H_branch[im],en)
            Mn=Hd-em*Fd
            for name,w in weights.items():
                out['N_'+name]+=integrate_fs(Fd,yl,yr,w,1,1.0/chi0)
                out['M_'+name]+=integrate_fs(Mn,yl,yr,w,2,1.0/(chi0*chi0))
    return out,cuts
