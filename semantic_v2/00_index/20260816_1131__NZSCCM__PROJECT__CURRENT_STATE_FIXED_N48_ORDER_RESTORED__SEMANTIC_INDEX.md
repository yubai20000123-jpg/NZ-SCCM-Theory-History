# NZ-SCCM current semantic index — fixed N48 order restored

**Timestamp:** 2026-08-16 11:31 +08:00  
**Status:** CURRENT OPERATIONAL ENTRY

## User correction applied

The 11:10 multirate order escalation is withdrawn from current governance.

```text
U=256 / C=1024 / T=1280 / T7=512 = RETRACTED_FROM_CURRENT_PRODUCTION
```

The material compiler order is restored and locked as

```text
MATERIAL_COMPILER_ORDER = 48
U_ORDER = 48
C_ORDER = 48
T_ORDER = 48
T7_ORDER = 48
```

Current order-level compiler family:

```text
U  = N48-C1
C  = N48-C1
T7 = N48-C1
T  = N48-C1-CONSTRAINED-MINIMAX
```

No future order change is permitted without explicit user authorization.

## Important distinction

The fixed order is restored, but the old Z6-wide coefficient set is **not** restored for Z0–Z5.

The 10:54 audit remains valid:

```text
wide interval [-2.35,+1.90]
T error ~ .704
T7 error ~ .796
```

inside the actual Z0–Z5 material domain.

Therefore:

```text
FIXED_N48_ORDER = CURRENT
OLD_Z6_WIDE_N48_Z0_Z5_COEFFICIENT_SET = PROHIBITED
```

The next repair must stay at degree 48 and improve only coefficient generation / analytic representation of the unchanged R10 source law.

## Frozen structural scope

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
Zhou/Winter calibration=NO
```

## Capacity status

```text
Z6_AR2_Pu = 51.30 MN  # user accepted
Z0_Z5_1043_Pu = RETRACTED_PENDING_RECALCULATION
NEW_Z0_Z5_Pu = NOT_CALCULATED
```

## Current next gate

`Z0_Z5_AR2_FIXED_N48_CURRENT_OPERATOR_FIDELITY_REBUILD_ZERO_SPATIAL_INTEGRATION`

## Read order

1. `../10_governance/20260816_1131__NZSCCM__N48_ORDER_RESTORATION_AND_MULTIRATE_RETRACTION__LOCK.md`
2. `../60_validation/steel_shell/20260816_1131__NZSCCM__MULTIRATE_ORDER_RETRACTION_AND_N48_RESTORATION__AUDIT.md`
3. `20260816_1054__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_COMPILER_FIDELITY_RETRACTION__SEMANTIC_INDEX.md`
4. `20260816_1110__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY_PASS__SEMANTIC_INDEX.md` — historical diagnostic only; superseded for current compiler order
5. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md`
