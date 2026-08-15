import sys,math,json,time,numpy as np
sys.path.insert(0,'/mnt/data');import base as b, steel_poly as sp

# ordinary dict helpers
pc=b.pc; mon=b.mon; padd=b.padd; ps=b.ps; pmul=b.pmul
S3y=padd(mon(0,1,0,3),mon(0,3,0,-4)); C3y=padd(pc(1),mon(0,2,0,-4))
S3x=padd(mon(1,0,0,3),mon(3,0,0,-4)); C3x=padd(pc(1),mon(2,0,0,-4))

def C2dict():
 c=pc(1);c=padd(c,mon(2,0,0),-1);c=padd(c,mon(0,2,0),-1);c=padd(c,mon(2,2,0),1);return c

def concrete_der(D,q,c,q0,mode):
 bb,L,t,e0=c['b'],c['ell'],c['tc'],c['eps0'];k=bb/L;pi2=math.pi**2;A=pi2/e0*(q0+q);Bq=pi2*t/(2*e0*bb);M=pi2/e0*(q0*q+.5*q*q);B=pi2*t/(2*e0*bb)*q
 if mode=='q31':
  omx= padd(pc(1),mon(2,0,0),-1); ys3=pmul(mon(0,1,0),S3y)
  exq=ps(pmul(omx,ys3),A);exq=padd(exq,ps(pmul(mon(1,0,1),S3y),Bq))
  omy=padd(pc(1),mon(0,2,0),-1); cc3=pmul(omy,C3y)
  eyq=ps(pmul(mon(2,0,0),cc3),3*A*k*k);eyq=padd(eyq,ps(pmul(mon(1,0,1),S3y),9*k*k*Bq))
  y38=padd(mon(0,1,0,3),mon(0,3,0,-8));uq=ps(pmul(mon(1,0,0),y38),A);uq=padd(uq,ps(pmul(mon(0,0,1),C3y),-3*Bq))
 elif mode=='q13':
  omx=padd(pc(1),mon(2,0,0),-1); cc3=pmul(omx,C3x)
  exq=ps(pmul(mon(0,2,0),cc3),3*A);exq=padd(exq,ps(pmul(mon(0,1,1),S3x),9*Bq))
  omy=padd(pc(1),mon(0,2,0),-1); xs3=pmul(mon(1,0,0),S3x)
  eyq=ps(pmul(omy,xs3),A*k*k);eyq=padd(eyq,ps(pmul(mon(0,1,1),S3x),k*k*Bq))
  x38=padd(mon(1,0,0,3),mon(3,0,0,-8));uq=ps(pmul(x38,mon(0,1,0)),A);uq=padd(uq,ps(pmul(mon(0,0,1),C3x),-3*Bq))
 else:raise ValueError
 u=ps(mon(1,1,0),M);u=padd(u,ps(mon(0,0,1),B),-1);ggq=ps(pmul(C2dict(),pmul(u,uq)),4*k*k)
 return exq,eyq,ggq

def base_ExxEyy(D,q,c,q0,nu=.18):
 bb,L,t,e0=c['b'],c['ell'],c['tc'],c['eps0'];k=bb/L;M=math.pi**2/e0*(q0*q+.5*q*q);B=math.pi**2*t/(2*e0*bb)*q
 ex=pc(nu*D);ex=padd(ex,ps(mon(0,2,0),M));ex=padd(ex,ps(mon(2,2,0),-M));ex=padd(ex,ps(mon(1,1,1),B));ey=pc(-D);ey=padd(ey,ps(mon(2,0,0),k*k*M));ey=padd(ey,ps(mon(2,2,0),-k*k*M));ey=padd(ey,ps(mon(1,1,1),k*k*B));Exx=ps(padd(ex,ps(ey,nu)),1/(1-nu**2));Eyy=ps(padd(ps(ex,nu),ey),1/(1-nu**2));return Exx,Eyy

def concrete_R(D,q,c,q0,mode,tol=5e-7):
 S,f=b.buildS(D,q,c,tol,q0=q0);A,Bs=S;Exx,Eyy=base_ExxEyy(D,q,c,q0);exq,eyq,ggq=concrete_der(D,q,c,q0,mode);Exxc=b.p2c(Exx);Eyyc=b.p2c(Eyy);exqc=b.p2c(exq);eyqc=b.p2c(eyq);Yxx=b.scale(b.add(Exxc,np.array([[[-b.lc]]]),tol=tol),1/b.lh,tol);Yyy=b.scale(b.add(Eyyc,np.array([[[-b.lc]]]),tol=tol),1/b.lh,tol);trq=b.add(exqc,eyqc,tol=tol);yw=b.add(b.mul(Yxx,exqc,tol),b.mul(Yyy,eyqc,tol),1,tol);ggc=b.p2c(ps(ggq,1/(2*(1+.18)*b.lh)));yw=b.add(yw,ggc,1,tol);Q=b.add(b.mul(A,trq,tol),b.mul(Bs,yw,tol),1,tol);return c['fc']*c['eps0']*c['b']*c['ell']*c['tc']/(2*math.pi**2)*b.integ(Q)

def steel_der(D,q,c,q0,face,mode):
 bb,L,tc,ts,e0=c['b'],c['ell'],c['tc'],c['ts'],c['eps0'];k=bb/L;pi2=math.pi**2;A=pi2/e0*(q0+q);z=sp.add(sp.const(face*(tc/2+ts/2)),sp.mono(0,0,1,ts/2));zq=sp.scale(z,pi2/(e0*bb));M=pi2/e0*(q0*q+.5*q*q);u=sp.add(sp.scale(sp.mono(1,1,0),M),sp.scale(z,pi2*q/(e0*bb)),-1);C2=sp.const(1);C2=sp.add(C2,sp.mono(2,0,0),-1);C2=sp.add(C2,sp.mono(0,2,0),-1);C2=sp.add(C2,sp.mono(2,2,0),1)
 s3y=sp.add(sp.mono(0,1,0,3),sp.mono(0,3,0,-4));c3y=sp.add(sp.const(1),sp.mono(0,2,0,-4));s3x=sp.add(sp.mono(1,0,0,3),sp.mono(3,0,0,-4));c3x=sp.add(sp.const(1),sp.mono(2,0,0,-4));omx=sp.add(sp.const(1),sp.mono(2,0,0),-1);omy=sp.add(sp.const(1),sp.mono(0,2,0),-1)
 if mode=='q31':
  exq=sp.scale(sp.mul(omx,sp.mul(sp.mono(0,1,0),s3y)),A);exq=sp.add(exq,sp.mul(zq,sp.mul(sp.mono(1,0,0),s3y)));eyq=sp.scale(sp.mul(sp.mono(2,0,0),sp.mul(omy,c3y)),3*A*k*k);eyq=sp.add(eyq,sp.scale(sp.mul(zq,sp.mul(sp.mono(1,0,0),s3y)),9*k*k));uq=sp.scale(sp.mul(sp.mono(1,0,0),sp.add(sp.mono(0,1,0,3),sp.mono(0,3,0,-8))),A);uq=sp.add(uq,sp.scale(sp.mul(zq,c3y),-3))
 else:
  exq=sp.scale(sp.mul(sp.mono(0,2,0),sp.mul(omx,c3x)),3*A);exq=sp.add(exq,sp.scale(sp.mul(zq,sp.mul(s3x,sp.mono(0,1,0))),9));eyq=sp.scale(sp.mul(omy,sp.mul(sp.mono(1,0,0),s3x)),A*k*k);eyq=sp.add(eyq,sp.scale(sp.mul(zq,sp.mul(s3x,sp.mono(0,1,0))),k*k));uq=sp.scale(sp.mul(sp.add(sp.mono(1,0,0,3),sp.mono(3,0,0,-8)),sp.mono(0,1,0)),A);uq=sp.add(uq,sp.scale(sp.mul(zq,c3x),-3))
 ggq=sp.scale(sp.mul(C2,sp.mul(u,uq)),4*k*k);return exq,eyq,ggq

def steel_R(D,q,c,q0,mode,deg=20,tol=2e-9,nus=.3):
 irq=0
 for face in (-1,1):
  f=sp.fields(D,q,c,q0=q0,face=face);exq,eyq,ggq=steel_der(D,q,c,q0,face,mode);r=sp.scale(f['vm2'],1/c['fy']**2,tol);alpha,_=sp.alpha_field_from_r(r,deg,6.25,tol,100);term=sp.add(sp.mul(sp.add(f['ex'],sp.scale(f['ey'],nus)),exq,tol),sp.mul(sp.add(sp.scale(f['ex'],nus),f['ey']),eyq,tol),1,tol);term=sp.add(term,sp.scale(ggq,(1-nus)/2),1,tol);fac=c['Es']*c['eps0']/(1-nus*nus);Q=sp.scale(term,fac*c['eps0'],tol);irq+=sp.integ(sp.mul(alpha,Q,tol))
 return c['b']*c['ell']*c['ts']/(2*math.pi**2)*irq
