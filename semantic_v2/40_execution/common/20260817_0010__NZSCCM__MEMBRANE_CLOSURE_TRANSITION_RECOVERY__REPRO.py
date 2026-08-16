"""NZ-SCCM membrane closure transition recovery reproducer.

Purpose
-------
1) Reproduce the exact elastic Airy leading direction and K-projections of
   the previously stored Case21 membrane points.
2) Reproduce the 19:12 legacy-N48 projected Newton diagnostic from the
   recorded R/J matrix.
3) Provide a direct frozen-R10 Gauss-Legendre AUDIT ORACLE for the same
   historical Case21 D,q state, showing:
   - positive scalar Airy projected root;
   - full five-coordinate Rm=0 root;
   - loss of internal Krr symmetric-part stability.

The Gauss-Legendre part is explicitly audit-only. It is NOT a formal
structural production integrator. Formal project counters remain zero.
"""
import numpy as np, math
from numpy.polynomial.legendre import leggauss
from scipy.optimize import root, brentq

# ---- exact elastic five-term coupling ----
nu=.18
Kbar=np.array([
 [1,0,0,0,0],
 [0,.5,0,0,0],
 [0,0,(3-nu)/8,0,(1+nu)/8],
 [0,0,0,.5,0],
 [0,0,(1+nu)/8,0,(3-nu)/8]],float)
a=np.array([-(1+nu)/4,-(1-nu)/4,.25,-(1-nu)/4,.25])
assert np.all(np.linalg.eigvalsh(Kbar)>0)
assert abs(a@Kbar@a-.19155)<1e-12

def Knorm(x): return float(np.sqrt(x@Kbar@x))
def proj(M,r):
    lam=float((a@Kbar@r)/(M*(a@Kbar@a)))
    rp=r-lam*M*a
    return lam,Knorm(rp)/Knorm(r)

p1=(.0012041861829080321,np.array([-.0004765646208971642,-.000232281931854189,.0002805628349612065,-.0002432861950486819,.00030341587937381494]))
p2=(.002455595353381085,np.array([-.0009851269073948984,-.0004459452528374698,.0006055135286393538,-.0003630828054164307,.0005376886688340636]))
bad=(.029575053233322175,np.array([-.012475802483156403,-.007141864103343101,.04699488414266459,.041946118067216,-.09983629747628982]))
print('point1 projection',proj(*p1))
print('point2 projection',proj(*p2))
print('retracted peak projection',proj(*bad))

# ---- recorded 19:12 legacy-N48 diagnostic ----
Mhist=.02869338081034484
Rlegacy=np.array([2.69233687,.13819441,-.31339370,-15.52815375,3.00791537])
Jlegacy=np.array([
 [448.483939,16.366324,-16.407897,1.448734,-2.781585],
 [16.464411,223.457600,2.909393,-3.059928,.555910],
 [-29.372389,-.411754,131.031918,1.413017,39.744523],
 [-602.844440,-272.711727,25.354833,117.628140,6.391122],
 [-286.584350,-327.662779,270.294124,4.492820,78.413268]])
adR=float(a@Rlegacy); dR=float(Mhist*(a@Jlegacy@a))
print('legacy N48 a.R=',adR,'projected derivative=',dR,'one-Newton lambda=',1-adR/dR)

# ---- frozen direct R10 audit oracle ----
fc=21.23; E0=20321.; eps0=.00209; b=1220.; tp=19.30; q0=.0025
Es=200000.; rsx=rsy=.00375
kappa=E0*eps0/fc; rho=.1; xcr=rho/kappa; eta0=xcr/20
ur=.03; hh=.09799750427197301; acc=.1072329249362415; at=1-2**(-1/8)

def Pi(z):
    z=np.asarray(z,float); return z*z*(np.sqrt(z*z+eta0*eta0)+z)/(2*(z*z+eta0*eta0))
def uR(t):
    t=np.asarray(t,float); rr=t/xcr; out=np.empty_like(rr)
    m=rr<=1; r=rr[m]
    out[m]=rho*r+(10*hh-6*rho)*r**3+(8*rho-15*hh)*r**4+(6*hh-3*rho)*r**5
    m2=(rr>1)&(rr<=10); s=(rr[m2]-1)/9
    out[m2]=hh+(ur-hh)*(10*s**3-15*s**4+6*s**5); out[rr>10]=ur
    return out
def scalar_targets(lam):
    c=Pi(-lam); t=Pi(lam); C=kappa*c/(1+(kappa-2)*c+c*c); u=uR(t); T=u/rho
    U=kappa*lam-C+kappa*c+u-kappa*t
    return U,C,T,T**7
def matfun(vals,vecs,fvals):
    return np.einsum('...ia,...a,...ja->...ij',vecs,fvals,vecs,optimize=True)
def concrete_S(Exx,Eyy,G):
    E=np.empty(Exx.shape+(2,2)); E[...,0,0]=Exx; E[...,1,1]=Eyy; E[...,0,1]=G; E[...,1,0]=G
    vals,vecs=np.linalg.eigh(E); Uv,Cv,Tv,T7v=scalar_targets(vals)
    U=matfun(vals,vecs,Uv); C=matfun(vals,vecs,Cv); T=matfun(vals,vecs,Tv); T7=matfun(vals,vecs,T7v)
    detC=C[...,0,0]*C[...,1,1]-C[...,0,1]*C[...,1,0]
    detT=T[...,0,0]*T[...,1,1]-T[...,0,1]*T[...,1,0]
    trT=T[...,0,0]+T[...,1,1]; trT7=T7[...,0,0]+T7[...,1,1]
    CT=np.einsum('...ik,...kj->...ij',C,T,optimize=True)
    I=np.zeros_like(U); I[...,0,0]=1; I[...,1,1]=1
    S=U-acc*detC[...,None,None]*C+trT[...,None,None]*C-CT-rho*at*detT[...,None,None]*(trT7[...,None,None]*I-T7)
    return S

def Rm_direct(D,q,r,nxy=28,nz=14):
    gx,wx=leggauss(nxy); gz,wz=leggauss(nz)
    X=(gx+1)*math.pi/2; W=wx*math.pi/2
    XX=X[:,None,None]; YY=X[None,:,None]; ZZ=gz[None,None,:]
    WW=W[:,None,None]*W[None,:,None]*wz[None,None,:]
    sx=np.sin(XX);cx=np.cos(XX);sy=np.sin(YY);cy=np.cos(YY)
    c2x=np.cos(2*XX);c2y=np.cos(2*YY);s2x=np.sin(2*XX);s2y=np.sin(2*YY);c2xy=c2x*c2y;s2xy=s2x*s2y
    Cm=math.pi**2/eps0*(q0*q+.5*q*q); Cb=math.pi**2*tp/(2*eps0*b)*q
    r0,r20,r22,s02,s22=r
    ex=nu*D+Cm*cx**2*sy**2+Cb*sx*sy*ZZ+r0+r20*c2x+r22*c2xy
    ey=-D+Cm*sx**2*cy**2+Cb*sx*sy*ZZ+s02*c2y+s22*c2xy
    g=2*Cm*sx*cx*sy*cy-2*Cb*cx*cy*ZZ-(r22+s22)*s2xy
    Exx=(ex+nu*ey)/(1-nu**2); Eyy=(nu*ex+ey)/(1-nu**2); G=g/(2*(1+nu))
    S=concrete_S(Exx,Eyy,G); sxx=S[...,0,0];syy=S[...,1,1];sxy=S[...,0,1]
    integ=lambda v:float(np.sum(WW*v))
    Rc=fc/2*np.array([integ(sxx),integ(sxx*c2x),integ(sxx*c2xy-sxy*s2xy),integ(syy*c2y),integ(syy*c2xy-sxy*s2xy)])
    X2=X[:,None];Y2=X[None,:];sx2=np.sin(X2);cx2=np.cos(X2);sy2=np.sin(Y2);cy2=np.cos(Y2)
    c2x2=np.cos(2*X2);c2y2=np.cos(2*Y2);c2xy2=c2x2*c2y2;WA=W[:,None]*W[None,:]
    ex0=nu*D+Cm*cx2**2*sy2**2+r0+r20*c2x2+r22*c2xy2
    ey0=-D+Cm*sx2**2*cy2**2+s02*c2y2+s22*c2xy2
    area=lambda v:float(np.sum(WA*v))
    Rs=np.array([rsx*Es*eps0*area(ex0),rsx*Es*eps0*area(ex0*c2x2),rsx*Es*eps0*area(ex0*c2xy2),rsy*Es*eps0*area(ey0*c2y2),rsy*Es*eps0*area(ey0*c2xy2)])
    return Rc+Rs

def jac_fd(fun,x,h=2e-5):
    x=np.asarray(x,float); J=np.zeros((len(x),len(x)))
    for j in range(len(x)):
        xp=x.copy();xm=x.copy();xp[j]+=h;xm[j]-=h;J[:,j]=(fun(xp)-fun(xm))/(2*h)
    return J

D=.8359179831666168; q=.0017897894751107222
# scalar Airy manifold audit
f=lambda lam: float(a@Rm_direct(D,q,lam*Mhist*a,36,18))
lam=brentq(f,0,.5,xtol=1e-10)
Rscalar=Rm_direct(D,q,lam*Mhist*a,50,24)
h=1e-4; dscalar=(f(lam+h)-f(lam-h))/(2*h)
print('direct R10 scalar lambda=',lam,'dR/dlambda=',dscalar,'Rm=',Rscalar,'norm=',np.linalg.norm(Rscalar))

# full five-coordinate audit root
sol=root(lambda r:Rm_direct(D,q,r,36,18)/10,Mhist*a,method='hybr',options={'xtol':1e-10,'maxfev':120})
r5=sol.x; Rhi=Rm_direct(D,q,r5,50,24); J5=jac_fd(lambda r:Rm_direct(D,q,r,32,16),r5)
print('direct R10 full root=',r5,'high-order residual norm=',np.linalg.norm(Rhi),'projection=',proj(Mhist,r5))
print('Krr raw eig=',np.linalg.eigvals(J5))
print('Krr sym eig=',np.linalg.eigvalsh((J5+J5.T)/2))

# low-q stored states: tangent sign audit
for name,Dp,qp,rp in [('p1',.016046306,1e-4,p1[1]),('p2',.031737797,2e-4,p2[1])]:
    Jp=jac_fd(lambda r:Rm_direct(Dp,qp,r,24,12),rp,1e-5)
    print(name,'Krr sym eig=',np.linalg.eigvalsh((Jp+Jp.T)/2))

print('FORMAL_spatial_sampling=0')
print('FORMAL_spatial_quadrature=0')
print('AUDIT_Gauss_oracle_only=YES')
print('NEW_Pu=NOT_RUN')
