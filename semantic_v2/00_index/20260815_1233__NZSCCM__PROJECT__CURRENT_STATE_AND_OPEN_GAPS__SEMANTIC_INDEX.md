# CURRENT STATE AND OPEN GAPS — NZ-SCCM

**Timestamp:** 2026-08-15 12:33 +08:00  
**Identity:** CURRENT_PRIMARY / OPERATIONAL ENTRY / USER-DIRECTED COMPARISON CORRECTION  
**Supersedes as operational entry:** `20260815_1148__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md`

---

## 0. Parent NZ-SCCM theory remains locked

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

The NZ steel-shell object retains its project reduction: internal steel webs are equivalent/absorbed into the continuous concrete core; only the two outer faceplates remain explicit steel-shell members.

---

## 1. Comparison identity corrected by user direction

The former next task

```text
D1-R_REDERIVE_REDUCED_Dx_Dy_H_AND_SOURCE_CONSISTENT_Pcr
```

is cancelled.

The current comparison intentionally uses different representations on the two sides:

```text
NZ_OBJECT = reduced analytical object / web steel equivalent into concrete
ZHOU_OBJECT = original full MCFSTW / internal steel webs retained
ZHOU_FORMULAS = original source formulas without reduction
COMPARISON = intentional cross-representation reference
```

The previous `PROJECT_TRANSFERRED_REDUCED_EMPIRICAL_COMPARATOR` is historical only and is superseded for current Z0-Z6 comparison.

Governance:

- `semantic_v2/10_governance/20260815_1233__NZSCCM_REDUCED_VS_ZHOU_ORIGINAL_FULL__COMPARISON_IDENTITY__LOCK.md`

---

## 2. Current NZ values used for comparison

Z0-Z5 use the current user-directed `A0=a/500 + local progressive radial-cap`, degree-32 engineering-diagnostic recalculation. Z6 uses the same current degree-32 comparator identity from the Z6-C execution.

```text
Z0 = 36.619330 MN
Z1 = 23.190470 MN
Z2 = 40.208070 MN
Z3 = 45.022780 MN
Z4 = 66.886850 MN
Z5 = 13.177570 MN
Z6 = 37.50942609 MN
```

These are not promoted to new strict production certificates; the local-cap material compiler remains diagnostic and the direct Chapter-5 restatement of the `a/500` imperfection has not been separately recovered.

---

## 3. Zhou original full-MCFSTW Z0-Z6 recalculation completed

Original source chain replayed:

```text
full MCFSTW steel/concrete areas
-> Pyth = fy As + fc' Ac
-> original Dx,Dy,Dxy,Dmu,H
-> four-edge SSSS Eq.5-79 integer-m Pcr
-> lambda_n = sqrt(Pyth/Pcr)
-> Eqs.5-87/5-88 phi_N
-> Pu_Zhou_original = phi_N Pyth
```

Final results:

|case|Zhou original full Pu MN|NZ current MN|NZ-Zhou|
|---|---:|---:|---:|
|Z0|36.945541|36.619330|-0.883%|
|Z1|23.721432|23.190470|-2.238%|
|Z2|41.213379|40.208070|-2.439%|
|Z3|44.320271|45.022780|+1.585%|
|Z4|70.187272|66.886850|-4.702%|
|Z5|14.681648|13.177570|-10.245%|
|Z6|49.672436|37.509426|-24.486%|

Summary:

```text
MAPE_Z0_Z5 = 3.6821%
MAPE_Z0_Z6 = 6.6541%
Z0_Z4 = all within +/-5%
Z5 = secondary underprediction
Z6 = dominant outlier
```

The Zhou-original formula values are 6.8%-13.1% higher than the superseded project-transferred reduced comparator for these seven cases.

Selected Eq.5-79 integer halfwaves:

```text
Z0 m*=1
Z1 m*=1
Z2 m*=1
Z3 m*=1
Z4 m*=1
Z5 m*=2
Z6 m*=1
```

All `m=1..50` candidates are generated and printed by the reproduction kernel; selected states and initial candidates are retained in the intermediate JSON.

Artifacts:

- `semantic_v2/40_execution/steel_shell/20260815_1233__ZHOU_ORIGINAL_FULL_MCFSTW__Z0_Z6__RECALCULATION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260815_1233__ZHOU_ORIGINAL_FULL_MCFSTW__Z0_Z6__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260815_1233__ZHOU_ORIGINAL_FULL_MCFSTW__Z0_Z6__REPRO.py`
- `semantic_v2/50_results/steel_shell/20260815_1233__ZHOU_ORIGINAL_FULL_MCFSTW__Z0_Z6__RESULT.csv`

---

## 4. Current interpretation

```text
NZ_INTERNAL_WEB_EQUIVALENCE = RETAINED
ZHOU_INTERNAL_WEB_FULL_TOPOLOGY = RETAINED
D1_R_REDUCED_ZHOU_REDERIVATION = CANCELLED
OLD_TRANSFERRED_REDUCED_ZHOU_COMPARATOR = SUPERSEDED_FOR_CURRENT_COMPARISON
ZHOU_ORIGINAL_Z0_Z6_FORMULA_REPLAY = COMPLETE
Z0_Z4_ENGINEERING_AGREEMENT = STRONG
Z5_OUTLIER = MODERATE
Z6_OUTLIER = LARGE / REMAINS PRIMARY DIAGNOSTIC TARGET
R10_CHANGE = NOT JUSTIFIED
N48_ORDER_CHANGE = NOT JUSTIFIED
```

The corrected comparison does not support a universal material correction: Z0-Z4 are already within +/-5%, while Z6 remains approximately 24.5% low. Any next causal work should therefore target geometry/slenderness/half-wave/stability-control mechanisms that distinguish Z6, not globally refit the parent material model.

---

## 5. Open project debts retained

```text
CASE21 = COMPLETE / FULL L-KZ PASS
SWARTZ24_Pu = 24/24 AVAILABLE
SWARTZ24_FULL_24_PANEL_SAME_EXPRESSION_L_KZ = OPEN / DEFERRED
Z1_Z3_Z4_Z5_OLD_IDENTITY_STRICT_RQ_L_CERTIFICATES = RETAINED PROVENANCE
LOCAL_CAP_FULL_INCREMENTAL_J2_FLOW_HISTORY = NOT CLAIMED
```

---

## 6. Current next-task state

The user-requested Zhou-original Z0-Z6 recalculation is complete.

```text
CURRENT_NEXT_TASK = USER_DIRECTED_AFTER_ZHOU_ORIGINAL_Z0_Z6_RECALCULATION
```

No new model modification is authorized by this state file alone.
