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

## 3. C1 coefficient-generation method and verification

For each source primitive, the coefficient definition is the overdetermined Gauss-Chebyshev material-coordinate least-squares projection on the guard interval with exact R10 C1 equality constraints at `lambda=0`.

```text
U : value=0, derivative=kappa
C : value=0, derivative=0
T : value=0, derivative=0
T7: value=0, derivative=0
```

For the oversampled Gauss-Chebyshev roots, `V^T V` is diagonal. The committed reproducer therefore evaluates the unconstrained projection with DCT-II and applies the exact two-constraint correction through the 2x2 Schur system

`H^-1 G^T (G H^-1 G^T)^-1 (d-G a0)`.

This is algebraically the same constrained least-squares problem as the dense KKT form, but is fast enough for orders 1024–1280 and was independently rerun after the initial artifact write.

Material-coordinate nodes are coefficient-generation/audit coordinates only. They are not plate coordinates, material points, structural collocation points or numerical spatial integration points.

## 4. Primitive fidelity

Verified operational-core source errors are approximately:

```text
U  N=256   E0=8.60e-5   derivative-relative-to-source-peak=0.940%
C  N=1024  E0=1.57e-4   derivative-relative-to-source-peak=7.61%
T  N=1280  E0=6.01e-4   derivative-relative-to-source-peak=2.812%
T7 N=512   E0=4.37e-4   derivative-relative-to-source-peak=0.691%
```

Coefficient magnitudes remain O(1):

```text
U  max|a|=.5948283  sum|a|=1.70739
C  max|a|=.5812636  sum|a|=1.65631
T  max|a|=.3287288  sum|a|=2.02398
T7 max|a|=.1154567  sum|a|=1.70141
```

No large-coefficient pathology is introduced.

## 5. Current-master audit

The compiled U/C/T/T7 functions are inserted into the unchanged R10 spectral master; the master itself is not fitted.

Verified material-coordinate audit on the operational core gives:

```text
max spectral stress-scalar abs error = 0.000421529302935264
worst pair = (-0.9948333333,+0.0010833333)
source stress scalar   = -0.9939997881
compiled stress scalar = -0.9944213174

max first-spectral-derivative error = 0.8431213563
source peak tangent magnitude       = 29.8917328975
relative tangent error              = 2.8206%
```

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

This closes the process defect identified at 10:54 at the source-material level: the upcoming stocky-panel calculation will no longer evaluate the small-positive mixed tension/compression transition with the former 70–80% activation-function error.

## 7. C1 / coefficient verification

The rerun retains the exact source anchors to numerical roundoff. Representative residual levels are `10^-13` or smaller in value/first derivative, and every coefficient remains O(1).

The JSON companion records the verified coefficient heads/tails, diagnostic float64 hashes, source errors and operator audit values. The bit hashes are reproducibility diagnostics only, not theory gates.

## 8. Structural zero-integration status

This gate performs no structural-space quadrature.

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
```

Each new primitive is still a finite polynomial, so Cayley-Hamilton and General D15 remain formally applicable.

However, the existing Z0–Z6 structural kernel is coded around fixed N48 recurrence. It has not yet been rebuilt for the multirate orders above. Therefore no corrected Z0–Z5 Pu is calculated in this execution.

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

The next gate must implement the variable-order recurrence/moment path, avoid full spatial-point evaluation, verify coefficient conditioning and computational tractability, and only after those checks calculate new Z0–Z5 connected branches. The recalculated continuous principal spectrum must remain inside `[-1.40,+0.30]`; otherwise the material hull is rebuilt before any Pu is accepted.