from __future__ import annotations

"""Finite resultant-only RC shell-capacity diagnostic for Swartz common-8.

Architecture:
    frozen Marguerre-Air y demand -> finite RC shell resultant feasibility -> Pu.

No concrete strain history, point concrete stress path, CC/TC/TT states,
thickness integration, material-point grid, or experimental load is used by the
solver.  Pf is printed only after q_u is frozen.

This is an R01 diagnostic, not a production solver.  The terminal model follows
Brondum-Nielsen's ultimate-limit resultant philosophy, with source-faithful
neglect of tensile concrete and compression reinforcement.
"""

import math
import numpy as np
from scipy.optimize import minimize

B = 1220.0
NU = 0.18
ES = 200000.0
FY = 530.0
Q0 = 1.0 / 400.0

CASES = {
    4: dict(t=25.40,fc=23.63,E0=23772.,p=.0050,hr=9.20,L=2,ell=2440./3.,Pf=534.231415992786),
    5: dict(t=25.40,fc=22.72,E0=21460.,p=.0075,hr=9.20,L=2,ell=2440./3.,Pf=623.640670459522),
    6: dict(t=26.40,fc=24.43,E0=18058.,p=.0075,hr=9.70,L=2,ell=2440./3.,Pf=691.6984611730078),
    8: dict(t=24.64,fc=22.05,E0=20830.,p=.0100,hr=8.82,L=2,ell=610.,Pf=455.0530712411491),
    9: dict(t=31.75,fc=17.67,E0=15480.,p=.0020,hr=0.,L=1,ell=2440./3.,Pf=625.8647812671522),
    14:dict(t=32.26,fc=19.79,E0=17995.,p=.0075,hr=12.63,L=2,ell=2440.,Pf=716.1636800569404),
    21:dict(t=19.30,fc=24.98,E0=20321.,p=.0075,hr=0.,L=1,ell=1220.,Pf=368.3127497435694),
    23:dict(t=19.38,fc=23.40,E0=23818.,p=.0100,hr=0.,L=1,ell=2440./3.,Pf=346.96128599031897),
}


def structural(c):
    t,E0,p,hr,L,ell=c['t'],c['E0'],c['p'],c['hr'],c['L'],c['ell']
    # Project-corrected Swartz interpretation: p is total two-direction ratio.
    As_dir_total=p*t/2.0
    As_layer=As_dir_total/L
    zs=np.array([0.0]) if L==1 else np.array([-hr,+hr],dtype=float)
    den=1.0-NU**2
    Q=E0/den; Q12=NU*E0/den; Q66=E0/(2.0*(1.0+NU))
    tconc=t-2.0*As_dir_total
    A11=Q*tconc+ES*As_dir_total
    A22=A11; A12=Q12*tconc
    Ig=t**3/12.0
    Iconc=Ig-np.sum(2.0*As_layer*zs**2)
    Dx=Q*Iconc+ES*np.sum(As_layer*zs**2)
    Dy=Dx; Dmu=Q12*Iconc; D66=Q66*Iconc; H=Dmu+2.0*D66
    alpha=math.pi/B; beta=math.pi/ell
    Delta=A11*A22-A12*A12
    Pcr=B*(Dx*alpha**4+2.0*H*alpha**2*beta**2+Dy*beta**4)/(beta**2)/1000.0
    Kx=B**2*alpha**2*Delta/(8.0*A22)
    Ky=B**2*beta**2*Delta/(8.0*A11)
    C=B/2.0*(Ky+Kx*alpha**2/beta**2)/1000.0
    Jx=B*(Dx*alpha**2+Dmu*beta**2)
    Jy=B*(Dmu*alpha**2+Dy*beta**2)
    d=np.array([alpha**2,beta**2],dtype=float)
    d/=np.linalg.norm(d)
    return dict(As=As_layer,zs=zs,Pcr=Pcr,Kx=Kx,Ky=Ky,C=C,Jx=Jx,Jy=Jy,d=d)


def demand(c,q):
    s=structural(c); Qg=q*(q+2.0*Q0)
    P=s['Pcr']*q/(q+Q0)+s['C']*Qg
    Nx=+s['Kx']*Qg
    Ny=-(P*1000.0/B-s['Ky']*Qg)
    Mx=s['Jx']*q; My=s['Jy']*q
    return P,Nx,Ny,Mx,My


def solve(c,nstarts=50):
    st=structural(c); L=c['L']; zs=st['zs']; As=st['As']; fc=c['fc']; t=c['t']; h=t/2.0
    d=st['d']; capS=As*FY
    # x=[q,ct,cb,Cxt,Cxb,Cyt,Cyb,Sx_i...,Sy_i...]
    iSx=7; iSy=7+L; nvar=7+2*L
    bounds=[(1e-8,.1),(0,t),(0,t),(-fc*t,0),(-fc*t,0),(-fc*t,0),(-fc*t,0)] \
           +[(0,capS)]*(2*L)

    def eq(x):
        q,ct,cb=x[:3]; zt=h-ct/2.0; zb=-h+cb/2.0
        P,Nx,Ny,Mxd,Myd=demand(c,q)
        Sx=x[iSx:iSx+L]; Sy=x[iSy:iSy+L]
        Mxu=zt*x[3]+zb*x[4]+np.dot(zs,Sx)
        Myu=zt*x[5]+zb*x[6]+np.dot(zs,Sy)
        return np.array([
            x[3]+x[4]+Sx.sum()-Nx,
            x[5]+x[6]+Sy.sum()-Ny,
            d[0]*Mxu+d[1]*Myu-(d[0]*Mxd+d[1]*Myd),
        ])

    def ine(x):
        q,ct,cb=x[:3]
        return np.array([
            t-ct-cb,
            x[3]+fc*ct, x[5]+fc*ct,
            x[4]+fc*cb, x[6]+fc*cb,
        ])

    cons=[{'type':'eq','fun':eq},{'type':'ineq','fun':ine}]
    rng=np.random.default_rng(777+int(t*100)); best=None
    for _ in range(nstarts):
        q0=10.0**rng.uniform(-4.0,-1.4)
        ct=rng.uniform(.02*t,.8*t); cb=rng.uniform(.02*t,.8*t)
        if ct+cb>t:
            sc=.98*t/(ct+cb); ct*=sc; cb*=sc
        x=np.zeros(nvar); x[:3]=[q0,ct,cb]
        P,Nx,Ny,_,_=demand(c,q0)
        x[5]=max(-fc*ct,Ny/2.0); x[6]=max(-fc*cb,Ny-x[5])
        x[iSx:iSx+L]=np.clip(max(0.0,Nx)/L,0.0,capS)
        rr=minimize(lambda xx:-xx[0],x,method='SLSQP',bounds=bounds,constraints=cons,
                    options={'ftol':1e-10,'maxiter':1800})
        if rr.success and np.linalg.norm(eq(rr.x))<2e-5 and np.min(ine(rr.x))>-2e-6:
            if best is None or rr.x[0]>best.x[0]:
                best=rr
    if best is None:
        raise RuntimeError('no finite resultant-capacity solution')
    q=float(best.x[0]); P=float(demand(c,q)[0])
    return q,P


def main():
    errs=[]
    print('case,ell_rep_mm,q_u,Pu_kN,Pf_kN,error_pct')
    for case,c in CASES.items():
        q,P=solve(c)
        e=(P/c['Pf']-1.0)*100.0; errs.append(e)
        print(f"{case},{c['ell']:.10f},{q:.10f},{P:.10f},{c['Pf']:.10f},{e:.8f}")
    a=np.asarray(errs)
    print('mean_signed_pct',a.mean())
    print('MAE_pct',np.abs(a).mean())
    print('RMSE_pct',np.sqrt(np.mean(a*a)))


if __name__ == '__main__':
    main()
