# R10 artifact evidence

**Date:** 2026-08-10

Local execution package:

```text
NZ_SCCM_R10_1D_ENERGY_SMOOTHING_REINSERTION_CASE21_20260810.zip
SHA256 = 1b92f1c8dc5360704d773a232d8227743280fd7b5e759c4986dfbfe6c1afa8f9
```

Canonical execution files in the package include:

- `00_R10_report.md`
- `01_1D_energy_smoothing_curve.csv`
- `02_case21_same_execution_results.csv`
- `03_material_energy_contract.json`
- `04_1D_source_vs_energy_smooth.png`
- `05_energy_smoothed_surface_with_projections.png`
- `06_case21_capacity_comparison.png`
- `08_gate_decision.json`
- `MANIFEST_SHA256.json`

Final same-execution audit checkpoint:

```text
SOURCE_FOSTER Pu      = 342.3340294633849 kN
ENERGY_SMOOTHED Pu    = 368.7234641272992 kN
Energy-smoothed error = +0.11151232948064638 %
```

Formal identity boundary:

```text
R10 structural Gauss evaluator = AUDIT ONLY
R10 zero-spatial D15 production = HOLD pending R10B
```
