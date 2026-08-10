from __future__ import annotations

from dataclasses import dataclass
import math
from typing import List

import numpy as np
from scipy.special import beta, betainc


@dataclass(frozen=True)
class InPlanePrincipalThresholdFront:
    """Principal-strain threshold front at a fixed thickness z."""

    S: float
    A: float
    delta: float
    kx: float
    ky: float
    z: float
    lam: float

    def strain_components(self, u: float, v: float):
        uv = max(0.0, u*v)
        cc = max(0.0, (1.0-u)*(1.0-v))
        ex = self.S*self.kx**2*(1.0-u)*v + self.z*self.A*self.kx**2*math.sqrt(uv)
        ey = -self.delta + self.S*self.ky**2*u*(1.0-v) + self.z*self.A*self.ky**2*math.sqrt(uv)
        ga = (
            2.0*self.S*self.kx*self.ky*math.sqrt(max(0.0, u*(1.0-u)*v*(1.0-v)))
            - 2.0*self.z*self.A*self.kx*self.ky*math.sqrt(cc)
        )
        return ex, ey, ga

    def principal_strains(self, u: float, v: float):
        ex, ey, ga = self.strain_components(u, v)
        mean = 0.5*(ex+ey)
        radius = math.sqrt(0.25*(ex-ey)**2 + 0.25*ga**2)
        return mean+radius, mean-radius

    def p0_p1(self, u: float, v: float):
        S,A,delta,kx,ky,z,lam = (
            self.S,self.A,self.delta,self.kx,self.ky,self.z,self.lam
        )
        p0 = (
            A*A*kx*kx*ky*ky*z*z*(u+v-1.0)
            - S*delta*kx*kx*v
            - S*kx*kx*lam*v
            - S*ky*ky*lam*u
            + delta*lam + lam*lam
            + u*v*(S*delta*kx*kx + S*kx*kx*lam + S*ky*ky*lam)
        )
        p1 = A*z*(
            S*kx*kx*ky*ky*(2.0-u-v)
            - delta*kx*kx
            - lam*(kx*kx+ky*ky)
        )
        return p0, p1

    def physical_equation(self, u: float, v: float):
        p0, p1 = self.p0_p1(u, v)
        return p0 + math.sqrt(max(0.0, u*v))*p1

    def polynomial_equation(self, u: float, v: float):
        p0, p1 = self.p0_p1(u, v)
        return p0*p0 - u*v*p1*p1

    def cubic_coefficients_in_v(self, u: float):
        S,A,delta,kx,ky,z,lam = (
            self.S,self.A,self.delta,self.kx,self.ky,self.z,self.lam
        )
        return (
            A**4*kx**4*ky**4*u**2*z**4 - 2*A**4*kx**4*ky**4*u*z**4 + A**4*kx**4*ky**4*z**4 - 2*A**2*S*kx**2*ky**4*lam*u**2*z**2 + 2*A**2*S*kx**2*ky**4*lam*u*z**2 + 2*A**2*delta*kx**2*ky**2*lam*u*z**2 - 2*A**2*delta*kx**2*ky**2*lam*z**2 + 2*A**2*kx**2*ky**2*lam**2*u*z**2 - 2*A**2*kx**2*ky**2*lam**2*z**2 + S**2*ky**4*lam**2*u**2 - 2*S*delta*ky**2*lam**2*u - 2*S*ky**2*lam**3*u + delta**2*lam**2 + 2*delta*lam**3 + lam**4,
            2*A**4*kx**4*ky**4*u*z**4 - 2*A**4*kx**4*ky**4*z**4 - A**2*S**2*kx**4*ky**4*u**3*z**2 + 4*A**2*S**2*kx**4*ky**4*u**2*z**2 - 4*A**2*S**2*kx**4*ky**4*u*z**2 + 2*A**2*S*delta*kx**4*ky**2*z**2 + 2*A**2*S*kx**4*ky**2*lam*z**2 - A**2*delta**2*kx**4*u*z**2 - 2*A**2*delta*kx**4*lam*u*z**2 - 2*A**2*delta*kx**2*ky**2*lam*u*z**2 + 2*A**2*delta*kx**2*ky**2*lam*z**2 - A**2*kx**4*lam**2*u*z**2 - 2*A**2*kx**2*ky**2*lam**2*u*z**2 + 2*A**2*kx**2*ky**2*lam**2*z**2 - A**2*ky**4*lam**2*u*z**2 - 2*S**2*delta*kx**2*ky**2*lam*u**2 + 2*S**2*delta*kx**2*ky**2*lam*u - 2*S**2*kx**2*ky**2*lam**2*u**2 + 2*S**2*kx**2*ky**2*lam**2*u - 2*S**2*ky**4*lam**2*u**2 + 2*S*delta**2*kx**2*lam*u - 2*S*delta**2*kx**2*lam + 4*S*delta*kx**2*lam**2*u - 4*S*delta*kx**2*lam**2 + 2*S*delta*ky**2*lam**2*u + 2*S*kx**2*lam**3*u - 2*S*kx**2*lam**3 + 2*S*ky**2*lam**3*u,
            A**4*kx**4*ky**4*z**4 - 2*A**2*S**2*kx**4*ky**4*u**2*z**2 + 4*A**2*S**2*kx**4*ky**4*u*z**2 - 2*A**2*S*delta*kx**4*ky**2*z**2 - 2*A**2*S*kx**4*ky**2*lam*z**2 + S**2*delta**2*kx**4*u**2 - 2*S**2*delta**2*kx**4*u + S**2*delta**2*kx**4 + 2*S**2*delta*kx**4*lam*u**2 - 4*S**2*delta*kx**4*lam*u + 2*S**2*delta*kx**4*lam + 2*S**2*delta*kx**2*ky**2*lam*u**2 - 2*S**2*delta*kx**2*ky**2*lam*u + S**2*kx**4*lam**2*u**2 - 2*S**2*kx**4*lam**2*u + S**2*kx**4*lam**2 + 2*S**2*kx**2*ky**2*lam**2*u**2 - 2*S**2*kx**2*ky**2*lam**2*u + S**2*ky**4*lam**2*u**2,
            -A**2*S**2*kx**4*ky**4*u*z**2,
        )

    def physical_roots_v(self, u: float, tol: float = 1.0e-8) -> List[float]:
        coeff = list(self.cubic_coefficients_in_v(u))
        scale = max(1.0e-30, max(abs(x) for x in coeff))
        while len(coeff) > 1 and abs(coeff[-1]) <= 1.0e-13*scale:
            coeff.pop()
        roots = np.roots(list(reversed(coeff)))
        accepted: List[float] = []
        for root in roots:
            if abs(root.imag) > 1.0e-8:
                continue
            value = float(root.real)
            if value < -tol or value > 1.0+tol:
                continue
            value = min(1.0, max(0.0, value))
            p0, p1 = self.p0_p1(u, value)
            residual = self.physical_equation(u, value)
            local_scale = max(
                1.0e-14,
                abs(p0),
                abs(math.sqrt(max(0.0, u*value))*p1)
            )
            if abs(residual) <= tol*local_scale:
                if all(abs(value-old) > 1.0e-7 for old in accepted):
                    accepted.append(value)
        return sorted(accepted)

    def midplane_boundary_v(self, u: float):
        if abs(self.z) > 1.0e-14:
            raise ValueError("midplane_boundary_v requires z=0")
        C0 = self.delta*self.lam + self.lam*self.lam
        Cu = -self.S*self.ky*self.ky*self.lam
        Cv = -self.S*self.delta*self.kx*self.kx - self.S*self.kx*self.kx*self.lam
        Cuv = (
            self.S*self.delta*self.kx*self.kx
            + self.S*self.kx*self.kx*self.lam
            + self.S*self.ky*self.ky*self.lam
        )
        denominator = Cv + Cuv*u
        if abs(denominator) <= 1.0e-16:
            return None
        return -(C0+Cu*u)/denominator


def full_panel_beta_moment(p: int, q: int, r: int, s: int) -> float:
    if q % 2 or s % 2:
        return 0.0
    ax = 0.5*(p+1)
    bx = 0.5*(q+1)
    ay = 0.5*(r+1)
    by = 0.5*(s+1)
    return float(beta(ax,bx)*beta(ay,by))


def incomplete_beta_interval(v0: float, v1: float, r: int, s: int) -> float:
    if s % 2:
        raise ValueError("odd cosine power cancels only after full symmetric pairing")
    a = 0.5*(r+1)
    b = 0.5*(s+1)
    return float(beta(a,b)*(betainc(a,b,v1)-betainc(a,b,v0)))


def front_moment_representation(p: int, q: int, r: int, s: int) -> str:
    if q % 2 or s % 2:
        return "0 by full-panel reflection symmetry"
    ax = f"({p}+1)/2"
    bx = f"({q}+1)/2"
    ay = f"({r}+1)/2"
    by = f"({s}+1)/2"
    return (
        "Integral_0^1 u^(a_x-1)(1-u)^(b_x-1) "
        "Sum_j[B_vplus(a_y,b_y)-B_vminus(a_y,b_y)] du; "
        f"a_x={ax}, b_x={bx}, a_y={ay}, b_y={by}"
    )
