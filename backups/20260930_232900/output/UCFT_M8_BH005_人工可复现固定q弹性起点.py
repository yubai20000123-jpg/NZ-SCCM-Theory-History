#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BH005 first human-reproducible fixed-q elastic base point.
No spatial Gauss quadrature defines the residual.
"""
import math, numpy as np

b=250.0; ah=500.0; r=b/ah; q0=0.0025; q=1e-5
tc=42.0; ts=4.0; zs=tc/2+ts/2
Ec=43400.0; Es=206000.0; nu=0.30; fy=355.0; Aw=1332.0

S=Ec*tc+2*Es*ts
A11=S/(1-nu**2)
A66=S/(2*(1+nu))
D11=(Ec*tc**3/12+2*Es*(ts**3/12+ts*zs**2))/(1-nu**2)
Q=q*q+2*q0*q
Cq=math.pi**2*Q/8
Cqp=math.pi**2*(q+q0)/4
area=b*ah

R0=np.array([
0,0,
-area*A11*nu*Cq*r*r/2,
-area*A11*nu*Cq/2,
0,0,
area*A11*Cqp*Cq*(1+r**4)/2
+q*area*math.pi**4*D11*(1+r*r)**2/(4*b*b)
],float)

J=np.zeros((7,7))
J[0,0]=area*A11; J[0,1]=area*A11*nu
J[1,0]=area*A11*nu; J[1,1]=area*A11; J[1,6]=ah
J[2,2]=area*A11/2; J[3,3]=area*A11/2
J[4,4]=area*(A11+A66*r*r)/4
J[4,5]=area*(nu*A11+A66)/4
J[5,4]=area*(nu*A11+A66)/4
J[5,5]=area*(A11+A66/(r*r))/4
J[6,2]=-area*A11*Cqp*nu*r*r/2
J[6,3]=-area*A11*Cqp*nu/2
J[6,6]=-ah*r*r*Cqp

dx=np.linalg.solve(J,-R0)
Ex,Ey,Bx,By,Hx,Hy,P=dx
R1=R0+J@dx
Pc=-b*Ec*tc*Ey
Ps=-b*Es*ts*Ey
chi=1+Aw/(b*tc)*(Es/Ec-1)
Prep=chi*Pc+2*Ps
Delta=-ah*(Ey-Cq*r*r)

k0=math.pi**2*q/b
et1=5.571309/Ec
ec1=119.49/Ec
ex_bound=Cq+(tc/2)*k0*(1+nu*r*r)/(1-nu**2)
ey_dev=Cq*r*r+(tc/2)*k0*(r*r+nu)/(1-nu**2)

C0=np.array([[1,nu,0],[nu,1,0],[0,0,(1-nu)/2]],float)/(1-nu**2)
W=np.array([[1,-.5,0],[-.5,1,0],[0,0,3.0]])
H=C0.T@W@C0
base=np.array([Ex,Ey,0.0])
ebase=math.sqrt(base@H@base)
de=np.array([
 Cq*(1+nu*r*r)+25*k0,
 Cq*(r*r+nu)+25*r*r*k0,
 25*2*r*k0
])
ebar_upper=ebase+math.sqrt(np.linalg.eigvalsh(H).max())*np.linalg.norm(de)

print("R0",R0)
print("state",dx)
print("R1",R1)
print("P_kN",P/1000)
print("Pc_kN",Pc/1000,"Ps_each_kN",Ps/1000)
print("chi_w",chi,"P_report_kN",Prep/1000)
print("Delta_mm",Delta)
print("UHPC_ex_abs_bound",ex_bound,"tension_threshold",et1)
print("UHPC_ey_interval",Ey-ey_dev,Ey+ey_dev,"compression_threshold",-ec1)
print("steel_ebar_upper",ebar_upper,"yield_strain",fy/Es)
