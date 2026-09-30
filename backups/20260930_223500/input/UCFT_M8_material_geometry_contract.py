#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UCFT M8 production material/geometry contract — input-freeze v3 (actual final INP UHPC_UC141).

No FEM/test Pu target enters this contract.

UHPC production monotonic backbone
----------------------------------
The UHPC normal-stress backbone is reconstructed directly from the user's final
Abaqus INP material UHPC_UC141. For compression hardening and tension
stiffening(STRAIN), total uniaxial strain is
    eps_total = eps_inelastic_or_cracking + sigma/Ec.
Because Abaqus linearly interpolates each tabular branch in its supplied strain
coordinate, this affine change of coordinate yields an exactly piecewise-linear
sigma(eps_total) backbone. The resulting finite piecewise-linear law is therefore
an exact representation of the submitted monotonic tabular envelope, not a fit.

The CDP dilation angle, eccentricity, fb0/fc0, Kc, viscosity, and damage tables
remain recorded FEM-material provenance. They are NOT silently promoted into
new coefficients/history variables of the current low-dimensional directional
UHPC operator.
"""
from dataclasses import dataclass
import numpy as np
from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import UCFT_M8_UHPC_UC141_material as UHPC

EC=UHPC.E0
NUC=UHPC.NU
FC=141.1
EPS_C0=UHPC.summary()["compression_peak_total_strain"]
FT=UHPC.summary()["tension_peak_stress_MPa"]
EPS_TP=UHPC.summary()["tension_peak_total_strain"]

RHO_UHPC=UHPC.RHO
CDP_DILATION_DEG=36.0
CDP_ECCENTRICITY=0.1
CDP_FB0_FC0=1.16
CDP_KC=0.6667
CDP_VISCOSITY=1.0e-5

ES=206000.0
NUS=0.30
FY=355.0
TC=42.0
TS=4.0
AW=1332.0
Q0=0.0025

uhpc_stress=UHPC.stress
uhpc_tangent=UHPC.tangent
uhpc_F=UHPC.primitive_F
uhpc_H=UHPC.primitive_H
UHPC_KNOT_STRAINS=UHPC.KNOT_STRAINS
UHPC_KNOT_STRESSES=UHPC.KNOT_STRESSES
UHPC_BRANCHES=UHPC.BRANCHES

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
    Specimen("BH005",250.0,500.0), Specimen("BH010",500.0,1000.0),
    Specimen("BH020",1000.0,2000.0), Specimen("BH032",1600.0,3200.0),
    Specimen("BH050",2500.0,5000.0), Specimen("BH060",3000.0,6000.0),
    Specimen("BH070",3500.0,7000.0), Specimen("BH085",4250.0,8500.0),
    Specimen("BH100",5000.0,10000.0),
]

def choose_first_local_mode(event_q_by_mode, initial_max_mode=12):
    finite=[(q,N,m) for (N,m),q in event_q_by_mode.items() if np.isfinite(q)]
    if not finite:
        raise RuntimeError("No local tangent event was found in the current candidate window.")
    q,N,m=min(finite)
    maxN=max(k[0] for k in event_q_by_mode)
    maxm=max(k[1] for k in event_q_by_mode)
    if N in (1,maxN) or m in (1,maxm):
        raise RuntimeError(f"Selected mode ({N},{m}) is on candidate-window boundary; expand the integer search window before freezing the mode.")
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
    s=UHPC.summary()
    assert abs(uhpc_stress(0.0)) < 1e-12
    assert abs(s["compression_peak_stress_MPa"]-141.1) < 1e-12
    assert abs(s["compression_peak_total_strain"]-0.003500000073732719) < 1e-14
    assert abs(s["tension_peak_stress_MPa"]-7.3) < 1e-12
    assert abs(s["tension_peak_total_strain"]-0.0009722027649769585) < 1e-14
    assert NUC==0.30
    assert len(SPECIMENS)==9
    assert all(s.a_h==2*s.b for s in SPECIMENS)
    return True

if __name__ == "__main__":
    print("production_ready:",assert_production_ready())
    print("UHPC:",UHPC.summary())
    print(local_mode_identification_rule())
    for s in SPECIMENS:
        print(s.name,s.b,s.a_h,s.chi_w,s.A0_local_coefficient,s.A0_local_peak)
