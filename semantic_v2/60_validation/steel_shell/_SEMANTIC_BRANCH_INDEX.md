# Steel-shell validation semantic branch

## Current preliminary gate

Primary validation:

- `20260813_1854__NZSCCM__STEEL_SHELL__ZERO_QUADRATURE_SSSS_NAVIER_ZHOU_ABAQUS__VALIDATION.md`

Reproducible execution:

- `semantic_v2/40_execution/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__ZERO_QUADRATURE_SSSS_EXACT_MOMENT_TEST.py`

Result table:

- `semantic_v2/50_results/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__SSSS_EXACT_VS_ABAQUS__RESULT_TABLE.csv`

Current verdict:

```text
FINITE_THICKNESS_STEEL_SHELL_EXACT_MOMENTS = PASS
ZERO_NUMERICAL_SPATIAL_QUADRATURE = PASS
ZERO_NUMERICAL_THICKNESS_QUADRATURE = PASS
SSSS_NAVIER_ELASTIC_DEGENERATION = PASS
OFFICIAL_ABAQUS_BENCHMARK = PASS
ZHOU_FOUR_EDGE_SSSS_ARCHITECTURE_COMPATIBILITY = PASS
ZHOU_LITERAL_NUMERICAL_FE_TABLE_REPRODUCTION = PENDING_PRIMARY_TABLE_RECOVERY
FULL_NONLINEAR_STEEL_CURRENT_MAP_COMPILER = PENDING
FULL_CONCRETE_PLUS_STEEL_SHELL_Pu = NOT_YET_PRODUCTION
```

The preliminary gate proves the integration/structural architecture. It deliberately uses the exact elastic plane-stress degeneration so that no nonlinear steel-material approximation can mask an integration error.

For the classical square SSSS plate used in the Abaqus verification problem, the exact-moment shell operator returns `Ncr=90.38099268396850`, matching the classical closed-form `90.38099268396849` at machine roundoff.
