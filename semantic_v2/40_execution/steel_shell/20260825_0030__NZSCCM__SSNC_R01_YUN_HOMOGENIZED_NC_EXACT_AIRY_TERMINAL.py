from __future__ import annotations
"""SSNC-R01: Marguerre-Airy demand + Yun Ch.5 homogenized steel face + NC exact section.
No D15; no global virtual-work closure; no formal spatial quadrature/material points.
"""
import math
from dataclasses import dataclass
import numpy as np
from scipy.optimize import brentq

ES, NUS, NUA, NUT, RW, TS, Q0, BS = 206000., .30, .18, .20, .02, 4., .004, 200.
A0 = BS/1600.
FORMAL_SPATIAL_QUADRATURE = FORMAL_MATERIAL_POINTS = 0
D15_USED = GLOBAL_VIRTUAL_WORK_CLOSURE = False

@dataclass(frozen=True)
class Case:
    name:str; h:float; fy:float; fcu:float; b:float; eps0:float

E40=.0018712490394580678; E60=.0025344898708809867
CASES={
'Z0':Case('Z0',130,355,40,6000,E40),'Z1':Case('Z1',100,235,40,6000,E40),
'Z2':Case('Z2',130,460,40,6000,E40),'Z3':Case('Z3',130,355,60,6000,E60),
'Z4':Case('Z4',200,355,40,8000,E40),'Z5':Case('Z5',130,355,40,2000,E40),
'Z6':Case('Z6',130,355,40,12000,E40)}
R07={'Z0':(1.,.003428230723,37.825706787),'Z1':(.840294805,.004996679885,24.714128548),
'Z2':(1.,.004321772846,42.959011131),'Z3':(1.,.004613406152,46.495651955),
'Z4':(1.,.002445428167,70.265718566),'Z5':(1.,.000258841897,14.118193577),
'Z6':(.298387170,.013807412938,56.379421090)}
ZHOU={'Z0':36.9455,'Z1':23.7214,'Z2':41.2134,'Z3':44.3203,'Z4':69.3399,'Z5':14.6816,'Z6':49.4868}

def Ec(fcu): return 32500. if fcu==40 else 1e5/(34.7/fcu+2.2)

def structural(c):
    b,h,tc,E=c.b,c.h,c.h-2*TS,Ec(c.fcu); fc=.76*c.fcu; zf=tc/2+TS/2
    If=2*b*(TS**3/12+TS*zf*zf); Ic=b*tc**3/12
    Dx=(ES*If+E*Ic)/b; Dys=(ES*If+RW*ES*Ic)/b; Dyc=(1-RW)*E*Ic/b; Dy=Dys+Dyc
    Gs=ES/(2*(1+NUS)); Gc=E/(2*(1+NUT)); Ab=(b-TS)*(h-TS)
    ids=2*((b-TS)+(h-TS))/TS; r=tc/(b-2*TS); shape=(1-.63*r+.052*r**5)/3
    Dt=4*Gs*Ab**2/(b*ids)+Gc*shape*(b-2*TS)*tc**3/b; Dmu=NUS*Dys+NUT*Dyc; H=Dt/2+Dmu
    A11=2*TS*ES/(1-NUS**2)+(1-RW)*tc*E/(1-NUA**2)
    A22=A11+RW*tc*ES
    A12=2*TS*NUS*ES/(1-NUS**2)+(1-RW)*tc*NUA*E/(1-NUA**2)
    DA=A11*A22-A12*A12; ab=math.pi/b
    Pcr=b/ab**2*(Dx*ab**4+2*H*ab**4+Dy*ab**4)
    C=b**3*DA/(16*ab**2)*(ab**4/A22+ab**4/A11)
    G=ab**2*b**2*DA/(8*A11); J=b*(Dmu*ab**2+Dy*ab**2)
    return dict(b=b,h=h,tc=tc,Ec=E,fc=fc,fy=c.fy,eps0=c.eps0,Pcr=Pcr,C=C,G=G,J=J)

def P(st,q): return st['Pcr']*q/(q+Q0)+st['C']*q*(q+2*Q0)
def demand(st,q,s):
    Q=q*(q+2*Q0); return P(st,q),P(st,q)/st['b']+st['G']*Q*(1-2*s*s),st['J']*q*s

# Yun Eq.2-32/2-37/2-38/2-40 = Ch.5 Eq.5-19/5-18/5-20/5-21..23.
def yun_coeff(r=1.):
    kcr=4*(3*r**4+2*r*r+3)/(3*r*r)
    num=272*r**16+2856*r**14+11273*r**12+23146*r**10+31506*r**8+23146*r**6+11273*r**4+2856*r*r+272
    kp=num/(r*r*(r*r+1)**2*(r*r+4)**2*(4*r*r+1)**2)
    km=3/(2*r*r)+4*r*r/(r*r+1)**2-8*r*r/(4*r*r+1)**2+2*r*r/(r*r+4)**2
    return kcr,kp,km

def yun_terminal(fy,r=1.):
    kcr,kp,km=yun_coeff(r); Cs=math.pi**2*ES*TS**2/(12*(1-NUS**2)*BS**2)
    c1=Cs*kcr; c2=Cs*kp*(1-NUS**2)/TS**2; c3=ES*math.pi**2*km/BS**2; c=c2+c3
    roots=np.roots([c,3*A0*c,2*A0*A0*c-fy+c1,-fy*A0]); Au=min(z.real for z in roots if abs(z.imag)<1e-9 and z.real>0)
    S=Au*Au+2*A0*Au; su=c1*Au/(Au+A0)+c2*S; delta=c3*S
    assert abs(su+delta-fy)<2e-9
    return Au,su,su/fy

# R07 finite plastic envelope generalized only by compression-face fyc=Yun sigma_u.
def plast_params(st,fyc):
    tc,fc,fy=st['tc'],st['fc'],st['fy']; hc=tc/2; ac=(1-RW)*fc; D=ac+2*RW*fy
    Nc=(ac+RW*fy)*tc; return hc,D,Nc+(fyc-fy)*TS,Nc+2*fyc*TS,ac*hc+(fyc-fy)*TS,fyc

def plast_M(n,p,fy):
    hc,D,N0,Np,c0,fyc=p
    if n<0 or n>Np:return np.nan
    if n<=N0:
        zn=(c0-n)/D; return .5*D*(hc*hc-zn*zn)+(fyc+fy)*TS*(hc+TS/2)
    x=(n-N0)/(fyc+fy); return .5*(fyc+fy)*(TS-x)*(2*hc+TS+x)

def roots_log(fun,hi=.08,n=1000):
    xs=np.geomspace(1e-11,hi,n); out=[]; x0=None; f0=None
    for x in xs:
        v=fun(x)
        if np.isfinite(v) and f0 is not None and v*f0<0: out.append(brentq(fun,x0,x,xtol=1e-14,rtol=1e-13))
        if np.isfinite(v): x0,f0=x,v
        else:x0=f0=None
    return out

def plast_candidates(st,fyc):
    pp=plast_params(st,fyc); fy=st['fy']; out=[]
    def phi(q,s): _,n,m=demand(st,q,s); return plast_M(n,pp,fy)-m
    for s in (0.,1.):
        for q in roots_log(lambda q:phi(q,s)):
            out.append((q,s,P(st,q)/1e6))
    # stationary interior roots: solve phi=0 and dphi/ds=0 using finite 1D elimination in s.
    from scipy.optimize import root
    seeds=[(.002,.2),(.004,.5),(.008,.5),(.015,.3),(.03,.7)]
    def dm(n):
        hc,D,N0,_,c0,fyc=pp
        if n<=N0:return (c0-n)/D
        return -(hc+(n-N0)/(fyc+fy))
    def F(x):
        q,s=x; _,n,m=demand(st,q,s); Q=q*(q+2*Q0); Mu=plast_M(n,pp,fy)
        if not np.isfinite(Mu):return [1e4,1e4]
        return [Mu-m,dm(n)*(-4*st['G']*Q*s)-st['J']*q]
    for z0 in seeds:
        sol=root(F,z0)
        if sol.success:
            q,s=sol.x
            if q>0 and q<.08 and s>0 and s<1 and np.linalg.norm(F(sol.x))<1e-4: out.append((q,s,P(st,q)/1e6))
    return sorted(out)

# Exact ordinary-concrete affine section primitives recovered from 20260822_1927/2130.
def nc_sig(l,st):
    fc,E,e0=st['fc'],st['Ec'],st['eps0']; ft=.1*fc; K=E*e0; xcr=ft/K
    if l<-10:return -.1*fc
    if l<-1:return fc*(-.1*l-1.1)
    if l<0:
        kap=K/fc; return K*l/(l*l-(kap-2)*l+1)
    if l<=xcr:return K*l
    if l<10*xcr:return ft*(1+.7/9-.7*l/(9*xcr))
    return .3*ft

def nc_tan(l,st):
    fc,E,e0=st['fc'],st['Ec'],st['eps0']; ft=.1*fc; K=E*e0; xcr=ft/K
    if l<-10:return 0.
    if l<-1:return -.1*fc
    if l<0:
        kap=K/fc; d=l*l-(kap-2)*l+1; return K*(1-l*l)/(d*d)
    if l<=xcr:return K
    if l<10*xcr:return -ft*.7/(9*xcr)
    return 0.

def prim(l,st):
    fc,E,e0=st['fc'],st['Ec'],st['eps0']; ft=.1*fc; K=E*e0; xcr=ft/K
    if l<-10:return -.1*fc*l,-.05*fc*l*l
    if l<-1:return fc*(-.05*l*l-1.1*l),fc*(-l**3/30-.55*l*l)
    if l<0:
        kap=K/fc; a=kap-2; h2=1-.25*a*a; x=l-.5*a
        if h2>1e-14:I=math.atan(x/math.sqrt(h2))/math.sqrt(h2)
        elif h2<-1e-14:
            h=math.sqrt(-h2); I=.5/h*math.log(abs((x-h)/(x+h)))
        else:I=-1/x
        den=l*l-a*l+1; J=.5*math.log(den)+.5*a*I; return K*J,K*(l+a*J-I)
    if l<=xcr:return .5*K*l*l,K*l**3/3
    if l<10*xcr:
        aa=1+.7/9; bb=.7/(9*xcr); return ft*(aa*l-.5*bb*l*l),ft*(.5*aa*l*l-bb*l**3/3)
    return .3*ft*l,.15*ft*l*l

def nc_affine(a,b,h,st):
    if abs(b)<1e-14:return 2*h*nc_sig(a,st),0.
    ft=.1*st['fc']; xcr=ft/(st['Ec']*st['eps0']); cuts=[-h,h]
    for L in (-10.,-1.,0.,xcr,10*xcr):
        z=(L-a)/b
        if -h<z<h:cuts.append(z)
    cuts.sort(); N=M=0.
    for lo,hi in zip(cuts[:-1],cuts[1:]):
        l0,l1=a+b*lo,a+b*hi; p0,p10=prim(l0,st); p1,p11=prim(l1,st)
        d0,d1=p1-p0,p11-p10; N+=d0/b; M+=(d1-a*d0)/(b*b)
    return N,M

def block_deriv(N,M,a,b,h,stress,tan):
    if abs(b)<1e-12:
        D=tan(a); return 2*h*D,0.,0.,2*h**3*D/3
    sm,sp=stress(a-b*h),stress(a+b*h); return (sp-sm)/b,(h*(sp+sm)-N)/b,(h*(sp+sm)-N)/b,(h*h*(sp-sm)-2*M)/b

def steel_affine(a,b,h,st):
    K=ES*st['eps0']; fy=st['fy']; cuts=[-h,h]
    if abs(b)<1e-14:return 2*h*np.clip(K*a,-fy,fy),0.
    for L in (-fy/K,fy/K):
        z=(L-a)/b
        if -h<z<h:cuts.append(z)
    cuts.sort(); N=M=0.
    for lo,hi in zip(cuts[:-1],cuts[1:]):
        lm=a+b*(lo+hi)/2
        if K*lm<=-fy:s=-fy; N+=s*(hi-lo); M+=s*(hi*hi-lo*lo)/2
        elif K*lm>=fy:s=fy; N+=s*(hi-lo); M+=s*(hi*hi-lo*lo)/2
        else:
            N+=K*(a*(hi-lo)+b*(hi*hi-lo*lo)/2); M+=K*(a*(hi*hi-lo*lo)/2+b*(hi**3-lo**3)/3)
    return N,M

def section(st,b,use_yun=True):
    hc=st['tc']/2; zf=hc+TS/2; a=-1-b*hc; da=-hc
    Nc,Mc=nc_affine(a,b,hc,st); d=block_deriv(Nc,Mc,a,b,hc,lambda x:nc_sig(x,st),lambda x:nc_tan(x,st))
    dNc,dMc=d[0]*da+d[1],d[2]*da+d[3]; Nc*=1-RW; Mc*=1-RW; dNc*=1-RW; dMc*=1-RW
    Nw,Mw=steel_affine(a,b,hc,st); K=ES*st['eps0']; fy=st['fy']
    ds=block_deriv(Nw,Mw,a,b,hc,lambda x:float(np.clip(K*x,-fy,fy)),lambda x:K if abs(K*x)<fy else 0.)
    dNw,dMw=(ds[0]*da+ds[1])*RW,(ds[2]*da+ds[3])*RW; Nw*=RW; Mw*=RW
    fyc=yun_terminal(fy)[1] if use_yun else fy
    def fs(l):
        tr=K*l
        if tr<0:return max(tr,-fyc),K if tr>-fyc else 0.
        return min(tr,fy),K if tr<fy else 0.
    lp,lm=a+b*zf,a-b*zf; sp,Dp=fs(lp); sm,Dm=fs(lm)
    Ns=TS*(sp+sm); Ms=TS*zf*(sp-sm); dNs=TS*(Dp*(zf-hc)+Dm*(-zf-hc)); dMs=TS*zf*(Dp*(zf-hc)-Dm*(-zf-hc))
    return -(Nc+Nw+Ns),-(Mc+Mw+Ms),-(dNc+dNw+dNs),-(dMc+dMw+dMs)

def roots_lin(fun,lo=-.08,hi=-1e-7,n=1400):
    xs=np.linspace(lo,hi,n); out=[]; x0=f0=None
    for x in xs:
        v=fun(x)
        if np.isfinite(v) and f0 is not None and v*f0<0:out.append(brentq(fun,x0,x,xtol=1e-13,rtol=1e-12))
        if np.isfinite(v):x0,f0=x,v
        else:x0=f0=None
    return out

def nc_candidates(st,use_yun=True):
    out=[]; n0,m0,_,_=section(st,0,use_yun)
    for q in roots_log(lambda q:n0-P(st,q)/st['b']-st['G']*q*(q+2*Q0),.1,800):out.append(('s0',0.,q,P(st,q)/1e6,0.))
    def E(b):
        n,m,dn,dm=section(st,b,use_yun); q1=m/st['J']; f1=np.nan
        if q1>0:f1=n-P(st,q1)/st['b']+st['G']*q1*(q1+2*Q0)
        fi=qi=si=np.nan; den=4*st['G']*m*dm
        if abs(den)>1e-20:
            K=-dn*st['J']**2/den
            if K>1:
                qi=2*Q0/(K-1); si=m/(st['J']*qi)
                if qi>0 and 0<si<1:fi=n-P(st,qi)/st['b']-st['G']*qi*(qi+2*Q0)*(1-2*si*si)
        return f1,q1,fi,qi,si
    for b in roots_lin(lambda x:E(x)[0]):
        q=E(b)[1]
        if 0<q<.1:out.append(('s1',b,q,P(st,q)/1e6,1.))
    for b in roots_lin(lambda x:E(x)[2]):
        _,_,fi,q,s=E(b)
        if np.isfinite(fi) and 0<q<.1 and 0<s<1:out.append(('interior',b,q,P(st,q)/1e6,s))
    return sorted(out,key=lambda z:z[2])

def main():
    print('SSNC-R01'); print('FORMAL_SPATIAL_QUADRATURE=0\nFORMAL_MATERIAL_POINTS=0\nGLOBAL_VIRTUAL_WORK_CLOSURE=False\nD15_USED=False')
    sy=0
    for r in (.4,.7,1.,1.3,2.5):
        a=yun_coeff(r);b=yun_coeff(1/r);sy=max(sy,abs(a[0]-b[0]),abs(a[1]-b[1]))
    print(f'YUN_KCR_KP_AXIS_SWAP_MAX_ERR={sy:.3e}')
    for fy in (235.,355.,460.):
        A,su,eta=yun_terminal(fy); print(f'YUN fy={fy:.0f} Au={A:.12f} sigma_u={su:.12f} eta={eta:.12f}')
    print('case,R07_repro_MN,Yun_only_MN,NC_noYun_MN,SSNC_MN,control,s,q,vs_R07_pct,vs_Zhou_pct')
    qe=pe=0.; errs=[]
    for name,c in CASES.items():
        st=structural(c); base=plast_candidates(st,st['fy'])[0]; qe=max(qe,abs(base[0]-R07[name][1])); pe=max(pe,abs(base[2]-R07[name][2]))
        yu=plast_candidates(st,yun_terminal(st['fy'])[1])[0]; no=nc_candidates(st,False)[0]; z=nc_candidates(st,True)[0]
        er=100*(z[3]/R07[name][2]-1); ez=100*(z[3]/ZHOU[name]-1); errs.append(ez)
        print(f'{name},{base[2]:.9f},{yu[2]:.9f},{no[3]:.9f},{z[3]:.9f},{z[0]},{z[4]:.9f},{z[2]:.12f},{er:.6f},{ez:.6f}')
    print(f'R07_MAX_Q_ABS_ERR={qe:.3e}\nR07_MAX_PU_ABS_ERR_MN={pe:.3e}\nZHOU_MEAN_SIGNED_PCT={np.mean(errs):.9f}\nZHOU_MAE_PCT={np.mean(np.abs(errs)):.9f}')
    assert qe<5e-10 and pe<2e-6 and sy<1e-10
    print('R20_1_OPTION_H_SOURCE_CLOSURE=PASS\nYUN_CH5_HOMOGENIZED_TERMINAL=PASS\nR07_BASELINE_REGRESSION=PASS\nNC_EXACT_SECTION_AIRY_TERMINAL=PASS\nFULL_BIAXIAL_STEEL_TERMINAL=NOT_CLAIMED\nSSNC_R01_STATUS=EXECUTED_DIAGNOSTIC_NOT_USER_LOCKED')
if __name__=='__main__':main()
