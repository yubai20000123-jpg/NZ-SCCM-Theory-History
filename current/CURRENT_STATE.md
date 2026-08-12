# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-13 00:47 +08:00  
**Purpose:** 唯一当前工作入口；正式文件采用“内容描述 + YYYYMMDD_HHMM”时间戳命名。

## 0. Current governing baseline

Theory:

- `current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_ANALYTIC_LIMIT_TANGENT_UNIFIED_THEORY_20260812_1734.md`

Case21 contract:

- `current/workflows/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_EXECUTION_CONTRACT_20260812_1734.md`

Naming governance:

- `current/governance/NZ_SCCM_TIMESTAMP_NAMING_AND_BASELINE_DECISION_20260812_1734.md`

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
PANEL_LEVEL_SURROGATE = NO
```

---

## 1. Current fresh Case21 evidence package

Raw input freeze:

- `current/case21/NZ_SCCM_CASE21_RAW_INPUT_FREEZE_20260812_1734.md`

Fresh material coefficients:

- `current/case21/NZ_SCCM_CASE21_FRESH_MATERIAL_COEFFICIENTS_20260812_1802.csv`

Theory result frozen before experiment:

- `current/results/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_THEORY_FREEZE_20260812_1802.md`

Experiment-only source opened after theory freeze:

- `current/case21/NZ_SCCM_CASE21_EXPERIMENT_ONLY_SOURCE_20260812_1802.md`

Final closure:

- `current/results/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_FULL_CLOSURE_20260812_1802.md`

Swartz24 current fresh completion / failure comparison:

- `current/results/NZ_SCCM_SWARTZ24_FRESH_PU_COMPLETION_FAILURE_COMPARISON_AND_EXTERNAL_PANEL_SCREEN_20260813_0047.md`
- `current/results/NZ_SCCM_SWARTZ24_CURRENT_FRESH_PU_FAILURE_COMPARISON_20260813_0047.csv`

---

## 2. Isolation status

```text
HISTORICAL_CASE21_D_Q_P_Pu_ROOT_PATH_USED = NO
HISTORICAL_CASE21_ANALYTIC_RESULT_USED = NO
HISTORICAL_FE_GAUSS_SIMPSON_RESULT_USED = NO
HISTORICAL_MATERIAL_POINT_HISTORY_USED = NO
EXPERIMENT_USED_DURING_SOLVE = NO
EXPERIMENT_USED_FOR_ROOT_SELECTION = NO
EXPERIMENT_USED_FOR_PARAMETER_TUNING = NO
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
```

---

## 3. Fresh Case21 current result

Corrected general-D15 primary branch first `+ -> -` load maximum:

\[
\boxed{D_u=0.7822850963110681},
\]

\[
\boxed{q_u=0.0017707520964949533},
\]

\[
\boxed{A_u=2.160317557723843\ \mathrm{mm}},
\]

\[
\boxed{P_u^{theory}=365.580427565\ \mathrm{kN}}.
\]

Load components:

\[
P_c=336.968777333\ \mathrm{kN},
\qquad
P_s=28.611650232\ \mathrm{kN}.
\]

Residual gates:

\[
R_{norm}=1.5607568553\times10^{-6}<10^{-5},
\]

\[
|L_{norm}|=4.0119433896\times10^{-6}<10^{-5}.
\]

Continuous compiler-domain certificate: PASS.

Reinforcement whole-field elastic-branch certificate: PASS.

---

## 4. Current tangent control

Zero-state regression:

\[
\boxed{K_Z(0,0)=823.416805664979\ \mathrm{N/mm}}
\]

```text
ZERO_STATE_TANGENT_REGRESSION = PASS
```

At the first load maximum:

\[
K_{Z,c}^{mat}=765.4620815266977,
\]

\[
K_{Z,c}^{geo}=-719.5765678312335,
\]

\[
K_{Z,s}^{mat}=0,
\]

\[
K_{Z,s}^{geo}=-45.50598684467001\ \mathrm{N/mm},
\]

hence

\[
\boxed{K_Z=+0.37952685079415716\ \mathrm{N/mm}>0}.
\]

First tangent-zero on the same corrected primary branch:

\[
D_T=0.7824254327857517,
\qquad
q_T=0.0017710077550576295,
\]

with

\[
K_Z\approx0.
\]

Since

\[
D_T-D_u=0.0001403364746835889>10^{-4},
\]

current classification:

```text
PRELIMIT_TANGENT_STABILITY = PASS
LIMIT_POINT_CONTROL = YES
COUPLED_LIMIT_TANGENT_CONTROL = NO
```

The coefficient-space tangent implementation was independently rechecked at unloaded and loaded Case21 during the 2026-08-13 Swartz24 continuation and reproduces the governing tangent to numerical roundoff / coefficient-set micro-difference.

---

## 5. Material compiler fidelity record

Current timestamped Case21 contract requires reporting but does not freeze a new numerical cutoff for global E1. Fresh records:

| primitive | E0 value metric | E1 tangent metric |
|---|---:|---:|
| U | 0.00245360402031 | 0.906633445993 |
| C | 0.0140129840394 | 1.21310364652 |
| T | 0.0895720993894 | 199.312325124 |
| T7 | 0.112736914660 | 64.1319479976 |

No new threshold, N48-order change or R10 modification was introduced in this calculation.

---

## 6. Case21 experimental quantities: distinguish Pcr from Pf

Nguyen Chapter 5 table labels Case21 experimental buckling/critical load as:

\[
P_{cr,exp}=336\ \mathrm{kN}.
\]

This is a **buckling/critical** quantity and must not be used as the ultimate/failure-load accuracy metric.

The Swartz experimental **failure/ultimate** load used for current Pu validation is:

\[
\boxed{P_{f,exp}=368.3127497435694\ \mathrm{kN}}.
\]

With

\[
P_u^{theory}=365.580427565\ \mathrm{kN},
\]

the ultimate-load comparison is:

\[
\Delta P=-2.7323221785694\ \mathrm{kN},
\]

\[
\boxed{\delta_{Pu/Pf}=-0.741848\%}.
\]

The older `+8.8037%` value is specifically `Pu_theory` versus experimental `Pcr=336 kN`; it remains a buckling-vs-limit diagnostic only, not a failure-load error.

---

## 7. Swartz24 current fresh completion

User authorization supersedes the earlier `SWARTZ24_RECALCULATION = NOT AUTHORIZED` state.

```text
SWARTZ24_RECALCULATION_AUTHORIZED = YES
SWARTZ24_FRESH_PU_VALUES = 24/24 AVAILABLE
SWARTZ24_FAILURE_LOAD_COMPARISON = COMPLETE
SWARTZ24_FULL_L_KZ_PRODUCTION_GATE = PENDING_24_PANEL_BULK_COMPLETION
CASE21_FULL_L_KZ_GATE = PASS
```

Current 24-panel failure-load comparison statistics:

```text
mean signed error = -2.8105 %
MAE               = 12.0600 %
RMSE(error %)      = 13.5244 %
median |error|     = 11.7819 %
mean Pu/Pf         = 0.97190
|error| <= 5%      = 4/24
|error| <= 10%     = 8/24
|error| <= 15%     = 17/24
```

Thickness/slenderness group diagnostics:

|Group|Cases|mean signed error|MAE|
|---|---|---:|---:|
|b/t ~ 48|1–8|+6.313%|13.135%|
|b/t ~ 38.3|9–16|-11.849%|14.662%|
|b/t ~ 63.1|17–24|-2.896%|8.383%|

The strongest systematic bias is the Case9–16 thick-panel group. This is treated as a model-form/current-tangent/post-buckling redistribution diagnostic; no R10/N48/group-factor calibration is authorized or performed.

---

## 8. Additional uploaded physical-panel screen

```text
ADDITIONAL_UPLOADED_PHYSICAL_RC_PANEL_DATASETS
BOTH_STRUCTURE_COMPATIBLE_AND_INPUT_COMPLETE = 0
```

Current classifications:

- Ernst (1952): `INPUT_INCOMPLETE`.
- Saheb & Desayi (1990): `OUT_OF_CURRENT_SCOPE + INPUT_INCOMPLETE` because the tests use constant eccentricity `e=t/6` and the uploaded material lacks a complete specimen-by-specimen current-contract input table.
- Attard (1994): `REFERENCE_ANALYTICAL_ONLY`.
- Sanjayan/Maheswaran-related tests referenced by Nguyen: `INPUT_INCOMPLETE / POSSIBLE_BOUNDARY_MISMATCH`.
- Nguyen high-strength/parametric cases: `NUMERICAL_REFERENCE_ONLY`.
- Uploaded steel-wall/CFT/UHPC material/interface tests: `OUT_OF_CURRENT_SCOPE` for the present ordinary-RC-panel production contract.

No missing parameter is inferred from experimental Pu/Pf.

---

## 9. Current status

```text
CASE21_ZERO_SPATIAL_ANALYTIC_CALCULATION = COMPLETE
CASE21_19_ITEM_CONTRACT = COMPLETE
CASE21_CALCULATION_CLOSURE = PASS
CASE21_CONTROL = FIRST +->- LIMIT POINT
CASE21_PRELIMIT_TANGENT_STABILITY = PASS
CASE21_THEORY_Pu = 365.580427565 kN
CASE21_FAILURE_LOAD_Pf = 368.3127497435694 kN
CASE21_Pu_VS_Pf_ERROR = -0.741848 %
NGUYEN_CASE21_336_kN = EXPERIMENTAL_Pcr / NOT Pf
SWARTZ24_FRESH_Pu = 24/24 AVAILABLE
SWARTZ24_Pu_VS_FAILURE_COMPARISON = COMPLETE
SWARTZ24_FULL_L_KZ_GATE = PENDING_BULK_COMPLETION
ADDITIONAL_COMPATIBLE_INPUT_COMPLETE_PHYSICAL_RC_PANEL_DATASETS = 0
CURRENT_NEXT_TASK = BULK_24_PANEL_L_KZ_GATE_OR_USER_DIRECTED
```
