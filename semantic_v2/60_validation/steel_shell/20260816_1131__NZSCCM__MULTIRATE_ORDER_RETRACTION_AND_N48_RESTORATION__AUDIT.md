# NZ-SCCM — audit: multirate-order retraction and fixed N48 restoration

**Timestamp:** 2026-08-16 11:31 +08:00

## Audit question

Did the 11:10 source-fidelity repair change a previously frozen material compiler order without user authorization?

Yes. It introduced primitive orders `256/1024/1280/512`, while the prior material compiler governance had fixed order 48.

## Corrective decision

```text
MULTIRATE_ORDER_ESCALATION_1110 = RETRACTED_FROM_CURRENT_GOVERNANCE
MATERIAL_COMPILER_ORDER = 48
U_ORDER = 48
C_ORDER = 48
T_ORDER = 48
T7_ORDER = 48
```

The 11:10 numerical source-fidelity study remains useful only as diagnostic evidence that the R10 small-positive transition is difficult to represent. It does not authorize order escalation.

## Retained earlier defect

The separate 10:54 finding remains active:

```text
Z6_WIDE_N48_COEFFICIENT_SET_ON_[-2.35,+1.90] = INVALID_FOR_Z0_Z5
```

because its errors in the occupied Z0–Z5 material domain were approximately

```text
T ~ .704
T7 ~ .796
```

Therefore restoring N48 does **not** restore the invalid wide-hull coefficient set as acceptable production input.

## Current valid interpretation

The only currently authorized repair space is:

```text
fixed degree 48
+ unchanged R10 physical operator
+ source-only coefficient-generation / analytic-representation improvement
+ exact C1 anchors
+ Cayley-Hamilton / General-D15 compatibility
+ zero spatial numerical integration
```

No new Z0–Z5 Pu is authorized until fixed-N48 source fidelity passes.

## Verdict

```text
USER_ORDER_CORRECTION = APPLIED
FIXED_N48_ORDER = RESTORED
1110_MULTIRATE_COMPILER = HISTORICAL_DIAGNOSTIC_ONLY
OLD_WIDE_N48_Z0_Z5_USE = STILL_PROHIBITED
Z6_51.30_MN = RETAINED
Z0_Z5_CORRECTED_Pu = NOT_YET_CALCULATED
```
