# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 10:54 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_1054__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_COMPILER_FIDELITY_RETRACTION__SEMANTIC_INDEX.md`

## Current production scope

```text
PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
R10 physical current operator = ACTIVE
Cayley-Hamilton = ACTIVE
General D15 exact moments = ACTIVE
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid=PROHIBITED
Zhou/Winter calibration=PROHIBITED
```

## Accepted Z6 base

User-accepted result remains:

```text
Z6 a/b=2
m*=2
ell=b=12000 mm
q0=.004
Pu=51.30 MN
Pcr=39.2880147150 MN
Pyth=88.089888 MN
Zhou=49.4867667519 MN
Winter=50.1858541295 MN
```

No current action retracts this user-accepted Z6 value.

## Z0–Z5 10:43 calculation status

The 10:43 AR2 capacities and their Zhou/Winter error percentages are now:

```text
RETRACTED_PENDING_RECALCULATION
```

They are preserved in GitHub as challenged historical calculation artifacts but must not be used as current production values.

## Proven reason

The 10:43 process reused the Z6-wide single N48 compiler over

`lambda in [-2.35,+1.90]`.

The frozen R10 tension activation functions are not represented faithfully on this hull:

```text
T max error   ~= 0.704
T^7 max error ~= 0.796
```

The decisive point is that these order-one errors occur **inside the actual Z0–Z5 reachable material ranges**, around `lambda~+0.04 to +0.05`, not only in a remote unused part of the wide hull.

Therefore the earlier 8–24% capacity differences cannot be physically interpreted.

## Independent localization checks

### Exact flat q=0 reference

Using the exact scalar R10 target with uniform steel/web caps gives:

```text
Z0 45.0752 MN   vs Zhou Pyth 44.0449
Z1 31.0016 MN   vs Zhou Pyth 30.3196
Z2 51.5421 MN   vs Zhou Pyth 50.6221
Z3 55.9792 MN   vs Zhou Pyth 54.9488
Z4 80.7600 MN   vs Zhou Pyth 79.3861
Z5 15.0251 MN   vs Zhou Pyth 14.6816
```

Thus the base material/section assembly is healthy at the uniform axial state and does not explain a 20–36% loss.

### q-amplitude sanity

The challenged `A/A0` values are broadly comparable to the classical imperfect-plate estimate `eta/(1-eta)`. Hence an order-of-magnitude error in the generalized q-equilibrium is **not established**.

However, because `A0=a/500=0.004b` in AR2, Z0–Z4 have `A0/tc≈0.17–0.26` and challenged total deflection `A_total/tc≈0.26–0.50`; this geometric sensitivity must be reassessed after the material compiler is repaired.

## Narrow single-N48 precheck

Simply narrowing a single N48 interval is still insufficient. Trial reachable-range errors remain approximately:

```text
Z0 T~.197  T7~.354
Z1 T~.121  T7~.274
Z2 T~.256  T7~.392
Z3 T~.133  T7~.237
Z4 T~.170  T7~.214
Z5 T~.104  T7~.217
```

So the next fix is not another arbitrary single-interval N48 sweep.

## Current mandatory next gate

```text
Z0_Z5_AR2_CURRENT_OPERATOR_FIDELITY_REBUILD_ZERO_SPATIAL_INTEGRATION
```

Requirements:
- retain original R10 physical material law;
- retain one complete representative halfwave and Nguyen second-order kinematics;
- retain General D15 and zero spatial numerical integration;
- rebuild the material-coordinate analytic representation so the small-positive tension transition is faithfully represented;
- validate material fidelity before any new Pu solve;
- only then recompute Z0–Z5 and compare with Zhou/Winter.

## Current artifacts

- `semantic_v2/10_governance/20260816_1054__NZSCCM__Z0_Z5_AR2_RESULT_RETRACTION_AND_COMPILER_FIDELITY_GATE__LOCK.md`
- `semantic_v2/40_execution/steel_shell/20260816_1054__NZSCCM__Z0_Z5_AR2_DISCREPANCY_LOCALIZATION__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260816_1054__NZSCCM__Z0_Z5_AR2_DISCREPANCY_LOCALIZATION__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260816_1054__NZSCCM__Z0_Z5_AR2_DISCREPANCY_LOCALIZATION__REPRO.py`
- `semantic_v2/00_index/20260816_1054__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_COMPILER_FIDELITY_RETRACTION__SEMANTIC_INDEX.md`

Historical 10:43 Z0–Z5 files remain preserved but are superseded as production evidence.
