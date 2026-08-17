# NZ-SCCM semantic index — Z6 rectangular Airy / compiler reorganization

**Timestamp:** 2026-08-17 13:37 +08:00

## Current active task

```text
Z6_CONVERGENT_SERIES_FINITE_MOMENT_MATERIAL_COMPILER
```

## Trigger

The user clarified that the successful Case21 N48/CH/D15 route was intended as a reasoning precedent, not a literal compiler-copy instruction. Z6 was selected as the next diagnostic. The real Z6 mechanics branch is calculable, but fixed-N48 direct reuse over the required wide material domain fails a same-state source-fidelity gate.

## Controlling files

Governance:
- `semantic_v2/10_governance/20260817_1337__NZSCCM__Z6_RECTANGULAR_AIRY_AND_COMPILER_REORGANIZATION__LOCK.md`

Theory:
- `semantic_v2/20_theory/nc_steel_shell_panel/20260817_1337__NZSCCM__RECTANGULAR_AIRY_SCALAR_AND_CONVERGENT_SERIES_FINITE_MOMENT_COMPILER__THEORY.md`

Execution:
- `semantic_v2/40_execution/steel_shell/20260817_1337__NZSCCM__Z6_RECTANGULAR_AIRY_DIRECT_R10_AND_N48_FIXED_STATE_GATE__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260817_1337__NZSCCM__Z6_RECTANGULAR_AIRY_DIRECT_R10_AND_N48_FIXED_STATE_GATE__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260817_1337__NZSCCM__Z6_RECTANGULAR_AIRY_AND_COMPILER_GATE__REPRO.py`

## Current state

```text
REAL_Z6 = a9000 / b12000 / ell9000 / k=4/3 / q0=.0015
VIRTUAL_AR2_AS_Z6 = PROHIBITED
RECTANGULAR_AIRY_DIRECTION = DERIVED_AND_ELASTICALLY_CHECKED
DIRECT_R10_Z6_MECHANICS = CALCULABLE_AUDIT_ONLY
DIRECT_R10_AUDIT_Pu ~= 43.46 MN
WIDE_FIXED_N48_SAME_STATE_CONCRETE_ERROR ~= -10.4%
FORMAL_Z6_Pu_FROM_WIDE_FIXED_N48 = NOT_RELEASED
NEXT = CONVERGENT_SERIES + TERM-BY-TERM CH + FINITE EXACT D15 TARGET MOMENTS
```

## Formal counters

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```
