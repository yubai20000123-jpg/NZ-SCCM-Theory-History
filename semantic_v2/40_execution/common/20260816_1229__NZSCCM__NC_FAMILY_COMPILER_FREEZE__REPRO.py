import math
import hashlib
import numpy as np
from scipy.integrate import quad
from scipy.fft import dct
from numpy.polynomial.chebyshev import chebval, chebder

RHO=0.1
MT=-7.0/90.0
ETA_R=0.05
U_R=0.03
A_CC=0.1072329249362415
A_T=1.0-2.0**(-1.0/8.0)
CORE=(-2.35,1.90)
GUARD=(-2.60,2.15)
KAPPA_AUDIT=(1.9993148515,2.0005129533678754,2.0008935611)
CANDIDATES=[48,96,192,384,768]+list(range(1024,3584+1,256))
E_SIG_LIM=0.005
E_TAN_LIM=0.05
E_DIV_LIM=0.05


def foster_H(r,r0):
    r=np.asarray(r,dtype=float)
    return 0.5*((r-r0)+np.sqrt((r-r0)**2+ETA_R**2))-0.5*((-r0)+math.sqrt(r0*r0+ETA_R**2))


def Tsrc(r):
    return r+(MT-1.0)*foster_H(r,1.0)-MT*foster_H(r,10.0)

I_TSRC=quad(lambda x: float(Tsrc(x)),0.0,10.0,epsabs=1e-13,epsrel=1e-13)[0]
# Wsrc/xcr = rho * I_Tsrc, so h is independent of kappa for the frozen R10 construction.
H_PEAK=(RHO*I_TSRC-RHO/10.0-4.5*U_R)/5.0


def make_r10(kappa):
    xcr=RHO/kappa
    eta=xcr/20.0
    def Pi(z):
        z=np.asarray(z,dtype=float)
        return z*z*(np.sqrt(z*z+eta*eta)+z)/(2.0*(z*z+eta*eta))
    def C(lam):
        c=Pi(-np.asarray(lam,dtype=float))
        return kappa*c/(1.0+(kappa-2.0)*c+c*c)
    def T(lam):
        t=Pi(np.asarray(lam,dtype=float))
        tau=t/xcr
        s=(t-xcr)/(9.0*xcr)
        u1=RHO*tau+(10*H_PEAK-6*RHO)*tau**3+(8*RHO-15*H_PEAK)*tau**4+(6*H_PEAK-3*RHO)*tau**5
        u2=H_PEAK+(U_R-H_PEAK)*(10*s**3-15*s**4+6*s**5)
        us=np.where(t<=xcr,u1,np.where(t<=10*xcr,u2,U_R))
        return us/RHO
    def T7(lam):
        return T(lam)**7
    def U(lam):
        lam=np.asarray(lam,dtype=float)
        c=Pi(-lam); t=Pi(lam)
        return kappa*lam-C(lam)+kappa*c+RHO*T(lam)-kappa*t
    return {"U":U,"C":C,"T":T,"T7":T7,"xcr":xcr,"eta":eta}


def src_der(f,x):
    x=np.asarray(x,dtype=float)
    h=2e-6
    return (f(x+h)-f(x-h))/(2*h)


def constrained_cheb(f,N,a,b,d0,d1):
    M=8*(N+1)
    j=np.arange(M)
    th=np.pi*(j+0.5)/M
    lam=(a+b)/2.0+(b-a)/2.0*np.cos(th)
    D=dct(f(lam),type=2,norm=None)
    c=D[:N+1]/M
    c[0]*=0.5
    lc=(a+b)/2.0; lh=(b-a)/2.0; xi0=-lc/lh
    n=np.arange(N+1)
    th0=math.acos(xi0)
    g0=np.cos(n*th0)
    g1=np.zeros(N+1)
    g1[1:]=n[1:]*np.sin(n[1:]*th0)/math.sin(th0)/lh
    G=np.vstack([g0,g1])
    Hinv=np.empty(N+1)
    Hinv[0]=1.0/M; Hinv[1:]=2.0/M
    rhs=np.array([d0,d1])-G@c
    c += Hinv*(G.T@np.linalg.solve((G*Hinv)@G.T,rhs))
    return c


def peval(c,lam,a,b):
    return chebval((np.asarray(lam)-(a+b)/2.0)/((b-a)/2.0),c)


def pder(c,lam,a,b):
    return chebval((np.asarray(lam)-(a+b)/2.0)/((b-a)/2.0),chebder(c))/((b-a)/2.0)


def compile_r10(kappa,N):
    r=make_r10(kappa)
    a,b=GUARD
    return {
        "U":constrained_cheb(r["U"],N,a,b,0.0,kappa),
        "C":constrained_cheb(r["C"],N,a,b,0.0,0.0),
        "T":constrained_cheb(r["T"],N,a,b,0.0,0.0),
        "T7":constrained_cheb(r["T7"],N,a,b,0.0,0.0),
    }


def spectral_row(pack,i):
    U,C,T,T7=pack["U"],pack["C"],pack["T"],pack["T7"]
    Ud,Cd,Td,T7d=pack["Ud"],pack["Cd"],pack["Td"],pack["T7d"]
    U1,C1,T1,T71=U[i],C[i],T[i],T7[i]
    Ud1,Cd1,Td1,T7d1=Ud[i],Cd[i],Td[i],T7d[i]
    s1=U1-A_CC*C1*C1*C+C1*T-RHO*A_T*T1*T*T7
    s2=U-A_CC*C*C*C1+C*T1-RHO*A_T*T*T1*T71
    ds11=Ud1-2*A_CC*C1*Cd1*C+Cd1*T-RHO*A_T*Td1*T*T7
    ds12=-A_CC*C1*C1*Cd+C1*Td-RHO*A_T*T1*(Td*T7+T*T7d)
    ds22=Ud-2*A_CC*C*Cd*C1+Cd*T1-RHO*A_T*Td*T1*T71
    ds21=-A_CC*C*C*Cd1+C*Td1-RHO*A_T*T*(Td1*T71+T1*T7d1)
    return s1,s2,ds11,ds12,ds21,ds22


def audit(kappa,N):
    r=make_r10(kappa)
    c=compile_r10(kappa,N)
    lam=np.unique(np.concatenate([
        np.linspace(CORE[0],CORE[1],1001),
        np.linspace(-0.05,0.65,1001),
        np.array([CORE[0],CORE[1],-2,-1,0,0.039,0.048,r["xcr"],10*r["xcr"],1,1.8])
    ]))
    sp={}; cp={}
    for name in ("U","C","T","T7"):
        sp[name]=r[name](lam); sp[name+"d"]=src_der(r[name],lam)
        cp[name]=peval(c[name],lam,*GUARD); cp[name+"d"]=pder(c[name],lam,*GUARD)
    max_st=max_tan=max_div=peak_st=peak_tan=peak_div=0.0
    for i,l1 in enumerate(lam):
        so=spectral_row(sp,i); co=spectral_row(cp,i)
        for k in (0,1):
            peak_st=max(peak_st,float(np.max(np.abs(so[k]))))
            max_st=max(max_st,float(np.max(np.abs(co[k]-so[k]))))
        for k in (2,3,4,5):
            peak_tan=max(peak_tan,float(np.max(np.abs(so[k]))))
            max_tan=max(max_tan,float(np.max(np.abs(co[k]-so[k]))))
        den=l1-lam; mask=np.abs(den)>1e-10
        gs=np.empty_like(lam); gc=np.empty_like(lam)
        gs[mask]=(so[0][mask]-so[1][mask])/den[mask]
        gc[mask]=(co[0][mask]-co[1][mask])/den[mask]
        gs[~mask]=so[2][~mask]-so[3][~mask]
        gc[~mask]=co[2][~mask]-co[3][~mask]
        peak_div=max(peak_div,float(np.max(np.abs(gs))))
        max_div=max(max_div,float(np.max(np.abs(gc-gs))))
    return {
        "kappa":kappa,"N":N,
        "E_sigma":max_st/peak_st,
        "E_tan":max_tan/peak_tan,
        "E_div":max_div/peak_div,
        "pass":(max_st/peak_st<=E_SIG_LIM and max_tan/peak_tan<=E_TAN_LIM and max_div/peak_div<=E_DIV_LIM),
        "coeffs":c,
    }


def main():
    ref=KAPPA_AUDIT[1]
    chosen=None
    for N in CANDIDATES:
        out=audit(ref,N)
        print(N,out["E_sigma"],out["E_tan"],out["E_div"],out["pass"])
        if out["pass"]:
            chosen=N
            break
    assert chosen==3584, chosen
    for k in KAPPA_AUDIT:
        out=audit(k,chosen)
        print("kappa",k,"E",out["E_sigma"],out["E_tan"],out["E_div"])
        assert out["pass"]
        if k==ref:
            for name,c in out["coeffs"].items():
                digest=hashlib.sha256(np.asarray(c,dtype='<f8').tobytes()).hexdigest()
                print(name,digest,float(np.max(np.abs(c))),float(np.sum(np.abs(c))))

if __name__=="__main__":
    main()
