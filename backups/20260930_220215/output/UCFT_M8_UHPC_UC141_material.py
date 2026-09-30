#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UCFT M8 production UHPC_UC141 monotonic backbone reconstructed from final Abaqus INP.

Abaqus CDP tabular coordinates:
  compression hardening: (sigma_c>0, inelastic_strain)
  tension stiffening STRAIN: (sigma_t>0, cracking_strain)

For the monotonic uniaxial envelope with initial modulus E0,
    eps_total = eps_inelastic_or_cracking + sigma/E0.
Abaqus tabular interpolation is linear in the tabulated strain variable; because the
mapping to total strain is affine within each segment, sigma(eps_total) is also exactly
piecewise linear between the transformed knots.

UCFT sign convention here: tension e>0, compression e<0 and stress has same sign.
The CDP damage tables are retained as provenance/diagnostic data only; they are not
silently converted into a history-damage law in the current low-dimensional theory.
"""
from __future__ import annotations
from dataclasses import dataclass
import bisect, math

E0 = 43400.0
NU = 0.30
RHO = 2.5e-9

COMPRESSION_HARDENING = [
(119.49,0.0),(132.75,9.13521e-05),(141.1,0.000248848),(138.58,0.000656904),
(132.28,0.00115204),(123.94,0.00169426),(114.85,0.00225371),(112.11,0.00242185),
(108.49,0.00264516),(105.83,0.00281164),(101.49,0.00308658),(98.96,0.00324981),
(97.31,0.00335783),(89.5,0.0038877),(87.31,0.00404324),(84.49,0.00424814),
(82.46,0.00439998),(76.16,0.00489512),(70.55,0.00537442),(53.58,0.00716538),
(42.57,0.00881905),(35.06,0.0103923),(29.67,0.0119163),(25.65,0.0134089),
(22.56,0.0148802),(20.11,0.0163367),(19.99,0.0164134),(16.49,0.0192201),
(15.12,0.0206517),(12.5,0.0242119)]

TENSION_STIFFENING = [
(5.571309,0.0),(6.203384,0.000246),(6.63126,0.000333),(6.919437,0.000424),
(7.107793,0.000517),(7.222692,0.000611),(7.282395,0.000707),(7.3,0.000804),
(7.285159,0.000901),(7.245135,0.000999),(7.18549,0.001098),(7.110544,0.001197),
(7.02369,0.001296),(6.92762,0.001396),(6.824487,0.001495),(6.716025,0.001595),
(6.603636,0.001695),(6.488463,0.001794),(5.898099,0.002294),(5.3246,0.002793),
(4.793703,0.003292),(4.312849,0.003789),(2.851377,0.005766)]

COMPRESSION_DAMAGE = [
(0,0),(0.014607,9.13521e-05),(0.0362051,0.000248848),(0.0892994,0.000656904),
(0.148118,0.00115204),(0.207765,0.00169426),(0.265113,0.00225371),(0.28159,0.00242185),
(0.302951,0.00264516),(0.318494,0.00281164),(0.34346,0.00308658),(0.357869,0.00324981),
(0.367238,0.00335783),(0.411269,0.0038877),(0.42359,0.00404324),(0.439408,0.00424814),
(0.450827,0.00439998),(0.486296,0.00489512),(0.518103,0.00537442),(0.616623,0.00716538),
(0.683619,0.00881905),(0.731449,0.0103923),(0.767066,0.0119163),(0.794518,0.0134089),
(0.816278,0.0148802),(0.833927,0.0163367),(0.834769,0.0164134),(0.860772,0.0192201),
(0.871207,0.0206517),(0.891565,0.0242119)]

TENSION_DAMAGE = [
(0,0),(0.393674,0.000246),(0.439294,0.000333),(0.477144,0.000424),
(0.509385,0.000517),(0.537378,0.000611),(0.562037,0.000707),(0.584009,0.000804),
(0.603772,0.000901),(0.621684,0.000999),(0.638025,0.001098),(0.653016,0.001197),
(0.666835,0.001296),(0.679628,0.001396),(0.691516,0.001495),(0.702599,0.001595),
(0.712964,0.001695),(0.722682,0.001794),(0.763513,0.002294),(0.794881,0.002793),
(0.819813,0.003292),(0.840127,0.003789),(0.893861,0.005766)]

@dataclass(frozen=True)
class LinearBranch:
    lo: float
    hi: float
    m: float
    c: float
    F_c: float
    H_c: float
    label: str

def _raw_total_knots():
    comp=[(- (ein + sig/E0), -sig) for sig,ein in COMPRESSION_HARDENING]
    comp=sorted(comp)
    tens=[(ecr + sig/E0, sig) for sig,ecr in TENSION_STIFFENING]
    return comp, tens

def _build_branches():
    comp,tens=_raw_total_knots()
    nodes=sorted(comp+[(0.0,0.0)]+tens)
    seg=[]
    for (e0,s0),(e1,s1) in zip(nodes[:-1],nodes[1:]):
        m=(s1-s0)/(e1-e0); c=s0-m*e0
        seg.append((e0,e1,m,c))
    iz=max(i for i,(a,b,_,__) in enumerate(seg) if a < 0 <= b)
    out=[None]*len(seg)
    a,b,m,c=seg[iz]
    out[iz]=LinearBranch(a,b,m,c,0.0,0.0,"compression_to_origin")
    def Fval(e,m,c,Fc): return 0.5*m*e*e+c*e+Fc
    def Hval(e,m,c,Hc): return (m/3)*e**3+0.5*c*e*e+Hc
    prev=out[iz]
    for j in range(iz+1,len(seg)):
        a,b,m,c=seg[j]
        targetF=Fval(a,prev.m,prev.c,prev.F_c)
        targetH=Hval(a,prev.m,prev.c,prev.H_c)
        Fc=targetF-(0.5*m*a*a+c*a)
        Hc=targetH-((m/3)*a**3+0.5*c*a*a)
        out[j]=LinearBranch(a,b,m,c,Fc,Hc,"tension")
        prev=out[j]
    nxt=out[iz]
    for j in range(iz-1,-1,-1):
        a,b,m,c=seg[j]
        targetF=Fval(b,nxt.m,nxt.c,nxt.F_c)
        targetH=Hval(b,nxt.m,nxt.c,nxt.H_c)
        Fc=targetF-(0.5*m*b*b+c*b)
        Hc=targetH-((m/3)*b**3+0.5*c*b*b)
        out[j]=LinearBranch(a,b,m,c,Fc,Hc,"compression")
        nxt=out[j]
    return nodes,out

NODES,BRANCHES=_build_branches()
KNOT_STRAINS=[e for e,_ in NODES]
KNOT_STRESSES=[s for _,s in NODES]

def branch_index(e: float) -> int:
    if e <= KNOT_STRAINS[0]: return 0
    if e >= KNOT_STRAINS[-1]: return len(BRANCHES)-1
    return max(0,min(len(BRANCHES)-1,bisect.bisect_right(KNOT_STRAINS,e)-1))

def stress(e: float) -> float:
    if e <= KNOT_STRAINS[0]: return KNOT_STRESSES[0]
    if e >= KNOT_STRAINS[-1]: return KNOT_STRESSES[-1]
    b=BRANCHES[branch_index(e)]
    return b.m*e+b.c

def tangent(e: float) -> float:
    if e <= KNOT_STRAINS[0] or e >= KNOT_STRAINS[-1]: return 0.0
    return BRANCHES[branch_index(e)].m

def primitive_F(e: float) -> float:
    if e <= KNOT_STRAINS[0]:
        b=BRANCHES[0]; ek=KNOT_STRAINS[0]
        return 0.5*b.m*ek**2+b.c*ek+b.F_c + KNOT_STRESSES[0]*(e-ek)
    if e >= KNOT_STRAINS[-1]:
        b=BRANCHES[-1]; ek=KNOT_STRAINS[-1]
        base=0.5*b.m*ek**2+b.c*ek+b.F_c
        return base+KNOT_STRESSES[-1]*(e-ek)
    b=BRANCHES[branch_index(e)]
    return 0.5*b.m*e*e+b.c*e+b.F_c

def primitive_H(e: float) -> float:
    if e <= KNOT_STRAINS[0]:
        b=BRANCHES[0]; ek=KNOT_STRAINS[0]
        base=(b.m/3)*ek**3+0.5*b.c*ek**2+b.H_c
        return base+0.5*KNOT_STRESSES[0]*(e*e-ek*ek)
    if e >= KNOT_STRAINS[-1]:
        b=BRANCHES[-1]; ek=KNOT_STRAINS[-1]
        base=(b.m/3)*ek**3+0.5*b.c*ek**2+b.H_c
        return base+0.5*KNOT_STRESSES[-1]*(e*e-ek*ek)
    b=BRANCHES[branch_index(e)]
    return (b.m/3)*e**3+0.5*b.c*e*e+b.H_c

def summary():
    comp,tens=_raw_total_knots()
    peak_c=min(comp,key=lambda p:p[1])
    peak_t=max(tens,key=lambda p:p[1])
    return {
      "E0_MPa":E0,"nu":NU,
      "compression_first_total_strain":-comp[-1][0],
      "compression_peak_stress_MPa":-peak_c[1],
      "compression_peak_total_strain":-peak_c[0],
      "compression_last_total_strain":-comp[0][0],
      "compression_last_stress_MPa":-comp[0][1],
      "tension_first_total_strain":tens[0][0],
      "tension_peak_stress_MPa":peak_t[1],
      "tension_peak_total_strain":peak_t[0],
      "tension_last_total_strain":tens[-1][0],
      "tension_last_stress_MPa":tens[-1][1],
      "n_piecewise_linear_segments":len(BRANCHES),
    }

if __name__=='__main__':
    print(summary())
    err=max(abs(stress(e)-s) for e,s in NODES)
    print('max_knot_stress_error',err)
