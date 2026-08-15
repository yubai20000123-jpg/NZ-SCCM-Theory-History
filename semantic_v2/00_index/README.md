# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260815_2153__NZSCCM__PROJECT__CURRENT_STATE_D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM_RUNTIME_GATE__SEMANTIC_INDEX.md`

This is the current operational status entry after executing the first fixed-D=.50 coupled `q,c,p20,p02` membrane-equilibrium solve.

The 21:53 stage does **not** publish Pu and does not continue D. It establishes:

```text
DQC POSTBUCKLING MEMBRANE COMPLETENESS = FAIL_CONFIRMED (parent 21:44)
MINIMUM FvK MEMBRANE SYSTEM = [c,p20,p02]
FIXED_D050_AUGMENTED_NEAR_EQUILIBRIUM = FOUND
STRICT_FIXED_D050_CERTIFICATE = NOT_REACHED
FAILURE = REPRESENTATION/RUNTIME GATE
GENERAL_D15 = UNCHANGED
```

The best released fixed-D state is approximately

```text
D=.50
q=.008002
c=-.077622
p20=-.060657
p02=.165133
P=37.69591555 MN
Rq=-3.0633, Rc=+0.0101, R20=-0.0530, R02=-0.0237 MN mm
```

This state is an engineering near-equilibrium checkpoint, not a strict same-expression certificate and not Pu.

The active next execution is:

`DIRECTIONAL_MOMENT_FIRST_AUGMENTED_MEMBRANE_EVALUATOR_AT_D050`

Its purpose is to remove the dense coefficient-composition runtime gate without changing R10/N48/Cayley-Hamilton/General-D15 or the formal zero-spatial-quadrature identity. D continuation and Pu remain blocked until D=.50 is certified.

## Repository semantic read order

1. `20260815_2153__NZSCCM__PROJECT__CURRENT_STATE_D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM_RUNTIME_GATE__SEMANTIC_INDEX.md`
2. `../10_governance/20260815_2153__NZSCCM__D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM_RUNTIME_GATE__LOCK.md`
3. `../40_execution/steel_shell/20260815_2153__NZSCCM__D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM__EXECUTION_REPORT.md`
4. `../40_execution/steel_shell/20260815_2153__NZSCCM__D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM__PARAMS_AND_INTERMEDIATES.json`
5. `20260815_2144__NZSCCM__PROJECT__CURRENT_STATE_R20_R02_PROJECTION_AND_MEMBRANE_ACTIVATION__SEMANTIC_INDEX.md`
6. `20260815_2134__NZSCCM__PROJECT__CURRENT_STATE_MINIMAL_FVK_MEMBRANE_COMPLETION__SEMANTIC_INDEX.md`
7. `20260815_2118__NZSCCM__PROJECT__CURRENT_STATE_POSTBUCKLING_MEMBRANE_COMPATIBILITY_AUDIT__SEMANTIC_INDEX.md`
8. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`
9. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_SEMANTIC_TREE__SEMANTIC_MANIFEST.md`
10. `20260813_1328__NZSCCM__REPOSITORY__AUDITED_ARTIFACTS__SEMANTIC_MANIFEST.csv`
11. `20260813_1328__NZSCCM__REPOSITORY__ARTIFACT_SUPERSESSION__SUPERSESSION_MAP.csv`
12. `20260813_1328__NZSCCM__REPOSITORY__LEGACY_TO_CANONICAL__RENAME_MAP.csv`
13. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_AUDIT_COVERAGE_AND_FRONTIER__AUDIT.md`
14. `20260813_1604__NZSCCM__REPOSITORY__SEMANTIC_MAP_CROSSCHECK_CORRECTIONS__AUDIT.md`
15. `20260813_1604__NZSCCM__REPOSITORY__CONTROLLED_PHYSICAL_MIGRATION_READINESS__AUDIT.md`

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
