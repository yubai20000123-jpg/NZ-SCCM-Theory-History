# RC CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 17:12 +08:00

```text
RC_PRIORITY = WAVELENGTH CONSISTENCY / WAVEFORM REPRESENTATION
CURRENT_EXPLICIT_METHOD = UNCHANGED
PANELS_1_16_NGUYEN_CLASS = APPROXIMATE ONE-HALF-WAVE
PANELS_17_24_NGUYEN_CLASS = TWO-HALF-WAVE
PANELS_1_16_EXACT_ELL_2440 = WITHDRAWN
PANELS_17_24_EXACT_ELL_1220_PANEL_BY_PANEL = NOT_PROVEN
20260822_1656_RERUN = ENDPOINT_SENSITIVITY_ONLY
WAVEFORM_CONDITIONED_2D_PROPAGATION = PAUSED
MATERIAL_RETUNING = OFF
Z6_ACTIVESET_PROOF = DEPRIORITIZED_BY_USER
```

Superseding correction:

`semantic_v2/40_execution/20260822_1712__NZSCCM__SWARTZ_RC_WAVELENGTH_BINARY_ASSUMPTION_CORRECTION.md`

Current result card:

`current/results/NZ_SCCM_SWARTZ_RC_OBSERVED_HALFWAVE_CURRENT_20260822.md`

## Current source-level conclusion

Nguyen's wording for Panels1-16 is `approximate one half sinusoidal wave`, not an exact 2440-mm half-wave identity. Panels17-24 are classified as two half-waves, but exact equal 1220-mm local wavelength is not established specimen-by-specimen. Swartz experimental bulge locations and shapes are not strictly identical within the nominal groups.

## Mathematical consequence

An intermediate physical/effective wavelength cannot simply be inserted into the same full-panel one-term Navier sine while preserving exact simply-supported end conditions. It may represent a localized bulge, unequal local half-waves, or a finite mixture of admissible integer modes.

## Next RC step

Before any further 1D/2D ultimate-load rerun:

1. recover/measure source-supported per-panel bulge/nodal locations where possible;
2. construct a wavelength/effective-shape ledger with `ell_obs/b` or bounded intervals;
3. test within-pair and within-group consistency;
4. decide whether the formal representation should remain a discrete Navier mode, use a finite mode mixture, or define a source-closed local representative half-wave;
5. only then rerun capacity.

```text
NEXT_RC_TASK = PER_PANEL_WAVELENGTH_CONSISTENCY_AND_REPRESENTATION_AUDIT
```
