"""DEVELOPMENT/AUDIT ONLY.

Dense multivariate Chebyshev coefficient-space spectral evaluator used to diagnose
the Case21 branch restriction. This explicitly enumerates coefficient tensors and
is therefore NOT an authorized formal production architecture.
"""
import numpy as np, math, time
from scipy.signal import fftconvolve
from numpy.polynomial.chebyshev import cheb2poly
class P3:
 def __init__(self,N):self.N=N;self.S=N+1
 def zero(self):return np.zeros((self.S,self.S,self.S))
 def mono(self,v,i=0,j=0,k=0):a=self.zero();a[i,j,k]=v;return a
 def add(self,a,b,sa=1,sb=1):return sa*a+sb*b
 def mul(self,a,b):
  if not np.any(a) or not np.any(b):return self.zero()
  N=self.N;S=self.S;c=N
  def TL(aa):
   aa=aa.copy();aa[np.abs(aa)<1e-15]=0;idx=np.arange(1,S)
   Lx=np.zeros((2*N+1,S,S));Lx[c]=aa[0];Lx[c+idx]=aa[1:]/2;Lx[c-idx]=aa[1:]/2
   Ly=np.zeros((2*N+1,2*N+1,S));Ly[:,c]=Lx[:,0];Ly[:,c+idx]=Lx[:,1:]/2;Ly[:,c-idx]=Lx[:,1:]/2
   L=np.zeros((2*N+1,2*N+1,2*N+1));L[:,:,c]=Ly[:,:,0];L[:,:,c+idx]=Ly[:,:,1:]/2;L[:,:,c-idx]=Ly[:,:,1:]/2;return L
  C=fftconvolve(TL(a),TL(b),mode='full');base=2*N;out=C[base:base+S,base:base+S,base:base+S].copy();out[1:]*=2;out[:,1:]*=2;out[:,:,1:]*=2;out[np.abs(out)<1e-14]=0;return out
 def eval(self,a,u,v,z):
  def tv(x):
   t=np.empty(self.S);t[0]=1
   if self.N:t[1]=x
   for n in range(2,self.S):t[n]=2*x*t[n-1]-t[n-2]
   return t
  return np.einsum('ijk,i,j,k',a,tv(u),tv(v),tv(z))
 def integ(self,a):
  mx=[];mz=[]
  for n in range(self.S):
   c=np.zeros(n+1);c[n]=1;pp=cheb2poly(c);sx=0;sz=0
   for j,aa in enumerate(pp):
    sx+=aa*math.sqrt(math.pi)*math.gamma((j+1)/2)/math.gamma(j/2+1)
    if j%2==0:sz+=aa*2/(j+1)
   mx.append(sx);mz.append(sz)
  return np.einsum('ijk,i,j,k',a,np.array(mx),np.array(mx),np.array(mz))
 def scalar_cheb_coeff(self,fun,lo,hi,deg):
  nn=max(8*deg+1,129);x=np.cos(np.pi*(np.arange(nn)+.5)/nn);xx=(lo+hi)/2+(hi-lo)/2*x;yy=np.array([fun(float(q)) for q in xx]);return np.polynomial.chebyshev.chebfit(x,yy,deg)
 def peval(self,x,cf,lo,hi):
  xi=self.add(x,self.mono((-(hi+lo)/2)),1,1);xi=xi*(2/(hi-lo));b1=self.zero();b2=self.zero()
  for ck in cf[:0:-1]:b0=self.add(self.add(self.mul(xi,b1)*2,b2,1,-1),self.mono(float(ck)));b2,b1=b1,b0
  return self.add(self.add(self.mul(xi,b1),b2,1,-1),self.mono(float(cf[0])))

def material_funcs():
 fc=21.23;E0=20321.;eps=.00209;k=E0*eps/fc;rho=.1;eta=(rho/k)/20;H=.09799750427197301;UR=.03;a=rho/k
 def pi(z):return z*z*(math.sqrt(z*z+eta*eta)+z)/(2*(z*z+eta*eta))
 def f(l):
  c=pi(-l);t=pi(l);C=k*c/(1+(k-2)*c+c*c)
  if t<=a:
   x=t/a;u=rho*x+(10*H-6*rho)*x**3+(8*rho-15*H)*x**4+(6*H-3*rho)*x**5
  elif t<=10*a:
   s=(t-a)/(9*a);u=H+(UR-H)*(10*s**3-15*s**4+6*s**5)
  else:u=UR
  T=u/rho;U=k*l-C+k*c+u-k*t
  return U,C,T,T**7
 return f

def run(N,D,q,lam,dm=16,dp=64,dgap=16):
 p=P3(N);one=p.mono(1);zero=p.zero();I=(one,one,zero)
 fc=21.23;eps=.00209;nu=.18;b=1220.;tp=19.30;q0=1/400;rho=.1;acc=.1072329249362415;at=1-2**(-1/8)
 u=p.mono(1,1,0,0);v=p.mono(1,0,1,0);z=p.mono(1,0,0,1);u2=p.mul(u,u);v2=p.mul(v,v);omu=p.add(one,u2,1,-1);omv=p.add(one,v2,1,-1);c2=p.mul(omu,omv);uv=p.mul(u,v);uvz=p.mul(uv,z);cx=p.add(one,u2,1,-2);cy=p.add(one,v2,1,-2);cxy=p.mul(cx,cy)
 M=math.pi**2/eps*(q0*q+.5*q*q);B=math.pi**2*tp/(2*eps*b)*q;r0=-lam*M*(1+nu)/4;r20=-lam*M*(1-nu)/4;r22=lam*M/4;s02=-lam*M*(1-nu)/4;s22=lam*M/4
 ex=p.add(p.mono(nu*D+r0),p.mul(omu,v2)*M);ex=p.add(ex,uvz*B);ex=p.add(ex,cx*r20);ex=p.add(ex,cxy*r22)
 ey=p.add(p.mono(-D),p.mul(u2,omv)*M);ey=p.add(ey,uvz*B);ey=p.add(ey,cy*s02);ey=p.add(ey,cxy*s22)
 x11=p.add(ex,ey,1,nu)/(1-nu**2);x22=p.add(ex,ey,nu,1)/(1-nu**2);h=p.add(uv*(M-4*r22)/(1+nu),z*(-B/(1+nu)))
 tr=p.add(x11,x22);diff=p.add(x11,x22,1,-1);gap2=p.add(p.mul(diff,diff),p.mul(c2,p.mul(h,h))*4)
 cfsq=p.scalar_cheb_coeff(lambda x:math.sqrt(x),.30,1.0,dgap);gap=p.peval(gap2,cfsq,.30,1.0)
 cfinv=p.scalar_cheb_coeff(lambda x:1/x,.50,1.05,dgap);ig=p.peval(gap,cfinv,.50,1.05)
 lp=p.add(tr,gap)*.5;lm=p.add(tr,gap,1,-1)*.5
 Pp=(p.mul(p.add(x11,lm,1,-1),ig),p.mul(p.add(x22,lm,1,-1),ig),p.mul(h,ig))
 mf=material_funcs();los={'m':(-1.0,-.55),'p':(-.10,.10)};coeff={}
 for branch,deg in [('m',dm),('p',dp)]:
  lo,hi=los[branch]
  for idx,name in enumerate(['U','C','T','T7']):coeff[(branch,name)]=p.scalar_cheb_coeff(lambda x,ii=idx:mf(x)[ii],lo,hi,deg)
 def feval(field,branch,name):lo,hi=los[branch];return p.peval(field,coeff[(branch,name)],lo,hi)
 def matfun(name):
  fm=feval(lm,'m',name);fp=feval(lp,'p',name);delta=p.add(fp,fm,1,-1)
  return (p.add(fm,p.mul(delta,Pp[0])),p.add(fm,p.mul(delta,Pp[1])),p.mul(delta,Pp[2]))
 U=matfun('U');C=matfun('C');T=matfun('T');T7=matfun('T7')
 def mmul(A,B):
  qv=p.mul(c2,p.mul(A[2],B[2]));return p.add(p.mul(A[0],B[0]),qv),p.add(p.mul(A[1],B[1]),qv),p.add(p.mul(A[0],B[2]),p.mul(A[2],B[1]))
 def det(A):return p.add(p.mul(A[0],A[1]),p.mul(c2,p.mul(A[2],A[2])),1,-1)
 def adj(A):return A[1],A[0],-A[2]
 dC=det(C);CC=tuple(p.mul(dC,x) for x in C);CadjT=mmul(C,adj(T));dT=det(T);trT7=p.add(T7[0],T7[1]);last=(p.add(trT7,T7[0],1,-1),p.add(trT7,T7[1],1,-1),-T7[2]);last=tuple(p.mul(dT,x) for x in last)
 S=tuple(p.add(p.add(U[i],CC[i],1,-acc),CadjT[i]) for i in range(3));S=tuple(p.add(S[i],last[i],1,-rho*at) for i in range(3))
 return p,S

if __name__=='__main__':
 D=.7887924801;q=.0018083572562965242;lam=.08623596353826937;nu=.18;fc=21.23;eps=.00209;b=ell=1220.;tp=19.30;q0=1/400;Es=200000.;rs=.00375
 for N,dm,dp,dg in [(12,18,96,20),(14,18,96,20),(16,18,96,20),(20,18,96,20),(24,18,96,20)]:
  t0=time.time();p,S=run(N,D,q,lam,dm,dp,dg);sx,sy,sh=S;one=p.mono(1);u=p.mono(1,1,0,0);v=p.mono(1,0,1,0);z=p.mono(1,0,0,1);u2=p.mul(u,u);v2=p.mul(v,v);uv=p.mul(u,v);c2=p.mul(p.add(one,u2,1,-1),p.add(one,v2,1,-1));cx=p.add(one,u2,1,-2);cy=p.add(one,v2,1,-2);cxy=p.mul(cx,cy);shear22=p.mul(uv,c2)*4;uvz=p.mul(uv,z);c2z=p.mul(c2,z);integ=p.integ
  J=np.array([integ(sx),integ(p.mul(sx,cx)),integ(p.mul(sx,cy)),integ(p.mul(sx,cxy)),integ(sy),integ(p.mul(sy,cx)),integ(p.mul(sy,cy)),integ(p.mul(sy,cxy)),integ(p.mul(sh,shear22)),integ(p.mul(sx,uvz)),integ(p.mul(sy,uvz)),integ(p.mul(sh,c2z))])*fc
  Mv=math.pi**2/eps*(q0*q+.5*q*q);Mq=math.pi**2/eps*(q0+q);Bq=math.pi**2/(2*eps)*(tp/b);Cvol=eps*b*ell*tp/(2*math.pi**2)/1000;Pc=-b*tp/(2*math.pi**2)*J[4]/1000
  RAc=Cvol*(-(1+nu)/4*J[0]-(1-nu)/4*J[1]+.25*J[3]-(1-nu)/4*J[6]+.25*J[7]-.5*J[8]);Rqc=Cvol*(Mq/4*(J[0]+J[1]-J[2]-J[3]+J[4]-J[5]+J[6]-J[7]+2*J[8])+Bq*(J[9]+J[10]-2*J[11]))
  Cs=rs*tp*b*Es*eps/1000;CR=rs*Es*eps**2*b*ell*tp/(32*1000);Ps=Cs*(D-Mv/4);RAs=-CR*(8*D*nu*(nu+1)+Mv*(5-(4*nu**2+5)*lam));Rqs=CR*Mq*(8*D*(nu-1)+Mv*(9-5*lam))
  print(dict(N=N,seconds=time.time()-t0,P_kN=Pc+Ps,Pc_kN=Pc,Rq=Rqc+Rqs,RA=RAc+RAs,T12=J.tolist()))
