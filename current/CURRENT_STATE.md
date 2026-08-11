# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-11 22:55 +08:00  
**Purpose:** 唯一当前工作入口；保持主线简单。

## 0. Highest-priority contract

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

No spatial Gauss/Simpson/adaptive quadrature, material-point grid, moving TT/TC/CC cells, whole-structure P/R fitting, structural-load material calibration, or finite-difference production derivatives.

---

## 1. Material theory — closed R10 formula

The governing material chain is

```text
source Foster current relation
-> R10 one-dimensional energy-smoothed scalar
-> SAME U/C/T + CC/TC/TT multidimensional current map
```

Define

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad x_{cr}=\frac{\rho}{\kappa},
\]

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr,
\]

\[
\boxed{h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right)}.
\]

Rise branch:

\[
\boxed{u_1(\tau)=\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5}.
\]

Fall branch:

\[
\boxed{u_2(s)=h+(u_r-h)(10s^3-15s^4+6s^5)}.
\]

The multidimensional relation remains

\[
U_i=\kappa\lambda_i-C_i+\kappa c_i+\rho T_i-\kappa t_i,
\]

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8,
\]

\[
s_-=U_- -a_{cc}C_-^2C_+ + C_-T_+ -\rho a_tT_-T_+^8.
\]

No new material route is active.

---

## 2. N48 analytic compiler

\[
\boxed{N_M=48}.
\]

For \(F\in\{U,C,T,T^7\}\),

\[
\boxed{F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi)},
\]

\[
\theta_j=\frac{(j+\tfrac12)\pi}{49},\qquad \lambda_j=\lambda_c+\lambda_h\cos\theta_j,
\]

\[
\boxed{a_n^{(F)}=\frac{2-\delta_{n0}}{49}\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),\qquad n=0,\ldots,48.}
\]

No long decimal coefficient table is part of the theory.

---

## 3. Paper-style derivation, Case21 closure and canonical workflow

Canonical derivation:

- `current/theory/NZ_SCCM_R10_N48_D15_PAPER_STYLE_DERIVATION_20260811.md`

Case21 fresh closure:

- `current/theory/NZ_SCCM_CASE21_FRESH_R10_N48_D15_CLOSURE_20260811.md`
- `current/theory/NZ_SCCM_CASE21_FRESH_R10_N48_D15_CLOSURE_results.json`
- `governance/CASE21_FRESH_R10_N48_D15_CLOSURE_DECISION_20260811.md`

Canonical workflow:

- `current/workflows/NZ_SCCM_CASE21_CALCULATION_PROCESS_TEMPLATE_V1_20260811.md`

Execution chain:

```text
INPUT
-> R10
-> continuous spectral certificate
-> N48 regenerate
-> Nguyen continuous kinematics
-> Cayley-Hamilton current-map
-> D15 exact moments
-> steel branch check
-> Rq=0 equilibrium branch
-> L=0 limit state
-> final self-check
-> experiment-only comparison
```

Case21 is a process exemplar only; its numerical result is not a target for other panels.

---

## 4. Swartz 24-panel fresh blind calculation — COMPLETE

Canonical files:

- `current/results/NZ_SCCM_SWARTZ24_FRESH_BLIND_THEORY_RESULTS_20260811.csv`
- `current/results/NZ_SCCM_SWARTZ24_FRESH_THEORY_VS_EXPERIMENT_20260811.csv`
- `current/results/NZ_SCCM_SWARTZ24_FRESH_R10_N48_D15_REPORT_20260811.md`

The blind theory table was committed before the experiment-comparison table. The solve did not use historical Case roots, historical Case loads, historical load paths, historical FE results, or experiment loads.

```text
SWARTZ24_FRESH_THEORY_PREDICTIONS = 24/24 PASS
BLIND_THEORY_FREEZE_BEFORE_EXPERIMENT = PASS
EXPERIMENTAL_COMPARISON = COMPLETE
STRUCTURAL_CALIBRATION = NO
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
MATERIAL_COMPILER_ORDER = 48
COMPILER_DOMAIN_CERTIFICATE = 24/24 PASS
STEEL_BRANCH_CHECK = 24/24 ELASTIC
SAME_EXPRESSION_LIMIT_CONDITION = 24/24 PASS
```

Full-sample statistics after blind prediction freeze:

- mean theory/experiment = 0.9638;
- mean signed error = -3.62%;
- MAPE = 12.06%;
- RMSE = 79.26 kN.

| Group | Approx. b/t | Mean error | MAPE | RMSE |
|---|---:|---:|---:|---:|
| Case 1–8 | ~48 | +4.43% | 12.66% | 73.60 kN |
| Case 9–16 | ~38.3 | -13.23% | 15.45% | 108.29 kN |
| Case 17–24 | ~63.1 | -2.07% | 8.06% | 41.25 kN |

---

## 5. Primary-source Swartz24 mechanism audit — COMPLETE

Canonical files:

- `current/results/NZ_SCCM_SWARTZ24_PRIMARY_MECHANISM_AUDIT_TABLE_20260811.csv`
- `current/results/NZ_SCCM_SWARTZ24_PRIMARY_MECHANISM_AUDIT_20260811.md`

The original Swartz Table 1 and Table 2 were digitized panel-by-panel and merged with the already frozen fresh blind Pu values. Added diagnostic fields include actual b/t, Pcr, Pf, Pf/Pcr, fcr/fcyl, reinforcement ratio, layer count, buckling location and Pcr measurement method.

Current diagnostic ranking:

```text
STRONGEST_TESTED_DIAGNOSTIC = fcr/fcyl
Spearman(error, fcr/fcyl) = -0.753
Spearman(error, fcr/fcyl; excluding Southwell Cases 1 and 4) = -0.819
Spearman(error, Pf/Pcr) = -0.548
Spearman(abs_error, b/t) = -0.462
FULL_SAMPLE_STEEL_RATIO_EFFECT = WEAK
LAYER_COUNT_EFFECT = WEAK_AND_CONFOUNDED
BUCKLING_LOCATION_LABEL_EFFECT = WEAK
```

Interpretation boundary:

- `fcr/fcyl` is the strongest tested diagnostic: panels buckling closer to the concrete material peak tend to be underpredicted more severely by the current Pu model.
- `Pf/Pcr` supports a post-buckling-reserve hypothesis, but shares Pf with the error definition and therefore is not independent causal proof.
- Pcr method is not uniform: Cases1/4 use Southwell, Cases5/6 deflection profiles, most others surface-strain criterion.
- Reinforcement has weak full-sample correlation with error, but this does not negate its ultimate/post-buckling role; within Case17–24 the signed error changes strongly with steel ratio.

No calibration is authorized from these correlations.

---

## 6. Supplemental source review — COMPLETE

Canonical file:

- `evidence/literature/NZ_SCCM_SWARTZ_ATTARD_OTHER3_SOURCE_REVIEW_20260811.md`

Source identities and retained uses:

1. **Swartz/Rosebraugh/Rogacki, A Method...** — primary experimental-method supplement: finite-stiffness frame/support details, load redistribution after buckling, one/two bulge patterns, Southwell limitations, preferred strain-based Pcr criterion.
2. **Attard 1994** — primary analytical tangent-stability supplement: orthotropic tangent plate equation, loaded-direction tangent modulus, transverse-stiffness approximation, closed buckling/slenderness expressions, and moment amplification from imperfections. Use only as an independent stability benchmark/diagnostic; do not import `Eyt=0.4Ec` into current R10.
3. **Doh/Fragomeni/Kim review** — secondary literature map: one-way/two-way scope, eccentricity/support/load-control distinctions, Saheb-Desayi ultimate-strength trends, and validation-data limitations. Use as future validation-matrix guide, not a primary formula source.

New evidence-based diagnostic priorities:

```text
P1 = tangent-state / fcr-fc regime audit
P2 = post-buckling membrane redistribution audit
P3 = support-stiffness / observed-mode sensitivity audit
P4 = reinforcement-postbuckling interaction audit
P5 = external validation matrix segmented by eccentricity/boundary/load-control
```

These are diagnostics only. R10, N48, q0 and the current zero-spatial architecture remain frozen.

---

## 7. Independent reproducibility audit package — READY

Three representative panels were selected across the three source groups:

```text
Case 1  -> b/t ~ 48 group
Case 14 -> b/t ~ 38 group
Case 21 -> b/t ~ 63 group
```

Canonical audit files:

- `current/audits/NZ_SCCM_CASE1_CASE14_CASE21_FULL_REPRODUCTION_AUDIT_PACKAGE_20260811.md`
- `current/audits/NZ_SCCM_CASE1_CASE14_CASE21_BLIND_INPUT_20260811.md`
- `current/audits/NZ_SCCM_CASE1_CASE14_CASE21_BLANK_CHAT_PROMPT_20260811.txt`

The blind input intentionally contains no final D, q, Pu or experiment loads. An independent chat must regenerate R10, N48, Cayley-Hamilton, D15, steel contributions and solve Rq=L=0 before any answer comparison.

---

## 8. Status

```text
R10_CLOSED_PARAMETER_FORMULA = GOVERNING
MATERIAL_COMPILER_ORDER = 48
N112_REQUIREMENT = SUPERSEDED
LONG_DECIMAL_COEFFICIENT_TABLE_IN_THEORY = PROHIBITED
R10_N48_D15_PAPER_STYLE_DERIVATION = COMPLETE
CASE21_FRESH_R10_N48_D15_CLOSURE = PASS
CASE21_CALCULATION_PROCESS_TEMPLATE = COMPLETE
SWARTZ24_FRESH_BLIND_THEORY = 24/24 PASS
SWARTZ24_EXPERIMENT_COMPARISON = COMPLETE
SWARTZ24_PRIMARY_TABLE1_TABLE2_DIGITIZATION = COMPLETE
SWARTZ24_PRIMARY_MECHANISM_AUDIT = COMPLETE
SUPPLEMENTAL_OTHER3_SOURCE_REVIEW = COMPLETE
HISTORICAL_CASE_COMPUTED_RESULTS_USED_IN_SWARTZ24_SOLVE = NO
THREE_PANEL_INDEPENDENT_REPRO_PACKAGE = READY
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_Pu_CALIBRATION = NO
CURRENT_NEXT_TASK = USER_DIRECTED_MECHANISM_DIAGNOSTIC_OR_INDEPENDENT_BLIND_REPRODUCTION_AUDIT
```
