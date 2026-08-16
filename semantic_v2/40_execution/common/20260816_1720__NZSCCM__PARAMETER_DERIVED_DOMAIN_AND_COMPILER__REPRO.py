"""Reproduce the 2026-08-16 17:20 parameter-derived-domain gate.

Formal structural spatial/thickness sampling/quadrature = 0.
All numerical nodes below are MATERIAL-COORDINATE coefficient/audit nodes only.
No Pu/root solve is performed.
"""
import math
import numpy as np
from scipy.fft import dct
from numpy.polynomial.chebyshev import chebval, chebder

NU=.18; RHO=.1; UR=.03; H=.09799750427197301
ACC=.1072329249362415
AT=1.0-2.0**(-1.0/8.0)
Q0=.004; DMAX=2.0; DOMAIN_GUARD=.05; Q_GUARD=1.25
ORDERS=[48,96,192,384,768,1024,1280,1536,1792,2048,2304,2560,2816,3072,3328,3584,3840,4096]
GATES=(.005,.05,.05)

CASES={
'Z0':dict(Pcr=78.306708780004,Pyth=44.044944,b=6000,tc=122,eps0=.0018712490394580678,kappa=2.000512953368),
'Z1':dict(Pcr=40.350205992294,Pyth=30.319584,b=6000,tc=92,eps0=.0018712490394580678,kappa=2.000512953368),
'Z2':dict(Pcr=78.306708780004,Pyth=50.622144,b=6000,tc=122,eps0=.0018712490394580678,kappa=2.000512953368),
'Z3':dict(Pcr=81.797439948099,Pyth=54.948816,b=6000,tc=122,eps0=.0025344898708809867,kappa=2.0009130559586734),
'Z4':dict(Pcr=179.754773113184,Pyth=79.386112,b=8000,tc=192,eps0=.0018712490394580678,kappa=2.000512953368),
'Z5':dict(Pcr=231.788407676832,Pyth=14.681648,b=2000,tc=122,eps0=.0018712490394580678,kappa=2.000512953368),
'Z6':dict(Pcr=39.288014715,Pyth=88.089888,b=12000,tc=122,eps0=.0018712490394580678,kappa=2.000512953368),
}

def derived_domain(c):
    kp=3*(1-NU**2)/8
    apost=math.sqrt(max(c['Pyth']/c['Pcr']-1,0)/kp)
    qpost=(c['tc']/c['b'])*apost
    qmax=Q_GUARD*max(Q0,qpost)
    Cm=math.pi**2/c['eps0']*(Q0*qmax+.5*qmax*qmax)
    Cb=math.pi**2/(2*c['eps0'])*(c['tc']/c['b'])*qmax
    A=Cm/(1-NU**2); B1=Cb/(1-NU); B2=Cb/(1+NU)
    r=math.hypot(B1/(2*A),B2/(2*A))
    hi=A+(B1*B1+B2*B2)/(4*A) if r<=1 else math.hypot(B1,B2)
    lo=-DMAX-B1
    w=hi-lo; pad=DOMAIN_GUARD*w
    return dict(apost=apost,qpost=qpost,qmax=qmax,Cm=Cm,Cb=Cb,core=(lo,hi),guard=(lo-pad,hi+pad))

def make_source(kappa):
    xcr=RHO/kappa; eta=xcr/20
    def Pi(z):
        z=np.asarray(z,float); r=np.sqrt(z*z+eta*eta)
        return z*z*(r+z)/(2*(z*z+eta*eta))
    def Pi_d(z):
        z=np.asarray(z,float); e2=eta*eta; r=np.sqrt(z*z+e2)
        A=z*z*(r+z); Ap=2*z*(r+z)+z*z*(z/r+1)
        B=2*(z*z+e2); Bp=4*z
        return (Ap*B-A*Bp)/(B*B)
    def uR(t):
        t=np.asarray(t,float); out=np.empty_like(t)
        m1=t<=xcr; tau=t[m1]/xcr
        out[m1]=RHO*tau+(10*H-6*RHO)*tau**3+(8*RHO-15*H)*tau**4+(6*H-3*RHO)*tau**5
        m2=(t>xcr)&(t<=10*xcr); s=(t[m2]-xcr)/(9*xcr)
        out[m2]=H+(UR-H)*(10*s**3-15*s**4+6*s**5)
        out[t>10*xcr]=UR
        return out
    def uR_d(t):
        t=np.asarray(t,float); out=np.empty_like(t)
        m1=t<=xcr; tau=t[m1]/xcr
        out[m1]=(RHO+3*(10*H-6*RHO)*tau**2+4*(8*RHO-15*H)*tau**3+5*(6*H-3*RHO)*tau**4)/xcr
        m2=(t>xcr)&(t<=10*xcr); s=(t[m2]-xcr)/(9*xcr)
        out[m2]=(UR-H)*(30*s**2-60*s**3+30*s**4)/(9*xcr)
        out[t>10*xcr]=0
        return out
    def C(c): return kappa*c/(1+(kappa-2)*c+c*c)
    def Cd(c):
        den=1+(kappa-2)*c+c*c
        return kappa*(den-c*((kappa-2)+2*c))/(den*den)
    def src(lam):
        lam=np.asarray(lam,float); c=Pi(-lam); t=Pi(lam)
        cd=-Pi_d(-lam); td=Pi_d(lam)
        cc=C(c); ccd=Cd(c)*cd
        uu=uR(t); uud=uR_d(t)*td
        T=uu/RHO; Td=uud/RHO; T7=T**7; T7d=7*T**6*Td
        U=kappa*lam-cc+kappa*c+uu-kappa*t
        Ud=kappa-ccd+kappa*cd+uud-kappa*td
        return dict(U=U,Ud=Ud,C=cc,Cd=ccd,T=T,Td=Td,T7=T7,T7d=T7d)
    return src,xcr

def coeff(src,name,N,guard,kappa):
    a,b=guard; M=8*(N+1); j=np.arange(M); th=np.pi*(j+.5)/M
    lam=(a+b)/2+(b-a)/2*np.cos(th)
    cc=dct(src(lam)[name],type=2,norm=None)[:N+1]/M; cc[0]*=.5
    lc=(a+b)/2; lh=(b-a)/2; xi0=-lc/lh; n=np.arange(N+1); th0=math.acos(xi0)
    g0=np.cos(n*th0); g1=np.zeros(N+1); g1[1:]=n[1:]*np.sin(n[1:]*th0)/math.sin(th0)/lh
    G=np.vstack([g0,g1]); Hinv=np.empty(N+1); Hinv[0]=1/M; Hinv[1:]=2/M
    target=np.array([0.,kappa if name=='U' else 0.])
    cc += Hinv*(G.T@np.linalg.solve((G*Hinv)@G.T,target-G@cc))
    return cc

def compiled(src,N,guard,kappa,lam):
    lc=(guard[0]+guard[1])/2; lh=(guard[1]-guard[0])/2; xi=(lam-lc)/lh; out={}
    for n,dn in [('U','Ud'),('C','Cd'),('T','Td'),('T7','T7d')]:
        c=coeff(src,n,N,guard,kappa); out[n]=chebval(xi,c); out[dn]=chebval(xi,chebder(c))/lh
    return out

def row(p,i):
    U,C,T,T7=p['U'],p['C'],p['T'],p['T7']; Ud,Cd,Td,T7d=p['Ud'],p['Cd'],p['Td'],p['T7d']
    U1,C1,T1,T71=U[i],C[i],T[i],T7[i]; Ud1,Cd1,Td1,T7d1=Ud[i],Cd[i],Td[i],T7d[i]
    s1=U1-ACC*C1*C1*C+C1*T-RHO*AT*T1*T*T7
    s2=U-ACC*C*C*C1+C*T1-RHO*AT*T*T1*T71
    d11=Ud1-2*ACC*C1*Cd1*C+Cd1*T-RHO*AT*Td1*T*T7
    d12=-ACC*C1*C1*Cd+C1*Td-RHO*AT*T1*(Td*T7+T*T7d)
    d22=Ud-2*ACC*C*Cd*C1+Cd*T1-RHO*AT*Td*T1*T71
    d21=-ACC*C*C*Cd1+C*Td1-RHO*AT*T*(Td1*T71+T1*T7d1)
    return s1,s2,d11,d12,d21,d22

def metrics(ref,test,lam):
    ms=mt=md=ps=pt=pd=0.
    for i in range(len(lam)):
        a=row(ref,i); b=row(test,i)
        for k in (0,1): ms=max(ms,float(np.max(np.abs(b[k]-a[k])))); ps=max(ps,float(np.max(np.abs(a[k]))))
        for k in (2,3,4,5): mt=max(mt,float(np.max(np.abs(b[k]-a[k])))); pt=max(pt,float(np.max(np.abs(a[k]))))
        den=lam[i]-lam; mask=np.abs(den)>1e-9; ga=np.empty_like(lam); gb=np.empty_like(lam)
        ga[mask]=(a[0][mask]-a[1][mask])/den[mask]; gb[mask]=(b[0][mask]-b[1][mask])/den[mask]
        ga[~mask]=a[2][~mask]-a[3][~mask]; gb[~mask]=b[2][~mask]-b[3][~mask]
        md=max(md,float(np.max(np.abs(gb-ga)))); pd=max(pd,float(np.max(np.abs(ga))))
    return ms/ps,mt/pt,md/pd

def main():
    print('FORMAL STRUCTURAL SPATIAL/THICKNESS QUADRATURE = 0')
    for name,c in CASES.items():
        d=derived_domain(c); src,xcr=make_source(c['kappa']); core=d['core']; guard=d['guard']
        chunks=[np.linspace(core[0],core[1],321),np.array([0,xcr,10*xcr])]
        for ctr,w,n in [(0,.08,181),(xcr,.03,121),(10*xcr,.08,81)]:
            lo=max(core[0],ctr-w); hi=min(core[1],ctr+w)
            if hi>lo: chunks.append(np.linspace(lo,hi,n))
        lam=np.unique(np.concatenate(chunks)); lam=lam[(lam>=core[0])&(lam<=core[1])]; ref=src(lam)
        print('\n',name,'domain=',d)
        for N in ORDERS:
            m=metrics(ref,compiled(src,N,guard,c['kappa'],lam),lam)
            print(N,m)
            if m[0]<=GATES[0] and m[1]<=GATES[1] and m[2]<=GATES[2]:
                print('FIRST PASS',name,N,m); break
if __name__=='__main__': main()
