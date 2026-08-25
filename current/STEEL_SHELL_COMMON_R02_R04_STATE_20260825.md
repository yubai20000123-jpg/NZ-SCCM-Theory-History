# CURRENT STATE — Steel-shell common R02/R04 interface

**Updated:** 2026-08-25 14:50 +08:00  
**Status:** `COMMON_AUDIT_COMPLETE / SSNC_AND_SSUHPC_SHARED / NO_PRODUCTION_CHANGE`

Canonical parent:

`current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`

Canonical common audit:

`semantic_v2/40_execution/steel_shell/20260825_1450__NZSCCM__STEEL_SHELL_COMMON_R02_R04_LOCAL_YIELD_AUDIT_Z6_T360_R01.md`

---

## 0. Highest-priority scope correction

```text
R02/R04 = STEEL-SHELL COMMON MODULE
NOT = SSUHPC-SPECIFIC MODULE
```

SSNC and SSUHPC use the same R02 finite PBL/Yun face operator and the same R04 path-free ideal-EP mean-stress Mises cap.

Therefore any future local-yield/resultant refinement must be common to both families.

The previous `SSUHPC-only R06` interpretation is superseded in scope. The preceding SSUHPC diagnosis remains useful as T360 evidence, but it is not a material-specific repair authorization.

---

## 1. Z6 control result

Current Z6 R05 remains frozen:

```text
Pu = 49.45439833719624 MN
local cell = 200 x 200 x 4 mm
sigma_cr = 794.3887 MPa > fy = 355 MPa
A0 = 0.125 mm
U = 0.1270986807 mm
U/A0 = 1.01678945
```

At the current Z6 endpoint:

```text
mean trial Mises = 507.41735 MPa
max finite-harmonic local membrane Mises ≈ 507.50506 MPa
local/mean amplification = 1.00017284
R04 lambda = 0.69962132
first local-Mises yield eta = 0.69950131
first mean-Mises yield eta = 0.69962132
Yun axial-yield eta ≈ 1.18491 > current terminal scale
```

Decision:

```text
Z6_LOCAL_BUCKLING_BEFORE_YIELD = NO
Z6_LOCAL_FIELD_HOMOGENIZATION_ERROR = NEGLIGIBLE AT CURRENT R05 ENDPOINT
Z6_R05_Pu = NOT REOPENED
```

---

## 2. T360 contrast result

Current T360 R01 remains frozen:

```text
Pu = 12.18255684307 MN
local cell = 360 x 375 x 4 mm
sigma_cr = 245.7949 MPa < fy = 355 MPa
A0 = 0.225 mm
U_top/A0 = 3.44535
U_bottom/A0 = 12.73991
```

Upper face:

```text
mean trial Mises = 347.6065 MPa < fy
max local membrane Mises ≈ 374.5803 MPa > fy
R04 lambda = 1
```

Lower face:

```text
mean trial Mises = 549.2084 MPa
R04 lambda = 0.64638493
current capped mean Mises = 355 MPa
max local membrane Mises before mean cap ≈ 919.8894 MPa
hypothetical same-lambda local Mises ≈ 594.603 MPa > fy
Yun-source local axial compression at current state ≈ 864.49 MPa > fy
first local axial-yield eta ≈ 0.41317
first local-Mises yield eta ≈ 0.41924
first mean-Mises yield eta ≈ 0.62378
```

Decision:

```text
T360_LOCAL_BUCKLING_BEFORE_YIELD = YES
T360_LOCAL_VS_MEAN_YIELD_SEPARATION = STRONG
T360_CURRENT_R04_CAN_RETAIN_EXCESS_FACE_RESULTANT = DIAGNOSTICALLY_CONFIRMED
T360_R01_Pu = NOT YET REPLACED
```

---

## 3. Common regime interpretation

The same steel-shell operator has two regimes:

```text
STOCKY / YIELD-FIRST:
    sigma_cr > fy
    U/A0 near 1
    local redistribution weak
    local and mean yielding nearly coincide
    example: Z6

LOCAL-BUCKLING-FIRST:
    sigma_cr < fy
    U/A0 grows strongly
    local redistribution strong
    local yield can precede mean-Mises cap materially
    example: T360
```

Therefore:

```text
CORE_MATERIAL_LABEL (NC vs UHPC) = NOT THE ACTIVATION VARIABLE
LOCAL STEEL-SHELL STATE = ACTIVATION VARIABLE
```

---

## 4. Current production and next boundary

Until a common refinement passes all gates:

```text
R02 = RETAIN
R04 = RETAIN AS CURRENT PRODUCTION
Z6_R05 = FROZEN
SSUHPC_R01_7CASE = FROZEN
EFFECTIVE_WIDTH/AREA = PROHIBITED
COMPARATOR_IN_ROOT_SELECTION = 0
R03_REOPENED = NO
```

If the user authorizes the next step, it must be:

```text
STEEL_SHELL_COMMON_R06
```

not `SSUHPC_R06`.

Required gates:

1. common implementation for SSNC and SSUHPC;
2. finite R02 local harmonic field retained;
3. formal spatial sampling/quadrature/material points remain zero;
4. no effective-width construction;
5. zero/local-weak redistribution degeneration recovers current R04;
6. Z6 blind non-regression;
7. T360 and BH032 blind local-buckling reruns;
8. comparator reopening only after root fixation.
