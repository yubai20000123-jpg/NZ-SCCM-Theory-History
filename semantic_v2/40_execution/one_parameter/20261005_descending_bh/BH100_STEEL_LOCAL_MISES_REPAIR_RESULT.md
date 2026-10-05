# BH100 continuous local Mises-cap steel repair: recomputation result

Status: PROVISIONAL MECHANICS AUDIT RESULT. Not accepted as final theory.

## Frozen UHPC
The corrected plane-stress equivalent-uniaxial UHPC damage activation from the preceding BH100 trial is held fixed:
eta_t_eq = positive_part(eps1 + nu_c*eps2)/(1-nu_c^2)
eta_c_eq = positive_part(-eps2 - nu_c*eps1)/(1-nu_c^2)

No FEM/test data enters the solve.

## Steel repair
The previous whole-face scalar recoverable amplitude e is removed from force recovery.

For each continuous steel point:
1. calculate global elastic/current base stress g=(gx,gy,gt);
2. if global Mises exceeds fy, apply the current-state radial Mises cap to g;
3. calculate the Yun/R06 local elastic increment l=(lx,ly,lt);
4. set sigma = g + lambda*l;
5. if Phi(g+l)<=fy^2, lambda=1;
6. otherwise solve the explicit quadratic
   a*lambda^2 + 2*b*lambda + c - fy^2 = 0
   and take the admissible connected root in [0,1];
7. continuously integrate sigma_y over the whole face and thickness.

The old BH100 predictor field is reproduced before the new local cap: at w=82.15506222 mm the unreduced TOP max Mises is about 444-446 MPa and BOTTOM is about 355 MPa, consistent with the preceding whole-face evaluator.

## Key A/B point: w=82.15506222 mm
Frozen corrected UHPC:
PU = 7.21809 MN

New continuous local-cap steel:
TOP = 4.93411 MN
BOTTOM = 5.43196 MN
Total = 17.58416 MN

Mean steel axial stresses:
TOP = 246.705 MPa
BOTTOM = 271.598 MPa

Steel resultant eccentricity about the core mid-plane:
e_s = 1.105 mm

For comparison, the rejected single-e corrector had:
TOP = 2.96108 MN
BOTTOM = 5.43196 MN
which corresponded to about 6.77 mm steel-resultant eccentricity.

Thus the large TOP/BOTTOM split was indeed generated mainly by the whole-face corrector.

At w=82.155 mm the continuous yielded-area fractions in the numerical evaluator are approximately:
TOP = 19.7 percent
BOTTOM = 0 percent.

## Recomputed load-deflection path
Selected points:
w=20: P=5.58597 MN
w=40: P=8.64357 MN
w=60: P=12.45834 MN
w=70: P=14.68696 MN
w=80: P=17.06392 MN
w=82.1551: P=17.58416 MN
w=90: P=19.40300 MN
w=100: P=21.29628 MN
w=110: P=22.55932 MN
w=120: P=23.51774 MN
w=130: P=24.30742 MN
w=140: P=24.79478 MN
w=146.3179: P=24.89391 MN
w=150: P=24.76118 MN
w=160: P=23.54722 MN

## Refined first external maximum
The refined peak is approximately:
w_u = 146.32 mm
P_u = 24.895 MN

At the peak:
PU = 12.103 MN
P_TOP = 6.164 MN
P_BOTTOM = 6.627 MN
rho_A = about 0.7575
rho_D = about 0.6743
w_P = about 86.40 mm

Mean steel axial stresses:
TOP = about 308.2 MPa
BOTTOM = about 331.3 MPa

Steel resultant eccentricity:
e_s = about 0.83 mm

The numerical evaluator indicates approximate yielded-area fractions:
TOP about 78 percent
BOTTOM about 38 percent.

The peak occurs near the UHPC compressive-peak event: eta_c_eq,max is slightly above 0.0035. It is no longer artificially locked to BOTTOM first yield.

## Convergence / evaluator note
The theory is defined by continuous face/thickness integrals and algebraic yield level sets. The numerical evaluator used increasing deterministic quadrature orders only to evaluate the continuous integral. Around the refined peak the total load varied by only a few kN across the final order checks (about 24.895 MN).

## Interpretation
The steel corrector repair works mechanically in the narrow sense that:
- one local yield point no longer collapses an entire face;
- TOP/BOTTOM forces remain comparable;
- steel-resultant eccentricity stays around 1 mm instead of jumping to ~7 mm;
- the artificial peak near 82 mm disappears.

However, the repaired model now predicts a very high and late peak (~24.9 MN at ~146 mm). Therefore the prior 13-16 MN peak agreement was produced by compensating errors. The remaining model inconsistency is upstream/global: steel and UHPC global force/kinematic compatibility and load partition must be audited before any smaller BH specimen is recomputed.

Do not resume BH085-BH005.
