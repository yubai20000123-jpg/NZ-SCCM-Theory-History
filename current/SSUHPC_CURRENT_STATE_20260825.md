# CURRENT STATE — Steel-Shell UHPC

**Updated:** 2026-08-25 15:15 +08:00  
**Status:** `RC_SSNC_MILESTONE_ANCHORED / CORE_NM_SUBSTITUTION_ONLY / THEORY_CLOSED / SEVEN_CASE_BLIND_EXECUTED / ABAQUS_POSTCHECK_COMPLETE / R02_R04_ROOT_CAUSE_IDENTIFIED / NO_PRODUCTION_REPAIR_YET`

Canonical parent:

`current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`

Canonical SSUHPC theory:

`semantic_v2/20_theory/20260825_1330__NZSCCM__SSUHPC_FROM_RC_SSNC_MILESTONE_CORE_NM_SUBSTITUTION_V1.md`

Canonical closure/execution report:

`semantic_v2/40_execution/steel_shell/20260825_1435__NZSCCM__SSUHPC_MILESTONE_CORE_NM_CLOSURE_7CASE_BLIND_ABAQUS_POSTCHECK_R01.md`

Canonical steel-face overprediction diagnosis:

`semantic_v2/40_execution/steel_shell/20260825_1515__NZSCCM__R02_R04_LOCAL_YIELD_RESULTANT_OVERPREDICTION_DIAGNOSIS_R01.md`

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
R04_IDEAL_EP_MISES_FACE_CAP = RETAIN AS CURRENT PRODUCTION UNTIL R06 PASSES
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

## 4. Seven blind results — current production values remain frozen pending R06

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
final bottom mean Mises = 355 MPa
```

All four normal resultants close against the unchanged Airy demand to approximately 1e-10 or better at retained precision. Full arithmetic is in the canonical closure report.

---

## 7. New source-level diagnosis: the current plastic cap is applied after local-field homogenization

Yun's source uses the postbuckling mean-stress path only as the **average resultant path**. Ultimate is obtained by reconstructing the nonuniform local membrane stress field and finding the first amplitude at which the maximum local axial stress reaches `fy`; the corresponding average stress is the resultant capacity.

Current R02 already contains both:

```text
mean_compression_stress = full-area mean postbuckling stress
airy_fluctuation_tension = finite-harmonic local stress redistribution
local_mises = local diagnostic
```

But current production R04 is applied only to the R02 **mean** trial stress. Therefore it checks

\[
\sigma_{VM}(\bar\sigma)=f_y
\]

instead of retaining the local postbuckling stress concentration in the capacity check.

Direct T360 audit at the fixed current root:

```text
upper mean VM = 347.61 MPa < 355, so current R04 does not cap it
upper R02 local membrane max VM ≈ 374.58 MPa > 355

lower R02 mean trial = (-87.59,-587.74) MPa
lower current R04 mean cap = (-56.62,-379.91) MPa, mean VM = 355
lower R02 local membrane max VM before mean cap ≈ 919.89 MPa
lower max local axial compression ≈ 865 MPa
```

Thus first local steel yielding occurs substantially earlier than the current mean-Mises terminal.

A diagnostic proportional-strain continuation gives first-local-yield scales approximately:

```text
upper: eta ≈ 0.951635, U ≈ 0.733832 mm, mean stress ≈ (+79.59,-284.06) MPa
lower: eta ≈ 0.419237, U ≈ 1.59139 mm, mean stress ≈ (-67.80,-276.15) MPa
```

The independent Yun scalar cell check gives an ultimate average axial stress near `297.87 MPa` for the T360 360x375x4 mm local panel, versus the current lower-face retained axial mean magnitude `379.91 MPa`.

Therefore:

\[
\boxed{
PRIMARY\_OVERPREDICTION\_CAUSE
= \text{mean-stress plastic cap applied after R02 local-field homogenization}.
}
\]

The problem is not absence of local buckling in R02; it is loss of the local buckling stress concentration before the terminal strength cap.

---

## 8. Why this diagnosis matches the seven-case pattern

Diagnostic correlations only; not a calibration law:

\[
\mathrm{corr}(b/t,error)\approx0.897
\]

for all seven and about `0.840` for the primary six.

More directly,

\[
\mathrm{corr}(1/\sigma_{cr},error)\approx0.976
\]

for all seven and about `0.893` for the primary six.

This supports a steel-shell local-resultant issue rather than reopening UHPC material physics.

---

## 9. R06 concept — source-consistent local-yield resultant gate, not yet production

Retain R02 completely. Do not use effective width.

With

\[
u=\cos(k_xx),\qquad v=\cos(k_yy),
\]

the R02 finite harmonic field makes the normal stresses finite polynomials in `(u,v)` and gives

\[
\tau=\sqrt{1-u^2}\sqrt{1-v^2}P_\tau(u,v).
\]

Hence

\[
\Phi(u,v)=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau^2
\]

is a finite polynomial over `[-1,1]^2`.

The exact local-yield maximum can therefore be obtained from a finite algebraic candidate set:

```text
interior: dPhi/du = dPhi/dv = 0
edges: one-variable stationary roots
corners: four finite values
```

so the future formal gate can retain

```text
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH = 0
```

Candidate architecture:

```text
R02 amplitude + finite local harmonic field
-> exact max local Mises admissibility
-> full-area mean face resultant at the local-yield boundary
-> source-justified plastic reserve only where needed
```

Yun indicates plastic reserve mainly matters for stockier `b/t < 70`; the problematic T360/BH032/BH050 are `b/t = 90/80/125`. Therefore the first-local-yield resultant is a particularly relevant source-supported candidate for these slender cases, but it must not be blindly imposed on stocky T120/BH005/BH010/BH020.

---

## 10. Next gate

```text
NEXT = R06 FINITE-ALGEBRAIC LOCAL-YIELD RESULTANT GATE
STEP 1 = implement exact finite extrema of Phi(u,v), no spatial grid
STEP 2 = x-y symmetry and zero-buckling degeneration checks
STEP 3 = blind T360 + BH032 rerun
STEP 4 = stocky-case non-regression
STEP 5 = only after roots fixed reopen Abaqus
```

Until R06 passes:

```text
CURRENT_SEVEN_CASE_Pu = FROZEN AS R01 RESULTS
R04 = CURRENT PRODUCTION CAP
R06 = DIAGNOSTIC/CANDIDATE ONLY
NO EFFECTIVE WIDTH
NO UHPC RETUNING
NO COMPARATOR-BASED CORRECTION
```
