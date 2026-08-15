# CURRENT STATE AND OPEN GAPS — NZ-SCCM

**Timestamp:** 2026-08-15 10:58 +08:00  
**Identity:** CURRENT_PRIMARY / OPERATIONAL ENTRY / NO PARENT-THEORY CHANGE  
**Supersedes as current operational entry:** `20260815_0126__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md`.

---

## 0. Governing parent identity unchanged

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
HALFWAVE_SELECTION = THEORETICAL ENERGY/MINIMUM PRINCIPLE FROM DESIGN DATA
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
R10 = FROZEN
COMPILER = N48-C1/MM
CAYLEY_HAMILTON = GOVERNING
GENERAL_D15 = FROZEN
DIRECT_LIMIT = Rq=0 + L=0 + first admissible maximum where smooth
ZHOU/NAVIER_KZ = SAME-BRANCH CONTROL CHECK
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

Z1/Z3/Z4/Z5 same-expression Rq-L certificates remain PASS and are not reopened.

Swartz24 Pu remains 24/24 available; its full 24-panel same-expression L/KZ bulk gate remains open but deferred by the current Z6 priority.

---

## 1. Z6 root-cause sequence completed so far

### Z6-A comparator/imperfection identity

The batch uses `q0=1/400` (`A0=b/400=30 mm` for Z6). Zhou's source FE methodology uses first-mode imperfection scaled by member/wall height `a/500`, which would be `18 mm` for Z6 if the Chapter-2 convention carries into the Table-5.1 series. This has not been silently promoted to production input.

Sensitivity result:

```text
formal q0=1/400 whole-shell-cap Pu = 34.26125 MN
source-equivalent a/500 sensitivity Pu ~= 37.3777 MN
Zhou comparator = 44.74040 MN
```

Therefore imperfection normalization is a significant partial cause, but does not close Z6.

### Z6-B concrete material compiler width

Expanding the already widened Z6 N48 material interval changes Pu by only about `0.20 MN` while worsening the T-minimax objective. Compiler breadth is not the dominant 23.4% cause.

### Z6-C steel post-yield mechanism

Zhou steel is ideal elastic-perfectly-plastic; strain hardening is not an admissible explanation.

The old reduced continuation used one global whole-shell radial factor after the first yielded point. A new zero-formal-spatial-quadrature diagnostic instead uses a **local current radial-cap field** compiled in material coordinate and contracted by exact D15 moments.

Result for the formal `q0=1/400` identity:

```text
first-yield cusp at D=0.663425 is NOT retained as the local-cap terminal state
local progressive branch continues to D ~= 0.6922
terminal q-equilibrium fold q ~= 0.00580
P_local ~= 34.59 MN
increase over whole-shell-cap baseline ~= 0.333 MN
remaining error vs Zhou ~= -22.68 %
```

Thus the whole-shell cap **does create an artificial first-yield cusp**, but removing that globalization recovers only about `3.2%` of the original Z6 load gap.

For the separate `a/500` comparator-imperfection sensitivity:

```text
whole-shell-cap sensitivity ~= 37.3777 MN
local progressive radial-cap sensitivity ~= 37.49–37.51 MN
remaining error vs Zhou ~= -16.2 %
```

Again, local progressive spreading adds only about `0.11–0.13 MN` beyond the imperfection sensitivity.

Execution/report:

- `semantic_v2/40_execution/steel_shell/20260815_1058__NZSCCM__Z6__LOCAL_PROGRESSIVE_RADIAL_CAP_D15__EXECUTION_REPORT.md`
- `semantic_v2/50_results/steel_shell/20260815_1058__NZSCCM__Z6__LOCAL_PROGRESSIVE_RADIAL_CAP__RESULT.csv`

Identity boundary:

```text
LOCAL_PROGRESSIVE_RADIAL_CAP = ROOT-CAUSE DIAGNOSTIC CURRENT MAP
FULL_INCREMENTAL_LOCAL_J2_FLOW_HISTORY = NOT CLAIMED
```

---

## 2. Current Z6 decisions

```text
Z6_A_IMPERFECTION_IDENTITY = SIGNIFICANT PARTIAL CAUSE
Z6_B_N48_COMPILER_WIDTH = MINOR / NOT DOMINANT
Z6_C_STEEL_HARDENING_FIX = REJECTED
Z6_C_WHOLE_SHELL_CAP = ARTIFICIAL YIELD-CUSP SOURCE
Z6_C_WHOLE_SHELL_CAP_AS_PRIMARY_23P4_PERCENT_CAUSE = NOT SUPPORTED
R10_CHANGE = NOT JUSTIFIED
N48_ORDER_CHANGE = NOT JUSTIFIED
Z1_Z3_Z4_Z5_RERUN = NOT JUSTIFIED
```

The previous preflight label `homogeneous whole-shell cap = primary reduced-model deficiency candidate` is therefore superseded: it is a real deficiency, but quantitatively too small to be the main Z6 error source.

---

## 3. New active frontier: Z6-D geometry/comparator/stability identity

The highest-priority unresolved question moves to the extreme-slenderness/comparator side.

Required next execution order:

```text
Z6-D1 SAME-OBJECT COMPARATOR AUDIT
- verify that the reduced two-faceplate + concrete object used by NZ-SCCM is genuinely represented by the Zhou ultimate comparator at Z6
- especially audit what happens to internal-web support/stiffness when web steel bearing terms are deleted

Z6-D2 HALFWAVE / ENERGY-MINIMUM AUDIT
- independently replay the design-side admissible halfwave minimum for Z6
- no FE/test observed bulge used as input

Z6-D3 SAME-BRANCH KZ ORDERING
- evaluate KZ along the surviving local-cap branch
- establish whether tangent loss precedes the q-equilibrium fold / load maximum

Z6-D4 COMPARATOR VALIDITY AT EXTREME lambda
- Z6 has lambda ~= 1.386 and is the clear high-slenderness outlier
- audit whether Zhou Eqs. 5-87/5-88 remain a same-object comparator after the project reduction
```

No structural load factor, halfwave fit, R10 refit or experimental root selection is authorized.

---

## 4. Current operational status

```text
NC_PARENT_THEORY = LOCKED
CASE21 = COMPLETE / FULL L-KZ PASS
SWARTZ24_Pu = 24/24 AVAILABLE
SWARTZ24_FULL_24_PANEL_L_KZ = OPEN / DEFERRED
STEEL_SHELL_EXTENSION = ACTIVE
ZHOU_Z0_Z6_REDUCED_BATCH = 7/7 CALCULATED
Z1_Z3_Z4_Z5_SAME_EXPRESSION_RQ_L = 4/4 PASS
Z0_Z2 = YIELD-CUSP EVENT CASES
Z6_A = COMPLETE PARTIAL-CAUSE AUDIT
Z6_B = COMPLETE MINOR-CAUSE AUDIT
Z6_C = EXECUTED; ARTIFICIAL CUSP CONFIRMED BUT CAPACITY EFFECT SMALL
CURRENT_NEXT_TASK = Z6_D1_SAME_OBJECT_COMPARATOR_AUDIT
FORMAL_SPATIAL_QUADRATURE = 0
STRUCTURAL_CALIBRATION = NO
```
