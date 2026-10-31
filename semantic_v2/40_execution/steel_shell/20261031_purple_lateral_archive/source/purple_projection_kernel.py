#!/usr/bin/env python3
"""Two-mode PURPLE seven-node Lagrange analytic Fourier projection.
Axial coordinate y. One shell only. No FEM calibration, no surface quadrature.
New Ritz in-plane condensation, original purple RMS Mises chord, double vertex
chord, elastic bending correction and positive membrane virtual-work capacity.
The multi-mode cap is a declared extension, not old purple's numerical constant.
"""
from dataclasses import dataclass
import numpy as np
from scipy.optimize import root,least_squares,brentq
from scipy.special import comb
import math,csv,sys
# local analytic Fourier integration, no external dependencies except numpy/scipy
import fourier_exact as f
P=math.pi
@dataclass
class Params:
 b:float=2500.
 a:float=2500.
 t:float=4.
 E:float=206000.
 nu:float=.3
 fy:float=355.
 N:int=5
 m:int=4
 W0:float=None
 A0:float=None
 def __post_init__(self):
  if self.W0 is None:self.W0=self.b/400
  if self.A0 is None:self.A0=self.t/60

# Fourier spectral exact trigonometric integration
zero=lambda:{ }
def vadd(x,y,s=1):return [f.add(x[i],y[i],fb=s) for i in range(3)]
def vscale(x,s):return [f.scale(i,s) for i in x]
def vdot_integral(x,y,C,moment):
 return sum(C[i,j]*moment(f.mul(x[i],y[j])) for i in range(3) for j in range(3) if C[i,j])
def vd(x,y,ww):
 out={}
 for i in range(3):
  for j in range(3):
   if ww[i,j]:out=f.add(out,f.scale(f.mul(x[i],y[j]),ww[i,j]))
 return out

def polypow(basis,N):
 out=[f.const()]
 for _ in range(N):out.append(f.mul(out[-1],basis))
 return out

class Model:
 def __init__(self,p):
  self.p=p
  self.C=p.E/(1-p.nu**2)*np.array([[1,p.nu,0],[p.nu,1,0],[0,0,(1-p.nu)/2]])
  self.H=np.array([[1,-.5,0],[-.5,1,0],[0,0,3]])
  self.HC=self.C@self.H@self.C
  # global simply supported 1 sine halfwave; local clamped 1 positive bulge per bay
  phi=f.mul(f.sinfreq(1,'x'),f.sinfreq(1,'y'))
  psi=f.scale(f.mul(f.add(f.const(),f.cosfreq(2*p.N,'x'),fb=-1),f.add(f.const(),f.cosfreq(2*p.m,'y'),fb=-1)),.25)
  self.phi=phi;self.psi=psi
  px=f.deriv(phi,'x',p.b);py=f.deriv(phi,'y',p.a)
  sx=f.deriv(psi,'x',p.b);sy=f.deriv(psi,'y',p.a)
  grad=lambda ax,ay,bx,by:[f.mul(ax,bx),f.mul(ay,by),f.add(f.mul(ax,by),f.mul(ay,bx))]
  self.GG=vscale(grad(px,py,px,py),.5)
  self.GL=grad(px,py,sx,sy)
  self.LL=vscale(grad(sx,sy,sx,sy),.5)
  curvature=lambda sh:[f.scale(f.deriv(f.deriv(sh,'x',p.b),'x',p.b),-p.t),f.scale(f.deriv(f.deriv(sh,'y',p.a),'y',p.a),-p.t),f.scale(f.deriv(f.deriv(sh,'x',p.b),'y',p.a),-2*p.t)]
  self.Kcur=[curvature(phi),curvature(psi)]
  # interior planar displacements analytic elimination. No nonlinear DOFs beyond W,A.
  # global second harmonic, and local-bay even harmonic, all plain sin cos.
  ux_g=f.scale(f.sinfreq(2,'x'),p.b/(2*P)); vy_g=f.scale(f.sinfreq(2,'y'),p.a/(2*P))
  ux_gl=f.scale(f.mul(f.sinfreq(2,'x'),f.cosfreq(2,'y')),p.b/(2*P))
  vy_gl=f.scale(f.mul(f.cosfreq(2,'x'),f.sinfreq(2,'y')),p.a/(2*P))
  ux_l=f.scale(f.mul(f.sinfreq(2*p.N,'x'),f.add(f.const(),f.cosfreq(2*p.m,'y'),fb=-1)),p.b/(2*P*p.N))
  vy_l=f.scale(f.mul(f.add(f.const(),f.cosfreq(2*p.N,'x'),fb=-1),f.sinfreq(2*p.m,'y')),p.a/(2*P*p.m))
  mkux=lambda u:[f.deriv(u,'x',p.b),{},f.deriv(u,'y',p.a)]
  mkvy=lambda v:[{},f.deriv(v,'y',p.a),f.deriv(v,'x',p.b)]
  self.modes=[mkux(ux_g),mkux(ux_gl),mkvy(vy_g),mkvy(vy_gl),mkux(ux_l),mkvy(vy_l)]
  self.base=[[f.const(p.nu),f.const(-1),{}],self.GG,self.GL,self.LL]
  K=np.array([[vdot_integral(u,v,self.C,f.mean) for v in self.modes] for u in self.modes])
  B=np.array([[vdot_integral(u,v,self.C,f.mean) for v in self.base] for u in self.modes])
  self.Kplan=K
  # elastic stationary coefficients h=cond@ [d,2W0W+W², W0 A+A0 W+WA,2 A0 A+A²]
  self.cond=np.linalg.solve(K,-B)
  self.basis=[self.base[i] for i in range(4)]
  for k in range(4):
   for j in range(len(self.modes)):
    self.basis[k]=vadd(self.basis[k],vscale(self.modes[j],self.cond[j,k]))
  # exactly seven Lagrange basis on T=psi². Neither numerical points nor Gauss.
  self.q=(1-np.cos(np.arange(7)*P/6))/2
  self.poly=[]
  for i in range(7):
   roots=np.delete(self.q,i)
   coef=np.polynomial.polynomial.polyfromroots(roots)
   coef/=np.prod(self.q[i]-roots)
   self.poly.append(np.asarray(coef,float))
  # gamma moments for T^r = sin^(4r)(N X)*sin^(4r)(mY)
  def get_integ(k,order,freq):
   r=2*order
   return sum(((-1.)**j)*comb(2*r,r-j,exact=True)/4**r*f.oned(k+2*j*freq) for j in range(-r,r+1))
  self.mean_T=[]
  for r in range(7):
   def mr(field,r=r):
    ans=sum(v*get_integ(k,r,p.N)*get_integ(l,r,p.m) for (k,l),v in field.items())
    if abs(ans.imag)>max(1,abs(ans.real))*5e-9:raise ArithmeticError(('complex',ans))
    return float(ans.real)
   self.mean_T.append(mr)
  self.omega=np.array([sum(co*integr(f.const()) for co,integr in zip(coefs,self.mean_T)) for coefs in self.poly])
  if not np.all(np.abs(self.omega)>1e-6):raise ValueError(('bad omega',self.omega))
  def weighted(ff,j):return sum(c*integ(ff) for c,integ in zip(self.poly[j],self.mean_T))
  self.weighted=weighted
  self.m1=np.zeros((7,4,3));self.mb=np.zeros((7,2,3));
  self.Q00=np.zeros((7,4,4));self.Q01=np.zeros((7,4,2));self.Q11=np.zeros((7,2,2))
  for j in range(7):
   for i in range(4):
    for k in range(3):self.m1[j,i,k]=weighted(self.basis[i][k],j)/self.omega[j]
   for i in range(2):
    for k in range(3):self.mb[j,i,k]=weighted(self.Kcur[i][k],j)/self.omega[j]
   for i in range(4):
    for ii in range(i,4):
     q=weighted(vd(self.basis[i],self.basis[ii],self.HC),j)/self.omega[j]
     self.Q00[j,i,ii]=self.Q00[j,ii,i]=q
    for ii in range(2):self.Q01[j,i,ii]=weighted(vd(self.basis[i],self.Kcur[ii],self.HC),j)/self.omega[j]
   for i in range(2):
    for ii in range(i,2):
     q=weighted(vd(self.Kcur[i],self.Kcur[ii],self.HC),j)/self.omega[j]
     self.Q11[j,i,ii]=self.Q11[j,ii,i]=q
  self.Dexact=np.array([[vdot_integral(x,y,self.C,f.mean) for y in self.Kcur] for x in self.Kcur])
  self.Drep=sum(self.omega[j]*self.mb[j]@self.C@self.mb[j].T for j in range(7))
  self.Dmissing=self.Dexact-self.Drep
  # pure geometry bases for capacity, scalar nonuniform axial strain = ggy and gl_y and lly
  self.geom_y=np.array([[weighted(a[1],j)/self.omega[j] for a in [self.GG,self.GL,self.LL]] for j in range(7)])
  self.geom_x=np.array([[weighted(a[0],j)/self.omega[j] for a in [self.GG,self.GL,self.LL]] for j in range(7)])
  self.geom_mean_y=np.array([f.mean(g[1]) for g in [self.GG,self.GL,self.LL]])
  self.geom_mean_x=np.array([f.mean(g[0]) for g in [self.GG,self.GL,self.LL]])
  # scalar critical strain, classical simply-supported reference k=4 (purple legacy)
  self.ecr=4*P**2/(12*(1-p.nu**2)*(p.b/p.t)**2)
  print('model precomputed',p,'omega',self.omega,'Dmissing',self.Dmissing,flush=True)

 def solve_section(self,j,q0,kvec):
  p=self.p;t=p.t
  q=np.array([np.dot(q0,self.Q00[j]@q0),2*np.dot(q0,self.Q01[j]@kvec),np.dot(kvec,self.Q11[j]@kvec)])
  ca,cb,cc=q[2],q[1],q[0]
  # Negative RMS square from signed interpolation is not physical: fail, no clipping.
  xs=[-.5,.5]
  if ca>1e-20:
   disc=cb*cb-4*ca*(cc-p.fy*p.fy)
   if disc>0:
    for x in [(-cb-math.sqrt(disc))/(2*ca),(-cb+math.sqrt(disc))/(2*ca)]:
     if -.5+1e-10<x<.5-1e-10:xs.append(float(x))
  elif abs(cb)>1e-20:
   x=(p.fy*p.fy-cc)/cb
   if -.5+1e-10<x<.5-1e-10:xs.append(float(x))
  xs=sorted(set(xs))
  if len(xs)==2 and ca>1e-20:
   xv=-cb/(2*ca)
   if -.5<xv<.5 and ca*xv*xv+cb*xv+cc>p.fy*p.fy:
    xs=[-.5,xv,.5]
  s0=self.C@np.einsum('i,ij->j',q0,self.m1[j])
  s1=self.C@np.einsum('i,ij->j',kvec,self.mb[j])
  nn=np.zeros(3); mm=np.zeros(3); elastic_I2=0.;npos=0
  for lo,hi in zip(xs[:-1],xs[1:]):
   xm=(lo+hi)/2;Qmid=ca*xm*xm+cb*xm+cc
   if Qmid<=p.fy*p.fy:
    nn+=(hi-lo)*s0+(.5*(hi*hi-lo*lo))*s1
    mm+=.5*(hi*hi-lo*lo)*s0+((hi**3-lo**3)/3)*s1
    elastic_I2+=(hi**3-lo**3)/3
   else:
    def linevalue(x):
     qx=ca*x*x+cb*x+cc
     if qx<=0:raise ValueError(('negative Q',j,x,qx))
     return (s0+x*s1)*(p.fy/math.sqrt(qx))
    sl=linevalue(lo);sh=linevalue(hi)
    nn+=(hi-lo)*.5*(sl+sh)
    mm+=(hi-lo)/6*((2*lo+hi)*sl+(lo+2*hi)*sh)
  return nn,mm,elastic_I2,q

 def evaluate(self,d,W,A,cap=True):
  p=self.p
  # q0=[d, 2W0W+W², W0 A+A0 W+WA,2A0A+A²]
  U=p.W0+W;L=p.A0+A
  q0=np.array([d,U**2-p.W0**2,U*L-p.W0*p.A0,L**2-p.A0**2])
  dW=np.array([0,2*U,L,0]);dA=np.array([0,0,U,2*L])
  kvec=np.array([W,A]);kW=np.array([1,0]);kA=np.array([0,1])
  n=[];m=[];I2=[];QQ=[]
  for j in range(7):
   try:nn,mm,ec,q=self.solve_section(j,q0,kvec)
   except ValueError as exc:return {'ok':False,'cause':str(exc)}
   n.append(nn);m.append(mm);I2.append(ec);QQ.append(q)
  n=np.array(n);m=np.array(m);I2=np.array(I2)
  mid=np.einsum('jk,k->j',self.geom_y,q0[1:])
  midx=np.einsum('jk,k->j',self.geom_x,q0[1:])
  # Independent membrane positive-work channel, generalization of purple:
  # geometry-induced strain d e_geom / d amplitude, orthogonalized by mean
  # axial+Poisson transverse geometry, never change axial N.
  derG=np.array([dW[1:],dA[1:]])
  chi=12*np.dot(self.omega,I2)
  out=[]
  for ix,dr in enumerate([dW,dA]):
   drb=np.array([1.,0.]) if ix==0 else np.array([0.,1.])
   de=np.einsum('k,jkl->jl',dr,self.m1)
   dk=np.einsum('k,jkl->jl',drb,self.mb)
   Rmem=np.sum(self.omega*np.sum(n*de,axis=1))
   Rbend=np.sum(self.omega*np.sum(m*dk,axis=1))
   Rextra=(drb@self.Dmissing@kvec)/12*chi
   Rcap=0
   if cap:
    # independent axial membrane channel after removing uniform Poisson-coupled response
    cg=np.einsum('k,jkl->jl',dr[1:],np.stack([self.geom_x,self.geom_y,np.zeros_like(self.geom_y)],axis=2))
    cm=float(np.dot(dr[1:],self.geom_mean_y+p.nu*self.geom_mean_x))
    independent=np.sum(n*cg,axis=1)-cm*n[:,1]
    effstrain=np.abs(mid - np.dot(q0[1:],self.geom_mean_y))
    gj=np.maximum(0,1-self.ecr/np.maximum(effstrain,1e-30))
    Rcap=-np.sum(self.omega*gj*np.maximum(independent,0))
   out.append([Rmem,Rbend,Rextra,Rcap])
  # applied compressive force per width from true average representative n_y
  sigma=-np.dot(self.omega,n[:,1]);Force=sigma*p.b*p.t/1e6
  return {'ok':True,'R':np.sum(out,axis=1),'parts':np.array(out),'sigma':sigma,'MN':Force,'chi':chi,'q0':q0,'n':n,'m':m}

def scan(p,ds,cap=True):
 mod=Model(p);records=[]
 scale=p.E*p.t/p.b**2
 for d in ds:
  fun=lambda x:mod.evaluate(d,float(x[0]),float(x[1]),cap)
  candidate=[]
  def push(x,s,kind):
   if not s['ok']:return
   if kind=='interior' and (x[0]<=1e-8 or x[1]<=1e-7):return
   if kind=='boundary_A0' and s['R'][1]<-1e-8:return
   if kind=='boundary_W0' and s['R'][0]<-1e-8:return
   if (np.linalg.norm(s['R'])/scale if kind=='interior' else abs(s['R'][0 if kind=='boundary_A0' else 1])/scale)>1e-7:return
   if any(np.linalg.norm(x-z[0])<1e-3 for z in candidate):return
   candidate.append((x,s,kind))
  # A=0: solve W equilibrium, then test unilateral condition R_A >= 0.
  wg=np.concatenate([[0.],np.geomspace(1e-5,4*p.b,80)])
  last=None
  for w in wg:
   s=mod.evaluate(d,w,0.,cap)
   if not s['ok']:continue
   if last is not None and s['R'][0]*last[1]['R'][0]<0:
    wr=brentq(lambda w:mod.evaluate(d,w,0.,cap)['R'][0],last[0],w,xtol=1e-10)
    rr=mod.evaluate(d,wr,0.,cap);push(np.array([wr,0.]),rr,'boundary_A0')
   last=(w,s)
  # W=0: solve A equilibrium, then test unilateral condition R_W>=0.
  ag=np.concatenate([[0.],np.geomspace(1e-5,20*p.t,80)])
  last=None
  for a in ag:
   s=mod.evaluate(d,0.,a,cap)
   if not s['ok']:continue
   if last is not None and s['R'][1]*last[1]['R'][1]<0:
    ar=brentq(lambda a:mod.evaluate(d,0.,a,cap)['R'][1],last[0],a,xtol=1e-10)
    rr=mod.evaluate(d,0.,ar,cap);push(np.array([0.,ar]),rr,'boundary_W0')
   last=(a,s)
  # Interior A>0, W>0: solve both residuals with independent starts.
  for wseed in [0.01*p.W0,0.25*p.W0,p.W0,4*p.W0,12*p.W0]:
   for aseed in [.05*p.t,.25*p.t,p.t,4*p.t,10*p.t]:
    def residual(x):
     st=fun(x)
     if not st['ok']:return [1e6,1e6]
     return (st['R']/scale).tolist()
    sol=least_squares(residual,[wseed,aseed],bounds=([0,0],[2*p.b,5*p.b]),max_nfev=250,ftol=1e-12,xtol=1e-12,gtol=1e-12)
    st=fun(sol.x)
    if st['ok'] and np.linalg.norm(st['R'])/scale<1e-7:push(sol.x,st,'interior')
  for x,s,kind in candidate:
   U=p.W0+x[0];L=p.A0+x[1]
   q0=np.array([d,U*U-p.W0*p.W0,U*L-p.W0*p.A0,L*L-p.A0*p.A0]);kv=np.array(x)
   qmins=[]
   for j in range(7):
    ca=kv@mod.Q11[j]@kv;cb=2*q0@mod.Q01[j]@kv;cc=q0@mod.Q00[j]@q0
    vals=[ca*.25-cb*.5+cc,ca*.25+cb*.5+cc]
    if ca>0 and -.5<-cb/(2*ca)<.5:vals.append(cc-cb*cb/(4*ca))
    qmins.append(min(vals))
   qmin=min(qmins)
   records.append(dict(d=d,W=x[0],A=x[1],sigma=s['sigma'],MN=s['MN'],chi=s['chi'],resnorm=np.linalg.norm(s['R'])/scale,R_W=s['R'][0],R_A=s['R'][1],kind=kind,cap=cap,Qmin=qmin,projected_Q_nonnegative=qmin>=-1e-6))
  if not candidate:records.append(dict(d=d,W=np.nan,A=np.nan,sigma=np.nan,MN=np.nan,chi=np.nan,resnorm=np.nan,R_W=np.nan,R_A=np.nan,kind='none',cap=cap,Qmin=np.nan,projected_Q_nonnegative=False))
  print('d',d,'found',len(candidate),'root(s)',[(kind,np.round(x,3),round(st['MN'],4)) for x,st,kind in candidate],flush=True)
 return records

if __name__=='__main__':
 p=Params()
 mod=Model(p)
 # strict input checks and internal identities
 assert np.max(np.abs(mod.Dmissing-mod.Dmissing.T))<1e-5
 assert abs(mod.omega.sum()-1)<1e-8
 for d in [.0001,.001]:
  e=mod.evaluate(d,p.W0*.4,p.t*.5)
  print('single',d,e['ok'],e.get('R'),e.get('parts'),e.get('MN'))
 ds=[.00005,.0001,.0002,.0004,.0008,.0012,.0018,.0026,.004,.006]
 out=scan(p,ds,cap=True)
 with open('/mnt/data/purple_two_mode_20261031/curve.csv','w') as fh:
  writer=csv.DictWriter(fh,fieldnames=list(out[0]));writer.writeheader();writer.writerows(out)