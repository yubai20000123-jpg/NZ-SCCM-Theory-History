# NZ-SCCM semantic_v2 tree delta — 2026-08-20 14:30

## New active material checkpoint

`semantic_v2/20_theory/20260820_1430__NZSCCM__NC_M2_SINGLE_FORM_NINE_GRID_CONSTITUTIVE_CANDIDATE.md`

Status: `ACTIVE_MATERIAL_CANDIDATE / NOT_YET_PRODUCTION_LOCK`

## New execution/audit checkpoint

`semantic_v2/40_execution/combined/20260820_1430__NZSCCM__NC_M2_CURVE_AUDIT_AND_ARTIFACT_REPORT.md`

## Supersession / rejection

NC-M1 multi-segment candidate is rejected for production use because apparent formula simplicity was achieved by adding internal thresholds, piecewise branches and min/max logic. It remains diagnostic history only.

## Current material-design rule

Use the user's 3x3 principal-strain classification as the only top-level material partition. Inside each physical CC / TC / CT / TT cell, prefer one explicit formula. A short rational function is considered simpler than several piecewise linear branches if it reduces state logic and integration complexity.

## Current NC-M2 formulas

- Compression: `C(c)=2c/(1+c^2)`
- Tension: `T(t)=t/(1-t+t^2)`
- TC/CT softening: `beta(t)=1/(1+0.15t^2)`
- CC enhancement: `eta(c1,c2)=1+0.16*C(c1)*C(c2)`

No Case21 Pu calibration has been used.
