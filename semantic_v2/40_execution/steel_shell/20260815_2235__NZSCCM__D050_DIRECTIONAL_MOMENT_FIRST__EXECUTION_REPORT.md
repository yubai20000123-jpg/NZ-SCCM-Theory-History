# NZ-SCCM — D=.50 directional moment-first augmented membrane execution

**Timestamp:** 2026-08-15 22:35 +08:00  
**Identity:** fixed-D certificate execution; no Pu; no D continuation.

## 1. Objective

The 22:20 gate identified dense high-order bounding-box fill-in as the representation bottleneck. This run executes the authorized next step:

```text
DIRECTIONAL_MOMENT_FIRST_AUGMENTED_MEMBRANE_EVALUATOR_AT_D050
```

The q,c,p20,p02 physical system and current operator are unchanged.

## 2. Parent state reproduction at inherited tolerance

At

```text
D=.50
q=.007244278905
c=-.0154563484942
p20=p02=0
concrete pruning tol=7e-7
```

the directional evaluator gives

```text
P   =37.3451401318 MN
Pc  =21.0700464911 MN
Ps  =16.2750936407 MN
Rq  =+0.0013815858 MN mm
Rc  =+0.0000996113 MN mm
R20 =-19.4868584406 MN mm
R02 =-23.4734835682 MN mm
```

This reproduces the 21:44/21:53 parent state and its large missing FvK membrane projections.

Measured current-runtime concrete material-pair build time was about `8.31 s`.

## 3. Augmented fixed coordinate convergence sweep

A near-root coordinate set obtained from the prior 2e-4 solve was held fixed:

```text
q=0.008004910720924569
c=-0.07773103572950019
p20=-0.06077731545895354
p02=0.16537305620798107
```

The concrete pruning tolerance was tightened without changing the equations:

```text
2e-4 -> 1e-4 -> 5e-5 -> 2e-5 -> 1e-5 -> 5e-6 -> 2e-6 -> 7e-7
```

The axial resultant stabilized around `37.687 MN`. The parent implementation tolerance `7e-7` completed in about `37.9 s` rather than exceeding the prior 90 s execution window.

At the fixed coordinates and `7e-7`:

```text
P=37.6870272882 MN
Rq=+1.5029406102 MN mm
Rc=-0.0532865265 MN mm
R20=+0.0039669308 MN mm
R02=-0.0023234518 MN mm
```

The nonzero Rq/Rc show that the old 2e-4 coordinates must be corrected when the inherited tolerance is restored; this is a coordinate/root shift, not a failure of the physical model.

## 4. Parent-tolerance coordinate correction

Using the previously stored full-current residual Jacobian as a preconditioner, the correction from the fixed 7e-7 state was

```text
dq   = -1.84729867185e-6
dc   = +7.06944309824e-5
dp20 = +1.19077532320e-4
dp02 = -1.16275074841e-4
```

This produced the certificate candidate

```text
D=.50
q=0.008003063422252722
c=-0.07766034129851779
p20=-0.06065823792663306
p02=0.16525678113314005
```

At **the inherited 7e-7 concrete pruning tolerance**:

```text
P  =37.6899290259 MN
Pc =21.8783795851 MN
Ps =15.8115494408 MN
```

Residuals, MN mm:

```text
Rq =-0.3465589605
Rc =-0.0055395219
R20=+0.0076892296
R02=+0.0024794016
```

Internal decomposition:

```text
Rqc  =-2978.7938462449
Rqs  =+2978.4472872844
Rcc  =-13.3051556635
Rcs  =+13.2996161416
R20c =-3.9856498360
R20s =+3.9933390656
R02c =-12.5672975175
R02s =+12.5697769191
```

Residual/internal-cancellation ratios:

```text
Rq  0.00581744 %
Rc  0.02082154 %
R20 0.09636847 %
R02 0.00986352 %
```

All four are below the locked engineering gate `0.1%` at the inherited current-map tolerance.

Therefore:

```text
D050_PARENT_TOLERANCE_DIRECTIONAL_EQUILIBRIUM_CERTIFICATE = PASS
THEOREM_LEVEL_EXACT_ZERO_RESIDUAL = NOT CLAIMED
```

The certificate-state evaluation took about `36.7 s` in the current execution runtime. The previous augmented full-stress implementation had exceeded the 90 s execution window when approaching the same tolerance, so the observed runtime reduction is at least about 59% relative to that lower-bound timeout.

## 5. What the optimization actually changed

It does **not** remove the dense N48 material pair. `buildS(K1,K2)` is still evaluated.

It removes the unnecessary final sequence

```text
build Sxx,Syy full fields
-> multiply each by q/c/p20/p02 virtual-strain fields
-> build a new full 3D coefficient tensor for each residual
-> integrate
```

and replaces it with

```text
retain S=A I+B Y
-> directly contract A and B with each low-order virtual-strain weight
-> exact Chebyshev product moments
```

Thus the gain is an evaluation-order gain, not a physical or integration approximation.

## 6. Why P still looks close to the old number

This question must distinguish three quantities.

### A. Same-D valid comparison

Old boundary-admissible D+q+c state at D=.50:

```text
P_parent =37.3451401318 MN
```

Current augmented certificate at the same D=.50:

```text
P_aug =37.6899290259 MN
```

Difference:

```text
+0.3447888941 MN = +0.92325%
```

The change is real but modest in the *global axial resultant*.

Internally it is not modest:

```text
Pc: 21.07004649 -> 21.87837959 MN   (+0.80833 MN)
Ps: 16.27509364 -> 15.81154944 MN   (-0.46354 MN)
```

The concrete gain and steel loss partially cancel, leaving only +0.345 MN in total P. This is precisely what a membrane **redistribution** mode can do: greatly alter spatial/phase load sharing while changing the global resultant much less.

### B. Historical old Pu is not the same quantity

The old reduced-branch `Pu≈37.50943 MN` was a peak on a different D-q path at a different D/state. The present `37.68993 MN` is only a fixed `D=.50` equilibrium checkpoint. Their numerical closeness is not a valid measure of whether the FvK correction has an effect.

Indeed, the current D=.50 augmented checkpoint already lies above that historical old peak, while its q,c,p20,p02 state is completely different. Therefore the old peak has been invalidated as the peak of the corrected path; a new Pu can only be obtained after connected D continuation.

### C. Why self-equilibrated modes need not strongly change P at one D

The p20/p02 warps vanish on the loaded edges and do not change the imposed mean end shortening. Their principal role is to satisfy previously missing in-plane virtual-work directions. Hence much of their first effect is redistribution of membrane force rather than a large change of the mean axial resultant.

The expected impact on Pu is therefore primarily through the **entire updated path** `q(D),c(D),p20(D),p02(D)` and its tangent/peak location, not through a dramatic jump of P at one arbitrarily fixed D.

## 7. Current status and next gate

```text
D=.50 parent-tolerance directional certificate = PASS
formal spatial quadrature = 0
General D15 = unchanged
Pu = NOT SOLVED
```

The next controlled execution is:

```text
D055_AUGMENTED_DIRECTIONAL_MOMENT_FIRST_CONNECTED_CHECKPOINT
```

using the D=.50 certificate state as the connected initial state.