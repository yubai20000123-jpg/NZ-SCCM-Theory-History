# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260815_2343__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__SEMANTIC_INDEX.md`

Current user-directed result:

```text
Z6 comparison specimen a/b=2
m=2, ell=12000 mm
updated membrane coordinates = [c,p20,p02]
Rq=Rc=R20=R02=0
single complete representative out-of-plane halfwave
R10 physical current operator unchanged

UPDATED_FVK_DIRECT_R10_CONTINUUM_AUDIT_PATH = SOLVED
Pu_audit ≈ 40.97 MN
D_peak ≈ .8308
```

Important interpretation:

```text
old AR2 direct-R10 audit without complete membrane redistribution = 44.5529191054 MN
updated membrane-equilibrium audit                              ≈ 40.9733400613 MN
change                                                          ≈ -8.03%
```

Thus the missing FvK membrane redistribution is mechanically active but does not automatically raise postbuckling capacity. In the current reduced two-face steel object it lowers the connected peak and activates local steel yielding near the peak.

Identity restrictions:

```text
FORMAL_N48_D15_ZERO_QUADRATURE_PRODUCTION_Pu = NOT RELEASED
PROJECT FORMAL ZERO-QUADRATURE GOVERNANCE = UNCHANGED
PBL/WEB LONGITUDINAL STEEL PHASE IN AUGMENTED EQUILIBRIUM = NOT INCLUDED
FULL ZHOU SECTION FINAL Pu = NOT CLAIMED
```

The direct R10 continuum result uses high-order Gauss-Legendre only as an **audit executor** to answer the current physical-theory question while the formal augmented N48/D15 implementation still has a representation/compiler gate.

## Repository semantic read order

1. `20260815_2343__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__SEMANTIC_INDEX.md`
2. `../10_governance/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__LOCK.md`
3. `../40_execution/steel_shell/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__EXECUTION_REPORT.md`
4. `../40_execution/steel_shell/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__PARAMS_AND_INTERMEDIATES.json`
5. `../50_results/steel_shell/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__PATH.csv`
6. `../50_results/steel_shell/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__PEAK_CONVERGENCE.csv`
7. `../50_results/steel_shell/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__RESULT.md`
8. `20260815_2306__NZSCCM__PROJECT__CURRENT_STATE_D055_DIRECTIONAL_CONTINUATION_REPRESENTATION_GATE__SEMANTIC_INDEX.md`
9. `20260815_2235__NZSCCM__PROJECT__CURRENT_STATE_D050_DIRECTIONAL_MOMENT_FIRST_CERTIFICATE__SEMANTIC_INDEX.md`
10. `20260815_2220__NZSCCM__PROJECT__CURRENT_STATE_UPDATED_FVK_THEORY_AND_EXPANSION_AUDIT__SEMANTIC_INDEX.md`
11. `20260815_2144__NZSCCM__PROJECT__CURRENT_STATE_R20_R02_PROJECTION_AND_MEMBRANE_ACTIVATION__SEMANTIC_INDEX.md`
12. `20260815_2134__NZSCCM__PROJECT__CURRENT_STATE_MINIMAL_FVK_MEMBRANE_COMPLETION__SEMANTIC_INDEX.md`
13. `20260815_2118__NZSCCM__PROJECT__CURRENT_STATE_POSTBUCKLING_MEMBRANE_COMPATIBILITY_AUDIT__SEMANTIC_INDEX.md`
14. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`
15. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_SEMANTIC_TREE__SEMANTIC_MANIFEST.md`
16. `20260813_1328__NZSCCM__REPOSITORY__AUDITED_ARTIFACTS__SEMANTIC_MANIFEST.csv`
17. `20260813_1328__NZSCCM__REPOSITORY__ARTIFACT_SUPERSESSION__SUPERSESSION_MAP.csv`
18. `20260813_1328__NZSCCM__REPOSITORY__LEGACY_TO_CANONICAL__RENAME_MAP.csv`
19. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_AUDIT_COVERAGE_AND_FRONTIER__AUDIT.md`
20. `20260813_1604__NZSCCM__REPOSITORY__SEMANTIC_MAP_CROSSCHECK_CORRECTIONS__AUDIT.md`
21. `20260813_1604__NZSCCM__REPOSITORY__CONTROLLED_PHYSICAL_MIGRATION_READINESS__AUDIT.md`

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
