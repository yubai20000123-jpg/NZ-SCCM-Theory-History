# Case21 execution semantic branch

Current resumable Case21 inputs are represented by two canonical locators:

- `20260812_1734__NZSCCM__CASE21__GEOMETRY_MATERIAL_REBAR_COMPILER_INTERVAL__INPUT_FREEZE.LOCATOR.md`
- `20260812_1802__NZSCCM__CASE21__R10_N48C1MM_U_C_T_T7__COEFFICIENT_TABLE.LOCATOR.md`

Together they identify the frozen geometry/material/rebar/compiler interval and the final 49x4 U/C/T/T7 coefficient set used by the current Case21 calculation.

The result files live under `semantic_v2/50_results/case21/`; historical candidate coefficients and obsolete tail/Chebyshev artifacts live under `semantic_v2/80_history/case21/`.

This branch does not authorize formal spatial sampling, spatial quadrature, material-point grids or multi-cell subdivision.
