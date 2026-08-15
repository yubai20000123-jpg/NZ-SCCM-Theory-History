# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260815_2220__NZSCCM__PROJECT__CURRENT_STATE_UPDATED_FVK_THEORY_AND_EXPANSION_AUDIT__SEMANTIC_INDEX.md`

This is the current operational entry after consolidating the updated single-halfwave augmented FvK postbuckling theory and auditing the observed implementation “inflation”.

Current locked interpretation:

```text
membrane_coordinates = [c,p20,p02]
flat_membrane_Jacobian = 3x3
General_D15 = UNCHANGED
formal_spatial_sampling = 0
formal_spatial_quadrature = 0
formal_spatial_subdomains = 1

PHYSICAL_THEORY_DOF_INFLATION = CONTROLLED_MINIMUM
KINEMATIC_POLYNOMIAL_DEGREE_INFLATION = NO
LOW_ORDER_INVARIANT_SUPPORT_EXPLOSION = NO
DENSE_HIGH_ORDER_BOUNDING_BOX_FILL_IN = YES
STRICT_D050_CERTIFICATE = NOT_REACHED
Pu = NOT_SOLVED
D_CONTINUATION = BLOCKED
```

The 22:20 audit refines the 21:53 runtime diagnosis: the p20/p02 completion does not enlarge the low-order polynomial degree family. The expensive behavior comes from high-order numerical tails retaining larger **dense rectangular coefficient boxes** in the inherited N48 implementation; `trim(A,tol)` is an axis-tail box trimmer, not element-wise sparse coefficient pruning.

The active next execution remains:

`DIRECTIONAL_MOMENT_FIRST_AUGMENTED_MEMBRANE_EVALUATOR_AT_D050`

Its purpose is to reproduce/certify D=.50 by computing only the required moment contractions for `P,Rq,Rc,R20,R02` and the flat Jacobian, without changing the physical theory or formal zero-spatial-quadrature identity.

## Repository semantic read order

1. `20260815_2220__NZSCCM__PROJECT__CURRENT_STATE_UPDATED_FVK_THEORY_AND_EXPANSION_AUDIT__SEMANTIC_INDEX.md`
2. `../10_governance/20260815_2220__NZSCCM__AUGMENTED_FVK_THEORY_AND_EXPANSION_AUDIT__LOCK.md`
3. `../20_theory/nc_steel_shell_panel/20260815_2220__NZSCCM__UPDATED_SINGLE_HALFWAVE_AUGMENTED_FVK_POSTBUCKLING_THEORY__THEORY.md`
4. `../60_validation/steel_shell/20260815_2220__NZSCCM__UPDATED_FVK_THEORY_AND_EXPANSION__AUDIT.md`
5. `../40_execution/steel_shell/20260815_2220__NZSCCM__UPDATED_FVK_THEORY_EXPANSION_AUDIT__PARAMS_AND_INTERMEDIATES.json`
6. `../50_results/steel_shell/20260815_2220__NZSCCM__AUGMENTED_FVK_EXPANSION_AUDIT__RESULT.csv`
7. `20260815_2153__NZSCCM__PROJECT__CURRENT_STATE_D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM_RUNTIME_GATE__SEMANTIC_INDEX.md`
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
