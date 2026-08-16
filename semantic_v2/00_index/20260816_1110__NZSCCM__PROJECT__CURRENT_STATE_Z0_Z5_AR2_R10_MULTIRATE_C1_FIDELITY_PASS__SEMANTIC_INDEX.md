# NZ-SCCM current semantic index — Z0–Z5 AR2 R10 multirate-C1 fidelity pass

**Timestamp:** 2026-08-16 11:10 +08:00  
**Status:** CURRENT OPERATIONAL ENTRY

## Governing state

```text
PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
R10 physical current operator = FROZEN
Cayley-Hamilton = ACTIVE
General D15 exact moments = ACTIVE
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Zhou/Winter calibration=NO
```

## Result status

```text
Z6_AR2_Pu = 51.30 MN  # user accepted and retained
Z0_Z5_20260816_1043_Pu = RETRACTED_PENDING_RECALCULATION
```

The 10:54 diagnosis that the Z6-wide single N48 compiler was invalid for Z0–Z5 is retained.

## Material compiler rebuild

The current Z0–Z5 material candidate is now

`R10-MR-C1(256,1024,1280,512)`

with one global guard hull

`[-1.50,+0.35]`

and source-tangent-certified operational core

`[-1.40,+0.30]`.

Primitive orders:

```text
U 256
C 1024
T 1280
T7 512
```

No material-zone or spatial subdivision is introduced.

## Fidelity result

Operational-core primitive maximum value errors:

```text
U  8.60e-5
C  1.57e-4
T  6.01e-4
T7 4.37e-4
```

Unchanged R10 current-master source audit:

```text
max spectral stress error = 4.215e-4
max tangent error / source peak tangent = 2.821%
```

Rejected old wide N48 on the same core:

```text
max spectral stress error = .71852
max tangent error / source peak tangent = 81.53%
```

Thus:

```text
R10_CURRENT_OPERATOR_FIDELITY_REBUILD = PASS
C1_ANCHOR_GATE = PASS
O1_COEFFICIENT_GATE = PASS
CAYLEY_HAMILTON_FORMAL_COMPATIBILITY = PASS
GENERAL_D15_FORMAL_COMPATIBILITY = PASS
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
```

## Important remaining block

The existing structural execution kernel is fixed around N48 recurrence. The high-order multirate primitives have not yet been recompiled into a variable-order moment-first D15 structural evaluator.

Therefore:

```text
NEW_Z0_Z5_Pu = NOT_CALCULATED
```

## Unique next gate

`Z0_Z5_AR2_MULTIRATE_R10_TO_VARIABLE_ORDER_MOMENT_FIRST_D15_RECOMPILE_GATE`

That gate must:
- implement variable-order Cayley-Hamilton recurrence without spatial quadrature;
- use moment-first D15 operations rather than a material-point field grid;
- check coefficient conditioning and computational tractability;
- blind-solve the connected branch only after the backend passes;
- certify the recalculated continuous principal spectrum remains inside `[-1.40,+0.30]`, or fail and rebuild the material hull.

## Read order

1. `../10_governance/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_COMPILER_FIDELITY__LOCK.md`
2. `../20_theory/nc_material/20260816_1110__NZSCCM__NC_MATERIAL__R10_MULTIRATE_C1_SOURCE_FIDELITY__THEORY.md`
3. `../40_execution/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY_REBUILD__EXECUTION_REPORT.md`
4. `../40_execution/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY__PARAMS_AND_INTERMEDIATES.json`
5. `../40_execution/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY__REPRO.py`
6. `../60_validation/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_SOURCE_FIDELITY__AUDIT.md`
7. `20260816_1054__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_COMPILER_FIDELITY_RETRACTION__SEMANTIC_INDEX.md`
8. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md`
