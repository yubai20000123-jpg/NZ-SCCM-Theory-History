# CURRENT STATE AND OPEN GAPS — NZ-SCCM

**Timestamp:** 2026-08-15 11:48 +08:00  
**Identity:** CURRENT_PRIMARY / OPERATIONAL ENTRY / NO PARENT-THEORY CHANGE  
**Supersedes as operational entry:** `20260815_1058__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md`

---

## 0. Parent theory remains locked

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
R10 = FROZEN
N48-C1/MM = FROZEN
CAYLEY_HAMILTON = GOVERNING
GENERAL_D15 = GOVERNING
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

Case21 remains complete. Swartz24 24/24 Pu remains available; full 24-panel same-expression L/KZ gate remains open/deferred.

---

## 1. User-directed Z0-Z5 recalculation completed

The two Z6-exposed mechanisms were applied to Z0-Z5:

```text
IMPERFECTION_SENSITIVITY = A0=a/500 ; q0=a/(500b)
STEEL_POSTYIELD_DIAGNOSTIC = local progressive radial-cap current map
LOCAL_CAP_MATERIAL_COMPILER_PRIMARY_DEGREE = 32
LOCAL_CAP_DEGREE_SENSITIVITY = 24/32/40
FORMAL_STRUCTURAL_QUADRATURE = 0
```

This identity is not yet promoted to production because Chapter-5 Table-5.1 has not been directly recovered restating `a/500`, and local-cap degree sensitivity is non-negligible.

Degree-32 first-connected-maximum results:

|case|Pu diagnostic MN|current transferred comparator MN|error|
|---|---:|---:|---:|
|Z0|36.61933|33.42912|+9.543%|
|Z1|23.19047|22.20815|+4.423%|
|Z2|40.20807|36.85884|+9.087%|
|Z3|45.02278|41.15815|+9.390%|
|Z4|66.88685|62.04303|+7.807%|
|Z5|13.17757|13.09760|+0.611%|

```text
OLD_Z0_Z5_MAPE_VS_TRANSFERRED_COMPARATOR ~= 2.575%
NEW_D32_Z0_Z5_MAPE_VS_TRANSFERRED_COMPARATOR ~= 6.810%
ALL_NEW_SIGNED_ERRORS = POSITIVE
```

The old Z1/Z3/Z4/Z5 strict Rq-L certificates remain valid records of the old `q0=1/400 + whole-shell-cap` identity and are not overwritten.

Artifacts:

- `semantic_v2/40_execution/steel_shell/20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP_D15__RECALCULATION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP_D15__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP_D15__REPRO.py`
- `semantic_v2/50_results/steel_shell/20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP__RESULT.csv`

---

## 2. Z6-D1 same-object comparator audit completed

Decision:

```text
SOURCE_EXACT_SAME_OBJECT_ZHOU_COMPARATOR = NO
CURRENT_NUMERIC_ZHOU_COMPARATOR = TRANSFERRED_REDUCED_EMPIRICAL_COMPARATOR
```

Decomposition:

```text
Pyth_reduced = valid same-reduced-section strength replay
D_EI_reduced = valid reduced sandwich E*I diagnostic
Pcr currently used = project reduced isotropic diagnostic
source-exact reduced Dx,Dy,Dxy,Dmu,H = not closed
source-exact reduced Eq5-79 Pcr = not closed
phi_N(lambda) invariance after deleting internal webs = not demonstrated
```

Therefore previous Z0-Z6 error percentages must be interpreted as error relative to a **project-transferred comparator**, not relative to a source-exact Zhou capacity for the same reduced structure.

Z6 topology magnitude audit additionally shows that, if `ns=60` cells implies at least 59 internal separator webs, the omitted internal-web-only steel area is approximately `28792 mm2`, about `29.99%` of the retained outer-faceplate steel area. A strength-bookkeeping lower-bound difference is about `9.3459 MN`; no such correction is applied because web stiffness/support topology cannot be represented by a scalar strength addition.

Audit:

- `semantic_v2/60_validation/steel_shell/20260815_1148__NZSCCM__Z6_D1__ZHOU_COMPARATOR_SAME_OBJECT_TOPOLOGY__AUDIT.md`

---

## 3. Current interpretation

```text
Z6_A_IMPERFECTION_IDENTITY = SIGNIFICANT PARTIAL CAUSE
Z6_B_N48_COMPILER_WIDTH = MINOR
Z6_C_GLOBAL_CAP_ARTIFICIAL_CUSP = CONFIRMED
Z6_C_CAPACITY_RECOVERY_FROM_LOCAL_SPREADING = SMALL
Z6_D1_COMPARATOR_SAME_OBJECT_CLAIM = FAIL / RELABELLED
Z6_ERROR_AS_PURE_NZSCCM_MODEL_ERROR = PROHIBITED
R10_CHANGE = NOT JUSTIFIED
N48_ORDER_CHANGE = NOT JUSTIFIED
```

The Z0-Z5 recalculation reinforces the comparator concern: after a/500 + local spreading, Z0-Z4 generally move above the current transferred comparator instead of converging uniformly toward it.

---

## 4. Current next task

```text
CURRENT_NEXT_TASK = D1-R_REDERIVE_REDUCED_Dx_Dy_H_AND_SOURCE_CONSISTENT_Pcr
```

Required route:

1. stay on exactly the reduced object (continuous concrete core + two faceplates, no internal web steel member);
2. derive its source-consistent `Dx,Dy,Dxy,Dmu,H` rather than using the isotropic `D_EI` shortcut;
3. replay Zhou/Navier Eq.5-79 with those reduced stiffnesses;
4. only then recompute `lambda_n`;
5. separately decide whether Zhou's empirical `phi_N(lambda)` may be transferred across the topology change;
6. do not fit any of these quantities to the Z0-Z6 loads.

Alternative full-object route would require explicitly restoring web topology in NZ-SCCM and is not the current priority.
