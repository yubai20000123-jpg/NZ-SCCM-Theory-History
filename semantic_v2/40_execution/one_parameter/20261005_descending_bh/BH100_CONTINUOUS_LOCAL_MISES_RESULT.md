# BH100 continuous local-Mises steel recalculation result

Status: PROVISIONAL / MECHANISM AUDIT, not accepted as final UCFT theory.

## Frozen UHPC
The corrected UHPC multiaxial driver is unchanged:
eta_t_eq = positive_part(eps1 + nu_c*eps2)/(1-nu_c^2)
eta_c_eq = positive_part(-eps2 - nu_c*eps1)/(1-nu_c^2)

ABS/raw UC141 damage and ABS/raw plastic functions are unchanged.

## Steel repair executed
The rejected whole-face single-e corrector is removed.

At every continuous steel point:
1. calculate the global elastic steel stress;
2. if global Mises exceeds fy, apply the current-state radial Mises cap to the global stress;
3. calculate the Yun/R06 local elastic stress increment;
4. solve the explicit quadratic Phi(g + lambda*l)=fy^2 for the admissible lambda in [0,1];
5. recover sigma_y = g_y + lambda*l_y;
6. integrate sigma_y continuously over the steel face and thickness.

For this A/B run the same predictor amplitude A_plus/A_minus used by the previous BH100 path is retained. The local normal-stress fluctuations are the seven-harmonic R06 field. The axial local increment is assembled so that, before plastic limiting, global spatial variation is retained and the whole-face axial mean equals the old Yun predictor mean.

## Repaired state at w = 82.15506222 mm
UHPC:
P_U = 7.21811 MN
rho_A = 0.853316
rho_D = 0.771535
w_P = 31.5968 mm

TOP:
A_plus = 4.431234 mm
old Yun predictor mean = 251.08788 MPa
global elastic mean = 223.79310 MPa
repaired continuous local-cap mean = 246.75 MPa
P_top = about 4.935 MN
local-limited fraction = about 19.5 percent
global-only capped fraction = about 7.0 percent

BOTTOM:
A_minus = 4.659835 mm
old Yun predictor mean = 271.59798 MPa
global elastic mean = 299.07675 MPa
repaired mean = 271.59798 MPa
P_bottom = 5.43196 MN
local-limited fraction = 0
global-only capped fraction = 0

Thus the repaired top/bottom difference is about 24.9 MPa, rather than the rejected 123.5 MPa split.

Total at this same state:
P_total(82.1551) is about 17.585 MN.

## Repaired load-deflection branch
Representative points:
w=20 mm: P=5.586 MN
w=40 mm: P=8.644 MN
w=60 mm: P=12.458 MN
w=70 mm: P=14.687 MN
w=80 mm: P=17.064 MN
w=90 mm: P=19.405 MN
w=100 mm: P=21.296 MN
w=110 mm: P=22.558 MN
w=120 mm: P=23.517 MN
w=130 mm: P=24.306 MN
w=140 mm: P=24.794 MN
w=145 mm: P=24.884 MN
w=150 mm: P=24.762 MN
w=160 mm: P=23.550 MN
w=180 mm: P=19.126 MN

## First external maximum on this repaired branch
Refined peak:
w_u = about 146.33 mm
P_u = about 24.897 MN

Peak components:
P_UHPC = about 12.1032 MN
P_TOP = about 6.165 MN
P_BOTTOM = about 6.628 MN

Peak steel face means:
TOP about 308.25 MPa
BOTTOM about 331.42 MPa

Steel resultant eccentricity at the peak:
about 0.83 mm from the steel-face midplane.

UHPC peak state:
rho_A about 0.7575
rho_D about 0.6743
w_P about 86.42 mm

Steel predictor amplitudes:
A_plus about 7.524 mm
A_minus about 7.731 mm

At the peak the global elastic trial Mises field is above yield over essentially the full area of both faces, so the global current-state cap is active almost everywhere. The local-cap active fraction is about 78 percent on TOP and 38 percent on BOTTOM.

## Peak numerical evaluation convergence
The theory is defined by continuous integrals and algebraic yield-level sets. Independent numerical evaluations of that same continuous integral at w about 146.328 mm gave:
- UHPC order 100 / steel order 64: P = 24.89441 MN
- 120 / 80: P = 24.89503 MN
- 160 / 96: P = 24.89417 MN
- 200 / 128: P = 24.89629 MN
- 220 / 144: P = 24.89659 MN

This numerical evaluator is not part of the constitutive definition. The formal production identity remains a continuous integral over algebraically defined elastic/yielded regions.

## Post-freeze DIRECT comparison
Previously extracted BH100 DIRECT peak:
P_DIRECT = 13.486 MN at incremental overall deflection about 97.392 mm.

The repaired branch therefore overpredicts peak load by about 84.6 percent and places the maximum much too late.

At the DIRECT peak deflection w=97.392 mm, the repaired theoretical branch already gives about 20.875 MN:
P_UHPC about 8.603 MN
P_TOP about 5.650 MN
P_BOTTOM about 6.622 MN.

## Mechanism conclusion
The local continuous Mises-cap repair successfully removes the unphysical whole-face TOP stress collapse. Therefore the previous 148 MPa versus 272 MPa split was indeed caused mainly by the single-e corrector.

However, once that artificial suppression is removed, the total steel force becomes far too large. This exposes a second, upstream steel problem: the predictor/mean-stress level is still treating the Yun whole-face mean as a total face mean while the global base already carries the overall axial demand. The remaining error is therefore a global/local mean-level double-counting or compatibility issue, not a reason to restore the rejected whole-face corrector.

BH085 and smaller specimens remain paused.
