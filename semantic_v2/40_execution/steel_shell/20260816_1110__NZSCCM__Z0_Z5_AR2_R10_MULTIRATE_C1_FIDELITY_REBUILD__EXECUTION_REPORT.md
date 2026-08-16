# NZ-SCCM — Z0–Z5 AR2 R10 multirate-C1 fidelity rebuild execution report

**Timestamp:** 2026-08-16 11:10 +08:00  
**Executed gate:** `Z0_Z5_AR2_CURRENT_OPERATOR_FIDELITY_REBUILD_ZERO_SPATIAL_INTEGRATION`

## 1. Result

The gate passes at the material-operator level.

The rejected single wide N48 compiler is replaced, for the upcoming Z0–Z5 recalculation, by a single-hull multirate polynomial compiler:

```text
R10-MR-C1(256,1024,1280,512)
U degree   256
C degree  1024
T degree  1280
T7 degree  512
```

The physical R10 law is unchanged. This is not a new concrete model.

## 2. Material intervals

Coefficient-generation guard hull:

`[-1.50,+0.35]`

Production tangent-fidelity core:

`[-1.40,+0.30]`

The previous challenged Z0–Z5 structural spectra are used only to construct a conservative equation-derived starting envelope; no experimental load, Zhou load, Winter load or desired Pu enters coefficient generation.

The upcoming blind structural recalculation must verify that its continuous reachable spectrum remains in the operational core. Otherwise the calculation stops and the compiler interval is regenerated.

## 3. C1 coefficient-generation method

For each source primitive, use an overdetermined Chebyshev material-coordinate least-squares problem on the guard interval with exact equality constraints at `lambda=0` enforced by a KKT system.

```text
U : value=0, derivative=kappa
C : value=0, derivative=0
T : value=0, derivative=0
T7: value=0, derivative=0
```

Material-coordinate nodes are coefficient-generation/audit coordinates only. They are not plate coordinates, material points, structural collocation points or numerical spatial integration points.

## 4. Primitive fidelity

Operational-core source errors:

```text
U  N=256   E0=8.6015e-5   derivative-relative-to-source-peak=0.9403%
C  N=1024  E0=1.5651e-4   derivative-relative-to-source-peak=7.6098%
T  N=1280  E0=6.0062e-4   derivative-relative-to-source-peak=2.8118%
T7 N=512   E0=4.3650e-4   derivative-relative-to-source-peak=0.6909%
```

Coefficient magnitudes:

```text
U  max|a|=.5948283  sum|a|=1.70739
C  max|a|=.5812636  sum|a|=1.65631
T  max|a|=.3287288  sum|a|=2.02398
T7 max|a|=.1154567  sum|a|=1.70141
```

No large coefficient pathology is introduced.

## 5. Current-master audit

The compiled U/C/T/T7 functions are inserted into the unchanged R10 spectral master; the master itself is not fitted.

On the material-coordinate operational core, the maximum audited spectral stress-scalar error is

`4.215293029e-4`.

Worst audited pair:

```text
lambda_1=-.9948333333
lambda_2=+.0010833333
source stress scalar   = -.9939997881
compiled stress scalar = -.9944213174
```

The maximum first-spectral-derivative discrepancy is

`0.8431213563`,

versus a source peak tangent magnitude

`29.8917328975`,

so

`max tangent error / source peak tangent = 2.8206%`.

## 6. Old-vs-new comparison on the same operational core

Rejected wide N48:

```text
max spectral stress error = .7185201
max tangent relative error = 81.5263%
```

New R10-MR-C1:

```text
max spectral stress error = .00042153
max tangent relative error = 2.8206%
```

Improvement factors:

```text
stress-scalar error reduction ~= 1705x
tangent-relative error reduction ~= 28.9x
```

This directly closes the process defect identified at 10:54: the upcoming stocky-panel calculation will no longer evaluate mixed tension/compression states with a 70–80% primitive activation error.

## 7. Exact C1 audit

```text
U(0)    = +2.22e-16
U'(0)   = 2.000512953367875
C(0)    = +1.11e-16
C'(0)   = -4.80e-16
T(0)    = -1.11e-16
T'(0)   = -2.69e-14
T7(0)   = +5.55e-17
T7'(0)  = +2.88e-15
```

## 8. Structural zero-integration status

This gate performs no structural-space quadrature.

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
```

Each new primitive is still a finite polynomial, so Cayley-Hamilton and General D15 remain formally applicable.

However the existing Z0–Z6 execution kernel is coded around fixed N48 recurrence. It has not yet been rewritten for the multirate orders above. Therefore no corrected Z0–Z5 Pu is calculated in this execution.

## 9. Gate decision

```text
R10_MATERIAL_PHYSICS_CHANGED = NO
OLD_WIDE_N48_FOR_Z0_Z5 = REJECTED
R10_MR_C1_SOURCE_FIDELITY = PASS
C1_ANCHORS = PASS
O1_COEFFICIENTS = PASS
CH_D15_FORMAL_COMPATIBILITY = PASS
ZERO_SPATIAL_INTEGRATION = PASS
OLD_1043_Z0_Z5_Pu = RETRACTED
NEW_Z0_Z5_Pu = NOT_CALCULATED
Z6_51_30_MN = RETAINED_USER_ACCEPTED
```

## 10. Unique next execution

`Z0_Z5_AR2_MULTIRATE_R10_TO_VARIABLE_ORDER_MOMENT_FIRST_D15_RECOMPILE_GATE`

The next gate must implement the variable-order recurrence/moment path, avoid full spatial-point evaluation, verify coefficient conditioning and continuous spectrum containment, and only after those checks calculate new Z0–Z5 connected branches.