from __future__ import annotations

# STEEL-SHELL COMMON R06
# Shared by SSNC and SSUHPC.  R02 is retained.  Yield-first cells degenerate
# exactly to R04.  Local-buckling-first cells are capped at the first finite-
# algebraic local-Mises yield boundary along the current face-strain ray.

from dataclasses import dataclass
from math import pi, sqrt
import numpy as np
import sympy as sp

FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH_PRODUCTION = False
COMPARATOR_IN_OPERATOR = False

HARMONICS = {
    (0, 1): +0.5,
    (0, 2): -0.5,
    (1, 0): +0.5,
    (1, 1): -1.0,
    (1, 2): +0.5,
    (2, 0): -0.5,
    (2, 1): +0.5,
}


def _kp_num(r: float) -> float:
    return (272*r**16 + 2856*r**14 + 11273*r**12 + 23146*r**10
            + 31506*r**8 + 23146*r**6 + 11273*r**4 + 2856*r**2 + 272)


def yun_kcr(r: float) -> float:
    return 4.0*(3.0*r**4 + 2.0*r**2 + 3.0)/(3.0*r**2)


@dataclass(frozen=True)
class PBLCell:
    Lx: float
    Ly: float
    t: float
    E: float
    nu: float
    fy: float
    A0: float

    @property
    def kx(self): return 2.0*pi/self.Lx
    @property
    def ky(self): return 2.0*pi/self.Ly
    @property
    def Q(self): return self.E/(1.0-self.nu**2)
    @property
    def G(self): return self.E/(2.0*(1.0+self.nu))
    @property
    def D(self): return self.E*self.t**3/(12.0*(1.0-self.nu**2))
    @property
    def cx(self): return 3.0*self.kx**2/8.0
    @property
    def cy(self): return 3.0*self.ky**2/8.0
    @property
    def Kb(self):
        return self.D*(0.75*(self.kx**4+self.ky**4)+0.5*self.kx**2*self.ky**2)
    @property
    def KA(self):
        r=self.kx/self.ky
        return (self.ky**4*_kp_num(r)
                /(256.0*(r*r+1.0)**2*(r*r+4.0)**2*(4.0*r*r+1.0)**2))


def sigma_cr_elastic(cell: PBLCell) -> float:
    r=cell.Ly/cell.Lx
    csig=pi*pi*cell.E*cell.t**2/(12.0*(1.0-cell.nu**2)*cell.Lx**2)
    return csig*yun_kcr(r)


def _real_cubic_roots(B3,B1,B0):
    rr=np.roots([B3,0.0,B1,B0])
    return [float(z.real) for z in rr if abs(z.imag)<1e-9]


def _amp_coeff(cell: PBLCell, ex: float, ey: float):
    L0=cell.Q*(cell.cx*(ex+cell.nu*ey)+cell.cy*(ey+cell.nu*ex))
    Cg=cell.Q*(cell.cx**2+cell.cy**2+2.0*cell.nu*cell.cx*cell.cy)
    B3=4.0*cell.t*cell.E*cell.KA+2.0*cell.t*Cg
    B1=cell.Kb-2.0*cell.t*L0-B3*cell.A0**2
    B0=-cell.Kb*cell.A0
    return B3,B1,B0


def _energy(cell,U,ex,ey):
    d=U*U-cell.A0**2
    mx=ex-cell.cx*d; my=ey-cell.cy*d
    Um=0.5*cell.t*cell.Q*(mx*mx+my*my+2.0*cell.nu*mx*my)
    Ub=0.5*cell.Kb*(U-cell.A0)**2
    Ua=cell.t*cell.E*cell.KA*d*d
    return Ub+Um+Ua


def solve_amplitude(cell: PBLCell, ex: float, ey: float) -> float:
    roots=_real_cubic_roots(*_amp_coeff(cell,ex,ey))
    roots=[u for u in roots if u>=-1e-11]
    if not roots:
        raise RuntimeError('no admissible R02 amplitude root')
    return min(roots,key=lambda U:_energy(cell,U,ex,ey))


def mean_physical_stress(cell: PBLCell,U:float,ex_comp:float,ey_comp:float,gamma:float=0.0):
    d=U*U-cell.A0**2
    mx=ex_comp-cell.cx*d; my=ey_comp-cell.cy*d
    sx=cell.Q*(mx+cell.nu*my)
    sy=cell.Q*(my+cell.nu*mx)
    # R02 normal convention is compression-positive; terminal convention tension-positive.
    return np.array([-sx,-sy,cell.G*gamma],dtype=float)


def _cos_poly(m,z):
    if m==0: return sp.Integer(1)
    if m==1: return z
    if m==2: return 2*z*z-1
    raise ValueError(m)


def _sin_factor(m,z):
    # sin(mX)=sqrt(1-z^2)*factor for m=1,2.
    if m==1: return sp.Integer(1)
    if m==2: return 2*z
    if m==0: return sp.Integer(0)
    raise ValueError(m)


def phi_polynomial(cell: PBLCell,U:float,ex_comp:float,ey_comp:float):
    """Return finite polynomial Phi(u,v)=local VM^2 for gamma_xy=0."""
    u,v=sp.symbols('u v',real=True)
    mean=mean_physical_stress(cell,U,ex_comp,ey_comp,0.0)
    d=U*U-cell.A0**2
    sx=sp.Float(mean[0],17); sy=sp.Float(mean[1],17); ps=sp.Integer(0)
    for (m,n),h in HARMONICS.items():
        src=h*cell.kx**2*cell.ky**2
        eig=((m*cell.kx)**2+(n*cell.ky)**2)**2
        F=cell.E*d*src/eig
        cm=_cos_poly(m,u); cn=_cos_poly(n,v)
        sx += sp.Float(-(n*cell.ky)**2*F,17)*cm*cn
        sy += sp.Float(-(m*cell.kx)**2*F,17)*cm*cn
        if m and n:
            ps += sp.Float(-(m*cell.kx)*(n*cell.ky)*F,17)*_sin_factor(m,u)*_sin_factor(n,v)
    phi=sp.expand(sx*sx-sx*sy+sy*sy+3*(1-u*u)*(1-v*v)*ps*ps)
    return sp.Poly(phi,u,v)


def finite_algebraic_global_max(phi: sp.Poly, sig_digits: int=12):
    """Finite algebraic extrema only: interior resultant roots, edges, corners.

    Decimal numeric input coefficients are rationalized before the resultant so
    this routine never replaces the domain by a spatial grid.
    """
    u,v=phi.gens
    terms={(i,j):sp.Rational(f'{float(c):.{sig_digits}g}') for (i,j),c in phi.terms()}
    f=sum(c*u**i*v**j for (i,j),c in terms.items())
    fu=sp.diff(f,u); fv=sp.diff(f,v)
    val=sp.lambdify((u,v),f,'numpy')
    cand=[]
    for uu in (-1.0,1.0):
        for vv in (-1.0,1.0): cand.append((float(val(uu,vv)),uu,vv,'corner'))
    for uu in (-1.0,1.0):
        p=sp.Poly(fv.subs(u,int(uu)),v)
        for rr in (sp.nroots(p) if p.degree()>0 else []):
            z=complex(rr)
            if abs(z.imag)<1e-8 and -1.0<=z.real<=1.0:
                cand.append((float(val(uu,z.real)),uu,z.real,'edge-u'))
    for vv in (-1.0,1.0):
        p=sp.Poly(fu.subs(v,int(vv)),u)
        for rr in (sp.nroots(p) if p.degree()>0 else []):
            z=complex(rr)
            if abs(z.imag)<1e-8 and -1.0<=z.real<=1.0:
                cand.append((float(val(z.real,vv)),z.real,vv,'edge-v'))
    R=sp.Poly(sp.resultant(fu,fv,v),u)
    for ru in sp.nroots(R,maxsteps=200):
        zu=complex(ru)
        if abs(zu.imag)>=1e-7 or not (-1.0<zu.real<1.0): continue
        pu=sp.Poly(fu.subs(u,sp.Rational(str(zu.real))),v)
        for rv in sp.nroots(pu,maxsteps=100):
            zv=complex(rv)
            if abs(zv.imag)>=1e-7 or not (-1.0<zv.real<1.0): continue
            g1=float(sp.N(fu.subs({u:zu.real,v:zv.real})))
            g2=float(sp.N(fv.subs({u:zu.real,v:zv.real})))
            if abs(g1)<1e-2 and abs(g2)<1e-2:
                cand.append((float(val(zu.real,zv.real)),zu.real,zv.real,'interior'))
    return max(cand,key=lambda x:x[0]),cand


def mises(s):
    sx,sy,tau=s
    return sqrt(sx*sx-sx*sy+sy*sy+3.0*tau*tau)


def r04_mean_cap(cell: PBLCell,epsx:float,epsy:float):
    ex=-epsx; ey=-epsy
    U=solve_amplitude(cell,ex,ey)
    trial=mean_physical_stress(cell,U,ex,ey,0.0)
    vm=mises(trial)
    lam=min(1.0,cell.fy/vm) if vm>0 else 1.0
    return {'mode':'R04_YIELD_FIRST','U':U,'eta':None,'stress':lam*trial,'lambda':lam}


def r06_branch(cell: PBLCell) -> str:
    return 'R04_YIELD_FIRST' if sigma_cr_elastic(cell)>=cell.fy else 'R06_LOCAL_BUCKLING_FIRST'

# Full radial projection requires repeated finite_algebraic_global_max calls.
# Blind T360/BH032 execution used the certified active edge v=-1 during Newton,
# followed by a full finite-algebraic candidate enumeration at every fixed final
# face state.  The execution report records those certificates.
