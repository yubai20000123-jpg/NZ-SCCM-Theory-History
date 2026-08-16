# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 11:10 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_1110__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY_PASS__SEMANTIC_INDEX.md`

## Frozen production scope

```text
PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
R10 physical current operator = FROZEN / UNCHANGED
Cayley-Hamilton = ACTIVE
General D15 exact moments = ACTIVE
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid=PROHIBITED
Zhou/Winter calibration=PROHIBITED
```

## Capacity-result status

```text
Z6_AR2_Pu = 51.30 MN  # user accepted and retained
Z0_Z5_20260816_1043_Pu = RETRACTED_PENDING_RECALCULATION
Z0_Z5_20260816_1043_ZHOU_WINTER_TABLE = RETRACTED_PENDING_RECALCULATION
```

The previous physical interpretation that membrane redistribution itself caused the 20–36% Z0–Z4 loss remains withdrawn.

## 10:54 proven process defect

The challenged run reused the Z6-wide single N48 material compiler on

`lambda in [-2.35,+1.90]`.

Inside the actual Z0–Z5 material ranges, it produced approximately

```text
T error   ~= .704
T7 error  ~= .796
```

and an unchanged-R10 current-master audit over the stocky operational range gives approximately

```text
spectral stress-scalar max error ~= .71852
spectral tangent relative error  ~= 81.5%
```

The old wide N48 compiler is prohibited for Z0–Z5 production.

## 11:10 material-fidelity rebuild

The R10 physical law was retained exactly. The new source-only representation candidate is

`R10-MR-C1(256,1024,1280,512)`

with one global material guard interval

`[-1.50,+0.35]`

and tangent-certified operational core

`[-1.40,+0.30]`.

Orders:

```text
U=256
C=1024
T=1280
T7=512
```

`MR` is material-primitive multirate polynomial order only; it is not a material-zone or spatial-domain subdivision.

The coefficient generator uses oversampled Gauss-Chebyshev **material coordinates**. Because their normal matrix is diagonal, the reproducible implementation uses a DCT-II source projection plus an exact two-equality Schur correction for the R10 C1 anchors. These coordinates are not structural spatial points.

### Source primitive fidelity on operational core

```text
U  max value error ~= 8.60e-5
C  max value error ~= 1.57e-4
T  max value error ~= 6.01e-4
T7 max value error ~= 4.37e-4
```

All coefficient maxima remain O(1), with overall maximum below `.60`.

### Unchanged current-master fidelity

Reinsert the compiled primitives into the exact unchanged R10 spectral master. Material-coordinate audit gives

```text
max spectral stress-scalar abs error = 4.2153e-4
max spectral tangent abs error       = 8.4312e-1
source peak tangent magnitude        = 2.98917e1
relative tangent error               = 2.8206%
```

Worst stress pair approximately:

```text
(lambda1,lambda2)=(-.994833,+.001083)
source   = -.9939997881
compiled = -.9944213174
```

Relative to the rejected wide N48 representation, the stress error is reduced by about `1705x` and tangent-relative error by about `28.9x`.

Therefore:

```text
R10_MR_C1_SOURCE_VALUE_GATE = PASS
R10_MR_C1_CURRENT_MASTER_VALUE_GATE = PASS
R10_MR_C1_CURRENT_MASTER_TANGENT_GATE = PASS_ON_OPERATIONAL_CORE
C1_ANCHOR_GATE = PASS
O1_COEFFICIENT_GATE = PASS
CAYLEY_HAMILTON_FORMAL_COMPATIBILITY = PASS
GENERAL_D15_FORMAL_COMPATIBILITY = PASS
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
```

## Remaining block

The current structural execution kernel is fixed around N48-style recurrence. The multirate orders up to 1280 have not yet been implemented in the variable-order moment-first structural D15 backend.

Therefore:

```text
NEW_Z0_Z5_Pu = NOT_CALCULATED
```

No new Z0–Z5 capacity may be released from this material gate alone.

The next blind structural calculation must also certify that its continuous reachable principal spectrum remains inside `[-1.40,+0.30]`. Leaving that core is a fail-fast event requiring material-hull regeneration.

## Current unique next gate

`Z0_Z5_AR2_MULTIRATE_R10_TO_VARIABLE_ORDER_MOMENT_FIRST_D15_RECOMPILE_GATE`

Required next actions:
1. implement variable-order Cayley-Hamilton recurrence for U/C/T/T7;
2. preserve moment-first General-D15 and zero spatial quadrature;
3. audit coefficient conditioning/computational tractability;
4. only after backend PASS, blind-solve Z0–Z5 connected `Rq=0` branches;
5. continuously enclose principal-value spectrum and verify core containment;
6. only then release corrected Pu and post-solve Zhou/Winter comparison.

## Current 11:10 artifacts

- `semantic_v2/10_governance/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_COMPILER_FIDELITY__LOCK.md`
- `semantic_v2/20_theory/nc_material/20260816_1110__NZSCCM__NC_MATERIAL__R10_MULTIRATE_C1_SOURCE_FIDELITY__THEORY.md`
- `semantic_v2/40_execution/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY_REBUILD__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY__REPRO.py`
- `semantic_v2/60_validation/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_SOURCE_FIDELITY__AUDIT.md`
- `semantic_v2/00_index/20260816_1110__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY_PASS__SEMANTIC_INDEX.md`
