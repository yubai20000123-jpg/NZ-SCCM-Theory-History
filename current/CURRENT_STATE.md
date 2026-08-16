# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 17:20 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_1720__NZSCCM__PROJECT__CURRENT_STATE_PARAMETER_DERIVED_DOMAIN_GATE_RESULT__SEMANTIC_INDEX.md`

## Frozen project-wide production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1 = ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
source current material operator = REQUIRED
same-state current stress + consistent current tangent = REQUIRED
Cayley-Hamilton / approved finite matrix lift = ACTIVE
General D15 moment-first exact moments = ACTIVE
P,Rq,L connected-branch topology = ACTIVE
same-state material + geometric KZ audit = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Gauss/Simpson/adaptive/collocation/material-point-grid = PROHIBITED
experiment/Zhou/Winter calibration in solve/compiler = PROHIBITED
```

## Unified workflow clarification retained

Unified workflow means one governing rule set, not identical numerical boundary/domain values for all specimens.

For specimen `i`, a common source/design-side reachability rule generates

\[
\Lambda_i=\mathcal B(\text{geometry}_i,\text{physical boundary}_i,\text{halfwave}_i,\theta_{m,i},\text{declared generalized-coordinate bounds}).
\]

The same material-family compiler policy and source-value/tangent/divided-difference gates are then applied on `Lambda_i`.

```text
same rule + different specimen parameters -> different domains/orders = ALLOWED
case label / Pu error / experiment -> special domain/order = PROHIBITED
```

## 17:20 parameter-derived-domain gate — executed

For the current Zhou AR2 Z0-Z6 set:

```text
boundary = theoretical four-edge SSSS/Navier
m*=2
ell=b
q0=.004
D in [0,2]
q_post=(tc/b)*sqrt(max(Pyth/Pcr-1,0)/kp)
kp=3*(1-nu^2)/8
q_max=1.25*max(q0,q_post)
```

`D_max=2` and the 25% amplitude/domain guards are project-level source/design-side search-envelope rules, not capacity calibration. If a future connected branch hits a declared generalized-coordinate bound before a valid first limit point, the same bound-expansion rule is rerun and the compiler/domain is regenerated before acceptance.

The continuous material spectrum is bounded analytically, with no spatial sampling, using the rank-one positive membrane structure plus the bounded bending operator.

Generated certified cores:

```text
Z0 [-2.326966,+.398162]
Z1 [-2.246565,+.304377]
Z2 [-2.326966,+.398162]
Z3 [-2.241404,+.293969]
Z4 [-2.385927,+.469962]
Z5 [-2.980899,+1.194486]
Z6 [-2.768805,+2.128027]
```

All previously stored diagnostic/engineering envelopes lie inside these domains; those old states were checked only after generation and did not generate the bounds.

## Same baseline compiler convergence on each derived domain

The former wide single-global-lambda Chebyshev grammar was retained only as a common baseline screen:

```text
channels=U,C,T,T7
M=8*(N+1) material-coordinate projection nodes
exact C1 zero anchors
E_sigma<=.005
E_tangent<=.05
E_divided_difference<=.05
same order sequence for every specimen
```

First passing orders:

```text
Z0 N=1792
Z1 N=1536
Z2 N=1792
Z3 N=1536
Z4 N=1792
Z5 N=3072
Z6 N=3840
```

Hence:

```text
PARAMETER_DERIVED_DOMAIN_RULE = PASS
OLD_IDENTICAL_FAMILY_WIDE_PRODUCTION_DOMAIN = RETIRED
N3584_FAMILY_WIDE_RESULT = RETAINED_DIAGNOSTIC_ONLY
SINGLE_GLOBAL_LAMBDA_POLYNOMIAL_LOW_COMPLEXITY = FAIL
R10_PHYSICAL_OPERATOR = UNCHANGED
```

The governance correction was necessary but does not by itself make one-global-lambda polynomial compilation a low-order theory. The persistent Z5/Z6 order confirms that the next step must address representation architecture, not force identical domains and not immediately modify R10 physics.

## Retained exact-Pi diagnostic

The 14:17 exact-`Pi_eta` elliptic-period result remains mathematically valid, but it is not the current mandatory next route.

```text
EXACT_PI_MATRIX_LIFT = PASS
EXACT_PI_TO_EXISTING_GENERAL_D15 = FAIL
PI_REGULARIZATION_AS_MANDATORY_NEXT_TASK = CANCELLED
```

## Capacity-result status

```text
Z6_AR2_Pu = 51.30 MN  # retained user-accepted engineering baseline only
Z6_UNIFIED_RERUN = NOT COMPLETED
Z0_Z5_20260816_1043_Pu = RETRACTED
Z0_Z5_20260816_1248_LOCATORS = DIAGNOSTIC_ONLY
NEW_Z0_Z6_PRODUCTION_Pu = NOT RELEASED
SAME_EXPRESSION_L = NOT COMPLETED
SAME_STATE_KZ = NOT COMPLETED
```

## Current unique next gate

```text
UNIFIED_V1_PARAMETER_DERIVED_DOMAIN_PLUS_HISTORICAL_MULTISCALE_COMPILER_RECONNECTION_GATE
```

Required next work:

1. keep the corrected specimen-derived domains/source-side domain rule;
2. reconnect the historical R5/MSAC/source-landmark multiscale compiler and G26 moment-first contraction lessons;
3. build one common NC multiscale analytic compiler policy whose numerical coefficients/orders may vary only through the same specimen-derived domain and source landmarks;
4. retain source stress/tangent/divided-difference gates;
5. retain zero formal spatial/thickness numerical integration and General-D15 compatibility;
6. do not use case labels, experiment, Zhou/Winter or desired Pu to choose maps/orders;
7. do not modify R10 or Pi_eta unless this corrected multiscale compiler gate independently fails.

## Current key artifacts

- `semantic_v2/10_governance/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER_GATE__LOCK.md`
- `semantic_v2/40_execution/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER__REPRO.py`
- `semantic_v2/60_validation/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_GLOBAL_COMPILER__AUDIT.md`
- `semantic_v2/00_index/20260816_1720__NZSCCM__PROJECT__CURRENT_STATE_PARAMETER_DERIVED_DOMAIN_GATE_RESULT__SEMANTIC_INDEX.md`
