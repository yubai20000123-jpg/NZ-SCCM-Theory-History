import numpy as np
from numpy.polynomial.chebyshev import chebfit, chebval

# Frozen material-only reference constants
kappa=2.0005129533678754
rho=0.1
xcr=rho/kappa
eta_pi0=xcr/20.0
eta_r0=0.05
m_t=-7.0/90.0
a_cc=0.1072329249362415
a_t=1.0-2.0**(-1.0/8.0)
LAM_MIN=-2.4390243902439024
LAM_MAX=0.7317073170731706


def Pi_eta(z,eta):
    z=np.asarray(z)
    return z*z*(np.sqrt(z*z+eta*eta)+z)/(2.0*(z*z+eta*eta))


def H(r,r0,eta):
    r=np.asarray(r)
    return 0.5*((r-r0)+np.sqrt((r-r0)**2+eta**2))-0.5*((-r0)+np.sqrt(r0**2+eta**2))


def primitives(lam,k_pi=1.0,k_H=1.0,alpha_T=1.0):
    c=Pi_eta(-lam,eta_pi0*k_pi)
    t=Pi_eta(lam,eta_pi0*k_pi)
    C=kappa*c/(1.0+(kappa-2.0)*c+c*c)
    r=t/xcr
    T=(r+(m_t-1.0)*H(r,1.0,eta_r0*k_H)-m_t*H(r,10.0,eta_r0*k_H))*alpha_T
    U=kappa*lam-C+kappa*c+rho*T-kappa*t
    return U,C,T


def current_map(l1,l2,k_pi=1.0,k_H=1.0,alpha_T=1.0):
    U1,C1,T1=primitives(l1,k_pi,k_H,alpha_T)
    U2,C2,T2=primitives(l2,k_pi,k_H,alpha_T)
    s1=U1-a_cc*C1*C1*C2+C1*T2-rho*a_t*T1*T2**8
    s2=U2-a_cc*C2*C2*C1+C2*T1-rho*a_t*T2*T1**8
    return s1,s2


_lam_t=np.linspace(0.0,0.8,200001)
_ft_ref=float(current_map(_lam_t,0.0)[0].max())


def anchor_alpha(k_pi,k_H):
    lo,hi=0.5,1.5
    for _ in range(60):
        mid=0.5*(lo+hi)
        p=float(current_map(_lam_t,0.0,k_pi,k_H,mid)[0].max())
        if p<_ft_ref: lo=mid
        else: hi=mid
    return 0.5*(lo+hi)


def curvature_peaks(k_pi,k_H,alpha_T):
    x=np.linspace(-0.02,0.62,320001)
    T=primitives(x,k_pi,k_H,alpha_T)[2]
    h=x[1]-x[0]
    d2=np.gradient(np.gradient(T,h),h)
    out=[]
    for lo,hi in [(0.0,0.01),(0.03,0.08),(0.45,0.56)]:
        m=(x>=lo)&(x<=hi)
        out.append(float(np.max(np.abs(d2[m]))))
    return out


def jacobian(l1,l2,k_pi,k_H,alpha_T):
    h=1e-30
    s1,s2=current_map(l1+1j*h,l2,k_pi,k_H,alpha_T)
    d11,d21=np.imag(s1)/h,np.imag(s2)/h
    s1,s2=current_map(l1,l2+1j*h,k_pi,k_H,alpha_T)
    d12,d22=np.imag(s1)/h,np.imag(s2)/h
    return np.array([[d11,d12],[d21,d22]],float)


def cheb_screen(k,alpha,deg,lo,hi,nfit=12001,nval=200001):
    lf=np.linspace(lo,hi,nfit)
    xf=(2.0*lf-(hi+lo))/(hi-lo)
    Tf=primitives(lf,k,k,alpha)[2]
    co=chebfit(xf,Tf,deg)
    lv=np.linspace(lo,hi,nval)
    xv=(2.0*lv-(hi+lo))/(hi-lo)
    Tv=primitives(lv,k,k,alpha)[2]
    P=chebval(xv,co)
    scale=max(float(np.max(np.abs(Tv))),1e-15)
    e=np.abs(P-Tv)/scale
    return float(e.max()),float(np.percentile(e,95)),float(np.max(np.abs(P-Tv)))


if __name__=='__main__':
    base_curv=np.array(curvature_peaks(1.0,1.0,1.0))
    print('ft_ref=',_ft_ref)
    print('base_curvature=',base_curv)
    for k in [1.0,1.25,1.5,1.75,2.0,4.0,8.0]:
        a=1.0 if k==1.0 else anchor_alpha(k,k)
        curv=np.array(curvature_peaks(k,k,a))
        print('k=',k,'alpha=',a,'curvature_ratio=',curv/base_curv)
    for k in [1.0,1.25,1.5,2.0]:
        a=1.0 if k==1.0 else anchor_alpha(k,k)
        print('full n32',k,cheb_screen(k,a,32,LAM_MIN,LAM_MAX))
        print('full n64',k,cheb_screen(k,a,64,LAM_MIN,LAM_MAX))
    print('lambda+ n32',cheb_screen(1.0,1.0,32,-0.1051,0.13584,4001,100001))
    print('lambda- n6',cheb_screen(1.0,1.0,6,-0.86569,-0.62473,4001,100001))
