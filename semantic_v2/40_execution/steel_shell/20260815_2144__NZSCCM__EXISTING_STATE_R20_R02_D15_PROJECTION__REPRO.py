"""NZ-SCCM existing-state FvK membrane residual projection gate.

No new Pu, no new root, no spatial quadrature.
Imports the already accepted Z6 boundary-warp current-operator kernel and adds
only two admissible virtual-strain directions p20 and p02.
"""
from pathlib import Path
import importlib.util, math

HERE=Path(__file__).resolve().parent

def load(name,path):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

bw=load('bw',HERE/'20260815_1844__NZSCCM__Z6__BOUNDARY_WARP_D050_CURRENT_OPERATOR__REPRO.py')
base,loc=bw.base,bw.loc

def projection_dicts(c):
    k=c['b']/c['ell']
    # p20: ex = cos2X sin^2Y; ey=(k^2/2)cos2X cos2Y; gamma=0
    ex20=base.padd(base.mon(0,2,0),base.mon(2,2,0,-2))
    ey20=base.ps(base.pmul(
        base.padd(base.pc(1),base.mon(2,0,0,-2)),
        base.padd(base.pc(1),base.mon(0,2,0,-2))),0.5*k*k)
    # p02: ex=0; ey=cos2Y; gamma=0
    ex02={}
    ey02=base.padd(base.pc(1),base.mon(0,2,0,-2))
    return ex20,ey20,ex02,ey02

def concrete_projection(D,q,cw,c,tol=7e-7):
    nu=c['nuc']; b,L,t,e0=c['b'],c['ell'],c['tc'],c['eps0']; k=b/L; q0=c['q0']
    M=math.pi**2/e0*(q0*q+.5*q*q); B=math.pi**2*t/(2*e0*b)*q
    Mq=math.pi**2/e0*(q0+q); Bq=math.pi**2*t/(2*e0*b)
    ex=base.ps(base.mon(0,2,0),M); ex=base.padd(ex,base.ps(base.mon(2,2,0),-M)); ex=base.padd(ex,base.ps(base.mon(1,1,1),B))
    ey=base.pc(-D); ey=base.padd(ey,base.ps(base.mon(2,0,0),k*k*M)); ey=base.padd(ey,base.ps(base.mon(2,2,0),-k*k*M)); ey=base.padd(ey,base.ps(base.mon(1,1,1),k*k*B))
    exc,eyc=bw.warp_dict(c); ex=base.padd(ex,base.ps(exc,cw)); ey=base.padd(ey,base.ps(eyc,cw))
    exq=base.ps(base.mon(0,2,0),Mq); exq=base.padd(exq,base.ps(base.mon(2,2,0),-Mq)); exq=base.padd(exq,base.ps(base.mon(1,1,1),Bq))
    eyq=base.ps(base.mon(2,0,0),k*k*Mq); eyq=base.padd(eyq,base.ps(base.mon(2,2,0),-k*k*Mq)); eyq=base.padd(eyq,base.ps(base.mon(1,1,1),k*k*Bq))
    C2=base.pc(1); C2=base.padd(C2,base.mon(2,0,0,-1)); C2=base.padd(C2,base.mon(0,2,0,-1)); C2=base.padd(C2,base.mon(2,2,0,1))
    uu=base.padd(base.ps(base.mon(1,1,0),M),base.mon(0,0,1,-B)); uuq=base.padd(base.ps(base.mon(1,1,0),Mq),base.mon(0,0,1,-Bq))
    g2=base.ps(base.pmul(C2,base.pmul(uu,uu)),4*k*k); ggq=base.ps(base.pmul(C2,base.pmul(uu,uuq)),4*k*k)
    den=1-nu*nu; Exx=base.ps(base.padd(ex,base.ps(ey,nu)),1/den); Eyy=base.ps(base.padd(base.ps(ex,nu),ey),1/den)
    I1=base.padd(Exx,Eyy); I2=base.padd(base.pmul(Exx,Eyy),base.ps(g2,-1/(4*(1+nu)**2)))
    K1=base.p2c(base.ps(base.padd(I1,base.pc(-2*base.lc)),1/base.lh)); K2=base.p2c(base.ps(base.padd(base.padd(I2,base.ps(I1,-base.lc)),base.pc(base.lc*base.lc)),1/base.lh**2))
    A,B=bw.buildS(K1,K2,tol); Yxx=base.p2c(base.ps(base.padd(Exx,base.pc(-base.lc)),1/base.lh)); Yyy=base.p2c(base.ps(base.padd(Eyy,base.pc(-base.lc)),1/base.lh))
    Sxx=base.add(A,base.mul(B,Yxx,tol),1,tol); Syy=base.add(A,base.mul(B,Yyy,tol),1,tol)
    Pc=-c['fc']*b*t/(2*math.pi**2)*base.integ(Syy)
    def R(exd,eyd,ggd=None):
        Q=base.add(base.mul(Sxx,base.p2c(exd),tol),base.mul(Syy,base.p2c(eyd),tol),1,tol)
        if ggd:
            Q=base.add(Q,base.scale(base.mul(B,base.p2c(ggd),tol),1/(2*(1+nu)*base.lh),tol),1,tol)
        return c['fc']*e0*b*L*t/(2*math.pi**2)*base.integ(Q)
    ex20,ey20,ex02,ey02=projection_dicts(c)
    return dict(Pc=Pc,Rq=R(exq,eyq,ggq),Rc=R(exc,eyc),R20=R(ex20,ey20),R02=R(ex02,ey02))

def steel_projection(D,q,cw,c,deg=24,tol=1e-9):
    b,L,tc,ts,e0,Es,nus=c['b'],c['ell'],c['tc'],c['ts'],c['eps0'],c['Es'],c['nus']; k=b/L; q0=c['q0']
    M=math.pi**2/e0*(q0*q+.5*q*q); Mq=math.pi**2/e0*(q0+q); kb=math.pi**2*q/(e0*b); kbq=math.pi**2/(e0*b)
    exc,eyc=map(bw.d2p,bw.warp_dict(c)); ex20,ey20,ex02,ey02=map(bw.d2p,projection_dicts(c))
    P=Rq=Rc=R20=R02=0.0
    for face in (-1,1):
        z=loc.add(loc.const(face*(tc/2+ts/2)),loc.mono(0,0,1,ts/2)); bz=loc.scale(z,kb); bzq=loc.scale(z,kbq)
        ex=loc.scale(loc.mono(0,2,0),M); ex=loc.add(ex,loc.scale(loc.mono(2,2,0),-M)); ex=loc.add(ex,loc.mul(bz,loc.mono(1,1,0))); ex=loc.add(ex,loc.scale(exc,cw))
        ey=loc.const(-D); ey=loc.add(ey,loc.scale(loc.mono(2,0,0),k*k*M)); ey=loc.add(ey,loc.scale(loc.mono(2,2,0),-k*k*M)); ey=loc.add(ey,loc.scale(loc.mul(bz,loc.mono(1,1,0)),k*k)); ey=loc.add(ey,loc.scale(eyc,cw))
        exq=loc.scale(loc.mono(0,2,0),Mq); exq=loc.add(exq,loc.scale(loc.mono(2,2,0),-Mq)); exq=loc.add(exq,loc.mul(bzq,loc.mono(1,1,0)))
        eyq=loc.scale(loc.mono(2,0,0),k*k*Mq); eyq=loc.add(eyq,loc.scale(loc.mono(2,2,0),-k*k*Mq)); eyq=loc.add(eyq,loc.scale(loc.mul(bzq,loc.mono(1,1,0)),k*k))
        C2=loc.const(1); C2=loc.add(C2,loc.mono(2,0,0),-1); C2=loc.add(C2,loc.mono(0,2,0),-1); C2=loc.add(C2,loc.mono(2,2,0),1)
        u=loc.add(loc.scale(loc.mono(1,1,0),M),bz,-1); uq=loc.add(loc.scale(loc.mono(1,1,0),Mq),bzq,-1); g2=loc.scale(loc.mul(C2,loc.mul(u,u)),4*k*k); ggq=loc.scale(loc.mul(C2,loc.mul(u,uq)),4*k*k)
        fac=Es*e0/(1-nus*nus); sx=loc.scale(loc.add(ex,loc.scale(ey,nus)),fac); sy=loc.scale(loc.add(loc.scale(ex,nus),ey),fac); tau2=loc.scale(g2,(fac*(1-nus)/2)**2)
        vm2=loc.add(loc.add(loc.mul(sx,sx),loc.mul(sy,sy)),loc.mul(sx,sy),-1); vm2=loc.add(vm2,loc.scale(tau2,3)); alpha=loc.alpha_field(loc.scale(vm2,1/c['fy']**2,tol),deg,8.0,tol,100.0)
        P += loc.integ(loc.mul(alpha,sy,tol))
        def Qdir(exd,eyd,ggd=None):
            Q=loc.add(loc.mul(loc.add(ex,loc.scale(ey,nus)),exd),loc.mul(loc.add(loc.scale(ex,nus),ey),eyd))
            if ggd is not None: Q=loc.add(Q,loc.scale(ggd,(1-nus)/2))
            return loc.integ(loc.mul(alpha,loc.scale(Q,fac*e0),tol))
        Rq+=Qdir(exq,eyq,ggq); Rc+=Qdir(exc,eyc); R20+=Qdir(ex20,ey20); R02+=Qdir(ex02,ey02)
    pref=b*L*ts/(2*math.pi**2)
    return dict(Ps=-b*ts/(2*math.pi**2)*P,Rq=pref*Rq,Rc=pref*Rc,R20=pref*R20,R02=pref*R02)

def evaluate(D,q,cw,c):
    cc=concrete_projection(D,q,cw,c); ss=steel_projection(D,q,cw,c)
    P=cc['Pc']+ss['Ps']
    out=dict(D=D,q=q,c=cw,P=P,Pc=cc['Pc'],Ps=ss['Ps'])
    for key in ('Rq','Rc','R20','R02'): out[key]=cc[key]+ss[key]
    out.update(R20c=cc['R20'],R20s=ss['R20'],R02c=cc['R02'],R02s=ss['R02'])
    out['eta20_Pell']=abs(out['R20'])/(P*c['ell']); out['eta02_Pell']=abs(out['R02'])/(P*c['ell'])
    return out

if __name__=='__main__':
    base.set_compiler(-1.75,0.45,601)
    c=dict(b=12000.,ell=9000.,tc=122.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=355.,nuc=.18,nus=.3,q0=.0015)
    states=[(.50,.007244278905,-.0154563484942),(.55,.008198205,-.02004071),(.60,.009177472,-.02655088)]
    for state in states:
        r=evaluate(*state,c)
        print({k:(v/1e6 if k in ('P','Pc','Ps','Rq','Rc','R20','R02','R20c','R20s','R02c','R02s') else v) for k,v in r.items()})
