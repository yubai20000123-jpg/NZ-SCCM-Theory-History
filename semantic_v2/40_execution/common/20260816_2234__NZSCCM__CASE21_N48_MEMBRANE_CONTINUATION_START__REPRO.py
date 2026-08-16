"""Case21 N48-C1/MM + CH-equivalent Chebyshev-in-sine + General-D15 reproducer.
2026-08-16 22:34 +08:00

Formal structural spatial quadrature/sampling = 0.  FFT is used only for
coefficient-index convolution in a symmetric Laurent representation.
The script reproduces (1) the 2026-08-12 18:02 r=0 fingerprint and
(2) the first nonzero five-membrane connected-continuation state.
"""
from pathlib import Path
import math
import numpy as np
from scipy.signal import fftconvolve
from numpy.polynomial.chebyshev import cheb2poly

ROOT = Path(__file__).resolve().parents[3]
COEFF = ROOT / "current/case21/NZ_SCCM_CASE21_FRESH_MATERIAL_COEFFICIENTS_20260812_1802.csv"
raw = np.genfromtxt(COEFF, delimiter=",", names=True)
CFS = {"U":raw["U_C1"], "C":raw["C_C1"], "T":raw["T_MM"], "T7":raw["T7_C1"]}

THR = 1e-10              # floating coefficient noise floor, not a theory parameter
N = 28                    # formal corrector tensor cap inherited from Case21 coefficient-space implementation
S = N + 1
fc, E0, eps0, nu = 21.23, 20321.0, 0.00209, 0.18
b = ell = 1220.0
tp, q0 = 19.30, 1/400
Es, rsx, rsy = 200000.0, 0.00375, 0.00375
lc, lh = -0.515, 0.635
acc, rho, at = 0.1072329249362415, 0.1, 1-2**(-1/8)


def zero(): return np.zeros((S,S,S), float)
def mono(v,i=0,j=0,k=0):
    a=zero(); a[i,j,k]=v; return a
def add(a,b,sa=1.0,sb=1.0): return sa*a+sb*b
def scale(a,c): return a*c


def to_laurent(a):
    aa=a.copy(); aa[np.abs(aa)<THR]=0.0; c=N
    Lx=np.zeros((2*N+1,S,S)); Lx[c]=aa[0]
    Lx[c+np.arange(1,S)]=aa[1:]/2; Lx[c-np.arange(1,S)]=aa[1:]/2
    Ly=np.zeros((2*N+1,2*N+1,S)); Ly[:,c]=Lx[:,0]
    Ly[:,c+np.arange(1,S)]=Lx[:,1:]/2; Ly[:,c-np.arange(1,S)]=Lx[:,1:]/2
    L=np.zeros((2*N+1,2*N+1,2*N+1)); L[:,:,c]=Ly[:,:,0]
    L[:,:,c+np.arange(1,S)]=Ly[:,:,1:]/2; L[:,:,c-np.arange(1,S)]=Ly[:,:,1:]/2
    return L


def mul(a,b_):
    if not np.any(a) or not np.any(b_): return zero()
    C=fftconvolve(to_laurent(a),to_laurent(b_),mode="full")
    base=2*N; out=C[base:base+S,base:base+S,base:base+S].copy()
    out[1:]*=2; out[:,1:]*=2; out[:,:,1:]*=2
    out[np.abs(out)<THR]=0.0
    return out

U2=add(scale(mono(1),.5),scale(mono(1,2,0,0),.5))
V2=add(scale(mono(1),.5),scale(mono(1,0,2,0),.5))
OMU2=add(mono(1),U2,1,-1); OMV2=add(mono(1),V2,1,-1)
C2=mul(OMU2,OMV2)
COS2X=scale(mono(1,2,0,0),-1); COS2Y=scale(mono(1,0,2,0),-1)
COS2XY=mul(COS2X,COS2Y); UV=mono(1,1,1,0); SHEAR=scale(mul(UV,C2),4)


def madd(A,B,sa=1.0,sb=1.0): return tuple(add(A[i],B[i],sa,sb) for i in range(3))
def mscale(A,c): return tuple(scale(x,c) for x in A)
def mmul(A,B):
    a,b_,h=A; d,e,g=B; q=mul(C2,mul(h,g))
    return add(mul(a,d),q), add(mul(b_,e),q), add(mul(a,g),mul(h,e))
def detm(A): return add(mul(A[0],A[1]),mul(C2,mul(A[2],A[2])),1,-1)
def adjm(A): return A[1],A[0],scale(A[2],-1)


def kinematics(D,q,r):
    r0,r20,r22,s02,s22=r
    Cm=math.pi**2/eps0*(q0*q+.5*q*q); Cb=math.pi**2*tp/(2*eps0*b)*q
    ex=add(mono(nu*D),scale(mul(OMU2,V2),Cm)); ex=add(ex,scale(mono(1,1,1,1),Cb))
    ey=add(mono(-D),scale(mul(U2,OMV2),Cm)); ey=add(ey,scale(mono(1,1,1,1),Cb))
    ex=add(add(add(ex,mono(r0)),scale(COS2X,r20)),scale(COS2XY,r22))
    ey=add(add(ey,scale(COS2Y,s02)),scale(COS2XY,s22))
    x11=scale(add(ex,ey,1,nu),1/(1-nu**2)); x22=scale(add(ex,ey,nu,1),1/(1-nu**2))
    h=add(scale(UV,(Cm-2*(r22+s22))/(1+nu)),scale(mono(1,0,0,1),-Cb/(1+nu)))
    return (x11,x22,h),(ex,ey),Cm,Cb


def stress(D,q,r):
    X,ee,Cm,Cb=kinematics(D,q,r); I=(mono(1),mono(1),zero()); Y=mscale(madd(X,mscale(I,-lc)),1/lh)
    Tm1,T0=I,Y
    F={k:madd(mscale(I,CFS[k][0]),mscale(T0,CFS[k][1])) for k in CFS}
    for n in range(1,48):
        T1=madd(mscale(mmul(Y,T0),2),Tm1,1,-1)
        for k in F: F[k]=madd(F[k],mscale(T1,CFS[k][n+1]))
        Tm1,T0=T0,T1
    U,C,T,T7=(F[k] for k in ("U","C","T","T7"))
    CC=tuple(mul(detm(C),x) for x in C); CT=mmul(C,adjm(T)); TT7=tuple(mul(detm(T),x) for x in adjm(T7))
    return madd(madd(madd(U,CC,1,-acc),CT),TT7,1,-rho*at),ee,Cm,Cb

mx=[]; mz=[]
for n in range(S):
    c=np.zeros(n+1); c[n]=1; p=cheb2poly(c)
    mx.append(sum(a*math.sqrt(math.pi)*math.gamma((j+1)/2)/math.gamma(j/2+1) for j,a in enumerate(p)))
    mz.append(sum(a*(0 if j%2 else 2/(j+1)) for j,a in enumerate(p)))
mx=np.asarray(mx); mz=np.asarray(mz)
W=mx[:,None,None]*mx[None,:,None]*mz[None,None,:]; WA=mx[:,None]*mx[None,:]
def integ(a): return float(np.sum(a*W))
def area(a): return float(np.sum(a[:,:,0]*WA))


def evaluate(D,q,r):
    St,(ex,ey),Cm,Cb=stress(D,q,np.asarray(r,float)); sx,sy,sh=St
    Rc=np.array([integ(sx),integ(mul(sx,COS2X)),integ(mul(sx,COS2XY))-integ(mul(sh,SHEAR)),
                 integ(mul(sy,COS2Y)),integ(mul(sy,COS2XY))-integ(mul(sh,SHEAR))])*fc/2
    ex0=ex.copy(); ex0[:,:,1:]=0; ey0=ey.copy(); ey0[:,:,1:]=0
    Rs=np.array([rsx*Es*eps0*area(ex0),rsx*Es*eps0*area(mul(ex0,COS2X)),rsx*Es*eps0*area(mul(ex0,COS2XY)),
                 rsy*Es*eps0*area(mul(ey0,COS2Y)),rsy*Es*eps0*area(mul(ey0,COS2XY))])
    Pc=-fc*b*tp/(2*math.pi**2)*integ(sy)/1000
    Ps=-rsy*tp*b*Es*eps0/math.pi**2*area(ey0)/1000
    Cmq=math.pi**2/eps0*(q0+q); Cbq=math.pi**2*tp/(2*eps0*b)
    exq=add(scale(mul(OMU2,V2),Cmq),scale(mono(1,1,1,1),Cbq))
    eyq=add(scale(mul(U2,OMV2),Cmq),scale(mono(1,1,1,1),Cbq))
    gh=add(scale(UV,2*Cmq),scale(mono(1,0,0,1),-2*Cbq))
    Q=add(add(mul(sx,exq),mul(sy,eyq)),mul(C2,mul(sh,gh)))
    JO=b*ell*tp/(2*math.pi**2); Rqc=fc*eps0*JO*integ(Q)/1000
    exq0=exq.copy(); exq0[:,:,1:]=0; eyq0=eyq.copy(); eyq0[:,:,1:]=0
    Rqs=(rsx*Es*eps0**2*tp*b*ell/math.pi**2*area(mul(ex0,exq0)) +
         rsy*Es*eps0**2*tp*b*ell/math.pi**2*area(mul(ey0,eyq0)))/1000
    return {"D":D,"q":q,"r":list(map(float,r)),"Cm":Cm,"Cb":Cb,"D15_Syy":integ(sy),"D15_Qq":integ(Q),
            "Rm":(Rc+Rs).tolist(),"Rm_norm2":float(np.linalg.norm(Rc+Rs)),"Pc_kN":Pc,"Ps_kN":Ps,"P_kN":Pc+Ps,
            "Rqc_kNmm":Rqc,"Rqs_kNmm":Rqs,"Rq_kNmm":Rqc+Rqs}

if __name__ == "__main__":
    baseline=evaluate(0.7822850963110681,0.0017707520964949533,[0,0,0,0,0])
    first=evaluate(0.016046306,1e-4,[-0.0004765646208971642,-0.000232281931854189,0.0002805628349612065,-0.0002432861950486819,0.00030341587937381494])
    print("BASELINE_1802",baseline)
    print("FIRST_CONNECTED_POINT",first)
    print("N_formal_spatial_sampling=0")
    print("N_formal_spatial_quadrature=0")
    print("N_formal_spatial_subdomains=1")
    print("N_formal_thickness_quadrature=0")
    print("NEW_membrane_redistributed_Pu=NOT_RELEASED")
