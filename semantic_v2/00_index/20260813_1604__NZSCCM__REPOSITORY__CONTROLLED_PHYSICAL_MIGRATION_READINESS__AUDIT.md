# NZ-SCCM controlled physical migration readiness audit

**Timestamp:** 2026-08-13 16:04 +08:00  
**Mode:** post-interruption semantic-v2 completion audit  
**Theory/result change:** NONE

## 1. What is now complete enough

```text
SEMANTIC_V2_TREE = ESTABLISHED
DECLARED_LEAF_BRANCH_INDEX_COVERAGE = COMPLETE
PRIMARY_CURRENT_LOCATORS = COMPLETE_FOR_CURRENT_CHAIN
HIGH_RISK_SUPERSESSION_LOCATORS = SUBSTANTIALLY_COMPLETED
CONTENT_FIRST_NAMING_POLICY = ESTABLISHED
LEGACY_TO_CANONICAL_RENAME_MAP_13_28 = PRESENT
SUPERSESSION_MAP_13_28 = PRESENT
CROSS_MAP_CORRECTION_OVERLAY_16_04 = PRESENT
DESTRUCTIVE_PHYSICAL_RENAME = NOT_STARTED
THEORY_CHANGED = NO
RESULT_CHANGED = NO
```

## 2. Why physical migration is still held

A physical move/rename changes paths used by historical documents, source maps and recovery links. The semantic layer is now navigable, but the following migration-specific gates are not yet closed:

1. the 13:28 rename map has not yet been regenerated as a consolidated v2 incorporating the two newly closed supersession endpoints;
2. the 13:28 audited-artifact CSV still uses canonical-ID shorthand and therefore needs either regeneration or a permanent schema note before path-moving automation consumes it;
3. canonical locator coverage is intentionally selective for source/history B/C leaves; a batch migration must define which leaves move and which remain legacy-only;
4. no repository-wide internal-link/backreference dry run has yet proved that a proposed batch move leaves every startup/source/recovery reference resolvable;
5. files with section-level partial supersession must not be moved as if the whole body had one simple CURRENT/HISTORY identity.

## 3. Decision

```text
CONTROLLED_PHYSICAL_MIGRATION = HOLD
DESTRUCTIVE_MOVE_OR_DELETE = NOT_AUTHORIZED
NONDESTRUCTIVE_LOCATOR_AND_INDEX_WORK = AUTHORIZED_AND_COMPLETED_FOR_THIS_PASS
```

This is not a rollback. The repository is now in a stronger resumable state than the interrupted 14:05 checkpoint.

## 4. Next safe migration gate

Before the first physical move, generate a **dry-run migration plan** with:

- exact legacy path;
- exact canonical target path;
- status and valid/superseded scope;
- inbound references found in repository text;
- proposed locator stub after move;
- rollback commit/base SHA;
- a small first batch limited to artifacts with whole-file identity and no ambiguous partial supersession.

Recommended first physical batch, if later approved, should exclude Case21 full-closure partial-supersession files and raw/source archives. Start only with low-risk whole-file semantic-history artifacts after link verification.
