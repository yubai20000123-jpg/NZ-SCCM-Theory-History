# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_1932__NZSCCM__PROJECT__CURRENT_STATE_RC1_ADJOINT_TARGET_PREFLIGHT_FAIL__SEMANTIC_INDEX.md`

## Frozen production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
R10 source current material operator
reinforcement/steel phase before root solve
same-state current stress + consistent tangent
Cayley-Hamilton / approved finite matrix lift
General-D15 exact target moments
P,Rq,L connected-branch topology
same-state material + geometric KZ
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Five-term membrane model retained

Global production remains `(D,q)`. Compatible membrane redistribution uses finite internal coordinates

```text
r=[r0,r20,r22,s02,s22]
```

with current equilibrium `Rm=0` and consistent Schur condensation. The exact elastic Airy/FvK recovery and General-D15 target closure remain PASS.

## R10-MSAC-RC1 material status

`R10-MSAC-RC1` remains material-level source-fidelity PASS for Z0-Z6. Its nested factor graph is retained and full monomial expansion remains prohibited.

## 19:32 adjoint target gate

The adjoint/transpose Clenshaw algebra was implemented and verified exactly against a low-order nested beta/Chebyshev D15 example:

```text
final nested degree = 192
DIRECT_MINUS_ADJOINT = 0 exactly
functional/pi = .11633931515896061
```

However the contributing target kernels reached degrees `65,129,193`; adjoint Clenshaw changes recurrence direction but does not remove nested composition degree unless multiplication by the nested atom has a direct closed moment rule.

Active RC1 composition preflight gives `DuR/DT7` from about `7.16e7` to `5.69e8` and nominal TT total-degree scale up to `1.708e9` for Z6. These are diagnostics, not production orders. They show that resolving the nested target back into ordinary polynomial General-D15 leaves recreates expansion swell.

```text
ADJOINT_CLENSHAW_ALGEBRA = PASS_EXACT
LOW_ORDER_GENERAL_D15_TARGET_IDENTITY = PASS_EXACT
RC1_NESTED_ATOM_CLOSED_MOMENT_RULE = ABSENT
ACTIVE_RC1_STRUCTURAL_TARGET_RUNTIME = FAIL_PREFLIGHT
NEW_Pu = NOT_RUN
```

This structural failure does not revoke the RC1 material source-fidelity pass and does not change the R10 physical law.

## Capacity boundary

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
Z0-Z5 old values = retracted/diagnostic under current governance
NEW membrane-redistributed Pu = not released
```

## Current next gate

```text
UNIFIED_V1_NC_EXACT_NESTED_ATOM_MOMENT_CLOSURE_OR_STRUCTURALLY_CLOSED_COMPILER_REDESIGN_GATE
```

The next route must either derive a true exact moment transform for RC1 nested atoms or redesign the NC analytic compiler, without changing R10 physics, into a source-faithful basis whose structural target moments close directly through General-D15/CAS/special-function algebra. Repeating forward/adjoint ordinary polynomial Clenshaw without such a closure is not a new route.

## Repository semantic read order

1. `20260816_1932__NZSCCM__PROJECT__CURRENT_STATE_RC1_ADJOINT_TARGET_PREFLIGHT_FAIL__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1932__NZSCCM__RC1_ADJOINT_TARGET_FAILURE_AND_NEXT_CLOSURE__GATE_LOCK.md`
3. `../20_theory/nc_rebar_panel/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_CLOSURE__THEORY.md`
4. `../40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__EXECUTION_REPORT.md`
5. `../40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__PARAMS_AND_INTERMEDIATES.json`
6. `../40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__REPRO.py`
7. `../60_validation/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__AUDIT.md`
8. `20260816_1912__NZSCCM__PROJECT__CURRENT_STATE_FIVE_TERM_MEMBRANE_CONDENSATION_PARTIAL_PASS__SEMANTIC_INDEX.md` — predecessor
9. `20260816_1734__NZSCCM__PROJECT__CURRENT_STATE_R10_MSAC_RC1_MATERIAL_PASS__SEMANTIC_INDEX.md` — compiler predecessor

No legacy file is deleted, moved or renamed solely from filename identity.
