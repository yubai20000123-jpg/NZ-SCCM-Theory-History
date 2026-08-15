# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260815_2144__NZSCCM__PROJECT__CURRENT_STATE_R20_R02_PROJECTION_AND_MEMBRANE_ACTIVATION__SEMANTIC_INDEX.md`

This is the current operational status entry after the existing-state single-halfwave FvK membrane residual projection gate.

The 21:44 stage does **not** publish a new Pu. It establishes:

```text
DQC_STATIONARY_IN_p20 = FAIL
DQC_STATIONARY_IN_p02 = FAIL
CURRENT_DQC_POSTBUCKLING_MEMBRANE_COMPLETENESS = FAIL_CONFIRMED
MINIMAL_MEMBRANE_UNKNOWN_VECTOR = [c,p20,p02]^T
GENERAL_D15 = UNCHANGED
```

At the certified D=.50 state:

```text
R20=-19.48685822 MN mm
R02=-23.47348406 MN mm
```

The active next execution is:

`FIXED_D050_COUPLED_q_c_p20_p02_EQUILIBRIUM`

No D continuation and no Pu release should precede that fixed-D coupled checkpoint.

## Repository semantic read order

1. `20260815_2144__NZSCCM__PROJECT__CURRENT_STATE_R20_R02_PROJECTION_AND_MEMBRANE_ACTIVATION__SEMANTIC_INDEX.md`
2. `../10_governance/20260815_2144__NZSCCM__R20_R02_PROJECTION_GATE_AND_MEMBRANE_SYSTEM_ACTIVATION__LOCK.md`
3. `../40_execution/steel_shell/20260815_2144__NZSCCM__EXISTING_STATE_R20_R02_D15_PROJECTION__EXECUTION_REPORT.md`
4. `20260815_2134__NZSCCM__PROJECT__CURRENT_STATE_MINIMAL_FVK_MEMBRANE_COMPLETION__SEMANTIC_INDEX.md`
5. `../20_theory/nc_steel_shell_panel/20260815_2134__NZSCCM__SINGLE_HALFWAVE_MINIMAL_FVK_MEMBRANE_COMPLETION__THEORY.md`
6. `20260815_2118__NZSCCM__PROJECT__CURRENT_STATE_POSTBUCKLING_MEMBRANE_COMPATIBILITY_AUDIT__SEMANTIC_INDEX.md`
7. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`
8. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_SEMANTIC_TREE__SEMANTIC_MANIFEST.md`
9. `20260813_1328__NZSCCM__REPOSITORY__AUDITED_ARTIFACTS__SEMANTIC_MANIFEST.csv`
10. `20260813_1328__NZSCCM__REPOSITORY__ARTIFACT_SUPERSESSION__SUPERSESSION_MAP.csv`
11. `20260813_1328__NZSCCM__REPOSITORY__LEGACY_TO_CANONICAL__RENAME_MAP.csv`
12. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_AUDIT_COVERAGE_AND_FRONTIER__AUDIT.md`
13. `20260813_1604__NZSCCM__REPOSITORY__SEMANTIC_MAP_CROSSCHECK_CORRECTIONS__AUDIT.md`
14. `20260813_1604__NZSCCM__REPOSITORY__CONTROLLED_PHYSICAL_MIGRATION_READINESS__AUDIT.md`

The 16:04 correction audit is an overlay for repository-path/canonical-ID metadata only. It does not alter theory or numerical results.

## Audit levels

- `A_DIRECT_CONTENT_AUDIT`: file body opened/read; identity derived from content + chronology.
- `B_CONTENT_DERIVED_REGISTRY_OR_LEDGER`: stable source/history role derived from a content-read registry/ledger; open the leaf before using it for a technical claim.
- `C_NOT_YET_DIRECT_CONTENT_AUDITED`: locator known, semantic identity not yet asserted beyond family/locator role.

## Canonical naming

```text
YYYYMMDD_HHMM__NZSCCM__<SCOPE>__<SPECIFIC_CONTENT>__<ARTIFACT_KIND>.<ext>
```

If date is known but clock time is not defensible, use `YYYYMMDD_TUNK`; do not invent `00:00`.

Mutable status is stored in the semantic manifest/current-state entry rather than treated as filename truth.

## Migration rule

Existing legacy paths remain preserved until their contents/supersession relations are sufficiently audited. Canonical `.LOCATOR.md` files under `semantic_v2/` provide the clean semantic entry points without duplicating or silently rewriting theory/result bodies.

No legacy file is to be deleted, moved, or renamed solely from its filename.
