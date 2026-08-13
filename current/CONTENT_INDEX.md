# CONTENT INDEX — semantic entry point

**Purpose:** locate artifacts by what they actually contain, not by directory or filename.

## Mandatory warning

`current/` is presently **legacy-contaminated**: it contains current production artifacts, retained predecessors, historical result tables, correction audits, and old exploratory branches. Therefore:

```text
PATH_NAME_IS_LOCATOR_ONLY = YES
PATH_NAME_CONFERS_CURRENT_STATUS = NO
FILENAME_TOKEN_FRESH_CURRENT_PRODUCTION_PASS_IS_AUTHORITATIVE = NO
CONTENT_AUDIT_REQUIRED_BEFORE_USE = YES
```

The repository semantic-identity rule is:

- `governance/CONTENT_SEMANTIC_IDENTITY_RULE_20260813.md`

The first content-derived manifest is:

- `current/CONTENT_SEMANTIC_MANIFEST_20260813.csv`

This manifest is intentionally incomplete rather than inferred from names. `UNKNOWN_NOT_CONTENT_AUDITED` / partial status is preferable to a guessed identity.

## Current verified primary production chain

For current ordinary-concrete + rebar RC panel production, the content-audited primary execution contract is:

- `current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_PRODUCTION_THEORY_CONTRACT_20260812_2245.md`

The 17:34 unified theory remains the mechanics baseline incorporated into the later production contract:

- `current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_ANALYTIC_LIMIT_TANGENT_UNIFIED_THEORY_20260812_1734.md`

Final Case21 current state is indexed in:

- `current/CURRENT_STATE.md`
- `current/results/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_THEORY_FREEZE_20260812_1802.md`
- `current/results/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_FULL_CLOSURE_20260812_1802.md`

Final Swartz24 current Pu table is:

- `current/results/NZ_SCCM_SWARTZ24_CURRENT_FRESH_PU_FAILURE_COMPARISON_20260813_0047.csv`

The current completion report prints current roots only for Cases19–24:

- `current/results/NZ_SCCM_SWARTZ24_FRESH_PU_COMPLETION_FAILURE_COMPARISON_AND_EXTERNAL_PANEL_SCREEN_20260813_0047.md`

## Known misleading artifact

`current/results/NZ_SCCM_SWARTZ24_FRESH_BLIND_THEORY_RESULTS_20260811.csv` is **not** the current C1/MM + general-D15 root table. Its contents are the superseded old direct-N48 Swartz24 roots/results. It must not be selected as current merely because it lives under `current/results/` and contains `FRESH` in its filename.

## Migration boundary

No destructive move/rename/delete should be done until content classification is sufficiently complete. The immediate job is to read and classify contents, then build a clean semantic tree from the manifest rather than reorganize by filename guesses.
