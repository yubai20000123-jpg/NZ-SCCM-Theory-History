# CURRENT WORKSPACE

## Important: directory name is not semantic status

This directory is **not presently semantically pure**. It contains a mixture of current production artifacts, retained predecessors, historical result tables, correction audits and old exploratory branches. Therefore a file must not be treated as current-valid merely because it is under `current/`.

Mandatory entry points:

1. `CONTENT_INDEX.md`
2. `CONTENT_SEMANTIC_MANIFEST_20260813.csv`
3. `CURRENT_STATE.md`
4. `../governance/CONTENT_SEMANTIC_IDENTITY_RULE_20260813.md`

```text
PATH_NAME_IS_LOCATOR_ONLY = YES
PATH_NAME_CONFERS_CURRENT_STATUS = NO
CONTENT_AUDIT_REQUIRED_BEFORE_USE = YES
```

The previous statement that this directory contains only files directly used for the next step is no longer relied upon as a factual description of the actual tree. The actual recursive tree shows old PF1/M1R/R09-era artifacts and superseded Swartz24 result tables still under `current/`.

Do not perform destructive cleanup by filename. First classify content in the semantic manifest; only then may a later controlled migration move/rename artifacts while preserving provenance and supersession.
