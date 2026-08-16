"""NZ-SCCM 20260816_1110 R10 multirate-C1 source fidelity reproducer.

No structural spatial sampling/quadrature is used.
Material-coordinate nodes below are coefficient-generation/audit coordinates only.
The R10 physical current operator is unchanged.
"""
import hashlib, math
import numpy as np
from numpy.polynomial.chebyshev import chebvander, chebval, chebder

KAPPA=2.0005129533678754
RHO=.1
XCR=RHO/KAPPA
ETA=XCR/20
UR=.03
HH=.09799750427197301
ACC=.1072329249362415
AT=1-2**(-1/8)
LA,LB=-1.50,.35
LC,LH=(LA+LB)/2,(LB-LA)/2
CORE=(-1.40,.30)
ORDERS={'U':256,'C':1024,'T':1280,'T7':512}
IDX={'U':0,'C':1,'T':2,'T7':3}


def Pi(z):
    z=np.asarray(z,float); s=z*z+ETA*ETA; r=np.sqrt(s)
    return z*z*(r+z)/(2*s)


def dPi(z):
    z=np.asarray(z,float); s=z*z+ETA*ETA; r=np.sqrt(s); B=r+z
    return .5*(2*z*B/s + z*z*(z/r+1)/s - z*z*B*(2*z)/(s*s))


def uR(t):
    t=np.asarray(t,float); r=t/XCR; o=np.empty_like(r)
    m=r<=1; rr=r[m]
    o[m]=RHO*rr+(10*HH-6*RHO)*rr**3+(8*RHO-15*HH)*rr**4+(6*HH-3*RHO)*rr**5
    m2=(r>1)&(r<=10); s=(r[m2]-1)/9
    o[m2]=HH+(UR-HH)*(10*s**3-15*s**4+6*s**5)
    o[r>10]=UR
    return o


def duR(t):
    t=np.asarray(t,float); r=t/XCR; o=np.empty_like(r)
    m=r<=1; rr=r[m]
    o[m]=(RHO+3*(10*HH-6*RHO)*rr**2+4*(8*RHO-15*HH)*rr**3+5*(6*HH-3*RHO)*rr**4)/XCR
    m2=(r>1)&(r<=10); s=(r[m2]-1)/9
    o[m2]=(UR-HH)*(30*s**2-60*s**3+30*s**4)/(9*XCR)
    o[r>10]=0
    return o


def targets(lam):
    lam=np.asarray(lam,float); c=Pi(-lam); t=Pi(lam)
    C=KAPPA*c/(1+(KAPPA-2)*c+c*c); u=uR(t); T=u/RHO
    U=KAPPA*lam-C+KAPPA*c+u-KAPPA*t
    return [U,C,T,T**7]


def target_derivatives(lam):
    lam=np.asarray(lam,float); c=Pi(-lam); t=Pi(lam)
    dc=-dPi(-lam); dt=dPi(lam)
    den=1+(KAPPA-2)*c+c*c
    Cp=KAPPA*(1-c*c)/(den*den)*dc
    up=duR(t)*dt; T=uR(t)/RHO; Tp=up/RHO
    Up=KAPPA-Cp+KAPPA*dc+up-KAPPA*dt
    return [Up,Cp,Tp,7*T**6*Tp]


def compile_primitive(name,oversample=4):
    idx=IDX[name]; deg=ORDERS[name]; n=oversample*(deg+1)
    th=(np.arange(n)+.5)*math.pi/n
    lam=LC+LH*np.cos(th); xi=(lam-LC)/LH
    V=chebvander(xi,deg); y=targets(lam)[idx]
    E=np.eye(deg+1); xi0=-LC/LH
    vr=np.array([chebval(xi0,E[j]) for j in range(deg+1)])
    dr=np.array([chebval(xi0,chebder(E[j]))/LH for j in range(deg+1)])
    G=np.vstack([vr,dr])
    d=np.array([0,KAPPA]) if name=='U' else np.array([0.,0.])
    H=V.T@V
    K=np.block([[H,G.T],[G,np.zeros((2,2))]])
    return np.linalg.solve(K,np.r_[V.T@y,d])[:deg+1]


def primitive_metrics(name,coef,a,b,n=60001):
    idx=IDX[name]; x=np.linspace(a,b,n); xi=(x-LC)/LH
    p=chebval(xi,coef); dp=chebval(xi,chebder(coef))/LH
    y=targets(x)[idx]; dy=target_derivatives(x)[idx]
    e0=np.abs(p-y); e1=np.abs(dp-dy)
    return {
        'E0':float(e0.max()),'E0_at':float(x[e0.argmax()]),
        'E1_abs':float(e1.max()),
        'E1_rel_peak':float(e1.max()/max(np.abs(dy).max(),1e-30)),
        'E1_at':float(x[e1.argmax()]),
    }


def eval_comp(coefs,name,x):
    return chebval((np.asarray(x)-LC)/LH,coefs[name])


def eval_comp_derivative(coefs,name,x):
    return chebval((np.asarray(x)-LC)/LH,chebder(coefs[name]))/LH


def operator_metrics(coefs,n=1201):
    lam=np.linspace(CORE[0],CORE[1],n)
    Ue,Ce,Te,T7e=targets(lam); Uep,Cep,Tep,T7ep=target_derivatives(lam)
    Uc,Cc,Tc,T7c=[eval_comp(coefs,k,lam) for k in ('U','C','T','T7')]
    Ucp,Ccp,Tcp,T7cp=[eval_comp_derivative(coefs,k,lam) for k in ('U','C','T','T7')]

    sp_e=Ue[:,None]-ACC*Ce[:,None]**2*Ce[None,:]+Ce[:,None]*Te[None,:]-RHO*AT*Te[:,None]*Te[None,:]**8
    sp_c=Uc[:,None]-ACC*Cc[:,None]**2*Cc[None,:]+Cc[:,None]*Tc[None,:]-RHO*AT*Tc[:,None]*(T7c[None,:]*Tc[None,:])
    se=np.abs(sp_c-sp_e); ix=np.unravel_index(np.argmax(se),se.shape)

    d11e=Uep[:,None]-2*ACC*Ce[:,None]*Cep[:,None]*Ce[None,:]+Cep[:,None]*Te[None,:]-RHO*AT*Tep[:,None]*Te[None,:]**8
    d12e=-ACC*Ce[:,None]**2*Cep[None,:]+Ce[:,None]*Tep[None,:]-RHO*AT*Te[:,None]*(8*Te[None,:]**7*Tep[None,:])
    d11c=Ucp[:,None]-2*ACC*Cc[:,None]*Ccp[:,None]*Cc[None,:]+Ccp[:,None]*Tc[None,:]-RHO*AT*Tcp[:,None]*(T7c[None,:]*Tc[None,:])
    d12c=-ACC*Cc[:,None]**2*Ccp[None,:]+Cc[:,None]*Tcp[None,:]-RHO*AT*Tc[:,None]*(T7cp[None,:]*Tc[None,:]+T7c[None,:]*Tcp[None,:])
    te=np.maximum(np.abs(d11c-d11e),np.abs(d12c-d12e)); it=np.unravel_index(np.argmax(te),te.shape)
    source_peak=max(np.abs(d11e).max(),np.abs(d12e).max())
    return {
        'stress_max_abs':float(se[ix]),
        'stress_pair':(float(lam[ix[0]]),float(lam[ix[1]])),
        'stress_source':float(sp_e[ix]),'stress_compiled':float(sp_c[ix]),
        'tangent_max_abs':float(te[it]),
        'tangent_pair':(float(lam[it[0]]),float(lam[it[1]])),
        'source_peak_tangent':float(source_peak),
        'tangent_rel_source_peak':float(te[it]/source_peak),
    }


def main():
    print('FORMAL STRUCTURAL SAMPLING/QUADRATURE = 0')
    print('guard',LA,LB,'core',CORE,'orders',ORDERS)
    coefs={k:compile_primitive(k) for k in ORDERS}
    for name,coef in coefs.items():
        xi0=-LC/LH
        print(name,'degree',ORDERS[name],
              'sha256',hashlib.sha256(np.asarray(coef,dtype='<f8').tobytes()).hexdigest(),
              'maxabs',np.max(np.abs(coef)),'sumabs',np.sum(np.abs(coef)),
              'F0',chebval(xi0,coef),
              'dF0',chebval(xi0,chebder(coef))/LH,
              'core',primitive_metrics(name,coef,*CORE))
    print('operator',operator_metrics(coefs))
    print('NEW_Z0_Z5_PU=NOT_CALCULATED')
    print('NEXT=Z0_Z5_AR2_MULTIRATE_R10_TO_VARIABLE_ORDER_MOMENT_FIRST_D15_RECOMPILE_GATE')


if __name__=='__main__':
    main()
