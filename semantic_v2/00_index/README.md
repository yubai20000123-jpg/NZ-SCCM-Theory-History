# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_1355__NZSCCM__PROJECT__CURRENT_STATE_R10_INTRINSIC_SCALE_GLOBAL_ORDER_DIAGNOSIS__SEMANTIC_INDEX.md`

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

The same workflow serves NC+rebar, NC+steel shell, UHPC+rebar and UHPC+steel shell. Physical adapters may differ; the common mechanics may not change case by case.

## NC representation status after 13:55 diagnosis

R10 physical material equations remain frozen.

The earlier wide-global N3584 source screen remains valid evidence:

```text
E_sigma=.00107218
E_tangent=.04066517
E_divided_difference=.00381386
```

but N3584 is no longer the preferred production representation basis.

Historical reconnection plus a new intrinsic-scale audit established:

```text
core/eta  = 1700.436
guard/eta = 1900.487
N3584 C/T derivative-error maxima localize at lambda≈±.0028-.0029
Pi_eta alone remains difficult for one wide global lambda polynomial
```

In intrinsic source coordinates:

```text
C(c), N=6 -> derivative error / peak ≈3.88%
u_R(t), N=64 -> derivative error / peak ≈3.59%
```

A material-only exact-Pi factor screen with `N_C=6,N_u=64` passes the same assembled source gates:

```text
E_sigma=.003337
E_tangent=.030469
E_divided_difference=.046869
```

using 72 fitted scalar coefficients rather than 14340 in four N3584 channels.

This screen is not production because exact `Pi_eta` has not yet been contracted through the formal zero-spatial exact-moment backend.

Therefore:

```text
R10_PHYSICS = UNCHANGED
N3584_SOURCE_FIDELITY_WITNESS = RETAINED
N3584_NEXT_PRODUCTION_BASIS = REJECTED
LOW_COMPLEXITY_INTRINSIC_FACTOR_SCREEN = MATERIAL_ONLY PASS DIAGNOSTIC
```

## Capacity status

```text
Z6 51.30 MN = retained user-accepted engineering baseline only
Z6 unified rerun = incomplete
Z0-Z5 10:43 values = retracted
Z0-Z5 12:48 values = diagnostic locators only
new Z0-Z6 production Pu = not released
```

## Current next gate

`UNIFIED_V1_R10_INTRINSIC_SCALE_FACTORIZED_PI_ADAPTER_GATE`

The next task is to preserve exact R10 while connecting its intrinsic factor graph, especially `Pi_eta`, to General-D15 or another already-approved zero-spatial exact-moment contraction. No case-specific compiler/order/domain, Z6-only fallback, material-width change or structural-response calibration is authorized.

## Repository semantic read order

1. `20260816_1355__NZSCCM__PROJECT__CURRENT_STATE_R10_INTRINSIC_SCALE_GLOBAL_ORDER_DIAGNOSIS__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1355__NZSCCM__R10_GLOBAL_ORDER_HISTORICAL_RECONNECTION_AND_INTRINSIC_SCALE__LOCK.md`
3. `../40_execution/common/20260816_1355__NZSCCM__R10_GLOBAL_ORDER_HISTORICAL_RECONNECTION__EXECUTION_REPORT.md`
4. `../40_execution/common/20260816_1355__NZSCCM__R10_INTRINSIC_SCALE_AUDIT__PARAMS_AND_INTERMEDIATES.json`
5. `../40_execution/common/20260816_1355__NZSCCM__R10_INTRINSIC_SCALE_AUDIT__REPRO.py`
6. `../60_validation/common/20260816_1355__NZSCCM__R10_GLOBAL_ORDER_CAUSE_AND_INTRINSIC_FACTOR_SCREEN__AUDIT.md`
7. `20260816_1248__NZSCCM__PROJECT__CURRENT_STATE_N3584_COMMON_BACKEND_TRACTABILITY_FAIL__SEMANTIC_INDEX.md` — predecessor
8. `../20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`
9. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — retained Z6 engineering baseline

No legacy file is deleted, moved or renamed solely from filename identity.
