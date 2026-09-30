#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UCFT M8 production input contract.
This file freezes only inputs actually recovered from project sources.
It intentionally refuses to invent unresolved UHPC tensile polynomial coefficients
or whole-face steel-local wave numbers.
"""

ES = 206000.0
NU_S = 0.3
FY = 355.0
EC = 43400.0
NU_C = 0.2
FC = 141.1
EPS_C0 = 0.0035
TS = 4.0
TC = 42.0
AW = 1332.0
Q0 = 0.0025

SPECIMENS = {
    "BH005": {"b": 250.0, "a_h": 500.0, "A0_strip_scale": 0.03515625, "N_plus": None, "m_plus": None, "N_minus": None, "m_minus": None},
    "BH010": {"b": 500.0, "a_h": 1000.0, "A0_strip_scale": 0.0703125, "N_plus": None, "m_plus": None, "N_minus": None, "m_minus": None},
    "BH020": {"b": 1000.0, "a_h": 2000.0, "A0_strip_scale": 0.140625, "N_plus": None, "m_plus": None, "N_minus": None, "m_minus": None},
    "BH032": {"b": 1600.0, "a_h": 3200.0, "A0_strip_scale": 0.225, "N_plus": None, "m_plus": None, "N_minus": None, "m_minus": None},
    "BH050": {"b": 2500.0, "a_h": 5000.0, "A0_strip_scale": 0.3515625, "N_plus": None, "m_plus": None, "N_minus": None, "m_minus": None},
    "BH060": {"b": 3000.0, "a_h": 6000.0, "A0_strip_scale": 0.421875, "N_plus": None, "m_plus": None, "N_minus": None, "m_minus": None},
    "BH070": {"b": 3500.0, "a_h": 7000.0, "A0_strip_scale": 0.4921875, "N_plus": None, "m_plus": None, "N_minus": None, "m_minus": None},
    "BH085": {"b": 4250.0, "a_h": 8500.0, "A0_strip_scale": 0.59765625, "N_plus": None, "m_plus": None, "N_minus": None, "m_minus": None},
    "BH100": {"b": 5000.0, "a_h": 10000.0, "A0_strip_scale": 0.703125, "N_plus": None, "m_plus": None, "N_minus": None, "m_minus": None},
}

def chi_w(b):
    Ac=b*TC
    return 1.0 + AW/Ac*(ES/EC-1.0)

def steel_equivalent_stress(e_bar):
    """M5-compatible project-native ideal-plastic equivalent uniaxial law."""
    ey=FY/ES
    if e_bar <= ey:
        return ES*e_bar
    return FY

def steel_equivalent_tangent(e_bar):
    ey=FY/ES
    if e_bar < ey:
        return ES
    return 0.0

REQUIRED_UNRESOLVED = {
    "UHPC_tension": ["Pt1_coefficients","Pt2_coefficients","epsilon_t_peak","epsilon_t_terminal"],
    "whole_face_local_modes": ["N_plus","m_plus","N_minus","m_minus"],
}

def assert_production_ready():
    unresolved=[]
    for c,d in SPECIMENS.items():
        for key in ("N_plus","m_plus","N_minus","m_minus"):
            if d[key] is None:
                unresolved.append(f"{c}.{key}")
    unresolved += [f"UHPC_tension.{x}" for x in REQUIRED_UNRESOLVED["UHPC_tension"]]
    if unresolved:
        raise RuntimeError("M8 production inputs unresolved: " + ", ".join(unresolved))

if __name__ == "__main__":
    for c,d in SPECIMENS.items():
        print(c, "b=",d["b"],"a_h=",d["a_h"],"chi_w=",chi_w(d["b"]),"A0_strip_scale=",d["A0_strip_scale"])
    try:
        assert_production_ready()
    except RuntimeError as e:
        print(e)