# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260816_1134__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_FIXED_N48_REPRESENTATION_CAPACITY_FAIL__SEMANTIC_INDEX.md`

## Current locked status

```text
PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
R10 physical current operator = FROZEN / UNCHANGED
MATERIAL_COMPILER_ORDER = 48 FOR U/C/T/T7
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

No order change is permitted without explicit user authorization. The 11:10 multirate order escalation remains historical diagnostic only.

## 11:34 fixed-N48 result

A source-only constrained-minimax test was run inside the same single global degree-48 C1 polynomial space.

Best found T maximum value errors on conservative Z0–Z5 envelopes are:

```text
Z0 .19812
Z1 .12199
Z2 .25816
Z3 .13381
Z4 .17144
Z5 .10580
```

The unchanged R10 current master reconstructed from separately value-minimax U/C/T/T7 still has maximum stress-scalar errors:

```text
Z0 .21376
Z1 .13061
Z2 .28470
Z3 .14902
Z4 .18634
Z5 .11574
```

A favorable audit with U/C/T7 exact and only T replaced by the best found fixed-N48 T polynomial leaves approximately `.106–.257` current-master stress error. Therefore the controlling limitation is the single-global degree-48 representation of the narrow R10 tensile transition itself.

```text
FIXED_N48_ORDER = RETAINED
SINGLE_GLOBAL_N48_COEFFICIENT_ONLY_REPAIR = FAIL_REPRESENTATION_CAPACITY
NEW_Z0_Z5_Pu = NOT_CALCULATED
```

## Current next gate

`Z0_Z5_AR2_FIXED_N48_MULTISCALE_ANALYTIC_REPRESENTATION_GATE`

The next representation must keep the order ceiling at 48 and change only the analytic factorization/enrichment needed to resolve the R10 small-positive tensile scale. It must remain source-only, retain exact C1 behavior, preserve Cayley-Hamilton / moment-first D15 zero-spatial compatibility, and pass current-master value/tangent fidelity before any Pu recalculation.

## Repository semantic read order

1. `20260816_1134__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_FIXED_N48_REPRESENTATION_CAPACITY_FAIL__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1134__NZSCCM__Z0_Z5_FIXED_N48_FIDELITY_REBUILD__LOCK.md`
3. `../20_theory/nc_material/20260816_1134__NZSCCM__NC_MATERIAL__FIXED_N48_REPRESENTATION_CAPACITY__THEORY.md`
4. `../40_execution/steel_shell/20260816_1134__NZSCCM__Z0_Z5_FIXED_N48_FIDELITY_REBUILD__EXECUTION_REPORT.md`
5. `../40_execution/steel_shell/20260816_1134__NZSCCM__Z0_Z5_FIXED_N48_FIDELITY__PARAMS_AND_INTERMEDIATES.json`
6. `../40_execution/steel_shell/20260816_1134__NZSCCM__Z0_Z5_FIXED_N48_FIDELITY__REPRO.py`
7. `../60_validation/steel_shell/20260816_1134__NZSCCM__Z0_Z5_FIXED_N48_FIDELITY__AUDIT.md`
8. `20260816_1131__NZSCCM__PROJECT__CURRENT_STATE_FIXED_N48_ORDER_RESTORED__SEMANTIC_INDEX.md`
9. `20260816_1054__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_COMPILER_FIDELITY_RETRACTION__SEMANTIC_INDEX.md`
10. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — user-accepted Z6 base
11. `20260816_1110__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY_PASS__SEMANTIC_INDEX.md` — historical diagnostic only
12. `20260816_0007__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT_GATE_PASS__SEMANTIC_INDEX.md`

## Audit levels

- `A_DIRECT_CONTENT_AUDIT`: file body opened/read; identity derived from content + chronology.
- `B_CONTENT_DERIVED_REGISTRY_OR_LEDGER`: stable source/history role derived from a content-read registry/ledger; open the leaf before using it for a technical claim.
- `C_NOT_YET_DIRECT_CONTENT_AUDITED`: locator known, semantic identity not yet asserted beyond family/locator role.

## Canonical naming

`YYYYMMDD_HHMM__NZSCCM__<SCOPE>__<SPECIFIC_CONTENT>__<ARTIFACT_KIND>.<ext>`

No legacy file is deleted, moved or renamed solely from filename identity.
