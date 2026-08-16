# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 17:34 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_1734__NZSCCM__PROJECT__CURRENT_STATE_R10_MSAC_RC1_MATERIAL_PASS__SEMANTIC_INDEX.md`

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

## Unified workflow/domain rule

Unified workflow means one common governing rule set, not one identical numerical boundary/domain/order for all specimens.

For specimen `i`, the common source/design-side reachability rule generates its certified material domain from geometry, physical/source boundary, selected complete halfwave, material parameters and declared generalized-coordinate bounds. The same material-family compiler policy and source-fidelity gates are then applied.

```text
same rule + different specimen parameters -> different domains/orders = ALLOWED
case label / Pu error / experiment -> special domain/order = PROHIBITED
```

The 17:20 parameter-derived domains remain active:

```text
Z0 [-2.326966,+.398162]
Z1 [-2.246565,+.304377]
Z2 [-2.326966,+.398162]
Z3 [-2.241404,+.293969]
Z4 [-2.385927,+.469962]
Z5 [-2.980899,+1.194486]
Z6 [-2.768805,+2.128027]
```

## R10 source identity

R10 ordinary-concrete current material physics remains frozen and unchanged.

The old single-global-lambda baseline on the specimen-derived domains required first passing orders:

```text
Z0 1792
Z1 1536
Z2 1792
Z3 1536
Z4 1792
Z5 3072
Z6 3840
```

This remains a source-representability baseline only, not the preferred production grammar.

## 17:34 historical multiscale reconnection — R10-MSAC-RC1

The historical R3/R4/R5 architecture has been reconnected to the corrected specimen-derived domains as the deterministic current reconstruction candidate:

```text
R10-MSAC-RC1
```

RC1 means a current reconstruction of the historical multiscale principles, not a claim of bitwise identity with an old NC-MSAC-v1 executable.

Common architecture:

```text
lambda guard
 -> finite beta-lens gate around lambda=0
 -> c(lambda), t(lambda)
 -> C(c) in natural compression coordinate
 -> uR(t), T7(t) using xcr and 10*xcr source landmarks
 -> T=uR/rho
 -> U reassembled from the same factors
 -> full 2D R10 current master
```

The same map-generation rule, source landmarks, origin constraints, fidelity gates and resolution ladder are used for Z0-Z6.

First passing material levels:

```text
Z0 L2: Ng=512,  Nc=14, Nt=256, coeff=1555
Z1 L3: Ng=640,  Nc=14, Nt=320, coeff=1939
Z2 L2: Ng=512,  Nc=14, Nt=256, coeff=1555
Z3 L2: Ng=512,  Nc=14, Nt=256, coeff=1555
Z4 L2: Ng=512,  Nc=14, Nt=256, coeff=1555
Z5 L6: Ng=1024, Nc=14, Nt=512, coeff=3091
Z6 L7: Ng=1152, Nc=16, Nt=576, coeff=3477
```

Worst first-pass source errors:

```text
max E_sigma = .0008861083
max E_tangent = .0379151680
max E_divided_difference = .0221037356
```

All pass the frozen `.005/.05/.05` material gates. The immediately higher common-ladder level also passes for every specimen.

Compared with the single-global-lambda baseline, scalar coefficient count is reduced by approximately `3.17x` to `4.61x`.

## Important structural boundary

R10-MSAC-RC1 is currently a **material-level passing candidate**, not yet a fully promoted structural production compiler.

The finite beta-lens/Chebyshev object must remain nested. Expanding it into ordinary monomials would inflate first-pass formal degrees to roughly `6656-29952`, recreating the historical expression-swell failure.

```text
R10_MSAC_RC1_FULL_2D_SOURCE_FIDELITY = PASS_Z0_Z6
NEXT_LEVEL_CONFIRMATION = PASS_Z0_Z6
FULL_MONOMIAL_EXPANSION = PROHIBITED
NESTED_FACTOR_GRAPH = REQUIRED
NESTED_GENERAL_D15_TARGET_FUNCTIONAL_ADAPTER = OPEN
```

The old exact-Pi elliptic-period result remains a valid mathematical diagnostic but does not control the current route. No R10/eta transition regularization has been authorized or executed.

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

No new `Pu` was run in the 17:34 material gate.

## Current unique next gate

```text
UNIFIED_V1_R10_MSAC_RC1_NESTED_CLENSHAW_QNM_D15_CONTRACTION_GATE
```

Required next work:

1. keep RC1 factor graph and parameter-derived specimen domains unchanged;
2. reconnect the historical `Q_nm` / adjoint-Clenshaw target-functional moment-first contraction;
3. do not expand the nested compiler into a giant ordinary polynomial;
4. preserve zero formal spatial/thickness numerical integration;
5. verify nested algebra identity and fixed-state D15 tractability before any new Pu solve;
6. after the adapter passes, use the same backend for `P,Rq,L` and same-state `KZ`.

## Current key artifacts

- `semantic_v2/10_governance/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION_GATE__LOCK.md`
- `semantic_v2/40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__REPRO.py`
- `semantic_v2/60_validation/common/20260816_1734__NZSCCM__R10_MSAC_RC1_SOURCE_FIDELITY_AND_COMPLEXITY__AUDIT.md`
- `semantic_v2/00_index/20260816_1734__NZSCCM__PROJECT__CURRENT_STATE_R10_MSAC_RC1_MATERIAL_PASS__SEMANTIC_INDEX.md`
- `semantic_v2/40_execution/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER__EXECUTION_REPORT.md` — predecessor
