# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260816_1054__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_COMPILER_FIDELITY_RETRACTION__SEMANTIC_INDEX.md`

## Current locked status

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
Zhou/Winter calibration=NO

Z6_AR2_USER_ACCEPTED_Pu = 51.30 MN
Z0_Z5_20260816_1043_Pu = RETRACTED_PENDING_RECALCULATION
```

## Proven current issue

The challenged 10:43 Z0–Z5 calculation reused the Z6-wide single N48 material compiler on `[-2.35,+1.90]`.

Inside the actually visited Z0–Z5 material domain, the sharp positive-tension transition is represented with order-one error:

```text
T max error   ~= 0.704
T^7 max error ~= 0.796
```

Therefore the earlier Z0–Z4 systematic underprediction interpretation is withdrawn.

Exact uniform `q=0` checks return capacities only about +1.7 to +2.3% above Zhou's full-section `Pyth`, so the base section/material assembly is not responsible for the challenged 20–36% loss.

The challenged q-amplitudes remain of the same order as classical imperfect-plate amplification, so the generalized q-equilibrium is not yet proven wrong.

## Current next gate

```text
Z0_Z5_AR2_CURRENT_OPERATOR_FIDELITY_REBUILD_ZERO_SPATIAL_INTEGRATION
```

A simple narrower single N48 interval is still too inaccurate in `T/T7`; the next representation must preserve the original R10 law while resolving the small-positive material transition analytically/multiscale, with zero structural spatial integration.

## Repository semantic read order

1. `20260816_1054__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_COMPILER_FIDELITY_RETRACTION__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1054__NZSCCM__Z0_Z5_AR2_RESULT_RETRACTION_AND_COMPILER_FIDELITY_GATE__LOCK.md`
3. `../40_execution/steel_shell/20260816_1054__NZSCCM__Z0_Z5_AR2_DISCREPANCY_LOCALIZATION__EXECUTION_REPORT.md`
4. `../40_execution/steel_shell/20260816_1054__NZSCCM__Z0_Z5_AR2_DISCREPANCY_LOCALIZATION__PARAMS_AND_INTERMEDIATES.json`
5. `../40_execution/steel_shell/20260816_1054__NZSCCM__Z0_Z5_AR2_DISCREPANCY_LOCALIZATION__REPRO.py`
6. `20260816_1043__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z6_AR2_SSSS_CAPACITY_MATRIX__SEMANTIC_INDEX.md` — preserved challenged calculation; superseded for current production use
7. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — user-accepted Z6 base
8. `20260816_0007__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT_GATE_PASS__SEMANTIC_INDEX.md`
9. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`

## Audit levels

- `A_DIRECT_CONTENT_AUDIT`: file body opened/read; identity derived from content + chronology.
- `B_CONTENT_DERIVED_REGISTRY_OR_LEDGER`: stable source/history role derived from a content-read registry/ledger; open the leaf before using it for a technical claim.
- `C_NOT_YET_DIRECT_CONTENT_AUDITED`: locator known, semantic identity not yet asserted beyond family/locator role.

## Canonical naming

`YYYYMMDD_HHMM__NZSCCM__<SCOPE>__<SPECIFIC_CONTENT>__<ARTIFACT_KIND>.<ext>`

No legacy file is deleted, moved or renamed solely from filename identity.
