# NZ-SCCM — RC two-slope full-2D three-panel current result

**Updated:** 2026-08-22 19:27 +08:00  
**Status:** `EXECUTED / MATERIAL_FUNCTIONS_FROZEN / TWO_SLOPE_SECTION_PASS / DIAGNOSTIC_EVENTS_NOT_PRODUCTION_Pu`

Detailed execution:

`semantic_v2/40_execution/20260822_1927__NZSCCM__PANEL1_14_21_TWO_SLOPE_FULL2D_MATERIAL_LIMIT_DIAGNOSTIC.md`

Reproduction:

`semantic_v2/40_execution/rc/20260822_1927__NZSCCM__PANEL1_14_21_TWO_SLOPE_FULL2D_SECTION_DIAGNOSTIC.py`

## Two-slope interface

\[
\lambda_x(z)=a_x+b_xz,\qquad
\lambda_y(z)=a_y+b_yz.
\]

This allows the frozen source waveform to transmit `Nx, Ny, Mx, My` simultaneously into the section material state. Formal concrete section integration and same-law Jacobian remain exact finite analytic calculations with zero spatial quadrature/material points.

## Current diagnostic events

|Panel|event|P_event / kN|Pf / kN|difference|
|---:|---|---:|---:|---:|
|1|current-map section fold|589.0817|490.1940|+20.173%|
|14|lower y-rebar compression-yield active-set terminal|770.5483|716.1637|+7.594%|
|21|current-map section fold|192.6906|368.3127|−47.683%|

## Material reading

- Panel1: equilibrated thickness `CC -> TC`; current TC-R2 `gamma_c` never activates before terminal. Even at the measured failure load, the source TC transition measure is already about `1.321`, while current `gamma_c=1`. Primary open material issue: postcrack TC interaction/compression degradation begins too late in the current reduction.
- Panel14: equilibrated thickness `CC -> TC`, but the terminal is a longitudinal rebar active-set kink. It is not a clean concrete CC/TC calibration panel under the current perfect-plastic reduced steel law.
- Panel21: equilibrated terminal is `TC -> CC`, not `CC -> TC -> TT`. The fold is overwhelmingly transverse-tension tangent controlled and occurs far too early. Primary open material issue: the current universal Foster `alpha2=0.3` suppresses source reinforcement/bond dependence and likely makes high-reinforcement tension stiffening too weak.

```text
PANEL21_TT_AT_EQUILIBRATED_TERMINAL = NO
TC_R2_GAMMA_ACTIVE_AT_TERMINALS = NO_ALL_3
NC_CC_REOPEN_FROM_THIS_AUDIT = NO
TT_REOPEN_FROM_THIS_AUDIT = NO_FIRST_PRIORITY
PRIMARY_MATERIAL_REOPEN_1 = REINFORCEMENT_DEPENDENT_TENSION_STIFFENING
PRIMARY_MATERIAL_REOPEN_2 = POSTCRACK_TC_INTERACTION_BEFORE_GAMMA_ONSET
PANEL14_CONCRETE_DIAGNOSTIC = BLOCKED_BY_REBAR_ACTIVESET
MATERIAL_PARAMETER_REFIT = NO
```
