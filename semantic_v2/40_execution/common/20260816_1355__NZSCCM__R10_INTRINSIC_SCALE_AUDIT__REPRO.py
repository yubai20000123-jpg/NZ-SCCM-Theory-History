"""R10 intrinsic-scale / global-order diagnostic.

Formal structural spatial sampling/quadrature = 0.
All grids below are MATERIAL-COORDINATE audit grids only.
No Pu, Rq, L or KZ structural solve is performed here.
"""
import math
import numpy as np
from scipy.fft import dct
from numpy.polynomial.chebyshev import chebval, chebder

KAPPA=2.0005129533678754
RHO=.1
XCR=RHO/KAPPA
ETA=XCR/20.0
UR=.03
H=.09799750427197301
ACC=.1072329249362415
AT=1.0-2.0**(-1.0/8.0)
CORE=(-2.35,1.90)
GUARD=(-2.60,2.15)


def Pi(z):
    z=np.asarray(z,float)
    r=np.sqrt(z*z+ETA*ETA)
    return z*z*(r+z)/(2.0*(z*z+ETA*ETA))


def Pi_d(z):
    # analytic derivative from product/quotient differentiation
    z=np.asarray(z,float)
    e2=ETA*ETA
    r=np.sqrt(z*z+e2)
    A=z*z*(r+z)
    Ap=2*z*(r+z)+z*z*(z/r+1.0)
    B=2.0*(z*z+e2)
    Bp=4.0*z
    return (Ap*B-A*Bp)/(B*B)


def uR(t):
    t=np.asarray(t,float)
    out=np.empty_like(t)
    m1=t<=XCR
    tau=t[m1]/XCR
    out[m1]=(RHO*tau+(10*H-6*RHO)*tau**3
             +(8*RHO-15*H)*tau**4+(6*H-3*RHO)*tau**5)
    m2=(t>XCR)&(t<=10*XCR)
    s=(t[m2]-XCR)/(9*XCR)
    out[m2]=H+(UR-H)*(10*s**3-15*s**4+6*s**5)
    out[t>10*XCR]=UR
    return out


def uR_d(t):
    t=np.asarray(t,float)
    out=np.empty_like(t)
    m1=t<=XCR
    tau=t[m1]/XCR
    out[m1]=(RHO+3*(10*H-6*RHO)*tau**2
             +4*(8*RHO-15*H)*tau**3
             +5*(6*H-3*RHO)*tau**4)/XCR
    m2=(t>XCR)&(t<=10*XCR)
    s=(t[m2]-XCR)/(9*XCR)
    out[m2]=(UR-H)*(30*s**2-60*s**3+30*s**4)/(9*XCR)
    out[t>10*XCR]=0.0
    return out


def C_of_c(c):
    c=np.asarray(c,float)
    return KAPPA*c/(1+(KAPPA-2)*c+c*c)


def dCdc(c):
    c=np.asarray(c,float)
    den=1+(KAPPA-2)*c+c*c
    return KAPPA*(den-c*((KAPPA-2)+2*c))/(den*den)


def source(lam):
    lam=np.asarray(lam,float)
    c=Pi(-lam); t=Pi(lam)
    cd=-Pi_d(-lam); td=Pi_d(lam)
    C=C_of_c(c); Cd=dCdc(c)*cd
    uu=uR(t); uud=uR_d(t)*td
    T=uu/RHO; Td=uud/RHO
    T7=T**7; T7d=7*T**6*Td
    U=KAPPA*lam-C+KAPPA*c+uu-KAPPA*t
    Ud=KAPPA-Cd+KAPPA*cd+uud-KAPPA*td
    return dict(U=U,Ud=Ud,C=C,Cd=Cd,T=T,Td=Td,T7=T7,T7d=T7d)


def cheb_project(func,N,a,b):
    M=8*(N+1)
    j=np.arange(M)
    th=np.pi*(j+.5)/M
    x=(a+b)/2+(b-a)/2*np.cos(th)
    cc=dct(func(x),type=2,norm=None)[:N+1]/M
    cc[0]*=.5
    return cc


def constrained_lambda_channel(name,N):
    a,b=GUARD
    M=8*(N+1)
    j=np.arange(M); th=np.pi*(j+.5)/M
    lam=(a+b)/2+(b-a)/2*np.cos(th)
    vals=source(lam)[name]
    cc=dct(vals,type=2,norm=None)[:N+1]/M
    cc[0]*=.5
    lc=(a+b)/2; lh=(b-a)/2; xi0=-lc/lh
    n=np.arange(N+1); th0=math.acos(xi0)
    g0=np.cos(n*th0)
    g1=np.zeros(N+1)
    g1[1:]=n[1:]*np.sin(n[1:]*th0)/math.sin(th0)/lh
    G=np.vstack([g0,g1])
    Hinv=np.empty(N+1); Hinv[0]=1/M; Hinv[1:]=2/M
    target=np.array([0.0,KAPPA if name=='U' else 0.0])
    rhs=target-G@cc
    cc += Hinv*(G.T@np.linalg.solve((G*Hinv)@G.T,rhs))
    return cc


def eval_cheb(cc,x,a,b):
    xi=(np.asarray(x)-(a+b)/2)/((b-a)/2)
    return chebval(xi,cc)


def eval_cheb_d(cc,x,a,b):
    xi=(np.asarray(x)-(a+b)/2)/((b-a)/2)
    return chebval(xi,chebder(cc))/((b-a)/2)


def spectral_row(p,i):
    U,C,T,T7=p['U'],p['C'],p['T'],p['T7']
    Ud,Cd,Td,T7d=p['Ud'],p['Cd'],p['Td'],p['T7d']
    U1,C1,T1,T71=U[i],C[i],T[i],T7[i]
    Ud1,Cd1,Td1,T7d1=Ud[i],Cd[i],Td[i],T7d[i]
    s1=U1-ACC*C1*C1*C+C1*T-RHO*AT*T1*T*T7
    s2=U-ACC*C*C*C1+C*T1-RHO*AT*T*T1*T71
    ds11=Ud1-2*ACC*C1*Cd1*C+Cd1*T-RHO*AT*Td1*T*T7
    ds12=-ACC*C1*C1*Cd+C1*Td-RHO*AT*T1*(Td*T7+T*T7d)
    ds22=Ud-2*ACC*C*Cd*C1+Cd*T1-RHO*AT*Td*T1*T71
    ds21=-ACC*C*C*Cd1+C*Td1-RHO*AT*T*(Td1*T71+T1*T7d1)
    return s1,s2,ds11,ds12,ds21,ds22


def assembled_metrics(ref,test,lam):
    maxs=maxt=maxd=peaks=peakt=peakd=0.0
    for i,l1 in enumerate(lam):
        a=spectral_row(ref,i); b=spectral_row(test,i)
        for k in (0,1):
            maxs=max(maxs,float(np.max(np.abs(b[k]-a[k]))))
            peaks=max(peaks,float(np.max(np.abs(a[k]))))
        for k in (2,3,4,5):
            maxt=max(maxt,float(np.max(np.abs(b[k]-a[k]))))
            peakt=max(peakt,float(np.max(np.abs(a[k]))))
        den=l1-lam; mask=np.abs(den)>1e-10
        ga=np.empty_like(lam); gb=np.empty_like(lam)
        ga[mask]=(a[0][mask]-a[1][mask])/den[mask]
        gb[mask]=(b[0][mask]-b[1][mask])/den[mask]
        ga[~mask]=a[2][~mask]-a[3][~mask]
        gb[~mask]=b[2][~mask]-b[3][~mask]
        maxd=max(maxd,float(np.max(np.abs(gb-ga))))
        peakd=max(peakd,float(np.max(np.abs(ga))))
    return maxs/peaks,maxt/peakt,maxd/peakd


def hybrid_pack(lam,Nc,Nu):
    cmax=float(Pi(-CORE[0])); tmax=float(Pi(CORE[1]))
    cc=cheb_project(C_of_c,Nc,0,cmax)
    cu=cheb_project(uR,Nu,0,tmax)
    c=Pi(-lam); t=Pi(lam); cd=-Pi_d(-lam); td=Pi_d(lam)
    C=eval_cheb(cc,c,0,cmax); Cd=eval_cheb_d(cc,c,0,cmax)*cd
    uu=eval_cheb(cu,t,0,tmax); uud=eval_cheb_d(cu,t,0,tmax)*td
    T=uu/RHO; Td=uud/RHO; T7=T**7; T7d=7*T**6*Td
    U=KAPPA*lam-C+KAPPA*c+uu-KAPPA*t
    Ud=KAPPA-Cd+KAPPA*cd+uud-KAPPA*td
    return dict(U=U,Ud=Ud,C=C,Cd=Cd,T=T,Td=Td,T7=T7,T7d=T7d)


def main():
    print('FORMAL STRUCTURAL SPATIAL SAMPLING/QUADRATURE = 0')
    print('xcr eta core/eta guard/eta=',XCR,ETA,(CORE[1]-CORE[0])/ETA,(GUARD[1]-GUARD[0])/ETA)
    print('u1 coeff=',[0,RHO,0,10*H-6*RHO,8*RHO-15*H,6*H-3*RHO])
    print('u2 coeff=',[H,0,0,10*(UR-H),-15*(UR-H),6*(UR-H)])

    grid=np.linspace(CORE[0],CORE[1],40001)
    ref=source(grid)
    lc=(GUARD[0]+GUARD[1])/2; lh=(GUARD[1]-GUARD[0])/2
    xi=(grid-lc)/lh
    for N in (48,384,768,1536,2048,3072,3584):
        row=[N]
        for name,dname in [('C','Cd'),('T','Td'),('T7','T7d')]:
            cc=constrained_lambda_channel(name,N)
            v=chebval(xi,cc); d=chebval(xi,chebder(cc))/lh
            row += [float(np.max(np.abs(v-ref[name]))),float(np.max(np.abs(d-ref[dname])))]
        print('global',row)

    # Direct Pi wide-global screen.
    for N in (48,384,768,1536,2048,3072,3584):
        cp=cheb_project(Pi,N,*GUARD)
        cm=cheb_project(lambda x:Pi(-x),N,*GUARD)
        ep=float(np.max(np.abs(eval_cheb_d(cp,grid,*GUARD)-Pi_d(grid))))
        em=float(np.max(np.abs(eval_cheb_d(cm,grid,*GUARD)+Pi_d(-grid))))
        print('Pi derivative',N,ep,em)

    # Natural coordinate diagnostics.
    cmax=float(Pi(-CORE[0])); tmax=float(Pi(CORE[1]))
    cg=np.linspace(0,cmax,40001); tg=np.linspace(0,tmax,40001)
    for N in (4,6,8,10,16):
        cc=cheb_project(C_of_c,N,0,cmax)
        er=float(np.max(np.abs(eval_cheb_d(cc,cg,0,cmax)-dCdc(cg)))/np.max(np.abs(dCdc(cg))))
        print('C(c)',N,er)
    for N in (32,48,64,96,192):
        cu=cheb_project(uR,N,0,tmax)
        er=float(np.max(np.abs(eval_cheb_d(cu,tg,0,tmax)-uR_d(tg)))/np.max(np.abs(uR_d(tg))))
        print('uR(t)',N,er)

    # Combined material-only screen. Material coordinate points only.
    lam=np.unique(np.concatenate([np.linspace(CORE[0],CORE[1],801),np.linspace(-.02,.08,501),np.array([0,XCR,10*XCR])]))
    ref=source(lam)
    for Nc,Nu in [(6,48),(6,56),(6,60),(6,64),(8,64),(10,64)]:
        out=hybrid_pack(lam,Nc,Nu)
        print('hybrid',Nc,Nu,assembled_metrics(ref,out,lam))

    print('N3584 four-channel coefficient count=',4*(3584+1))
    print('Nc=6, Nu=64 fitted coefficient count=',7+65)
    print('MATERIAL ONLY: exact Pi has NOT yet been contracted through production D15.')


if __name__=='__main__':
    main()
