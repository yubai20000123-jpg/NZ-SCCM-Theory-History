# NZ-SCCM repository copy-only rebuild governance

Time basis: 2026-08-13 16:27 +08:00

## Purpose

The repository rebuild exists primarily to diagnose why several later theory/execution changes reduced predictive accuracy compared with earlier successful stages. The rebuild itself must not create another theory mutation.

## User-authorized recovery rule

```text
COPY_ONLY_SEMANTIC_MIGRATION = AUTHORIZED
LEGACY_TREE_DELETE = PROHIBITED_FOR_NOW
LEGACY_TREE_MOVE = NOT_REQUIRED
THEORY_REWRITE_DURING_MIGRATION = PROHIBITED
CURRENT_SUCCESSFUL_THEORY_PRESERVATION = HIGHEST_PRIORITY
MISSING_LOW_VALUE_ARTIFACT = MAY_REMAIN_UNMIGRATED
MISSING_RECOMPUTABLE_ARTIFACT = MAY_BE_RECOMPUTED_LATER
UNKNOWN_IDENTITY = MAY_BE_LEFT_BLANK_WITH_EXPLICIT_NOTE
```

## Operational interpretation

1. Read/audit high-risk theory, governance, workflow and result artifacts before classification.
2. For content whose identity is already established, create a canonical semantic_v2 path that points to the same Git blob SHA. This is a byte-identical copy, not a rewrite.
3. Preserve the legacy path so old provenance and historical links continue to resolve.
4. Source PDFs, raw datasets and other stable evidence may be copied directly once their source identity is known; they do not require a new theory interpretation merely for migration.
5. If a historical artifact is missing, ambiguous, or only useful for a calculation that can be reproduced, do not block the rebuild. Leave an explicit gap and continue.
6. The minimum successful rebuild is a self-contained preserved current production theory plus the key historical comparison artifacts needed to explain accuracy degradation.

## Non-goals

The migration does not calibrate materials, change Pu/Pcr definitions, change root-selection logic, or modify any numerical result.
