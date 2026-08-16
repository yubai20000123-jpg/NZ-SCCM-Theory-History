"""R10-MSAC-RC1 multiscale material compiler reconnection gate.

Formal structural spatial/thickness numerical integration is ZERO.
All coefficient-generation and audit points used here live only in material-coordinate space.
This script does NOT compute P, Rq, L, KZ or Pu.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.fft import dct
from scipy.special import beta, betainc
from numpy.polynomial.chebyshev import chebval, chebder

RHO=0.1
H=0.09799750427197301
UR=0.03
ACC=0.1072329249362415
AT=1.0-2.0**(-1.0/8.0)
KAPPA=2.0005129533678754

def Bmax(p,q):
    return (p/(p+q))**p*(q/(p+q))**q

def B_beta(s,p,q):
    s=np.asarray(s,float)
    return np.where((s>=0)&(s<=1),s**p*(1-s)**q/Bmax(p,q),np.nan)

def I_beta(s,p,q):
    # For integer p,q this is the value of a finite polynomial antiderivative.
    return betainc(p+1,q+1,s)*beta(p+1,q+1)/Bmax(p,q)

def chi_map(s,p,q,alpha):
    I=I_beta(np.asarray(s),p,q)
    I1=beta(p+1,q+1)/Bmax(p,q)
    return -1+2*(np.asarray(s)+alpha*I)/(1+alpha*I1)

def chi_deriv_s(s,p,q,alpha):
    I1=beta(p+1,q+1)/Bmax(p,q)
    return 2*(1+alpha*B_beta(np.asarray(s),p,q))/(1+alpha*I1)

def invert_monotone_vec(xis,func,niter=55):
    xis=np.asarray(xis,float); lo=np.zeros_like(xis); hi=np.ones_like(xis)
    for _ in range(niter):
        mid=(lo+hi)/2; val=func(mid); mask=val<xis
        lo=np.where(mask,mid,lo); hi=np.where(mask,hi,mid)
    return (lo+hi)/2

def fit_warped_fast(f,a,b,N,p,q,alpha,Mfactor=8):
    M=Mfactor*(N+1); th=np.pi*(np.arange(M)+.5)/M; xis=np.cos(th)
    ss=invert_monotone_vec(xis,lambda s:chi_map(s,p,q,alpha),55)
    xx=a+(b-a)*ss; vals=f(xx)
    cc=dct(vals,type=2,norm=None)[:N+1]/M; cc[0]*=.5
    return cc

def fit_warped_constrained_fast(f,a,b,N,p,q,alpha,target0=0,targetd0=0,Mfactor=8):
    cc=fit_warped_fast(f,a,b,N,p,q,alpha,Mfactor)
    s0=(0-a)/(b-a); xi0=float(chi_map(s0,p,q,alpha)); dxi0=float(chi_deriv_s(s0,p,q,alpha)/(b-a))
    n=np.arange(N+1); theta=math.acos(max(-1,min(1,xi0)))
    g0=np.cos(n*theta); g1=np.zeros(N+1)
    g1[1:]=n[1:]*np.sin(n[1:]*theta)/math.sin(theta)*dxi0
    G=np.vstack([g0,g1]); rhs=np.array([target0,targetd0])-G@cc
    cc += G.T@np.linalg.solve(G@G.T,rhs)
    return cc

def eval_warped(cc,x,a,b,p,q,alpha):
    s=(np.asarray(x)-a)/(b-a); return chebval(chi_map(s,p,q,alpha),cc)

def eval_warped_d(cc,x,a,b,p,q,alpha):
    s=(np.asarray(x)-a)/(b-a); xi=chi_map(s,p,q,alpha)
    return chebval(xi,chebder(cc))*chi_deriv_s(s,p,q,alpha)/(b-a)

def fit_cheb(f,a,b,N,Mfactor=8):
    M=Mfactor*(N+1); th=np.pi*(np.arange(M)+.5)/M
    x=(a+b)/2+(b-a)/2*np.cos(th)
    cc=dct(f(x),type=2,norm=None)[:N+1]/M; cc[0]*=.5
    return cc

def fit_cheb_constrained(f,a,b,N,target0,targetd0,Mfactor=8):
    cc=fit_cheb(f,a,b,N,Mfactor)
    xi0=(0-(a+b)/2)/((b-a)/2); n=np.arange(N+1)
    theta=math.acos(max(-1,min(1,float(xi0))))
    g0=np.cos(n*theta); g1=np.zeros(N+1)
    g1[1:]=n[1:]*np.sin(n[1:]*theta)/math.sin(theta)/((b-a)/2)
    G=np.vstack([g0,g1]); rhs=np.array([target0,targetd0])-G@cc
    cc += G.T@np.linalg.solve(G@G.T,rhs)
    return cc

def eval_cheb2(cc,x,a,b):
    xi=(np.asarray(x)-(a+b)/2)/((b-a)/2); return chebval(xi,cc)

def eval_cheb2_d(cc,x,a,b):
    xi=(np.asarray(x)-(a+b)/2)/((b-a)/2); return chebval(xi,chebder(cc))/((b-a)/2)

def chi_multi(s,lenses):
    s=np.asarray(s,float); num=s.copy(); den=1.0
    for p,q,alpha in lenses:
        I1=beta(p+1,q+1)/Bmax(p,q); num=num+alpha*I_beta(s,p,q); den+=alpha*I1
    return -1+2*num/den

def chi_multi_der_s(s,lenses):
    s=np.asarray(s,float); num=np.ones_like(s); den=1.0
    for p,q,alpha in lenses:
        I1=beta(p+1,q+1)/Bmax(p,q); num=num+alpha*B_beta(s,p,q); den+=alpha*I1
    return 2*num/den

def fit_multi_fast(f,a,b,N,lenses,Mfactor=8):
    M=Mfactor*(N+1); th=np.pi*(np.arange(M)+.5)/M; xis=np.cos(th)
    ss=invert_monotone_vec(xis,lambda s:chi_multi(s,lenses),55)
    x=a+(b-a)*ss; vals=f(x)
    cc=dct(vals,type=2,norm=None)[:N+1]/M; cc[0]*=.5
    return cc

def fit_multi_constrained(f,a,b,N,lenses,target0,targetd0,Mfactor=8):
    cc=fit_multi_fast(f,a,b,N,lenses,Mfactor)
    s0=(0-a)/(b-a); xi0=float(chi_multi(s0,lenses)); dxi0=float(chi_multi_der_s(s0,lenses)/(b-a))
    n=np.arange(N+1); theta=math.acos(max(-1,min(1,xi0)))
    g0=np.cos(n*theta); g1=np.zeros(N+1)
    g1[1:]=n[1:]*np.sin(n[1:]*theta)/math.sin(theta)*dxi0
    G=np.vstack([g0,g1]); rhs=np.array([target0,targetd0])-G@cc
    cc += G.T@np.linalg.solve(G@G.T,rhs)
    return cc

def eval_multi(cc,x,a,b,lenses):
    s=(np.asarray(x)-a)/(b-a); return chebval(chi_multi(s,lenses),cc)

def eval_multi_d(cc,x,a,b,lenses):
    s=(np.asarray(x)-a)/(b-a); xi=chi_multi(s,lenses)
    return chebval(xi,chebder(cc))*chi_multi_der_s(s,lenses)/(b-a)

def source_pack_k(lam,kappa):
    rho=RHO; xcr=rho/kappa; eta=xcr/20
    def pi(x):
        x=np.asarray(x,float); r=np.sqrt(x*x+eta*eta); return x*x*(r+x)/(2*(x*x+eta*eta))
    def pid(x):
        x=np.asarray(x,float); e2=eta*eta; r=np.sqrt(x*x+e2)
        A=x*x*(r+x); Ap=2*x*(r+x)+x*x*(x/r+1); B=2*(x*x+e2); Bp=4*x
        return (Ap*B-A*Bp)/(B*B)
    def cf(c): return kappa*c/(1+(kappa-2)*c+c*c)
    def cfd(c):
        den=1+(kappa-2)*c+c*c; return kappa*(den-c*((kappa-2)+2*c))/den**2
    def ur(t):
        t=np.asarray(t,float); out=np.empty_like(t); m1=t<=xcr; tau=t[m1]/xcr
        out[m1]=rho*tau+(10*H-6*rho)*tau**3+(8*rho-15*H)*tau**4+(6*H-3*rho)*tau**5
        m2=(t>xcr)&(t<=10*xcr); s=(t[m2]-xcr)/(9*xcr)
        out[m2]=H+(UR-H)*(10*s**3-15*s**4+6*s**5); out[t>10*xcr]=UR; return out
    def urd(t):
        t=np.asarray(t,float); out=np.empty_like(t); m1=t<=xcr; tau=t[m1]/xcr
        out[m1]=(rho+3*(10*H-6*rho)*tau**2+4*(8*rho-15*H)*tau**3+5*(6*H-3*rho)*tau**4)/xcr
        m2=(t>xcr)&(t<=10*xcr); s=(t[m2]-xcr)/(9*xcr)
        out[m2]=(UR-H)*(30*s**2-60*s**3+30*s**4)/(9*xcr); out[t>10*xcr]=0; return out
    lam=np.asarray(lam,float); c=pi(-lam); t=pi(lam); cd=-pid(-lam); td=pid(lam)
    C=cf(c); Cd=cfd(c)*cd; uu=ur(t); uud=urd(t)*td; T=uu/rho; Td=uud/rho; T7=T**7; T7d=7*T**6*Td
    U=kappa*lam-C+kappa*c+uu-kappa*t; Ud=kappa-Cd+kappa*cd+uud-kappa*td
    return dict(U=U,Ud=Ud,C=C,Cd=Cd,T=T,Td=Td,T7=T7,T7d=T7d)

def build_msac(lam,core,guard,kappa=KAPPA,Ng=600,Nc=14,Nt=192,alpha_g=30,alpha_t=50,gridN=10001):
    rho=RHO; xcr=rho/kappa; eta=xcr/20
    def pi(x):
        x=np.asarray(x,float); r=np.sqrt(x*x+eta*eta); return x*x*(r+x)/(2*(x*x+eta*eta))
    def cf(c): return kappa*np.asarray(c,float)/(1+(kappa-2)*np.asarray(c,float)+np.asarray(c,float)**2)
    def ur(t):
        t=np.asarray(t,float); out=np.empty_like(t); m1=t<=xcr; tau=t[m1]/xcr
        out[m1]=rho*tau+(10*H-6*rho)*tau**3+(8*rho-15*H)*tau**4+(6*H-3*rho)*tau**5
        m2=(t>xcr)&(t<=10*xcr); s=(t[m2]-xcr)/(9*xcr)
        out[m2]=H+(UR-H)*(10*s**3-15*s**4+6*s**5); out[t>10*xcr]=UR; return out
    a,b=guard; s0=-a/(b-a); fr=Fraction(float(s0)).limit_denominator(32); pg,qg=fr.numerator,fr.denominator-fr.numerator
    ccg=fit_warped_constrained_fast(lambda x:pi(-x),a,b,Ng,pg,qg,alpha_g,0,0,8)
    ctg=fit_warped_constrained_fast(pi,a,b,Ng,pg,qg,alpha_g,0,0,8)
    chat=eval_warped(ccg,lam,a,b,pg,qg,alpha_g); chd=eval_warped_d(ccg,lam,a,b,pg,qg,alpha_g)
    that=eval_warped(ctg,lam,a,b,pg,qg,alpha_g); thd=eval_warped_d(ctg,lam,a,b,pg,qg,alpha_g)
    gg=np.linspace(a,b,gridN); cgv=eval_warped(ccg,gg,a,b,pg,qg,alpha_g); tgv=eval_warped(ctg,gg,a,b,pg,qg,alpha_g)
    ec=float(np.max(np.abs(cgv-pi(-gg)))); et=float(np.max(np.abs(tgv-pi(gg))))
    cdom=(float(cgv.min()-(1.25*ec+1e-10)),float(cgv.max()+(1.25*ec+1e-10)))
    tdom=(float(tgv.min()-(1.25*et+1e-10)),float(tgv.max()+(1.25*et+1e-10)))
    ccoef=fit_cheb_constrained(cf,*cdom,Nc,0.0,kappa,8)
    C=eval_cheb2(ccoef,chat,*cdom); Cd=eval_cheb2_d(ccoef,chat,*cdom)*chd
    lenses=[]
    for lm in (xcr,10*xcr):
        pos=(lm-tdom[0])/(tdom[1]-tdom[0])
        if 0<pos<1:
            fr2=Fraction(float(pos)).limit_denominator(32); pp=fr2.numerator; qq=fr2.denominator-pp
            if pp>0 and qq>0: lenses.append((pp,qq,alpha_t))
    ucoef=fit_multi_constrained(ur,*tdom,Nt,lenses,0.0,kappa,8)
    t7coef=fit_multi_constrained(lambda z:(ur(z)/rho)**7,*tdom,Nt,lenses,0.0,0.0,8)
    uu=eval_multi(ucoef,that,*tdom,lenses); uud=eval_multi_d(ucoef,that,*tdom,lenses)*thd
    T=uu/rho; Td=uud/rho; T7=eval_multi(t7coef,that,*tdom,lenses); T7d=eval_multi_d(t7coef,that,*tdom,lenses)*thd
    U=kappa*lam-C+kappa*chat+uu-kappa*that; Ud=kappa-Cd+kappa*chd+uud-kappa*thd
    meta={"gate":{"p":pg,"q":qg,"center":float(fr),"s0":float(s0),"alpha":alpha_g},
          "gate_errors":{"c":ec,"t":et},"cdom":cdom,"tdom":tdom,
          "lenses":[{"p":p,"q":q,"alpha":aa} for p,q,aa in lenses],
          "coefficient_count":2*(Ng+1)+(Nc+1)+2*(Nt+1),
          "naive_gate_degree":Ng*(pg+qg+1),
          "naive_tension_degree":Nt*max([p+q+1 for p,q,_ in lenses] or [1])}
    return dict(U=U,Ud=Ud,C=C,Cd=Cd,T=T,Td=Td,T7=T7,T7d=T7d),meta

def audit_lam(core,kappa):
    xcr=RHO/kappa
    chunks=[np.linspace(core[0],core[1],501),np.linspace(max(core[0],-.03),min(core[1],.08),401)]
    if core[0]<xcr<core[1]: chunks.append(np.linspace(max(core[0],xcr-.01),min(core[1],xcr+.01),201))
    if core[0]<10*xcr<core[1]: chunks.append(np.linspace(max(core[0],10*xcr-.03),min(core[1],10*xcr+.03),201))
    chunks.append(np.array([0.0,xcr,10*xcr]))
    pts=np.concatenate(chunks); pts=pts[(pts>=core[0])&(pts<=core[1])]
    return np.unique(pts)

def assembled_metrics(ref,test,lam):
    def make(p):
        U1=p['U'][:,None]; U2=p['U'][None,:]; C1=p['C'][:,None]; C2=p['C'][None,:]
        T1=p['T'][:,None]; T2=p['T'][None,:]; T71=p['T7'][:,None]; T72=p['T7'][None,:]
        Ud1=p['Ud'][:,None]; Ud2=p['Ud'][None,:]; Cd1=p['Cd'][:,None]; Cd2=p['Cd'][None,:]
        Td1=p['Td'][:,None]; Td2=p['Td'][None,:]; T7d1=p['T7d'][:,None]; T7d2=p['T7d'][None,:]
        s1=U1-ACC*C1*C1*C2+C1*T2-RHO*AT*T1*T2*T72
        s2=U2-ACC*C2*C2*C1+C2*T1-RHO*AT*T2*T1*T71
        d11=Ud1-2*ACC*C1*Cd1*C2+Cd1*T2-RHO*AT*Td1*T2*T72
        d12=-ACC*C1*C1*Cd2+C1*Td2-RHO*AT*T1*(Td2*T72+T2*T7d2)
        d22=Ud2-2*ACC*C2*Cd2*C1+Cd2*T1-RHO*AT*Td2*T1*T71
        d21=-ACC*C2*C2*Cd1+C2*Td1-RHO*AT*T2*(Td1*T71+T1*T7d1)
        return s1,s2,d11,d12,d21,d22
    a=make(ref); b=make(test)
    maxs=max(np.max(np.abs(b[0]-a[0])),np.max(np.abs(b[1]-a[1]))); peaks=max(np.max(np.abs(a[0])),np.max(np.abs(a[1])))
    maxt=max(np.max(np.abs(b[k]-a[k])) for k in range(2,6)); peakt=max(np.max(np.abs(a[k])) for k in range(2,6))
    L1=lam[:,None]; L2=lam[None,:]; den=L1-L2; mask=np.abs(den)>1e-12
    ga=np.empty_like(den); gb=np.empty_like(den); ga[mask]=(a[0]-a[1])[mask]/den[mask]; gb[mask]=(b[0]-b[1])[mask]/den[mask]
    diag=np.eye(len(lam),dtype=bool); ga[diag]=(a[2]-a[3])[diag]; gb[diag]=(b[2]-b[3])[diag]
    return float(maxs/peaks),float(maxt/peakt),float(np.max(np.abs(gb-ga))/np.max(np.abs(ga)))

LEVELS=[("L0",256,10,128),("L1",384,12,192),("L2",512,14,256),("L3",640,14,320),("L4",768,14,384),("L5",896,14,448),("L6",1024,14,512),("L7",1152,16,576),("L8",1280,16,640)]
CASES={
"Z0":{"core":(-2.326966223778822,0.3981623553727774),"guard":(-2.4632226527364014,0.534418784330357),"kappa":2.000512953368},
"Z1":{"core":(-2.2465646933414067,0.30437677393062584),"guard":(-2.3741117667045084,0.4319238472937275),"kappa":2.000512953368},
"Z2":{"core":(-2.326966223778822,0.3981623553727774),"guard":(-2.4632226527364014,0.534418784330357),"kappa":2.000512953368},
"Z3":{"core":(-2.241404,0.293969),"guard":(-2.368172,0.420738),"kappa":2.0009130559586734},
"Z4":{"core":(-2.385927,0.469962),"guard":(-2.528721,0.612756),"kappa":2.000512953368},
"Z5":{"core":(-2.980899,1.194486),"guard":(-3.189668,1.403255),"kappa":2.000512953368},
"Z6":{"core":(-2.768805,2.128027),"guard":(-3.013646,2.372868),"kappa":2.000512953368}}

def main():
    print('FORMAL STRUCTURAL COUNTERS: sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0')
    for case,d in CASES.items():
        lam=audit_lam(d['core'],d['kappa']); ref=source_pack_k(lam,d['kappa']); first=None
        for idx,(level,Ng,Nc,Nt) in enumerate(LEVELS):
            test,meta=build_msac(lam,d['core'],d['guard'],kappa=d['kappa'],Ng=Ng,Nc=Nc,Nt=Nt)
            es,et,ed=assembled_metrics(ref,test,lam); passed=(es<=.005 and et<=.05 and ed<=.05)
            print(case,level,Ng,Nc,Nt,es,et,ed,passed,'gate',meta['gate'],'lenses',meta['lenses'],'coeff',meta['coefficient_count'])
            if passed and first is None: first=idx
            elif first is not None and idx==first+1: break

if __name__=='__main__': main()
