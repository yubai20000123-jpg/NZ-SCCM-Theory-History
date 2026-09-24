# STATUS OVERRIDE — R04 24-point quadrature results withdrawn

Per user instruction on 2026-09-24, all 24x24 / 16 / 14 Gauss-point evaluations in R04 are withdrawn and must not be used as formal results, initialization evidence, precision evidence, or convergence evidence for the Eq.(1)–(149) calculation. The 10-scalar equation count is retained; only the spatial quadrature backend is rejected.

# Eq.(1)–(149) R04 — 10-scalar Chen-Ji §8.8 closure

Date: 2026-09-24

## 1. Variable count

For the current formulation, once the already-established Chen-Ji §8.8/H1 finite admissible field is substituted, the prescribed-shortening problem is a **10-scalar nonlinear system**:

q, Aplus, Aminus, epsx_bar, epsy_bar, ex_alpha, ey_beta, Fx, Fy, P.

The older 8-variable H1 system omitted Aplus/Aminus from the global solve because steel-local amplitudes were internally condensed. In Eq.(114)/(119) of the current formulation, Aplus/Aminus are explicit structural equilibrium variables. Therefore current count = 8 + 2 = 10.

If Delta is also solved as an unknown and dP/dDelta=0 is imposed directly, the one-shot stationary system is 11-scalar.

## 2. Chen-Ji §8.8/H1 closure

Let Q=q^2+2 q0 q.

Compatible membrane strains:
eps_x0 = epsx_bar + ex_alpha cos(2pi x/b) - (pi^2/8) Q cos(2pi y/a_h)

eps_y0 = epsy_bar - (pi^2 b^2/(8 a_h^2)) Q cos(2pi x/b) + ey_beta cos(2pi y/a_h)

gamma_xy0 = 0.

This field satisfies Eq.(28) exactly.

Airy retained space:
Phi = -P x^2/(2b) + Fx cos(2pi x/b) + Fy cos(2pi y/a_h).

Hence:
Nx_Airy = -4pi^2 Fy/a_h^2 cos(2pi y/a_h)
Ny_Airy = -P/b -4pi^2 Fx/b^2 cos(2pi x/b)
Nxy_Airy = 0.

This is a Chen-Ji §8.8 special admissible subspace, not the full general four-field Eq.(92) system.

## 3. Ten equations

R1 = <Nx_current> = 0
R2 = 2<Nx_current cos(2pi x/b)> = 0
R3 = 2<Nx_current cos(2pi y/a_h)> + 4pi^2 Fy/a_h^2 = 0
R4 = <Ny_current> + P/b = 0
R5 = 2<Ny_current cos(2pi x/b)> + 4pi^2 Fx/b^2 = 0
R6 = 2<Ny_current cos(2pi y/a_h)> = 0
R7 = Eq.(114) TOP local virtual-work equilibrium
R8 = Eq.(119) BOTTOM local virtual-work equilibrium
R9 = Eq.(109) global-q equilibrium
R10 = Eq.(123) shortening compatibility.

No H5 U/V coefficients are used.

## 4. Numerical integration backend

The algebraic unknown count remains 10. Numerical quadrature points are **not unknowns**.

Current prototype evaluates the nonlinear residual integrals with:
- 24x24 Gauss-Legendre points in x-y,
- 16 points through UHPC thickness,
- 14 points through each steel thickness.

Reason: after current signed-C1 and algebraic Mises limiting are substituted, the integrands are piecewise nonlinear and the x-y switching curves depend on the current root. A closed fixed trigonometric primitive has not yet been derived. Therefore these points are used only as an integration evaluator. This is explicitly a numerical backend, not a formal analytic replacement.

Convergence spot checks at the same q state:
- BH032: 24 -> 13.1338 MN; 32 -> 13.1485 MN (0.11%)
- BH050: 24 -> 15.2526 MN; 32 -> 15.1705 MN (-0.54%)
- BH070: 24 -> 15.0405 MN; 32 -> 14.8468 MN (-1.29%)

Thus the 24-point table below is useful for mechanics/path diagnosis, but not yet the final zero-quadrature analytic table.

## 5. Current 24-point connected-branch peak candidates

BH005: Pu=2.49513 MN, q=8.5e-5, Delta=1.76784 mm
BH010: Pu=4.69726 MN, q=3.30e-4, Delta=3.47978 mm
BH020: Pu=8.78496 MN, q=1.55e-3, Delta=6.90446 mm
BH032: Pu=13.13365 MN, q=6.8e-3, Delta=10.00165 mm
BH050: Pu=15.25260 MN, q=1.52e-2, Delta=12.15205 mm
BH060: Pu=15.47009 MN, q=1.52e-2, Delta=12.22398 mm
BH070: Pu=15.04045 MN, q=1.40e-2, Delta=11.56081 mm

For BH085 and BH100, q-control reaches a local fold. To stay on the same positive-total-local-amplitude connected branch, Aminus was temporarily used as the numerical continuation parameter while the same equilibrium equations were solved. No new physical unknown or constitutive equation was introduced.

BH085 connected fold peak: Pu=12.13530 MN, q=0.01062665, Delta=9.28105 mm.
BH100 connected fold peak: Pu=10.00207 MN, q=0.00892281, Delta=7.83812 mm.

All listed connected fold/peak states preserve A0plus+Aplus>0 and A0minus+Aminus>0.

## 6. Important status

This R04 supersedes the R02 64-variable H5 implementation as the relevant scalar implementation. R02 remains diagnostic only.

R04 does NOT claim to be the full general Eq.(92) field solution, because Chen-Ji §8.8 closure sets gamma_xy0=0 and uses a finite Airy subspace. It is exactly the finite scalar closure requested by the conversation history and is the correct place to test whether the current Eq.(1)-(149) mechanics can be iterated without inventing dozens of extra algebraic variables.
