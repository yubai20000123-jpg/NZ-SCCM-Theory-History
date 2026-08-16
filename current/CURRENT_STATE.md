# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 11:31 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_1131__NZSCCM__PROJECT__CURRENT_STATE_FIXED_N48_ORDER_RESTORED__SEMANTIC_INDEX.md`

## Frozen production scope

```text
PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
R10 physical current operator = FROZEN / UNCHANGED
Cayley-Hamilton = ACTIVE
General D15 exact moments = ACTIVE
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid=PROHIBITED
Zhou/Winter calibration=PROHIBITED
```

## Material compiler order — restored by user instruction

The 11:10 multirate proposal is no longer current:

```text
U=256
C=1024
T=1280
T7=512
```

is classified as

```text
RETRACTED_FROM_CURRENT_PRODUCTION / HISTORICAL_DIAGNOSTIC_ONLY
```

The formal material compiler order is restored and locked to

```text
MATERIAL_COMPILER_ORDER = 48
U_ORDER  = 48
C_ORDER  = 48
T_ORDER  = 48
T7_ORDER = 48
```

Current order-level compiler family:

```text
U  = N48-C1
C  = N48-C1
T7 = N48-C1
T  = N48-C1-CONSTRAINED-MINIMAX
```

No order change is permitted without explicit user authorization.

## Important retained fidelity finding

Restoring degree 48 does **not** restore the old Z6-wide coefficient set for Z0–Z5.

The 10:54 audit remains valid:

```text
wide compiler interval = [-2.35,+1.90]
T max error   ~= .704
T7 max error  ~= .796
```

inside the actually occupied Z0–Z5 small-positive tension region.

Therefore:

```text
FIXED_N48_ORDER = ACTIVE
REUSE_Z6_WIDE_N48_COMPILER_FOR_Z0_Z5 = PROHIBITED
```

The next repair must remain degree 48 and address source fidelity only through coefficient-generation / analytic-representation strategy, while leaving R10 material physics unchanged.

## Capacity-result status

```text
Z6_AR2_Pu = 51.30 MN  # user accepted and retained
Z0_Z5_20260816_1043_Pu = RETRACTED_PENDING_RECALCULATION
Z0_Z5_20260816_1043_ZHOU_WINTER_TABLE = RETRACTED_PENDING_RECALCULATION
NEW_Z0_Z5_Pu = NOT_CALCULATED
```

The withdrawn interpretation that membrane redistribution itself caused the former 20–36% Z0–Z4 loss remains withdrawn.

## Current unique next gate

`Z0_Z5_AR2_FIXED_N48_CURRENT_OPERATOR_FIDELITY_REBUILD_ZERO_SPATIAL_INTEGRATION`

Requirements:
1. keep U/C/T/T7 at degree 48;
2. keep R10 physical law unchanged;
3. use no experiment, Zhou/Winter load, desired Pu or structural error to choose coefficients;
4. retain exact C1 anchors and Cayley-Hamilton / General-D15 compatibility;
5. retain zero structural spatial integration;
6. pass source-value and source-tangent fidelity before any new Z0–Z5 Pu solve.

## Current artifacts

- `semantic_v2/10_governance/20260816_1131__NZSCCM__N48_ORDER_RESTORATION_AND_MULTIRATE_RETRACTION__LOCK.md`
- `semantic_v2/60_validation/steel_shell/20260816_1131__NZSCCM__MULTIRATE_ORDER_RETRACTION_AND_N48_RESTORATION__AUDIT.md`
- `semantic_v2/00_index/20260816_1131__NZSCCM__PROJECT__CURRENT_STATE_FIXED_N48_ORDER_RESTORED__SEMANTIC_INDEX.md`

The 11:10 multirate files remain in GitHub as historical diagnostics but are superseded for current compiler governance.
