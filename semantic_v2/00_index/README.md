# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260815_2118__NZSCCM__PROJECT__CURRENT_STATE_POSTBUCKLING_MEMBRANE_COMPATIBILITY_AUDIT__SEMANTIC_INDEX.md`

This is the current operational status entry after the no-Pu Nguyen/FvK postbuckling membrane-compatibility audit. Earlier current-state indexes remain provenance and are not deleted.

The 21:18 stage does **not** publish a new Pu. It changes the active causal-theory frontier to:

`SINGLE_HALFWAVE_FVK_MEMBRANE_RESIDUAL_PROJECTION_COMPLETENESS`

which has not yet been executed.

## Repository semantic read order

1. `20260815_2118__NZSCCM__PROJECT__CURRENT_STATE_POSTBUCKLING_MEMBRANE_COMPATIBILITY_AUDIT__SEMANTIC_INDEX.md`
2. `20260815_2118__NZSCCM__POSTBUCKLING_MEMBRANE_AUDIT__ARTIFACT_MANIFEST.csv`
3. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`
4. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_SEMANTIC_TREE__SEMANTIC_MANIFEST.md`
5. `20260813_1328__NZSCCM__REPOSITORY__AUDITED_ARTIFACTS__SEMANTIC_MANIFEST.csv`
6. `20260813_1328__NZSCCM__REPOSITORY__ARTIFACT_SUPERSESSION__SUPERSESSION_MAP.csv`
7. `20260813_1328__NZSCCM__REPOSITORY__LEGACY_TO_CANONICAL__RENAME_MAP.csv`
8. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_AUDIT_COVERAGE_AND_FRONTIER__AUDIT.md`
9. `20260813_1604__NZSCCM__REPOSITORY__SEMANTIC_MAP_CROSSCHECK_CORRECTIONS__AUDIT.md`
10. `20260813_1604__NZSCCM__REPOSITORY__CONTROLLED_PHYSICAL_MIGRATION_READINESS__AUDIT.md`

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
