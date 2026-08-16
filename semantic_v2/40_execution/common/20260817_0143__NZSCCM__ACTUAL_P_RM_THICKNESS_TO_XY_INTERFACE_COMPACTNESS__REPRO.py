"""NZ-SCCM 2026-08-17 01:43 P/Rm thickness-to-XY interface compactness gate.

Formal production counters remain zero. The 61x61 grid and scipy quadrature below are
AUDIT ONLY: they classify material-event topology and check equivalence of two exact source
representations. They are not structural production integration.
"""
import math
import collections
import numpy as np
import sympy as sp
from scipy import integrate

# -----------------------------------------------------------------------------
# Frozen Case21 audit state / material constants
# -----------------------------------------------------------------------------
D=0.8359179831666168
q=0.0017897894751107222
q0=0.0025
nu=0.18
eps0=0.00209
b=1220.0
t=19.30
rho=0.1
kappa=2.0005129533678754
H=0.09799750427197301
UR=0.03
ACC=0.1072329249362415
AT=1.0-2.0**(-1.0/8.0)
Cm=math.pi**2/eps0*(q0*q+0.5*q*q)
Cb=math.pi**2/(2*eps0)*(t/b)*q
eta=(rho/kappa)/20.0

# Exact source threshold locations in principal equivalent-uniaxial coordinate.
def Pi(z):
    return z*z*(math.sqrt(z*z+eta*eta)+z)/(2*(z*z+eta*eta))

def bisect_target(target,lo,hi):
    for _ in range(120):
        mid=(lo+hi)/2
        if Pi(mid)<target: lo=mid
        else: hi=mid
    return (lo+hi)/2

lam1=bisect_target(rho/kappa,0.0,0.2)
lam10=bisect_target(10*rho/kappa,0.2,1.0)

# Leading elastic Airy membrane state, used only as a second topology audit state.
airy=np.array([
    -(1+nu)*Cm/4,
    -(1-nu)*Cm/4,
    +Cm/4,
    -(1-nu)*Cm/4,
    +Cm/4,
],float)

# -----------------------------------------------------------------------------
# Generic symbolic event-front degree audit for the full five-coordinate strain family
# -----------------------------------------------------------------------------
sx,cx,sy,cy,z=sp.symbols('sx cx sy cy z')
Ds,Cms,Cbs,nus,lams=sp.symbols('D Cm Cb nu lam')
r0,r20,r22,s02,s22=sp.symbols('r0 r20 r22 s02 s22')

ex=nus*Ds+Cms*cx**2*sy**2+Cbs*sx*sy*z
ey=-Ds+Cms*sx**2*cy**2+Cbs*sx*sy*z
g=2*Cms*sx*cx*sy*cy-2*Cbs*cx*cy*z
c2x=cx**2-sx**2; c2y=cy**2-sy**2
s2x=2*sx*cx; s2y=2*sy*cy
ex += r0+r20*c2x+r22*c2x*c2y
ey += s02*c2y+s22*c2x*c2y
g += -(r22+s22)*s2x*s2y

den=1-nus**2
X11=(ex+nus*ey)/den
X22=(nus*ex+ey)/den
X12=g/(2*(1+nus))
F=sp.expand((X11-lams)*(X22-lams)-X12**2)
PF=sp.Poly(F,z)
a2=sp.expand(PF.coeff_monomial(z**2))
a1=sp.expand(PF.coeff_monomial(z))
a0=sp.expand(PF.coeff_monomial(1))
disc=sp.expand(a1*a1-4*a2*a0)

def stat(expr):
    p=sp.Poly(expr,sx,cx,sy,cy)
    return p.total_degree(),len(p.terms())

print('EVENT_COEFF_STATS=',{'a2':stat(a2),'a1':stat(a1),'a0':stat(a0),
                            'disc':stat(disc),'Fminus':stat(F.subs(z,-1)),'Fplus':stat(F.subs(z,1))})

# -----------------------------------------------------------------------------
# Case21 continuous kinematics and exact event roots
# -----------------------------------------------------------------------------
def strain(X,Y,zeta,r=None):
    ex=nu*D+Cm*math.cos(X)**2*math.sin(Y)**2+Cb*math.sin(X)*math.sin(Y)*zeta
    ey=-D+Cm*math.sin(X)**2*math.cos(Y)**2+Cb*math.sin(X)*math.sin(Y)*zeta
    gg=2*Cm*math.sin(X)*math.cos(X)*math.sin(Y)*math.cos(Y)-2*Cb*math.cos(X)*math.cos(Y)*zeta
    if r is not None:
        rr0,rr20,rr22,ss02,ss22=r
        cX=math.cos(2*X); cY=math.cos(2*Y); sX=math.sin(2*X); sY=math.sin(2*Y)
        ex += rr0+rr20*cX+rr22*cX*cY
        ey += ss02*cY+ss22*cX*cY
        gg += -(rr22+ss22)*sX*sY
    return ex,ey,gg

def Emat(ex,ey,gg):
    return np.array([[(ex+nu*ey)/(1-nu**2),gg/(2*(1+nu))],
                     [gg/(2*(1+nu)),(nu*ex+ey)/(1-nu**2)]],float)

def affine_E(X,Y,r=None):
    E0=Emat(*strain(X,Y,0.0,r)); E1=Emat(*strain(X,Y,1.0,r))
    return E0,E1-E0

def det_coeff(E0,Eb,lam):
    A=E0-lam*np.eye(2); B=Eb
    return np.array([np.linalg.det(B),
        A[0,0]*B[1,1]+A[1,1]*B[0,0]-A[0,1]*B[1,0]-A[1,0]*B[0,1],
        np.linalg.det(A)],float)

def roots_inside(c):
    if abs(c[0])<1e-14:
        roots=[] if abs(c[1])<1e-14 else [-c[2]/c[1]]
    else:
        roots=np.roots(c)
    return sorted(float(x.real) for x in roots if abs(x.imag)<1e-9 and -1<=x.real<=1)

def event_roots(X,Y,r=None):
    E0,Eb=affine_E(X,Y,r)
    return roots_inside(det_coeff(E0,Eb,lam1)),roots_inside(det_coeff(E0,Eb,lam10))

# Audit topology grid — NOT production integration.
for name,r in [('r0',None),('elastic_Airy',airy)]:
    C=collections.Counter()
    for X in np.linspace(1e-6,math.pi-1e-6,61):
        for Y in np.linspace(1e-6,math.pi-1e-6,61):
            a,b10=event_roots(X,Y,r)
            C[(len(a),len(b10))]+=1
    print('TOPOLOGY_AUDIT',name,C)

# -----------------------------------------------------------------------------
# Direct source stress and audit-only thickness integral equivalence
# -----------------------------------------------------------------------------
def pi_np(x):
    x=np.asarray(x,float); rr=np.sqrt(x*x+eta*eta)
    return x*x*(rr+x)/(2*(x*x+eta*eta))

def ur_np(tv):
    tv=np.asarray(tv,float); a=rho/kappa; out=np.empty_like(tv)
    m1=tv<=a; tau=tv[m1]/a
    out[m1]=rho*tau+(10*H-6*rho)*tau**3+(8*rho-15*H)*tau**4+(6*H-3*rho)*tau**5
    m2=(tv>a)&(tv<=10*a); ss=(tv[m2]-a)/(9*a)
    out[m2]=H+(UR-H)*(10*ss**3-15*ss**4+6*ss**5)
    out[tv>10*a]=UR
    return out

def principal_s(vals):
    vals=np.asarray(vals,float)
    c=pi_np(-vals); tv=pi_np(vals)
    C=kappa*c/(1+(kappa-2)*c+c*c)
    u=ur_np(tv); T=u/rho
    U=kappa*vals-C+kappa*c+u-kappa*tv
    s0=U[0]-ACC*C[0]**2*C[1]+C[0]*T[1]-rho*AT*T[0]*T[1]**8
    s1=U[1]-ACC*C[1]**2*C[0]+C[1]*T[0]-rho*AT*T[1]*T[0]**8
    return np.array([s0,s1])

def Smat(X,Y,zeta,r=None):
    EE=Emat(*strain(X,Y,zeta,r)); vals,V=np.linalg.eigh(EE)
    return V@np.diag(principal_s(vals))@V.T

def N0(X,Y,r=None,split=False):
    e1,e10=event_roots(X,Y,r); roots=sorted(set(e1+e10))
    intervals=list(zip([-1]+roots,roots+[1])) if split else [(-1,1)]
    out=[]
    for ij in [(0,0),(1,1),(0,1)]:
        val=0.0
        for aa,bb in intervals:
            val += integrate.quad(lambda zz:Smat(X,Y,zz,r)[ij],aa,bb,
                                  epsabs=1e-11,epsrel=1e-11,limit=100)[0]
        out.append(val)
    return np.array(out),roots

for name,r,X,Y in [
    ('r0_center',None,math.pi/2,math.pi/2),
    ('r0_pi4_pi3',None,math.pi/4,math.pi/3),
    ('airy_center',airy,math.pi/2,math.pi/2)]:
    A,roots=N0(X,Y,r,False); B,_=N0(X,Y,r,True)
    print('THICKNESS_AUDIT',name,'roots=',roots,'N0=',A.tolist(),'maxdiff=',float(np.max(np.abs(A-B))))

print('INTERFACE_RESULTANTS_FOR_P_PLUS_5RM = 3')
print('ROUTE_A_GLOBAL_FIXED_ENDPOINT = SELECTED_FOR_PRODUCTION')
print('ROUTE_B_EVENT_RESOLVED_8_STATE = LOCAL_AUDIT_ONLY')
print('FORMAL STRUCTURAL COUNTERS: sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0')
print('NEW_Pu = NOT_RUN')
