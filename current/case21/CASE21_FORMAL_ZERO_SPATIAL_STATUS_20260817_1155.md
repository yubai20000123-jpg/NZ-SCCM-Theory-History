# Case21 formal zero-spatial status — 2026-08-17 11:55 +08:00

## Current end-to-end task

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

No new project task has been created.

## Formal boundary

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
R10 = FROZEN
Airy-scalar r=lambda*M*a(nu) = ACTIVE
high-order coefficient enumeration as production = PROHIBITED
```

## Current direct-source mechanics oracle

```text
D      = 0.7887924801
q      = 0.0018083572563
lambda = 0.0862359635383
M      = 0.0290703347837
Pc     = 337.923030 kN
Ps     =  28.844798 kN
Pu     = 366.767829 kN
Pf_exp = 368.312750 kN
error  = -0.419459 %
```

This remains audit/mechanics only, not the formal zero-spatial release.

## 11:55 exact runtime advance

The smoothed source now uses the exact stable conformal identities

\[
\pi_\eta(E)=EW(I+W)^2(I+W^2)^{-2},
\]

\[
\pi_\eta(-E)=EW(I-W)^2(I+W^2)^{-2},
\]

with

\[
W=E(\sqrt{E^2+\eta^2I}+\eta I)^{-1}.
\]

A tensor Bernstein enclosure, with no spatial sampling, certifies throughout the current formal search box

```text
D      in [0.75,0.82]
q      in [0.00175,0.00187]
lambda in [0.0,0.15]

gap >= 0.7242936864852092
t_minus/a <= 4.804460717539394e-5 < 1
t_plus/a  <= 2.6948274361042803 < 10
```

Therefore only the first tensile source knot can be active and the exact current R10 field is bounded by the four radical generators

```text
g      = sqrt(Delta_E)
splus  = sqrt(lambda_plus^2+eta^2)
sminus = sqrt(lambda_minus^2+eta^2)
h1     = sqrt((t_plus-a)^2)
```

so

```text
CASE21_CERTIFIED_SEARCH_BOX_ALGEBRAIC_STATE_BOUND = 16
GENERIC_GLOBAL_R10_BOUND = 64  # still retained outside this box
```

## Refined runtime identity

The first Foster knot is actually crossed inside the physical complete halfwave. At `X=Y=pi/2`,

```text
lambda_plus(-1) = -0.0817474943281
lambda_plus(+1) = +0.0830009484933
lambda1         = +0.0500805176491
zeta_cross      = +0.600355180536
```

The frozen tensile source is C2 but has a nonzero third-derivative jump. Therefore `h1=|t_plus-a|` is a semialgebraic gluing, not one analytic algebraic branch through the whole interval.

The exact one-domain tangent-half-angle rationalization maps the complete `(X,Y,zeta)` domain to one fixed unit cube. The surviving formal object is therefore

```text
SINGLE_FIXED_DOMAIN_SEMIALGEBRAIC_PERIOD
```

with no XY/thickness cells.

## Current blocker

```text
NONENUMERATIVE_SINGLE_DOMAIN_SEMIALGEBRAIC_PERIOD_NUMERIC_RUNTIME
    = NOT IMPLEMENTED / BLOCKING

FORMAL_T12_VALUES = NOT RELEASED
FORMAL_T12_DERIVATIVES = NOT RELEASED
FORMAL_Rq_RA_L3_SOLVE = NOT RUN
FORMAL_CASE21_Pu = NOT RELEASED
```

The former generic wording `blocked at algebraic-period runtime` is thus refined: the missing primitive is specifically a non-enumerative evaluator for the positive-part-glued semialgebraic period.

A dense spectral coefficient prototype was also rerun only as development evidence; its fixed-state load is close to the oracle but its `Rq/RA` remain order-sensitive, so it is explicitly **not** promoted to formal production.

## Canonical 11:55 evidence

- `../../semantic_v2/10_governance/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_REFINEMENT__LOCK.md`
- `../../semantic_v2/20_theory/nc_rebar_panel/20260817_1155__NZSCCM__CASE21_STABLE_CONFORMAL_SOURCE_16_STATE_AND_SINGLE_DOMAIN_SEMIALGEBRAIC_PERIOD__THEORY.md`
- `../../semantic_v2/40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__EXECUTION_REPORT.md`
- `../../semantic_v2/40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__PARAMS_AND_INTERMEDIATES.json`
- `../../semantic_v2/40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__REPRO.py`
- `../../semantic_v2/40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__DEVELOPMENT_DENSE_SPECTRAL_T12_REPRO.py`
