# NZ-SCCM — Z0–Z5 AR2 R10 multirate-C1 material compiler fidelity lock

**Timestamp:** 2026-08-16 11:10 +08:00  
**Status:** CURRENT MATERIAL-COMPILER GOVERNANCE LOCK

## Frozen physics and structural boundary

```text
R10 physical current operator = FROZEN / UNCHANGED
PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
Cayley-Hamilton = ACTIVE
General D15 exact moments = ACTIVE
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Zhou/Winter calibration=NO
```

The 10:43 Z0–Z5 capacities remain `RETRACTED_PENDING_RECALCULATION`. Z6 `Pu=51.30 MN` remains user-accepted and is not reopened by this gate.

## Why the old compiler is not reusable

The rejected Z6-wide N48 compiler on `[-2.35,+1.90]` has, inside the Z0–Z5 occupied material range, approximately

```text
U  E0 ~ .02625
C  E0 ~ .08247
T  E0 ~ .70402
T7 E0 ~ .79606
```

and current-operator source audit over the stocky operational range gives approximately

```text
spectral stress-scalar max abs error ~ .71852
spectral tangent max error / source peak tangent ~ 81.5%
```

It is prohibited for Z0–Z5 production.

## Rebuild strategy

Do not add a new material mechanism and do not partition the structural domain. Instead use one global material-coordinate guard interval

`lambda in [-1.50,+0.35]`

and retain exact R10 C1 anchors at `lambda=0`, while allocating polynomial order according to the actual source primitive difficulty:

```text
U  : degree 256, C1
C  : degree 1024, C1
T  : degree 1280, C1
T7 : degree 512, C1
```

Identity:

`R10-MR-C1(256,1024,1280,512)`

"MR" means **material-primitive multirate polynomial order**, not spatial multiscale subdivision.

Each primitive remains a single finite Chebyshev polynomial on the same global material interval. There is no piecewise material-zone integration, no spatial cell, no material-point state machine and no second structural subdomain.

## Source-only operational core

Because very-high-order polynomial derivatives are least reliable at the unused guard endpoints, production structural use is permitted only if the recalculated continuous principal spectrum remains inside

`lambda in [-1.40,+0.30]`.

This operational core was formed from the previous equation-derived reachable spectrum with conservative margins; no experiment, Zhou capacity, Winter capacity or desired Pu enters it.

After the blind structural solve, spectrum self-consistency is mandatory. If any recalculated state exits the core, stop and rebuild the guard/core before accepting Pu.

## Fidelity gate

On the operational core, the selected source-only compiler achieves approximately

```text
primitive value max errors:
U  = 8.60e-5
C  = 1.57e-4
T  = 6.01e-4
T7 = 4.37e-4
```

The exact two-principal-value R10 current master is then reconstructed from those primitives without refitting. A source-only material-coordinate audit gives

```text
max spectral stress-scalar abs error = 4.22e-4
max spectral tangent abs error       = 8.43e-1
source peak tangent magnitude        = 2.989e1
relative tangent error               = 2.82%
```

Compared with the old wide N48 compiler, stress-scalar error is reduced by about 1.7e3 times and tangent-relative error by about 29 times.

All coefficient maxima remain O(1), below 0.60, and the R10 value/first-derivative anchors at zero are retained to numerical roundoff.

Therefore:

```text
R10_SOURCE_VALUE_FIDELITY_GATE = PASS
R10_SOURCE_TANGENT_FIDELITY_GATE = PASS_ON_OPERATIONAL_CORE
O1_COEFFICIENT_GATE = PASS
C1_ANCHOR_GATE = PASS
CAYLEY_HAMILTON_FORMAL_COMPATIBILITY = PASS
GENERAL_D15_FORMAL_COMPATIBILITY = PASS
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
```

## Important limit

This gate validates the **material representation**, not yet a new Z0–Z5 capacity. The existing structural compiler is hardwired around N48-style recurrence and has not yet been rebuilt for variable primitive orders up to 1280.

Therefore:

```text
NEW_Z0_Z5_Pu = NOT_CALCULATED
OLD_1043_Z0_Z5_Pu = STILL_RETRACTED
```

## Unique next execution

`Z0_Z5_AR2_MULTIRATE_R10_TO_VARIABLE_ORDER_MOMENT_FIRST_D15_RECOMPILE_GATE`

That gate must ingest the above compiler into the zero-spatial moment-first backend without expanding a spatial point grid, verify numerical conditioning and spectrum self-consistency, and only then release new connected-branch Pu values.