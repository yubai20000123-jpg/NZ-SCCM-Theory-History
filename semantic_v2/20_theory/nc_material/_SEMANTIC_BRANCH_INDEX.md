# NC material semantic branch

## Current material target

- R10 physical current material target remains **CURRENT_SUPPORT / FROZEN**.
- Governing project workflow is `UNIFIED_PRODUCTION_WORKFLOW_V1`.
- Production material domains are specimen-parameter-derived under one common source/design-side rule.

## Retained global-polynomial diagnostics

The earlier family-wide/global-lambda screens remain useful as source-representability diagnostics, not as the desired NC production grammar.

On the corrected specimen-derived domains, the first passing single-global-lambda orders were:

```text
Z0 1792
Z1 1536
Z2 1792
Z3 1536
Z4 1792
Z5 3072
Z6 3840
```

Thus the fixed common-domain governance error was corrected, but one global lambda polynomial remained too high-order.

## Retained intrinsic/exact-Pi diagnostics

The 13:55 intrinsic-coordinate screen showed that R10 is much lower-complexity in natural material coordinates. The 14:17 exact-Pi calculation established that exact `Pi_eta` leaves the present finite Beta/Gamma General-D15 closure even in a simple trigonometric witness.

Those results remain mathematically valid, but no R10/eta regularization is currently authorized or required.

## 17:34 R10-MSAC-RC1 multiscale reconnection

Current governance/execution:

- `../../10_governance/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION_GATE__LOCK.md`
- `../../40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__EXECUTION_REPORT.md`
- `../../40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260816_1734__NZSCCM__R10_MSAC_RC1_MULTISCALE_RECONNECTION__REPRO.py`
- `../../60_validation/common/20260816_1734__NZSCCM__R10_MSAC_RC1_SOURCE_FIDELITY_AND_COMPLEXITY__AUDIT.md`

`R10-MSAC-RC1` is a current deterministic reconstruction of the historical R3/R4/R5 multiscale principles. It is not claimed to be bitwise identical to an older NC-MSAC-v1 executable.

Common factor graph:

```text
specimen-derived lambda guard
 -> finite beta-lens gate around lambda=0
 -> c(lambda), t(lambda)
 -> C(c) in natural compression coordinate
 -> uR(t), T7(t) using xcr and 10*xcr source landmarks
 -> T=uR/rho
 -> U reassembled from the same factors
 -> full 2D R10 current master
```

The map-generation rule, rational-center denominator limit, source landmarks, origin C1 constraints, source-fidelity gates and resolution ladder are common to all Z0-Z6 specimens.

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

Worst first-pass metrics:

```text
max E_sigma = .0008861083
max E_tangent = .0379151680
max E_divided_difference = .0221037356
```

All pass the current material gates. Each first-pass candidate is also confirmed by a passing next ladder level.

The finite scalar coefficient count is approximately `3.17x` to `4.61x` smaller than the corrected one-global-lambda baseline.

## Meaning of “same NC method”

All NC specimens share:

```text
R10 source operator
parameter-derived domain law
RC1 source-landmark map-generation rule
source stress/tangent/divided-difference gates
common resolution ladder and first-pass rule
downstream Nguyen/membrane/D15/P-Rq-L/KZ mechanics
```

Numerical domains, lens indices and converged orders may differ only because the same rules receive different specimen/source parameters.

Not allowed:

```text
case label -> manual interval/order/map
observed Pu error -> compiler change
experiment/Zhou/Winter -> domain/order/map selection
Z6-only fallback solver
```

## Structural compiler boundary

RC1 is currently **material-level passing**, not yet fully promoted for structural production.

The nested beta-lens/Chebyshev representation must not be expanded into ordinary monomials. Naive full expansion would raise first-pass ordinary-polynomial degrees into approximately `6656-29952`.

```text
R10_MSAC_RC1_MATERIAL_LEVEL = PASS_Z0_Z6
FULL_MONOMIAL_EXPANSION = PROHIBITED
NESTED_FACTOR_GRAPH = REQUIRED
NESTED_GENERAL_D15_TARGET_FUNCTIONAL_ADAPTER = OPEN
```

## Common mechanics inherited by every NC specimen

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
NGUYEN_SECOND_ORDER
MEMBRANE_STRESS_REDISTRIBUTION
CURRENT_STRESS + CONSISTENT_CURRENT_TANGENT
CAYLEY_HAMILTON / APPROVED FINITE MATRIX LIFT
MOMENT_FIRST_GENERAL_D15
ZERO_FORMAL_SPATIAL_AND_THICKNESS_QUADRATURE
COMMON_P_Rq_L_CONNECTED_BRANCH_LIMIT
SAME_STATE_MATERIAL_PLUS_GEOMETRIC_KZ
```

## Current numerical result boundary

```text
Z6 51.30 MN = RETAINED ENGINEERING BASELINE ONLY
Z0-Z5 10:43 Pu = RETRACTED
Z0-Z5 12:48 values = DIAGNOSTIC LOCATORS ONLY
NEW Z0-Z6 PRODUCTION Pu = NOT RELEASED
```

## Current next gate

```text
UNIFIED_V1_R10_MSAC_RC1_NESTED_CLENSHAW_QNM_D15_CONTRACTION_GATE
```

The next task is to connect the RC1 factor graph directly to the historical `Q_nm` / adjoint-Clenshaw target-functional General-D15 contraction, preserving the nested basis and zero structural spatial integration. No full monomial expansion is permitted.
