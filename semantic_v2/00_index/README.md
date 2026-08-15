# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260815_2358__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_POSTBUCKLING_REDERIVATION_GATE__SEMANTIC_INDEX.md`

Current locked status:

```text
AR2_2343_GAUSS_PATH = RETRACTED_FROM_CURRENT_EVIDENCE
Pu_40.97334_MN = INVALID_FOR_CURRENT_PROJECT
ANY_SPATIAL_NUMERICAL_QUADRATURE_INCLUDING_AUDIT = PROHIBITED
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1

OLD_DQC_INPLANE_SPACE_INCOMPLETE = RETAINED
P20_P02_AS_FINAL_CLASSICAL_MEMBRANE_CLOSURE = REOPENED / UNPROVEN
NEW_Pu = BLOCKED
```

The current mandatory next stage is not a capacity calculation. It is:

`CLASSICAL_ELASTIC_THIN_PLATE_POSTBUCKLING_LIMIT_GATE`

The membrane closure must first be rederived from the classical Kármán/FvK compatibility + in-plane equilibrium + boundary-condition system (preferably through the Airy stress function / membrane resultants), using exact analytical moments only. A slender elastic plate must recover the classical stable postbuckling carrying branch before the closure is allowed back into R10/N48/Cayley-Hamilton nonlinear material calculations.

The 23:43 files are preserved only as historical error evidence because they used spatial Gauss-Legendre and therefore violate the present project boundary.

## Repository semantic read order

1. `20260815_2358__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_POSTBUCKLING_REDERIVATION_GATE__SEMANTIC_INDEX.md`
2. `../10_governance/20260815_2358__NZSCCM__STRICT_ZERO_SPATIAL_INTEGRATION_AND_AR2_RETRACTION__LOCK.md`
3. `../60_validation/steel_shell/20260815_2358__NZSCCM__AR2_MEMBRANE_THEORY_CLASSICAL_LIMIT_REOPEN__AUDIT.md`
4. `20260815_2343__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__SEMANTIC_INDEX.md` — superseded historical invalid stage
5. `20260815_2306__NZSCCM__PROJECT__CURRENT_STATE_D055_DIRECTIONAL_CONTINUATION_REPRESENTATION_GATE__SEMANTIC_INDEX.md`
6. `20260815_2235__NZSCCM__PROJECT__CURRENT_STATE_D050_DIRECTIONAL_MOMENT_FIRST_CERTIFICATE__SEMANTIC_INDEX.md`
7. `20260815_2220__NZSCCM__PROJECT__CURRENT_STATE_UPDATED_FVK_THEORY_AND_EXPANSION_AUDIT__SEMANTIC_INDEX.md`
8. `20260815_2144__NZSCCM__PROJECT__CURRENT_STATE_R20_R02_PROJECTION_AND_MEMBRANE_ACTIVATION__SEMANTIC_INDEX.md`
9. `20260815_2134__NZSCCM__PROJECT__CURRENT_STATE_MINIMAL_FVK_MEMBRANE_COMPLETION__SEMANTIC_INDEX.md`
10. `20260815_2118__NZSCCM__PROJECT__CURRENT_STATE_POSTBUCKLING_MEMBRANE_COMPATIBILITY_AUDIT__SEMANTIC_INDEX.md`
11. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`
12. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_SEMANTIC_TREE__SEMANTIC_MANIFEST.md`
13. `20260813_1328__NZSCCM__REPOSITORY__AUDITED_ARTIFACTS__SEMANTIC_MANIFEST.csv`
14. `20260813_1328__NZSCCM__REPOSITORY__ARTIFACT_SUPERSESSION__SUPERSESSION_MAP.csv`
15. `20260813_1328__NZSCCM__REPOSITORY__LEGACY_TO_CANONICAL__RENAME_MAP.csv`
16. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_AUDIT_COVERAGE_AND_FRONTIER__AUDIT.md`
17. `20260813_1604__NZSCCM__REPOSITORY__SEMANTIC_MAP_CROSSCHECK_CORRECTIONS__AUDIT.md`
18. `20260813_1604__NZSCCM__REPOSITORY__CONTROLLED_PHYSICAL_MIGRATION_READINESS__AUDIT.md`

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
