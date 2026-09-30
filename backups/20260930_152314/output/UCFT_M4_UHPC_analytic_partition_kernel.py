#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UCFT M4 — UHPC piecewise-polynomial active-set analytic partition kernel.

Theory contract
---------------
X = pi*x/b, Y = pi*y/a_h, r=b/a_h.
q is the outer continuation parameter.
The UHPC directional current inputs are
  e_x = (eps_x + nu*eps_y)/(1-nu^2)
  e_y = (eps_y + nu*eps_x)/(1-nu^2).

Thickness integration is exact through cumulative stress primitives.
For fixed X the in-plane Y active-set boundaries are exact roots in
s = sin(Y), because every face strain is
  e_face = A(X) + B(X)*cos(2Y) + C_face(X)*sin(Y)
         = A+B+C*s-2B*s^2.

After splitting 0<=s<=1 at all material-face crossing roots, the Y
integrands are finite Laurent polynomials times 1/sqrt(1-s^2), so the
Y integral is elementary. Only the final outer X integral is retained
as a one-dimensional deterministic integral.

No FEM target and no high-dimensional Gauss-point material definition
is used by this kernel.
"""

from dataclasses import dataclass
from pathlib import Path
import math
import numpy as np
import pandas as pd
from numpy.polynomial import Polynomial as Polynomial
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad_vec

@dataclass
class PiecewiseUHPC:
    # ordered thresholds: e_z < 0 < e_tp < e_tu
    e_z: float
    e_tp: float
    e_tu: float
    # stress polynomials for compression, tension ascending, tension softening
    P_c: Polynomial
    P_t1: Polynomial
    P_t2: Polynomial

    def __post_init__(self):
        E = Polynomial([0.0, 1.0])
        # raw primitives on each non-zero branch
        Fc = self.P_c.integ()
        Hc = (E*self.P_c).integ()
        Ft1 = self.P_t1.integ()
        Ht1 = (E*self.P_t1).integ()
        Ft2 = self.P_t2.integ()
        Ht2 = (E*self.P_t2).integ()

        # globally continuous cumulative primitives.
        # Lower and upper zero-stress tails are constant.
        F0 = Polynomial([0.0])
        H0 = Polynomial([0.0])

        FC = Fc - Fc(self.e_z)
        HC = Hc - Hc(self.e_z)

        FT1 = Polynomial([FC(0.0)-Ft1(0.0)]) + Ft1
        HT1 = Polynomial([HC(0.0)-Ht1(0.0)]) + Ht1

        FT2 = Polynomial([FT1(self.e_tp)-Ft2(self.e_tp)]) + Ft2
        HT2 = Polynomial([HT1(self.e_tp)-Ht2(self.e_tp)]) + Ht2

        FU = Polynomial([FT2(self.e_tu)])
        HU = Polynomial([HT2(self.e_tu)])

        self.F_branch = [F0, FC, FT1, FT2, FU]
        self.H_branch = [H0, HC, HT1, HT2, HU]
        self.P_branch = [Polynomial([0.0]), self.P_c, self.P_t1,
                         self.P_t2, Polynomial([0.0])]
        self.thresholds = [self.e_z, 0.0, self.e_tp, self.e_tu]

    def branch_index(self, e):
        if e <= self.e_z:
            return 0
        if e <= 0.0:
            return 1
        if e <= self.e_tp:
            return 2
        if e <= self.e_tu:
            return 3
        return 4

    def FH(self, e):
        i = self.branch_index(e)
        return float(self.F_branch[i](e)), float(self.H_branch[i](e))

    def stress(self, e):
        i = self.branch_index(e)
        return float(self.P_branch[i](e))


def build_validation_law(Ec=43400.0, fc=141.1, eps_c0=0.0035,
                         ft=7.0, r_t=2.0, lambda_t=5.0):
    """
    M2 central diagnostic family ONLY, used for numerical equivalence validation.
    It is NOT promoted here to the final production tensile material calibration.
    """
    E = Polynomial([0.0, 1.0])
    A_c = Ec*eps_c0/fc
    B_c = 6.0 - 5.0*A_c
    C_c = 4.0*A_c - 5.0

    P_c = (Ec*E
           + fc*B_c/eps_c0**5 * E**5
           - fc*C_c/eps_c0**6 * E**6)

    eps_tp = r_t*ft/Ec
    eps_tu = lambda_t*eps_tp
    P_t1 = (ft*r_t/eps_tp)*E \
         + ft*(3.0-2.0*r_t)/eps_tp**2 * E**2 \
         + ft*(r_t-2.0)/eps_tp**3 * E**3

    s = (E-eps_tp)/(eps_tu-eps_tp)
    P_t2 = ft*(1.0 - 3.0*s**2 + 2.0*s**3)

    # first post-peak zero of the currently locked compression polynomial
    e_z = -1.35286765*eps_c0
    return PiecewiseUHPC(e_z, eps_tp, eps_tu, P_c, P_t1, P_t2)


def directional_face_polynomials(X, q, Ex, Ey, Bx, By, Hx, Hy,
                                 b, a_h, t_c, nu, q0, direction):
    r = b/a_h
    D = 1.0 - nu*nu
    c2x = math.cos(2.0*X)
    sx = math.sin(X)
    Cq = math.pi**2*(q*q + 2.0*q0*q)/8.0

    if direction == "x":
        A = (Ex + nu*Ey + (Bx - nu*Cq*r*r)*c2x)/D
        B = (-Cq + nu*By + (Hx + nu*Hy)*c2x)/D
        chi0 = (math.pi**2*q/b)*(1.0 + nu*r*r)/D * sx
    elif direction == "y":
        A = (Ey + nu*Ex + (-Cq*r*r + nu*Bx)*c2x)/D
        B = (By - nu*Cq + (Hy + nu*Hx)*c2x)/D
        chi0 = (math.pi**2*q/b)*(r*r + nu)/D * sx
    else:
        raise ValueError("direction must be x or y")

    # s = sin(Y): e_m = (A+B) - 2B*s^2, chi = chi0*s
    em = Polynomial([A+B, 0.0, -2.0*B])
    e_plus = em + Polynomial([0.0, 0.5*t_c*chi0])
    e_minus = em - Polynomial([0.0, 0.5*t_c*chi0])
    return em, e_plus, e_minus, chi0


def explicit_threshold_roots(face_poly, threshold, tol=1e-13):
    """
    Solve face_poly(s)=threshold for a quadratic/linear face strain.
    Only roots strictly inside 0<s<1 are returned.
    """
    c = np.pad((face_poly-threshold).coef, (0, 3), constant_values=0.0)[:3]
    c0, c1, c2 = [float(x) for x in c]
    roots = []
    if abs(c2) <= tol:
        if abs(c1) > tol:
            roots = [-c0/c1]
    else:
        disc = c1*c1 - 4.0*c2*c0
        if disc >= -100.0*tol:
            disc = max(disc, 0.0)
            sd = math.sqrt(disc)
            roots = [(-c1-sd)/(2.0*c2), (-c1+sd)/(2.0*c2)]
    return [float(s) for s in roots if tol < s < 1.0-tol]


def partition_s(e_plus, e_minus, thresholds):
    pts = [0.0, 1.0]
    for e_j in thresholds:
        pts.extend(explicit_threshold_roots(e_plus, e_j))
        pts.extend(explicit_threshold_roots(e_minus, e_j))
    pts.sort()
    out = []
    for s in pts:
        if not out or abs(s-out[-1]) > 1e-11:
            out.append(s)
    return out


def laurent_from_polynomial(poly, denominator_power, scale, rel_tol=1e-11):
    """
    Return exponent->coefficient for scale*poly(s)/s^denominator_power.
    """
    cc = np.asarray(poly.coef, dtype=float)*scale
    ref = max(1.0, float(np.max(np.abs(cc))))
    out = {}
    for n, value in enumerate(cc):
        if abs(value) > rel_tol*ref:
            out[n-denominator_power] = float(value)
    return out


def J_primitive(n, s):
    """
    Primitive of s^n/sqrt(1-s^2) for integer n >= -2.
    """
    s = min(1.0, max(0.0, float(s)))
    root = math.sqrt(max(0.0, 1.0-s*s))
    if n == -2:
        if s == 0.0:
            return -math.inf
        return -root/s
    if n == -1:
        if s == 0.0:
            return -math.inf
        return math.log(s/(1.0+root))
    if n == 0:
        return math.asin(s)
    if n == 1:
        return -root
    return -(s**(n-1))*root/n + (n-1.0)/n*J_primitive(n-2, s)


def J_definite(n, a, b):
    return J_primitive(n, b) - J_primitive(n, a)


def integrate_laurent(coeffs, a, b, weight):
    """
    weight = 1, cos2Y=(1-2s^2), or sinY=s.
    The full 0<=Y<=pi integral is twice the returned half-domain integral.
    """
    value = 0.0
    for n, c in coeffs.items():
        if weight == "1":
            value += c*J_definite(n, a, b)
        elif weight == "cos2":
            value += c*(J_definite(n, a, b)-2.0*J_definite(n+2, a, b))
        elif weight == "sin":
            value += c*J_definite(n+1, a, b)
        else:
            raise ValueError("weight must be 1, cos2, or sin")
    return value


def y_moments_exact(law, X, state, geom, direction):
    """
    Exact Y integration for one fixed X.
    Returns integrals over 0<=Y<=pi:
      N_1, N_cos2, N_sin, M_1, M_cos2, M_sin.
    """
    q, Ex, Ey, Bx, By, Hx, Hy = [state[k] for k in
                                  ("q","Ex","Ey","Bx","By","Hx","Hy")]
    b, a_h, t_c, nu, q0 = [geom[k] for k in
                            ("b","a_h","t_c","nu","q0")]
    em, ep, en, chi0 = directional_face_polynomials(
        X,q,Ex,Ey,Bx,By,Hx,Hy,b,a_h,t_c,nu,q0,direction)

    # chi=0 is a continuous limit, used at q=0 or measure-zero X endpoints.
    if abs(chi0) < 1e-14:
        def direct_half(s, weight):
            e = float(em(s))
            N = t_c*law.stress(e)
            w = {"1":1.0, "cos2":1.0-2.0*s*s, "sin":s}[weight]
            return N*w/math.sqrt(max(1e-30,1.0-s*s))
        result = {}
        for w in ("1","cos2","sin"):
            val, _ = quad(lambda ss: direct_half(ss,w), 0.0, 1.0,
                          epsabs=1e-10, epsrel=1e-10, limit=100)
            result["N_"+w] = 2.0*val
            result["M_"+w] = 0.0
        return result

    pts = partition_s(ep, en, law.thresholds)
    total = {f"{kind}_{w}":0.0 for kind in ("N","M")
             for w in ("1","cos2","sin")}

    for sa, sb in zip(pts[:-1], pts[1:]):
        sm = 0.5*(sa+sb)
        ip = law.branch_index(float(ep(sm)))
        im = law.branch_index(float(en(sm)))

        Fdiff = law.F_branch[ip](ep) - law.F_branch[im](en)
        Hdiff = law.H_branch[ip](ep) - law.H_branch[im](en)

        N_laurent = laurent_from_polynomial(Fdiff, 1, 1.0/chi0)
        M_numer = Hdiff - em*Fdiff
        M_laurent = laurent_from_polynomial(M_numer, 2, 1.0/(chi0*chi0))

        # A true negative-power coefficient at s=0 would contradict the
        # continuous chi->0 limit. Remove only roundoff-level remnants.
        if sa == 0.0:
            for dct in (N_laurent, M_laurent):
                for n in list(dct):
                    if n < 0 and abs(dct[n]) < 1e-7:
                        del dct[n]

        for w in ("1","cos2","sin"):
            total["N_"+w] += integrate_laurent(N_laurent, sa, sb, w)
            total["M_"+w] += integrate_laurent(M_laurent, sa, sb, w)

    # symmetry: Y and pi-Y have the same normal active state
    for key in total:
        total[key] *= 2.0
    return total


def point_NM_global_primitive(law, X, Y, state, geom, direction):
    q, Ex, Ey, Bx, By, Hx, Hy = [state[k] for k in
                                  ("q","Ex","Ey","Bx","By","Hx","Hy")]
    b, a_h, t_c, nu, q0 = [geom[k] for k in
                            ("b","a_h","t_c","nu","q0")]
    em_poly, _, _, chi0 = directional_face_polynomials(
        X,q,Ex,Ey,Bx,By,Hx,Hy,b,a_h,t_c,nu,q0,direction)
    s = math.sin(Y)
    em = float(em_poly(s))
    chi = chi0*s
    if abs(chi) < 1e-14:
        return t_c*law.stress(em), 0.0
    e_plus = em + 0.5*t_c*chi
    e_minus = em - 0.5*t_c*chi
    Fp, Hp = law.FH(e_plus)
    Fm, Hm = law.FH(e_minus)
    dF = Fp-Fm
    N = dF/chi
    M = (Hp-Hm-em*dF)/(chi*chi)
    return float(N), float(M)


def point_NM_explicit_sorted(law, X, Y, state, geom, direction):
    """
    Independent exact thickness check: explicitly form z_j, sort, and integrate
    branch-by-branch. This is algebraically equivalent to the cumulative primitive.
    """
    q, Ex, Ey, Bx, By, Hx, Hy = [state[k] for k in
                                  ("q","Ex","Ey","Bx","By","Hx","Hy")]
    b, a_h, t_c, nu, q0 = [geom[k] for k in
                            ("b","a_h","t_c","nu","q0")]
    em_poly, _, _, chi0 = directional_face_polynomials(
        X,q,Ex,Ey,Bx,By,Hx,Hy,b,a_h,t_c,nu,q0,direction)
    s = math.sin(Y)
    em = float(em_poly(s))
    chi = chi0*s
    h = 0.5*t_c
    if abs(chi) < 1e-14:
        return t_c*law.stress(em), 0.0

    # raw branch primitives, constants irrelevant inside a single segment
    E = Polynomial([0.0,1.0])
    rawF = [Polynomial([0.0]),
            law.P_c.integ(),
            law.P_t1.integ(),
            law.P_t2.integ(),
            Polynomial([0.0])]
    rawH = [Polynomial([0.0]),
            (E*law.P_c).integ(),
            (E*law.P_t1).integ(),
            (E*law.P_t2).integ(),
            Polynomial([0.0])]

    zpts = [-h, h]
    for e_j in law.thresholds:
        z = (e_j-em)/chi
        if -h < z < h:
            zpts.append(float(z))
    zpts = sorted(zpts)

    N = 0.0
    M = 0.0
    for za, zb in zip(zpts[:-1], zpts[1:]):
        zm = 0.5*(za+zb)
        idx = law.branch_index(em+chi*zm)
        if idx in (0,4):
            continue
        ea, eb = em+chi*za, em+chi*zb
        dF = rawF[idx](eb)-rawF[idx](ea)
        dH = rawH[idx](eb)-rawH[idx](ea)
        N += dF/chi
        M += (dH-em*dF)/(chi*chi)
    return float(N), float(M)


def area_normal_integrals_exactY(law, state, geom,
                                 epsabs=1e-5, epsrel=2e-9):
    """
    Only one outer deterministic X integral remains.
    Returned physical-area quantities:
      int Nx dA, int Ny dA,
      int Nx cos2X dA, int Ny cos2Y dA,
      int Nx cos2X cos2Y dA, int Ny cos2X cos2Y dA,
      int Mx sinX sinY dA, int My sinX sinY dA.
    """
    b, a_h = geom["b"], geom["a_h"]
    factor = b*a_h/math.pi**2

    def outer(X):
        mx = y_moments_exact(law,X,state,geom,"x")
        my = y_moments_exact(law,X,state,geom,"y")
        c2x = math.cos(2.0*X)
        sx = math.sin(X)
        return np.array([
            mx["N_1"],
            my["N_1"],
            c2x*mx["N_1"],
            my["N_cos2"],
            c2x*mx["N_cos2"],
            c2x*my["N_cos2"],
            sx*mx["M_sin"],
            sx*my["M_sin"],
        ])

    value, error = quad_vec(outer,0.0,math.pi,epsabs=epsabs,
                            epsrel=epsrel,limit=180)
    return factor*value, error


def area_normal_integrals_gauss2d(law, state, geom, nx=80, ny=120):
    """
    Independent diagnostic only. Not a production residual definition.
    """
    b, a_h = geom["b"], geom["a_h"]
    factor = b*a_h/math.pi**2
    gx, wx = leggauss(nx)
    gy, wy = leggauss(ny)
    Xs = 0.5*math.pi*(gx+1.0)
    Ys = 0.5*math.pi*(gy+1.0)
    WX = 0.5*math.pi*wx
    WY = 0.5*math.pi*wy
    total = np.zeros(8)

    for X, wX in zip(Xs, WX):
        c2x = math.cos(2.0*X)
        sx = math.sin(X)
        for Y, wY in zip(Ys, WY):
            Nx, Mx = point_NM_global_primitive(law,X,Y,state,geom,"x")
            Ny, My = point_NM_global_primitive(law,X,Y,state,geom,"y")
            c2y = math.cos(2.0*Y)
            sy = math.sin(Y)
            total += wX*wY*np.array([
                Nx, Ny, c2x*Nx, c2y*Ny,
                c2x*c2y*Nx, c2x*c2y*Ny,
                sx*sy*Mx, sx*sy*My
            ])
    return factor*total


def active_boundaries(law, X, state, geom, direction):
    q, Ex, Ey, Bx, By, Hx, Hy = [state[k] for k in
                                  ("q","Ex","Ey","Bx","By","Hx","Hy")]
    b, a_h, t_c, nu, q0 = [geom[k] for k in
                            ("b","a_h","t_c","nu","q0")]
    _, ep, en, _ = directional_face_polynomials(
        X,q,Ex,Ey,Bx,By,Hx,Hy,b,a_h,t_c,nu,q0,direction)
    labels = ["e_z","0","e_tp","e_tu"]
    out = []
    for face, poly in [("+",ep),("-",en)]:
        for label, thr in zip(labels, law.thresholds):
            for s in explicit_threshold_roots(poly,thr):
                out.append({
                    "direction":direction,
                    "face":face,
                    "threshold":label,
                    "s=sinY":s,
                    "Y_left_rad":math.asin(s),
                    "Y_right_rad":math.pi-math.asin(s)
                })
    return out
