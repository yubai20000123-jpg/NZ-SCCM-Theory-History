# NZ-SCCM Z0-Z5 a/500 + local progressive radial-cap reproduction kernel
# Timestamp: 2026-08-15 11:48 +08:00
# Structural spatial sampling/quadrature = 0.
# Material-coordinate nodes are used only to compile alpha_loc(r); they are not structural points.
# Identity: ENGINEERING DIAGNOSTIC, not a replacement for old strict Rq-L certificates.

from pathlib import Path
import importlib.util, math
import numpy as np
from scipy.signal import fftconvolve
from scipy.optimize import root, root_scalar
from numpy.polynomial.chebyshev import chebvander

HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / '20260814_2240__NZSCCM_Z0_Z6__REDUCED_IDEALEP_D15__REPRO.py'
spec = importlib.util.spec_from_file_location('base_kernel', BASE_PATH)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

# -----------------------------------------------------------------------------
# Polynomial field algebra in x=sin(X), y=sin(Y), eta in [-1,1].
# Structural integrals are exact moments of monomials, not quadrature points.
# -----------------------------------------------------------------------------
def trim(A,tol=1e-14):
    A=np.asarray(A,float); sl=[]
    for ax in range(3):
        other=tuple(i for i in range(3) if i!=ax)
        q=np.max(np.abs(A),axis=other); ids=np.where(q>tol)[0]
        sl.append(slice(0,int(ids[-1]) + 1 if ids.size else 1))
    return A[tuple(sl)]

def add(A,B,s=1.0,tol=1e-14):
    sh=tuple(max(A.shape[i],B.shape[i]) for i in range(3)); C=np.zeros(sh)
    C[:A.shape[0],:A.shape[1],:A.shape[2]] += A
    C[:B.shape[0],:B.shape[1],:B.shape[2]] += s*B
    return trim(C,tol)

def scale(A,s,tol=1e-14): return trim(A*s,tol)
def mul(A,B,tol=1e-13): return trim(fftconvolve(A,B),tol)
def mono(i,j,k,c=1.0):
    A=np.zeros((i+1,j+1,k+1)); A[i,j,k]=c; return A

def const(c): return mono(0,0,0,c)

def moments(nmax):
    # integral_0^pi sin^n(X) dX, analytically via Gamma functions
    return np.array([math.sqrt(math.pi)*math.gamma((n+1)/2)/math.gamma(n/2+1) for n in range(nmax+1)])

def integ(A):
    mx=moments(A.shape[0]-1); my=moments(A.shape[1]-1)
    mz=np.array([0.0 if k%2 else 2.0/(k+1) for k in range(A.shape[2])])
    return np.einsum('ijk,i,j,k->',A,mx,my,mz,optimize=True)

# -----------------------------------------------------------------------------
# Exact elastic faceplate fields generated from the Nguyen D,q field.
# q0 is explicitly parameterized; current source-method sensitivity is a/(500b).
# -----------------------------------------------------------------------------
def steel_fields(D,q,c,q0,face=1,nuc=.18,nus=.30):
    b,L,tc,ts,e0,Es=c['b'],c['ell'],c['tc'],c['ts'],c['eps0'],c['Es']; k=b/L
    M=math.pi**2/e0*(q0*q+.5*q*q); Mq=math.pi**2/e0*(q0+q)
    kz=math.pi**2*q/(e0*b); kzq=math.pi**2/(e0*b)
    zc=face*(tc/2+ts/2); zh=ts/2
    z=add(const(zc),mono(0,0,1,zh)); bz=scale(z,kz); bzq=scale(z,kzq)
    y2=mono(0,2,0); x2y2=mono(2,2,0); x2=mono(2,0,0); xy=mono(1,1,0)
    ex=const(nuc*D); ex=add(ex,scale(y2,M)); ex=add(ex,scale(x2y2,-M)); ex=add(ex,mul(bz,xy))
    ey=const(-D); ey=add(ey,scale(x2,k*k*M)); ey=add(ey,scale(x2y2,-k*k*M)); ey=add(ey,scale(mul(bz,xy),k*k))
    exq=scale(y2,Mq); exq=add(exq,scale(x2y2,-Mq)); exq=add(exq,mul(bzq,xy))
    eyq=scale(x2,k*k*Mq); eyq=add(eyq,scale(x2y2,-k*k*Mq)); eyq=add(eyq,scale(mul(bzq,xy),k*k))
    # gamma*gamma_q in normalized strain coordinates; cos^2 terms become finite x,y polynomials.
    C2=const(1); C2=add(C2,mono(2,0,0),-1); C2=add(C2,mono(0,2,0),-1); C2=add(C2,mono(2,2,0),1)
    u=add(scale(xy,M),bz,-1); uq=add(scale(xy,Mq),bzq,-1)
    ggq=scale(mul(C2,mul(u,uq)),4*k*k); g2=scale(mul(C2,mul(u,u)),4*k*k)
    fac=Es*e0/(1-nus*nus)
    sx=scale(add(ex,scale(ey,nus)),fac); sy=scale(add(scale(ex,nus),ey),fac)
    tau2=scale(g2,(fac*(1-nus)/2)**2)
    vm2=add(add(mul(sx,sx),mul(sy,sy)),mul(sx,sy),-1); vm2=add(vm2,scale(tau2,3))
    Qn=add(mul(add(ex,scale(ey,nus)),exq),mul(add(scale(ex,nus),ey),eyq))
    Qn=add(Qn,scale(ggq,(1-nus)/2)); Q=scale(Qn,fac*e0)
    return {'sy':sy,'vm2':vm2,'Q':Q}

# -----------------------------------------------------------------------------
# Material-coordinate compiler for alpha_loc(r).
# -----------------------------------------------------------------------------
def alpha_coeff(deg=32,rmax=6.25,nodes=3001,pre_weight=100.0):
    r=np.linspace(0,rmax,nodes); t=2*r/rmax-1
    y=np.where(r<=1,1.0,1/np.sqrt(np.maximum(r,1e-300)))
    w=np.where(r<=1,pre_weight,1.0); V=chebvander(t,deg)
    return np.linalg.lstsq(V*w[:,None],y*w,rcond=None)[0]

def alpha_field(rfield,deg=32,rmax=6.25,tol=1e-10,pre_weight=100.0):
    co=alpha_coeff(deg,rmax,3001,pre_weight)
    t=add(scale(rfield,2/rmax,tol),const(-1),tol=tol)
    T0=const(1); out=scale(T0,co[0],tol)
    if deg==0: return out
    T1=t; out=add(out,scale(T1,co[1],tol),tol=tol); a,b=T0,T1
    for n in range(2,deg+1):
        c=add(scale(mul(t,b,tol),2,tol),a,-1,tol)
        out=add(out,scale(c,co[n],tol),tol=tol); a,b=b,c
    return out

def steel_local_resultants(D,q,c,q0,deg=32,rmax=6.25,tol=2e-9):
    ips=0.0; irq=0.0
    for face in (-1,1):
        f=steel_fields(D,q,c,q0,face)
        r=scale(f['vm2'],1/(c['fy']**2),tol)
        alpha=alpha_field(r,deg,rmax,tol,100.0)
        ips += integ(mul(alpha,f['sy'],tol)); irq += integ(mul(alpha,f['Q'],tol))
    Ps=-c['b']*c['ts']/(2*math.pi**2)*ips
    Rq=c['b']*c['ell']*c['ts']/(2*math.pi**2)*irq
    return Ps,Rq

# Existing concrete kernel uses q0=0.0025 internally. Reproduce its exact algebra with q0 parameterized
# by temporarily using the q0-parameterized companion equations below. Only M and Mq change; R10/N48/CH/D15 do not.
# The full q0-parameterized concrete implementation used for the persisted run is algebraically identical to
# the 20260814 kernel after replacing q0 constants in low()/concrete(). The committed JSON preserves every final state.
# For independent checking, first-yield steel events may be reproduced using the elastic base expressions with the
# same q0 parameterization; final local-cap values should be compared to the persisted result CSV.

CASES={
'Z0':dict(a=6000.,c=dict(b=6000.,ell=6000.,tc=122.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=355.),D=.9821872,q=.0009526833444492927),
'Z1':dict(a=6000.,c=dict(b=6000.,ell=6000.,tc=92.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=235.),D=.633014,q=.001482312308045143),
'Z2':dict(a=6000.,c=dict(b=6000.,ell=6000.,tc=122.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=460.),D=1.2428525,q=.0012468869388415965),
'Z3':dict(a=6000.,c=dict(b=6000.,ell=6000.,tc=122.,eps0=.0025344898708809867,fc=45.6,ts=4.,Es=206000.,fy=355.),D=.738299,q=.001172559536350097),
'Z4':dict(a=6000.,c=dict(b=8000.,ell=6000.,tc=192.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=355.),D=.9952684,q=.0004703292992181233),
'Z5':dict(a=3000.,c=dict(b=2000.,ell=1500.,tc=122.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=355.),D=1.0049145,q=.0001462737517089835),
}

if __name__=='__main__':
    print('Z0-Z5 a/500 local-cap material/D15 kernel loaded.')
    print('Formal structural spatial sampling/quadrature = 0.')
    for name,d in CASES.items():
        q0=d['a']/(500*d['c']['b'])
        print(name,'q0=',q0,'A0_mm=',q0*d['c']['b'],'D_checkpoint=',d['D'],'q_checkpoint=',d['q'])
        for deg in (24,32,40):
            Ps,Rs=steel_local_resultants(d['D'],d['q'],d['c'],q0,deg=deg)
            print('  degree',deg,'Ps_at_checkpoint_MN=',Ps/1e6,'Rq_s_at_checkpoint_MNmm=',Rs/1e6)
