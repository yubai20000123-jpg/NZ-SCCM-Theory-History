# CONTENT SEMANTIC IDENTITY RULE — 2026-08-13

**Status:** CURRENT GOVERNANCE / REPOSITORY-STRUCTURE CORRECTION

## 0. Root cause

The repository path and filename are not reliable semantic identities. In particular, tokens such as `current`, `fresh`, `closure`, `production`, `PASS`, a date, or an `R/V` label must not be interpreted as current-valid status without reading the file content and its supersession chain.

This rule is introduced because the active repository currently contains legacy/current mixtures and misleading names. The defect is repository semantic indexing, not search precision.

## 1. Mandatory identity order

For every artifact used in theory recovery, execution recovery, result comparison, or continuation, identity must be determined in this order:

1. read the artifact content;
2. identify what equations/data/code/results it actually contains;
3. identify explicit self-declared role/status inside the content;
4. check later current/governance supersession, revocation, rollback, correction, or incorporation;
5. only then use path, filename and timestamp as locator metadata.

`PATH_NAME_ONLY_CLASSIFICATION = PROHIBITED`.

## 2. Path does not confer status

The following implications are invalid:

```text
current/* -> CURRENT                 INVALID
history/* -> INVALID                 INVALID
*FRESH* -> CURRENT                   INVALID
*PRODUCTION* -> CURRENT              INVALID
*PASS* -> CURRENT                    INVALID
newer_timestamp -> automatically governing  INVALID
```

A file under `current/` may be historical, superseded, diagnostic, or retained lineage. A file under `history/` may contain the only original execution evidence for a currently relevant calculation lineage.

## 3. Required semantic manifest

Important artifacts must be registered in a content-derived semantic manifest with at least:

```text
artifact_path
content_role
content_identity
current_status
supersedes
superseded_by_or_incorporated_by
contains_theory
contains_code
contains_inputs
contains_roots
contains_derivatives
contains_KZ
case_coverage
material/compiler identity
execution identity
notes
```

Unknown fields must be recorded as `UNKNOWN_NOT_CONTENT_AUDITED`; they must not be inferred from the filename.

## 4. Current repository contamination warning

Until a full content audit and controlled migration is completed:

```text
CURRENT_DIRECTORY_SEMANTIC_PURITY = FALSE
FILENAME_SEMANTIC_RELIABILITY = FALSE
DESTRUCTIVE_RENAME_MOVE_DELETE = PROHIBITED_WITHOUT_CONTENT_AUDIT
```

Do not clean the tree by filename alone. First classify content, then move/rename only after the semantic manifest is complete enough to preserve provenance and supersession.

## 5. Recovery rule

When recovering a result such as Swartz24 Cases1–18 roots, do not search only for filenames containing `Swartz`, `root`, `current`, `Pu`, or a date. Instead inspect the contents of candidate result CSV/JSON/MD/code/audit files and follow explicit values, equations, code identities, supersession statements and commit chronology.

## 6. Immediate verified examples

The following examples are already content-audited and prove the problem:

- `current/results/NZ_SCCM_SWARTZ24_FRESH_BLIND_THEORY_RESULTS_20260811.csv` contains the old direct-N48 Swartz24 roots/results (e.g. Case1 Pu=599.515895 kN), not the final current C1/MM + general-D15 result set. Its path/name is therefore semantically misleading.
- `current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_ANALYTIC_LIMIT_TANGENT_UNIFIED_THEORY_20260812_1734.md` self-declares `CURRENT GOVERNING THEORY BASELINE` at 17:34.
- `current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_PRODUCTION_THEORY_CONTRACT_20260812_2245.md` is later and self-declares `CURRENT PRODUCTION THEORY + EXECUTION CONTRACT`, incorporating the successful Swartz24 production chain and formal updates.
- `current/CURRENT_STATE.md` still points to the 17:34 theory as its primary theory entry, so the current pointer layer and the later production-contract layer are not fully synchronized.
- `current/README.md` claims old routes are all in `history/`, while the actual `current/theory/` tree still contains numerous old exploratory PF1/M1R/R09 and related artifacts.

These examples establish a repository information-architecture defect, not a keyword-search defect.

## 7. Current action boundary

This rule changes no theory, no result and no calculation. It only changes how repository artifacts are identified and recovered.
