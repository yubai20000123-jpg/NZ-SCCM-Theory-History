from __future__ import annotations

"""R03 membrane work-conjugacy diagnostic for the fixed Swartz common-8.

Three controlled terminal variants use the SAME Marguerre-Air y structural
front end and the SAME resultant-only Brondum-Nielsen-family strength bounds:
  A hard shell point: Nx + Ny + M_parallel
  B release hard Nx, retain local projected M_parallel
  C axial y-normal cut: Ny + My

No pointwise concrete stress/strain law, thickness material quadrature,
material-point grid, generic optimizer, or experimental load enters root selection.
"""

import math
import numpy as np
from scipy.optimize import brentq

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
    As_total=p*t/2.0
    As=As_total/L
    zs=np.array([0.0]) if L==1 else np.array([-hr,+hr])
    den=1.0-NU**2
    Q=E0/den; Q12=NU*E0/den; Q66=E0/(2.0*(1.0+NU))
    tconc=t-2.0*As_total
    A11=Q*tconc+ES*As_total; A12=Q12*tconc
    Iconc=t**3/12.0-np.sum(2.0*As*zs**2)
    D=Q*Iconc+ES*np.sum(As*zs**2)
    Dmu=Q12*Iconc; D66=Q66*Iconc; H=Dmu+2.0*D66
    alpha=math.pi/B; beta=math.pi/ell
    Delta=A11*A11-A12*A12
    Pcr=B*(D*alpha**4+2.0*H*alpha**2*beta**2+D*beta**4)/beta**2/1000.0
    Kx=B**2*alpha**2*Delta/(8.0*A11)
    Ky=B**2*beta**2*Delta/(8.0*A11)
    C=B/2.0*(Ky+Kx*alpha**2/beta**2)/1000.0
    Jx=B*(D*alpha**2+Dmu*beta**2)
    Jy=B*(Dmu*alpha**2+D*beta**2)
    d=np.array([alpha**2,beta**2]); d/=np.linalg.norm(d)
    return dict(As=As,zs=zs,Pcr=Pcr,Kx=Kx,Ky=Ky,C=C,Jx=Jx,Jy=Jy,d=d)


def demand(c,q):
    s=structural(c); Q=q*(q+2.0*Q0)
    P=s['Pcr']*q/(q+Q0)+s['C']*Q
    Nx=s['Kx']*Q
    Ny=-(P*1000.0/B-s['Ky']*Q)
    return P,Nx,Ny,s['Jx']*q,s['Jy']*q


def roots(fun,qmin=1e-7,qmax=.03,n=4000):
    qs=np.geomspace(qmin,qmax,n)
    vv=[float(fun(q)) for q in qs]
    out=[]
    for a,b,fa,fb in zip(qs[:-1],qs[1:],vv[:-1],vv[1:]):
        if not (np.isfinite(fa) and np.isfinite(fb)): continue
        if fa==0.0: r=a
        elif fa*fb<0.0: r=brentq(fun,a,b,xtol=1e-13,rtol=1e-12)
        else: continue
        if r>0 and all(abs(r-x)>1e-9 for x in out): out.append(r)
    return out


def solve_hard_shell_point(case,c):
    """R02 exact active families: hard Nx, Ny and projected M_parallel."""
    s=structural(c); h=c['t']/2.0; fc=c['fc']; Fs=s['As']*FY; d=s['d']
    if case in (4,5,6,8,9,23):
        zplus=c['hr'] if c['L']==2 else 0.0
        Ty=Fs if c['L']==2 else 0.0; Tx=Fs
        def f(q):
            _,Nx,Ny,Mxd,Myd=demand(c,q)
            cb=(Ty-Ny)/fc; zb=-h+cb/2.0
            Mxu=zb*(Nx-Tx)+zplus*Tx
            Myu=zb*(-fc*cb)+zplus*Ty
            return d[0]*Mxu+d[1]*Myu-(d[0]*Mxd+d[1]*Myd)
        aa=[]
        for q in roots(f):
            _,Nx,Ny,_,_=demand(c,q)
            cb=(Ty-Ny)/fc; Cxb=Nx-Tx
            if 0<=cb<=c['t'] and -fc*cb<=Cxb<=0: aa.append(q)
        return max(aa)
    if case==21:
        def cb(q):
            _,Nx,_,_,_=demand(c,q)
            return h+d[0]*(Nx-Fs)/(2.0*d[1]*fc)
        def f(q):
            _,Nx,_,Mxd,Myd=demand(c,q); cc=cb(q); zb=-h+cc/2.0
            Mpu=zb*(d[0]*(Nx-Fs)-d[1]*fc*cc)
            return Mpu-(d[0]*Mxd+d[1]*Myd)
        aa=[]
        for q in roots(f):
            _,Nx,Ny,_,_=demand(c,q); cc=cb(q)
            Sy=Ny+fc*cc; Cxb=Nx-Fs
            if 0<=cc<=c['t'] and 0<=Sy<=Fs and -fc*cc<=Cxb<=0: aa.append(q)
        return max(aa)
    if case==14:
        return max(roots(lambda q:demand(c,q)[2]+fc*c['t']))
    raise KeyError(case)


def solve_release_Nx_projected(c):
    """Release hard Nx, retain local shell-point M_parallel."""
    s=structural(c); h=c['t']/2.0; fc=c['fc']; Fs=s['As']*FY; d=s['d']
    zplus=c['hr'] if c['L']==2 else 0.0
    def f(q):
        _,_,Ny,Mxd,Myd=demand(c,q)
        lo=max(0.0,-Ny/fc)
        hi=min(c['t'],(Fs-Ny)/fc)
        if lo>hi: return -1e12
        cb0=h+d[1]*zplus/(d[0]+d[1])
        cb=min(max(cb0,lo),hi)
        Ty=Ny+fc*cb
        base=fc*cb*(h-cb/2.0)
        Mxu=base+zplus*Fs
        Myu=base+zplus*Ty
        return d[0]*Mxu+d[1]*Myu-(d[0]*Mxd+d[1]*Myd)
    return max(roots(f))


def solve_axial_cut(c):
    """Selected y-normal collapse cut: hard Ny and My only."""
    s=structural(c); h=c['t']/2.0; fc=c['fc']; Fs=s['As']*FY
    zplus=c['hr'] if c['L']==2 else 0.0
    def f(q):
        _,_,Ny,_,Myd=demand(c,q)
        lo=max(0.0,-Ny/fc)
        hi=min(c['t'],(Fs-Ny)/fc)
        if lo>hi: return -1e12
        cb=min(max(h+zplus,lo),hi)
        Ty=Ny+fc*cb
        Myu=fc*cb*(h-cb/2.0)+zplus*Ty
        return Myu-Myd
    return max(roots(f))


def main():
    ea=[]; eb=[]; ec=[]
    print('case,ell_mm,q_hard,Pu_hard,q_releaseNx,Pu_releaseNx,q_axialcut,Pu_axialcut,Pf,error_hard,error_releaseNx,error_axialcut')
    for case,c in CASES.items():
        qa=solve_hard_shell_point(case,c)
        qb=solve_release_Nx_projected(c)
        qc=solve_axial_cut(c)
        Pa=demand(c,qa)[0]; Pb=demand(c,qb)[0]; Pc=demand(c,qc)[0]; Pf=c['Pf']
        ee=[(Pa/Pf-1)*100,(Pb/Pf-1)*100,(Pc/Pf-1)*100]
        ea.append(ee[0]); eb.append(ee[1]); ec.append(ee[2])
        print(f'{case},{c["ell"]:.10f},{qa:.12f},{Pa:.9f},{qb:.12f},{Pb:.9f},{qc:.12f},{Pc:.9f},{Pf:.9f},{ee[0]:.8f},{ee[1]:.8f},{ee[2]:.8f}')
    for name,a in [('HARD',ea),('RELEASE_NX_PROJECTED',eb),('AXIAL_CUT',ec)]:
        a=np.asarray(a)
        print(name,'mean_signed',a.mean(),'MAE',np.abs(a).mean(),'RMSE',np.sqrt(np.mean(a*a)))


if __name__=='__main__':
    main()
