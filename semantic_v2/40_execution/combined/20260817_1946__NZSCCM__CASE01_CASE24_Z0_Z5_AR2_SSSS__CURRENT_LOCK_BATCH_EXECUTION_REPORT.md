# NZ-SCCM — 当前最终锁定理论下 Case01–Case24 与 Z0–Z5（AR2/SSSS）统一批量计算

**Timestamp:** 2026-08-17 19:46 +09:00  
**Status:** CURRENT THEORY BATCH EXECUTION / SAME CHAIN / NO COMPARATOR CALIBRATION  
**Canonical lock:** `semantic_v2/10_governance/20260817_1824__NZSCCM__ZERO_SPATIAL_DISCRETIZATION_FINITE_CURRENT_TRUE_INFINITE_D15__CANONICAL_LOCK.md`  
**Canonical commit:** `f39bdeaebcb2d08132883cd7eb9915fdd829f4da`

## 1. Governing identity

This batch uses one chain only:

```text
actual geometry + theoretical four-edge simple supports
-> mechanically controlling complete representative halfwave
-> ONE_CONTINUOUS_COMPLETE_HALFWAVE
-> Nguyen second-order finite trigonometric-thickness strain field
-> finite current material operator
-> exact true-infinite analytic representation
-> nth analytic term
-> exact 2x2 Cayley-Hamilton reduction
-> exact General-D15 continuous-domain moment
-> n->infinity target sum
-> finite total P,Rq,RA and same-source tangent/Jacobian
-> finite coupled equilibrium/limit root
-> Pu
-> Pf / Zhou / Winter comparison only after Pu is frozen
```

Formal counters:

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

The continuum integral exists mathematically. No spatial numerical quadrature or spatial discretization is part of the formal operator. The analytic-series index is not a spatial DOF.

## 2. Decimal root localization

Stage III already establishes the identity

\[
\lim_{N\to\infty}D15[W:S_N]=D15[W:S_{current}].
\]

For decimal root localization/checking in this bulk run, a direct-current continuum evaluator is used only as an independent numerical localizer for the same finite target functions. It does not define the formal integral and does not change the formal counters. Pf, Zhou and Winter are never supplied to root selection.

At the Case21 exact released root:
- exact true-infinite/D15 `Pu = 366.767828685 kN`;
- 64x64x26 independent continuum localizer gives `366.759799765 kN`.

The difference is about `0.0080 kN` (`0.0022%`). This is retained only as an engineering localization audit. Case21 itself is reported using the exact released D15 value.

## 3. Case01–Case24 common geometry and input convention

All Swartz panels are calculated at:

```text
b = 1220 mm
physical a = 2440 mm = 2b
m* = 2
representative complete halfwave ell = a/m* = b = 1220 mm
q0 = b/400 / b = 0.0025
boundary = theoretical four-edge simply supported
```

The original panel-specific `t, fc, eps0, E0, reinforcement layer count and layer offset` are retained.

Current NZ-SCCM reinforcement input convention follows the accepted Case21 input lock: the table percentage is treated as the **total bidirectional percentage** and is split equally between x and y. Thus, for example, Case21 `0.75% total -> rho_sx=rho_sy=0.00375`. This convention is applied uniformly to all 24 panels. No Pf value is used in this mapping or in the solve.

## 4. Case01–Case24 results

|Case|D|q|Pu (kN)|Pf (kN)|误差|
|---:|---:|---:|---:|---:|---:|
|1|0.987087|0.0006942|585.13|490.19|+19.37%|
|2|0.986792|0.0006228|573.11|506.65|+13.12%|
|3|1.041434|0.0006562|504.63|444.38|+13.56%|
|4|1.026694|0.0005611|537.80|534.23|+0.67%|
|5|1.072199|0.0006405|534.69|623.64|-14.26%|
|6|1.091134|0.0008189|607.02|691.70|-12.24%|
|7|1.100954|0.0007240|602.41|640.10|-5.89%|
|8|1.115945|0.0007297|515.68|455.05|+13.32%|
|9|1.009610|0.0004137|516.37|625.86|-17.49%|
|10|1.005446|0.0003691|533.22|696.15|-23.40%|
|11|1.069528|0.0003871|516.58|636.54|-18.85%|
|12|1.080031|0.0005877|552.92|639.65|-13.56%|
|13|1.140598|0.0004945|566.02|511.99|+10.55%|
|14|1.108294|0.0004283|637.42|716.16|-11.00%|
|15|1.168924|0.0004653|671.40|766.43|-12.40%|
|16|1.210005|0.0005509|594.67|721.95|-17.63%|
|17|0.942732|0.0012256|330.38|429.25|-23.03%|
|18|0.955481|0.0010255|350.63|396.34|-11.53%|
|19|0.943436|0.0013625|356.84|377.65|-5.51%|
|20|0.880152|0.0015992|351.21|372.76|-5.78%|
|21|0.788792|0.0018084|366.77|368.31|-0.42%|
|22|0.855280|0.0016560|370.28|355.86|+4.05%|
|23|0.975055|0.0012736|376.49|346.96|+8.51%|
|24|0.960757|0.0013881|442.54|400.34|+10.54%|

Error statistics versus Pf:

```text
mean signed error = -4.138 %
MAE               = 11.946 %
RMSE               = 13.407 %
largest low bias   = Case 10: -23.405 %
largest high bias  = Case 1: +19.367 %
```

Case21 remains the exact released anchor:

\[
P_u=366.767828685\text{ kN},\qquad
P_f=368.312749744\text{ kN},\qquad
\Delta=-0.419459\%.
\]

## 5. Z0–Z5 modified geometry

Only physical length is standardized to `a=2b`; section/material parameters are retained. All are theoretical four-edge simply supported.

```text
Z0: b=6000 mm, a=12000 mm, ell=6000 mm
Z1: b=6000 mm, a=12000 mm, ell=6000 mm
Z2: b=6000 mm, a=12000 mm, ell=6000 mm
Z3: b=6000 mm, a=12000 mm, ell=6000 mm
Z4: b=8000 mm, a=16000 mm, ell=8000 mm
Z5: b=2000 mm, a=4000 mm, ell=2000 mm
m*=2 for all
A0=a/500
q0=A0/b=0.004
```

Full-section current operator:
- ordinary concrete: frozen finite R10 current operator;
- concrete effective fraction `1-rho_w=0.98` to avoid web-volume double counting;
- two face plates: finite local ideal-EP radial current map;
- longitudinal web/PBL steel phase: continuous homogenized uniaxial ideal-EP current map with `rho_w=0.02`;
- all phases enter `P,Rq,RA` before the coupled solve.

## 6. Z0–Z5 results and post-solve comparators

|Case|D|q|Pc,eff (MN)|Ps,face (MN)|Pw (MN)|Pu (MN)|Zhou (MN)|误差|Winter (MN)|误差|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|Z0|0.919410|0.0025866|10.09|16.87|5.03|31.99|36.95|-13.41%|41.50|-22.91%|
|Z1|0.609480|0.0044311|7.27|10.35|2.40|20.02|23.72|-15.59%|26.10|-23.28%|
|Z2|1.175921|0.0081200|11.11|19.38|6.05|36.54|41.21|-11.34%|45.73|-20.11%|
|Z3|0.677684|0.0024716|16.26|16.90|5.04|38.20|44.32|-13.81%|49.05|-22.11%|
|Z4|0.915645|0.0010605|25.63|23.09|10.72|59.43|69.34|-14.29%|79.39|-25.14%|
|Z5|0.928662|0.0001284|4.99|5.91|1.73|12.64|14.68|-13.93%|14.68|-13.93%|

Comparator replay is the same project Zhou/Winter calculation for the modified AR2 objects. No comparator quantity enters the NZ-SCCM root.

Mean comparison:

```text
mean NZ-SCCM - Zhou   = -13.729 %
MAE  vs Zhou          = 13.729 %
mean NZ-SCCM - Winter = -21.248 %
MAE  vs Winter        = 21.248 %
```

## 7. Immediate batch reading

### Swartz 24

The current theory is not uniformly biased across all 24 panels. It gives:
- near coincidence for Case4 and Case21;
- positive deviations in Cases1–3, 8, 13, 22–24;
- negative deviations in most of Cases5–7, 9–12, 14–20.

The full-sample mean signed error is only about `-4.14%`, but MAE is about `11.95%`; therefore cancellation between high and low predictions is substantial and the per-panel distribution must be retained.

### Z0–Z5

With every object standardized to `a/b=2`, the current NZ-SCCM predictions are consistently below both comparison curves:
- versus Zhou: approximately `-11.34%` to `-15.59%`;
- versus Winter: approximately `-13.93%` to `-25.14%`.

This is a systematic cross-specimen trend after the AR2/SSSS normalization. It is reported as a result, not calibrated away.

## 8. Identity / governance audit

```text
FORMAL_SPATIAL_DISCRETIZATION = 0
FORMAL_SPATIAL_NUMERICAL_QUADRATURE = 0
FINITE_CURRENT_OPERATOR = YES
TRUE_INFINITE_ANALYTIC_REPRESENTATION = YES
EXACT_NTH_TERM_CH_D15 = GOVERNING
SERIES_INDEX_AS_SPATIAL_DOF = NO
REINFORCEMENT_STEEL_ENTER_BEFORE_SOLVE = YES
EXPERIMENT_USED_TO_SELECT_ROOT = NO
ZHOU_USED_TO_SELECT_ROOT = NO
WINTER_USED_TO_SELECT_ROOT = NO
PANEL_LEVEL_SURROGATE = NO
```
