# NC + rebar panel theory semantic branch

## Current end-to-end production-development identity

The current mainline remains a **single Case21 end-to-end formal calculation**, not a sequence of newly created project tasks:

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

Current path:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
 -> Nguyen second-order continuous strain
 -> Airy-compatible scalar membrane redistribution r=lambda*M*a(nu)
 -> same-state frozen R10 concrete + reinforcement
 -> regular source/matrix material DAG
 -> global fixed-endpoint compact algebraic period
 -> finite T12 / XY target contraction
 -> low-dimensional connected (D,q,lambda) solve
 -> Rq=0, RA=0, L3=0
 -> formal Case21 Pu
```

The final formal solve is currently blocked only because the executable fixed-endpoint algebraic-period numeric runtime is not yet implemented. The `T12 fixed-endpoint descriptor` is an internal implementation layer of this same end-to-end task, not a new physical route.

## Formal counters

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## Frozen physics

```text
R10 physical current operator = FROZEN
reinforcement before solve = REQUIRED
Airy-scalar r=lambda*M*a(nu) = ACTIVE
five-free nonlinear Rm relaxation = REJECTED
Z6 analytical boundary = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```

## Case21 load identities

```text
Pcr_exp = 336.285554 kN   # buckling only
Pf_exp  = 368.312750 kN   # failure / ultimate
```

Cross-comparison is prohibited.

## Mechanics qualification retained

Exact restricted-coordinate residual transformation:

```text
R_lambda = M*RA
Rq_restricted = Rq_base + lambda*Mq*RA
```

Pure isotropic continuum benchmark:

```text
lambda=1 exactly
```

Actual reinforced linear scalar benchmark for Case21:

```text
lambda_lin_RC = 0.999266844854884
              + 0.0096124785693025*D/M
```

Scalar internal stability criterion:

```text
dRA/dlambda > 0
```

At the current direct-source peak:

```text
dRA/dlambda = +25.24850924
M*dRA/dlambda = +0.733982616
```

so no scalar internal membrane instability is found before the current mechanics peak.

## Current direct-source mechanics oracle

```text
D = 0.7887924801
q = 0.0018083573
lambda = 0.0862359635
M = 0.02907033478
Pc = 337.923030 kN
Ps = 28.844798 kN
Pu = 366.767829 kN
Pf_exp = 368.312750 kN
error = -0.419459 %
```

This is an audit/mechanics oracle only, not a formal zero-spatial numeric release.

## Source regularity and algebraic state identities

The old rationalized `c0,c1` pole at `x=21/260` is a representation artifact. Production remains at source/matrix level through Fréchet/Sylvester differentiation.

```text
64_STATE = valid global branch-free algebraic closure bound
8_STATE  = exact branch-aware full-R10 stress bound on fixed event topology
```

The 8-state form remains local exact/audit only because source-knot event topology changes over `(X,Y)`.

## Production thickness representation

```text
GLOBAL_FIXED_ENDPOINT_POSITIVE_PART_FACTORISED_PERIOD = PRODUCTION
EVENT_RESOLVED_8_STATE = LOCAL_EXACT/AUDIT ONLY
```

Fixed physical thickness endpoints:

```text
zeta=-1,+1
```

No moving event fronts are promoted to formal XY subdomains.

## Current T12 structural contract

The Airy-scalar concrete value interface is the fixed 12-functional package

```text
Jx00, Jx20, Jx02, Jx22c,
Jy00, Jy20, Jy02, Jy22c,
Jxy22s,
Jx11s_1, Jy11s_1, Jxy11c_1
```

which feeds exactly

```text
Pc
RAc
Rqc
```

without reconstructing a full stress surface.

Finite thickness family:

```text
stress moments  : k=0,1
tangent kernels : k=0,1,2
```

## 11:26 descriptor execution status

Compact pointwise R10 identity against the direct frozen source:

```text
max abs physical stress mismatch = 7.11e-15 MPa
COMPACT_SOURCE_R10 = PASS
```

Independent 128x128x68 audit of the T12 contract at the current peak reconstructs

```text
P  = 366.767769971 kN
Rq = +7.34325e-5
RA = +9.46701e-5
```

and the T12 audit Jacobian gives

```text
dP/dD along equilibrium branch = -0.008393 kN
```

near zero at the independently refined direct-source peak.

Therefore:

```text
T12_VALUE_CONTRACT = PASS_AUDIT
T12_DERIVATIVE_CONTRACT = PASS_AUDIT
```

## Current true blocker

The mathematical compact representation is retained, but the repository does not yet contain an executable production routine that maps

```text
(D,q,lambda)
 -> source-regular fixed-endpoint algebraic periods
 -> formal T12 + same-source derivatives
```

without prohibited fallback mechanisms.

```text
FORMAL_FIXED_ENDPOINT_ALGEBRAIC_PERIOD_NUMERIC_RUNTIME = NOT IMPLEMENTED / BLOCKING
FORMAL_CASE21_Rq_RA_L3_SOLVE = NOT RUN
FORMAL_CASE21_Pu = NOT RELEASED
```

This is an implementation/runtime gap, not a mechanics failure or a T12 failure.

## Prohibited regressions

```text
NO XY EVENT-TOPOLOGY CELLS/SUBDOMAINS
NO MATERIAL-POINT GRID/HISTORY
NO GAUSS/SIMPSON/ADAPTIVE PRODUCTION INTEGRATION
NO N1000/N3000/N5000 COEFFICIENT ENUMERATION
NO EXPLICIT 64-RATIONAL-COEFFICIENT CANONICALIZATION AS PRODUCTION REQUIREMENT
NO N48 FALLBACK AS FIX FOR COMPACT-EXACT BLOCKERS
NO AUTOMATIC NEW CAS/BACKEND CHAIN
```

## Current artifacts

- `../../10_governance/20260817_1126__NZSCCM__CASE21_FORMAL_ZERO_SPATIAL_CONTINUATION_NO_TASK_PROLIFERATION__LOCK.md`
- `20260817_1126__NZSCCM__CASE21_T12_FIXED_ENDPOINT_DESCRIPTOR_FORM_AND_RUNTIME_BOUNDARY__THEORY.md`
- `../../40_execution/common/20260817_1126__NZSCCM__CASE21_T12_FIXED_ENDPOINT_DESCRIPTOR_ATTEMPT__EXECUTION_REPORT.md`
- `../../40_execution/common/20260817_1126__NZSCCM__CASE21_T12_FIXED_ENDPOINT_DESCRIPTOR_ATTEMPT__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260817_1126__NZSCCM__CASE21_T12_FIXED_ENDPOINT_DESCRIPTOR_ATTEMPT__REPRO.py`

## Current status

```text
CURRENT_END_TO_END_TASK = CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
STATUS = BLOCKED_AT_FIXED_ENDPOINT_ALGEBRAIC_PERIOD_NUMERIC_RUNTIME
NEW_PROJECT_TASK_CREATED = NO
ROUTE_CHANGED_DUE_TO_USER_QUESTION = NO
```
