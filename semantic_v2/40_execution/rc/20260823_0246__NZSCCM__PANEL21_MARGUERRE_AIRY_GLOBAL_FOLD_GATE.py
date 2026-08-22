from __future__ import annotations

"""Panel21 Marguerre–Airy explicit global-fold gate.

Purpose
-------
1. Reproduce the current locked RC Marguerre–Airy elastic structural backbone
   with the corrected Swartz reinforcement mapping rho_x=rho_y=p_total/2.
2. Select the elastic halfwave number from the specimen itself.
3. Build the exact one-mode Airy/Galerkin postbuckling law
       P_pb(q)=P_cr*q/(q+q0)+C*q*(q+2*q0).
4. Test the *global structural fold* condition dP_pb/dq=0.

No experiment is used in root selection.  No spatial quadrature, material-point
sampling, load stepping or path continuation is used.

Important interpretation
------------------------
This script deliberately does NOT impose any local N-M capacity or det(J_sec)=0
terminal condition.  Therefore if dP_pb/dq has no positive root, the correct
result is "NO FINITE GLOBAL FOLD IN V1", not an invented Pu.
"""

import math

# ---- Panel21 frozen raw inputs ---------------------------------------------
a_phys = 2440.0   # mm
b = 1220.0        # mm
t = 19.30         # mm
E0 = 20321.0      # MPa
nu = 0.18
Es = 200000.0     # MPa
p_total = 0.0075  # nominal total two-way reinforcement ratio
q0 = 1.0 / 400.0
z_layer = 0.0     # mm, one central layer

# Correct Nguyen/Swartz mapping: total two-way ratio is split by direction.
rho_x = p_total / 2.0
rho_y = p_total / 2.0
ax = rho_x * t    # mm^2/mm
ay = rho_y * t

# ---- RC A matrix -----------------------------------------------------------
Qc = E0 / (1.0 - nu**2)
Qc12 = nu * E0 / (1.0 - nu**2)
Qc66 = E0 / (2.0 * (1.0 + nu))
t_conc = t - ax - ay

A11 = Qc * t_conc + Es * ax
A22 = Qc * t_conc + Es * ay
A12 = Qc12 * t_conc
A66 = Qc66 * t_conc
DeltaA = A11 * A22 - A12**2

# ---- RC D matrix; central rebar has z=0 so it contributes no layer z^2 term
Ieff = t**3 / 12.0
Dx = Qc * Ieff
Dy = Qc * Ieff
Dmu = Qc12 * Ieff
D66 = Qc66 * Ieff
H = Dmu + 2.0 * D66

alpha = math.pi / b

# ---- specimen-selected integer halfwave -----------------------------------
def pcr_for_j(j: int) -> float:
    beta_j = j * math.pi / a_phys
    ncr = (
        Dx * alpha**4
        + 2.0 * H * alpha**2 * beta_j**2
        + Dy * beta_j**4
    ) / beta_j**2
    return b * ncr  # N

candidates = [(j, pcr_for_j(j)) for j in range(1, 7)]
m_star, Pcr = min(candidates, key=lambda x: x[1])
ell = a_phys / m_star
beta = math.pi / ell

# ---- exact Airy/Galerkin coefficients -------------------------------------
Kb = Dx * alpha**4 + 2.0 * H * alpha**2 * beta**2 + Dy * beta**4
Pcr_check = b * Kb / beta**2
assert abs(Pcr_check - Pcr) < 1e-8

Km = DeltaA / 16.0 * (alpha**4 / A22 + beta**4 / A11)
C = b**3 * Km / beta**2  # N

# Airy membrane-redistribution coefficient in
# n(x)=P/b+G*q(q+2q0)*cos(2 alpha x)
G = beta**2 * b**2 * DeltaA / (8.0 * A11)  # N/mm

# ---- global one-coordinate postbuckling path ------------------------------
def P_pb(q: float) -> float:
    return Pcr * q / (q + q0) + C * q * (q + 2.0 * q0)


def dP_dq(q: float) -> float:
    # Exact derivative.  For q>=0, q0>0, Pcr>0 and C>0 both terms are positive.
    return Pcr * q0 / (q + q0) ** 2 + 2.0 * C * (q + q0)


assert q0 > 0.0 and Pcr > 0.0 and C > 0.0
assert all(dP_dq(q) > 0.0 for q in (0.0, 1e-4, 5e-4, 1e-3, 2e-3, 4e-3, 8e-3, 2e-2))

print("PANEL21_MA_V1_GLOBAL_FOLD_GATE")
print(f"rho_x = rho_y = {rho_x:.8f}")
print(f"ax = ay = {ax:.9f} mm")
print(f"t_conc = {t_conc:.9f} mm")
print()
print("A/D coefficients")
for name, value in (
    ("A11", A11), ("A22", A22), ("A12", A12), ("A66", A66),
    ("DeltaA", DeltaA), ("Dx", Dx), ("Dy", Dy), ("Dmu", Dmu),
    ("D66", D66), ("H", H),
):
    print(f"{name} = {value:.12g}")
print()
print("Elastic halfwave candidates")
for j, p in candidates:
    print(f"j={j}: ell={a_phys/j:.9f} mm, Pcr={p/1000:.9f} kN")
print(f"m_star = {m_star}")
print(f"ell = {ell:.9f} mm")
print()
print(f"Pcr = {Pcr/1000:.12f} kN")
print(f"Km = {Km:.12g}")
print(f"C = {C/1000:.12f} kN")
print(f"G = {G:.12f} N/mm")
print()
print("P_pb(q) = Pcr*q/(q+q0) + C*q*(q+2*q0)")
print("dP_pb/dq = Pcr*q0/(q+q0)^2 + 2*C*(q+q0)")
print()
for q in (0.0, 0.002, 0.004, 0.006, 0.008, 0.010, 0.020):
    print(f"q={q:.6f}: P={P_pb(q)/1000:.9f} kN, dP/dq={dP_dq(q)/1000:.9f} kN")
print()
print("GLOBAL_FOLD_ROOT = NONE_FOR_q_GE_0")
print("MA_V1_GEOMETRIC_GLOBAL_FOLD = PROVEN_ABSENT")
print("FINITE_Pu_WITHOUT_LOCAL_CAPACITY_OR_GLOBAL_MATERIAL_DEGRADATION = NOT_DEFINED")
