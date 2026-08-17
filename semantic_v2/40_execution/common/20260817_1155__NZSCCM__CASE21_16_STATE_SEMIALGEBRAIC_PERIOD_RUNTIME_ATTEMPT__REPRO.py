"""NZ-SCCM Case21 2026-08-17 11:55 exact reduction / runtime-boundary reproducer.

This file does NOT compute formal Pu. It proves exact source identities, a no-spatial-
sampling Bernstein enclosure for the current peak and a nearby formal search box,
and the resulting 16-state current-branch algebraic bound. It also identifies the
non-analytic Foster-knot gluing that blocks a naive single analytic Pfaffian runtime.

No structural spatial/thickness numerical quadrature is used.
"""
import math, json
from math import comb
import numpy as np
import sympy as sp

fc=21.23; E0=20321.0; eps0=0.00209; nu=0.18
b=ell=1220.0; tp=19.30; q0=1/400
rho=0.1; H=0.09799750427197301; UR=0.03
kappa=E0*eps0/fc; eta=(rho/kappa)/20; a=rho/kappa
PEAK=dict(D=0.7887924801,q=0.0018083572562965242,lam=0.08623596353826937)
BOX=dict(D=(0.75,0.82),q=(0.00175,0.00187),lam=(0.0,0.15))


def pi_eta(x):
    return x*x*(math.sqrt(x*x+eta*eta)+x)/(2*(x*x+eta*eta))


def bisect_root(fun,lo,hi,n=100):
    flo=fun(lo)
    for _ in range(n):
        mid=(lo+hi)/2; fm=fun(mid)
        if flo*fm<=0: hi=mid
        else: lo=mid; flo=fm
    return (lo+hi)/2

lambda1=bisect_root(lambda x:pi_eta(x)-a,0.0,0.2)
lambda10=bisect_root(lambda x:pi_eta(x)-10*a,0.2,1.0)


def bernstein_coeffs(poly, vars_):
    P=sp.Poly(sp.expand(poly), *vars_)
    deg=P.degree_list(); pd={mon:float(coef) for mon,coef in P.terms()}
    shape=tuple(d+1 for d in deg); out=np.zeros(shape)
    for idx in np.ndindex(shape):
        s=0.0
        for mon,val in pd.items():
            if all(mon[i]<=idx[i] for i in range(len(vars_))):
                fac=1.0
                for i,n in enumerate(deg): fac*=comb(idx[i],mon[i])/comb(n,mon[i])
                s+=val*fac
        out[idx]=s
    return out,deg


def invariants(D,q,lam,U,V,W):
    M=sp.Float(math.pi**2/eps0)*(sp.Float(q0)*q+sp.Rational(1,2)*q*q)
    B=sp.Float(math.pi**2/(2*eps0)*(tp/b))*q
    CX=1-2*U**2; CY=1-2*V**2; zeta=2*W-1
    ex=sp.Float(nu)*D + M/4*(1+CX-CY-CX*CY-lam*(1+nu)-lam*(1-nu)*CX+lam*CX*CY)+B*U*V*zeta
    ey=-D + M/4*(1-CX+CY-CX*CY-lam*(1-nu)*CY+lam*CX*CY)+B*U*V*zeta
    trE=sp.expand((ex+ey)/(1-nu))
    diff=sp.expand((ex-ey)/(1+nu))
    h=(M*(1-lam)*U*V-B*zeta)/(1+nu)
    Delta=sp.expand(diff**2+4*(1-U**2)*(1-V**2)*h**2)
    return trE,Delta


def principal_bounds(trlo,trhi,dlo,dhi):
    glo=math.sqrt(dlo); ghi=math.sqrt(dhi)
    return dict(gap=(glo,ghi),
                lambda_plus=((trlo+glo)/2,(trhi+ghi)/2),
                lambda_minus=((trlo-ghi)/2,(trhi-glo)/2))

# exact conformal identity
x,e,w=sp.symbols('x e w', positive=True)
xw=2*e*w/(1-w**2); sw=e*(1+w**2)/(1-w**2)
pplus=sp.factor(xw**2*(sw+xw)/(2*(xw**2+e**2)))
pminus=sp.factor(xw**2*(sw-xw)/(2*(xw**2+e**2)))
rhs_plus=sp.factor(xw*w*(1+w)**2/(1+w**2)**2)
rhs_minus=sp.factor(xw*w*(1-w)**2/(1+w**2)**2)
assert sp.simplify(pplus-rhs_plus)==0 and sp.simplify(pminus-rhs_minus)==0

# current-peak Bernstein enclosure
U,V,W=sp.symbols('U V W', real=True)
tr,Delta=invariants(sp.Float(PEAK['D']),sp.Float(PEAK['q']),sp.Float(PEAK['lam']),U,V,W)
btr,dtr=bernstein_coeffs(tr,(U,V,W)); bde,dde=bernstein_coeffs(Delta,(U,V,W))
peak_bounds=principal_bounds(float(btr.min()),float(btr.max()),float(bde.min()),float(bde.max()))
peak_bounds.update(dict(tr=(float(btr.min()),float(btr.max())),Delta=(float(bde.min()),float(bde.max())),tr_degree=dtr,Delta_degree=dde))

# six-variable formal search-box Bernstein enclosure
Ud,Vd,Wd,sd,sq,sl=sp.symbols('Ud Vd Wd sd sq sl', real=True)
Db=BOX['D'][0]+(BOX['D'][1]-BOX['D'][0])*sd
qb=BOX['q'][0]+(BOX['q'][1]-BOX['q'][0])*sq
lb=BOX['lam'][0]+(BOX['lam'][1]-BOX['lam'][0])*sl
trb,Deb=invariants(Db,qb,lb,Ud,Vd,Wd)
btr6,dtr6=bernstein_coeffs(trb,(Ud,Vd,Wd,sd,sq,sl)); bde6,dde6=bernstein_coeffs(Deb,(Ud,Vd,Wd,sd,sq,sl))
box_bounds=principal_bounds(float(btr6.min()),float(btr6.max()),float(bde6.min()),float(bde6.max()))
box_bounds.update(dict(tr=(float(btr6.min()),float(btr6.max())),Delta=(float(bde6.min()),float(bde6.max())),tr_degree=dtr6,Delta_degree=dde6))

for BND in (peak_bounds,box_bounds):
    lplo,lphi=BND['lambda_plus']; lmlo,lmhi=BND['lambda_minus']
    BND['tplus_over_a_bounds']=(pi_eta(lplo)/a,pi_eta(lphi)/a)
    BND['tminus_over_a_bounds']=(pi_eta(lmlo)/a,pi_eta(lmhi)/a)

# one explicit witness of the physical first knot crossing
D0,q00,l0=PEAK['D'],PEAK['q'],PEAK['lam']
M0=math.pi**2/eps0*(q0*q00+.5*q00*q00); B0=math.pi**2/(2*eps0)*(tp/b)*q00

def center_lambda_plus(z):
    CX=CY=-1.0
    ex=nu*D0+M0/4*(1+CX-CY-CX*CY-l0*(1+nu)-l0*(1-nu)*CX+l0*CX*CY)+B0*z
    ey=-D0+M0/4*(1-CX+CY-CX*CY-l0*(1-nu)*CY+l0*CX*CY)+B0*z
    x11=(ex+nu*ey)/(1-nu**2); x22=(nu*ex+ey)/(1-nu**2)
    return max(x11,x22)
center_root=bisect_root(lambda z:center_lambda_plus(z)-lambda1,-1.0,1.0)
center_witness=dict(zeta_minus1=center_lambda_plus(-1),zeta_plus1=center_lambda_plus(1),zeta_lambda1=center_root)

# nonanalyticity of the frozen tensile source at the first knot
z,RH,HH,UU=sp.symbols('z RH HH UU')
low=RH*z+(10*HH-6*RH)*z**3+(8*RH-15*HH)*z**4+(6*HH-3*RH)*z**5
s=(z-1)/9
mid=HH+(UU-HH)*(10*s**3-15*s**4+6*s**5)
jumps=[sp.simplify(sp.diff(mid,z,n).subs(z,1)-sp.diff(low,z,n).subs(z,1)) for n in range(6)]
jump_num=[float(j.subs({RH:rho,HH:H,UU:UR})) for j in jumps]
A3=jump_num[3]/math.factorial(3)

# fixed one-domain rational coordinate map
r=sp.symbols('r', real=True)
Q=sp.expand(r*r+(1-r)**2)
sinR=sp.factor(2*r*(1-r)/Q); cosR=sp.factor((1-2*r)/Q); dR=sp.factor(2/Q)

out={
 'formal_counters':dict(N_formal_spatial_sampling=0,N_formal_spatial_quadrature=0,N_formal_spatial_subdomains=1,N_formal_thickness_quadrature=0),
 'constants':dict(kappa=kappa,eta=eta,a=a,lambda1=lambda1,lambda10=lambda10),
 'stable_conformal_identity':{
  'definition':'W=E*(sqrt(E^2+eta^2 I)+eta I)^(-1)',
  't':'pi_eta(E)=E*W*(I+W)^2*(I+W^2)^(-2)',
  'c':'pi_eta(-E)=E*W*(I-W)^2*(I+W^2)^(-2)',
  'scalar_symbolic_residual_t':str(sp.simplify(pplus-rhs_plus)),
  'scalar_symbolic_residual_c':str(sp.simplify(pminus-rhs_minus))},
 'peak_bernstein':peak_bounds,
 'formal_search_box':dict(bounds=BOX,bernstein=box_bounds),
 'first_knot_center_witness':center_witness,
 'tensile_knot_smoothness':dict(jumps_order_0_to_5=jump_num,A3_truncated_power=A3,C2=True,analytic=False),
 'current_branch_algebraic_field':{
  'generators':['g=sqrt(Delta_E)','splus=sqrt(lambda_plus^2+eta^2)','sminus=sqrt(lambda_minus^2+eta^2)','h1=sqrt((tplus-a)^2)'],
  'basis':'g^i*splus^j*sminus^k*h1^l, i,j,k,l in {0,1}',
  'dimension_bound':16,
  'conditions':['gap>0','tminus<a','tplus<10a','only first tensile knot active']},
 'single_domain_rationalization':{
  'coordinate':'r=tan(X/2)/(1+tan(X/2)) in [0,1]',
  'Q':'r^2+(1-r)^2','sinX':str(sinR),'cosX':str(cosR),'dX':str(dR),
  'zeta':'2*w-1, w in [0,1], dzeta=2 dw',
  'domain':'unit cube [0,1]^3, no XY or thickness subdivision'},
 'runtime_boundary':{
  'ordinary_single_analytic_pfaffian_across_first_knot':'BLOCKED: h1=|tplus-a| switches algebraic components at physical root; dh1 contains 1/h1 and source third derivative jumps',
  'mathematical_class':'single-fixed-domain semialgebraic period / positive-part glued algebraic density',
  'formal_numeric_runtime':'NOT IMPLEMENTED'}
}
print(json.dumps(out,indent=2,default=lambda o:list(o) if isinstance(o,tuple) else o))
