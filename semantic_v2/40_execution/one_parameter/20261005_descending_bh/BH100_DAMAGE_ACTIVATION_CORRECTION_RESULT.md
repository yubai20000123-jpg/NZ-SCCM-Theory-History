# BH100 corrected multiaxial UHPC damage-activation trial

Status: PROVISIONAL CORRECTED TRIAL

Only one mechanism was changed from the BH100 13.40-MN path: the multiaxial strain driver that feeds the existing ABS/raw UC141 damage and plastic functions.

Old driver:
eta_t_old = positive_part(eps1)
eta_c_old = positive_part(-eps2)

Corrected plane-stress equivalent-uniaxial driver:
eta_t_eq = positive_part(eps1 + nu_c*eps2) / (1 - nu_c^2)
eta_c_eq = positive_part(-eps2 - nu_c*eps1) / (1 - nu_c^2)

This makes pure uniaxial compression give eta_t_eq = 0, so Poisson lateral expansion cannot create tensile damage. Under uniaxial tension/compression the original UC141 uniaxial total-strain calibration is recovered.

## Peak
w_u = 82.15506222 mm
P_u = 15.61115 MN

Components:
P_UHPC = 7.21811 MN
P_TOP = 2.96108 MN
P_BOTTOM = 5.43196 MN

UHPC:
rho_A = 0.8533161
rho_D = 0.7715349
w_P = 31.59680 mm
eta_t_eq_max = 0.00123863
eta_c_eq_max = 0.00157270

TOP steel:
A_plus = 4.4312342 mm
e_plus = 1.8956005 mm
A_P_plus = 2.5356337 mm
mean axial stress = 148.05383 MPa
max Mises = 355.0000 MPa
unreduced trial Mises = about 446.08 MPa

BOTTOM steel:
A_minus = 4.6598346 mm
e_minus = A_minus
mean axial stress = 271.59798 MPa
max Mises = 355.0000 MPa

## A/B at the same w
Old principal-total-strain driver:
rho_A = 0.7540082
rho_D = 0.6822918
w_P = 45.35476 mm
P_UHPC = 5.00809 MN

Corrected driver:
rho_A = 0.8533161
rho_D = 0.7715349
w_P = 31.59680 mm
P_UHPC = 7.21811 MN

Changes:
- membrane retention: +9.93 percentage points
- bending retention: +8.92 percentage points
- projected plastic reference imperfection w_P: -30.33 percent
- UHPC axial contribution: +44.13 percent

## Peak neighborhood
P(82.1051) = 15.60666 MN
P(82.1451) = 15.61025 MN
P(82.1551) = 15.61115 MN
P(82.1651) = 15.61084 MN
P(82.2051) = 15.60960 MN

## Continuous-integral evaluator convergence
The theoretical definition remains continuous area integrals for rho_A, rho_D and w_P. These orders are only numerical evaluations of that same continuous integral:
order 80: 15.611354 MN
order 100: 15.611207 MN
order 120: 15.611129 MN
order 160: 15.611147 MN
order 200: 15.611181 MN

The final production backend still needs the already-derived level-set plus one-dimensional deterministic integral implementation.

## Post-freeze comparison
Previously extracted BH100 DIRECT peak = 13.486 MN.
After freezing the corrected theoretical result, the difference is +15.76 percent.
No FEM/test value was used in any root or material-state calculation.

Interpretation: the Poisson false-cracking mechanism was real. Removing it restores a large part of UHPC stiffness and reduces w_P, but it also shows that the former 13.40-MN agreement contained compensating errors. The next audit must focus on load partition and the steel global-local branch.
