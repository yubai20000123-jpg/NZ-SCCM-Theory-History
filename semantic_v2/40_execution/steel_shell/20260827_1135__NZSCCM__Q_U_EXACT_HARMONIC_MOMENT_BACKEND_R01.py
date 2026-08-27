from __future__ import annotations
from dataclasses import dataclass
from math import pi, sin
import cmath

FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1

HARMONICS_LL = {
    (0, 1): +0.5,
    (0, 2): -0.5,
    (1, 0): +0.5,
    (1, 1): -1.0,
    (1, 2): +0.5,
    (2, 0): -0.5,
    (2, 1): +0.5,
}


def sinc(z: float) -> float:
    return 1.0 if abs(z) < 1e-15 else sin(z)/z


def exp_average(omega: float, x0: float, L: float) -> complex:
    """Exact normalized average of exp(i omega x) over [x0,x0+L]."""
    return cmath.exp(1j*omega*(x0 + 0.5*L))*sinc(0.5*omega*L)


def exp_integral(omega: float, x0: float, L: float) -> complex:
    return L*exp_average(omega,x0,L)


def _kp_num(r: float) -> float:
    return (272*r**16 + 2856*r**14 + 11273*r**12 + 23146*r**10
            + 31506*r**8 + 23146*r**6 + 11273*r**4 + 2856*r**2 + 272)


def r02_KA(kx: float, ky: float) -> float:
    r=kx/ky
    return (ky**4*_kp_num(r)
            /(256.0*(r*r+1.0)**2*(r*r+4.0)**2*(4.0*r*r+1.0)**2))


def _avg_cos2(m: int) -> float:
    return 1.0 if m == 0 else 0.5


def _avg_sin2(m: int) -> float:
    return 0.0 if m == 0 else 0.5


def ll_airy_energy_coefficient(kx: float, ky: float, nu: float = 0.30) -> float:
    """Exact cell-average plane-stress complementary-energy coefficient for the
    LL Airy fluctuation with E=d=1. Orthogonality is analytic; there is no
    spatial quadrature. The result must equal the frozen R02 KA.
    """
    total=0.0
    for (m,n),h in HARMONICS_LL.items():
        eig=((m*kx)**2+(n*ky)**2)**2
        F=h*kx*kx*ky*ky/eig
        sx=-(n*ky)**2*F
        sy=-(m*kx)**2*F
        tau=-(m*kx)*(n*ky)*F
        cc=_avg_cos2(m)*_avg_cos2(n)
        ss=_avg_sin2(m)*_avg_sin2(n)
        total += 0.5*((sx*sx+sy*sy-2.0*nu*sx*sy)*cc
                     +2.0*(1.0+nu)*tau*tau*ss)
    return total


def ll_mean_coefficients(kx: float, ky: float) -> tuple[float,float,float]:
    """Exact normalized means: 1/2<phi_x^2>, 1/2<phi_y^2>, <phi_x phi_y>."""
    return 3.0*kx*kx/8.0, 3.0*ky*ky/8.0, 0.0


def phase_factor_cos_sin(r: float) -> complex:
    """C=<exp(i r t) sin(t)> on t in [0,2pi].
    The phase amplitude of <cos(theta+r t) sin t> is |C|.
    """
    def avg_t(w):
        return cmath.exp(1j*w*pi)*sinc(w*pi)
    return (avg_t(r+1)-avg_t(r-1))/(2j)


def phase_factor_sin_one_minus_cos(r: float) -> complex:
    """C=<exp(i r t)(1-cos t)> on t in [0,2pi]."""
    def avg_t(w):
        return cmath.exp(1j*w*pi)*sinc(w*pi)
    return avg_t(r)-0.5*(avg_t(r+1)+avg_t(r-1))


@dataclass(frozen=True)
class BHCell:
    name: str
    b: float
    @property
    def Lx(self): return 0.225*self.b
    @property
    def Ly(self): return 2.0*self.b/9.0
    @property
    def kx(self): return 2*pi/self.Lx
    @property
    def ky(self): return 2*pi/self.Ly
    @property
    def alpha(self): return pi/self.b
    @property
    def beta(self): return pi/self.b


def regression_row(cell: BHCell) -> dict:
    cx,cy,cxy=ll_mean_coefficients(cell.kx,cell.ky)
    ka=r02_KA(cell.kx,cell.ky)
    kae=ll_airy_energy_coefficient(cell.kx,cell.ky,0.30)
    rx=cell.alpha/cell.kx
    ry=cell.beta/cell.ky
    ax=abs(phase_factor_cos_sin(rx))
    ay=abs(phase_factor_sin_one_minus_cos(ry))
    bx=abs(phase_factor_sin_one_minus_cos(rx))
    by=abs(phase_factor_cos_sin(ry))
    return dict(name=cell.name,Lx=cell.Lx,Ly=cell.Ly,kx=cell.kx,ky=cell.ky,
                cx=cx,cy=cy,cxy=cxy,KA=ka,KA_from_Airy=kae,
                relerr_KA=abs(kae-ka)/ka,
                max_norm_GL_x=ax*ay,max_norm_GL_y=bx*by,
                alpha_over_kx=rx,beta_over_ky=ry)


if __name__ == "__main__":
    for c in (BHCell("BH032",1600.0),BHCell("BH050",2500.0)):
        print(regression_row(c))
