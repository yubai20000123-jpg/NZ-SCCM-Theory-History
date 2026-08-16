# NZ-SCCM — fixed N48 order restoration and multirate-order retraction

**Timestamp:** 2026-08-16 11:31 +08:00  
**Status:** CURRENT GOVERNANCE LOCK

## User correction

The user explicitly rejected the 11:10 change of material polynomial order and instructed the project to restore the previous fixed order.

Therefore the following 11:10 proposal is retracted from current production governance:

```text
R10-MR-C1(256,1024,1280,512)
U=256
C=1024
T=1280
T7=512
```

The 11:10 artifacts are retained only as historical source-fidelity diagnostics. They are not deleted, but they must not be used as the current material compiler or as the basis of any Z0–Z5 production calculation.

## Restored order lock

The formal material compiler order is restored to

```text
MATERIAL_COMPILER_ORDER = 48
U_ORDER  = 48
C_ORDER  = 48
T_ORDER  = 48
T7_ORDER = 48
```

The previously frozen compiler family identity is restored as the order-level baseline:

```text
U  = N48-C1
C  = N48-C1
T7 = N48-C1
T  = N48-C1-CONSTRAINED-MINIMAX
```

This order may not be changed again without explicit user authorization.

## What is and is not restored

The order is restored to 48, but the 10:54 fidelity finding remains valid:

```text
REUSE_Z6_WIDE_N48_COMPILER_FOR_Z0_Z5 = PROHIBITED
```

because the single Z6-wide interval `[-2.35,+1.90]` gave order-one errors in the actually occupied Z0–Z5 small-positive tension region.

Thus the project must not confuse two separate statements:

1. **degree/order = 48 is restored and locked**;
2. **the old wide-hull N48 coefficient set is still invalid for Z0–Z5**.

The next repair must remain within degree 48 and solve the material-fidelity problem by coefficient-generation / analytic-representation strategy only, without arbitrary order escalation.

## Frozen structural boundary

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

## Capacity status

```text
Z6_AR2_Pu = 51.30 MN  # user accepted and retained
Z0_Z5_20260816_1043_Pu = RETRACTED_PENDING_RECALCULATION
NEW_Z0_Z5_Pu = NOT_CALCULATED
```

## Current next gate

```text
Z0_Z5_AR2_FIXED_N48_CURRENT_OPERATOR_FIDELITY_REBUILD_ZERO_SPATIAL_INTEGRATION
```

Requirements:
- all four source primitives remain degree 48;
- R10 physical law unchanged;
- no experiment/Zhou/Winter/Pu enters coefficient generation;
- no spatial numerical integration or material-point grid;
- first pass source-value and source-tangent fidelity on the required material domain;
- only after that may Z0–Z5 be recalculated.
