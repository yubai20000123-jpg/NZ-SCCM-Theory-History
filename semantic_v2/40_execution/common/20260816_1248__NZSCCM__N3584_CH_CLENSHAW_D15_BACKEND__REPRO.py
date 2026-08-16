"""NZ-SCCM unified V1 N3584 Cayley-Hamilton / D15 backend probe.

Identity
--------
* source material operator: frozen NC R10
* source compiler candidate: 20260816_1229 N=3584 family source-fidelity pass
* structural field: one continuous complete halfwave, Nguyen second order
* structural spatial sampling/quadrature: ZERO
* this script probes coefficient-space structural tractability only

It intentionally does NOT promote the diagnostic Z0-Z5 locators to production Pu.
"""
from pathlib import Path
import importlib.util, math, time
import numpy as np
from numba import njit

HERE=Path(__file__).resolve().parent
STEEL=HERE.parent/'steel_shell'
COMP_PATH=HERE/'20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__REPRO.py'
BASE_PATH=STEEL/'20260814_2240__NZSCCM_Z0_Z6__REDUCED_IDEALEP_D15__REPRO.py'

def load(name,path):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

comp=load('nc_family_compiler',COMP_PATH)
base=load('historical_d15_kernel',BASE_PATH)

N=3584
KAPPA=comp.KAPPA_AUDIT[1]
GUARD=comp.GUARD
LC=(GUARD[0]+GUARD[1])/2
LH=(GUARD[1]-GUARD[0])/2
COEFF=comp.compile_r10(KAPPA,N)

# The historical low-order invariant generator uses global lc/lh.
# Only its finite kinematic/invariant algebra and exact coefficient moments are reused.
base.lc=LC
base.lh=LH

@njit(cache=True)
def trim_nb(A,tol):
    n0,n1,n2=A.shape;l0=l1=l2=1
    for i in range(n0-1,-1,-1):
        hit=False
        for j in range(n1):
            for k in range(n2):
                if abs(A[i,j,k])>tol:hit=True;break
            if hit:break
        if hit:l0=i+1;break
    for j in range(n1-1,-1,-1):
        hit=False
        for i in range(n0):
            for k in range(n2):
                if abs(A[i,j,k])>tol:hit=True;break
            if hit:break
        if hit:l1=j+1;break
    for k in range(n2-1,-1,-1):
        hit=False
        for i in range(n0):
            for j in range(n1):
                if abs(A[i,j,k])>tol:hit=True;break
            if hit:break
        if hit:l2=k+1;break
    return A[:l0,:l1,:l2].copy()

@njit(cache=True)
def mul_small_nb(A,B,tol):
    """Exact Chebyshev product A*B when B is the low-order K1/K2 field.

    Uses T_i T_j = 1/2[T_{i+j}+T_|i-j|] in each coordinate.
    No spatial points are introduced.
    """
    n0,n1,n2=A.shape;b0,b1,b2=B.shape
    out=np.zeros((n0+b0-1,n1+b1-1,n2+b2-1))
    for p in range(b0):
      for q in range(b1):
       for r in range(b2):
        bv=B[p,q,r]
        if abs(bv)<=tol:continue
        for i in range(n0):
         for j in range(n1):
          for k in range(n2):
           av=A[i,j,k]
           if abs(av)<=tol:continue
           ni=1 if p==0 else 2;nj=1 if q==0 else 2;nk=1 if r==0 else 2
           for ai in range(ni):
            ii=i if p==0 else (i+p if ai==0 else abs(i-p));wi=1.0 if p==0 else .5
            for aj in range(nj):
             jj=j if q==0 else (j+q if aj==0 else abs(j-q));wj=1.0 if q==0 else .5
             for ak in range(nk):
              kk=k if r==0 else (k+r if ak==0 else abs(k-r));wk=1.0 if r==0 else .5
              out[ii,jj,kk]+=av*bv*wi*wj*wk
    return trim_nb(out,tol)

@njit(cache=True)
def scale_nb(A,s,tol):return trim_nb(A*s,tol)

@njit(cache=True)
def add_nb(A,B,s,tol):
    n0=max(A.shape[0],B.shape[0]);n1=max(A.shape[1],B.shape[1]);n2=max(A.shape[2],B.shape[2])
    C=np.zeros((n0,n1,n2))
    C[:A.shape[0],:A.shape[1],:A.shape[2]]+=A
    C[:B.shape[0],:B.shape[1],:B.shape[2]]+=s*B
    return trim_nb(C,tol)

@njit(cache=True)
def add_const_nb(A,c,tol):
    C=A.copy();C[0,0,0]+=c;return trim_nb(C,tol)

@njit(cache=True)
def clenshaw_pair(K1,K2,co,tol):
    """Backward Chebyshev/CH pair.

    If B_k=A_k I+G_k Y and Y^2=K1*Y-K2*I,
      A_k=-2 K2 G_{k+1}-A_{k+2}+c_k
      G_k= 2 A_{k+1}+2 K1 G_{k+1}-G_{k+2}.
    """
    z=np.zeros((1,1,1));A1=z.copy();G1=z.copy();A2=z.copy();G2=z.copy()
    for k in range(co.shape[0]-1,0,-1):
        Ak=add_nb(scale_nb(mul_small_nb(G1,K2,tol),-2,tol),A2,-1,tol)
        Ak=add_const_nb(Ak,co[k],tol)
        Gk=add_nb(add_nb(scale_nb(A1,2,tol),scale_nb(mul_small_nb(G1,K1,tol),2,tol),1,tol),G2,-1,tol)
        A2,G2,A1,G1=A1,G1,Ak,Gk
    Af=add_nb(scale_nb(mul_small_nb(G1,K2,tol),-1,tol),A2,-1,tol)
    Af=add_const_nb(Af,co[0],tol)
    Gf=add_nb(add_nb(A1,mul_small_nb(G1,K1,tol),1,tol),G2,-1,tol)
    return Af,Gf

def pad_diff(A,B):
    sh=tuple(max(A.shape[d],B.shape[d]) for d in range(3))
    a=np.zeros(sh);b=np.zeros(sh)
    a[:A.shape[0],:A.shape[1],:A.shape[2]]=A
    b[:B.shape[0],:B.shape[1],:B.shape[2]]=B
    return float(np.max(np.abs(a-b)))

def n48_identity_check():
    c=dict(b=6000.,ell=6000.,tc=122.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=355.)
    f=base.low(.915,.00317,c,nu=.18,q0=.004)
    c48=comp.compile_r10(KAPPA,48)['T']
    forward=base.recur(f['K1'],f['K2'],c48,tol=1e-12)
    backward=clenshaw_pair(f['K1'],f['K2'],c48,1e-12)
    return pad_diff(forward[0],backward[0]),pad_diff(forward[1],backward[1])

def high_pair(D,q,c,q0,name,tol):
    f=base.low(D,q,c,nu=.18,q0=q0)
    return clenshaw_pair(f['K1'],f['K2'],COEFF[name],tol),f

def buildS_high(D,q,c,q0,tol):
    f=base.low(D,q,c,nu=.18,q0=q0);K1,K2=f['K1'],f['K2']
    U=clenshaw_pair(K1,K2,COEFF['U'],tol)
    C=clenshaw_pair(K1,K2,COEFF['C'],tol)
    T=clenshaw_pair(K1,K2,COEFF['T'],tol)
    T7=clenshaw_pair(K1,K2,COEFF['T7'],tol)
    CC=base.sm(base.det(C,K1,K2,tol),C,tol)
    TC=base.pa(base.sm(base.tr(T,K1,tol),C,tol),base.pm(C,T,K1,K2,tol),-1,tol)
    t7=base.tr(T7,K1,tol)
    inner=(base.add(t7,T7[0],-1,tol),base.scale(T7[1],-1,tol))
    TT=base.sm(base.det(T,K1,K2,tol),inner,tol)
    S=base.pa(base.pa(base.pa(U,CC,-base.acc,tol),TC,1,tol),TT,-base.rho*base.at,tol)
    return S,f,{'U':[U[0].shape,U[1].shape],'C':[C[0].shape,C[1].shape],
                'T':[T[0].shape,T[1].shape],'T7':[T7[0].shape,T7[1].shape],
                'S':[S[0].shape,S[1].shape]}

def concrete_high(D,q,c,q0,tol):
    S,f,diag=buildS_high(D,q,c,q0,tol);A,B=S
    Syy=base.add(A,base.mul(B,f['Yyy'],tol),1,tol)
    iS=base.integ(Syy)
    Pc=-c['fc']*c['b']*c['tc']/(2*math.pi**2)*iS
    trs=base.tr(S,f['K1'],tol)
    gm=base.add(f['Gq'],base.scale(f['I1q'],base.lc,tol),-1,tol)
    sxq=base.add(base.mul(A,f['I1q'],tol),base.scale(base.mul(B,gm,tol),1/base.lh,tol),1,tol)
    Q=base.add(base.scale(sxq,1.18,tol),base.scale(base.mul(f['I1q'],trs,tol),.18,tol),-1,tol)
    Rq=c['fc']*c['eps0']*c['b']*c['ell']*c['tc']/(2*math.pi**2)*base.integ(Q)
    return Pc,Rq,diag

if __name__=='__main__':
    print('FORMAL STRUCTURAL SPATIAL/THICKNESS QUADRATURE = 0')
    print('N48 forward/backward pair diff =',n48_identity_check())
    Z0=dict(b=6000.,ell=6000.,tc=122.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=355.)
    for tol in (2e-4,1e-4,5e-5,2e-5,1e-5):
        t=time.time();Pc,Rq,d=concrete_high(.915,.002573,Z0,.004,tol)
        print('Z0 backend tolerance',tol,'Pc_MN',Pc/1e6,'Rq_MNmm',Rq/1e6,'seconds',time.time()-t,'shapes',d)
    print('Z6 deep-state execution is a separate timeout/tractability probe; see execution report.')
