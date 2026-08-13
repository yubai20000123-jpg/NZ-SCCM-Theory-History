# NZ-SCCM Case1 — current-branch reconstruction checkpoint after independent full-field audit

**Date:** 2026-08-13  
**Time:** TUNK  
**Identity:** EXECUTION CHECKPOINT OVERLAY / AUDIT VALUES SEPARATED FROM FORMAL VALUES

This file supersedes only the `NOT_YET_RECOVERED` audit-state fields in the earlier 16:47 checkpoint. It does **not** replace the formal zero-spatial D15 gate.

## 1. Formal theory identity remains frozen

```text
R10 = FROZEN
U/C/T7 = N48-C1
T = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
NGUYEN_SECOND_ORDER = GOVERNING
GENERAL_D15 = FORMAL STRUCTURAL MOMENT ENGINE
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
```

## 2. Audit-only recovered current Case1 state

Independent reconstruction from the current formulas gives:

```text
D_L_current_AUDIT = 0.98833818 approximately
q_L_current_AUDIT = 0.00083313173 approximately
P_L_current_AUDIT = 608.92642 kN approximately
stored P_L_current = 608.925 kN
```

The load difference from the stored value is about 0.0014 kN.

At that audit-reconstructed state:

```text
KZ_c_mat_AUDIT  = +4322.43 N/mm approximately
KZ_c_geo_AUDIT  = -1234.75 N/mm approximately
KZ_s_mat_AUDIT  = 0
KZ_s_geo_AUDIT  = -20.99 N/mm approximately
KZ_total_AUDIT  = +3066.68 N/mm approximately
```

A 15-state audit trace from D=0.05 to the load maximum kept KZ positive at all checked points.

## 3. Formal fields remain intentionally blank

```text
D_L_current_FORMAL_D15 = <BLANK_NOT_YET_REGENERATED_FROM_PRODUCTION_ENGINE>
q_L_current_FORMAL_D15 = <BLANK_NOT_YET_REGENERATED_FROM_PRODUCTION_ENGINE>
KZ_L_current_FORMAL_D15 = <BLANK_NOT_YET_REGENERATED>
D_KZ0_current_FORMAL_D15 = <BLANK_NOT_YET_REGENERATED>
q_KZ0_current_FORMAL_D15 = <BLANK_NOT_YET_REGENERATED>
P_KZ0_current_FORMAL_D15 = <BLANK_NOT_YET_REGENERATED>
FORMAL_CONTROL_EVENT = <UNRESOLVED>
FORMAL_GOVERNING_P = <UNRESOLVED>
```

The audit values are not copied into these formal fields.

## 4. Root-cause decomposition now recovered

At the old direct-N48 state:

```text
P_directN48_old_state = 599.51589536 kN
P_current_C1MM_same_old_state = 618.67743205 kN
compiler value shift = +19.16153669 kN
```

The old state is not a current equilibrium state (`Rq_AUDIT ≈ -453.13 kN mm`). Re-equilibration to the current load maximum reduces P by about 9.7510 kN, leaving a net +9.4105 kN increase.

Therefore the Case1 worsening is not explained by Pcr/Pf identity and is not presently explained by an earlier full-field KZ zero. The dominant recovered mechanism is the finite compiler's value/tangent trade-off away from the exact C1 anchor.

## 5. Next production gate

```text
rebuild zero-spatial coefficient-space Case1 evaluator
-> reproduce current Case1 Rq=0 / first load maximum
-> compute general-D15 full-field KZ on same branch
-> locate first KZ=0 if it exists
-> compare event order
-> only then promote governing Case1 capacity
```

If the production coefficient engine cannot be reconstructed in the current runtime, these formal fields remain blank and the audit evidence remains diagnostic only.

See:

`semantic_v2/60_validation/swartz24/20260813_TUNK__NZSCCM__CASE1__COMPILER_VALUE_SHIFT_AND_FULL_FIELD_KZ_RECONSTRUCTION__AUDIT.md`
