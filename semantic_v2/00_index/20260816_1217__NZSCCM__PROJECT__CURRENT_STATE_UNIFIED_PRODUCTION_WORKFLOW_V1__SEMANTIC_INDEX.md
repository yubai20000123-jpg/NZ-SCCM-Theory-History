# NZ-SCCM current semantic index — unified production workflow V1

**Timestamp:** 2026-08-16 12:17 +08:00  
**Identity:** CURRENT OPERATIONAL ENTRY

## Current project-wide workflow

The current method is a modular but unified production workflow.

Common mechanics:

```text
one continuous complete halfwave
source/design-side halfwave selection
Nguyen second-order kinematics
membrane stress redistribution
source current material operator
source-faithful finite analytic material compiler
Cayley-Hamilton / approved finite matrix lift
moment-first General-D15 exact moments
formal spatial sampling = 0
formal spatial quadrature = 0
formal subdomains = 1
common P,Rq,L connected-branch primary limit root
same-state consistent material + geometric tangent/stability audit
```

Legitimate physical adapters:

```text
NC versus UHPC material source operator
rebar versus finite-thickness shell steel phase
source-grounded shell local amplitudes with exact condensation
physical boundary / energy halfwave selector
material-family analytic basis/order where required by the source operator
```

A case ID, measured Pu, Zhou/Winter value or desired error sign may not select a method, material compiler, root, boundary or halfwave.

## Four target combinations

```text
NC + rebar
NC + steel shell
UHPC + rebar
UHPC + steel shell
```

NC+rebar and NC+shell must share one frozen NC material-family compiler. UHPC+rebar and UHPC+shell must share one frozen UHPC material-family compiler after the UHPC multidimensional source operator is frozen.

## Current capacities

```text
Z6 51.30 MN = retained user-accepted engineering baseline; unified-workflow rerun required
Z0-Z5 10:43 values = retracted pending unified rerun
```

## Current next gate

`UNIFIED_PRODUCTION_WORKFLOW_V1_IMPLEMENTATION_AND_NC_FAMILY_COMPILER_FREEZE`

This gate must first freeze the NC family compiler under source-only value+tangent fidelity governance, then rerun Z0-Z6 through one identical NC material/compiler + common D15/root backend.

## Canonical read order

1. `../10_governance/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_COMMON_INVARIANTS_AND_TYPE_ADAPTERS__LOCK.md`
2. `../20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`
3. `../40_execution/common/20260816_1217__NZSCCM__UNIFIED_WORKFLOW_V1__INTERMEDIATE_STATE_SCHEMA_AND_CURRENT_BASELINE.json`
4. `../60_validation/common/20260816_1217__NZSCCM__UNIFIED_WORKFLOW_V1__COMMON_VS_TYPE_SPECIFIC_MATRIX__AUDIT.md`
5. `../60_validation/steel_shell/20260816_1205__NZSCCM__Z6_VS_Z0_Z5_CALCULABILITY_AND_COMPILER_CONSISTENCY__AUDIT.md`
6. `../10_governance/20260816_1152__NZSCCM__UNIFIED_COMPILER_WORKFLOW_ACROSS_NC_UHPC_REBAR_SHELL__LOCK.md` — superseded where V1 is more explicit about legitimate type-adapter differences
7. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — retained Z6 baseline

## Status

```text
UNIFIED_WORKFLOW_V1 = FROZEN_CURRENT
NC_SOURCE_OPERATOR = R10_FROZEN
NC_FAMILY_COMPILER_UNDER_V1 = NOT_YET_FROZEN
UHPC_SOURCE_OPERATOR = NOT_YET_FINAL_PRODUCTION_FROZEN
Z0_Z6_UNIFIED_RERUN = PENDING_NC_COMPILER_FREEZE
```