# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260816_0007__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT_GATE_PASS__SEMANTIC_INDEX.md`

Current locked status:

```text
STRICT_ZERO_SPATIAL_INTEGRATION = ACTIVE
CLASSICAL_ELASTIC_THIN_PLATE_POSTBUCKLING_LIMIT_GATE = PASS
POSITIVE_MEMBRANE_POSTBUCKLING_BRANCH = RECOVERED
EDGEWARD_AXIAL_STRESS_REDISTRIBUTION = RECOVERED
p20,p02 AS INDEPENDENT FREE MEMBRANE COORDINATES = RETIRED
p20,p02 HARMONIC LABELS = RETAINED ONLY
Pu_40.97334_MN = RETRACTED / INVALID FOR CURRENT PROJECT
NONLINEAR_Z6_Pu = BLOCKED
```

The exact canonical FvK/Airy benchmark gives

`N=Ncr*A/(A+A0)+E t (A^2+2A0A)/16*(beta^2+alpha^4/beta^2)`

and, for a perfect square representative halfwave,

`sigma/sigma_cr=1+3(1-nu^2)/8*(A/t)^2`.

Thus the classical positive postbuckling membrane contribution has been recovered with zero spatial numerical integration. The previous membrane-space diagnosis is refined: `(2,0)/(0,2)` harmonics are required, but their amplitudes are compatibility/equilibrium-coupled and must not be treated as two unrelated relaxation coordinates.

Current next execution:

`ZHOU_Z6_BOUNDARY_ADMISSIBLE_CLASSICAL_FVK_AIRY_CLOSURE_ZERO_QUADRATURE`

That gate must impose the actual Z6 in-plane boundary class on the classical Airy/membrane closure before any return to R10/N48 nonlinear-material capacity calculation.

The 23:43 Gauss-based AR2 files remain preserved only as historical error evidence and are not current capacity data.

## Repository semantic read order

1. `20260816_0007__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT_GATE_PASS__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_0007__NZSCCM__CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT_GATE__LOCK.md`
3. `../20_theory/nc_steel_shell_panel/20260816_0007__NZSCCM__CLASSICAL_FVK_AIRY_POSTBUCKLING_LIMIT__THEORY.md`
4. `../40_execution/steel_shell/20260816_0007__NZSCCM__CLASSICAL_FVK_POSTBUCKLING_LIMIT__PARAMS_AND_INTERMEDIATES.json`
5. `../60_validation/steel_shell/20260816_0007__NZSCCM__CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT__AUDIT.md`
6. `20260815_2358__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_POSTBUCKLING_REDERIVATION_GATE__SEMANTIC_INDEX.md`
7. `20260815_2343__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__SEMANTIC_INDEX.md` — historical invalid under current governance
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
