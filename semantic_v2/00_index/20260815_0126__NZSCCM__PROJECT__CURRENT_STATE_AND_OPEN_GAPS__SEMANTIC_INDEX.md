# CURRENT STATE AND OPEN GAPS — NZ-SCCM

**Timestamp:** 2026-08-15 01:26 +08:00  
**Identity:** CURRENT_PRIMARY / OPERATIONAL ENTRY / NO THEORY CHANGE  
**Supersedes as current-entry status:** `20260813_TUNK__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md` and legacy mutable `current/CURRENT_STATE.md` content dated 2026-08-13 00:47 +08:00.  
**Pre-update remote HEAD audited:** `a08540542f8322080592b56c4f2edec2bcd7f825` (`Persist Z1 Z3 Z4 Z5 strict same-expression AD certification`).

---

## 0. Governing production identity

The successful ordinary-concrete parent theory remains locked. No result in the 2026-08-14 steel-shell work reopens it.

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
HALFWAVE_SELECTION = THEORETICAL ENERGY/MINIMUM PRINCIPLE FROM DESIGN DATA
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
SECOND_ORDER_MEMBRANE_TERMS = INCLUDED
R10_MATERIAL_TARGET = FROZEN
COMPILER = N48-C1/MM
CAYLEY_HAMILTON = GOVERNING
FULL_DIRECTIONAL_CURRENT_TANGENT = REQUIRED
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
DIRECT_LIMIT_EQUATIONS = Rq=0 + L=0 + FIRST +->- MAXIMUM
CURRENT_TANGENT_STABILITY = ZHOU/NAVIER SAME-BRANCH CHECK
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
EXPERIMENTAL_LOAD_USED_FOR_TUNING = NO
PANEL_LEVEL_SURROGATE = NO
```

Parent governance:

- `semantic_v2/10_governance/20260813_1834__NZSCCM__NC_PANEL__ENERGY_MINIMUM_HALFWAVE_R10_N48C1MM_D15_DIRECT_LIMIT__LOCKED_BASELINE.md`

This lock explicitly rejects two superseded diagnostic interpretations:

1. experimental/FE observed long or irregular bulges do not redefine the formal production halfwave;
2. independent in-plane Ritz coordinates are not added to “repair” membrane action already present in Nguyen second-order kinematics.

---

## 1. Ordinary-concrete / Swartz status retained

Case21 remains the closed zero-spatial-quadrature benchmark:

```text
CASE21_ZERO_SPATIAL_ANALYTIC_CALCULATION = COMPLETE
CASE21_FULL_L_KZ_GATE = PASS
CASE21_CONTROL = FIRST +->- LIMIT POINT
CASE21_PRELIMIT_TANGENT_STABILITY = PASS
CASE21_THEORY_Pu = 365.580427565 kN
CASE21_FAILURE_LOAD_Pf = 368.3127497435694 kN
CASE21_Pu_VS_Pf_ERROR = -0.741848 %
NGUYEN_CASE21_336_kN = EXPERIMENTAL_Pcr / NOT Pf
```

Swartz24 remains:

```text
SWARTZ24_FRESH_Pu = 24/24 AVAILABLE
SWARTZ24_Pu_VS_FAILURE_COMPARISON = COMPLETE
SWARTZ24_FULL_SAME_EXPRESSION_L_KZ_GATE = NOT COMPLETE
```

The 2026-08-13 bulk-gate audit remains binding: old direct-N48 roots must not be attached to later C1/MM + general-D15 Pu values. The full 24-panel L/KZ signature is an open reproducibility/execution gap, not a failed theory result.

Relevant audit:

- `semantic_v2/60_validation/swartz24/20260813_1035__NZSCCM__SWARTZ24__FULL_SAME_EXPRESSION_L_KZ_BULK_GATE__EXECUTION_AUDIT.md`

Current project priority does **not** require reopening this bulk gate before the steel-shell Z6 diagnosis unless explicitly redirected.

---

## 2. Steel-shell extension identity

The active extension replaces the reinforcement contribution with continuous finite-thickness outer steel shell layer(s), while leaving the concrete/kinematics/compiler/moment/limit architecture unchanged:

```text
Pc + Ps(rebar)   -> Pc + Psh(finite-thickness shell)
Rq,c + Rq,s      -> Rq,c + Rq,sh
KZ,c + KZ,s      -> KZ,c + KZ,sh
```

Structural extension contract:

- `semantic_v2/20_theory/nc_steel_shell_panel/20260813_1834__NZSCCM__NC_STEEL_SHELL_PANEL__REBAR_REPLACEMENT_GENERAL_D15__THEORY_EXTENSION_CONTRACT.md`

Current reduced steel governance is:

```text
STEEL = IDEAL ELASTIC-PERFECTLY-PLASTIC
YIELD_FIRST -> no elastic Yun branch before yield
ELASTIC_LOCAL_BUCKLING_FIRST -> Yun-Lu large-deflection branch before yield
CONTINUING_PLASTIC_LOADING -> Et,eff = 0
STRENGTH_CAP -> |sigma_s| <= fy
B_s, Y_s, KZ=0, L=0 = DISTINCT EVENTS
```

Governing correction:

- `semantic_v2/10_governance/20260814_TUNK__NZSCCM__STEEL_SHELL__YUN_IDEAL_EP_TANGENT_AND_ZHOU_SSSS_BENCHMARK__LOCKED_CORRECTION.md`

The current Zhou Table-5.1 reduced execution uses a homogeneous whole-shell J2 radial strength cap only as an authorized **reduced branch diagnostic** after first yield. It is not claimed to be the final full 2D expanding-plastic-zone production operator.

---

## 3. Zhou Z0–Z6 representative batch — current numerical status

The seven points are representative parameter combinations within Zhou Table 5.1 ranges. They are **not** claimed to be seven literal physical test specimens or seven literal FE database rows.

Same-object comparison rule on both sides:

```text
continuous concrete core
+ two continuous outer steel faceplates
+ internal web steel deleted from independent steel-bearing/stiffness contribution
```

Current reduced connected-branch results:

|Case|NZ-SCCM Pu,diag (MN)|Zhou comparator (MN)|error|control|
|---|---:|---:|---:|---|
|Z0|34.2976005|33.4291234|+2.598%|yield-cusp first maximum|
|Z1|20.8986273|22.2081472|-5.897%|smooth post-yield maximum|
|Z2|37.7463434|36.8588415|+2.408%|yield-cusp first maximum|
|Z3|42.3390407|41.1581454|+2.869%|smooth post-yield maximum|
|Z4|62.0371297|62.0430260|-0.010%|smooth post-yield maximum|
|Z5|12.8784090|13.0976000|-1.674%|smooth post-yield maximum|
|Z6|34.2612499|44.7404028|-23.422%|yield-cusp first maximum|

```text
MAPE_Z0_Z6 = 5.554 %
MAPE_Z0_Z5 = 2.576 %
LARGEST_OUTLIER = Z6
```

Execution package:

- `semantic_v2/40_execution/steel_shell/20260814_2240__NZSCCM_Z0_Z6__VS_ZHOU__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260814_2240__NZSCCM_Z0_Z6__CONNECTED_BRANCH__KEYPOINTS.csv`
- `semantic_v2/40_execution/steel_shell/20260814_2240__NZSCCM_Z0_Z6__REDUCED_IDEALEP_D15__PARAMS.json`
- `semantic_v2/40_execution/steel_shell/20260814_2240__NZSCCM_Z0_Z6__REDUCED_IDEALEP_D15__REPRO.py`

---

## 4. Strict same-expression Rq-L certification already completed

Z1, Z3, Z4 and Z5 have been upgraded from smooth connected-branch peak localization to same-expression forward-AD `Rq=0 + L=0` engineering certificates.

|Case|D|q|Pu (MN)|error vs Zhou|Rnorm|Lnorm|decision|
|---|---:|---:|---:|---:|---:|---:|---|
|Z1|0.6076158841|0.001631384062|20.89868703|-5.8963%|4.39e-10|-8.59e-7|PASS|
|Z3|0.8469249001|0.001408113142|42.33906044|+2.8692%|7.89e-10|+2.74e-8|PASS|
|Z4|0.9497834233|0.000594936054|62.03715150|-0.00947%|1.76e-9|+4.02e-7|PASS|
|Z5|0.9886228551|0.000119178791|12.87876017|-1.6708%|3.89e-8|+5.16e-9|PASS|

The strict roots change the earlier smooth-peak loads by only approximately `0.02–0.35 kN`; the purpose of the latest execution was mathematical identity closure rather than numerical retuning.

Certificate:

- `semantic_v2/40_execution/steel_shell/20260815_0016__Z1_Z3_Z4_Z5__SAME_EXPRESSION_AD__CERTIFICATION_REPORT.md`
- `semantic_v2/50_results/steel_shell/20260815_0016__Z1_Z3_Z4_Z5__STRICT_RQ_L_CERTIFICATION__RESULT.csv`

```text
Z1_SAME_EXPRESSION_RQ_L = PASS
Z3_SAME_EXPRESSION_RQ_L = PASS
Z4_SAME_EXPRESSION_RQ_L = PASS
Z5_SAME_EXPRESSION_RQ_L = PASS
RERUN_Z1_Z3_Z4_Z5_WITHOUT_NEW_CAUSE = NOT CURRENT PRIORITY
```

---

## 5. Z0 and Z2 identity

Z0 and Z2 are currently localized at a **yield cusp**: the elastic connected branch rises to first yield and the authorized reduced post-yield branch immediately descends.

Therefore a fictitious smooth `L=0` root must not be manufactured across the constitutive cusp merely to imitate Z1/Z3/Z4/Z5. Their next mathematical work, if required, is event/cusp certification using the left/right branch identities, not forced smooth differentiation through yield.

```text
Z0_CONTROL = YIELD_CUSP_FIRST_MAXIMUM
Z2_CONTROL = YIELD_CUSP_FIRST_MAXIMUM
FORCED_SMOOTH_L0_ACROSS_CUSP = PROHIBITED
```

---

## 6. Z6 — active unresolved outlier

Current state:

```text
Z6_D = 0.663425
Z6_q = 0.0054394
Z6_Pc = 11.9026733 MN
Z6_Ps = 22.3585766 MN
Z6_Pu_diag = 34.2612499 MN
Z6_Zhou = 44.7404028 MN
Z6_ERROR = -23.422 %
Z6_CONTROL = YIELD_CUSP_FIRST_MAXIMUM
```

Geometry/material identity:

```text
a = 9000 mm
b = 12000 mm
h = 130 mm
tc = 122 mm
ts_each_face = 4 mm
fy = 355 MPa
fcu = 40 MPa
ell = 9000 mm
q0 = 1/400 = 0.0025
```

Z6 is qualitatively distinct from Z0–Z5:

1. it has the largest current equilibrium amplitude (`q=0.0054394`);
2. it has the most slender representative global geometry (`a/h≈69.23`, `b/h≈92.31`);
3. its continuous reachable material spectrum extends beyond the standard positive compiler bound;
4. its N48 T compiler therefore uses the expanded interval `[-1.15,0.23]` and has the largest recorded minimax objective (`~0.148153477`);
5. it remains strongly low relative to Zhou even after that interval extension.

This does **not** authorize a Z6-specific load factor, R10 refit, halfwave fit, cross-case scaling, or experimental/result-driven compiler tuning.

---

## 7. Z6 diagnostic priority and isolation order

The current next task is to isolate the Z6 discrepancy without reopening passed cases.

### Z6-A — comparator / imperfection identity

Audit whether the Z6 NZ-SCCM imperfection convention and the Zhou elastoplastic comparator use the same physical imperfection amplitude and normalization. This is a comparator-identity check, not a calibration step.

### Z6-B — compiler-fidelity sensitivity

Quantify how much of the `-23.422%` gap can plausibly be attributed to the expanded positive material spectrum / T-minimax error while keeping N48 and the frozen R10 target unchanged for production identity.

### Z6-C — reduced steel post-yield continuation

Audit the homogeneous whole-shell J2 radial cap against the yield-front mechanics actually required by a very wide/slender shell. Determine whether the reduced homogeneous cap creates excessive post-yield loss for Z6. Do not silently promote an unproved 2D plastic-zone model.

### Z6-D — geometry / halfwave / stability ordering

Recheck the design-side minimum-energy halfwave and same-branch `K_Z` ordering for the Z6 geometry. Experimental/FE observed mode shape remains prohibited as a production halfwave input.

### Decision rule

```text
DO_NOT_CHANGE_R10_FIRST
DO_NOT_RERUN_Z1_Z3_Z4_Z5_FIRST
DO_NOT_APPLY_Z6_FITTED_FACTOR
ISOLATE_COMPARATOR_IDENTITY_BEFORE_MATERIAL_REDESIGN
```

---

## 8. Repository governance/open gaps

The active semantic namespace is `semantic_v2/`.

The old 2026-08-13 current-state entry is retained as provenance but is no longer the operational entry after this file.

Repository branch cleanup remains separate from theory execution. At the pre-update audit, `canonical-rebuild-20260813` and `main` were diverged; the rebuild branch was not silently merged into the current theory head. No open PR or issue was present.

```text
SEMANTIC_V2 = ACTIVE
OLD_20260813_CURRENT_STATE = SUPERSEDED_AS_OPERATIONAL_ENTRY
REBUILD_BRANCH_CLEANUP = OPEN_REPOSITORY_GOVERNANCE_TASK
THEORY_RESULT_IDENTITY = UNAFFECTED_BY_BRANCH_CLEANUP
```

---

## 9. Current operational status

```text
NC_PARENT_THEORY = LOCKED
CASE21 = COMPLETE / FULL L-KZ PASS
SWARTZ24_Pu = 24/24 AVAILABLE
SWARTZ24_FAILURE_COMPARISON = COMPLETE
SWARTZ24_FULL_24_PANEL_L_KZ = OPEN / DEFERRED BY CURRENT PRIORITY
STEEL_SHELL_EXTENSION = ACTIVE
ZHOU_Z0_Z6_REDUCED_BATCH = 7/7 CALCULATED
Z1_Z3_Z4_Z5_SAME_EXPRESSION_RQ_L = 4/4 PASS
Z0_Z2 = YIELD_CUSP CONTROL / DO NOT FORCE SMOOTH L0
Z6 = ACTIVE OUTLIER / ROOT-CAUSE ISOLATION REQUIRED
FULL_2D_STEEL_PLASTIC_ZONE_OPERATOR = NOT CLAIMED
STRUCTURAL_CALIBRATION = NO
FORMAL_SPATIAL_QUADRATURE = 0
CURRENT_NEXT_TASK = Z6_ROOT_CAUSE_ISOLATION_BEGIN_WITH_COMPARATOR_IMPERFECTION_IDENTITY
```
