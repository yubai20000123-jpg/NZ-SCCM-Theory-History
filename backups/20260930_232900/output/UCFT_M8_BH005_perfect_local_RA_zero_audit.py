#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exact symbolic audit of RA at A0=A=0 on BH005 elastic base.
SymPy integrates finite trigonometric polynomials exactly over X,Y in [0,pi].
"""
import sympy as sp
X,Y=sp.symbols("X Y", real=True); pi=sp.pi
b=sp.Rational(250); ah=sp.Rational(500); r=sp.Rational(1,2)
q0=sp.Rational(25,10000); q=sp.Rational(1,100000)
tc=sp.Rational(42); ts=sp.Rational(4); zs=sp.Rational(23)
Ec=sp.Rational(43400); Es=sp.Rational(206000); nu=sp.Rational(3,10)
S=Ec*tc+2*Es*ts
D11=(Ec*tc**3/12+2*Es*(ts**3/12+ts*zs**2))/(1-nu**2)
Q=q*q+2*q0*q; Cq=pi**2*Q/8
Pcr=pi**2*D11*(1+r*r)**2/(b*r*r)
CA=b*S*pi**2*(1+r**4)/(16*r*r)
P=Pcr*q/(q+q0)+CA*Q
Ey=-P/(b*S); Ex=-nu*Ey; Bx=nu*Cq*r*r; By=nu*Cq
C0=sp.Matrix([[1,nu,0],[nu,1,0],[0,0,(1-nu)/2]])/(1-nu**2)
Ce=Es*C0
k0=pi**2*q/b
e0=sp.Matrix([Ex+Bx*sp.cos(2*X)-Cq*sp.cos(2*Y),
              Ey-Cq*r*r*sp.cos(2*X)+By*sp.cos(2*Y),0])
kg=sp.Matrix([k0*sp.sin(X)*sp.sin(Y),
              k0*r*r*sp.sin(X)*sp.sin(Y),
              -2*k0*r*sp.cos(X)*sp.cos(Y)])

def residual_A(N,m,side):
    N=sp.Integer(N); m=sp.Integer(m); s=sp.Integer(side)
    psi=(1-sp.cos(2*N*X))*(1-sp.cos(2*m*Y))
    px=sp.diff(psi,X)*pi/b; py=sp.diff(psi,Y)*pi/ah
    pxx=sp.diff(px,X)*pi/b; pyy=sp.diff(py,Y)*pi/ah
    pxy=sp.diff(px,Y)*pi/ah
    de=sp.Matrix([
      s*pi*(q0+q)*sp.cos(X)*sp.sin(Y)*px,
      s*pi*r*(q0+q)*sp.sin(X)*sp.cos(Y)*py,
      s*pi*(q0+q)*(sp.cos(X)*sp.sin(Y)*py+r*sp.sin(X)*sp.cos(Y)*px)])
    kA=sp.Matrix([-s*pxx,-s*pyy,-2*s*pxy])
    Nres=ts*Ce*(e0+s*zs*kg)
    Mres=(ts**3/12)*Ce*kg
    f=(de.dot(Nres)+kA.dot(Mres))*b*ah/pi**2
    return sp.simplify(sp.integrate(sp.integrate(sp.expand_trig(f),(Y,0,pi)),(X,0,pi)))

for N,m in [(1,1),(2,2)]:
    rp=residual_A(N,m,+1); rm=residual_A(N,m,-1)
    print(N,m,"RA+",sp.N(rp,16),"RA-",sp.N(rm,16))
