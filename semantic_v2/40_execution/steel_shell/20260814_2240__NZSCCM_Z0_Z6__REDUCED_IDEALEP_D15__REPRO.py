# NZ-SCCM Z0-Z6 reduced Zhou reproducibility kernel
# Timestamp: 2026-08-14 22:40 +08:00
# Formal structural spatial sampling/quadrature = 0.
# FFT is used only for exact coefficient-space Chebyshev/Laurent convolution; it is not spatial collocation.
# Material-coordinate LP nodes are used only to regenerate N48 T minimax coefficients for expanded compiler intervals.
# Result identity: CONNECTED_REDUCED_IDEAL_EP_DIAGNOSTIC, not full 2D plastic-zone production certification.

import numpy as np, math
from scipy.signal import fftconvolve
from scipy.optimize import root_scalar
from numpy.polynomial.chebyshev import chebvander, chebval, chebder, poly2cheb
kappa=2.0005129533678754; rho=.1; xcr=rho/kappa; eta=xcr/20; ur=.03; h=.09799750427197301
acc=.1072329249362415; at=1-2**(-1/8); lc=-.515; lh=.635

def Pi(z):
 z=np.asarray(z,float); return z*z*(np.sqrt(z*z+eta*eta)+z)/(2*(z*z+eta*eta))
def uR(t):
 t=np.asarray(t,float); r=t/xcr; o=np.empty_like(r); m=r<=1; rr=r[m]
 o[m]=rho*rr+(10*h-6*rho)*rr**3+(8*rho-15*h)*rr**4+(6*h-3*rho)*rr**5
 m2=(r>1)&(r<=10); s=(r[m2]-1)/9; o[m2]=h+(ur-h)*(10*s**3-15*s**4+6*s**5); o[r>10]=ur; return o
def targets(lam):
 lam=np.asarray(lam,float); c=Pi(-lam); t=Pi(lam); C=kappa*c/(1+(kappa-2)*c+c*c); u=uR(t); T=u/rho; U=kappa*lam-C+kappa*c+u-kappa*t; return U,C,T,T**7
th=(np.arange(49)+.5)*np.pi/49; nodes=lc+lh*np.cos(th); V=chebvander((nodes-lc)/lh,48); xi0=-lc/lh; E=np.eye(49)
vr=np.array([chebval(xi0,E[n]) for n in range(49)]); dr=np.array([chebval(xi0,chebder(E[n]))/lh for n in range(49)]); AE=np.vstack([vr,dr])
def cls(vals,b):
 H=V.T@V; K=np.block([[H,AE.T],[AE,np.zeros((2,2))]]); return np.linalg.solve(K,np.r_[V.T@vals,b])[:49]
Uv,Cv,Tv,T7v=targets(nodes); Ucoef=cls(Uv,[0,kappa]); Ccoef=cls(Cv,[0,0]); T7coef=cls(T7v,[0,0])
Tcoef=np.array([.175898643477104988,.332753009593392990,.279538323050278759,.202366690913507258,.115571744871195647,.034347493228315697,-.0285747373688849393,-.0654979508158327331,-.0749863066692420532,-.0615270754102322376,-.0338190768361813568,-.002221675768969998,.0239242937077384777,.0384128861703389932,.0392431266951378949,.0284772401417321408,.0110610100374321542,-.00696047294203041775,-.0202790730788860417,-.0257066333425670611,-.0227799294265627027,-.0135173669046293778,-.00150243306525367081,.00936062926756111961,.0160221180714108756,.0170634613762070744,.0129008768222890358,.0054286747585888927,-.00272375681029087989,-.00905624987191528709,-.0119159094137514538,-.0108773131416410121,-.00671636918169786143,-.00103615963677496418,.00430227823876152,.00775486537284359422,.00850744408825754306,.00662851997961389199,.00294959998660242976,-.00125860397635844793,-.00469864555384412724,-.00642051988282866734,-.00605906660041858995,-.00388381660894998072,-.000668954209411751644,.00256857560164184401,.00546469930671622441,.092353752428681517,-.000652654235998186612])
def padd(a,b,s=1):
 r=a.copy()
 for k,v in b.items():
  r[k]=r.get(k,0)+s*v
  if abs(r[k])<1e-15:r.pop(k,None)
 return r
def ps(a,s):return {k:v*s for k,v in a.items() if abs(v*s)>=1e-15}
def pmul(a,b):
 r={}
 for x,v in a.items():
  for y,w in b.items():
   k=tuple(x[i]+y[i] for i in range(3));r[k]=r.get(k,0)+v*w
 return {k:v for k,v in r.items() if abs(v)>=1e-15}
def pc(x):return {(0,0,0):float(x)} if x else {}
def mon(i,j,k,c=1):return {(i,j,k):float(c)}
mc={}
def mcheb(n):
 if n not in mc:
  p=np.zeros(n+1);p[n]=1;mc[n]=poly2cheb(p)
 return mc[n]
def p2c(p):
 mx=[0,0,0]
 for k in p:
  for d in range(3):mx[d]=max(mx[d],k[d])
 o=np.zeros(tuple(x+1 for x in mx))
 for (i,j,k),v in p.items():
  a=mcheb(i);b=mcheb(j);c=mcheb(k);t=v*a[:,None,None]*b[None,:,None]*c[None,None,:];o[:t.shape[0],:t.shape[1],:t.shape[2]]+=t
 return o
def trim(A,tol=2e-9):
 sl=[]
 for ax in range(3):
  q=np.max(np.abs(A),axis=tuple(i for i in range(3) if i!=ax));ids=np.where(q>tol)[0];last=int(ids[-1]) if ids.size else 0;sl.append(slice(0,last+1))
 return A[tuple(sl)]
def add(A,B,s=1,tol=2e-9):
 sh=tuple(max(A.shape[d],B.shape[d]) for d in range(3));C=np.zeros(sh,dtype=np.result_type(A,B));C[:A.shape[0],:A.shape[1],:A.shape[2]]+=A;C[:B.shape[0],:B.shape[1],:B.shape[2]]+=s*B;return trim(C,tol)
def scale(A,s,tol=2e-9):return trim(A*s,tol)
def ctl(A):
 A=np.asarray(A);n0,n1,n2=A.shape;L=np.zeros((2*n0-1,n1,n2),dtype=A.dtype);c0=n0-1;L[c0]+=A[0]
 for i in range(1,n0):h=.5*A[i];L[c0-i]+=h;L[c0+i]+=h
 L2=np.zeros((L.shape[0],2*n1-1,n2),dtype=A.dtype);c1=n1-1;L2[:,c1,:]+=L[:,0,:]
 for j in range(1,n1):h=.5*L[:,j,:];L2[:,c1-j,:]+=h;L2[:,c1+j,:]+=h
 L3=np.zeros((L2.shape[0],L2.shape[1],2*n2-1),dtype=A.dtype);c2=n2-1;L3[:,:,c2]+=L2[:,:,0]
 for k in range(1,n2):h=.5*L2[:,:,k];L3[:,:,c2-k]+=h;L3[:,:,c2+k]+=h
 return L3,(c0,c1,c2)
def mul(A,B,tol=2e-9):
 LA,a=ctl(A);LB,b=ctl(B);LC=fftconvolve(LA,LB);cc=tuple(a[d]+b[d] for d in range(3));md=tuple(A.shape[d]+B.shape[d]-2 for d in range(3));P=LC[tuple(slice(cc[d],cc[d]+md[d]+1) for d in range(3))].copy();f0=np.ones(P.shape[0]);f1=np.ones(P.shape[1]);f2=np.ones(P.shape[2]);f0[1:]=2;f1[1:]=2;f2[1:]=2;P*=f0[:,None,None]*f1[None,:,None]*f2[None,None,:];return trim(P,tol)
def low(D,q,c,nu=.18,q0=.0025):
 b,L,t,e0=c['b'],c['ell'],c['tc'],c['eps0'];k=b/L;M=math.pi**2/e0*(q0*q+.5*q*q);B=math.pi**2*t/(2*e0*b)*q;Mq=math.pi**2/e0*(q0+q);Bq=math.pi**2*t/(2*e0*b)
 J1=pc((nu-1)*D);J1=padd(J1,ps(mon(0,2,0),M));J1=padd(J1,ps(mon(2,0,0),M*k*k));J1=padd(J1,ps(mon(2,2,0),-M*(1+k*k)));J1=padd(J1,ps(mon(1,1,1),B*(1+k*k)))
 J1q=ps(mon(0,2,0),Mq);J1q=padd(J1q,ps(mon(2,0,0),Mq*k*k));J1q=padd(J1q,ps(mon(2,2,0),-Mq*(1+k*k)));J1q=padd(J1q,ps(mon(1,1,1),Bq*(1+k*k)))
 J2=pc(-nu*D*D);J2=padd(J2,ps(mon(2,0,0),D*M*k*k*nu));J2=padd(J2,ps(mon(0,2,0),-D*M));J2=padd(J2,ps(mon(2,2,0),D*M*(1-k*k*nu)));J2=padd(J2,ps(mon(1,1,1),B*D*(k*k*nu-1)))
 BM=B*M*k*k;J2=padd(J2,ps(mon(1,1,1),2*BM));J2=padd(J2,ps(mon(3,1,1),-BM));J2=padd(J2,ps(mon(1,3,1),-BM));BB=B*B*k*k;J2=padd(J2,ps(mon(2,0,2),BB));J2=padd(J2,ps(mon(0,2,2),BB));J2=padd(J2,ps(mon(0,0,2),-BB))
 J2q=ps(mon(2,0,0),D*Mq*k*k*nu);J2q=padd(J2q,ps(mon(0,2,0),-D*Mq));J2q=padd(J2q,ps(mon(2,2,0),D*Mq*(1-k*k*nu)));J2q=padd(J2q,ps(mon(1,1,1),Bq*D*(k*k*nu-1)))
 X=(Bq*M+B*Mq)*k*k;J2q=padd(J2q,ps(mon(1,1,1),2*X));J2q=padd(J2q,ps(mon(3,1,1),-X));J2q=padd(J2q,ps(mon(1,3,1),-X));X=2*B*Bq*k*k;J2q=padd(J2q,ps(mon(2,0,2),X));J2q=padd(J2q,ps(mon(0,2,2),X));J2q=padd(J2q,ps(mon(0,0,2),-X))
 I1=ps(J1,1/(1-nu));I1q=ps(J1q,1/(1-nu));I2=ps(padd(J2,ps(pmul(I1,I1),nu)),1/(1+nu)**2);I2q=ps(padd(J2q,ps(pmul(I1,I1q),2*nu)),1/(1+nu)**2);Gq=padd(pmul(I1,I1q),I2q,-1)
 ex=pc(nu*D);ex=padd(ex,ps(mon(0,2,0),M));ex=padd(ex,ps(mon(2,2,0),-M));ex=padd(ex,ps(mon(1,1,1),B));ey=pc(-D);ey=padd(ey,ps(mon(2,0,0),k*k*M));ey=padd(ey,ps(mon(2,2,0),-k*k*M));ey=padd(ey,ps(mon(1,1,1),k*k*B));Xyy=ps(padd(ps(ex,nu),ey),1/(1-nu**2))
 K1=ps(padd(I1,pc(-2*lc)),1/lh);K2=ps(padd(padd(I2,ps(I1,-lc)),pc(lc*lc)),1/lh**2);Yyy=ps(padd(Xyy,pc(-lc)),1/lh)
 return {n:p2c(v) for n,v in [('K1',K1),('K2',K2),('I1q',I1q),('Gq',Gq),('Yyy',Yyy)]}
def recur(K1,K2,co,tol=2e-9):
 one=np.ones((1,1,1));zero=np.zeros((1,1,1));ap=one;bp=zero;ac=zero;bc=one;FA=scale(one,co[0],tol);FB=scale(one,co[1],tol)
 for n in range(1,48):
  an=add(scale(mul(bc,K2,tol),-2,tol),ap,-1,tol);bn=add(add(scale(ac,2,tol),scale(mul(bc,K1,tol),2,tol),1,tol),bp,-1,tol);FA=add(FA,scale(an,co[n+1],tol),1,tol);FB=add(FB,scale(bn,co[n+1],tol),1,tol);ap,ac=ac,an;bp,bc=bc,bn
 return FA,FB
def pm(F,G,K1,K2,tol=2e-9):
 A,B=F;C,D=G;return add(mul(A,C,tol),mul(mul(B,D,tol),K2,tol),-1,tol),add(add(mul(A,D,tol),mul(B,C,tol),1,tol),mul(mul(B,D,tol),K1,tol),1,tol)
def pa(F,G,s=1,tol=2e-9):return add(F[0],G[0],s,tol),add(F[1],G[1],s,tol)
def sm(s,F,tol=2e-9):return mul(s,F[0],tol),mul(s,F[1],tol)
def tr(F,K1,tol=2e-9):return add(scale(F[0],2,tol),mul(F[1],K1,tol),1,tol)
def det(F,K1,K2,tol=2e-9):
 A,B=F;r=mul(A,A,tol);r=add(r,mul(mul(A,B,tol),K1,tol),1,tol);return add(r,mul(mul(B,B,tol),K2,tol),1,tol)
def buildS(D,q,c,tol=2e-9):
 f=low(D,q,c);K1,K2=f['K1'],f['K2'];U=recur(K1,K2,Ucoef,tol);C=recur(K1,K2,Ccoef,tol);T=recur(K1,K2,Tcoef,tol);T7=recur(K1,K2,T7coef,tol)
 CC=sm(det(C,K1,K2,tol),C,tol);TC=pa(sm(tr(T,K1,tol),C,tol),pm(C,T,K1,K2,tol),-1,tol);t7=tr(T7,K1,tol);inner=(add(t7,T7[0],-1,tol),scale(T7[1],-1,tol));TT=sm(det(T,K1,K2,tol),inner,tol);return pa(pa(pa(U,CC,-acc,tol),TC,1,tol),TT,-rho*at,tol),f
def integ(A):
 n0,n1,n2=A.shape;M0=np.array([math.pi if n==0 else 2*math.sin(n*math.pi/2)/n for n in range(n0)]);M1=np.array([math.pi if n==0 else 2*math.sin(n*math.pi/2)/n for n in range(n1)]);Z=np.array([0 if n%2 else 2/(1-n*n) for n in range(n2)],float);return np.einsum('ijk,i,j,k->',A,M0,M1,Z,optimize=True)
def concrete(D,q,c,tol=2e-9):
 S,f=buildS(D,q,c,tol);A,B=S;Syy=add(A,mul(B,f['Yyy'],tol),1,tol);iS=integ(Syy);Pc=-c['fc']*c['b']*c['tc']/(2*math.pi**2)*iS;trs=tr(S,f['K1'],tol);gm=add(f['Gq'],scale(f['I1q'],lc,tol),-1,tol);sxq=add(mul(A,f['I1q'],tol),scale(mul(B,gm,tol),1/lh,tol),1,tol);Q=add(scale(sxq,1.18,tol),scale(mul(f['I1q'],trs,tol),.18,tol),-1,tol);iQ=integ(Q);Rq=c['fc']*c['eps0']*c['b']*c['ell']*c['tc']/(2*math.pi**2)*iQ;return Pc,Rq,iS,iQ
def steel_el(D,q,c,nuc=.18,nus=.3,q0=.0025):
 b,L,t,ts,e0,Es=c['b'],c['ell'],c['tc'],c['ts'],c['eps0'],c['Es'];k=b/L;M=math.pi**2/e0*(q0*q+.5*q*q);Mq=math.pi**2/e0*(q0+q);B=math.pi**2/(e0*b)*q;Bq=math.pi**2/(e0*b);z1=t/2;z2=z1+ts;Z0=2*ts;Z2=2*(z2**3-z1**3)/3;sy=math.pi**2*(D*nuc*nus-D+M*(k*k+nus)/4);Ps=-(Es*e0/(1-nus*nus))*(b/math.pi**2)*Z0*sy;dt=(k*k*nuc*nus-k*k+nuc-nus);ix=math.pi**2/576*(144*B*Bq*(k*k+1)**2*Z2+(144*D*Mq*dt+M*Mq*(81*k**4+18*k*k+81))*Z0);Rq=(Es*e0**2/(1-nus*nus))*(b*L/math.pi**2)*ix;return Ps,Rq
def stress_center(D,q,c,nuc=.18,nus=.3,q0=.0025):
 b,L,t,ts,e0,Es=c['b'],c['ell'],c['tc'],c['ts'],c['eps0'],c['Es'];k=b/L;z=-(t/2+ts);chi=q0*q+.5*q*q;ex=e0*nuc*D+z*math.pi**2*q/b;ey=-e0*D+z*math.pi**2*q*k*k/b;fac=Es/(1-nus*nus);sx=fac*(ex+nus*ey);sy=fac*(nus*ex+ey);return math.sqrt(sx*sx-sx*sy+sy*sy)
def total(D,q,c):
 Pc,Rc,*_=concrete(D,q,c);Ps,Rs=steel_el(D,q,c);vm=stress_center(D,q,c);a=min(1,c['fy']/vm) if vm>0 else 1;return Pc+a*Ps,Rc+a*Rs,Pc,a*Ps,a,vm
def solveq(D,c,qg):
 def f(q):return total(D,q,c)[1]
 r=root_scalar(f,x0=qg,x1=qg*1.01+1e-7,method='secant',xtol=2e-9,rtol=1e-7,maxiter=8)
 if r.converged:return r.root
 raise RuntimeError('q root fail')
def set_compiler(la_new,lb_new,ngrid=5001):
 global lc,lh,Ucoef,Ccoef,Tcoef,T7coef
 from scipy.optimize import linprog
 lc=(la_new+lb_new)/2;lh=(lb_new-la_new)/2
 th=(np.arange(49)+.5)*np.pi/49;lam=lc+lh*np.cos(th);V=chebvander((lam-lc)/lh,48);xi0=-lc/lh;E=np.eye(49)
 vr=np.array([chebval(xi0,E[n]) for n in range(49)]);dr=np.array([chebval(xi0,chebder(E[n]))/lh for n in range(49)]);A=np.vstack([vr,dr]);U,C,T,T7=targets(lam)
 def cl(v,b):
  H=V.T@V;K=np.block([[H,A.T],[A,np.zeros((2,2))]]);return np.linalg.solve(K,np.r_[V.T@v,b])[:49]
 Ucoef=cl(U,[0,kappa]);Ccoef=cl(C,[0,0]);T7coef=cl(T7,[0,0])
 lg=np.linspace(la_new,lb_new,ngrid);Vg=chebvander((lg-lc)/lh,48);tg=targets(lg)[2];cc=np.r_[np.zeros(49),1.];Aub=np.vstack([np.c_[Vg,-np.ones(ngrid)],np.c_[-Vg,-np.ones(ngrid)]]);bub=np.r_[tg,-tg];res=linprog(cc,A_ub=Aub,b_ub=bub,A_eq=np.c_[A,np.zeros(2)],b_eq=[0,0],bounds=[(None,None)]*49+[(0,None)],method='highs');Tcoef=res.x[:49]
 return res.x[-1]

if __name__ == "__main__":
    # Final accepted checkpoint states are persisted in the companion RESULT.csv/PARAMS.json.
    # Use total(D,q,case) to reproduce any standard-interval state.
    # For Z2 call set_compiler(-1.35,0.15,6001) first.
    # For Z6 call set_compiler(-1.15,0.23,3001) first.
    print("NZ-SCCM coefficient-space D15 kernel loaded. See companion RESULT.csv and CONNECTED_BRANCH__KEYPOINTS.csv.")
