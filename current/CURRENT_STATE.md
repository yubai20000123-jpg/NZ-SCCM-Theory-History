# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-18 14:21 +08:00  
**Status:** `UNIFIED_YUN_IDEAL_EP_LOCAL_AMPLITUDE_Z1_Z4_RECALC = EXECUTED`

## Canonical current-state artifact

`semantic_v2/00_index/20260818_1421__NZSCCM__PROJECT__CURRENT_STATE_UNIFIED_YUN_IEP_Z1_Z4_RECALC__SEMANTIC_INDEX.md`

## Controlling execution artifact

`semantic_v2/40_execution/steel_shell/20260818_1421__NZSCCM__Z1_Z4__UNIFIED_YUN_IDEAL_EP_LOCAL_AMPLITUDE_FULL_RECALC.md`

Current face-shell interpretation:

```text
Yun/Karman local-amplitude geometry = retained continuously
pointwise scalar longitudinal ideal-EP steel = active
first yield = material event, not Yun branch deletion
one Yun Galerkin R_Ai row per real local subpanel = retained
old radial-cap/J2 face operator = not the active Z1/Z4 route
```

Current recalculated decimal-localized values:

```text
Z1 Pu ~= 14.44689544 MN
Z4 Pu ~= 52.43155584 MN
```

No comparator was used in the solve.

## Formal counters retained

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

The formal target remains analytic/General-D15 zero-spatial. Any direct-continuum evaluator used to print decimal coordinates is audit/localization only.

## Superseded current-stop interpretation

The 2026-08-18 12:01 `STEEL_SHELL_SOURCE_CONSISTENT_PLANE_STRESS_OPERATOR_GATE = OPEN` entry is retained as history but is no longer the active operational stop for the unified Yun-IEP steel-shell route.

Likewise, the 14:01 inference `sigma_cr,Yun > fy -> Yun inactive` is superseded. The numerical event-ordering calculation itself remains historical evidence; only that branch-deletion inference is withdrawn.
