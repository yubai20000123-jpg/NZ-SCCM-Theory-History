# NZ-SCCM semantic_v2 tree delta — 2026-08-20 14:51

## Superseding correction

The previous NC-M2 tension audit over-constrained the next tensile law by treating `T(1)=1`, `T'(1)=0`, and a finite-energy-at-infinity test as hard production gates.

This is superseded by:

`semantic_v2/20_theory/20260820_1451__NZSCCM__NC_M2_TENSION_AUDIT__REMOVE_FORCED_PEAK_GATE.md`

and the curve-direction diagnostic:

`semantic_v2/40_execution/combined/20260820_1451__NZSCCM__NC_TENSION_BROAD_PEAK_SINGLE_FORM_DIAGNOSTIC.md`

## Current rule

The next tensile backbone may have its peak at `t>1` and may have a broad peak region. The key constraints are physical trend, smoothness, low operator complexity, no internal material segmentation, and acceptable behavior over the structure-relevant strain range.

The infinity-tail energy behavior remains a diagnostic consideration, not an automatic rejection gate unless a fracture-energy/crack-band formulation is explicitly adopted.

## Diagnostic formula only

`T_d(t)=t(t+0.09)/(1-0.83t+1.04t^2+0.14t^3)`

This is NOT NC-M3 and is NOT production locked. It only proves that the user-requested broad-peak/slow-softening shape is achievable with one rational expression.
