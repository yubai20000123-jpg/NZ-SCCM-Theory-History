# NZ-SCCM current semantic index — Z0–Z5 AR2 compiler-fidelity retraction

**Timestamp:** 2026-08-16 10:54 +08:00  
**Status:** CURRENT OPERATIONAL ENTRY

## Current governing result status

```text
Z6_AR2_Pu = 51.30 MN  # user accepted, retained
Z0_Z5_20260816_1043_Pu = RETRACTED_PENDING_RECALCULATION
Z0_Z5_20260816_1043_ZHOU_WINTER_ERROR_TABLE = RETRACTED_PENDING_RECALCULATION
```

## Proven reason for retraction

The 10:43 Z0–Z5 run reused the Z6 wide single N48 material compiler over

`lambda in [-2.35,+1.90]`.

Inside every Z0–Z5 reachable material range, the small-positive tension transition has approximately

```text
T error   ~= 0.704
T^7 error ~= 0.796
```

which is an order-one material-operator fidelity failure. This is much larger than the 8–24% capacity differences being interpreted.

Thus the earlier physical interpretation of a systematic Z0–Z4 underprediction is withdrawn.

## Independent localization checks

Exact uniform `q=0` capacities from the original scalar R10 target plus steel/web caps are close to Zhou's full-section squash scale:

```text
Z0 45.0752 vs Pyth 44.0449 MN
Z1 31.0016 vs Pyth 30.3196 MN
Z2 51.5421 vs Pyth 50.6221 MN
Z3 55.9792 vs Pyth 54.9488 MN
Z4 80.7600 vs Pyth 79.3861 MN
Z5 15.0251 vs Pyth 14.6816 MN
```

Therefore the base section/material assembly is not the source of the 20–36% losses.

The challenged q amplitudes are broadly of the same order as classical imperfect-plate amplification, so an order-of-magnitude error in the generalized q-equilibrium is not currently established.

## Next mandatory gate

```text
Z0_Z5_AR2_CURRENT_OPERATOR_FIDELITY_REBUILD_ZERO_SPATIAL_INTEGRATION
```

The repair must preserve:

```text
R10 physical current operator
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
General D15
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Zhou/Winter calibration=NO
```

A simple narrower single-interval N48 precheck is still not accurate enough in T/T7; a materially faithful multiscale/analytic coefficient representation is required before recomputing Pu.

## Read order

1. `../10_governance/20260816_1054__NZSCCM__Z0_Z5_AR2_RESULT_RETRACTION_AND_COMPILER_FIDELITY_GATE__LOCK.md`
2. `../40_execution/steel_shell/20260816_1054__NZSCCM__Z0_Z5_AR2_DISCREPANCY_LOCALIZATION__EXECUTION_REPORT.md`
3. `../40_execution/steel_shell/20260816_1054__NZSCCM__Z0_Z5_AR2_DISCREPANCY_LOCALIZATION__PARAMS_AND_INTERMEDIATES.json`
4. `../40_execution/steel_shell/20260816_1054__NZSCCM__Z0_Z5_AR2_DISCREPANCY_LOCALIZATION__REPRO.py`
5. `20260816_1043__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z6_AR2_SSSS_CAPACITY_MATRIX__SEMANTIC_INDEX.md` — preserved as retracted challenged calculation
6. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — accepted Z6 base
