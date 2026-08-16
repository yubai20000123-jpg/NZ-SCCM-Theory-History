# NC material semantic branch

## Current material target

- R10 physical current material target remains **CURRENT_SUPPORT / FROZEN**.
- R10 material physics is not reopened.
- Material compiler order is restored and locked at **48 for every primitive** by explicit user instruction.

Current order-level identity:

```text
MATERIAL_COMPILER_ORDER = 48
U  = N48-C1
C  = N48-C1
T7 = N48-C1
T  = N48-C1-CONSTRAINED-MINIMAX
```

No future change of polynomial order is permitted without explicit user authorization.

## 2026-08-16 order restoration

Current governance:

- `../10_governance/20260816_1131__NZSCCM__N48_ORDER_RESTORATION_AND_MULTIRATE_RETRACTION__LOCK.md`

The 11:10 multirate candidate

`R10-MR-C1(256,1024,1280,512)`

is **RETRACTED_FROM_CURRENT_PRODUCTION** and retained only as historical diagnostic evidence that the source transition can be approximated accurately when approximation capacity is increased. It has no current production identity.

## Retained source-fidelity problem

The fixed order restoration does not revive the old Z6-wide N48 coefficient set for Z0–Z5.

The 10:54 audit established that on the wide interval `[-2.35,+1.90]`, inside the actually occupied Z0–Z5 small-positive tension region, the current wide-hull representation had approximately

```text
T error   ~= .704
T7 error  ~= .796
```

Therefore:

```text
REUSE_Z6_WIDE_N48_COMPILER_FOR_Z0_Z5 = PROHIBITED
```

The required repair space is now strictly:

```text
fixed degree 48
+ unchanged R10 source law
+ exact C1 anchors
+ improved source-only coefficient-generation / analytic representation
+ Cayley-Hamilton compatibility
+ General-D15 compatibility
+ zero structural spatial integration
```

## Current production-status boundary

```text
FIXED_N48_ORDER = ACTIVE
R10_PHYSICAL_OPERATOR = FROZEN
OLD_Z6_WIDE_N48_Z0_Z5_COEFFICIENT_SET = INVALID
1110_MULTIRATE_ORDER_ESCALATION = HISTORICAL_DIAGNOSTIC_ONLY
NEW_Z0_Z5_Pu = NOT_CALCULATED
```

Current next gate:

`Z0_Z5_AR2_FIXED_N48_CURRENT_OPERATOR_FIDELITY_REBUILD_ZERO_SPATIAL_INTEGRATION`

## Historical compiler-fidelity support

- `20260813_1719__NZSCCM__NC_MATERIAL__VALUE_TANGENT_BALANCED_MINIMAX_AND_REACHABLE_SPECTRUM__COMPILER_AUDIT.md`
- `20260812_TUNK__NZSCCM__NC_MATERIAL__N48C1_T_CONSTRAINED_MINIMAX__GOVERNANCE.md`
- `20260812_TUNK__NZSCCM__NC_MATERIAL__T_CONSTRAINED_MINIMAX_BOUNDARY_LAYER__AUDIT.md`

These may inform a fixed-N48 coefficient-generation repair, but they do not authorize a change of order.
