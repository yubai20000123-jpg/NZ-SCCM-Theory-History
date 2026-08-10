# R10 GOVERNANCE DECISION — 1D ENERGY SMOOTHING

**Date:** 2026-08-10 23:52 +08:00

## Decision

R10 validates the corrected material route:

```text
multidimensional/current NC operator
→ internal 1D Foster tensile scalar
→ 1D material-energy smoothing only
→ SAME multidimensional current operator
→ Case21 same-equation audit
```

The user's intended route is therefore retained.

```text
R10_1D_ENERGY_SMOOTHING = PASS
MULTIAXIAL_REINSERTION = PASS
CASE21_SAME_EXECUTION_AUDIT = PASS
STRUCTURAL_CALIBRATION_TO_Pf = NO
SWARTZ24 = NOT_STARTED
```

## Frozen R10 scalar

The source scalar is

\[
u_{t,src}(t)=\rho T_{Foster}(t),\qquad 0\le t\le10x_{cr}.
\]

Its retained material work is

\[
W_{src}=0.031741235181249904.
\]

R10 adopts a two-piece C2 quintic scalar patch preserving:

- origin stress = 0;
- origin tangent = \(\kappa\);
- zero curvature at the origin;
- one rounded peak at \(t=x_{cr}\);
- zero first and second derivative at the rounded peak;
- residual \(0.03f_c\) at \(10x_{cr}\);
- zero first and second derivative at the residual onset;
- total scalar work exactly equal to the source work.

The energy equation fixes the peak uniquely:

\[
\boxed{h=0.09799750427197301}.
\]

No Case21 or Swartz capacity is used to select \(h\).

## Same-execution Case21 audit

With the same structural evaluator and reinforcement model:

```text
SOURCE_FOSTER Pu        = 342.334029463 kN
ENERGY_SMOOTHED_1D Pu   = 368.723464127 kN
Delta Pu                = +26.389434664 kN
Case21 experiment       = 368.312750000 kN
Energy-smoothed error   = +0.111512329 %
```

This close agreement is an observed consequence after the material scalar was frozen and is not a calibration basis.

## Formal-production boundary

The R10 Case21 reinsertion calculation uses 48×48×28 full-halfwave Gauss only as a **same-equation audit**. It is not the formal production operator.

Therefore:

```text
FORMAL_ZERO_SPATIAL_QUADRATURE_PRODUCTION = HOLD
```

The next step is strictly a compiler/reintegration task. Material retuning is prohibited until R10B is completed.

## R10B mandatory task

```text
CURRENT_RECOMMENDED_NEXT_TASK
= R10B_RECOMPILE_FROZEN_ENERGY_SMOOTH_SCALAR_IN_EXISTING_ZERO_SPATIAL_D15_BACKEND
```

R10B must:

1. keep the R10 scalar formula and all values frozen;
2. replace the old Foster scalar in the existing nested-D15 material compiler with the R10 C2 scalar;
3. retain the same multidimensional U/C/T, CC/TC/TT and spectral architecture;
4. retain one continuous complete halfwave and Nguyen second-order kinematics;
5. use zero formal spatial sampling/quadrature;
6. obtain explicit finite representations of \(P(D,q)\) and \(R_q(D,q)\);
7. obtain \(P_D,P_q,R_{q,D},R_{q,q}\) from the same representation;
8. solve \(R_q=0\) and \(L=P_D R_{q,q}-P_qR_{q,D}=0\);
9. include reinforcement before root solving;
10. compare the formal result with the R10 audit value only after the zero-spatial result exists;
11. stop before Swartz24.

## Prohibited after R10

- changing \(h\) because of the 0.1115% Case21 agreement;
- changing the smoothing interval or endpoint conditions to improve Case21;
- adding free scalar coefficients;
- refitting the multidimensional interaction;
- using structural Gauss integration as production;
- fitting a whole-structure P/R/U surface from numerical spatial integration;
- starting Swartz24 before R10B zero-spatial closure.
