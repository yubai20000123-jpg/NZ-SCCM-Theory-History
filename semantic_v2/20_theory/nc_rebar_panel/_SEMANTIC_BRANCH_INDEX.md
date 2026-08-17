# NC + rebar panel theory semantic branch

## Current end-to-end production-development identity

The current mainline remains one continuous Case21 formal calculation:

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

Current path:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
 -> Nguyen second-order continuous strain
 -> Airy-compatible scalar membrane redistribution r=lambda*M*a(nu)
 -> same-state frozen R10 concrete + reinforcement
 -> stable conformal source/matrix DAG
 -> certified Case21 16-state source field
 -> single fixed-domain semialgebraic positive-part period
 -> T12 + same-source derivatives
 -> connected (D,q,lambda) solve
 -> Rq=0, RA=0, L3=0
 -> formal Case21 Pu
```

The last two structural stages are not yet executable because the non-enumerative semialgebraic-period numeric runtime remains absent. This is an internal blocker of the same end-to-end task, not a new project task.

## Formal counters / frozen physics

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
R10 = FROZEN
reinforcement before solve = REQUIRED
Airy-scalar r=lambda*M*a(nu) = ACTIVE
five-free nonlinear Rm relaxation = REJECTED
high-order coefficient enumeration as production = PROHIBITED
Z6 analytical boundary = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```

## Current direct-source mechanics oracle

```text
D = 0.7887924801
q = 0.0018083572563
lambda = 0.0862359635383
M = 0.0290703347837
Pc = 337.923030 kN
Ps = 28.844798 kN
Pu = 366.767829 kN
Pf_exp = 368.312750 kN
error = -0.419459 %
```

This remains an audit/mechanics oracle only.

## T12 structural contract

```text
Jx00, Jx20, Jx02, Jx22c,
Jy00, Jy20, Jy02, Jy22c,
Jxy22s,
Jx11s_1, Jy11s_1, Jxy11c_1
```

feeds exactly `Pc, RAc, Rqc` with

```text
stress moments  : k=0,1
tangent kernels : k=0,1,2.
```

11:26 audits remain:

```text
COMPACT_SOURCE_R10 = PASS
T12_VALUE_CONTRACT = PASS_AUDIT
T12_DERIVATIVE_CONTRACT = PASS_AUDIT
```

## 11:55 stable conformal R10 source

Define

\[
W=E(\sqrt{E^2+\eta^2I}+\eta I)^{-1}.
\]

Exact identities:

\[
\pi_\eta(E)=EW(I+W)^2(I+W^2)^{-2},
\]

\[
\pi_\eta(-E)=EW(I-W)^2(I+W^2)^{-2}.
\]

```text
STABLE_CONFORMAL_SOURCE_IDENTITY = PASS_EXACT
```

## 11:55 Case21 branch certificate and 16-state reduction

No-spatial-sampling tensor Bernstein enclosure over

```text
D      in [0.75,0.82]
q      in [0.00175,0.00187]
lambda in [0.0,0.15]
```

proves

```text
gap >= 0.7242936864852092
t_minus/a <= 4.804460717539394e-5 < 1
t_plus/a  <= 2.6948274361042803 < 10
```

so the exact source field in this Case21 solve box needs only

```text
g      = sqrt(Delta_E)
splus  = sqrt(lambda_plus^2+eta^2)
sminus = sqrt(lambda_minus^2+eta^2)
h1     = sqrt((t_plus-a)^2)
```

and therefore

```text
CASE21_CERTIFIED_SEARCH_BOX_ALGEBRAIC_STATE_BOUND = 16
GENERIC_GLOBAL_R10_BRANCH_FREE_STATE_BOUND = 64  # retained outside the box
```

## Period-classification refinement

The first Foster knot is physically crossed inside the complete halfwave and the frozen tensile source is C2 but not analytic there. Hence `h1=|t_plus-a|` glues two real algebraic branches.

The production representation

```text
GLOBAL_FIXED_ENDPOINT_POSITIVE_PART_FACTORISED_PERIOD
```

is retained but precisely classified as

```text
SINGLE_FIXED_DOMAIN_SEMIALGEBRAIC_PERIOD
```

rather than one holomorphic algebraic branch across the entire domain.

An exact tangent-half-angle map sends the whole `(X,Y,zeta)` domain to one unit cube, so this refinement preserves `N_formal_spatial_subdomains=1` and introduces no event cells.

## Current true blocker

An ordinary analytic 16-state Pfaffian propagator is singular at the real positive-part branch switch (`h1=0`) and is therefore not the missing production runtime.

The missing primitive is now precisely

```text
NONENUMERATIVE_SINGLE_DOMAIN_SEMIALGEBRAIC_PERIOD_NUMERIC_RUNTIME
```

which must return formal T12 and same-source `(D,q,lambda)` derivatives with no spatial quadrature/cells/material points/high-order multivariate coefficient enumeration.

```text
FORMAL_T12 = NOT RELEASED
FORMAL_Rq_RA_L3_SOLVE = NOT RUN
FORMAL_CASE21_Pu = NOT RELEASED
```

## Development-only coefficient audit

A branch-restricted dense spectral coefficient prototype was rerun at the fixed oracle state. `P` lies near 366.75–366.91 kN over caps N=12..24, but `Rq/RA` remain order-sensitive. It remains **development/audit only** and cannot be promoted to production.

## Prohibited regressions

```text
NO XY/THICKNESS EVENT CELLS OR SUBDOMAINS
NO MATERIAL-POINT GRID/HISTORY
NO FORMAL GAUSS/SIMPSON/ADAPTIVE INTEGRATION
NO HIGH-ORDER MULTIVARIATE COEFFICIENT ENUMERATION
NO EXPLICIT GIANT 64-RATIONAL CANONICALIZATION
NO N48 FALLBACK
NO AUTOMATIC NEW CAS/BACKEND CHAIN
NO NEW PROJECT TASK NAME FOR THIS BLOCKER
```

## Current artifacts

- `../../10_governance/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_REFINEMENT__LOCK.md`
- `20260817_1155__NZSCCM__CASE21_STABLE_CONFORMAL_SOURCE_16_STATE_AND_SINGLE_DOMAIN_SEMIALGEBRAIC_PERIOD__THEORY.md`
- `../../40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__EXECUTION_REPORT.md`
- `../../40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__REPRO.py`
- `../../40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__DEVELOPMENT_DENSE_SPECTRAL_T12_REPRO.py`

## Current status

```text
CURRENT_END_TO_END_TASK = CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
STATUS = BLOCKED_AT_NONENUMERATIVE_SINGLE_DOMAIN_SEMIALGEBRAIC_PERIOD_NUMERIC_RUNTIME
NEW_PROJECT_TASK_CREATED = NO
ROUTE_CHANGED = NO
```
