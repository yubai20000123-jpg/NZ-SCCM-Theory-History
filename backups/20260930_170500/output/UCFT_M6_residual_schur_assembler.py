#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UCFT M6 — residual / Jacobian / exact Schur-condensation contract.

This module does NOT define a new theory and does NOT run the nine specimens.
It freezes the algebraic interface that joins:
  M3 frequency-generated compatible inner membrane enrichment,
  M4 UHPC analytic active-set operator,
  M5 steel consistent secant-Mises active-set operator.

Structural hierarchy at fixed q:
  inner variables xi  -> G(xi,z;q)=0
  outer variables z=[P,Aplus,Aminus] -> R(xi,z;q)=0
with R=[Rq,RAplus,RAminus].

The exact full Newton matrix is
        [ G_xi   G_z ]
  J  =  [             ]
        [ R_xi   R_z ]

and exact Schur condensation gives
  Kcond = R_z - R_xi G_xi^{-1} G_z.

No inverse should be formed numerically; use linear solves/factorization.
"""

import math
import numpy as np


def Cq(q,q0):
    return math.pi**2*(q*q+2*q0*q)/8.0

def Cq_q(q,q0):
    return math.pi**2*(q+q0)/4.0

def Cq_qq():
    return math.pi**2/4.0


def baseline_C1_basis(X,Y,r):
    c2x=math.cos(2*X); c2y=math.cos(2*Y)
    s2x=math.sin(2*X); s2y=math.sin(2*Y)
    return {
        "Ex": np.array([1.0,0.0,0.0]),
        "Ey": np.array([0.0,1.0,0.0]),
        "Bx": np.array([c2x,0.0,0.0]),
        "By": np.array([0.0,c2y,0.0]),
        "Hx": np.array([c2x*c2y,0.0,-r*s2x*s2y]),
        "Hy": np.array([0.0,c2x*c2y,-(1.0/r)*s2x*s2y]),
    }

def C_family_basis(X,Y,r,k,l):
    cx=math.cos(k*X); cy=math.cos(l*Y)
    sx=math.sin(k*X); sy=math.sin(l*Y)
    return {
        f"Cx_{k}_{l}": np.array([cx*cy,0.0,-(l*r/k)*sx*sy]),
        f"Cy_{k}_{l}": np.array([0.0,cx*cy,-(k/(l*r))*sx*sy]),
    }

def S_family_basis(X,Y,r,k,l):
    sx=math.sin(k*X); sy=math.sin(l*Y)
    cx=math.cos(k*X); cy=math.cos(l*Y)
    return {
        f"Sx_{k}_{l}": np.array([sx*sy,0.0,-(l*r/k)*cx*cy]),
        f"Sy_{k}_{l}": np.array([0.0,sx*sy,-(k/(l*r))*cx*cy]),
    }

def Bx_family_basis(X,k):
    return {f"Bx_{k}": np.array([math.cos(k*X),0.0,0.0])}

def By_family_basis(Y,l):
    return {f"By_{l}": np.array([0.0,math.cos(l*Y),0.0])}


def psi_derivatives(X,Y,b,a_h,N,m):
    fx=1.0-math.cos(2*N*X)
    fy=1.0-math.cos(2*m*Y)
    sx=math.sin(2*N*X)
    sy=math.sin(2*m*Y)
    cx=math.cos(2*N*X)
    cy=math.cos(2*m*Y)
    psi=fx*fy
    psi_x=(2*math.pi*N/b)*sx*fy
    psi_y=(2*math.pi*m/a_h)*fx*sy
    psi_xx=(4*math.pi**2*N*N/b**2)*cx*fy
    psi_yy=(4*math.pi**2*m*m/a_h**2)*fx*cy
    psi_xy=(4*math.pi**2*N*m/(b*a_h))*sx*sy
    return psi,psi_x,psi_y,psi_xx,psi_yy,psi_xy


def global_curvature_q(X,Y,b,a_h):
    r=b/a_h
    return np.array([
        math.pi**2/b*math.sin(X)*math.sin(Y),
        math.pi**2*r*r/b*math.sin(X)*math.sin(Y),
        -2*math.pi**2*r/b*math.cos(X)*math.cos(Y)
    ])


def eps0_q(X,Y,q,q0,r):
    cp=Cq_q(q,q0)
    return np.array([
        -cp*math.cos(2*Y),
        -cp*r*r*math.cos(2*X),
        0.0
    ])

def eps0_qq(X,Y,r):
    cpp=Cq_qq()
    return np.array([
        -cpp*math.cos(2*Y),
        -cpp*r*r*math.cos(2*X),
        0.0
    ])


def steel_local_midstrain(X,Y,q,q0,A,A0,b,a_h,N,m,side):
    r=b/a_h
    _,px,py,_,_,_=psi_derivatives(X,Y,b,a_h,N,m)
    cross=q0*A + q*A0 + q*A
    local=A*A + 2*A0*A
    return np.array([
        side*math.pi*cross*math.cos(X)*math.sin(Y)*px
        +0.5*local*px*px,
        side*math.pi*r*cross*math.sin(X)*math.cos(Y)*py
        +0.5*local*py*py,
        side*math.pi*cross*(
            math.cos(X)*math.sin(Y)*py
            +r*math.sin(X)*math.cos(Y)*px)
        +local*px*py
    ])


def steel_local_midstrain_q(X,Y,q,A,A0,b,a_h,N,m,side):
    r=b/a_h
    _,px,py,_,_,_=psi_derivatives(X,Y,b,a_h,N,m)
    return np.array([
        side*math.pi*(A0+A)*math.cos(X)*math.sin(Y)*px,
        side*math.pi*r*(A0+A)*math.sin(X)*math.cos(Y)*py,
        side*math.pi*(A0+A)*(
            math.cos(X)*math.sin(Y)*py
            +r*math.sin(X)*math.cos(Y)*px)
    ])


def steel_local_midstrain_A(X,Y,q,q0,A,A0,b,a_h,N,m,side):
    r=b/a_h
    _,px,py,_,_,_=psi_derivatives(X,Y,b,a_h,N,m)
    return np.array([
        side*math.pi*(q0+q)*math.cos(X)*math.sin(Y)*px
        +(A0+A)*px*px,
        side*math.pi*r*(q0+q)*math.sin(X)*math.cos(Y)*py
        +(A0+A)*py*py,
        side*math.pi*(q0+q)*(
            math.cos(X)*math.sin(Y)*py
            +r*math.sin(X)*math.cos(Y)*px)
        +2*(A0+A)*px*py
    ])


def steel_local_midstrain_qA(X,Y,b,a_h,N,m,side):
    r=b/a_h
    _,px,py,_,_,_=psi_derivatives(X,Y,b,a_h,N,m)
    return np.array([
        side*math.pi*math.cos(X)*math.sin(Y)*px,
        side*math.pi*r*math.sin(X)*math.cos(Y)*py,
        side*math.pi*(
            math.cos(X)*math.sin(Y)*py
            +r*math.sin(X)*math.cos(Y)*px)
    ])


def steel_local_midstrain_AA(X,Y,b,a_h,N,m):
    _,px,py,_,_,_=psi_derivatives(X,Y,b,a_h,N,m)
    return np.array([px*px,py*py,2*px*py])


def steel_local_curvature_A(X,Y,b,a_h,N,m,side):
    _,_,_,pxx,pyy,pxy=psi_derivatives(X,Y,b,a_h,N,m)
    return np.array([-side*pxx,-side*pyy,-2*side*pxy])


def schur_condense(Gxi,Gz,Rxi,Rz,G,R):
    X_Gz=np.linalg.solve(Gxi,Gz)
    x_G=np.linalg.solve(Gxi,G)
    Kcond=Rz-Rxi@X_Gz
    rhs=-R+Rxi@x_G
    dz=np.linalg.solve(Kcond,rhs)
    dxi=-np.linalg.solve(Gxi,G+Gz@dz)
    return Kcond,rhs,dz,dxi


def condensed_q_sensitivity(Gxi,Gz,Rxi,Rz,Gq,Rq_partial):
    X_Gz=np.linalg.solve(Gxi,Gz)
    x_Gq=np.linalg.solve(Gxi,Gq)
    Kcond=Rz-Rxi@X_Gz
    Rbar_q=Rq_partial-Rxi@x_Gq
    zq=-np.linalg.solve(Kcond,Rbar_q)
    xiq=-np.linalg.solve(Gxi,Gq+Gz@zq)
    return Kcond,Rbar_q,zq,xiq


def direct_full_newton(Gxi,Gz,Rxi,Rz,G,R):
    J=np.block([[Gxi,Gz],[Rxi,Rz]])
    rhs=-np.concatenate([G,R])
    d=np.linalg.solve(J,rhs)
    n=Gxi.shape[0]
    return d[:n],d[n:]


def direct_full_q_sensitivity(Gxi,Gz,Rxi,Rz,Gq,Rq_partial):
    J=np.block([[Gxi,Gz],[Rxi,Rz]])
    rhs=-np.concatenate([Gq,Rq_partial])
    d=np.linalg.solve(J,rhs)
    n=Gxi.shape[0]
    return d[:n],d[n:]


def benchmark(seed=20260930,nxi=14,nz=3):
    rng=np.random.default_rng(seed)
    A=rng.normal(size=(nxi,nxi))
    Gxi=A.T@A + 3*np.eye(nxi)
    Gz=rng.normal(size=(nxi,nz))
    Rxi=rng.normal(size=(nz,nxi))
    B=rng.normal(size=(nz,nz))
    Rz=B + 4*np.eye(nz)
    G=rng.normal(size=nxi)
    R=rng.normal(size=nz)

    K,rhs,dz,dxi=schur_condense(Gxi,Gz,Rxi,Rz,G,R)
    dxi_f,dz_f=direct_full_newton(Gxi,Gz,Rxi,Rz,G,R)

    Gq=rng.normal(size=nxi)
    Rq=rng.normal(size=nz)
    K2,Rbarq,zq,xiq=condensed_q_sensitivity(Gxi,Gz,Rxi,Rz,Gq,Rq)
    xiq_f,zq_f=direct_full_q_sensitivity(Gxi,Gz,Rxi,Rz,Gq,Rq)

    return {
        "newton_dz_max_abs_diff":float(np.max(np.abs(dz-dz_f))),
        "newton_dxi_max_abs_diff":float(np.max(np.abs(dxi-dxi_f))),
        "q_sensitivity_dz_max_abs_diff":float(np.max(np.abs(zq-zq_f))),
        "q_sensitivity_dxi_max_abs_diff":float(np.max(np.abs(xiq-xiq_f))),
        "cond_Gxi":float(np.linalg.cond(Gxi)),
        "cond_Kcond":float(np.linalg.cond(K)),
        "det_Kcond":float(np.linalg.det(K))
    }


if __name__=="__main__":
    print(benchmark())
