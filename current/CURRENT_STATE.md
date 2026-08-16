# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-17 01:15 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current controlling governance

`semantic_v2/10_governance/20260817_0100__NZSCCM__SOURCE_REGULAR_DAG_AND_FACTORISED_ALGEBRAIC_PERIOD__LOCK.md`

## Frozen backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1 = ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
R10 physical current operator = FROZEN
reinforcement before coupled solve = REQUIRED
membrane-stress redistribution = REQUIRED
General-D15 target philosophy = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Z6_BOUNDARY = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```

Formal infinite/high-order analytic representations are allowed. Direct production computation by enumerating thousands of analytic coefficients is prohibited.

## Source-level regularity result

The old rationalized `c0,c1` connection pole at `x=21/260` is a representation artifact. The physical principal matrix square root is regular there and its Sylvester derivative operator has condition number 1 in the retained prototype.

```text
OLD_RATIONALIZED_c0_c1_CONNECTION = RETIRED_AS_PRODUCTION_DIFFERENTIAL_REPRESENTATION
SOURCE_LEVEL_MATRIX_SQRT_PLUS_FRECHET/SYLVESTER = RETAIN
TRUE_FOSTER_KNOTS = RETAIN_AS_SOURCE MATERIAL EVENTS
```

The source spline positive-part terms are retained in projector-free form

```text
D_+^p=((D+sqrt(D^2))/2)^p, p=3,4,5
```

with consistent tangent from finite divided differences/Frechet derivatives.

## Real target preflight

The actual compression interaction subtarget

```text
Yc=det(C)*Cyy
```

is an exact degree-4 algebraic target in the retained smooth four-state field. This establishes real-target compact algebraicity.

Explicit canonical rational annihilator generation in the present SymPy representation exceeded the fail-fast runtime and is rejected as a production architecture. The target remains factorized as an algebraic-period/descriptor object.

## New 01:15 full-Syy result: 64 is not the required branchwise runtime size

The two exact source knots are thresholds of functions of the same symmetric 2x2 strain matrix `E`. Their spectral projectors therefore share the same principal-value gap radical

```text
g=sqrt((tr E)^2-4 det E)
```

because

```text
(tr(E-lambda I))^2-4 det(E-lambda I)
= (tr E)^2-4 det E
```

for every threshold `lambda`.

The smooth R10 field has dimension <=4. A one-principal-value-active source-knot correction adds at most the single shared `g` extension. Therefore every exact source branch of the full R10 stress lies in

```text
B8=[1,q,s,q*s,g,q*g,s*g,q*s*g]
branchwise field dimension <= 8
```

rather than requiring an independent four-state tower for each knot.

This was executed on the complete retained prototype chain

```text
Pi(E),Pi(-E)
 -> c,t,C
 -> uR low/middle/high source branch
 -> T,U
 -> CH b7,b8
 -> complete Syy
```

with exact field support:

```text
uR low/middle/high = 4 / 8 / 8
Syy low/middle/high = 4 / 8 / 8
```

Observed complete `Syy` factor-graph assembly times were approximately `.85 / 1.05 / .96 s` in the retained Python/SymPy prototype without any high-order material series.

## Meaning of the historical 64-state result

```text
64_STATE = valid global branch-free closure bound
8_STATE  = current branch-aware exact full-Syy runtime bound
```

The 64-state result is not revoked; it remains the branch-free algebraic closure proof. The new 8-state result shows that exact source-knot resolution can substantially reduce production state size.

## Thickness material-event bound

At fixed `(X,Y)`, through-thickness strain is affine:

```text
E(zeta)=Em+zeta Eb
```

For either exact source threshold, the event equation

```text
det(E(zeta)-lambda_m I)=0
```

is quadratic in `zeta`. Therefore the two source thresholds create at most four exact thickness material events.

These are source events, not spatial cells; formal spatial/thickness subdomain count remains one.

## Critical downstream feedback before choosing production representation

The event-resolved 8-state form is locally much smaller, but its exact event roots

```text
zeta_m=zeta_m(X,Y)
```

may become variable algebraic endpoints passed to the later `(X,Y)` contraction.

Therefore the project must not choose the locally smallest thickness representation blindly.

Two exact candidates remain to be compared on an actual `P/Rm` target:

```text
A. global positive-part / factorised period form
   - larger local algebraic closure bound
   - hides event endpoints from XY layer

B. event-resolved <=8-state period form
   - much smaller thickness branch field
   - may expose algebraic zeta_m(X,Y) to XY layer
```

## Current unique next task

`ACTUAL_P_RM_THICKNESS_TO_XY_INTERFACE_COMPACTNESS_GATE`

Execute one actual `P` or `Rm` target through the thickness-to-XY interface under both exact representations where practical, and compare:

```text
1. resulting finite descriptor/state dimension;
2. whether variable knot roots are exposed explicitly;
3. algebraic/holonomic order delivered to the XY moment operator;
4. consistent derivative complexity;
5. whether the combined thickness+XY route retains a fixed finite bound.
```

Choose the production representation by combined end-to-end complexity, not by thickness complexity alone.

Do not compute new Pu until this interface is closed.

## Capacity status

```text
Case21 320.749185 kN = RETRACTED DIAGNOSTIC ONLY
Z6 43.762840 MN = RETRACTED DIAGNOSTIC ONLY
Case21 retained support baseline = 368.189 kN
Z6 retained engineering support baseline = 51.30 MN
NEW_CORRECTED_MEMBRANE_REDISTRIBUTED_Pu = NOT RELEASED
```

## Current artifacts

- `semantic_v2/40_execution/common/20260817_0100__NZSCCM__SOURCE_LEVEL_REGULARIZATION_AND_REAL_TARGET_PREFLIGHT__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260817_0100__NZSCCM__SOURCE_LEVEL_REGULARIZATION_AND_REAL_TARGET_PREFLIGHT__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260817_0100__NZSCCM__SOURCE_LEVEL_REGULARIZATION_AND_REAL_TARGET_PREFLIGHT__REPRO.py`
- `semantic_v2/10_governance/20260817_0100__NZSCCM__SOURCE_REGULAR_DAG_AND_FACTORISED_ALGEBRAIC_PERIOD__LOCK.md`
- `semantic_v2/40_execution/common/20260817_0115__NZSCCM__FULL_SYY_BRANCH_AWARE_8_STATE_REDUCTION__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260817_0115__NZSCCM__FULL_SYY_BRANCH_AWARE_8_STATE_REDUCTION__PARAMS_AND_INTERMEDIATES.json`
