"""NZ-SCCM 20260816_1134 fixed-N48 source-fidelity audit.

Material compiler order is fixed at 48 for U/C/T/T7.
No structural spatial sampling/quadrature is used.
All LP/audit coordinates are material coordinates for coefficient generation only.
"""
import math, numpy as np
from scipy.optimize import linprog
from numpy.polynomial.chebyshev import chebvander, chebval, chebder

KAPPA=2.0005129533678754; RHO=.1; XCR=RHO/KAPPA; ETA=XCR/20
UR=.03; HH=.09799750427197301; ACC=.1072329249362415; AT=1-2**(-1/8)
DEG=48
CASES={'Z0':(-1.25,.30),'Z1':(-.85,.25),'Z2':(-1.50,.35),'Z3':(-.95,.25),'Z4':(-1.25,.25),'Z5':(-1.15,.15)}
OCC={'Z0':(-1.1224371257,.2071403380),'Z1':(-.7489141618,.1826321890),'Z2':(-1.3894723959,.2695630424),'Z3':(-.8485265156,.1762333204),'Z4':(-1.1227628996,.1809175820),'Z5':(-1.0640988844,.0741783692)}
IDX={'U':0,'C':1,'T':2,'T7':3}

def Pi(z):
    z=np.asarray(z,float); s=z*z+ETA*ETA; return z*z*(np.sqrt(s)+z)/(2*s)

def uR(t):
    t=np.asarray(t,float); r=t/XCR; o=np.empty_like(r)
    m=r<=1; x=r[m]
    o[m]=RHO*x+(10*HH-6*RHO)*x**3+(8*RHO-15*HH)*x**4+(6*HH-3*RHO)*x**5
    m=(r>1)&(r<=10); x=(r[m]-1)/9
    o[m]=HH+(UR-HH)*(10*x**3-15*x**4+6*x**5)
    o[r>10]=UR
    return o

def targets(lam):
    lam=np.asarray(lam,float); c=Pi(-lam); t=Pi(lam)
    C=KAPPA*c/(1+(KAPPA-2)*c+c*c); u=uR(t); T=u/RHO
    U=KAPPA*lam-C+KAPPA*c+u-KAPPA*t
    return U,C,T,T**7

def minimax(name,la,lb,n=4001):
    lc=(la+lb)/2; lh=(lb-la)/2; x=np.linspace(la,lb,n); xi=(x-lc)/lh
    V=chebvander(xi,DEG); y=targets(x)[IDX[name]]
    E=np.eye(DEG+1); xi0=-lc/lh
    vr=np.array([chebval(xi0,E[k]) for k in range(DEG+1)])
    dr=np.array([chebval(xi0,chebder(E[k]))/lh for k in range(DEG+1)])
    G=np.vstack([vr,dr]); d=np.array([0.,KAPPA]) if name=='U' else np.zeros(2)
    obj=np.r_[np.zeros(DEG+1),1.]
    Aub=np.vstack([np.c_[V,-np.ones(n)],np.c_[-V,-np.ones(n)]])
    bub=np.r_[y,-y]
    res=linprog(obj,A_ub=Aub,b_ub=bub,A_eq=np.c_[G,np.zeros(2)],b_eq=d,
                bounds=[(None,None)]*(DEG+1)+[(0,None)],method='highs')
    if not res.success: raise RuntimeError(res.message)
    return lc,lh,res.x[:-1],res.x[-1]

def audit(name,lc,lh,coef,la,lb,n=50001):
    x=np.linspace(la,lb,n); y=targets(x)[IDX[name]]; p=chebval((x-lc)/lh,coef); e=np.abs(p-y); i=e.argmax()
    return float(e[i]),float(x[i])

def master_source(l1,l2):
    U1,C1,T1,_=targets(np.asarray(l1)); U2,C2,T2,_=targets(np.asarray(l2))
    return U1-ACC*C1*C1*C2+C1*T2-RHO*AT*T1*T2**8

def master_comp(lam,lc,lh,co):
    xi=(lam-lc)/lh; return [chebval(xi,co[k]) for k in ('U','C','T','T7')]

def master_error(lc,lh,co,la,lb,n=801):
    x=np.linspace(la,lb,n); U,C,T,T7=targets(x); Uc,Cc,Tc,T7c=master_comp(x,lc,lh,co)
    se=U[:,None]-ACC*C[:,None]**2*C[None,:]+C[:,None]*T[None,:]-RHO*AT*T[:,None]*T[None,:]**8
    sc=Uc[:,None]-ACC*Cc[:,None]**2*Cc[None,:]+Cc[:,None]*Tc[None,:]-RHO*AT*Tc[:,None]*(T7c[None,:]*Tc[None,:])
    e=np.abs(sc-se); i=np.unravel_index(np.argmax(e),e.shape)
    return float(e[i]),(float(x[i[0]]),float(x[i[1]]))

def t_only_error(lc,lh,Tco,la,lb,n=20001):
    anchor=max(la+.01,-1.0); l2=np.linspace(max(0.,la),lb,n)
    U1,C1,T1,_=targets(np.array([anchor])); _,C2,T2,_=targets(l2); Tc=chebval((l2-lc)/lh,Tco)
    se=U1[0]-ACC*C1[0]**2*C2+C1[0]*T2-RHO*AT*T1[0]*T2**8
    sc=U1[0]-ACC*C1[0]**2*C2+C1[0]*Tc-RHO*AT*T1[0]*Tc**8
    return float(np.max(np.abs(sc-se)))

if __name__=='__main__':
    print('FORMAL_SPATIAL_SAMPLING=0; QUADRATURE=0; SUBDOMAINS=1; DEGREE=48')
    for case,(la,lb) in CASES.items():
        co={}; meta={}; lc=lh=None
        for name in ('U','C','T','T7'):
            lc,lh,c,lp=minimax(name,la,lb); co[name]=c; meta[name]=audit(name,lc,lh,c,la,lb)
        me=master_error(lc,lh,co,la,lb); te=t_only_error(lc,lh,co['T'],la,lb)
        lc2,lh2,t2,_=minimax('T',*OCC[case]); occ=audit('T',lc2,lh2,t2,*OCC[case])[0]
        print(case,'primitive_E0',meta,'master',me,'T_only_master',te,'occupied_T_E0',occ)
    print('DECISION=SINGLE_GLOBAL_N48_COEFFICIENT_ONLY_REPAIR_FAIL')
    print('NEXT=Z0_Z5_AR2_FIXED_N48_MULTISCALE_ANALYTIC_REPRESENTATION_GATE')
