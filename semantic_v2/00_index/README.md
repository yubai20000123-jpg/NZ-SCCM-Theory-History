# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_1734__NZSCCM__PROJECT__CURRENT_STATE_R10_MSAC_RC1_MATERIAL_PASS__SEMANTIC_INDEX.md`

## Current locked production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
source current material operator
same-state current stress + consistent current tangent
Cayley-Hamilton / approved finite matrix lift
moment-first General-D15 exact structural moments
P,Rq,L connected-branch primary limit root
same-state material + geometric tangent/stability audit
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
structural calibration = NO
```

## Unified workflow/domain rule

One common source/design-side rule derives each specimen's reachable material domain from its own geometry, boundary, complete halfwave, material parameters and declared generalized-coordinate bounds. Different numerical domains/orders are allowed only as deterministic outputs of this common rule.

## 17:34 R10-MSAC-RC1 material-level result

The historical R3/R4/R5 multiscale/source-landmark architecture has been reconnected to the corrected Z0-Z6 domains as `R10-MSAC-RC1`.

First passing levels:

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

All pass the frozen material gates, and the immediately higher common-ladder level also passes for every specimen.

Compared with the corrected one-global-lambda baseline, finite scalar coefficient count falls by approximately `3.17x` to `4.61x`.

```text
R10_PHYSICAL_OPERATOR = UNCHANGED
R10_MSAC_RC1_MATERIAL_LEVEL = PASS_Z0_Z6
FULL_MONOMIAL_EXPANSION = PROHIBITED
NESTED_FACTOR_GRAPH = REQUIRED
NESTED_GENERAL_D15_TARGET_FUNCTIONAL_ADAPTER = OPEN
NEW_Z0_Z6_PRODUCTION_Pu = NOT_RUN
```

## Current next gate

```text
UNIFIED_V1_R10_MSAC_RC1_NESTED_CLENSHAW_QNM_D15_CONTRACTION_GATE
```

The next step must connect RC1 directly to the historical `Q_nm` / adjoint-Clenshaw moment-first General-D15 target contractions while keeping the compiler nested. No giant ordinary-polynomial expansion and no structural spatial numerical quadrature are permitted.

## Repository semantic read order

1. `20260816_1734__NZSCCM__PROJECT__CURRENT_STATE_R10_MSAC_RC1_MATERIAL_PASS__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION_GATE__LOCK.md`
3. `../40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__EXECUTION_REPORT.md`
4. `../40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__PARAMS_AND_INTERMEDIATES.json`
5. `../40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__REPRO.py`
6. `../60_validation/common/20260816_1734__NZSCCM__R10_MSAC_RC1_SOURCE_FIDELITY_AND_COMPLEXITY__AUDIT.md`
7. `20260816_1720__NZSCCM__PROJECT__CURRENT_STATE_PARAMETER_DERIVED_DOMAIN_GATE_RESULT__SEMANTIC_INDEX.md` — predecessor
8. `../20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`

No legacy file is deleted, moved or renamed solely from filename identity.
