# RC CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 17:25 +08:00

```text
RC_PRIORITY = WAVEFORM REPRESENTATION FROM RAW PER-PANEL EVIDENCE
CURRENT_EXPLICIT_METHOD = UNCHANGED
RAW_SWARTZ_TABLE2_PER_PANEL_BULGE_LOCATION = RECOVERED
BINARY_ELL_1220_2440_AS_EXPERIMENTAL_INPUT = REJECTED
PANELS_1_16_NGUYEN_CLASS = APPROXIMATE ONE-HALF-WAVE / FE GROUP IDEALIZATION
PANELS_17_24_NGUYEN_CLASS = TWO-HALF-WAVE / FE GROUP IDEALIZATION
EXACT_PER_PANEL_EXPERIMENTAL_SINE_WAVELENGTH = NOT_SOURCE_CLOSED
GROUP1_RAW_MORPHOLOGY = HETEROGENEOUS
GROUP2_RAW_MORPHOLOGY = RELATIVELY_CONSISTENT_MOSTLY_MIDDLE
GROUP3_RAW_MORPHOLOGY = HETEROGENEOUS_MULTI_ZONE
PANEL21_TWO_HALFWAVE_EXPERIMENT_LINK = STRONGEST_SOURCE_CASE
CURRENT_M2_ALL24_EXPERIMENTAL_WAVEFORM_VALIDATION = FAIL
20260822_1656_RERUN = ENDPOINT_SENSITIVITY_ONLY
WAVEFORM_CONDITIONED_2D_PROPAGATION = PAUSED
MATERIAL_RETUNING = OFF
Z6_ACTIVESET_PROOF = DEPRIORITIZED_BY_USER
```

Current detailed audit:

`semantic_v2/40_execution/20260822_1725__NZSCCM__SWARTZ24_PER_PANEL_BULGE_LOCATION_AND_EFFECTIVE_WAVELENGTH_AUDIT.md`

Per-panel evidence CSV:

`semantic_v2/40_execution/rc/20260822_1725__NZSCCM__SWARTZ24_PER_PANEL_BULGE_LOCATION_EVIDENCE.csv`

## Key correction

Swartz Table2 reports per-panel `buckling location / locations of bulges`, not an exact sinusoidal half-wave length. Explicit fractions such as `Top 2/3` can be converted to a region-length surrogate (for a=2440 mm, 2/3 a = 1626.7 mm) to show the spatial scale, but that number is not automatically an exact production `ell_eff`.

The raw experiment therefore falsifies a binary per-panel experimental wavelength assignment. Group1 and Group3 are morphologically heterogeneous; Group2 is mostly `Middle` and is relatively consistent in peak-zone location, but still does not provide a numerical common half-wave length.

Nguyen's `1-16 approx one halfwave / 17-24 two halfwaves` remains valid as a **group-level FE idealization**, not as 24 exact experimental wavelength measurements.

## Next RC step

Do not rerun 2D capacity yet. First define a boundary-compatible finite waveform representation that can express the raw unequal/localized bulge evidence without using experimental failure load in coefficient selection.

Two mathematical candidates remain open:

1. a source-closed local representative halfwave with continuous `ell_eff` plus a valid full-panel embedding;
2. a small finite global Navier mixture (first candidate: m=1 + m=2), with coefficients selected by tangent stability/current structural equations rather than Pf.

```text
NEXT_RC_TASK = FINITE_BOUNDARY_COMPATIBLE_WAVEFORM_PARAMETERIZATION_FROM_RAW_LOCATION_EVIDENCE
```
