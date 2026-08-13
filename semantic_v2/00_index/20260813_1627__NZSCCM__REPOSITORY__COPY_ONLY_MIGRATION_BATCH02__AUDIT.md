# Copy-only migration Batch 02 audit

Time basis: 2026-08-13 16:27 +08:00

## Scope

Batch 02 preserves the historical and diagnostic records needed to answer the user's original rebuild question: why prediction accuracy appeared to worsen after several changes.

All migrated historical artifacts reuse their exact legacy Git blob SHA. The newly authored root-cause audit is metadata/analysis only and does not modify theory or numerical result bodies.

```text
BYTE_IDENTICAL_HISTORICAL_COPIES = YES
LEGACY_PATHS_PRESERVED = YES
THEORY_BODY_CHANGED = NO
RESULT_BODY_CHANGED = NO
CURRENT_PRODUCTION_STATUS_CHANGED = NO
ACCURACY_ROOT_CAUSE_AUDIT_ADDED = YES
```

## Main finding at this checkpoint

The direct-N48 -> current C1/MM+general-D15 transition does not show a large whole-sample accuracy collapse: old and current 24-panel MAE are both about 12.06%. However, a systematic groupwise Pu shift exists. For Case21, about 98.95% of the old-to-current Pu shift entered at the compiler representation change, while later finalization changed only about 0.027 kN.

The representation change was mechanically motivated because old direct-N48 failed R10 first-tangent fidelity. Strict C1/MM restores that tangent identity but changes primitive value fidelity at fixed degree 48. This value/tangent trade-off is the current leading explanation for the systematic Pu shift.

A separate intermediate Case21 result was invalidated by a general-D15 Qq contraction mismatch, and an old comparison also confused 336 kN buckling/critical load with the approximately 368.313 kN failure/ultimate load. Those are execution/provenance errors, not evidence for changing R10.

## Next gate

Search older-than-2026-08-11 Swartz24/Case21 result stages, normalize all Pu comparisons to experimental failure/ultimate load, and identify whether the user-remembered more-accurate stage genuinely predates direct-N48.
