# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-11 23:27 +08:00  
**Purpose:** 唯一当前工作入口；保持主线简单。

## 0. Highest-priority contract

```text
DOMAIN = ONE_CONTINUOUS COMPLETE HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

Formal production continues to prohibit spatial Gauss/Simpson/adaptive quadrature, spatial Chebyshev collocation, material-point grids/cells, whole-structure P/R fitting and experiment-driven material tuning.

---

## 1. Governing material target — R10 unchanged

```text
source Foster current relation
-> R10 1D energy-smoothed tensile scalar
-> SAME U/C/T + CC/TC/TT multidimensional current map
```

Core parameters:

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad
x_{cr}=\frac{\rho}{\kappa},\qquad
\rho=0.1.
\]

R10 peak parameter:

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)dr,
\]

\[
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right).
\]

No P1 result authorizes any change to R10.

---

## 2. Current finite analytic material representation — N48

\[
N_M=48.
\]

For \(F\in\{U,C,T,T^7\}\),

\[
F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi),
\]

\[
\theta_j=\frac{(j+\tfrac12)\pi}{49},\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j,
\]

\[
a_n^{(F)}=\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j).
\]

N48 remains the frozen representation used in the completed fresh calculations. However, P1 has now separated **value representation identity** from **first-derivative/tangent fidelity**; see Section 6.

---

## 3. Closed Case21 workflow

Canonical files:

- `current/theory/NZ_SCCM_R10_N48_D15_PAPER_STYLE_DERIVATION_20260811.md`
- `current/theory/NZ_SCCM_CASE21_FRESH_R10_N48_D15_CLOSURE_20260811.md`
- `current/workflows/NZ_SCCM_CASE21_CALCULATION_PROCESS_TEMPLATE_V1_20260811.md`

Workflow:

```text
INPUT
-> R10
-> spectral certificate
-> N48 regenerate
-> Nguyen continuous kinematics
-> Cayley-Hamilton current-map
-> D15 exact moments
-> steel contribution
-> Rq=0
-> L=0
-> final self-check
-> experiment-only comparison
```

Case21 remains a process exemplar only; its numerical answer is not a target for another panel.

---

## 4. Swartz24 fresh blind value calculation — COMPLETE

Canonical files:

- `current/results/NZ_SCCM_SWARTZ24_FRESH_BLIND_THEORY_RESULTS_20260811.csv`
- `current/results/NZ_SCCM_SWARTZ24_FRESH_THEORY_VS_EXPERIMENT_20260811.csv`
- `current/results/NZ_SCCM_SWARTZ24_FRESH_R10_N48_D15_REPORT_20260811.md`

Blind theory was frozen before experiment comparison.

```text
SWARTZ24_FRESH_THEORY_PREDICTIONS = 24/24 COMPLETE
HISTORICAL_CASE_ROOTS_OR_LOADS_USED = NO
EXPERIMENT_USED_IN_SOLVE = NO
COMPILER_DOMAIN_CERTIFICATE = 24/24 PASS
STEEL_BRANCH_CHECK = 24/24 ELASTIC
FORMAL_SPATIAL_QUADRATURE = 0
```

Post-freeze statistics:

- mean theory/experiment = 0.9638;
- mean signed error = -3.62%;
- MAPE = 12.06%;
- RMSE = 79.26 kN.

| Group | Approx. b/t | Mean error | MAPE |
|---|---:|---:|---:|
| Case 1–8 | ~48 | +4.43% | 12.66% |
| Case 9–16 | ~38.3 | -13.23% | 15.45% |
| Case 17–24 | ~63.1 | -2.07% | 8.06% |

These values remain preserved as the completed blind **value-closure record**. P1 does not recalibrate them.

---

## 5. Primary Swartz mechanism audit — COMPLETE

Canonical files:

- `current/results/NZ_SCCM_SWARTZ24_PRIMARY_MECHANISM_AUDIT_TABLE_20260811.csv`
- `current/results/NZ_SCCM_SWARTZ24_PRIMARY_MECHANISM_AUDIT_20260811.md`
- `evidence/literature/NZ_SCCM_SWARTZ_ATTARD_OTHER3_SOURCE_REVIEW_20260811.md`

Strongest prior experimental diagnostic:

```text
Spearman(error, fcr/fcyl) = -0.753
Spearman(error, fcr/fcyl; excluding Southwell Case1/4) = -0.819
Spearman(error, Pf/Pcr) = -0.548
```

This established that panels buckling closer to the material peak tend to be more underpredicted, but did not yet identify which theoretical layer caused the discrepancy.

---

## 6. P1 current-tangent audit — COMPLETE; tangent fidelity warning frozen

Canonical files:

- `current/results/NZ_SCCM_SWARTZ24_P1_CURRENT_TANGENT_AUDIT_20260811.md`
- `current/results/NZ_SCCM_SWARTZ24_P1_CURRENT_TANGENT_AUDIT_COMPACT_20260811.csv`
- `evidence/literature/NZ_SCCM_ZHOU_ATTARD_TANGENT_STABILITY_INTERPRETATION_20260811.md`

### 6.1 Audit identity

The 24 frozen ultimate states \((D_u,q_u,P_u)\) were held fixed. No material, root, Pu, q0 or experimental quantity was tuned.

At the complete-halfwave center,

\[
X=Y=\pi/2,\qquad \zeta=0,
\]

so

\[
\lambda_+=0,\qquad \lambda_-=-D_u.
\]

This gives a clean material-state location for comparing the exact R10 target tangent, the N48 derivative, Attard orthotropic tangent ideas and a Zhou-form \(D_x-D_y-H\) stiffness decomposition.

### 6.2 Hard material-anchor finding

The closed R10 target has the exact zero-state anchors

\[
C(0)=T(0)=T^7(0)=0,
\]

\[
C'(0)=T'(0)=(T^7)'(0)=0.
\]

The current N48 representation does not preserve these first-derivative identities. Across the 24 panel-specific compiler intervals:

```text
T48(0) range       = -0.001473 ... +0.059057
T48'(0) range      = +8.689 ... +11.364      (R10 target = 0)
normal-tangent asymmetry inflation vs R10 target = 23.1 ... 31.1 times
```

### 6.3 Loaded-direction tangent regime

Group means at the center state:

| Group | mean Du | R10 target E_parallel,t/E0 | N48 E_parallel,t/E0 |
|---|---:|---:|---:|
| Case 1–8 | 1.042 | -0.0195 | 0.9928 |
| Case 9–16 | 1.083 | -0.0360 | 0.9362 |
| Case 17–24 | 0.902 | +0.0599 | 0.9659 |

The R10 target therefore preserves the expected near-peak tangent collapse and distinguishes the three material regimes. N48 first derivatives largely erase that distinction and return the loaded tangent to approximately elastic magnitude.

### 6.4 Zhou-form stiffness decomposition

Zhou Siming's source theory emphasizes that simply-supported orthotropic axial stability is jointly contributed by directional bending stiffnesses and torsional/Poisson coupling, not by one loaded-direction modulus alone.

P1 uses that source concept only as an audit mapping:

\[
D_x^{eq}=C_{xx,t}t^3/12,
\qquad
D_y^{eq}=C_{yy,t}t^3/12,
\]

\[
D_\mu^{eq}=\frac{C_{xy,t}+C_{yx,t}}{2}\frac{t^3}{12},
\qquad
D_{66}^{eq}=G_tt^3/12,
\]

\[
H^{eq}=D_\mu^{eq}+2D_{66}^{eq}.
\]

Results:

```text
N48/R10 equivalent H inflation = 4.72 ... 6.79 times; mean 6.21
N48/R10 center stability-margin inflation = 3.28 ... 4.42 times; mean 3.97
```

Approximate contribution structure:

```text
R10 target: Dx ~47–50%, 2H ~46–51%, Dy ~-2%...+3%, steel small
N48 tangent: Dx ~12–13%, 2H ~75%, Dy ~11%, steel small
```

Thus the first-derivative representation issue changes the full directional stiffness composition, especially the H contribution.

### 6.5 Attard diagnostic

Attard is retained only as an orthotropic tangent benchmark. His transverse approximation \(E_{trans}\approx0.4E_c\) is NOT imported into R10.

Under the R10 target tangent, Case3–16 have non-positive loaded-direction center tangent at the frozen Pu state, so a positive-tangent Attard perturbation formula is already beyond its direct applicability there. Case17–24 remain positive but have Attard margins below unity at Pu, consistent with a perfect branch that has already bifurcated before a finite-amplitude ultimate state.

N48, in contrast, makes the loaded tangent positive and near elastic for all panels, materially changing this diagnostic identity.

### 6.6 P1 decision

```text
R10_MATERIAL_TARGET = NOT_CHANGED
SWARTZ24_PU_VALUES = NOT_RECALIBRATED
P1_CURRENT_TANGENT_AUDIT = COMPLETE
N48_VALUE_REPRESENTATION = PRESERVED_AS_HISTORICAL_CURRENT_VALUE_CLOSURE
N48_TANGENT_FIDELITY_AT_LAMBDA_ZERO = FAIL_DIAGNOSTIC
FIRST_CLEAR_MECHANICAL_DEVIATION = R10_TARGET -> N48_FIRST_DERIVATIVE
ATTARD_COMPARISON = DIAGNOSTIC_ONLY
ZHOU_Dx_Dy_H_DECOMPOSITION = DIAGNOSTIC_MAPPING_ONLY
CURRENT_LIMIT_TANGENT_INTERPRETATION = PENDING_TANGENT_REPRESENTATION_REVIEW
```

This FAIL does **not** authorize a new material model or an automatic order escalation. It means the project must not attribute the Swartz24 pattern to missing concrete physics or missing post-buckling structural freedom before the existing R10-to-N48 first-derivative fidelity is resolved.

---

## 7. Independent three-panel reproduction package

Canonical files:

- `current/audits/NZ_SCCM_CASE1_CASE14_CASE21_FULL_REPRODUCTION_AUDIT_PACKAGE_20260811.md`
- `current/audits/NZ_SCCM_CASE1_CASE14_CASE21_BLIND_INPUT_20260811.md`
- `current/audits/NZ_SCCM_CASE1_CASE14_CASE21_BLANK_CHAT_PROMPT_20260811.txt`

These remain available for an independent blank-chat reproduction test.

---

## 8. Current status and next gate

```text
R10_CLOSED_PARAMETER_FORMULA = GOVERNING_AND_UNCHANGED
MATERIAL_COMPILER_ORDER = 48
CASE21_VALUE_CLOSURE = COMPLETE_RECORD
SWARTZ24_FRESH_BLIND_VALUE_CLOSURE = 24/24 COMPLETE_RECORD
SWARTZ24_PRIMARY_MECHANISM_AUDIT = COMPLETE
P1_CURRENT_TANGENT_AUDIT = COMPLETE
N48_TANGENT_FIDELITY = FAIL_DIAGNOSTIC
STRUCTURAL_Pu_CALIBRATION = NO
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
CURRENT_NEXT_TASK = REVIEW_N48_TANGENT_REPRESENTATION_WITHOUT_CHANGING_R10
```

The next gate is therefore narrow: preserve R10 and the zero-spatial architecture, and determine the simplest analytic representation that preserves both the R10 material values and the required first-derivative/tangent anchors. No new material route is authorized.
