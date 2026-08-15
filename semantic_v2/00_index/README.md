# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260816_0047__NZSCCM__PROJECT__CURRENT_STATE_ZHOU_END_RESTRAINT_PF_SERIES_AND_AR2_MAPPING__SEMANTIC_INDEX.md`

Current locked status:

```text
STRICT_ZERO_SPATIAL_INTEGRATION = ACTIVE
CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT_GATE = PASS
ZHOU_SOURCE_LOADED_EDGE_UX_ZERO = CONFIRMED
ZHOU_SIDE_INPLANE_FREE = CONFIRMED
p20,p02 AS INDEPENDENT FREE MEMBRANE COORDINATES = RETIRED
EXACT_SIDE_FREE_FVK_AIRY_CORRECTION = PASS
PAPKOVICH_FADLE_EVEN_EIGENFAMILY = DERIVED
SIDE_TRACTION_FREE_PER_PF_MODE = PASS
FORMAL_TRANSVERSE_END_RESTRAINT_PF_SERIES = CLOSED
N6_EXACT_MOMENT_TRUNCATION = PASS_AS_COEFFICIENT_SPACE_REPRO
AR2_M2_ONE_HALFWAVE_MAPPING = PASS
FICTITIOUS_INTERNAL_UX_ZERO = PROHIBITED
FULL_ZHOU_ALL_INPLANE_END_DOF_EQUIVALENCE = NOT_YET_PROVEN
R10/N48/D15 NONLINEAR MAPPING = BLOCKED_PENDING_NEXT_GATE
NEW_Z6_Pu = NOT CALCULATED
Pu_40.97334_MN = RETRACTED / INVALID FOR CURRENT PROJECT
```

The 00:47 stage closes the previously open x-dependent transverse loaded-end residual with a homogeneous even Papkovich–Fadle biharmonic strip series. The series satisfies free lateral tractions mode by mode and uses exact coefficient moments only; no spatial quadrature, spatial sampling, point collocation or spatial subdivision is used.

For the requested AR2 object (`a/b=2,m=2,ell=b`), one complete out-of-plane halfwave is exactly the physical half-panel from one loaded end to the midheight symmetry plane. The PF end layer therefore maps onto the one-halfwave domain without imposing the physical `ux=0` restraint at the internal halfwave interface.

Current next execution:

`AR2_PF_BOUNDARY_MEMBRANE_TO_R10_N48_D15_ZERO_QUADRATURE_MAPPING_GATE`

That gate must construct a nonlinear-material-compatible displacement/strain or rigorously equivalent mixed representation whose elastic limit reproduces the present PF/FvK closure. The elastic Airy stress field may not simply be transplanted as the nonlinear R10/N48 stress field.

## Repository semantic read order

1. `20260816_0047__NZSCCM__PROJECT__CURRENT_STATE_ZHOU_END_RESTRAINT_PF_SERIES_AND_AR2_MAPPING__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_0047__NZSCCM__ZHOU_END_RESTRAINT_PAPKOVICH_FADLE_ZERO_QUADRATURE__LOCK.md`
3. `../20_theory/nc_steel_shell_panel/20260816_0047__NZSCCM__ZHOU_END_RESTRAINT_PAPKOVICH_FADLE_SERIES__THEORY.md`
4. `../40_execution/steel_shell/20260816_0047__NZSCCM__ZHOU_END_RESTRAINT_PF_SERIES__EXECUTION_REPORT.md`
5. `../40_execution/steel_shell/20260816_0047__NZSCCM__ZHOU_END_RESTRAINT_PF_SERIES__PARAMS_AND_INTERMEDIATES.json`
6. `../40_execution/steel_shell/20260816_0047__NZSCCM__ZHOU_END_RESTRAINT_PF_SERIES__REPRO.py`
7. `../60_validation/steel_shell/20260816_0047__NZSCCM__ZHOU_END_RESTRAINT_PF_SERIES_AND_AR2_HALFWAVE_MAPPING__AUDIT.md`
8. `20260816_0016__NZSCCM__PROJECT__CURRENT_STATE_ZHOU_BOUNDARY_FVK_MIXED_BC_GATE__SEMANTIC_INDEX.md`
9. `20260816_0007__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT_GATE_PASS__SEMANTIC_INDEX.md`
10. `20260815_2358__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_POSTBUCKLING_REDERIVATION_GATE__SEMANTIC_INDEX.md`
11. `20260815_2343__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__SEMANTIC_INDEX.md` — historical invalid under current governance
12. `20260815_2306__NZSCCM__PROJECT__CURRENT_STATE_D055_DIRECTIONAL_CONTINUATION_REPRESENTATION_GATE__SEMANTIC_INDEX.md`
13. `20260815_2235__NZSCCM__PROJECT__CURRENT_STATE_D050_DIRECTIONAL_MOMENT_FIRST_CERTIFICATE__SEMANTIC_INDEX.md`
14. `20260815_2220__NZSCCM__PROJECT__CURRENT_STATE_UPDATED_FVK_THEORY_AND_EXPANSION_AUDIT__SEMANTIC_INDEX.md`
15. `20260815_2144__NZSCCM__PROJECT__CURRENT_STATE_R20_R02_PROJECTION_AND_MEMBRANE_ACTIVATION__SEMANTIC_INDEX.md`
16. `20260815_2134__NZSCCM__PROJECT__CURRENT_STATE_MINIMAL_FVK_MEMBRANE_COMPLETION__SEMANTIC_INDEX.md`
17. `20260815_2118__NZSCCM__PROJECT__CURRENT_STATE_POSTBUCKLING_MEMBRANE_COMPATIBILITY_AUDIT__SEMANTIC_INDEX.md`
18. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`
19. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_SEMANTIC_TREE__SEMANTIC_MANIFEST.md`
20. `20260813_1328__NZSCCM__REPOSITORY__AUDITED_ARTIFACTS__SEMANTIC_MANIFEST.csv`
21. `20260813_1328__NZSCCM__REPOSITORY__ARTIFACT_SUPERSESSION__SUPERSESSION_MAP.csv`
22. `20260813_1328__NZSCCM__REPOSITORY__LEGACY_TO_CANONICAL__RENAME_MAP.csv`
23. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_AUDIT_COVERAGE_AND_FRONTIER__AUDIT.md`
24. `20260813_1604__NZSCCM__REPOSITORY__SEMANTIC_MAP_CROSSCHECK_CORRECTIONS__AUDIT.md`
25. `20260813_1604__NZSCCM__REPOSITORY__CONTROLLED_PHYSICAL_MIGRATION_READINESS__AUDIT.md`

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
