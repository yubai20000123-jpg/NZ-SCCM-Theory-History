"""R11: exact FHWA strain-compatible steel-shell UHPC Ny-My terminal.

Formal identities
-----------------
- Full 2D Marguerre-Airy structural front is frozen.
- y-normal terminal is Ny-My.
- UHPC compression: FHWA alpha_u=0.85 elastic-to-plateau model, eps_cu=0.0035.
- UHPC tension is suppressed in R11 to isolate compression-model effects.
- External faces/web share one linear axial strain field; steel is elastic-perfectly plastic,
  with existing Yun compression caps retained where applicable.
- Every through-thickness integral is exact; no thickness quadrature/material points.
- Control-location formal candidates are s=0, s=1, and interior stationary roots.

BH structural coefficients are the R08 frozen coefficients at the precision stored in that
report. T120/T360 use the R08 physical-length-corrected coefficients.
"""
from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Dict, Tuple
import numpy as np
from scipy.optimize import brentq, root

FC=141.1
EC=43400.0
ALPHA_U=0.85
SIGP=ALPHA_U*FC
EPS_CU=0.0035
ES=206000.0
FY=355.0
TC=42.0
TS=4.0
H=TC/2.0
Q0=0.0025

@dataclass(frozen=True)
class Case:
    b: float
    Pcr: float   # MN
    C: float     # MN
    G: float     # N/mm
    J: float     # N
    rho: float
    fcs: float   # MPa compression cap of each external face

CASES: Dict[str,Case]={
    'T120':Case(1600.,30.822799056,7284.21452557,5.412338111e6,1.118592686e7,0.05506,355.0),
    'T360':Case(1600.,30.751943803,7055.99557435,5.074760452e6,1.095253234e7,0.01982,301.87133),
    'BH005':Case(250.,197.5373,1179.2700,5.3614e6,6.7473e7,0.12685714,355.0),
    'BH010':Case(500.,98.3195,2253.6479,4.8274e6,3.2496e7,0.06342857,355.0),
    'BH020':Case(1000.,49.0475,4400.9325,4.5604e6,1.5938e7,0.03171429,355.0),
    'BH032':Case(1600.,30.6284,6977.1939,4.4603e6,9.8889e6,0.01982143,295.42),
    'BH050':Case(2500.,19.5920,10841.3718,4.4002e6,6.3010e6,0.01268571,250.07),
}


def integrate_clipped(a:float,b:float,E:float,lo:float,hi:float,k:float,density:float=1.0)->Tuple[float,float]:
    """Exact N,M of clip(E*(EPS_CU-k*y),lo,hi) on y in [a,b]."""
    cuts=[a,b]
    if abs(k)>1e-16:
        for sth in (lo,hi):
            y=(EPS_CU-sth/E)/k
            if a<y<b: cuts.append(y)
    cuts=sorted(set(cuts))
    N=M=0.0
    for u,v in zip(cuts[:-1],cuts[1:]):
        mid=(u+v)/2.0
        trial=E*(EPS_CU-k*mid)
        if trial<=lo: A,B=lo,0.0
        elif trial>=hi: A,B=hi,0.0
        else: A,B=E*EPS_CU,-E*k
        A*=density; B*=density
        d1=v-u; d2=v*v-u*u; d3=v**3-u**3
        n=A*d1+0.5*B*d2
        first_y=0.5*A*d2+(B/3.0)*d3
        N+=n
        M+=H*n-first_y
    return N,M


def deriv_elastic(a,b,E,lo,hi,k,density=1.0):
    """Exact dN/dk,dM/dk; clip-boundary terms cancel by stress continuity."""
    if k<=0: return 0.0,0.0
    yl=(EPS_CU-hi/E)/k
    yh=(EPS_CU-lo/E)/k
    u=max(a,min(yl,yh)); v=min(b,max(yl,yh))
    if v<=u: return 0.0,0.0
    Nk=density*(-E)*0.5*(v*v-u*u)
    Mk=density*(-E)*(H*0.5*(v*v-u*u)-(v**3-u**3)/3.0)
    return Nk,Mk


def section(k:float,c:Case):
    parts=[
        (-TS,0.,ES,-FY,c.fcs,1.0),
        (0.,TC,EC,0.,SIGP,1.0-c.rho),
        (0.,TC,ES,-FY,FY,c.rho),
        (TC,TC+TS,ES,-FY,c.fcs,1.0),
    ]
    N=M=Nk=Mk=0.0
    for a,b,E,lo,hi,d in parts:
        n,m=integrate_clipped(a,b,E,lo,hi,k,d)
        dn,dm=deriv_elastic(a,b,E,lo,hi,k,d)
        N+=n; M+=m; Nk+=dn; Mk+=dm
    return N,M,Nk,Mk


def P(q:float,c:Case)->float:
    return c.Pcr*q/(q+Q0)+c.C*q*(q+2*Q0)


def demand(q:float,s:float,c:Case):
    Q=q*(q+2*Q0)
    n=P(q,c)*1e6/c.b+c.G*Q*(1-2*s*s)
    m=c.J*q*s
    return n,m


def k_for_n(n:float,c:Case):
    N0=section(0.0,c)[0]
    if n>N0: raise ValueError('axial demand exceeds section maximum')
    hi=1e-6
    while section(hi,c)[0]>n: hi*=2.0
    return brentq(lambda k:section(k,c)[0]-n,0.0,hi,xtol=1e-14,rtol=1e-12)


def endpoint_s1(c:Case):
    Nmax=section(0.0,c)[0]
    def axial(q): return demand(q,1.0,c)[0]-Nmax
    hi=1e-8
    while axial(hi)<0: hi*=2.0
    qa=brentq(axial,0.0,hi)
    def F(q):
        n,m=demand(q,1.0,c)
        k=k_for_n(n,c)
        return section(k,c)[1]-m
    q=brentq(F,1e-12,qa*(1-1e-10),xtol=1e-13,rtol=1e-11)
    n,m=demand(q,1.0,c); k=k_for_n(n,c)
    return q,k,n,m,P(q,c)


def stationary_res(x,c:Case):
    q,s,k=x
    N,M,Nk,Mk=section(k,c)
    n,m=demand(q,s,c)
    Q=q*(q+2*Q0)
    return np.array([
        (N-n)/1e4,
        (M-m)/1e5,
        (-4*c.G*Q*s*Mk-c.J*q*Nk)/1e10,
    ])


def interior_stationaries(c:Case):
    """Deterministic algebraic-root discovery for the finite stationary candidate family."""
    sols=[]
    for q0 in np.geomspace(1e-5,3e-2,6):
        for s0 in np.linspace(.1,.9,5):
            for k0 in np.geomspace(1e-5,3e-4,5):
                sol=root(lambda x:stationary_res(x,c),[q0,s0,k0],tol=1e-11)
                if sol.success:
                    q,s,k=map(float,sol.x)
                    if q>0 and 0<s<1 and k>0 and np.max(np.abs(stationary_res(sol.x,c)))<1e-7:
                        if not any(abs(q-a[0])<1e-7 and abs(s-a[1])<1e-5 for a in sols):
                            sols.append((q,s,k))
    return sols


def main():
    print('FHWA exact strain-compatible Ny-My R11')
    print('formal thickness quadrature/material points = 0')
    print('case q kappa n M Pu_MN interior_stationary_count')
    for name,c in CASES.items():
        q,k,n,m,pu=endpoint_s1(c)
        sta=interior_stationaries(c)
        print(f'{name:6s} {q:.12g} {k:.12g} {n:.6f} {m:.6f} {pu:.9f} {len(sta)}')

if __name__=='__main__':
    main()
