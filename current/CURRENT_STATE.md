# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-12 18:02 +08:00  
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

## 6. Experiment-only comparison

Only after theory-result freeze, Nguyen Chapter 5 experimental table was opened. Case21 experiment column:

\[
P_{exp}=336\ \mathrm{kN}.
\]

The thesis table labels this experimental quantity `Exp. Pcr`.

Comparison:

\[
\Delta P=+29.580427565\ \mathrm{kN},
\]

\[
\boxed{\delta_P=+8.803698680\%},
\]

\[
P_u^{theory}/P_{exp}=1.0880369868.
\]

---

## 7. Current status

```text
CASE21_ZERO_SPATIAL_ANALYTIC_CALCULATION = COMPLETE
CASE21_19_ITEM_CONTRACT = COMPLETE
CALCULATION_CLOSURE = PASS
CONTROL = FIRST +->- LIMIT POINT
PRELIMIT_TANGENT_STABILITY = PASS
THEORY_RESULT = 365.580427565 kN
EXPERIMENT = 336 kN
ERROR = +8.803698680 %
SWARTZ24_RECALCULATION = NOT AUTHORIZED / NOT PERFORMED
CURRENT_NEXT_TASK = USER_DIRECTED
```
