# Copy-only migration Batch 03 audit

Time basis: 2026-08-13 16:27 +08:00

Batch 03 copies the principal pre-2026-08-11 Case21 historical branches that are useful for reconstructing how the current zero-spatial theory evolved: nested-D15, direct analytic/CAS, revoked piecewise analytic, G31 locator, and selected policy/compiler reports.

All copied artifacts reuse the exact existing Git blob. Legacy paths remain intact.

```text
BYTE_IDENTICAL_COPY = YES
LEGACY_PATHS_PRESERVED = YES
CURRENT_THEORY_CHANGED = NO
CURRENT_RESULTS_CHANGED = NO
HISTORICAL_REJECTED_ROUTE_PROMOTED = NO
MISSING_G31_ORIGINAL_TEXT = ALLOWED_GAP_WITH_LOCATOR
```

A notable historical value in the nested-D15 local-validation snapshot is Pu approximately 342.108 kN. That snapshot was not a reproducible production closure and must not be compared against the current theory without first using the same experimental quantity. The current Pu validation target is failure/ultimate load, not the 336 kN buckling/critical-load quantity that appeared in some historical Case21 records.
