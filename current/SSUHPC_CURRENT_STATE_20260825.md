# CURRENT STATE — Steel-Shell UHPC

**Updated:** 2026-08-25 14:50 +08:00  
**Status:** `RC_SSNC_MILESTONE_ANCHORED / CORE_NM_SUBSTITUTION_ONLY / THEORY_CLOSED / SEVEN_CASE_BLIND_EXECUTED / ABAQUS_POSTCHECK_COMPLETE / COMMON_STEEL_SHELL_SCOPE_CORRECTED / NO_PRODUCTION_REPAIR`

Canonical parent:

`current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`

Canonical SSUHPC theory:

`semantic_v2/20_theory/20260825_1330__NZSCCM__SSUHPC_FROM_RC_SSNC_MILESTONE_CORE_NM_SUBSTITUTION_V1.md`

Canonical SSUHPC closure/execution report:

`semantic_v2/40_execution/steel_shell/20260825_1435__NZSCCM__SSUHPC_MILESTONE_CORE_NM_CLOSURE_7CASE_BLIND_ABAQUS_POSTCHECK_R01.md`

Earlier T360-centered diagnosis retained as evidence:

`semantic_v2/40_execution/steel_shell/20260825_1515__NZSCCM__R02_R04_LOCAL_YIELD_RESULTANT_OVERPREDICTION_DIAGNOSIS_R01.md`

Canonical **common steel-shell scope correction**:

`semantic_v2/40_execution/steel_shell/20260825_1450__NZSCCM__STEEL_SHELL_COMMON_R02_R04_LOCAL_YIELD_AUDIT_Z6_T360_R01.md`

Current common steel-shell state:

`current/STEEL_SHELL_COMMON_R02_R04_STATE_20260825.md`

---

## 0. Unique SSUHPC theory identity

```text
ANCHOR = RC–SSNC Unified Terminal-Capacity Milestone, 2026-08-25
PARENT = milestone SSNC
ONLY THEORY SUBSTITUTION = NC core longitudinal/transverse N-M -> UHPC core longitudinal/transverse N-M
```

Historical UHPC dialogue is used only to recover the UHPC material unit and its analytic N-M primitives. It does not replace the milestone steel-shell architecture.

---

## 1. Scope correction after the Z6–T360 common audit

The earlier T360 diagnosis correctly identified that the current R02 finite local postbuckling field can be homogenized before the R04 mean-stress Mises cap. Its **mechanical diagnosis remains valid**, but its former SSUHPC-only scope is superseded.

R02 and R04 are common SSNC/SSUHPC steel-shell operators. Therefore:

```text
SSUHPC_ONLY_R06 = REJECTED / SUPERSEDED
R02_R04_ISSUE = STEEL-SHELL COMMON ISSUE
ACTIVATION_VARIABLE = LOCAL STEEL-SHELL STATE
ACTIVATION_VARIABLE != CORE MATERIAL LABEL
```

The direct Z6–T360 audit shows two regimes.

### Z6 R05 — stocky/yield-first local steel

```text
local cell = 200 x 200 x 4 mm
sigma_cr = 794.3887 MPa > fy = 355 MPa
A0 = 0.125 mm
U = 0.1270986807 mm
U/A0 = 1.01678945
mean trial VM = 507.41735 MPa
max R02 local membrane VM ≈ 507.50506 MPa
local/mean VM amplification = 1.00017284
eta_local_VM = 0.69950131
eta_mean_VM = 0.69962132
Yun axial-yield eta ≈ 1.18491 > 1
```

Thus the local-vs-mean yield separation is negligible at the current Z6 endpoint. The current Z6 R05 result is not reopened.

### T360 — local-buckling-first local steel

```text
local cell = 360 x 375 x 4 mm
sigma_cr = 245.7949 MPa < fy = 355 MPa
A0 = 0.225 mm
U_top/A0 = 3.44535
U_bottom/A0 = 12.73991
```

Upper face:

```text
mean VM = 347.6065 MPa < fy
max local membrane VM ≈ 374.5803 MPa > fy
```

Lower face:

```text
mean trial VM = 549.2084 MPa
current R04 lambda = 0.64638493
current capped mean VM = 355 MPa
max local membrane VM before mean cap ≈ 919.8894 MPa
hypothetical same-lambda local VM ≈ 594.603 MPa > fy
Yun local axial-yield eta ≈ 0.41317
local-Mises yield eta ≈ 0.41924
mean-Mises yield eta ≈ 0.62378
```

Thus the interface issue is strongly activated in T360.

The governing interpretation is now:

```text
STOCKY / YIELD-FIRST:
    sigma_cr > fy
    U/A0 near 1
    local redistribution weak
    local and mean yielding nearly coincide
    example = Z6

LOCAL-BUCKLING-FIRST:
    sigma_cr < fy
    U/A0 grows strongly
    local redistribution strong
    local yield can precede mean-Mises cap materially
    example = T360
```

---

## 2. Retained milestone architecture

```text
FULL_2D_MARGUERRE_AIRY = RETAIN
INITIAL_FULL_COMPOSITE_ABD = RETAIN
INTEGER_HALFWAVE_SELECTION = RETAIN
COMMON_TERMINAL_STRAIN/RESULTANT_ARCHITECTURE = RETAIN
R02_PBL_YUN_FACE = RETAIN
R04_IDEAL_EP_MISES_FACE_CAP = RETAIN AS CURRENT PRODUCTION UNTIL COMMON GATE PASSES
LONGITUDINAL_WEB = RETAIN
STEEL_FACE_OFFSET = INCLUDED ONCE ONLY
R03_AS_Pu_GATE = NO
CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH_PRODUCTION = NO
COMPARATOR_IN_ROOT_SELECTION = 0
```

---

## 3. UHPC core N-M closure remains unchanged

```text
fc    = 141.1 MPa
Ec    = 43.4 GPa
epsc0 = 0.0035
nu_c  = 0.20
fct   = 4.513133983249735 MPa
epst0 = 0.001
mt    = 0.4418
```

For affine directional strain

\[
\varepsilon_i(z)=A_i+B_i z,\qquad i=x,y,
\]

UHPC longitudinal and transverse resultants remain exact endpoint evaluations of the already-closed stress primitives.

```text
UHPC_NM_X = CLOSED
UHPC_NM_Y = CLOSED
UHPC_THICKNESS_QUADRATURE = 0
CC_TC_TT_POINTWISE_STATE_MACHINE = 0
```

No UHPC material repair is authorized by the common steel-shell audit.

---

## 4. Current SSUHPC blind results remain frozen

| Case | blind Pu / MN | local steel sigma_cr / MPa | shell local buckling before fy? |
|---|---:|---:|---|
| T120 | **12.76914369** | 2206.635 | NO |
| T360 | **12.18255684** | 245.795 | **YES** |
| BH005 | **2.46233215** | 10044.967 | NO |
| BH010 | **4.58337285** | 2511.242 | NO |
| BH020 | **8.55797773** | 627.810 | NO |
| BH032 | **12.35286995** | 245.238 | **YES** |
| BH050 | **15.69757377** | 100.450 | **YES** |

Abaqus values were opened only after these roots were fixed. No post-comparison retuning was performed.

---

## 5. Current production boundary

Until a **common steel-shell** refinement passes its gates:

```text
Z6_R05_Pu = 49.45439833719624 MN [FROZEN]
SSUHPC_R01_7CASE = FROZEN
R02 = CURRENT PRODUCTION
R04 = CURRENT PRODUCTION
NO EFFECTIVE WIDTH / EFFECTIVE AREA
NO UHPC fc RETUNING
NO R03 REOPENING
NO COMPARATOR-BASED ROOT CHANGE
```

If the next step is authorized, it is:

```text
NEXT = STEEL_SHELL_COMMON_R06
```

not `SSUHPC_R06`.

Required gates:

1. identical common implementation for SSNC and SSUHPC;
2. retain R02 amplitude and finite local harmonic field;
3. formal spatial sampling/quadrature/material points remain zero;
4. no effective-width construction;
5. exact degeneration to current R04 when local redistribution is absent/negligible;
6. blind Z6 non-regression;
7. blind T360 and BH032 local-buckling reruns;
8. only after roots are fixed may Zhou/Winter/Abaqus comparators be reopened.
