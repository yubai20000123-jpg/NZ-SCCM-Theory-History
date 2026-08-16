"""NZ-SCCM Case21 Airy-scalar current-R10 continuation reproducer.

This script reproduces the direct-source continuum AUDIT result for the selected
one-coordinate Airy membrane closure:

    r = lambda * M * a(nu)
    Rq = 0
    RA = a^T Rm = 0

The Gauss-Legendre grids below are audit executors only. They are NOT the formal
zero-spatial-quadrature production operator. Formal project counters remain zero.
"""
import math
import numpy as np
from scipy.optimize import root
from numpy.polynomial.legendre import leggauss

# Case21 frozen data
fc=21.23; E0=20321.0; eps0=0.00209; nu=0.18
b=ell=1220.0; tp=19.30; q0=1/400
Es=200000.0; rsx=rsy=0.00375; eps_yield=0.00265

# Frozen R10 source data
kappa=E0*eps0/fc
rho=0.1; eta=(rho/kappa)/20.0
H=0.09799750427197301; UR=0.03
ACC=0.1072329249362415; AT=1.0-2.0**(-1.0/8.0)

A_AIRY=np.array([-(1+nu)/4, -(1-nu)/4, .25, -(1-nu)/4, .25],float)


def pi_eta(z):
    z=np.asarray(z,float)
    rr=np.sqrt(z*z+eta*eta)
    return z*z*(rr+z)/(2*(z*z+eta*eta))


def ur_t(t):
    t=np.asarray(t,float); a=rho/kappa
    out=np.empty_like(t)
    m1=t<=a; tau=t[m1]/a
    out[m1]=(rho*tau +(10*H-6*rho)*tau**3 +(8*rho-15*H)*tau**4 +(6*H-3*rho)*tau**5)
    m2=(t>a)&(t<=10*a); s=(t[m2]-a)/(9*a)
    out[m2]=H+(UR-H)*(10*s**3-15*s**4+6*s**5)
    out[t>10*a]=UR
    return out


def principal_stresses(lam1,lam2):
    c1=pi_eta(-lam1); c2=pi_eta(-lam2)
    t1=pi_eta(lam1);  t2=pi_eta(lam2)
    C1=kappa*c1/(1+(kappa-2)*c1+c1*c1)
    C2=kappa*c2/(1+(kappa-2)*c2+c2*c2)
    u1=ur_t(t1); u2=ur_t(t2)
    T1=u1/rho; T2=u2/rho
    U1=kappa*lam1-C1+kappa*c1+u1-kappa*t1
    U2=kappa*lam2-C2+kappa*c2+u2-kappa*t2
    s1=U1-ACC*C1*C1*C2+C1*T2-rho*AT*T1*T2**8
    s2=U2-ACC*C2*C2*C1+C2*T1-rho*AT*T2*T1**8
    return s1,s2


def global_stress(ex,ey,g):
    x11=(ex+nu*ey)/(1-nu**2)
    x22=(nu*ex+ey)/(1-nu**2)
    x12=g/(2*(1+nu))
    mu=(x11+x22)/2; dd=(x11-x22)/2
    rr=np.sqrt(dd*dd+x12*x12)
    lp=mu+rr; lm=mu-rr
    sp,sm=principal_stresses(lp,lm)
    av=(sp+sm)/2; df=(sp-sm)/2
    fac=np.zeros_like(rr); mask=rr>1e-14; fac[mask]=df[mask]/rr[mask]
    return fc*(av+fac*dd), fc*(av-fac*dd), fc*(fac*x12)


def steel_sigma(eps):
    return np.clip(Es*eps,-Es*eps_yield,Es*eps_yield)


class Oracle:
    def __init__(self,nxy=64,nz=36):
        gx,wx=leggauss(nxy); gz,wz=leggauss(nz)
        X=(gx+1)*math.pi/2; W=wx*math.pi/2
        self.X3,self.Y3,self.Z3=np.meshgrid(X,X,gz,indexing='ij')
        self.W3=W[:,None,None]*W[None,:,None]*wz[None,None,:]
        self.X2,self.Y2=np.meshgrid(X,X,indexing='ij')
        self.W2=W[:,None]*W[None,:]
        self.c2x=np.cos(2*self.X3); self.c2y=np.cos(2*self.Y3)
        self.s2x=np.sin(2*self.X3); self.s2y=np.sin(2*self.Y3)
        self.c2xy=self.c2x*self.c2y; self.sb=-(self.s2x*self.s2y)
        self.c2X=np.cos(2*self.X2); self.c2Y=np.cos(2*self.Y2); self.c2XY=self.c2X*self.c2Y

    def kin(self,D,q,r,three=True):
        r0,r20,r22,s02,s22=r
        M=math.pi**2/eps0*(q0*q+.5*q*q)
        B=math.pi**2/(2*eps0)*(tp/b)*q
        if three:
            X,Y,Z=self.X3,self.Y3,self.Z3
            ex=nu*D+M*np.cos(X)**2*np.sin(Y)**2+B*np.sin(X)*np.sin(Y)*Z
            ey=-D+M*np.sin(X)**2*np.cos(Y)**2+B*np.sin(X)*np.sin(Y)*Z
            g=2*M*np.sin(X)*np.cos(X)*np.sin(Y)*np.cos(Y)-2*B*np.cos(X)*np.cos(Y)*Z
            ex += r0+r20*self.c2x+r22*self.c2xy
            ey += s02*self.c2y+s22*self.c2xy
            g += -(r22+s22)*self.s2x*self.s2y
        else:
            X,Y=self.X2,self.Y2
            ex=nu*D+M*np.cos(X)**2*np.sin(Y)**2
            ey=-D+M*np.sin(X)**2*np.cos(Y)**2
            g=2*M*np.sin(X)*np.cos(X)*np.sin(Y)*np.cos(Y)
            ex += r0+r20*self.c2X+r22*self.c2XY
            ey += s02*self.c2Y+s22*self.c2XY
            g += -(r22+s22)*np.sin(2*X)*np.sin(2*Y)
        return ex,ey,g,M,B

    def evaluate(self,D,q,r):
        ex,ey,g,M,B=self.kin(D,q,r,True)
        sx,sy,txy=global_stress(ex,ey,g)
        Cvol=eps0*b*ell*tp/(2*math.pi**2)
        Pc=-b*tp/(2*math.pi**2)*np.sum(sy*self.W3)/1000
        Rc=np.array([
            Cvol*np.sum(sx*self.W3),
            Cvol*np.sum(sx*self.c2x*self.W3),
            Cvol*np.sum((sx*self.c2xy+txy*self.sb)*self.W3),
            Cvol*np.sum(sy*self.c2y*self.W3),
            Cvol*np.sum((sy*self.c2xy+txy*self.sb)*self.W3)
        ])/1000

        ex0,ey0,_,_,_=self.kin(D,q,r,False)
        ssx=steel_sigma(eps0*ex0); ssy=steel_sigma(eps0*ey0)
        Ps=-rsy*tp*b/math.pi**2*np.sum(ssy*self.W2)/1000
        Svol=eps0*b*ell*tp/math.pi**2
        Rs=np.array([
            rsx*Svol*np.sum(ssx*self.W2),
            rsx*Svol*np.sum(ssx*self.c2X*self.W2),
            rsx*Svol*np.sum(ssx*self.c2XY*self.W2),
            rsy*Svol*np.sum(ssy*self.c2Y*self.W2),
            rsy*Svol*np.sum(ssy*self.c2XY*self.W2)
        ])/1000

        X,Y,Z=self.X3,self.Y3,self.Z3
        Mq=math.pi**2/eps0*(q0+q); Bq=math.pi**2/(2*eps0)*(tp/b)
        exq=Mq*np.cos(X)**2*np.sin(Y)**2+Bq*np.sin(X)*np.sin(Y)*Z
        eyq=Mq*np.sin(X)**2*np.cos(Y)**2+Bq*np.sin(X)*np.sin(Y)*Z
        gq=2*Mq*np.sin(X)*np.cos(X)*np.sin(Y)*np.cos(Y)-2*Bq*np.cos(X)*np.cos(Y)*Z
        Rqc=Cvol*np.sum((sx*exq+sy*eyq+txy*gq)*self.W3)/1000
        X2,Y2=self.X2,self.Y2
        exq0=Mq*np.cos(X2)**2*np.sin(Y2)**2
        eyq0=Mq*np.sin(X2)**2*np.cos(Y2)**2
        Rqs=Svol*np.sum((rsx*ssx*exq0+rsy*ssy*eyq0)*self.W2)/1000

        return dict(Pc=Pc,Ps=Ps,P=Pc+Ps,Rm=Rc+Rs,Rq=Rqc+Rqs,M=M,B=B,
                    steel=(float((eps0*ex0).min()),float((eps0*ex0).max()),
                           float((eps0*ey0).min()),float((eps0*ey0).max())))


def solve_at_D(oracle,D,x0):
    def F(x):
        q,lam=x
        M=math.pi**2/eps0*(q0*q+.5*q*q)
        ev=oracle.evaluate(D,q,lam*M*A_AIRY)
        return np.array([ev['Rq']/1000, np.dot(A_AIRY,ev['Rm'])/100])
    sol=root(F,np.asarray(x0,float),method='hybr',tol=1e-11,options={'maxfev':300})
    q,lam=sol.x; M=math.pi**2/eps0*(q0*q+.5*q*q)
    ev=oracle.evaluate(D,q,lam*M*A_AIRY)
    return sol,ev


def main():
    print('FORMAL COUNTERS: sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0')
    print('NOTE: grids below are audit-only and do not change those formal counters')
    D=0.7887924801
    guess=[0.00180836,0.08624]
    for nxy,nz in [(64,36),(80,44),(96,52),(112,60),(128,68),(144,76)]:
        o=Oracle(nxy,nz); sol,ev=solve_at_D(o,D,guess); guess=sol.x
        q,lam=sol.x; M=ev['M']; r=lam*M*A_AIRY
        print(nxy,nz,'D',D,'q',q,'lambda',lam,'P',ev['P'],'Pc',ev['Pc'],'Ps',ev['Ps'],
              'Rq',ev['Rq'],'RA',np.dot(A_AIRY,ev['Rm']),'r',r.tolist(),'steel',ev['steel'])

if __name__=='__main__':
    main()
