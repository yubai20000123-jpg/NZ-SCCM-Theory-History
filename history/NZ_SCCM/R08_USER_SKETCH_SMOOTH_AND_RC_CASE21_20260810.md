# R08 USER-SKETCH SMOOTHING CORRECTION AND RC CASE21

**Date:** 2026-08-10

## Trigger

User rejected the visual behavior of the R07R rational under-use curves: although they were globally smooth fits, the tensile side still contained an unnecessary local overshoot / dip / rebound sequence.

The user clarified the intended processing by sketch: when source / measured data contain a very sharp local peak or cut, it is acceptable to **not use the full sharp feature** and replace it by a much smoother curve, provided the final capacity is obtained from explicit formulas and explicit derivatives.

## Correction

R08 replaced the rational tensile regression by a shape-preserving quintic Hermite cap:

- one monotone rise from the origin;
- one rounded retained tensile peak at `0.09 fc`;
- one monotone decay to `0.03 fc` residual;
- zero tangent at the peak and at the residual onset;
- no secondary undershoot;
- no rebound.

Compression retained the already accepted Saenz / R06 postpeak data-processing target.

## Reinforcement

Case21 reinforcement was then coupled analytically into the SAME `P,Rq` equations using the source-consistent mapping

```text
rho_x = rho_y = 0.00375
Es = 200000 MPa
fy = 530 MPa
```

The RC limit was re-solved from

```text
R = Rc + Rs = 0
L = P_D R_q - P_q R_D = 0
P = Pc + Ps
```

and NOT by adding `As fy` after the concrete-only limit.

## Important execution correction

The first coarse global explicit `Pc/Rc` target produced an apparently converged RC root at `335.047660 kN`, but an independent audit showed an unacceptable residual mismatch. That value was explicitly rejected.

A local explicit target was then built around the mechanically located low-q branch, without using the experimental load to define the box. Degree sequence `12,14,16,18` was executed; degree 18 was retained.

## Final R08 result

```text
D_u = 0.7081086151600061
q_u = 0.016600100074508167
A_u = 20.252122090899963 mm
Pc  = 317.2665222395855 kN
Ps  = 18.32326091885251 kN
Pu  = 335.589783158438 kN
Pf_exp = 368.31275 kN
error = -8.884559886010457 %
```

Independent underlying-material audit at the same root:

```text
P_total_audit = 335.5853768252458 kN
R_total_audit = -1.0217933664688417 kN mm
```

All reinforcement remains elastic at this state.

## Interpretation

The corrected user-sketch curve is preferred over the R07R rational tensile shape.

The remaining ~8.9% underprediction is NOT a reason to restore the deleted sharp tensile feature. The next physical question is whether the minimal scalar current surface is missing a small, source-grounded multiaxial compression / tension-compression enhancement.

## Status

```text
USER_SKETCH_TENSION_SHAPE = PASS
R07R_RATIONAL_TENSILE_OSCILLATION = REJECTED_AS_UNNECESSARY
ANALYTIC_REINFORCEMENT_COUPLING = PASS
RC_CASE21_EXPLICIT_LIMIT = PASS_DIAGNOSTIC
FINAL_MULTIXIAL_NC = OPEN
FORMAL_ZERO_SPATIAL_QUADRATURE_PRODUCTION = HOLD
NEXT = R09_MINIMUM_SOURCE_GROUNDED_MULTIAXIAL_CORRECTION
```
