from math import sqrt

# Same reduced reference object used by the persisted NZ-SCCM diagnostic.
a = 6000.0
b = 6000.0
h = 130.0
ts = 4.0
Ac = 732000.0
As = 48000.0
fy = 355.0
fcu = 40.0
fc_prime = 0.76 * fcu
Es = 206000.0
Ec = 32500.0

# Cross-section strength reference, MN.
Psteel0 = fy * As / 1e6
Pconcrete0 = fc_prime * Ac / 1e6
Pyth = Psteel0 + Pconcrete0

# Source-grounded E*I reduced-section diagnostic, per unit width.
Ic = (h - 2.0 * ts) ** 3 / 12.0
Is = (h**3 - (h - 2.0 * ts) ** 3) / 12.0
Dc = Ec * Ic
Ds = Es * Is
D_EI = Dc + Ds
Pcr = 4.0 * 3.141592653589793**2 * D_EI / b / 1e6

# Zhou Siming Eqs. (5-87)-(5-88), four-edge simply-supported axial stability fit.
lambda_n = sqrt(Pyth / Pcr)
if lambda_n <= 1.0:
    Phi_N = 0.454 + 0.192 * lambda_n + 0.416 * lambda_n**2
else:
    Phi_N = -0.140 + 1.387 * lambda_n - 0.186 * lambda_n**2
if lambda_n <= 0.55:
    phi_N = 1.0
else:
    phi_N = 1.0 / (Phi_N + sqrt(Phi_N**2 - lambda_n**2))
Pu_Zhou_empirical = phi_N * Pyth

# Persisted same-object NZ-SCCM diagnostic branch-peak neighbourhood.
# Source: 20260814_1606__NZSCCM__ZHOU_REDUCED__RIGIDITY_AND_STEEL_TANGENT_LOSS_DIAGNOSTIC__EXECUTION_CHECKPOINT.md
# This is NOT relabelled as a newly certified Rq=0 + L=0 production root.
P_NZ = 26.1085

delta = P_NZ - Pu_Zhou_empirical
ratio = P_NZ / Pu_Zhou_empirical
relative_error_percent = delta / Pu_Zhou_empirical * 100.0

print(f"Psteel0 = {Psteel0:.10f} MN")
print(f"Pconcrete0 = {Pconcrete0:.10f} MN")
print(f"Pyth = {Pyth:.10f} MN")
print(f"Ic = {Ic:.12f} mm^3/unit width")
print(f"Is = {Is:.12f} mm^3/unit width")
print(f"D_EI = {D_EI:.6f} N mm")
print(f"Pcr = {Pcr:.12f} MN")
print(f"lambda_n = {lambda_n:.12f}")
print(f"Phi_N = {Phi_N:.12f}")
print(f"phi_N = {phi_N:.12f}")
print(f"Pu_Zhou_empirical = {Pu_Zhou_empirical:.12f} MN")
print(f"P_NZ_diagnostic = {P_NZ:.12f} MN")
print(f"NZ/Zhou = {ratio:.12f}")
print(f"NZ-Zhou = {delta:.12f} MN")
print(f"relative error NZ vs Zhou = {relative_error_percent:.12f} %")
