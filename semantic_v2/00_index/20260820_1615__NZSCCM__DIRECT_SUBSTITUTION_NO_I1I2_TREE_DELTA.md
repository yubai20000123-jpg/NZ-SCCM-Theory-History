# NZ-SCCM semantic_v2 tree delta — 2026-08-20 16:15

## New theory checkpoint

`semantic_v2/20_theory/20260820_1615__NZSCCM__NC_M4_DIRECT_SUBSTITUTION_NO_I1I2_AUDIT.md`

## Main correction

- `I1/I2` is no longer treated as a formal theory layer.
- Formal chain is restored to:
  `Nguyen second-order strain field -> NC-M4 current operator -> sigma_x, sigma_y, tau_xy -> R_A, R_m, P`.
- Direct matrix-function audit shows:
  - CC can be represented as a rational 2x2 matrix function without explicit principal-strain radicals;
  - TT can be represented as a rational 2x2 matrix function without explicit principal-strain radicals;
  - TC/CT remains the only branch where the current positive/negative principal-direction asymmetry introduces an explicit spectral square root under direct Cartesian evaluation.

## Current material-complexity diagnosis

The root/spectral complexity is not created by the discarded `I1/I2` variables. It is caused by the mixed TC/CT law assigning different scalar functions to the tensile and compressive principal directions.

Current recommended material-focus task:

`TC/CT direct 2x2 current-operator simplification while preserving the physical trend that increasing tensile strain reduces compressive capacity.`
