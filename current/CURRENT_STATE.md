# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-17 11:55 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260817_1155__NZSCCM__PROJECT__CASE21_FORMAL_ZERO_SPATIAL_16_STATE_SEMIALGEBRAIC_PERIOD__SEMANTIC_INDEX.md`

## Current controlling governance

`semantic_v2/10_governance/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_REFINEMENT__LOCK.md`

## Current end-to-end task

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

No new project-level task has been created. The 11:55 work continues the same Case21 formal calculation and refines the previously generic `fixed-endpoint algebraic-period runtime` blocker.

## Frozen backbone

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
R10 physical current operator = FROZEN
reinforcement before coupled solve = REQUIRED
Airy-scalar r=lambda*M*a(nu) = ACTIVE
General-D15 / target-first exact-moment philosophy = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
formal Gauss/Simpson/adaptive/cells/material-point-grid = PROHIBITED
high-order coefficient enumeration as production architecture = PROHIBITED
experimental calibration/root selection = PROHIBITED
Z6_BOUNDARY = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```

Gauss-Legendre and dense coefficient-space evaluators are audit/development tools only and never acquire formal production identity.

## Case21 load identity — hard locked

```text
Pcr_exp = 336.285554 kN   # experimental buckling only
Pf_exp  = 368.312750 kN   # experimental failure / ultimate
Nguyen FE buckling comparator = 298 kN
```

`Pcr` and `Pu` cross-comparison is prohibited.

## Active Case21 mechanics

```text
r = lambda*M*a(nu)
M = pi^2/eps0*(q0*q + 0.5*q^2)
a(0.18) = [-0.295,-0.205,+0.25,-0.205,+0.25]
RA = a^T Rm = 0
Rq_base = 0
```

Exact restricted-coordinate identities:

```text
R_lambda = M*RA
Rq_restricted = Rq_base + lambda*Mq*RA
```

Pure isotropic continuum benchmark: `lambda=1` exactly.

Current reinforced linear scalar benchmark:

```text
lambda_lin_RC = 0.999266844854884
              + 0.0096124785693025*D/M
```

Scalar internal stability criterion:

```text
dRA/dlambda > 0
```

At the direct-source peak:

```text
dRA/dlambda = +25.24850924
M*dRA/dlambda = +0.733982616
```

## Current direct-source mechanics oracle

```text
D      = 0.7887924801
q      = 0.0018083572563
lambda = 0.0862359635383
M      = 0.0290703347837
A_increment = 2.20620 mm
A_total     = 5.25620 mm

Pc = 337.923030 kN
Ps =  28.844798 kN
Pu = 366.767829 kN
Pf_exp = 368.312750 kN
error = -0.419459 %
```

This is the current direct-source mechanics/audit oracle, not a formal zero-spatial numeric release.

## T12 contract retained

Concrete values are represented by the fixed 12-functional target package

```text
Jx00, Jx20, Jx02, Jx22c,
Jy00, Jy20, Jy02, Jy22c,
Jxy22s,
Jx11s_1, Jy11s_1, Jxy11c_1
```

which feeds exactly `Pc, RAc, Rqc`.

Finite thickness family:

```text
stress moments  : k=0,1
tangent kernels : k=0,1,2
```

11:26 audit status remains:

```text
COMPACT_SOURCE_R10 = PASS
T12_VALUE_CONTRACT = PASS_AUDIT
T12_DERIVATIVE_CONTRACT = PASS_AUDIT
```

## 11:55 stable conformal source refinement

Define

\[
W=E(\sqrt{E^2+\eta^2I}+\eta I)^{-1}.
\]

The smoothed source maps now use the exact stable identities

\[
\pi_\eta(E)=EW(I+W)^2(I+W^2)^{-2},
\]

\[
\pi_\eta(-E)=EW(I-W)^2(I+W^2)^{-2}.
\]

These remove the poor conditioning of separate `I+W` / `I-W` inversions for strongly compressive principal states.

```text
STABLE_CONFORMAL_SOURCE_IDENTITY = PASS_EXACT
```

## 11:55 no-spatial-sampling Bernstein certificates

At the current peak, exact tensor Bernstein coefficient enclosure gives

```text
tr(E)    in [-0.9516607416735428, -0.6221638560307847]
Delta(E) in [+0.5843087672642922, +0.6592312757236101]
gap       in [+0.7644009205019916, +0.8119305855327844]

lambda_plus  in [-0.09362991058577558, +0.09488336475099984]
lambda_minus in [-0.8817956636031636, -0.6932823882663881]

t_plus/a  <= 1.8971668284751766 < 10
t_minus/a <= 4.506313752829062e-5 < 1
```

A six-variable Bernstein enclosure over the formal solve neighborhood

```text
D      in [0.75,0.82]
q      in [0.00175,0.00187]
lambda in [0.0,0.15]
```

certifies

```text
gap >= 0.7242936864852092
t_plus/a  <= 2.6948274361042803 < 10
t_minus/a <= 4.804460717539394e-5 < 1
```

No spatial point grid is used in either certificate.

## Case21 branch-specific algebraic state reduction

Inside the certified solve box the only required radicals are

```text
g      = sqrt(Delta_E)
splus  = sqrt(lambda_plus^2+eta^2)
sminus = sqrt(lambda_minus^2+eta^2)
h1     = sqrt((t_plus-a)^2) = |t_plus-a|
```

so the complete source/stress field is contained in

```text
g^i*splus^j*sminus^k*h1^l, i,j,k,l in {0,1}
```

and therefore

```text
CASE21_CERTIFIED_SEARCH_BOX_ALGEBRAIC_STATE_BOUND = 16
GENERIC_GLOBAL_R10_BRANCH_FREE_STATE_BOUND = 64  # retained outside the certified box
```

This is exact and does not use N48/N96 material approximation.

## Positive-part gluing and refined mathematical period identity

The first tensile source knot is physically crossed inside the complete halfwave. At `X=Y=pi/2`:

```text
lambda_plus(zeta=-1) = -0.0817474943281 < lambda1
lambda_plus(zeta=+1) = +0.0830009484933 > lambda1
zeta(lambda_plus=lambda1) ~= +0.600355180536
```

The frozen tensile source is C2 but not analytic at this knot:

```text
jump derivatives 0,1,2 = 0
jump derivative 3 = -3.485446758727596
A3 truncated-power coefficient = -0.580907793121266 != 0
```

Therefore `h1=|t_plus-a|` is a semialgebraic branch gluing. The previously selected

```text
GLOBAL_FIXED_ENDPOINT_POSITIVE_PART_FACTORISED_PERIOD
```

is retained, but its precise mathematical class is now

```text
SINGLE_FIXED_DOMAIN_SEMIALGEBRAIC_PERIOD
```

rather than one holomorphic algebraic branch across the physical Foster knot.

An exact tangent-half-angle rationalization maps the complete `(X,Y,zeta)` continuum to one fixed unit cube `[0,1]^3`, so this classification introduces no XY/thickness cells and preserves `N_formal_spatial_subdomains=1`.

## 11:55 actual runtime attempt verdict

An ordinary analytic 16-state Pfaffian propagator was preflighted against the real knot. Since

\[
h_1'=\frac{(t_+-a)t_+'}{h_1},
\]

it is singular at the physical `h1=0` branch switch and therefore cannot by itself represent the real positive-part gluing on the whole interval.

```text
ORDINARY_SINGLE_ANALYTIC_16_STATE_PFAFFIAN = FAIL_PRECONDITION
```

The missing formal primitive is now precisely

```text
NONENUMERATIVE_SINGLE_DOMAIN_SEMIALGEBRAIC_PERIOD_NUMERIC_RUNTIME
```

which must return T12 and same-source `(D,q,lambda)` derivatives without spatial quadrature, cells, material points, or high-order multivariate coefficient enumeration.

## Development-only dense spectral audit

A branch-restricted dense coefficient-space evaluator was rerun only for diagnosis. At the fixed mechanics-oracle state:

```text
N=12 P=366.907127085 kN Rq=-3.36219 RA=-0.07991
N=14 P=366.773503788 kN Rq=-2.20228 RA=-0.07074
N=16 P=366.750133196 kN Rq=-0.82994 RA=-0.05310
N=20 P=366.758757710 kN Rq=+0.53761 RA=-0.03878
N=24 P=366.744803343 kN Rq=+0.21580 RA=-0.02825
```

Although `P` is close to the direct-source oracle, the equilibrium residuals remain order-sensitive. This route is explicitly not promoted to production.

## Current capacity / blocker status

```text
CURRENT_END_TO_END_TASK = CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
STATUS = BLOCKED_AT_NONENUMERATIVE_SINGLE_DOMAIN_SEMIALGEBRAIC_PERIOD_NUMERIC_RUNTIME
NEW_PROJECT_TASK_CREATED = NO
ROUTE_CHANGED = NO

CASE21_CURRENT_DIRECT_SOURCE_MECHANICS_TARGET_Pu = 366.767829 kN
CASE21_FORMAL_ZERO_QUADRATURE_NUMERIC_RELEASE = OPEN
FORMAL_T12_VALUES = NOT RELEASED
FORMAL_T12_DERIVATIVES = NOT RELEASED
FORMAL_Rq_RA_L3_SOLVE = NOT RUN
FORMAL_CASE21_Pu = NOT RELEASED
Z6_NEW_CALCULATION_UNDER_CURRENT_CLOSURE = NOT YET RUN
```

## Current 11:55 artifacts

- `current/case21/CASE21_FORMAL_ZERO_SPATIAL_STATUS_20260817_1155.md`
- `semantic_v2/10_governance/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_REFINEMENT__LOCK.md`
- `semantic_v2/20_theory/nc_rebar_panel/20260817_1155__NZSCCM__CASE21_STABLE_CONFORMAL_SOURCE_16_STATE_AND_SINGLE_DOMAIN_SEMIALGEBRAIC_PERIOD__THEORY.md`
- `semantic_v2/40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__REPRO.py`
- `semantic_v2/40_execution/common/20260817_1155__NZSCCM__CASE21_16_STATE_SEMIALGEBRAIC_PERIOD_RUNTIME_ATTEMPT__DEVELOPMENT_DENSE_SPECTRAL_T12_REPRO.py`
- `semantic_v2/00_index/20260817_1155__NZSCCM__PROJECT__CASE21_FORMAL_ZERO_SPATIAL_16_STATE_SEMIALGEBRAIC_PERIOD__SEMANTIC_INDEX.md`
