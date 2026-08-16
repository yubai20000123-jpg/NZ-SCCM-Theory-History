# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260816_1110__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY_PASS__SEMANTIC_INDEX.md`

## Current locked status

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
Zhou/Winter calibration=NO

Z6_AR2_USER_ACCEPTED_Pu = 51.30 MN
Z0_Z5_20260816_1043_Pu = RETRACTED_PENDING_RECALCULATION
```

## Current material-compiler result

The Z6-wide single N48 representation is retired for Z0–Z5 because it had order-one source error inside their occupied mixed tension/compression range.

The replacement material representation has passed its source-only gate:

`R10-MR-C1(256,1024,1280,512)`

```text
guard material hull = [-1.50,+0.35]
operational fidelity core = [-1.40,+0.30]
U degree=256
C degree=1024
T degree=1280
T7 degree=512
```

All four are single global finite Chebyshev polynomials and retain exact R10 C1 anchors at `lambda=0`. No material-zone or spatial subdivision is introduced.

Operational-core primitive value errors are approximately

```text
U  8.60e-5
C  1.57e-4
T  6.01e-4
T7 4.37e-4
```

After reinsertion into the unchanged R10 spectral master:

```text
max spectral stress-scalar error = 4.215e-4
max tangent error / source peak tangent = 2.821%
```

The rejected wide N48 representation on the same core was approximately

```text
max spectral stress-scalar error = .71852
max tangent error / source peak tangent = 81.53%
```

Therefore the material-fidelity defect identified at 10:54 is closed at source-operator level.

## Current remaining block

The structural kernel still assumes fixed N48 recurrence. The variable-order multirate compiler has not yet been executed through the moment-first D15 structural backend.

```text
NEW_Z0_Z5_Pu = NOT_CALCULATED
```

Current unique next gate:

`Z0_Z5_AR2_MULTIRATE_R10_TO_VARIABLE_ORDER_MOMENT_FIRST_D15_RECOMPILE_GATE`

The next structural solve must remain zero-spatial-integration and must certify the recalculated continuous material spectrum remains inside `[-1.40,+0.30]` before any corrected Pu is accepted.

## Repository semantic read order

1. `20260816_1110__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY_PASS__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_COMPILER_FIDELITY__LOCK.md`
3. `../20_theory/nc_material/20260816_1110__NZSCCM__NC_MATERIAL__R10_MULTIRATE_C1_SOURCE_FIDELITY__THEORY.md`
4. `../40_execution/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY_REBUILD__EXECUTION_REPORT.md`
5. `../40_execution/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY__PARAMS_AND_INTERMEDIATES.json`
6. `../40_execution/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY__REPRO.py`
7. `../60_validation/steel_shell/20260816_1110__NZSCCM__Z0_Z5_AR2_R10_MULTIRATE_C1_SOURCE_FIDELITY__AUDIT.md`
8. `20260816_1054__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_COMPILER_FIDELITY_RETRACTION__SEMANTIC_INDEX.md`
9. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — user-accepted Z6 base
10. `20260816_0007__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT_GATE_PASS__SEMANTIC_INDEX.md`
11. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`

## Audit levels

- `A_DIRECT_CONTENT_AUDIT`: file body opened/read; identity derived from content + chronology.
- `B_CONTENT_DERIVED_REGISTRY_OR_LEDGER`: stable source/history role derived from a content-read registry/ledger; open the leaf before using it for a technical claim.
- `C_NOT_YET_DIRECT_CONTENT_AUDITED`: locator known, semantic identity not yet asserted beyond family/locator role.

## Canonical naming

`YYYYMMDD_HHMM__NZSCCM__<SCOPE>__<SPECIFIC_CONTENT>__<ARTIFACT_KIND>.<ext>`

No legacy file is deleted, moved or renamed solely from filename identity.