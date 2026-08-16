# NZ-SCCM current state — R10-MSAC-RC1 material-level multiscale reconnection pass

**Timestamp:** 2026-08-16 17:34 +08:00

## Current status

The 17:20 parameter-derived-domain correction remains active. The historical R3/R4/R5 multiscale/source-landmark compiler architecture has now been reconnected to those specimen-derived domains as the deterministic reconstruction candidate:

```text
R10-MSAC-RC1
```

R10 physical current material physics remains unchanged.

## Material-level result

One common RC1 rule set was applied to Z0-Z6:

```text
zero-gate source lens derived from specimen guard and lambda=0
compression compiled in natural c coordinate
tension lenses derived from xcr and 10*xcr source landmarks
U reassembled from c,t,C,uR rather than independently fitted
exact origin C1 constraints
same full-2D source stress/tangent/divided-difference gates
same resolution ladder
first pass + next level confirmation
```

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

Worst first-pass source metrics:

```text
max E_sigma = .0008861083
max E_tangent = .0379151680
max E_divided_difference = .0221037356
```

All pass the existing `.005/.05/.05` material gates. Every next ladder level also passes.

Relative to the one-global-lambda baseline on the same corrected domains, finite scalar coefficient count is reduced by approximately `3.17x` to `4.61x`.

## Structural boundary

RC1 is **not** yet a fully promoted production structural compiler.

The beta-lens/Chebyshev factor graph must remain nested. Naive ordinary-polynomial expansion would inflate first-pass degrees into approximately `6656-29952`, recreating the historical expression-swell route.

Therefore:

```text
R10_MSAC_RC1_MATERIAL_LEVEL = PASS_Z0_Z6
FULL_MONOMIAL_EXPANSION = PROHIBITED
NESTED_FACTOR_GRAPH = REQUIRED
NESTED_GENERAL_D15_TARGET_FUNCTIONAL_ADAPTER = OPEN
NEW_Z0_Z6_PRODUCTION_Pu = NOT_RUN
```

## Current unique next gate

```text
UNIFIED_V1_R10_MSAC_RC1_NESTED_CLENSHAW_QNM_D15_CONTRACTION_GATE
```

It must directly connect the finite RC1 factor graph to the historical Qnm / adjoint-Clenshaw moment-first General-D15 target contractions, without expanding the full spatial stress field and without any structural spatial quadrature.

## Key artifacts

- `../10_governance/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION_GATE__LOCK.md`
- `../40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__EXECUTION_REPORT.md`
- `../40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__PARAMS_AND_INTERMEDIATES.json`
- `../40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__REPRO.py`
- `../60_validation/common/20260816_1734__NZSCCM__R10_MSAC_RC1_SOURCE_FIDELITY_AND_COMPLEXITY__AUDIT.md`
- `20260816_1720__NZSCCM__PROJECT__CURRENT_STATE_PARAMETER_DERIVED_DOMAIN_GATE_RESULT__SEMANTIC_INDEX.md` — predecessor
