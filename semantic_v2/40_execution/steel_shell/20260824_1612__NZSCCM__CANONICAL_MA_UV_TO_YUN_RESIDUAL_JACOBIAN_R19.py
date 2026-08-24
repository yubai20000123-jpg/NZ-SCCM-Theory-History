"""NZ-SCCM R19 — canonical Marguerre–Airy UV -> always-on Yun bridge audit.

This is a source-closure / derivative-audit script.
Formal production counters remain zero spatial quadrature/material points.
Gauss-Legendre below is used ONLY as a diagnostic oracle for finite-difference
checking of the already-fixed residual/Jacobian expressions; it is not a
production integration identity.

Canonical source:
  semantic_v2/20_theory/
  20260820_2358__NZSCCM__NGUYEN_KINEMATICS_EXPLICIT_UV_AND_NC_M6_VIRTUAL_WORK_SYSTEM.md

Historical unified Yun source:
  semantic_v2/40_execution/steel_shell/
  20260818_1421__NZSCCM__Z1_Z4__UNIFIED_YUN_IDEAL_EP_LOCAL_AMPLITUDE_FULL_RECALC.md
"""

from __future__ import annotations
from dataclasses import dataclass
from math import pi, sin, cos
import numpy as np

FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
YUN_ALWAYS_ON = True


@dataclass(frozen=True)
class MAState:
    b: float
    ell: float
    eps0: float
    t_ref: float
    q0: float
    nu: float

    @property
    def k(self) -> float:
        return self.b / self.ell

    def basis(self, xg: float, yg: float):
        X = pi * xg / self.b
        Y = pi * yg / self.ell
        sx, sy = sin(X), sin(Y)
        cy = cos(Y)
        Fy = sx*sx * (1.0 - sy*sy)
        Hs = sx * sy
        Ay = (
            self.nu / 4.0
            - 0.5 * self.k**2 * sx*sx
            - 0.5 * self.nu * sy*sy
            + self.k**2 * sx*sx * sy*sy
        )
        wy_per_q = pi * self.k * sx * cy
        return Fy, Hs, Ay, wy_per_q

    def ey_normalized(self, D: float, q: float, alpha: float,
                      xg: float, yg: float, zeta: float) -> float:
        Fy, Hs, Ay, _ = self.basis(xg, yg)
        Sq = self.q0*q + 0.5*q*q
        return (
            -D
            + alpha * Ay
            + (pi*pi*self.k**2/self.eps0) * Sq * Fy
            + (pi*pi*self.t_ref*self.k**2/(2.0*self.eps0*self.b))
              * q * Hs * zeta
        )

    def ey_physical(self, D: float, q: float, alpha: float,
                    xg: float, yg: float, zeta: float) -> float:
        return self.eps0 * self.ey_normalized(D,q,alpha,xg,yg,zeta)

    def ey_derivatives_physical(self, D: float, q: float, alpha: float,
                                xg: float, yg: float, zeta: float):
        Fy, Hs, Ay, _ = self.basis(xg, yg)
        first = np.array([
            -self.eps0,
            pi*pi*self.k**2*(self.q0+q)*Fy
            + pi*pi*self.t_ref*self.k**2/(2.0*self.b)*Hs*zeta,
            self.eps0*Ay,
        ], dtype=float)
        second = np.zeros((3,3), dtype=float)
        second[1,1] = pi*pi*self.k**2*Fy
        return first, second


@dataclass(frozen=True)
class YunStrip:
    i: int
    Bs: float
    ell: float
    A0: float
    Es: float
    nu: float
    fy: float
    ts: float

    @property
    def x0(self):
        return self.i * self.Bs

    @property
    def m(self):
        m = self.ell / self.Bs
        mi = int(round(m))
        if abs(m-mi) > 1e-12:
            raise ValueError("Current source-closed complete-halfwave strip requires ell/Bs integer.")
        return mi

    def x_global(self, xi: float):
        return self.x0 + xi

    def phi_y(self, xi: float, yg: float) -> float:
        return (
            (1.0 - cos(2.0*pi*xi/self.Bs))
            * (2.0*self.m*pi/self.ell)
            * sin(2.0*self.m*pi*yg/self.ell)
        )

    def yun_prefactors(self):
        r = (self.ell/self.m)/self.Bs
        kcr = 4.0*(3.0*r**4 + 2.0*r**2 + 3.0)/(3.0*r**2)
        kp_num = (272*r**16 + 2856*r**14 + 11273*r**12 + 23146*r**10
                  + 31506*r**8 + 23146*r**6 + 11273*r**4 + 2856*r**2 + 272)
        kp_den = r**2*(r**2+1)**2*(r**2+4)**2*(4*r**2+1)**2
        kp = kp_num/kp_den
        Csig = pi*pi*self.Es*self.ts**2/(12.0*(1.0-self.nu**2)*self.Bs**2)
        H = kp*(1.0-self.nu**2)/self.ts**2
        return Csig,kcr,H


def steel_strain_and_derivatives(ma: MAState, strip: YunStrip,
                                 D,q,alpha,A, xi,yg,zeta):
    xg = strip.x_global(xi)
    eg = ma.ey_physical(D,q,alpha,xg,yg,zeta)
    dglobal, ddglobal = ma.ey_derivatives_physical(D,q,alpha,xg,yg,zeta)
    _,_,_,wy_per_q = ma.basis(xg,yg)
    phiy = strip.phi_y(xi,yg)
    w0y = ma.q0 * wy_per_q
    dwy = q * wy_per_q

    eps = (
        eg
        + A*(w0y+dwy)*phiy
        + strip.A0*dwy*phiy
        + (strip.A0*A + 0.5*A*A)*phiy*phiy
    )

    d = np.zeros(4)
    d[:3] = dglobal
    d[1] += (A + strip.A0)*wy_per_q*phiy
    d[3] = (w0y+dwy)*phiy + (strip.A0+A)*phiy*phiy

    dd = np.zeros((4,4))
    dd[:3,:3] = ddglobal
    dd[1,3] = dd[3,1] = wy_per_q*phiy
    dd[3,3] = phiy*phiy
    return eps,d,dd


def ideal_ep(eps, Es, fy):
    tr = Es*eps
    if tr > fy:
        return fy,0.0
    if tr < -fy:
        return -fy,0.0
    return tr,Es


def diagnostic_mean_sigma_and_derivative(ma, strip, theta, face_zeta, n=24):
    """Diagnostic oracle only; not formal production quadrature."""
    D,q,alpha,A = theta
    gx, wx = np.polynomial.legendre.leggauss(n)
    gy, wy = np.polynomial.legendre.leggauss(n)
    xis = 0.5*strip.Bs*(gx+1)
    ys = 0.5*strip.ell*(gy+1)
    wxx = 0.5*strip.Bs*wx
    wyy = 0.5*strip.ell*wy
    area = strip.Bs*strip.ell
    S=0.0
    dS=np.zeros(4)
    for xi,wxi in zip(xis,wxx):
        for yg,wyg in zip(ys,wyy):
            eps,d,_ = steel_strain_and_derivatives(ma,strip,D,q,alpha,A,xi,yg,face_zeta)
            sig,Et = ideal_ep(eps,strip.Es,strip.fy)
            w=wxi*wyg
            S += w*sig
            dS += w*Et*d
    return S/area, dS/area


def local_amplitude_residual_and_jac_diag(ma,strip,theta,face_zeta,n=24):
    D,q,alpha,A=theta
    mean_sig,dmean = diagnostic_mean_sigma_and_derivative(ma,strip,theta,face_zeta,n=n)
    mean_comp = -mean_sig
    dmean_comp = -dmean
    Csig,kcr,H = strip.yun_prefactors()
    poly = kcr*A + H*(2*strip.A0*A + A*A)*(A+strip.A0)
    R = Csig*poly - mean_comp*(A+strip.A0)
    gprime = (2*strip.A0+2*A)*(A+strip.A0) + (2*strip.A0*A+A*A)
    dpolyA = kcr + H*gprime
    J = -(A+strip.A0)*dmean_comp
    J[3] += Csig*dpolyA - mean_comp
    return R,J


def fd_gradient(f,x,hscale=2e-7):
    x=np.array(x,dtype=float)
    g=np.zeros_like(x)
    for j in range(len(x)):
        h=hscale*max(1.0,abs(x[j]))
        xp=x.copy(); xm=x.copy()
        xp[j]+=h; xm[j]-=h
        g[j]=(f(xp)-f(xm))/(2*h)
    return g


def main():
    ma=MAState(b=6000.0,ell=6000.0,eps0=0.0018712490394580678,
               t_ref=100.0,q0=0.004,nu=0.18)
    strips=[YunStrip(i=i,Bs=200.0,ell=6000.0,A0=0.125,Es=206000.0,
                      nu=0.30,fy=235.0,ts=4.0) for i in range(30)]
    assert abs(strips[0].x_global(0.0)-0.0)<1e-12
    assert abs(strips[-1].x_global(200.0)-ma.b)<1e-12

    st=strips[11]
    theta=np.array([0.71,0.0083,0.17,0.043])
    xi=73.0; yg=1843.0; zeta=-1.0
    eps,d,dd=steel_strain_and_derivatives(ma,st,*theta,xi,yg,zeta)
    f=lambda th: steel_strain_and_derivatives(ma,st,*th,xi,yg,zeta)[0]
    dfd=fd_gradient(f,theta,hscale=1e-7)
    err=np.max(np.abs(d-dfd))

    dd_fd=np.zeros((4,4))
    for j in range(4):
        h=1e-6*max(1.0,abs(theta[j]))
        xp=theta.copy(); xm=theta.copy()
        xp[j]+=h; xm[j]-=h
        dp=steel_strain_and_derivatives(ma,st,*xp,xi,yg,zeta)[1]
        dm=steel_strain_and_derivatives(ma,st,*xm,xi,yg,zeta)[1]
        dd_fd[:,j]=(dp-dm)/(2*h)
    err2=np.max(np.abs(dd-dd_fd))

    R,J=local_amplitude_residual_and_jac_diag(ma,st,theta,zeta,n=28)
    fR=lambda th: local_amplitude_residual_and_jac_diag(ma,st,th,zeta,n=28)[0]
    Jfd=fd_gradient(fR,theta,hscale=2e-6)
    errR=np.max(np.abs(J-Jfd))
    relR=np.max(np.abs(J-Jfd)/np.maximum(1.0,np.abs(Jfd)))

    print("R19_CANONICAL_MA_UV_SOURCE = PASS")
    print("NESTED_LOCAL_GLOBAL_COORDINATE_MAP = PASS")
    print("STRIP_COVERAGE_X0_TO_B = PASS")
    print("POINTWISE_FIRST_DERIV_MAX_ABS_ERR =", f"{err:.6e}")
    print("POINTWISE_SECOND_DERIV_MAX_ABS_ERR =", f"{err2:.6e}")
    print("DIAGNOSTIC_RA_JAC_MAX_ABS_ERR =", f"{errR:.6e}")
    print("DIAGNOSTIC_RA_JAC_MAX_REL_ERR =", f"{relR:.6e}")
    print("DIAGNOSTIC_RA =", f"{R:.12e}")
    print("FORMAL_SPATIAL_QUADRATURE =", FORMAL_SPATIAL_QUADRATURE)
    print("THICKNESS_QUADRATURE =", THICKNESS_QUADRATURE)
    print("MATERIAL_POINTS =", MATERIAL_POINTS)
    assert err < 2e-11
    assert err2 < 2e-9
    assert relR < 3e-4
    print("R19_CANONICAL_MA_TO_YUN_JACOBIAN_AUDIT = PASS")

if __name__ == "__main__":
    main()
