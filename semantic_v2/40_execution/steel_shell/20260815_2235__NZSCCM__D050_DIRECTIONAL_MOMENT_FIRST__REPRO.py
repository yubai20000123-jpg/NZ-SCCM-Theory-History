"""NZ-SCCM D=.50 augmented FvK directional moment-first evaluator.

Formal identity:
- one complete out-of-plane halfwave
- Nguyen second order
- frozen R10/N48/Cayley-Hamilton concrete map
- frozen local steel radial-cap map
- General D15 exact moments
- no formal structural spatial sampling/quadrature

This V1 keeps the inherited dense buildS(K1,K2) material pair but avoids
materializing Sxx/Syy and avoids a full stress*virtual-strain 3D field for every
residual.  It contracts the Cayley-Hamilton pair directly into exact moments.
"""
from pathlib import Path
import importlib.util, math, numpy as np
HERE=Path(__file__).resolve().parent

def load(name,path):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

base=load('base',HERE/'20260814_2240__NZSCCM_Z0_Z6__REDUCED_IDEALEP_D15__REPRO.py')
loc=load('loc',HERE/'20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP_D15__REPRO.py')
bw=load('bw',HERE/'20260815_1844__NZSCCM__Z6__BOUNDARY_WARP_D050_CURRENT_OPERATOR__REPRO.py')

CASE=dict(b=12000.,ell=9000.,tc=122.,eps0=.0018712490394580678,fc=30.4,
          ts=4.,Es=206000.,fy=355.,nuc=.18,nus=.3,q0=.0015)
CERT=dict(D=.5,q=.008003063422252722,cw=-.07766034129851779,
          p20=-.06065823792663306,p02=.16525678113314005)

# -----------------------------------------------------------------------------
# Exact Chebyshev-product moment contraction.
# base.integ uses mu_xy(n)=int_0^pi T_n(sin X)dX and
# mu_z(n)=int_-1^1 T_n(eta)deta.  Use T_m*T_n product identity directly.
# -----------------------------------------------------------------------------
def muxy(n):
    return math.pi if n==0 else 2*math.sin(n*math.pi/2)/n

def muz(n):
    return 0.0 if n%2 else 2.0/(1-n*n)

def pmom(i,j,axis):
    mu=muxy if axis=='xy' else muz
    return .5*(mu(i+j)+mu(abs(i-j)))

def inner_cheb(A,W):
    """Exact integral of A*W without materializing the full product field.
    Intended for high-order A and low-order W.
    """
    total=0.0
    for p,q,r in np.argwhere(np.abs(W)>0):
        w=W[p,q,r]
        mx=np.array([pmom(i,int(p),'xy') for i in range(A.shape[0])])
        my=np.array([pmom(j,int(q),'xy') for j in range(A.shape[1])])
        mz=np.array([pmom(k,int(r),'z') for k in range(A.shape[2])])
        total += w*np.einsum('ijk,i,j,k->',A,mx,my,mz,optimize=True)
    return total

def dirs(c=CASE):
    k=c['b']/c['ell']
    exc,eyc=bw.warp_dict(c)
    ex20=base.padd(base.mon(0,2,0),base.mon(2,2,0,-2))
    ey20=base.ps(base.pmul(base.padd(base.pc(1),base.mon(2,0,0,-2)),
                          base.padd(base.pc(1),base.mon(0,2,0,-2))),.5*k*k)
    ex02={}
    ey02=base.padd(base.pc(1),base.mon(0,2,0,-2))
    return exc,eyc,ex20,ey20,ex02,ey02

# -----------------------------------------------------------------------------
# Concrete directional evaluator.
# -----------------------------------------------------------------------------
def concrete_mf(D,q,cw,p20,p02,c=CASE,tol=7e-7):
    nu=c['nuc']; b,L,t,e0=c['b'],c['ell'],c['tc'],c['eps0']; k=b/L; q0=c['q0']
    M=math.pi**2/e0*(q0*q+.5*q*q); B=math.pi**2*t/(2*e0*b)*q
    Mq=math.pi**2/e0*(q0+q); Bq=math.pi**2*t/(2*e0*b)

    ex=base.ps(base.mon(0,2,0),M); ex=base.padd(ex,base.ps(base.mon(2,2,0),-M)); ex=base.padd(ex,base.ps(base.mon(1,1,1),B))
    ey=base.pc(-D); ey=base.padd(ey,base.ps(base.mon(2,0,0),k*k*M)); ey=base.padd(ey,base.ps(base.mon(2,2,0),-k*k*M)); ey=base.padd(ey,base.ps(base.mon(1,1,1),k*k*B))
    exc,eyc,ex20,ey20,ex02,ey02=dirs(c)
    ex=base.padd(ex,base.ps(exc,cw)); ey=base.padd(ey,base.ps(eyc,cw))
    ex=base.padd(ex,base.ps(ex20,p20)); ey=base.padd(ey,base.ps(ey20,p20)); ey=base.padd(ey,base.ps(ey02,p02))

    exq=base.ps(base.mon(0,2,0),Mq); exq=base.padd(exq,base.ps(base.mon(2,2,0),-Mq)); exq=base.padd(exq,base.ps(base.mon(1,1,1),Bq))
    eyq=base.ps(base.mon(2,0,0),k*k*Mq); eyq=base.padd(eyq,base.ps(base.mon(2,2,0),-k*k*Mq)); eyq=base.padd(eyq,base.ps(base.mon(1,1,1),k*k*Bq))

    C2=base.pc(1); C2=base.padd(C2,base.mon(2,0,0,-1)); C2=base.padd(C2,base.mon(0,2,0,-1)); C2=base.padd(C2,base.mon(2,2,0,1))
    uu=base.padd(base.ps(base.mon(1,1,0),M),base.mon(0,0,1,-B))
    uuq=base.padd(base.ps(base.mon(1,1,0),Mq),base.mon(0,0,1,-Bq))
    g2=base.ps(base.pmul(C2,base.pmul(uu,uu)),4*k*k)
    ggq=base.ps(base.pmul(C2,base.pmul(uu,uuq)),4*k*k)

    den=1-nu*nu
    Exx=base.ps(base.padd(ex,base.ps(ey,nu)),1/den)
    Eyy=base.ps(base.padd(base.ps(ex,nu),ey),1/den)
    I1=base.padd(Exx,Eyy)
    I2=base.padd(base.pmul(Exx,Eyy),base.ps(g2,-1/(4*(1+nu)**2)))
    K1=base.p2c(base.ps(base.padd(I1,base.pc(-2*base.lc)),1/base.lh))
    K2=base.p2c(base.ps(base.padd(base.padd(I2,base.ps(I1,-base.lc)),base.pc(base.lc*base.lc)),1/base.lh**2))

    A,Bb=bw.buildS(K1,K2,tol)
    Yxx=base.p2c(base.ps(base.padd(Exx,base.pc(-base.lc)),1/base.lh))
    Yyy=base.p2c(base.ps(base.padd(Eyy,base.pc(-base.lc)),1/base.lh))

    Pc=-c['fc']*b*t/(2*math.pi**2)*(base.integ(A)+inner_cheb(Bb,Yyy))

    def R(dx,dy,dgg=None):
        dx=base.p2c(dx); dy=base.p2c(dy)
        v=inner_cheb(A,base.add(dx,dy,1,1e-15))
        W=base.add(base.mul(Yxx,dx,1e-15),base.mul(Yyy,dy,1e-15),1,1e-15)
        v+=inner_cheb(Bb,W)
        if dgg is not None:
            v+=inner_cheb(Bb,base.p2c(dgg))/(2*(1+nu)*base.lh)
        return c['fc']*e0*b*L*t/(2*math.pi**2)*v

    return Pc,R(exq,eyq,ggq),R(exc,eyc),R(ex20,ey20),R(ex02,ey02)

# -----------------------------------------------------------------------------
# Steel: same local radial-cap algebra as 18:44/21:53, with p20/p02 added to
# ex/ey and the same exact monomial moments.
# -----------------------------------------------------------------------------
def d2p(p):
    if not p:return np.zeros((1,1,1))
    mx=[0,0,0]
    for key in p:
        for d in range(3):mx[d]=max(mx[d],key[d])
    A=np.zeros(tuple(v+1 for v in mx))
    for key,v in p.items():A[key]=v
    return A

def steel_aug(D,q,cw,p20,p02,c=CASE,deg=24,tol=1e-9):
    b,L,tc,ts,e0,Es,nus=c['b'],c['ell'],c['tc'],c['ts'],c['eps0'],c['Es'],c['nus']; k=b/L; q0=c['q0']
    M=math.pi**2/e0*(q0*q+.5*q*q); Mq=math.pi**2/e0*(q0+q)
    kb=math.pi**2*q/(e0*b); kbq=math.pi**2/(e0*b)
    exc,eyc,ex20,ey20,ex02,ey02=map(d2p,dirs(c))
    P=Rq=Rc=R20=R02=0.0
    for face in (-1,1):
        z=loc.add(loc.const(face*(tc/2+ts/2)),loc.mono(0,0,1,ts/2))
        bz=loc.scale(z,kb); bzq=loc.scale(z,kbq)
        ex=loc.scale(loc.mono(0,2,0),M); ex=loc.add(ex,loc.scale(loc.mono(2,2,0),-M)); ex=loc.add(ex,loc.mul(bz,loc.mono(1,1,0))); ex=loc.add(ex,loc.scale(exc,cw)); ex=loc.add(ex,loc.scale(ex20,p20))
        ey=loc.const(-D); ey=loc.add(ey,loc.scale(loc.mono(2,0,0),k*k*M)); ey=loc.add(ey,loc.scale(loc.mono(2,2,0),-k*k*M)); ey=loc.add(ey,loc.scale(loc.mul(bz,loc.mono(1,1,0)),k*k)); ey=loc.add(ey,loc.scale(eyc,cw)); ey=loc.add(ey,loc.scale(ey20,p20)); ey=loc.add(ey,loc.scale(ey02,p02))
        exq=loc.scale(loc.mono(0,2,0),Mq); exq=loc.add(exq,loc.scale(loc.mono(2,2,0),-Mq)); exq=loc.add(exq,loc.mul(bzq,loc.mono(1,1,0)))
        eyq=loc.scale(loc.mono(2,0,0),k*k*Mq); eyq=loc.add(eyq,loc.scale(loc.mono(2,2,0),-k*k*Mq)); eyq=loc.add(eyq,loc.scale(loc.mul(bzq,loc.mono(1,1,0)),k*k))
        C2=loc.const(1); C2=loc.add(C2,loc.mono(2,0,0),-1); C2=loc.add(C2,loc.mono(0,2,0),-1); C2=loc.add(C2,loc.mono(2,2,0),1)
        u=loc.add(loc.scale(loc.mono(1,1,0),M),bz,-1); uq=loc.add(loc.scale(loc.mono(1,1,0),Mq),bzq,-1)
        g2=loc.scale(loc.mul(C2,loc.mul(u,u)),4*k*k); ggq=loc.scale(loc.mul(C2,loc.mul(u,uq)),4*k*k)
        fac=Es*e0/(1-nus*nus)
        sx=loc.scale(loc.add(ex,loc.scale(ey,nus)),fac); sy=loc.scale(loc.add(loc.scale(ex,nus),ey),fac)
        tau2=loc.scale(g2,(fac*(1-nus)/2)**2)
        vm2=loc.add(loc.add(loc.mul(sx,sx),loc.mul(sy,sy)),loc.mul(sx,sy),-1); vm2=loc.add(vm2,loc.scale(tau2,3))
        alpha=loc.alpha_field(loc.scale(vm2,1/c['fy']**2,tol),deg,8.,tol,100.)
        P+=loc.integ(loc.mul(alpha,sy,tol))
        def Q(dx,dy,dgg=None):
            z=loc.add(loc.mul(loc.add(ex,loc.scale(ey,nus)),dx),loc.mul(loc.add(loc.scale(ex,nus),ey),dy))
            if dgg is not None:z=loc.add(z,loc.scale(dgg,(1-nus)/2))
            return loc.integ(loc.mul(alpha,loc.scale(z,fac*e0),tol))
        Rq+=Q(exq,eyq,ggq); Rc+=Q(exc,eyc); R20+=Q(ex20,ey20); R02+=Q(ex02,ey02)
    fp=-b*ts/(2*math.pi**2); fr=b*L*ts/(2*math.pi**2)
    return fp*P,fr*Rq,fr*Rc,fr*R20,fr*R02

def total(state=CERT,ctol=7e-7):
    c=concrete_mf(state['D'],state['q'],state['cw'],state['p20'],state['p02'],tol=ctol)
    s=steel_aug(state['D'],state['q'],state['cw'],state['p20'],state['p02'])
    return tuple(c[i]+s[i] for i in range(5)),c,s

if __name__=='__main__':
    base.set_compiler(-1.75,.45,601)
    tot,cc,ss=total()
    print('state=',CERT)
    print('total [P,Rq,Rc,R20,R02] =',[x/1e6 for x in tot])
    print('concrete=',[x/1e6 for x in cc])
    print('steel=',[x/1e6 for x in ss])
    print('formal spatial sampling/quadrature = 0; Pu not solved')
