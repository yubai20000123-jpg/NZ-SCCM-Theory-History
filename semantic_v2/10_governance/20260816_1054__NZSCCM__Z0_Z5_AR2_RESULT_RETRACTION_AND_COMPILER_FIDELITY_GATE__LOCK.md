# NZ-SCCM — Z0–Z5 AR2 result retraction and compiler-fidelity gate

**Timestamp:** 2026-08-16 10:54 +08:00  
**Status:** CURRENT GOVERNANCE LOCK

## Trigger

The user challenged the 10:43 Z0–Z5 AR2 results because stockier / lower-width-thickness-ratio specimens should not show such large strength losses from membrane redistribution without a clear mechanism.

The challenged 10:43 values are therefore not to be treated as production truth until the calculation chain is independently audited.

## Immediate decision

```text
20260816_1043_Z0_Z5_AR2_Pu_VALUES = RETRACTED_PENDING_RECALCULATION
20260816_1043_Z0_Z5_ZHOU_WINTER_ERROR_TABLE = RETRACTED_PENDING_RECALCULATION
Z6_51.30_MN = USER_ACCEPTED_AND_RETAINED
```

The 10:43 artifacts remain preserved as historical/error evidence and are not deleted.

## Proven process defect

The 10:43 run reused the Z6 wide material compiler interval

`lambda in [-2.35,+1.90]`

for every Z0–Z5 case. Under the frozen N48-C1/MM basis, the committed wide-hull scalar material representation has approximately

```text
T max error   ~= 0.704
T^7 max error ~= 0.796
```

and the same error peaks occur inside the actual Z0–Z5 reachable lambda ranges, around the small-positive tension transition (`lambda~0.04–0.05`).

This is not a tight remainder-certificate issue. It is an order-one material-operator fidelity failure. A capacity difference of 8–24% cannot be accepted when one material activation basis is wrong by roughly 70–80% in the actually visited material domain.

Therefore:

```text
REUSE_Z6_WIDE_N48_COMPILER_FOR_STOCKY_Z0_Z5 = PROHIBITED
```

## What is not yet blamed

The audit does **not** yet prove that the Nguyen second-order geometry, one-complete-halfwave mapping, or generalized q-equilibrium is wrong. The current 10:43 amplitudes are of the same order as the classical imperfect-plate amplification estimate.

## New mandatory next gate

```text
Z0_Z5_AR2_CURRENT_OPERATOR_FIDELITY_REBUILD_ZERO_SPATIAL_INTEGRATION
```

Requirements:
1. retain the original R10 physical current operator;
2. retain zero spatial sampling/quadrature/subdomains=1;
3. do not use Zhou/Winter in the solve;
4. replace the single wide N48 material representation by a materially faithful analytic/multiscale coefficient representation over the actually reached invariant domain;
5. validate the material representation before solving Pu;
6. only then recompute Z0–Z5 connected branches and peaks.

No corrected Z0–Z5 Pu is released by this lock.
