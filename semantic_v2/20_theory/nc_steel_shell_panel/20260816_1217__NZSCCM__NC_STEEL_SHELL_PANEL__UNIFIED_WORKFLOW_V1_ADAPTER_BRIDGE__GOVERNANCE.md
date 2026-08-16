# NC + steel-shell — unified workflow V1 adapter bridge

**Timestamp:** 2026-08-16 12:17 +08:00  
**Identity:** CURRENT BRANCH BRIDGE / NO NEW MATERIAL PHYSICS

This bridge aligns the existing concrete+steel-shell branch with project-wide `UNIFIED_PRODUCTION_WORKFLOW_V1` without deleting or rewriting the prior shell derivations.

## Common parent mechanics retained

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
MEMBRANE_STRESS_REDISTRIBUTION
R10 source current operator for NC
NC family compiler shared with NC+rebar after V1 freeze
Cayley-Hamilton / approved finite matrix lift
moment-first General-D15 exact moments
formal spatial quadrature = 0
formal thickness quadrature = 0
common P,Rq,L connected-branch primary limit root
same-state consistent material + geometric KZ audit
```

The former branch wording `N48-C1/MM compiler` is retained as historical/current-support implementation evidence, not as the final V1 family-compiler identity.

## Steel-shell adapter retained

The shell remains a bonded finite-thickness structural phase with exact analytic thickness treatment. It contributes

```text
P_sh
Rq_sh
same-expression derivatives
KZ_sh^mat
KZ_sh^geo
```

to the common parent system.

The shell may not cause the NC concrete compiler to differ from NC+rebar.

## Local shell buckling under V1

Where a source-grounded shell-local mode is physically active, its amplitude(s) are finite internal coordinates `a` with residuals `R_a=0`. They are handled by exact implicit differentiation/condensation:

```text
a_g = -R_aa^-1 R_ag
P_g_tilde = P_g + P_a a_g
Rq_g_tilde = Rq_g + Rq_a a_g
Kgg_cond = Kgg - Kga Kaa^-1 Kag
```

This is the allowed type-specific extension. It does not create a separate global solver or spatial discretization.

## Tangent requirement

The shell must use a source-approved plane-stress current operator and full consistent directional current tangent for production. Its material and current-stress geometric stiffness contributions are evaluated at the same current state as `P,Rq,L`.

A pre-buckling elastic tangent frozen after yielding/local-mode activation is prohibited.

## Current status

```text
NC_SOURCE_OPERATOR = R10_FROZEN
NC_FAMILY_COMPILER_UNDER_V1 = NOT_YET_FROZEN
STEEL_SHELL_STRUCTURAL_ADAPTER = CURRENT_SUPPORT
STEEL_SHELL_ZERO_SPATIAL_AND_THICKNESS_QUADRATURE = PASS_SUPPORT
STEEL_SHELL_2D_CURRENT_OPERATOR = SOURCE_FREEZE/PROMOTION MUST BE VERIFIED BEFORE PRODUCTION
Z0_Z6_UNIFIED_RERUN = PENDING_NC_COMPILER_FREEZE
```

Current project governance:
- `semantic_v2/10_governance/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_COMMON_INVARIANTS_AND_TYPE_ADAPTERS__LOCK.md`
- `semantic_v2/20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`
