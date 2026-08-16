# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_1229__NZSCCM__PROJECT__CURRENT_STATE_NC_FAMILY_COMPILER_SOURCE_FREEZE_PASS__SEMANTIC_INDEX.md`

## Current locked production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
source current material operator
same-state consistent current tangent
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

## Unified method / physical adapters

The same workflow serves NC+rebar, NC+steel shell, UHPC+rebar and UHPC+steel shell. Source material laws and steel-phase geometry may differ physically, but they may not replace the common kinematics, membrane redistribution, exact-moment engine, generalized root topology, consistent-tangent rule or zero-spatial-integration governance.

## NC family compiler source freeze

The frozen ordinary-concrete source remains R10.

```text
operational core = [-2.35,+1.90]
coefficient guard = [-2.60,+2.15]
channels = U,C,T,T7
one global Chebyshev polynomial per channel
same order for all channels
M=8*(N+1)
exact C1 at lambda=0
E_sigma <= 0.5%
E_tangent <= 5%
E_divided_difference <= 5%
```

The deterministic order ladder reaches its first passing candidate at

```text
N_NC = 3584
```

Reference assembled-current audit:

```text
E_sigma = 0.107218%
E_tangent = 4.06652%
E_divided_difference = 0.381386%
```

The same frozen order/core/guard/algorithm passes the current Swartz R10 kappa extrema.

```text
NC_FAMILY_SOURCE_COMPILER_FREEZE = PASS
N3584_CH_D15_STRUCTURAL_BACKEND = NOT_YET_EXECUTED
NEW_Z0_Z6_UNIFIED_RESULTS = NOT_CALCULATED
```

The earlier N48 and ad hoc multirate calculations remain historical diagnostics only.

## Capacity status

```text
Z6 51.30 MN = retained user-accepted engineering baseline; unified rerun required
Z0-Z5 10:43 values = retracted pending unified rerun
```

## Current next gate

`UNIFIED_V1_N3584_CH_MOMENT_FIRST_D15_BACKEND_AND_Z0_Z6_RERUN_GATE`

## Repository semantic read order

1. `20260816_1229__NZSCCM__PROJECT__CURRENT_STATE_NC_FAMILY_COMPILER_SOURCE_FREEZE_PASS__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_SOURCE_FIDELITY_AND_ORDER_FREEZE__LOCK.md`
3. `../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__EXECUTION_REPORT.md`
4. `../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__PARAMS_AND_INTERMEDIATES.json`
5. `../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__REPRO.py`
6. `../20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`
7. `20260816_1217__NZSCCM__PROJECT__CURRENT_STATE_UNIFIED_PRODUCTION_WORKFLOW_V1__SEMANTIC_INDEX.md`
8. `../60_validation/steel_shell/20260816_1205__NZSCCM__Z6_VS_Z0_Z5_CALCULABILITY_AND_COMPILER_CONSISTENCY__AUDIT.md`
9. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — retained Z6 baseline
10. `20260816_1134__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_FIXED_N48_REPRESENTATION_CAPACITY_FAIL__SEMANTIC_INDEX.md` — retained representation-capacity diagnostic

No legacy file is deleted, moved or renamed solely from filename identity.
