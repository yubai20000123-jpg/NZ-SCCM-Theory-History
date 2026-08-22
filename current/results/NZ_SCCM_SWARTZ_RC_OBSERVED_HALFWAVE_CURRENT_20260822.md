# NZ-SCCM — Swartz RC wavelength current result

**Updated:** 2026-08-22 17:12 +08:00  
**Status:** `BINARY_1220_2440_MAPPING_SUPERSEDED / ENDPOINT_SENSITIVITY_RETAINED / EXACT_WAVELENGTH_AUDIT_REQUIRED`

Superseding correction:

`semantic_v2/40_execution/20260822_1712__NZSCCM__SWARTZ_RC_WAVELENGTH_BINARY_ASSUMPTION_CORRECTION.md`

Previous execution retained only as an endpoint sensitivity test:

`semantic_v2/40_execution/20260822_1656__NZSCCM__SWARTZ_RC_OBSERVED_HALFWAVE_CONDITIONED_EXPLICIT_RERUN.md`

Reproduction script:

`semantic_v2/40_execution/rc/20260822_1656__NZSCCM__SWARTZ_RC_OBSERVED_HALFWAVE_EXPLICIT_RERUN.py`

## Corrected source reading

Nguyen supports the following **coarse morphology classes** only:

```text
Panels 1-16: approximate one-half sinusoidal-wave class
Panels 17-24: two-sinusoidal-half-wave class
```

This does **not** justify the exact binary identities

```text
Panels 1-16: ell = 2440 mm
Panels 17-24: ell = 1220 mm panel-by-panel
```

Swartz raw experimental bulge positions/shapes are not strictly identical within nominal groups.

## Status of the 16:56 numbers

The earlier numerical table remains reproducible and useful only for sensitivity:

- `ell=2440 mm` endpoint for Cases1/2/9/10;
- `ell=1220 mm` endpoint for Cases19/20/21/22.

It is **not** the current per-panel observed-wavelength prediction table.

## Mathematical representation issue

For an exact full-panel one-term Navier sine,

\[
w=A\sin(m\pi x/a)\sin(\pi y/b),
\]

simply-supported end conditions require integer `m`, so `ell=a/m` is discrete. An effective wavelength between 1220 and 2440 mm therefore signals a non-pure-sine/localized/mixed-mode shape or a local representative half-wave, not merely a continuous replacement of `ell` in the same global one-term sine.

## Current next task

```text
PER_PANEL_WAVELENGTH_LEDGER = REQUIRED
WAVEFORM_CONDITIONED_2D = PAUSED
MATERIAL_RETUNING = OFF
NEXT_RC_TASK = WAVELENGTH_CONSISTENCY_AND_REPRESENTATION_AUDIT
```
