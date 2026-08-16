"""NZ-SCCM Z0-Z5 AR2 discrepancy-localization reproducer.

Timestamp: 2026-08-16 10:54 +08:00
No structural spatial sampling/quadrature is used.
This script reproduces:
1) exact uniform q=0 flat-section capacities from the frozen scalar R10 target;
2) the wide N48-C1/MM material-compiler error over each reachable lambda range;
3) classical imperfect-plate amplitude diagnostics for the challenged 10:43 states.
"""
from math import sqrt, pi
import numpy as np
from scipy.optimize import linprog
from numpy.polynomial.chebyshev import chebvander, chebval, chebder

KAPPA=2.0005129533678754
RHO=.1
XCR=RHO/KAPPA
ETA=XCR/20
UR=.03
HH=.09799750427197301
ACC=.1072329249362415
AT=1-2**(-1/8)
ES=206000.0
NUC=.18
NUS=.30

def Pi(z):
    z=np.asarray(z,float)
    return z*z*(np.sqrt(z*z+ETA*ETA)+z)/(2*(z*z+ETA*ETA))

def uR(t):
    t=np.asarray(t,float); r=t/XCR; out=np.empty_like(r)
    m=r<=1; rr=r[m]
    out[m]=RHO*rr+(10*HH-6*RHO)*rr**3+(8*RHO-15*HH)*rr**4+(6*HH-3*RHO)*rr**5
    m2=(r>1)&(r<=10); s=(r[m2]-1)/9
    out[m2]=HH+(UR-HH)*(10*s**3-15*s**4+6*s**5)
    out[r>10]=UR
    return out

def targets(lam):
    lam=np.asarray(lam,float)
    c=Pi(-lam); t=Pi(lam)
    C=KAPPA*c/(1+(KAPPA-2)*c+c*c)
    u=uR(t); T=u/RHO
    U=KAPPA*lam-C+KAPPA*c+u-KAPPA*t
    return U,C,T,T**7

def spectral_stress(lams, funcs=None):
    lams=np.asarray(lams,float)
    U,C,T,T7=targets(lams) if funcs is None else funcs
    detC=np.prod(C); detT=np.prod(T)
    return U-ACC*detC*C+np.sum(T)*C-C*T-RHO*AT*detT*(np.sum(T7)-T7)

def exact_concrete_compression_ratio(D):
    # q=0 transforms the plane-stress strain state to Eu eigenvalues [0,-D].
    return -spectral_stress([0.0,-D])[1]

def face_steel_sy(D,eps0,fy):
    ex=NUC*D*eps0; ey=-D*eps0
    fac=ES/(1-NUS*NUS)
    sx=fac*(ex+NUS*ey); sy=fac*(NUS*ex+ey)
    vm=sqrt(sx*sx-sx*sy+sy*sy)
    alpha=min(1.0,fy/vm) if vm>0 else 1.0
    return -alpha*sy

def web_steel_sy(D,eps0,fy):
    return min(fy,ES*D*eps0)

def flat_capacity(D,c):
    rho_w=c['ts']/c['ls']
    Pc=(1-rho_w)*c['b']*c['tc']*c['fc']*exact_concrete_compression_ratio(D)
    Ps=2*c['b']*c['ts']*face_steel_sy(D,c['eps0'],c['fy'])
    Pw=rho_w*c['b']*c['tc']*web_steel_sy(D,c['eps0'],c['fy'])
    return (Pc+Ps+Pw)/1e6

def compile_wide(la=-2.35,lb=1.90,deg=48,ngrid=6001):
    lc=(la+lb)/2; lh=(lb-la)/2
    th=(np.arange(deg+1)+.5)*pi/(deg+1)
    lam=lc+lh*np.cos(th)
    V=chebvander((lam-lc)/lh,deg)
    xi0=-lc/lh; E=np.eye(deg+1)
    vr=np.array([chebval(xi0,E[n]) for n in range(deg+1)])
    dr=np.array([chebval(xi0,chebder(E[n]))/lh for n in range(deg+1)])
    AE=np.vstack([vr,dr])
    U,C,T,T7=targets(lam)
    def cls(vals,b):
        H=V.T@V
        K=np.block([[H,AE.T],[AE,np.zeros((2,2))]])
        return np.linalg.solve(K,np.r_[V.T@vals,b])[:deg+1]
    Uc=cls(U,[0,KAPPA]); Cc=cls(C,[0,0]); T7c=cls(T7,[0,0])
    lg=np.linspace(la,lb,ngrid); Vg=chebvander((lg-lc)/lh,deg); tg=targets(lg)[2]
    obj=np.r_[np.zeros(deg+1),1.0]
    Aub=np.vstack([np.c_[Vg,-np.ones(ngrid)],np.c_[-Vg,-np.ones(ngrid)]])
    bub=np.r_[tg,-tg]
    res=linprog(obj,A_ub=Aub,b_ub=bub,A_eq=np.c_[AE,np.zeros(2)],b_eq=[0,0],
                bounds=[(None,None)]*(deg+1)+[(0,None)],method='highs')
    return dict(lc=lc,lh=lh,U=Uc,C=Cc,T=res.x[:deg+1],T7=T7c,Terr=res.x[-1])

def max_error(comp,ra,rb,n=20001):
    lam=np.linspace(ra,rb,n); xi=(lam-comp['lc'])/comp['lh']
    U,C,T,T7=targets(lam)
    out={}
    for name,co,target in [('U',comp['U'],U),('C',comp['C'],C),('T',comp['T'],T),('T7',comp['T7'],T7)]:
        pred=chebval(xi,co); err=np.abs(pred-target); i=int(np.argmax(err))
        out[name]=(float(err[i]),float(lam[i]),float(pred[i]),float(target[i]))
    return out

CASES={
'Z0':dict(b=6000.,tc=122.,ts=4.,ls=200.,fc=30.4,eps0=.0018712490394580678,fy=355.,Pyth=44.044944,Pu=33.4910020249,Pcr=78.306708780004,D=.9152967877,q=.003167610641762143,A0=24.,lam=(-1.1224371257,.2071403380)),
'Z1':dict(b=6000.,tc=92.,ts=4.,ls=200.,fc=30.4,eps0=.0018712490394580678,fy=235.,Pyth=30.319584,Pu=19.7359954323,Pcr=40.350205992294,D=.5717563101,q=.003592522702744954,A0=24.,lam=(-.7489141618,.1826321890)),
'Z2':dict(b=6000.,tc=122.,ts=4.,ls=200.,fc=30.4,eps0=.0018712490394580678,fy=460.,Pyth=50.622144,Pu=35.9781279800,Pcr=78.306708780004,D=1.1199239029,q=.004121962352891406,A0=24.,lam=(-1.3894723959,.2695630424)),
'Z3':dict(b=6000.,tc=122.,ts=4.,ls=200.,fc=45.6,eps0=.0025344898708809867,fy=355.,Pyth=54.948816,Pu=39.6888676991,Pcr=81.797439948099,D=.6722931952,q=.003650178527755282,A0=24.,lam=(-.8485265156,.1762333204)),
'Z4':dict(b=8000.,tc=192.,ts=4.,ls=200.,fc=30.4,eps0=.0018712490394580678,fy=355.,Pyth=79.386112,Pu=63.7385190567,Pcr=179.754773113184,D=.9418453176,q=.0023439331763697186,A0=32.,lam=(-1.1227628996,.1809175820)),
'Z5':dict(b=2000.,tc=122.,ts=4.,ls=200.,fc=30.4,eps0=.0018712490394580678,fy=355.,Pyth=14.681648,Pu=14.7824166483,Pcr=231.788407676832,D=.9899205152,q=.0003781143321320562,A0=8.,lam=(-1.0640988844,.0741783692)),
}

if __name__=='__main__':
    print('FORMAL STRUCTURAL SAMPLING/QUADRATURE = 0')
    comp=compile_wide()
    print('wide T minimax',comp['Terr'])
    for name,c in CASES.items():
        Ds=np.linspace(0,2,20001)  # scalar load-parameter sweep, not spatial points
        P=np.array([flat_capacity(D,c) for D in Ds])
        i=int(np.argmax(P)); flat=P[i]
        eta=c['Pu']/c['Pcr']; A=c['q']*c['b']
        classical=eta/(1-eta)
        At=(c['A0']+A)/c['tc']
        bend=(c['tc']/2)*pi*pi*c['q']/c['b']/(c['D']*c['eps0'])
        e=max_error(comp,*c['lam'])
        print(name,'flat_D',Ds[i],'flat_MN',flat,'flat/Pyth',flat/c['Pyth'],
              'challenged_drop_pct',(c['Pu']-flat)/flat*100,
              'A/A0',A/c['A0'],'classical',classical,'At/t',At,'bend/axial',bend,
              'Terror',e['T'],'T7error',e['T7'])
