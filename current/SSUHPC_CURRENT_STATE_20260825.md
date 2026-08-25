# CURRENT STATE — Steel-Shell UHPC

**Updated:** 2026-08-25 14:35 +08:00  
**Status:** `RC_SSNC_MILESTONE_ANCHORED / CORE_NM_SUBSTITUTION_ONLY / THEORY_CLOSED / SEVEN_CASE_BLIND_EXECUTED / ABAQUS_POSTCHECK_COMPLETE / NO_REPAIR`

Canonical parent:

`current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`

Canonical SSUHPC theory:

`semantic_v2/20_theory/20260825_1330__NZSCCM__SSUHPC_FROM_RC_SSNC_MILESTONE_CORE_NM_SUBSTITUTION_V1.md`

Canonical closure/execution report:

`semantic_v2/40_execution/steel_shell/20260825_1435__NZSCCM__SSUHPC_MILESTONE_CORE_NM_CLOSURE_7CASE_BLIND_ABAQUS_POSTCHECK_R01.md`

---

## 0. Unique theory identity

```text
ANCHOR = RC–SSNC Unified Terminal-Capacity Milestone, 2026-08-25
PARENT = milestone SSNC
ONLY THEORY SUBSTITUTION = NC core longitudinal/transverse N-M -> UHPC core longitudinal/transverse N-M
```

The earlier 13:00 independent early-Hu reconstruction is not a current anchor. Historical UHPC dialogue is material-unit memory only.

---

## 1. Retained milestone structure and steel

```text
FULL_2D_MARGUERRE_AIRY = RETAIN
INITIAL_FULL_COMPOSITE_ABD = RETAIN
INTEGER_HALFWAVE_SELECTION = RETAIN
COMMON_TERMINAL_STRAIN/RESULTANT_ARCHITECTURE = RETAIN
R02_PBL_YUN_FACE = RETAIN
R04_IDEAL_EP_MISES_FACE_CAP = RETAIN
LONGITUDINAL_WEB = RETAIN
STEEL_FACE_OFFSET = INCLUDED_ONCE_ONLY
R03_AS_Pu_GATE = NO
CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH_PRODUCTION = NO
COMPARATOR_IN_ROOT_SELECTION = 0
```

---

## 2. UHPC material unit and exact N-M closure

```text
fc    = 141.1 MPa
Ec    = 43.4 GPa
epsc0 = 0.0035
nu_c  = 0.20
fct   = 4.513133983249735 MPa
epst0 = 0.001
mt    = 0.4418
```

Compression uses the recovered Hu-source curve

\[
\sigma_c=-f_c\frac{n_h\xi-\xi^2}{1+(n_h-2)\xi},
\qquad \xi=-\varepsilon/\varepsilon_{c0},\quad 0\le\xi\le1.
\]

Tension uses the recovered Hu-source tensile unit

\[
\sigma_t=f_{ct}e^{1/m_t}\xi_t
\exp[-\xi_t^{m_t}/m_t].
\]

Compression and tension both have exact stress/moment primitives. For affine directional strain

\[
\varepsilon_i(z)=A_i+B_i z,
\qquad i=x,y,
\]

UHPC longitudinal and transverse resultants are finite endpoint evaluations of the exact primitives. Thus

```text
UHPC_NM_X = CLOSED
UHPC_NM_Y = CLOSED
UHPC_THICKNESS_QUADRATURE = 0
CC_TC_TT_POINTWISE_STATE_MACHINE = 0
```

The terminal envelope is first UHPC compressed-face contact with \(-\varepsilon_{c0}\); post-peak compression does not extend Pu.

---

## 3. Closed terminal system

For each fixed finite station, solve the four normal resultant balances plus one finite active UHPC peak condition in

\[
(q,\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y).
\]

All seven current physical first-contact roots are controlled at

\[
\boxed{s=1}
\]

with

\[
\boxed{\varepsilon_y(-t_c/2)=-0.0035.}
\]

No earlier admissible interior contact was found.

---

## 4. Seven blind results

All roots below were fixed before Abaqus peak loads were opened.

| Case | blind Pu / MN | local steel sigma_cr / MPa | shell local buckling before fy? |
|---|---:|---:|---|
| T120 | **12.76914369** | 2206.635 | NO |
| T360 | **12.18255684** | 245.795 | **YES** |
| BH005 | **2.46233215** | 10044.967 | NO |
| BH010 | **4.58337285** | 2511.242 | NO |
| BH020 | **8.55797773** | 627.810 | NO |
| BH032 | **12.35286995** | 245.238 | **YES** |
| BH050 | **15.69757377** | 100.450 | **YES** |

---

## 5. Abaqus post-check

| Case | theory / MN | Abaqus R02 / MN | theory/Abaqus - 1 |
|---|---:|---:|---:|
| T120 | 12.76914369 | 12.6378 | +1.0393% |
| T360 | 12.18255684 | 10.9688 | +11.0655% |
| BH005 | 2.46233215 | 2.3558 | +4.5221% |
| BH010 | 4.58337285 | 4.3043 | +6.4836% |
| BH020 | 8.55797773 | 8.0076 | +6.8732% |
| BH032 | 12.35286995 | 10.9905 | +12.3959% |
| BH050* | 15.69757377 | 12.2198 | +28.4602% |

BH050 comparator remains lower-confidence/different model family and is excluded from the primary statistics.

Primary six:

\[
\boxed{\text{mean signed}=+7.0633\%,\quad MAE=7.0633\%,\quad RMSE=8.0303\%.}
\]

No post-comparison retuning was performed.

---

## 6. T360 full-worked-case identity

T360 is the canonical worked shell-buckling example for this state:

```text
b = 1600 mm
a_phys = 3000 mm
tc = 42 mm
ts = 4 mm
m* = 2
ell = 1500 mm
Pcr = 30.7519466757 MN
local Bs = 360 mm
local sigma_cr = 245.7948984 MPa < fy = 355 MPa
qu = 0.00162329439722115
Pu = 12.18255684307 MN
Abaqus R02 = 10.9688 MN
post-check error = +11.0655%
```

At terminal:

```text
R02 U_top    = 0.775204046541 mm
R02 U_bottom = 2.866479922145 mm
bottom trial Mises = 549.20835057 MPa
R04 lambda_bottom = 0.646384927748
final bottom Mises = 355 MPa
```

All four normal resultants close against the unchanged Airy demand to approximately 1e-10 or better at retained precision. Full arithmetic is in the canonical closure report.

---

## 7. Current diagnosis — recorded, not repaired

The comparison pattern is now clear enough to record:

```text
T120 (no shell local buckling): +1.04%
T360 (shell local buckling):   +11.07%
BH032 (shell local buckling):  +12.40%
BH050* (very slender shell):   +28.46%, lower-confidence comparator
```

Therefore the milestone-derived SSUHPC theory is algebraically and mechanically closed, but the remaining positive bias is strongly associated with shell-local/boundary resultant capacity after local buckling.

This run does NOT authorize:

```text
UHPC CC/TC/TT repair chain
Zhang/Liu/FHWA replacement
fc retuning
effective-width/effective-area repair
FEM/test calibration
R03 reopening
```

If further research is authorized, the next question is whether current R02/R04 full-area steel-face resultants sufficiently degrade the complete face N-M capacity under severe local buckling/boundary localisation.
