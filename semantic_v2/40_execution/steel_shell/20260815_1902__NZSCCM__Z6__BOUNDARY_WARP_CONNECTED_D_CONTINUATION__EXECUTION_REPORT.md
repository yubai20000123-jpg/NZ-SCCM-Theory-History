# NZ-SCCM Z6 boundary-warp connected-D continuation report

**Timestamp:** 2026-08-15 19:02 +08:00  
**Status:** CONNECTED PATH ADVANCED TO D=0.60; D>=0.625 NOT YET CERTIFIED; NO Pu RELEASE

## 1. Governing equations

At every fixed D, solve the same current-operator generalized equilibrium:

`Rq(D,q,c)=0`

`Rc(D,q,c)=0`

with N=1 boundary-admissible in-plane warp, one complete out-of-plane halfwave, Nguyen second-order kinematics, R10/N48-C1-MM/Cayley-Hamilton concrete current map, and degree24 local radial-cap outer-shell diagnostic.

No structural spatial sampling or numerical quadrature is used.

## 2. Continuation results

### D=0.50
Certified coupled checkpoint:
- q = 0.007244278905
- c = -0.0154563484942
- P = 37.345137133 MN
- Rq = +0.000722309 MN mm
- Rc = +0.000172877 MN mm

### D=0.55
Connected near-equilibrium:
- q = 0.0081982051032
- c = -0.0200407144410
- P = 38.410617205 MN
- Rq = -0.350377 MN mm
- Rc = -0.008332 MN mm

Against the underlying concrete/steel cancellation magnitudes (~3087 MN mm in Rq and ~38 MN mm in Rc), normalized residuals are about 1.1e-4 and 2.2e-4 respectively.

### D=0.60
Connected near-equilibrium:
- q = 0.0091774724300
- c = -0.0265508834600
- P = 39.126983390 MN
- Rq = +0.547691 MN mm
- Rc = +0.005610 MN mm

Against cancellation magnitudes (~3615 MN mm and ~44.47 MN mm), normalized residuals are about 1.5e-4 and 1.3e-4.

The connected load therefore rises monotonically over the certified/near-certified checkpoints:
`37.3451 -> 38.4106 -> 39.1270 MN`.

There is no evidence of a Pu peak by D=0.60.

### D=0.625
Best current attempt:
- q = 0.00964562658
- c = -0.03004767542
- P = 39.642739859 MN
- Rq = +5.060525 MN mm
- Rc = -0.559946 MN mm

Rq is already small relative to the ~3900 MN mm cancellation scale, but Rc remains ~1.2% of its ~47.5 MN mm cancellation scale. This point is retained as an intermediate only and is NOT accepted as equilibrium.

### D=0.65
Several predictor/corrector attempts were evaluated. A representative exploratory state:
- q = 0.00998451
- c = -0.02975383
- P = 40.374781978 MN
- Rq = +5.012527 MN mm
- Rc = +17.663445 MN mm

No simultaneous Rq=Rc root is released.

## 3. Execution gate encountered

As q and |c| increase beyond the D=0.60 state, the generalized N48/Cayley-Hamilton coefficient composition becomes sharply more expensive and locally ill-conditioned with respect to truncation/trim decisions. Small perturbations used for a 2x2 numerical Jacobian can require much larger coefficient tensors and runtime than the base state.

This is classified as:

`BOUNDARY_WARP_CONNECTED_PATH_REPRESENTATION_RUNTIME_GATE_AFTER_D060 = YES`

It is not evidence that the physical branch ends at D=0.60, and it is not a material-domain or energy-failure conclusion.

## 4. Causal implication so far

At D=0.50 the admissible boundary correction increased load only ~3.94% relative to the old free-Poisson equilibrium. Along the corrected path P continues upward through D=0.60, but no Pu has yet been reached. Therefore:

`BOUNDARY_KINEMATICS_IS_REAL = YES`

`BOUNDARY_KINEMATICS_ALONE_EXPLAINS_Z6_24P5_PERCENT_GAP = NOT ESTABLISHED`

`CORRECTED_Z6_Pu = NOT SOLVED`

## 5. Next mathematical task

Do not alter theory. Replace the current full generalized coefficient accumulation used for Jacobian perturbations by a genuinely directional moment-first contraction for only the three requested outputs P, Rq, Rc and their local 2x2 derivatives with respect to q,c. Then resume from the D=0.60 certified neighborhood.

Only after the Z6 branch reaches a first connected peak or a true mathematical domain gate should Z4 be run as the same-formulation control.
