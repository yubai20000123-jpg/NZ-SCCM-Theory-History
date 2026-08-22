# RC CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 17:40 +08:00

```text
RC_PRIORITY = OBSERVED WAVEFORM AS EXOGENOUS IMPERFECTION INPUT FOR MATERIAL DIAGNOSTICS
CURRENT_EXPLICIT_METHOD = UNCHANGED
RAW_SWARTZ_TABLE2_PER_PANEL_BULGE_LOCATION = RECOVERED
BINARY_ELL_1220_2440_AS_EXPERIMENTAL_INPUT = REJECTED
EXACT_PER_PANEL_EXPERIMENTAL_SINE_WAVELENGTH = NOT_SOURCE_CLOSED
OBSERVED_NONSTANDARD_WAVEFORM = PRESCRIBED_INPUT / NOT_PREDICTED
SELF_GROWN_WAVEFORM = OFF
TANGENT_MODE_GATE_AS_CURRENT_PRIORITY = OFF
WAVEFORM_COEFFICIENTS_FROM_GEOMETRY_EVIDENCE = ALLOWED
WAVEFORM_COEFFICIENTS_FROM_Pf = PROHIBITED
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
MATERIAL_RETUNING_BEFORE_WAVEFORM_DIAGNOSTIC = OFF
Z6_ACTIVESET_PROOF = DEPRIORITIZED_BY_USER
```

Governing correction:

`semantic_v2/20_theory/20260822_1740__NZSCCM__RC_OBSERVED_WAVEFORM_AS_EXOGENOUS_IMPERFECTION_INPUT.md`

Per-panel raw evidence audit:

`semantic_v2/40_execution/20260822_1725__NZSCCM__SWARTZ24_PER_PANEL_BULGE_LOCATION_AND_EFFECTIVE_WAVELENGTH_AUDIT.md`

Per-panel evidence CSV:

`semantic_v2/40_execution/rc/20260822_1725__NZSCCM__SWARTZ24_PER_PANEL_BULGE_LOCATION_EVIDENCE.csv`

## Current purpose

The observed nonstandard bulges are treated as casting/initial-imperfection outcomes that the current theory is not asked to predict. They are to be inserted into the current explicit structural path as prescribed geometry so that the resulting 2D material stress state and limiting event can be compared with experiment.

The diagnostic chain is:

\[
\boxed{
\text{observed waveform}
\rightarrow
\text{regenerated explicit structural demand}
\rightarrow
\text{fixed 2D material constraint/current operator}
\rightarrow
\text{material limit state / capacity}
\rightarrow
\text{post-solution comparison with experiment}
}
\]

The residual error after the observed waveform is accounted for is the quantity used to audit what the present material constraints may still be missing. The waveform is not chosen or adjusted to make `Pu` match `Pf`.

## Representation rule

A nonstandard observed shape may be frozen as a finite analytic representation, for example a finite Navier/Fourier expansion or a finite piecewise-analytic shape. Its coefficients are geometry evidence inputs, not structural unknowns. Once frozen, all formal structural integrals are evaluated exactly; digitized geometry points, if used, serve only to identify the finite shape and are not formal integration/material points.

The old `ell=2440/1220` rerun remains only an endpoint sensitivity experiment.

## Next RC task

Recover/freeze observed waveform representations for the best-supported representative panels (minimum Panel1, Panel14, Panel21; extend to other panels where source evidence is sufficient), then propagate each prescribed waveform through the unchanged explicit structural + fixed 2D material calculation.

```text
NEXT_RC_TASK = OBSERVED_WAVEFORM_TO_EXPLICIT_DEMAND_TO_2D_MATERIAL_LIMIT_DIAGNOSTIC
```
