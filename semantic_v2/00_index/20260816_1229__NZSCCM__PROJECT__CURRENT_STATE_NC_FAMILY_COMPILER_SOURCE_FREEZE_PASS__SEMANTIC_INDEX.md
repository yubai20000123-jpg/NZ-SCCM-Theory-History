# NZ-SCCM semantic current state — NC family compiler source freeze PASS

**Timestamp:** 2026-08-16 12:29 +08:00

## Current project backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1 = ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order = ACTIVE
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
same-state current stress + consistent tangent = REQUIRED
General-D15 moment-first = ACTIVE
P,Rq,L connected-branch root = ACTIVE
zero structural spatial/thickness quadrature = ACTIVE
```

## NC family compiler freeze

```text
source operator = frozen R10
operational core = [-2.35,+1.90]
coefficient guard = [-2.60,+2.15]
compiler channels = U,C,T,T7
one global Chebyshev polynomial per channel
same order for all channels
M = 8*(N+1)
exact C1 at lambda=0
E_sigma limit = 0.5%
E_tangent limit = 5%
E_divided-difference limit = 5%
selected family order = N_NC=3584
```

The deterministic candidate ladder reaches its first passing order at `N=3584`; `N=3328` still fails the tangent gate.

Reference R10 audit at `N=3584`:

```text
E_sigma = 0.107218%
E_tangent = 4.06652%
E_divided_difference = 0.381386%
```

The same compiler contract passes the current Swartz `kappa` extrema `1.9993148515` and `2.0008935611`.

## Important status boundary

```text
NC_FAMILY_SOURCE_COMPILER_FREEZE = PASS
HIGH_ORDER_N3584_CH_D15_STRUCTURAL_BACKEND = NOT_YET_EXECUTED
NEW_Z0_Z6_UNIFIED_Pu = NOT CALCULATED
Z6 51.30 MN = retained engineering baseline pending unified rerun
```

The next step is therefore not another specimen-specific compiler change. It is the common high-order CH / moment-first D15 backend implementation and tractability audit, followed by the unified Z0-Z6 rerun.

## Read order

1. `../10_governance/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_SOURCE_FIDELITY_AND_ORDER_FREEZE__LOCK.md`
2. `../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__EXECUTION_REPORT.md`
3. `../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__PARAMS_AND_INTERMEDIATES.json`
4. `../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__REPRO.py`
5. `20260816_1217__NZSCCM__PROJECT__CURRENT_STATE_UNIFIED_PRODUCTION_WORKFLOW_V1__SEMANTIC_INDEX.md`
6. `../60_validation/steel_shell/20260816_1205__NZSCCM__Z6_VS_Z0_Z5_CALCULABILITY_AND_COMPILER_CONSISTENCY__AUDIT.md`
