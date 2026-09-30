#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UCFT M8 production material/geometry contract — input-freeze v2.

No FEM/experiment Pu target is used here.

UHPC tension
------------
Amplitude: ft = 7.2 MPa from the project-adjacent 2% steel-fibre UHPC
direct material test source (Hu Wenxu project file).

Shape: source-scaled surrogate from Hiew et al. (2024), using the median
dimensionless tensile shape of the three 2% steel-fibre series
SL-2.0 / HL-2.0 / SL-HL-2.0:
  eps_cr=0.00042
  eps_peak=0.00380
  eps_loc=0.00690
  eps_lim=0.00759
  f_cr/f_peak=10.1/11.1
  f_loc/f_peak=10.7/11.1

The initial elastic tangent is forced to the project-locked Ec=43400 MPa.
The post-elastic curve is a finite piecewise cubic PCHIP through the
source-scaled anchors. It is therefore compatible with the M4 analytic
piecewise-polynomial active-set requirement. This is a source-based
production surrogate, not a claim that the exact project's direct-tension
curve was measured at all those strain coordinates.

Steel
-----
M5 consistent secant-Mises operator with ideal elastic-perfectly-plastic
equivalent uniaxial law:
  Es=206000 MPa, nu=0.30, fy=355 MPa.

Whole-face local mode
---------------------
N,m are NOT fitted inputs. They are discrete mode labels selected by the
same reduced equilibrium model:
  - run a perfect-local identification audit (A0+=A0-=0),
  - for each integer candidate pair (N,m), evaluate the local condensed
    tangent on the connected A=0 base path,
  - select the pair whose local condensed tangent/eigenvalue first reaches
    zero,
  - if the selected pair lies on the search-window boundary, expand the
    window and repeat.
This selects a mode, not a new structural DOF.

Local imperfection
------------------
The archived local subplate normalization uses the same
[1-cos][1-cos] shape and Bs=0.225 b with A0=Bs/1600. Since the current
whole-face psi has the same peak normalization max(psi)=4, retain the
coefficient
  A0 = 0.225 b / 1600.
The physical peak initial local geometry is 4*A0.
"""

from dataclasses import dataclass
import math
import numpy as np

EC=43400.0
NUC=0.20
FC=141.1
EPS_C0=0.0035
FT=7.2

ES=206000.0
NUS=0.30
FY=355.0

TC=42.0
TS=4.0
AW=1332.0
Q0=0.0025

# Tension anchors
FCR_RATIO=10.1/11.1
FLOC_RATIO=10.7/11.1
FCR=FT*FCR_RATIO
FLOC=FT*FLOC_RATIO
EPS_EL=FCR/EC
EPS_CR=0.00042
EPS_TP=0.00380
EPS_LOC=0.00690
EPS_TU=0.00759

# Polynomial coefficients in local coordinate s=e-e_left,
# c0+c1*s+c2*s^2+c3*s^3.
TENSION_SEGMENTS = [
    (0.000150952796114, 0.00042, (6.551351351351352, 0, 0, 0)),
    (0.00042, 0.0038, (6.551351351351352, 0, 170332.4416114583, -33596142.3296762)),
    (0.0038, 0.0069, (7.2, 0, -13340.72656647135, -4405863.420350799)),
    (0.0069, 0.00759, (6.94054054054054, -209.733547120836, -25915945.17534444, 16872466522.84817)),
]


def _poly_local(e, left, coeff):
    s=e-left
    c0,c1,c2,c3=coeff
    return ((c3*s+c2)*s+c1)*s+c0

def _dpoly_local(e, left, coeff):
    s=e-left
    _,c1,c2,c3=coeff
    return (3*c3*s+2*c2)*s+c1

def uhpc_tension_stress(e):
    e=float(e)
    if e <= 0.0:
        return 0.0
    if e <= EPS_EL:
        return EC*e
    if e > EPS_TU:
        return 0.0
    for left,right,c in TENSION_SEGMENTS:
        if e <= right+1e-15:
            return _poly_local(e,left,c)
    return 0.0

def uhpc_tension_tangent(e):
    e=float(e)
    if e < 0.0 or e > EPS_TU:
        return 0.0
    if e < EPS_EL:
        return EC
    for left,right,c in TENSION_SEGMENTS:
        if e <= right+1e-15:
            return _dpoly_local(e,left,c)
    return 0.0


@dataclass(frozen=True)
class Specimen:
    name:str
    b:float
    a_h:float

    @property
    def chi_w(self):
        Ac=self.b*TC
        return 1.0+AW/Ac*(ES/EC-1.0)

    @property
    def B_strip(self):
        return 0.225*self.b

    @property
    def A0_local_coefficient(self):
        return self.B_strip/1600.0

    @property
    def A0_local_peak(self):
        return 4.0*self.A0_local_coefficient


SPECIMENS = [
    Specimen("BH005",250.0,500.0),
    Specimen("BH010",500.0,1000.0),
    Specimen("BH020",1000.0,2000.0),
    Specimen("BH032",1600.0,3200.0),
    Specimen("BH050",2500.0,5000.0),
    Specimen("BH060",3000.0,6000.0),
    Specimen("BH070",3500.0,7000.0),
    Specimen("BH085",4250.0,8500.0),
    Specimen("BH100",5000.0,10000.0),
]


def choose_first_local_mode(event_q_by_mode, initial_max_mode=12):
    """
    event_q_by_mode: dict[(N,m)] -> first q at which the PERFECT-LOCAL
    condensed local tangent/eigenvalue reaches zero. Use +inf if no event
    on the tracked base path.

    Returns the earliest event pair, but refuses to freeze a pair lying on
    the candidate-window boundary: the caller must enlarge the window.
    """
    finite=[(q,N,m) for (N,m),q in event_q_by_mode.items()
            if np.isfinite(q)]
    if not finite:
        raise RuntimeError("No local tangent event was found in the current candidate window.")
    q,N,m=min(finite)
    maxN=max(k[0] for k in event_q_by_mode)
    maxm=max(k[1] for k in event_q_by_mode)
    if N in (1,maxN) or m in (1,maxm):
        raise RuntimeError(
            f"Selected mode ({N},{m}) is on candidate-window boundary; "
            "expand the integer search window before freezing the mode."
        )
    return {"N":int(N),"m":int(m),"q_event":float(q)}


def local_mode_identification_rule():
    return {
      "base_state":"same specimen connected global/C1 base path",
      "identification_imperfection":"A0+=A0-=0 only during mode identification",
      "candidate_start":"N,m=1..12",
      "selection":"earliest zero of exact inner-condensed local tangent/eigenvalue",
      "boundary_rule":"expand candidate window if selected mode is on a search boundary",
      "after_selection":"restore specimen A0=0.225*b/1600 and solve imperfect local path",
      "fit_to_FEM":False,
    }


def assert_production_ready():
    # material continuity / positivity checks
    assert abs(uhpc_tension_stress(0.0)) < 1e-12
    assert abs(uhpc_tension_stress(EPS_TP)-FT) < 1e-10
    assert abs(uhpc_tension_stress(EPS_TU)) < 1e-10
    assert abs(uhpc_tension_stress(EPS_EL)-FCR) < 1e-10
    assert len(SPECIMENS)==9
    assert all(s.a_h==2*s.b for s in SPECIMENS)
    assert all(s.A0_local_coefficient>0 for s in SPECIMENS)
    return True


if __name__ == "__main__":
    print("production_ready:",assert_production_ready())
    print(local_mode_identification_rule())
    for s in SPECIMENS:
        print(s.name,s.b,s.a_h,s.chi_w,s.A0_local_coefficient,s.A0_local_peak)
