# NZ-SCCM Swartz24 current fresh Pu completion, failure-load comparison, and external RC-panel screen

**Timestamp:** 2026-08-13 00:47 +08:00  
**Status:** CURRENT EXECUTION FREEZE / NON-CALIBRATING

## 0. Execution boundary

User authorization now explicitly permits continuation of Swartz24 calculation and comparison with experimental failure/ultimate loads.

The governing chain remains:

\[
R10\to N48\text{-}C1/MM\to CH\to Nguyen\to general\text{-}D15\to P,R_q,L\to K_Z.
\]

No R10 modification, N48 order change, panel-level calibration, structural surrogate, formal spatial Gauss/Simpson/adaptive quadrature, material-point grid, or spatial cell was introduced.

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
```

Experimental failure loads were not used to solve, select roots, set compiler intervals, or tune any material/structural parameter. They are opened only after the current theoretical Pu values are available.

## 1. Fresh completion of Cases 19–24

Cases 19, 20, 22, 23 and 24 were continued from raw panel inputs through fresh R10/N48-C1-MM/current-map/general-D15 equilibrium-limit calculations. Case21 uses the current governing fully closed result already frozen in `current/CURRENT_STATE.md`.

| Case | D_u | q_u | Pc / kN | Ps / kN | Pu / kN | Rq at root / kN mm |
|---:|---:|---:|---:|---:|---:|---:|
|19|0.895498262463|0.001490667301|336.793838|19.608371|356.402209|-4.41e-6|
|20|0.841997608509|0.001686144683|328.767761|19.130876|347.898637|-1.03e-5|
|21|0.782285096311|0.001770752096|336.968777|28.611650|365.580428|current formal gate PASS|
|22|0.829956917853|0.001656490263|338.847839|28.705329|367.553168|-1.44e-5|
|23|0.925495201721|0.001295223916|339.612749|36.305167|375.917916|-7.49e-7|
|24|0.922369098591|0.001430121260|400.126085|41.516378|441.642463|-2.19e-6|

Fresh exact-D15 contraction checks for these remaining panels include:

|Case|D[Syy]|D[Qq]|max |eps_s||
|---:|---:|---:|---:|
|19|-14.028246662|3.395287203|0.001684|
|20|-13.507172753|3.235178754|0.001667|
|22|-13.542680227|4.690254484|0.001643|
|23|-14.254938246|6.800873430|0.001546|
|24|-14.210001306|6.083235024|0.001725|

All listed steel strains remain below the frozen steel yield strain 0.00265.

Fresh zero-state tangent regression targets for Cases19–24 are respectively 861.0241, 807.1386, 823.4168, 853.8628, 977.1682 and 1083.2446 N/mm. The coefficient-space tangent implementation was independently rechecked at unloaded and loaded Case21 and reproduces the governing Case21 tangent to numerical roundoff / coefficient-set micro-difference. Case21 retains full tangent-gate PASS.

**Important scope statement:** this execution freezes 24/24 theoretical Pu values and the failure-load comparison. It does **not** yet claim that the full same-expression L and KZ production gate has been bulk-completed for every one of the 24 panels. The 24-panel bulk tangent gate remains a separate pending audit.

## 2. Current 24-panel theory versus experimental failure load

The comparison quantity is experimental **failure/ultimate load Pf**, not Nguyen's experimental buckling/critical load Pcr.

|Case|Pu theory / kN|Pf experiment / kN|error / %|
|---:|---:|---:|---:|
|1|608.925|490.194|+24.221|
|2|596.865|506.652|+17.806|
|3|519.198|444.377|+16.837|
|4|555.423|534.231|+3.967|
|5|546.874|623.641|-12.309|
|6|617.784|691.698|-10.686|
|7|612.628|640.099|-4.292|
|8|523.127|455.053|+14.960|
|9|532.126|625.865|-14.977|
|10|549.896|696.147|-21.009|
|11|525.373|636.541|-17.464|
|12|560.678|639.654|-12.347|
|13|569.612|511.990|+11.254|
|14|644.025|716.164|-10.073|
|15|671.979|766.429|-12.323|
|16|593.075|721.946|-17.851|
|17|333.398|429.253|-22.331|
|18|357.715|396.337|-9.745|
|19|356.402|377.654|-5.627|
|20|347.899|372.761|-6.670|
|21|365.580|368.313|-0.742|
|22|367.553|355.858|+3.287|
|23|375.918|346.961|+8.346|
|24|441.642|400.340|+10.317|

Overall statistics:

```text
mean signed error = -2.8105 %
MAE               = 12.0600 %
RMSE(error %)      = 13.5244 %
median |error|     = 11.7819 %
mean Pu/Pf         = 0.97190
sample std(Pu/Pf)  = 0.13514
|error| <= 5%      = 4/24
|error| <= 10%     = 8/24
|error| <= 15%     = 17/24
```

### 2.1 Thickness/slenderness groups

|Group|Cases|mean Pu / kN|mean Pf / kN|mean signed error|MAE|
|---|---|---:|---:|---:|---:|
|b/t ~ 48|1–8|572.603|548.243|+6.313%|13.135%|
|b/t ~ 38.3|9–16|580.846|664.342|-11.849%|14.662%|
|b/t ~ 63.1|17–24|368.263|380.935|-2.896%|8.383%|

The strongest systematic pattern remains the thick/low-slenderness Case9–16 group: current theory is low by about 11.85% on average. The most slender Case17–24 group is the best overall group. The transition group Case1–8 has positive and negative errors that partly cancel in the group mean.

### 2.2 Reinforcement-ratio grouping

|total reinforcement|mean signed error|MAE|
|---:|---:|---:|
|0.20%|-4.339%|18.348%|
|0.50%|-3.551%|10.485%|
|0.75%|-3.212%|8.059%|
|1.00%|-0.141%|11.348%|

There is no simple monotonic reinforcement-ratio bias. Thickness/slenderness and the associated material-nonlinearity/stability regime remain a stronger diagnostic signal.

## 3. Case21 correction: ultimate comparison versus buckling comparison

Current governing theoretical ultimate load is

\[
P_u^{theory}=365.580427565\ \mathrm{kN}.
\]

The relevant Swartz experimental **failure** load is

\[
P_f=368.312749744\ \mathrm{kN},
\]

hence

\[
\boxed{(P_u-P_f)/P_f=-0.74185\%}.
\]

Nguyen's `336 kN` value for Case21 is labelled experimental `Pcr` and is a buckling/critical load. Comparing current Pu directly with 336 kN answers a different question and must not be used as the ultimate-load accuracy metric.

## 4. Error-mechanism diagnosis without calibration

No parameter is changed from the observed errors.

Source evidence for Swartz panels indicates that the three thickness groups enter different stability/material-nonlinearity regimes. The thick Case9–16 group reaches a very high fraction of concrete strength before buckling, so post-buckling membrane redistribution and near-peak current tangent treatment are especially influential. The slender Case17–24 group buckles earlier and is more naturally aligned with a representative continuous halfwave/tangent-stability description. Therefore the systematic Case9–16 underprediction is treated as a model-form/free-degree/state-redistribution diagnostic, not as permission to raise R10 strength or fit a group factor.

The sign changes across the 24 panels also rule out a single global scale correction as a defensible next step.

## 5. Screen of other uploaded specimens for same-contract physical validation

The uploaded literature was screened for **physical RC wall/panel tests** satisfying the present structural contract and having enough raw specimen inputs for blind calculation.

|Source/test family|status|reason|
|---|---|---|
|Swartz et al. 24 RC panels|CALCULATED|four-side simply-supported, near-uniform one-direction compression; current validation set|
|Ernst (1952) panels|INPUT_INCOMPLETE|Nguyen supplies only broad geometry ranges in the uploaded material; not enough specimen-level concrete/rebar/imperfection/failure data for the current contract|
|Saheb & Desayi (1990), 24 two-way wall panels|OUT_OF_CURRENT_SCOPE + INPUT_INCOMPLETE|tests used constant load eccentricity e=t/6 and two reinforcement layers; current contract is central axial compression; uploaded summary also lacks a complete specimen-by-specimen raw table|
|Attard (1994)|REFERENCE_ANALYTICAL_ONLY|analytical tangent-modulus wall-buckling report; not a new physical test campaign|
|Sanjayan / Maheswaran-related wall tests referenced by Nguyen|INPUT_INCOMPLETE / POSSIBLE_BOUNDARY_MISMATCH|uploaded Nguyen/Attard material does not provide a complete current-contract specimen table; support/load-control conditions differ in the reviewed literature|
|Nguyen high-strength/parametric Chapter 5 cases|NUMERICAL_REFERENCE_ONLY|finite-element/analytical study cases, not an independent physical ultimate-load test set|
|Zhang Ning / Yun Lu / Sun Lipeng steel-wall or CFT specimens|OUT_OF_CURRENT_SCOPE|steel wall / steel-concrete composite structural objects, not the current RC wall-panel model|
|UHPC triaxial cylinder sources|OUT_OF_CURRENT_SCOPE|material tests rather than RC wall-panel structural tests|
|Hu steel-UHPC interface push-out tests|OUT_OF_CURRENT_SCOPE|interface shear specimens, not axial RC panels|

Therefore:

```text
ADDITIONAL_UPLOADED_PHYSICAL_RC_PANEL_DATASETS
BOTH_STRUCTURE_COMPATIBLE_AND_INPUT_COMPLETE = 0
```

No missing parameter was inferred from an experimental ultimate load.

## 6. Current execution status

```text
SWARTZ24_RECALCULATION_AUTHORIZED = YES
SWARTZ24_FRESH_PU_VALUES = 24/24 AVAILABLE
SWARTZ24_FAILURE_LOAD_COMPARISON = COMPLETE
SWARTZ24_FULL_L_KZ_PRODUCTION_GATE = PENDING_24_PANEL_BULK_COMPLETION
CASE21_FULL_L_KZ_GATE = PASS
CASE21_ULTIMATE_EXPERIMENT_REFERENCE = FAILURE_LOAD 368.3127497435694 kN
CASE21_PU_VS_FAILURE_ERROR = -0.741848 %
NGUYEN_CASE21_336_kN = EXPERIMENTAL_BUCKLING_LOAD_Pcr / NOT FAILURE_LOAD
ADDITIONAL_COMPATIBLE_INPUT_COMPLETE_PHYSICAL_RC_PANEL_DATASETS = 0
R10_MODIFIED = NO
N48_ORDER_CHANGED = NO
EXPERIMENT_CALIBRATION = NO
```

The machine-readable 24-panel comparison is frozen in:

`current/results/NZ_SCCM_SWARTZ24_CURRENT_FRESH_PU_FAILURE_COMPARISON_20260813_0047.csv`.
