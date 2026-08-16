# NZ-SCCM — audit: Z0–Z5 AR2 R10 multirate-C1 source fidelity

**Timestamp:** 2026-08-16 11:10 +08:00

## Audit question

Can the original R10 current operator be represented faithfully enough for the stocky AR2 Z0–Z5 problem without changing material physics, introducing spatial cells, or using Zhou/Winter calibration?

## Audited candidate

```text
identity = R10-MR-C1(256,1024,1280,512)
guard interval = [-1.50,+0.35]
operational core = [-1.40,+0.30]
U degree=256
C degree=1024
T degree=1280
T7 degree=512
```

All primitives remain one global Chebyshev polynomial each and retain the exact R10 C1 anchor at `lambda=0`.

## Source primitive audit

Operational-core maximum value errors:

```text
U  8.60e-5
C  1.57e-4
T  6.01e-4
T7 4.37e-4
```

Coefficient magnitudes remain O(1):

```text
max max|a_n| = .59483
```

## Source current-master audit

No two-dimensional stress surface is fitted. The candidate primitives are inserted into the unchanged R10 master.

Material-coordinate audit on `lambda1,lambda2 in [-1.40,+.30]` gives

```text
max spectral stress-scalar absolute error = 4.215e-4
max spectral tangent absolute error       = 8.431e-1
source peak spectral tangent magnitude    = 2.989e1
relative tangent error                    = 2.821%
```

The rejected Z6-wide N48 compiler on the same operational core gives approximately

```text
max spectral stress-scalar absolute error = .71852
relative tangent error                    = 81.53%
```

Thus the identified 10:54 process defect is removed at the source-material level.

## Spatial-integral audit

```text
structural spatial sampling = 0
structural spatial quadrature = 0
formal spatial subdomains = 1
material-coordinate coefficient nodes = NOT structural points
material-coordinate audit nodes = NOT structural points
```

No Gauss/Simpson/adaptive/collocation/material-point grid is used on the plate domain.

## Formal algebra audit

Because every primitive remains a finite polynomial:

```text
CAYLEY_HAMILTON_FORMAL_COMPATIBILITY = PASS
GENERAL_D15_FORMAL_COMPATIBILITY = PASS
```

The existing fixed-order structural implementation has not yet been converted to the new variable orders. Therefore formal compatibility is not the same as an executed structural backend pass.

## Spectrum self-consistency condition

The material tangent gate is certified on the operational core only. The next blind structural solve must provide a continuous principal-spectrum enclosure. If any reachable state leaves `[-1.40,+.30]`, the compiler is not accepted for that state and must be rebuilt before Pu is reported.

## Final audit verdict

```text
R10_MATERIAL_TARGET_CHANGED = NO
OLD_WIDE_N48_Z0_Z5_COMPILER = FAIL / RETIRED
R10_MR_C1_PRIMITIVE_VALUE_GATE = PASS
R10_MR_C1_CURRENT_MASTER_VALUE_GATE = PASS
R10_MR_C1_CURRENT_MASTER_TANGENT_GATE = PASS_ON_CORE
C1_ANCHOR_GATE = PASS
O1_COEFFICIENT_GATE = PASS
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
NEW_Z0_Z5_Pu = NOT_YET_CALCULATED
```

Unique next gate:

`Z0_Z5_AR2_MULTIRATE_R10_TO_VARIABLE_ORDER_MOMENT_FIRST_D15_RECOMPILE_GATE`.