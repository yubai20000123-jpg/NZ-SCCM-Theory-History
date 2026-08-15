"""Reproduce the 22:20 NZ-SCCM augmented-FvK representation expansion audit.

No Pu, no root solve, no structural quadrature.  This script only audits:
- sparse monomial support before/after p20,p02;
- low-order degree boxes;
- Jacobian scaling sensitivity;
- worst-case dense N48 bounding-box envelopes implied by the existing dense implementation.
"""
import math
import numpy as np
from numpy.polynomial.chebyshev import poly2cheb


def padd(a,b,s=1.0,tol=1e-15):
    r=dict(a)
    for k,v in b.items():
        r[k]=r.get(k,0.0)+s*v
        if abs(r[k])<tol: r.pop(k,None)
    return r

def ps(a,s,tol=1e-15): return {k:v*s for k,v in a.items() if abs(v*s)>=tol}
def pc(x): return {(0,0,0):float(x)} if x else {}
def mon(i,j,k,c=1.0): return {(i,j,k):float(c)}
def pmul(a,b,tol=1e-15):
    r={}
    for x,v in a.items():
        for y,w in b.items():
            k=tuple(x[i]+y[i] for i in range(3)); r[k]=r.get(k,0.0)+v*w
    return {k:v for k,v in r.items() if abs(v)>=tol}

def p2c_sparse(p):
    mx=[0,0,0]
    for k in p:
        for d in range(3): mx[d]=max(mx[d],k[d])
    out=np.zeros(tuple(x+1 for x in mx)); cache={}
    for (i,j,k),v in p.items():
        for n in (i,j,k):
            if n not in cache:
                a=np.zeros(n+1); a[n]=1.0; cache[n]=poly2cheb(a)
        A,B,C=cache[i],cache[j],cache[k]
        t=v*A[:,None,None]*B[None,:,None]*C[None,None,:]
        out[:t.shape[0],:t.shape[1],:t.shape[2]] += t
    return out

def build(D,q,cw,p20,p02):
    b=12000.; a=9000.; t=122.; e0=.0018712490394580678; nu=.18; q0=.0015
    k=b/a; M=math.pi**2/e0*(q0*q+.5*q*q); B=math.pi**2*t/(2*e0*b)*q
    ex=ps(mon(0,2,0),M); ex=padd(ex,ps(mon(2,2,0),-M)); ex=padd(ex,ps(mon(1,1,1),B))
    ey=pc(-D); ey=padd(ey,ps(mon(2,0,0),k*k*M)); ey=padd(ey,ps(mon(2,2,0),-k*k*M)); ey=padd(ey,ps(mon(1,1,1),k*k*B))
    exc=ps(mon(1,2,0),4/math.pi)
    eyc=ps(pmul(mon(1,0,0),padd(pc(1),mon(0,2,0,-2))),8*k*k/math.pi)
    ex20=padd(mon(0,2,0),mon(2,2,0,-2))
    ey20=ps(pmul(padd(pc(1),mon(2,0,0,-2)),padd(pc(1),mon(0,2,0,-2))),.5*k*k)
    ey02=padd(pc(1),mon(0,2,0,-2))
    ex=padd(ex,ps(exc,cw)); ey=padd(ey,ps(eyc,cw))
    ex=padd(ex,ps(ex20,p20)); ey=padd(ey,ps(ey20,p20)); ey=padd(ey,ps(ey02,p02))
    C2=pc(1); C2=padd(C2,mon(2,0,0,-1)); C2=padd(C2,mon(0,2,0,-1)); C2=padd(C2,mon(2,2,0,1))
    uu=padd(ps(mon(1,1,0),M),mon(0,0,1,-B))
    g2=ps(pmul(C2,pmul(uu,uu)),4*k*k)
    den=1-nu*nu
    Exx=ps(padd(ex,ps(ey,nu)),1/den); Eyy=ps(padd(ps(ex,nu),ey),1/den)
    I1=padd(Exx,Eyy); I2=padd(pmul(Exx,Eyy),ps(g2,-1/(4*(1+nu)**2)))
    lc=-.515; lh=.635
    K1=ps(padd(I1,pc(-2*lc)),1/lh)
    K2=ps(padd(padd(I2,ps(I1,-lc)),pc(lc*lc)),1/lh**2)
    return dict(ex=ex,ey=ey,g2=g2,Exx=Exx,Eyy=Eyy,I1=I1,I2=I2,K1=K1,K2=K2)

def info(p):
    md=tuple(max((k[i] for k in p),default=0) for i in range(3))
    return len(p),md

old=build(.5,.007244278905,-.0154563484942,0.,0.)
aug=build(.5,.008002,-.077622,-.060657,.165133)
for name in ('ex','ey','g2','Exx','Eyy','I1','I2','K1','K2'):
    print(name,'old',info(old[name]),'aug',info(aug[name]))
for state,label in ((old,'old'),(aug,'aug')):
    for name in ('K1','K2'):
        A=p2c_sparse(state[name]); nz=np.abs(A)>1e-12
        print(label,name,'shape',A.shape,'nnz',int(nz.sum()),'minabs',float(np.min(np.abs(A[nz]))))

J=np.array([
[2787333.552306,96636.847993,-7730.455557,19480.240744],
[67271.966759,7906.237458,-914.530413,2343.313840],
[-20821.855030,-785.947042,155.898351,46.725646],
[-4168.426027,2094.413911,-426.456221,882.897056]],float)
print('cond_raw',np.linalg.cond(J))
Jr=J/np.linalg.norm(J,axis=1)[:,None]
print('cond_row',np.linalg.cond(Jr))
Jc=J/np.linalg.norm(J,axis=0)[None,:]
print('cond_col',np.linalg.cond(Jc))
Jrc=Jr/np.linalg.norm(Jr,axis=0)[None,:]
print('cond_row_col',np.linalg.cond(Jrc))
xs=np.array([.008,.08,.06,.16]); Js=J*xs[None,:]; Jsr=Js/np.linalg.norm(Js,axis=1)[:,None]
print('cond_scaled_plus_row',np.linalg.cond(Jsr))
print('singular_values',np.linalg.svd(J,compute_uv=False))

# Dense upper-bound envelope implied by N48 degree and current full-field products.
d1=np.array([2,2,1]); F=48*d1; detF_F=3*F; stress=detF_F+d1
shape=stress+1; entries=int(np.prod(shape)); ctl=2*stress+1; ctl_entries=int(np.prod(ctl)); conv=2*ctl-1; conv_entries=int(np.prod(conv))
print('F48_degree',tuple(F))
print('detF_times_F_degree',tuple(detF_F))
print('stress_rough_degree',tuple(stress),'entries',entries,'MiB',entries*8/1024**2)
print('ctl_shape',tuple(ctl),'entries',ctl_entries,'GiB',ctl_entries*8/1024**3)
print('same_size_conv_shape',tuple(conv),'entries',conv_entries,'GiB_real',conv_entries*8/1024**3)
