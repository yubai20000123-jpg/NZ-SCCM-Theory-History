"""R14: Zhang-2023 peak-anchored strain-compatible steel-shell UHPC Ny-My terminal.

Formal identities
-----------------
- Full 2D Marguerre-Airy structural front is frozen.
- y-normal terminal is Ny-My.
- UHPC compression uses the Zhang-2023 zero-confinement ascending branch.
- Extreme UHPC compression fibre is anchored at eps_c0=0.0035 (first peak attainment).
- Zhang post-peak is source-retained but intentionally not used to extend the no-load-path mainline.
- External faces/web share the same plane-section strain field.
- Steel is elastic-perfectly plastic with existing Yun compression caps where applicable.
- Every through-thickness integral is exact; no thickness quadrature/material points.
- Formal control-location candidates are s=0, s=1, and interior stationary roots.
- Abaqus comparators are used only after roots are fixed.
"""
from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Dict, Tuple, List
import numpy as np
from scipy.optimize import brentq, root
from scipy.special import hyp2f1

FC=141.1
EC=43400.0
EPS0=0.0035
ES=206000.0
FY=355.0
TC=42.0
TS=4.0
H=TC/2.0
Q0=0.0025
KAPPA_T=EPS0/TC

KU=EC*EPS0/FC
R=KU/(KU-1.0)
A=R-1.0

@dataclass(frozen=True)
class Case:
    b: float
    Pcr: float
    C: float
    G: float
    J: float
    rho: float
    fcs: float

CASES: Dict[str,Case]={
    'T120':Case(1600.,30.822799056,7284.21452557,5.412338111e6,1.118592686e7,0.05506,355.0),
    'T360':Case(1600.,30.751943803,7055.99557435,5.074760452e6,1.095253234e7,0.01982,301.87133),
    'BH005':Case(250.,197.5373,1179.2700,5.3614e6,6.7473e7,0.12685714,355.0),
    'BH010':Case(500.,98.3195,2253.6479,4.8274e6,3.2496e7,0.06342857,355.0),
    'BH020':Case(1000.,49.0475,4400.9325,4.5604e6,1.5938e7,0.03171429,355.0),
    'BH032':Case(1600.,30.6284,6977.1939,4.4603e6,9.8889e6,0.01982143,295.42),
    'BH050':Case(2500.,19.5920,10841.3718,4.4002e6,6.3010e6,0.01268571,250.07),
}

COMPARATOR={
    'T120':12.6378,'T360':10.9688,'BH005':2.3558,'BH010':4.3043,
    'BH020':8.0076,'BH032':10.9905,'BH050':12.2198,
}


def I_m(x:float,m:int)->float:
    """Primitive of x^m/(A+x^R), x>=0."""
    if x<=0.0:
        return 0.0
    return float(x**(m+1)/((m+1)*A)*hyp2f1(
        1.0,(m+1)/R,1.0+(m+1)/R,-x**R/A))


def F0(x:float)->float:
    """Integral of Zhang ascending normalized stress g_a."""
    return R*I_m(x,1)


def F1(x:float)->float:
    """Integral of x*g_a."""
    return R*I_m(x,2)


def ga(x:float)->float:
    return R*x/(R-1.0+x**R)


def core_peak(k:float,rho:float)->Tuple[float,float]:
    """Exact UHPC N,M at eps_top=EPS0, 0<=k<KAPPA_T; full core stays compressive."""
    if k<0.0 or k>=KAPPA_T:
        raise ValueError('R14 peak-anchor candidate must keep the UHPC core in compression')
    if k<1e-18:
        sig=(1.0-rho)*FC
        return sig*TC,0.0
    kh=k/EPS0
    xl=1.0-kh*TC
    G0=F0(1.0)-F0(xl)
    G1=F1(1.0)-F1(xl)
    c=(1.0-rho)*FC
    N=c*G0/kh
    Iy=c*(G0-G1)/(kh*kh)
    M=H*N-Iy
    return N,M


def core_peak_deriv(k:float,rho:float)->Tuple[float,float]:
    """Exact dN/dk,dM/dk of core_peak."""
    if k<=1e-18:
        Et=(1.0-rho)*EC
        Nk=-Et*0.5*TC**2
        Mk=-Et*(H*0.5*TC**2-TC**3/3.0)
        return Nk,Mk
    kh=k/EPS0
    xl=1.0-kh*TC
    if xl<0.0:
        raise ValueError('UHPC tension would activate')
    G0=F0(1.0)-F0(xl)
    G1=F1(1.0)-F1(xl)
    gl=ga(xl)
    c=(1.0-rho)*FC
    dN_dkh=c*(TC*gl*kh-G0)/(kh*kh)
    K=G0-G1
    dIy_dkh=c*(TC**2*gl/kh-2.0*K/(kh**3))
    dM_dkh=H*dN_dkh-dIy_dkh
    return dN_dkh/EPS0,dM_dkh/EPS0


def integrate_clipped(a:float,b:float,E:float,lo:float,hi:float,k:float,density:float=1.0)->Tuple[float,float]:
    """Exact N,M of clip(E*(EPS0-k*y),lo,hi) on y in [a,b]."""
    cuts=[a,b]
    if abs(k)>1e-18:
        for sth in (lo,hi):
            y=(EPS0-sth/E)/k
            if a<y<b:
                cuts.append(y)
    cuts=sorted(set(cuts))
    N=M=0.0
    for u,v in zip(cuts[:-1],cuts[1:]):
        mid=0.5*(u+v)
        trial=E*(EPS0-k*mid)
        if trial<=lo:
            aa,bb=lo,0.0
        elif trial>=hi:
            aa,bb=hi,0.0
        else:
            aa,bb=E*EPS0,-E*k
        aa*=density; bb*=density
        d1=v-u; d2=v*v-u*u; d3=v**3-u**3
        n=aa*d1+0.5*bb*d2
        first_y=0.5*aa*d2+(bb/3.0)*d3
        N+=n
        M+=H*n-first_y
    return N,M


def deriv_elastic(a:float,b:float,E:float,lo:float,hi:float,k:float,density:float=1.0)->Tuple[float,float]:
    """Exact dN/dk,dM/dk over the currently elastic part of a clipped affine steel law."""
    if k<=0.0:
        return 0.0,0.0
    y1=(EPS0-hi/E)/k
    y2=(EPS0-lo/E)/k
    u=max(a,min(y1,y2)); v=min(b,max(y1,y2))
    if v<=u:
        return 0.0,0.0
    Nk=density*(-E)*0.5*(v*v-u*u)
    Mk=density*(-E)*(H*0.5*(v*v-u*u)-(v**3-u**3)/3.0)
    return Nk,Mk


def section(k:float,c:Case)->Tuple[float,float,float,float]:
    Nc,Mc=core_peak(k,c.rho)
    Nck,Mck=core_peak_deriv(k,c.rho)
    parts=[
        (0.0,TC,ES,-FY,FY,c.rho),
        (-TS,0.0,ES,-FY,c.fcs,1.0),
        (TC,TC+TS,ES,-FY,c.fcs,1.0),
    ]
    N,M,Nk,Mk=Nc,Mc,Nck,Mck
    for a,b,E,lo,hi,d in parts:
        n,m=integrate_clipped(a,b,E,lo,hi,k,d)
        dn,dm=deriv_elastic(a,b,E,lo,hi,k,d)
        N+=n; M+=m; Nk+=dn; Mk+=dm
    return N,M,Nk,Mk


def P(q:float,c:Case)->float:
    return c.Pcr*q/(q+Q0)+c.C*q*(q+2.0*Q0)


def demand(q:float,s:float,c:Case)->Tuple[float,float]:
    Q=q*(q+2.0*Q0)
    n=P(q,c)*1e6/c.b+c.G*Q*(1.0-2.0*s*s)
    m=c.J*q*s
    return n,m


def k_for_n(n:float,c:Case)->float:
    N0=section(0.0,c)[0]
    if n>N0:
        raise ValueError('axial demand exceeds peak-anchor section maximum')
    hi=1e-7
    while hi<KAPPA_T*(1.0-1e-10) and section(hi,c)[0]>n:
        hi*=2.0
    hi=min(hi,KAPPA_T*(1.0-1e-10))
    if section(hi,c)[0]>n:
        raise ValueError('required root would activate UHPC tension')
    return brentq(lambda k:section(k,c)[0]-n,0.0,hi,xtol=1e-14,rtol=1e-12)


def endpoint_s1(c:Case)->Tuple[float,float,float,float,float]:
    """First positive s=1 intersection. q-bracketing is algebraic-parameter search, not spatial quadrature."""
    def F(q:float)->float:
        n,m=demand(q,1.0,c)
        try:
            k=k_for_n(n,c)
        except ValueError:
            return float('nan')
        return section(k,c)[1]-m
    xs=np.unique(np.concatenate((np.geomspace(1e-10,5e-2,2400),np.linspace(1e-8,5e-2,2400))))
    vals=[F(float(q)) for q in xs]
    brackets=[]
    for i in range(len(xs)-1):
        fa,fb=vals[i],vals[i+1]
        if np.isfinite(fa) and np.isfinite(fb) and fa*fb<0.0:
            brackets.append((float(xs[i]),float(xs[i+1])))
    if not brackets:
        raise RuntimeError('no admissible s=1 root')
    roots=[]
    for a,b in brackets:
        q=brentq(F,a,b,xtol=1e-13,rtol=1e-11)
        if not roots or abs(q-roots[-1])>1e-8:
            roots.append(q)
    q=min(roots)
    n,m=demand(q,1.0,c)
    k=k_for_n(n,c)
    return q,k,n,m,P(q,c)


def endpoint_s0(c:Case)->Tuple[float,float]:
    """Pure-axial peak-anchor candidate k=0, M=0."""
    N0=section(0.0,c)[0]
    def F(q): return demand(q,0.0,c)[0]-N0
    xs=np.geomspace(1e-10,1e-1,2500)
    vals=[F(float(q)) for q in xs]
    for i in range(len(xs)-1):
        if vals[i]*vals[i+1]<0.0:
            q=brentq(F,float(xs[i]),float(xs[i+1]))
            return q,P(q,c)
    raise RuntimeError('no s=0 endpoint root')


def stationary_res(x,c:Case)->np.ndarray:
    q,s,k=x
    N,M,Nk,Mk=section(float(k),c)
    n,m=demand(float(q),float(s),c)
    Q=q*(q+2.0*Q0)
    return np.array([
        (N-n)/1e4,
        (M-m)/1e5,
        (-4.0*c.G*Q*s*Mk-c.J*q*Nk)/1e10,
    ])


def interior_stationaries(c:Case,q1:float,k1:float)->List[Tuple[float,float,float]]:
    sols=[]
    for q0 in np.geomspace(max(q1*0.2,1e-7),q1*2.0,6):
        for s0 in np.linspace(0.1,0.9,5):
            for k0 in np.linspace(max(k1*0.3,1e-7),min(KAPPA_T*0.98,k1*1.5),5):
                sol=root(lambda x:stationary_res(x,c),[q0,s0,k0],tol=1e-11)
                if not sol.success:
                    continue
                q,s,k=map(float,sol.x)
                if not (q>0.0 and 0.0<s<1.0 and 0.0<k<KAPPA_T):
                    continue
                if np.max(np.abs(stationary_res(sol.x,c)))>1e-6:
                    continue
                if not any(abs(q-a[0])<1e-8 and abs(s-a[1])<1e-6 for a in sols):
                    sols.append((q,s,k))
    return sols


def main()->None:
    print('R14 Zhang peak-anchored exact strain-compatible Ny-My')
    print('formal thickness quadrature/material points = 0')
    print('case q kappa Pu_MN s0_Pu_MN interior_count bottom_core_strain error_pct')
    primary=[]
    for name,c in CASES.items():
        q,k,n,m,pu=endpoint_s1(c)
        _,p0=endpoint_s0(c)
        sta=interior_stationaries(c,q,k)
        bottom=EPS0-k*TC
        err=100.0*(pu/COMPARATOR[name]-1.0)
        print(f'{name:6s} {q:.12g} {k:.12g} {pu:.9f} {p0:.9f} {len(sta)} {bottom:.12g} {err:.9f}')
        if name!='BH050':
            primary.append(err)
    primary=np.array(primary,dtype=float)
    print('primary6_mean_signed_pct',float(np.mean(primary)))
    print('primary6_MAE_pct',float(np.mean(np.abs(primary))))
    print('primary6_RMSE_pct',float(np.sqrt(np.mean(primary**2))))


if __name__=='__main__':
    main()
