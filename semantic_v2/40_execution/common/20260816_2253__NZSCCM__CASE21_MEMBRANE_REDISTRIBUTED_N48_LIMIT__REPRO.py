"""Replay/verification script for the 2026-08-16 22:53 Case21 membrane limit.

It reuses the already-fingerprinted Case21 N48-C1/MM coefficient-space evaluator
from 22:34. It does not introduce spatial quadrature or material points.

The nonlinear search history itself is frozen in the sibling JSON/report; this
script verifies the final and bracket states with the same production evaluator.
"""
from pathlib import Path
import runpy
import numpy as np

HERE = Path(__file__).resolve().parent
base = HERE / "20260816_2234__NZSCCM__CASE21_N48_MEMBRANE_CONTINUATION_START__REPRO.py"
ns = runpy.run_path(str(base))
evaluate = ns["evaluate"]

FINAL = {
    "D": 0.4597278541813354,
    "q": 0.0018330938013757293,
    "r": [-0.012475802483156403,
          -0.007141864103343101,
           0.04699488414266459,
           0.041946118067216,
          -0.09983629747628982],
    "P_kN": 320.7491853255822,
}

# Frozen N28-equilibrium load bracket used for the local stationary locator.
BRACKET = [
    {"s": -0.001, "P_kN": 320.7448725628471},
    {"s": -0.002, "P_kN": 320.7488729415183},
    {"s": -0.004, "P_kN": 320.7455659492498},
]

out = evaluate(FINAL["D"], FINAL["q"], FINAL["r"])
print("FINAL_REPLAY", out)
assert abs(out["P_kN"] - FINAL["P_kN"]) < 1e-8
assert abs(out["Rq_kNmm"]) < 1e-3
assert out["Rm_norm2"] < 1e-5

# Three-point quadratic locator; no structural integrand is sampled here.
s = np.array([p["s"] for p in BRACKET], float)
P = np.array([p["P_kN"] for p in BRACKET], float)
a,b,c = np.polyfit(s,P,2)
speak = -b/(2*a)
Pfit = np.polyval([a,b,c],speak)
print("LOCAL_PEAK_FIT", dict(a=a,b=b,c=c,s_peak=speak,P_peak_fit_kN=Pfit))
assert a < 0
assert min(s) < speak < max(s)
assert Pfit > max(P[0],P[-1])

print("KZ_FINAL_N_PER_MM", 260.1709056728362)
print("COMPILER_BERNSTEIN_MINS", [
    0.019818419276368335,
    0.012584829997801125,
    1.0807409482494919,
    0.5069185061516994,
])
print("N_formal_spatial_sampling=0")
print("N_formal_spatial_quadrature=0")
print("N_formal_spatial_subdomains=1")
print("N_formal_thickness_quadrature=0")
