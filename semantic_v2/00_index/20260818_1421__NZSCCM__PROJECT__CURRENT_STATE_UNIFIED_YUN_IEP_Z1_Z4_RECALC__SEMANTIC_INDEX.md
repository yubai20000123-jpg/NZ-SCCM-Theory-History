# NZ-SCCM CURRENT STATE — unified Yun + ideal-EP Z1/Z4 recalculation

**Updated:** 2026-08-18 14:21 +08:00  
**Status:** `UNIFIED_YUN_IDEAL_EP_LOCAL_AMPLITUDE_Z1_Z4_RECALC = EXECUTED`

This file supersedes `20260818_1201__NZSCCM__PROJECT__CURRENT_STATE_STEEL_SHELL_SOURCE_CONSISTENT_OPERATOR_GATE__SEMANTIC_INDEX.md` as the current operational entry. Historical radial-cap/J2 audits remain retained evidence but are not the active face-shell route for the present Z1/Z4 recalculation.

## Current active steel-shell route

The active route is the already-developed unified UCFT/R04 local-amplitude formulation:

```text
global continuous Nguyen/Karman strain field
+ local Yun finite-harmonic shape per real 200-mm steel subpanel
+ pointwise scalar longitudinal ideal elastic-perfectly-plastic steel
+ one continuous Yun Galerkin residual R_Ai for every local subpanel
+ exact/analytic General-D15 target
+ all concrete/face/web phases assembled before solve
```

`first yield` changes the steel material state but does not disable the Yun/Karman local-amplitude geometry.

No S0/S1/S2 activity-state switch is used in the current equations.

## Controlling execution artifact

`../40_execution/steel_shell/20260818_1421__NZSCCM__Z1_Z4__UNIFIED_YUN_IDEAL_EP_LOCAL_AMPLITUDE_FULL_RECALC.md`

The earlier `20260818_1401__...DIRECT_YUN_EVENT_ORDERING...md` is superseded specifically in its inference that `sigma_cr,Yun > fy` makes Yun inactive.

## Current recalculated values

```text
Z1:
  D ~= 1.33807919
  q ~= 0.0284082291
  alpha ~= 2.1411146461
  Pc ~= 7.36427864 MN
  Pface ~= 5.52501512 MN
  Pw ~= 1.55760168 MN
  Pu ~= 14.44689544 MN

Z4:
  D ~= 0.72578235
  q ~= 0.00222770385
  alpha ~= 0.0258607373
  Pc ~= 26.58171489 MN
  Pface ~= 17.43310876 MN
  Pw ~= 8.41673219 MN
  Pu ~= 52.43155584 MN
```

These are current decimal-localized values for the frozen Yun-IEP target equations. No Zhou/FE/test comparator was used in the solve.

## Formal counters retained

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

The direct continuum evaluator used in the execution report is only a decimal-localization/convergence oracle. The formal target remains finite trigonometric Yun fields + frozen current material functions + analytic-series/General-D15 exact moments.

## Immediate continuation

The active continuation is no longer to reopen a plane-stress radial-cap/J2 operator gate. The next direct engineering continuation is to apply the same unified Yun-IEP local-amplitude target to the remaining Z0/Z2/Z3/Z5 cases, then inspect the resulting full Z0-Z5 pattern and the same-state stability quantities without changing the material or local-amplitude equations.
