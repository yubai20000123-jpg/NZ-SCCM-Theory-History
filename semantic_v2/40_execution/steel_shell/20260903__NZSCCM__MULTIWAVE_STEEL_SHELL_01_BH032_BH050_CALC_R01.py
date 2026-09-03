from __future__ import annotations

"""NZ-SCCM Multiwave Steel Shell 01 -- BH032/BH050 no-slip execution R01.

Theory source:
  semantic_v2/20_theory/
  20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_01_NO_SHEAR_SLIP_FULL_DERIVATION_R01.md

Scope:
  - steel shell and UHPC fully bonded / no slip;
  - one complete global halfwave only;
  - standard equal-width steel cells use n0=floor(LG/s) and candidates n0-1,n0,n0+1;
  - non-standard edge strips are retained as full-thickness ideal-EP steel in this execution;
  - no qU, no partial interaction, no 99 independent local amplitudes, no effective width;
  - R06 local maximum uses the finite harmonic field. This script uses deterministic
    edge optimization plus interior screening for the nonlinear solve; final values are
    numerical execution results, not a theorem-level resultant certificate.
"""

import math
import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq, minimize_scalar, root

ES=206000.0; NU_S=0.30; FY=355.0
EC=43400.0; NU_C=0.20; FC=141.1; EPS_C0=0.0035
TS=4.0; TC=42.0; AW=1332.0; Q0=0.0025
HARM={(0,1):.5,(0,2):-.5,(1,0):.5,(1,1):-1.0,(1,2):.5,(2,0):-.5,(2,1):.5}

EPS_T=np.array([0.0,0.000420,0.003800,0.006900,0.007590])
SIG_T=np.array([0.0,9.767718,10.734818,10.347978,0.0])
PCHIP=PchipInterpolator(EPS_T,SIG_T,extrapolate=False)
AC=EC*EPS_C0/FC; BC=6.0-5.0*AC; CC=4.0*AC-5.0


def kp_num(r):
    return (272*r**16+2856*r**14+11273*r**12+23146*r**10+31506*r**8
            +23146*r**6+11273*r**4+2856*r**2+272)


def yun_kcr(r):
    return 4.0*(3*r**4+2*r**2+3)/(3*r**2)


class Cell:
    def __init__(self,Lx,Ly,A0):
        self.Lx=Lx; self.Ly=Ly; self.A0=A0
        self.kx=2*math.pi/Lx; self.ky=2*math.pi/Ly
        self.Q=ES/(1-NU_S**2)
        self.D=ES*TS**3/(12*(1-NU_S**2))
        self.cx=3*self.kx**2/8; self.cy=3*self.ky**2/8
        self.Kb=self.D*(.75*(self.kx**4+self.ky**4)+.5*self.kx**2*self.ky**2)
        r=self.kx/self.ky
        self.KA=self.ky**4*kp_num(r)/(256*(r*r+1)**2*(r*r+4)**2*(4*r*r+1)**2)
    def sigma_cr(self):
        return (math.pi**2*ES*TS**2/(12*(1-NU_S**2)*self.Lx**2)
                *yun_kcr(self.Ly/self.Lx))


def outer_params(b):
    a=2*b; rho=AW/(b*TC); zf=(TC+TS)/2
    Ks=ES/(1-NU_S**2); Kc=EC/(1-NU_C**2)
    Gs=ES/(2*(1+NU_S)); Gc=EC/(2*(1+NU_C))
    A11=2*TS*Ks+(1-rho)*TC*Kc
    A22=A11+rho*TC*ES
    A12=2*TS*NU_S*Ks+(1-rho)*TC*NU_C*Kc
    Df=2*Ks*(TS**3/12+TS*zf**2)
    Dc=(1-rho)*Kc*TC**3/12
    Dw=rho*ES*TC**3/12
    Dx=Df+Dc; Dy=Df+Dc+Dw
    Dmu=NU_S*Df+NU_C*Dc
    D66=2*Gs*(TS**3/12+TS*zf**2)+(1-rho)*Gc*TC**3/12
    H=Dmu+2*D66
    rows=[]
    for m in range(1,7):
        al=math.pi/b; be=m*math.pi/a
        Ncr=(Dx*al**4+2*H*al**2*be**2+Dy*be**4)/be**2
        rows.append((m,b*Ncr/1e6))
    mstar=min(rows,key=lambda t:t[1])[0]
    Pcr=min(rows,key=lambda t:t[1])[1]
    al=math.pi/b; be=mstar*math.pi/a
    DA=A11*A22-A12**2
    Kx=b*b*al*al/(8*(A22/DA))
    G=b*b*be*be/(8*(A11/DA))
    C=b**3*DA/(16*be**2)*(al**4/A22+be**4/A11)
    Jx=b*(Dx*al**2+Dmu*be**2)
    Jy=b*(Dmu*al**2+Dy*be**2)
    return dict(rho=rho,zf=zf,mstar=mstar,LG=a/mstar,Pcr=Pcr,Kx=Kx,G=G,C=C,Jx=Jx,Jy=Jy)


def amp_coeff(c,ex,ey):
    L0=c.Q*(c.cx*(ex+NU_S*ey)+c.cy*(ey+NU_S*ex))
    Cg=c.Q*(c.cx**2+c.cy**2+2*NU_S*c.cx*c.cy)
    B3=4*TS*ES*c.KA+2*TS*Cg
    B1=c.Kb-2*TS*L0-B3*c.A0**2
    B0=-c.Kb*c.A0
    return B3,B1,B0


def amp_energy(c,U,ex,ey):
    d=U*U-c.A0**2
    mx=ex-c.cx*d; my=ey-c.cy*d
    return (.5*c.Kb*(U-c.A0)**2
            +.5*TS*c.Q*(mx*mx+my*my+2*NU_S*mx*my)
            +TS*ES*c.KA*d*d)


def solve_amp(c,ex,ey):
    B3,B1,B0=amp_coeff(c,ex,ey)
    rr=np.roots([B3,0.0,B1,B0])
    roots=[float(z.real) for z in rr if abs(z.imag)<1e-8 and z.real>=-1e-10]
    return min(roots,key=lambda U:amp_energy(c,U,ex,ey))


def mean_phys(c,U,ex,ey):
    d=U*U-c.A0**2
    mx=ex-c.cx*d; my=ey-c.cy*d
    return np.array([-c.Q*(mx+NU_S*my),-c.Q*(my+NU_S*mx),0.0])


def vm2_uv(c,U,ex,ey,u,v):
    mean=mean_phys(c,U,ex,ey); d=U*U-c.A0**2
    shape=np.broadcast(u,v).shape
    sx=np.zeros(shape)+mean[0]; sy=np.zeros(shape)+mean[1]; ps=np.zeros(shape)
    for (m,n),h in HARM.items():
        src=h*c.kx**2*c.ky**2
        eig=((m*c.kx)**2+(n*c.ky)**2)**2
        F=ES*d*src/eig
        cm=1 if m==0 else (u if m==1 else 2*u*u-1)
        cn=1 if n==0 else (v if n==1 else 2*v*v-1)
        sx-= (n*c.ky)**2*F*cm*cn
        sy-= (m*c.kx)**2*F*cm*cn
        if m and n:
            fm=1 if m==1 else 2*u
            fn=1 if n==1 else 2*v
            ps-= (m*c.kx)*(n*c.ky)*F*fm*fn
    tau2=(1-u*u)*(1-v*v)*ps*ps
    return sx*sx-sx*sy+sy*sy+3*tau2


def local_max(c,U,ex,ey):
    g=np.linspace(-1,1,9); uu,vv=np.meshgrid(g,g,indexing='ij')
    best=float(np.max(vm2_uv(c,U,ex,ey,uu,vv)))
    for axis in (0,1):
        for sgn in (-1.0,1.0):
            if axis==0:
                fun=lambda z:-float(vm2_uv(c,U,ex,ey,sgn,z))
            else:
                fun=lambda z:-float(vm2_uv(c,U,ex,ey,z,sgn))
            r=minimize_scalar(fun,bounds=(-1,1),method='bounded',options={'xatol':1e-10})
            best=max(best,-r.fun)
    return best


def r06(c,epsx,epsy):
    ex=-epsx; ey=-epsy
    U=solve_amp(c,ex,ey); vmax=local_max(c,U,ex,ey)
    if vmax<=FY**2*(1+1e-9):
        return mean_phys(c,U,ex,ey),dict(eta=1.0,U=U,vmmax=math.sqrt(vmax))
    def f(eta):
        exi=-eta*epsx; eyi=-eta*epsy; Ui=solve_amp(c,exi,eyi)
        return local_max(c,Ui,exi,eyi)-FY**2
    eta=brentq(f,0,1,xtol=2e-10,rtol=2e-10)
    exi=-eta*epsx; eyi=-eta*epsy; U=solve_amp(c,exi,eyi)
    return mean_phys(c,U,exi,eyi),dict(eta=eta,U=U,vmmax=math.sqrt(local_max(c,U,exi,eyi)))


def ideal_ep(epsx,epsy):
    Q=ES/(1-NU_S**2)
    sx=Q*(epsx+NU_S*epsy); sy=Q*(epsy+NU_S*epsx)
    vm=math.sqrt(sx*sx-sx*sy+sy*sy)
    lam=min(1.0,FY/vm) if vm else 1.0
    return np.array([lam*sx,lam*sy,0.0])


# PCHIP analytic primitives
F0K=[0.0]; F1K=[0.0]
for j in range(len(EPS_T)-1):
    x0=EPS_T[j]; h=EPS_T[j+1]-x0
    d,c,b,a=PCHIP.c[:,j]
    I0=a*h+b*h**2/2+c*h**3/3+d*h**4/4
    I1=x0*I0+a*h**2/2+b*h**3/3+c*h**4/4+d*h**5/5
    F0K.append(F0K[-1]+I0); F1K.append(F1K[-1]+I1)


def F0(e):
    if e<=0:
        x=-e/EPS_C0
        return FC*EPS_C0*(AC*x*x/2+BC*x**6/6+CC*x**7/7)
    j=min(np.searchsorted(EPS_T,e,side='right')-1,len(EPS_T)-2)
    x0=EPS_T[j]; s=e-x0; d,c,b,a=PCHIP.c[:,j]
    return F0K[j]+a*s+b*s*s/2+c*s**3/3+d*s**4/4


def F1(e):
    if e<=0:
        x=-e/EPS_C0
        return -FC*EPS_C0**2*(AC*x**3/3+BC*x**7/7+CC*x**8/8)
    j=min(np.searchsorted(EPS_T,e,side='right')-1,len(EPS_T)-2)
    x0=EPS_T[j]; s=e-x0; d,c,b,a=PCHIP.c[:,j]
    I0=a*s+b*s*s/2+c*s**3/3+d*s**4/4
    return F1K[j]+x0*I0+a*s*s/2+b*s**3/3+c*s**4/4+d*s**5/5


def uhpc_NM(e0,k,rho):
    ep=e0+k*TC/2; em=e0-k*TC/2
    if -EPS_C0-1e-8<=ep<-EPS_C0: ep=-EPS_C0
    if -EPS_C0-1e-8<=em<-EPS_C0: em=-EPS_C0
    if min(ep,em)<-EPS_C0 or max(ep,em)>EPS_T[-1]: return None
    fac=1-rho
    if abs(k)<1e-12:
        if e0<0:
            x=-e0/EPS_C0; sig=-FC*(AC*x+BC*x**5+CC*x**6)
        else: sig=float(PCHIP(e0))
        return fac*TC*sig,0.0,ep,em
    df0=F0(ep)-F0(em); df1=F1(ep)-F1(em)
    return fac*df0/k,fac*(df1-e0*df0)/k**2,ep,em


def web_NM(e0,k,rho):
    z0,z1=-TC/2,TC/2; ey=FY/ES; zz=[z0,z1]
    if abs(k)>1e-14:
        for e in (-ey,ey):
            z=(e-e0)/k
            if z0<z<z1: zz.append(z)
    zz=sorted(zz); N=M=0.0
    for a,b in zip(zz[:-1],zz[1:]):
        mid=.5*(a+b); e=e0+k*mid
        if e<=-ey: sig=-FY; N+=sig*(b-a); M+=sig*(b*b-a*a)/2
        elif e>=ey: sig=FY; N+=sig*(b-a); M+=sig*(b*b-a*a)/2
        else:
            N+=ES*(e0*(b-a)+k*(b*b-a*a)/2)
            M+=ES*(e0*(b*b-a*a)/2+k*(b**3-a**3)/3)
    return rho*N,rho*M


def cells(b):
    s=.225*b; A0=s/1600; LG=b
    return {n:Cell(s,LG/n,A0) for n in (3,4,5)}


def face_stress(b,epsx,epsy,face,counts):
    E=ideal_ep(epsx,epsy); cc=cells(b); loc={}
    for n in (3,4,5):
        loc[n]=E if cc[n].sigma_cr()>=FY else r06(cc[n],epsx,epsy)[0]
    # actual BH same-side PBL layout: regular bays have width 0.225B.
    # Non-standard edge residual strips are E in this execution specialization.
    wE=.325 if face=='+' else .1
    w=.225
    return wE*E+w*(counts[0]*loc[3]+counts[1]*loc[4]+counts[2]*loc[5])


def residual5(x,b,ct,cb):
    ex0,kx,ey0,ky,q=x; o=outer_params(b); zf=o['zf']
    UX=uhpc_NM(ex0,kx,o['rho']); UY=uhpc_NM(ey0,ky,o['rho'])
    if UX is None or UY is None: return np.ones(5)*100
    Nw,Mw=web_NM(ey0,ky,o['rho'])
    top=face_stress(b,ex0+kx*zf,ey0+ky*zf,'+',ct)
    bot=face_stress(b,ex0-kx*zf,ey0-ky*zf,'-',cb)
    Nxs=TS*(top[0]+bot[0]); Mxs=TS*zf*(top[0]-bot[0])
    Nys=TS*(top[1]+bot[1]); Mys=TS*zf*(top[1]-bot[1])
    Q=q*(q+2*Q0); P=o['Pcr']*1e6*q/(q+Q0)+o['C']*Q
    demand=np.array([o['Kx']*Q,o['Jx']*q,-(P/b-o['G']*Q),o['Jy']*q])
    sec=np.array([UX[0]+Nxs,UX[1]+Mxs,UY[0]+Nys+Nw,UY[1]+Mys+Mw])
    R=(sec-demand)/np.array([5000.,30000.,7000.,30000.])
    return np.r_[R,(UY[3]+EPS_C0)/EPS_C0]


PATTERNS={
    'ALL_n0':((0,3,0),(0,4,0)),
    'BALANCED':((1,1,1),(1,2,1)),
    'ALL_nminus':((3,0,0),(4,0,0)),
    'ALL_nplus':((0,0,3),(0,0,4)),
}

GUESSES={
    1600:np.array([1.6e-4,2.1e-5,-.00249,4.8e-5,.00145]),
    2500:np.array([1.2e-5,4.5e-5,-.00213,6.52e-5,.00522]),
}

if __name__=='__main__':
    for b in (1600.0,2500.0):
        o=outer_params(b); print('\nCASE',b,'m*',o['mstar'],'LG',o['LG'],'Pcr',o['Pcr'])
        print('sigma_cr n=3/4/5',[cells(b)[n].sigma_cr() for n in (3,4,5)])
        for name,(ct,cb) in PATTERNS.items():
            sol=root(lambda x:residual5(x,b,ct,cb),GUESSES[b],method='hybr',options={'xtol':5e-9,'maxfev':500})
            if not sol.success or np.linalg.norm(residual5(sol.x,b,ct,cb))>1e-5:
                sol=root(lambda x:residual5(x,b,ct,cb),GUESSES[b],method='lm')
            q=sol.x[-1]; Q=q*(q+2*Q0); P=o['Pcr']*1e6*q/(q+Q0)+o['C']*Q
            print(name,'success=',sol.success,'state=',sol.x,'P_MN=',P/1e6,
                  'scaled_res_norm=',np.linalg.norm(residual5(sol.x,b,ct,cb)))
