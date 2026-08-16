# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260816_1131__NZSCCM__PROJECT__CURRENT_STATE_FIXED_N48_ORDER_RESTORED__SEMANTIC_INDEX.md`

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

MATERIAL_COMPILER_ORDER = 48
U_ORDER=48
C_ORDER=48
T_ORDER=48
T7_ORDER=48

Z6_AR2_USER_ACCEPTED_Pu = 51.30 MN
Z0_Z5_20260816_1043_Pu = RETRACTED_PENDING_RECALCULATION
```

## User correction applied

The 11:10 multirate order proposal

```text
U=256 / C=1024 / T=1280 / T7=512
```

is retracted from current production governance and retained only as historical source-fidelity diagnostic evidence.

The restored order-level compiler family is

```text
U  = N48-C1
C  = N48-C1
T7 = N48-C1
T  = N48-C1-CONSTRAINED-MINIMAX
```

No future order change is permitted without explicit user authorization.

## Retained compiler defect

Restoring order 48 does not make the old Z6-wide coefficient set valid for Z0–Z5.

The 10:54 source audit remains active:

```text
old wide interval [-2.35,+1.90]
T error   ~= .704
T7 error  ~= .796
```

inside the actual Z0–Z5 occupied material domain.

Therefore:

```text
FIXED_N48_ORDER = CURRENT
OLD_Z6_WIDE_N48_Z0_Z5_COEFFICIENT_SET = PROHIBITED
```

## Current next gate

`Z0_Z5_AR2_FIXED_N48_CURRENT_OPERATOR_FIDELITY_REBUILD_ZERO_SPATIAL_INTEGRATION`

The repair must remain at degree 48 and improve only coefficient generation / analytic representation of the unchanged R10 source material operator. No Pu recalculation is released until this source-fidelity gate passes.

## Repository semantic read order

1. `20260816_1131__NZSCCM__PROJECT__CURRENT_STATE_FIXED_N48_ORDER_RESTORED__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1131__NZSCCM__N48_ORDER_RESTORATION_AND_MULTIRATE_RETRACTION__LOCK.md`
3. `../60_validation/steel_shell/20260816_1131__NZSCCM__MULTIRATE_ORDER_RETRACTION_AND_N48_RESTORATION__AUDIT.md`
4. `20260816_1054__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_COMPILER_FIDELITY_RETRACTION__SEMANTIC_INDEX.md`
5. `20260816_1110__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_AR2_R10_MULTIRATE_C1_FIDELITY_PASS__SEMANTIC_INDEX.md` — historical diagnostic only; superseded for current compiler order
6. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — user-accepted Z6 base
7. `20260816_0007__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT_GATE_PASS__SEMANTIC_INDEX.md`
8. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`

## Audit levels

- `A_DIRECT_CONTENT_AUDIT`: file body opened/read; identity derived from content + chronology.
- `B_CONTENT_DERIVED_REGISTRY_OR_LEDGER`: stable source/history role derived from a content-read registry/ledger; open the leaf before using it for a technical claim.
- `C_NOT_YET_DIRECT_CONTENT_AUDITED`: locator known, semantic identity not yet asserted beyond family/locator role.

## Canonical naming

`YYYYMMDD_HHMM__NZSCCM__<SCOPE>__<SPECIFIC_CONTENT>__<ARTIFACT_KIND>.<ext>`

No legacy file is deleted, moved or renamed solely from filename identity.
