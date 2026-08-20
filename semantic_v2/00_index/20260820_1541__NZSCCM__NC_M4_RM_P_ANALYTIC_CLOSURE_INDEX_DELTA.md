# NZ-SCCM semantic_v2 tree delta — 2026-08-20 15:41

## New theory checkpoint

`semantic_v2/20_theory/20260820_1541__NZSCCM__NC_M4_RM_P_ANALYTIC_CLOSURE_AUDIT.md`

Key result:

- TT / CC rewritten as invariant rational matrix operators;
- TC / CT rewritten with one quadratic radical and no explicit principal-angle rotation;
- through-thickness analytic closure established;
- `R_m` and `P` reduced from triple integrals to exact thickness-condensed 2D continuous integrals.

## New execution checkpoint

`semantic_v2/40_execution/combined/20260820_1541__NZSCCM__NC_M4_RM_P_CAS_CLOSURE_REPORT.md`

CAS evidence:

- TT exact thickness primitive returned (`RootSum + Log`);
- CC exact thickness primitive returned (rational + `RootSum + Log`);
- TC/CT exact primitive returned but fully expanded expression is extremely large;
- generic naive SymPy symbolic rational integration timed out at 60 s.

## Current gates

- `THICKNESS_ANALYTIC_CLOSURE = PASS`
- `GENERAL_RECTANGLE_OUTER_2D_SHORT_CLOSED_FORM = NOT_YET_PASS`
- `CASE21_PU = NOT_STARTED_IN_NC_M4`
- `N_formal_spatial_sampling = 0`
- `N_formal_spatial_quadrature = 0`

## Current recommended next task

Continue with the outer `(x,y)` exact analytic compiler after thickness condensation, using tangent-half-angle variables and compact algebraic / RootSum / special-function objects. Do not reopen material fitting and do not revert to spatial quadrature.
