"""NZ-SCCM Z6 boundary-admissible N=1 current-map checkpoint.
Imports frozen R10/N48/D15 and local-cap algebra already committed in this repo.
No structural spatial sampling/quadrature.
"""
from pathlib import Path
import importlib.util, math, numpy as np
HERE=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
base=load('base',HERE/'20260814_2240__NZSCCM_Z0_Z6__REDUCED_IDEALEP_D15__REPRO.py')
loc=load('loc',HERE/'20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP_D15__REPRO.py')

def warp_dict(c):
 k=c['b']/c['ell'];exc=base.ps(base.mon(1,2,0),4/math.pi)
 eyc=base.ps(base.pmul(base.mon(1,0,0),base.padd(base.pc(1),base.mon(0,2,0,-2))),8*k*k/math.pi)
 return exc,eyc

def buildS(K1,K2,tol):
 U=base.recur(K1,K2,base.Ucoef,tol);C=base.recur(K1,K2,base.Ccoef,tol);T=base.recur(K1,K2,base.Tcoef,tol);T7=base.recur(K1,K2,base.T7coef,tol)
 CC=base.sm(base.det(C,K1,K2,tol),C,tol);TC=base.pa(base.sm(base.tr(T,K1,tol),C,tol),base.pm(C,T,K1,K2,tol),-1,tol)
 t7=base.tr(T7,K1,tol);inner=(base.add(t7,T7[0],-1,tol),base.scale(T7[1],-1,tol));TT=base.sm(base.det(T,K1,K2,tol),inner,tol)
 return base.pa(base.pa(base.pa(U,CC,-base.acc,tol),TC,1,tol),TT,-base.rho*base.at,tol)

def concrete(D,q,cw,c,tol=7e-7):
 nu=c['nuc'];b,L,t,e0=c['b'],c['ell'],c['tc'],c['eps0'];k=b/L;q0=c['q0']
 M=math.pi**2/e0*(q0*q+.5*q*q);B=math.pi**2*t/(2*e0*b)*q;Mq=math.pi**2/e0*(q0+q);Bq=math.pi**2*t/(2*e0*b)
 ex=base.ps(base.mon(0,2,0),M);ex=base.padd(ex,base.ps(base.mon(2,2,0),-M));ex=base.padd(ex,base.ps(base.mon(1,1,1),B))
 ey=base.pc(-D);ey=base.padd(ey,base.ps(base.mon(2,0,0),k*k*M));ey=base.padd(ey,base.ps(base.mon(2,2,0),-k*k*M));ey=base.padd(ey,base.ps(base.mon(1,1,1),k*k*B))
 exc,eyc=warp_dict(c);ex=base.padd(ex,base.ps(exc,cw));ey=base.padd(ey,base.ps(eyc,cw))
 exq=base.ps(base.mon(0,2,0),Mq);exq=base.padd(exq,base.ps(base.mon(2,2,0),-Mq));exq=base.padd(exq,base.ps(base.mon(1,1,1),Bq))
 eyq=base.ps(base.mon(2,0,0),k*k*Mq);eyq=base.padd(eyq,base.ps(base.mon(2,2,0),-k*k*Mq));eyq=base.padd(eyq,base.ps(base.mon(1,1,1),k*k*Bq))
 C2=base.pc(1);C2=base.padd(C2,base.mon(2,0,0,-1));C2=base.padd(C2,base.mon(0,2,0,-1));C2=base.padd(C2,base.mon(2,2,0,1))
 uu=base.padd(base.ps(base.mon(1,1,0),M),base.mon(0,0,1,-B));uuq=base.padd(base.ps(base.mon(1,1,0),Mq),base.mon(0,0,1,-Bq))
 g2=base.ps(base.pmul(C2,base.pmul(uu,uu)),4*k*k);ggq=base.ps(base.pmul(C2,base.pmul(uu,uuq)),4*k*k)
 den=1-nu*nu;Exx=base.ps(base.padd(ex,base.ps(ey,nu)),1/den);Eyy=base.ps(base.padd(base.ps(ex,nu),ey),1/den)
 I1=base.padd(Exx,Eyy);I2=base.padd(base.pmul(Exx,Eyy),base.ps(g2,-1/(4*(1+nu)**2)))
 K1=base.p2c(base.ps(base.padd(I1,base.pc(-2*base.lc)),1/base.lh));K2=base.p2c(base.ps(base.padd(base.padd(I2,base.ps(I1,-base.lc)),base.pc(base.lc*base.lc)),1/base.lh**2))
 A,Bb=buildS(K1,K2,tol);Yxx=base.p2c(base.ps(base.padd(Exx,base.pc(-base.lc)),1/base.lh));Yyy=base.p2c(base.ps(base.padd(Eyy,base.pc(-base.lc)),1/base.lh))
 Sxx=base.add(A,base.mul(Bb,Yxx,tol),1,tol);Syy=base.add(A,base.mul(Bb,Yyy,tol),1,tol)
 Pc=-c['fc']*b*t/(2*math.pi**2)*base.integ(Syy)
 def R(exd,eyd,ggd=None):
  Q=base.add(base.mul(Sxx,base.p2c(exd),tol),base.mul(Syy,base.p2c(eyd),tol),1,tol)
  if ggd:Q=base.add(Q,base.scale(base.mul(Bb,base.p2c(ggd),tol),1/(2*(1+nu)*base.lh),tol),1,tol)
  return c['fc']*e0*b*L*t/(2*math.pi**2)*base.integ(Q)
 return Pc,R(exq,eyq,ggq),R(exc,eyc)

def d2p(p):
 mx=[0,0,0]
 for k in p:
  for d in range(3):mx[d]=max(mx[d],k[d])
 A=np.zeros(tuple(v+1 for v in mx))
 for k,v in p.items():A[k]=v
 return A

def steel(D,q,cw,c,deg=24,tol=1e-9):
 b,L,tc,ts,e0,Es,nus=c['b'],c['ell'],c['tc'],c['ts'],c['eps0'],c['Es'],c['nus'];k=b/L;q0=c['q0']
 M=math.pi**2/e0*(q0*q+.5*q*q);Mq=math.pi**2/e0*(q0+q);kb=math.pi**2*q/(e0*b);kbq=math.pi**2/(e0*b);exc,eyc=map(d2p,warp_dict(c));P=Rq=Rc=0.
 for face in (-1,1):
  z=loc.add(loc.const(face*(tc/2+ts/2)),loc.mono(0,0,1,ts/2));bz=loc.scale(z,kb);bzq=loc.scale(z,kbq)
  ex=loc.scale(loc.mono(0,2,0),M);ex=loc.add(ex,loc.scale(loc.mono(2,2,0),-M));ex=loc.add(ex,loc.mul(bz,loc.mono(1,1,0)));ex=loc.add(ex,loc.scale(exc,cw))
  ey=loc.const(-D);ey=loc.add(ey,loc.scale(loc.mono(2,0,0),k*k*M));ey=loc.add(ey,loc.scale(loc.mono(2,2,0),-k*k*M));ey=loc.add(ey,loc.scale(loc.mul(bz,loc.mono(1,1,0)),k*k));ey=loc.add(ey,loc.scale(eyc,cw))
  exq=loc.scale(loc.mono(0,2,0),Mq);exq=loc.add(exq,loc.scale(loc.mono(2,2,0),-Mq));exq=loc.add(exq,loc.mul(bzq,loc.mono(1,1,0)))
  eyq=loc.scale(loc.mono(2,0,0),k*k*Mq);eyq=loc.add(eyq,loc.scale(loc.mono(2,2,0),-k*k*Mq));eyq=loc.add(eyq,loc.scale(loc.mul(bzq,loc.mono(1,1,0)),k*k))
  C2=loc.const(1);C2=loc.add(C2,loc.mono(2,0,0),-1);C2=loc.add(C2,loc.mono(0,2,0),-1);C2=loc.add(C2,loc.mono(2,2,0),1)
  u=loc.add(loc.scale(loc.mono(1,1,0),M),bz,-1);uq=loc.add(loc.scale(loc.mono(1,1,0),Mq),bzq,-1);g2=loc.scale(loc.mul(C2,loc.mul(u,u)),4*k*k);ggq=loc.scale(loc.mul(C2,loc.mul(u,uq)),4*k*k)
  fac=Es*e0/(1-nus*nus);sx=loc.scale(loc.add(ex,loc.scale(ey,nus)),fac);sy=loc.scale(loc.add(loc.scale(ex,nus),ey),fac);tau2=loc.scale(g2,(fac*(1-nus)/2)**2)
  vm2=loc.add(loc.add(loc.mul(sx,sx),loc.mul(sy,sy)),loc.mul(sx,sy),-1);vm2=loc.add(vm2,loc.scale(tau2,3));alpha=loc.alpha_field(loc.scale(vm2,1/c['fy']**2,tol),deg,8.,tol,100.)
  P+=loc.integ(loc.mul(alpha,sy,tol));Qq=loc.add(loc.mul(loc.add(ex,loc.scale(ey,nus)),exq),loc.mul(loc.add(loc.scale(ex,nus),ey),eyq));Qq=loc.add(Qq,loc.scale(ggq,(1-nus)/2));Rq+=loc.integ(loc.mul(alpha,loc.scale(Qq,fac*e0),tol))
  Qc=loc.add(loc.mul(loc.add(ex,loc.scale(ey,nus)),exc),loc.mul(loc.add(loc.scale(ex,nus),ey),eyc));Rc+=loc.integ(loc.mul(alpha,loc.scale(Qc,fac*e0),tol))
 return -b*ts/(2*math.pi**2)*P,b*L*ts/(2*math.pi**2)*Rq,b*L*ts/(2*math.pi**2)*Rc

def total(D,q,cw,c):
 Pc,Rqc,Rcc=concrete(D,q,cw,c);Ps,Rqs,Rcs=steel(D,q,cw,c);return Pc+Ps,Rqc+Rqs,Rcc+Rcs,Pc,Ps,Rqc,Rqs,Rcc,Rcs

if __name__=='__main__':
 base.set_compiler(-1.75,.45,601)
 c=dict(b=12000.,ell=9000.,tc=122.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=355.,nuc=.18,nus=.3,q0=.0015)
 r=total(.5,.007244278905,-.0154563484942,c)
 print(dict(P_MN=r[0]/1e6,Rq_MNmm=r[1]/1e6,Rc_MNmm=r[2]/1e6,Pc_MN=r[3]/1e6,Ps_MN=r[4]/1e6,Rqc_MNmm=r[5]/1e6,Rqs_MNmm=r[6]/1e6,Rcc_MNmm=r[7]/1e6,Rcs_MNmm=r[8]/1e6))
