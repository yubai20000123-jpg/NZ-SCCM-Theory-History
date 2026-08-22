# RC CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 19:27 +08:00

```text
RC_PRIORITY = SOURCE_WAVEFORM FULL2D MATERIAL-CONSTRAINT DIAGNOSTIC
CURRENT_EXPLICIT_METHOD = GENERALIZED WITHOUT CHANGING LOW-DIMENSIONAL ARCHITECTURE
OBSERVED_NONSTANDARD_WAVEFORM = PRESCRIBED_INPUT / NOT_PREDICTED
SELF_GROWN_WAVEFORM = OFF
WAVEFORM_COEFFICIENTS_FROM_GEOMETRY_EVIDENCE = ALLOWED
WAVEFORM_COEFFICIENTS_FROM_Pf = PROHIBITED

TWO_INDEPENDENT_AFFINE_SLOPE_SECTION_INTERFACE = PASS
FULL_NORMAL_BENDING_Nx_Ny_Mx_My = INCLUDED
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
MATERIAL_FUNCTIONS_CHANGED = FALSE
MATERIAL_PARAMETER_REFIT = FALSE

PANEL1_EVENT = CURRENT_MAP_SECTION_FOLD
PANEL1_EVENT_LOAD = 589.0817 kN
PANEL1_ERROR_VS_Pf = +20.173%
PANEL1_THICKNESS_STATE = CC -> TC
PANEL1_PRIMARY_DIAGNOSTIC = TC_POSTCRACK_INTERACTION_MISSING_BEFORE_CURRENT_GAMMA_ONSET

PANEL14_EVENT = LOWER_Y_REBAR_COMPRESSION_YIELD_ACTIVESET_TERMINAL
PANEL14_EVENT_LOAD = 770.5483 kN
PANEL14_ERROR_VS_Pf = +7.594%
PANEL14_THICKNESS_STATE = CC -> TC
PANEL14_CONCRETE_DIAGNOSTIC = BLOCKED_BY_REBAR_ACTIVESET

PANEL21_EVENT = CURRENT_MAP_SECTION_FOLD
PANEL21_EVENT_LOAD = 192.6906 kN
PANEL21_ERROR_VS_Pf = -47.683%
PANEL21_THICKNESS_STATE = TC -> CC
PANEL21_TT_AT_EQUILIBRATED_TERMINAL = NO
PANEL21_PRIMARY_DIAGNOSTIC = TRANSVERSE_TENSION_STIFFENING_TOO_WEAK / REINFORCEMENT_DEPENDENCE_MISSING

TC_R2_GAMMA_ACTIVE_AT_TERMINALS = NO_ALL_3
NC_CC_REOPEN_FROM_THIS_AUDIT = NO
TT_REOPEN_FROM_THIS_AUDIT = NO_FIRST_PRIORITY
PRIMARY_MATERIAL_REOPEN_1 = REINFORCEMENT_DEPENDENT_TENSION_STIFFENING
PRIMARY_MATERIAL_REOPEN_2 = POSTCRACK_TC_INTERACTION_BEFORE_GAMMA_ONSET
STEEL_REBAR_ACTIVESET_REPRESENTATION = OPEN_FOR_PANEL14
Z6_ACTIVESET_PROOF = DEPRIORITIZED_BY_USER
```

Detailed execution:

`semantic_v2/40_execution/20260822_1927__NZSCCM__PANEL1_14_21_TWO_SLOPE_FULL2D_MATERIAL_LIMIT_DIAGNOSTIC.md`

Reproduction script:

`semantic_v2/40_execution/rc/20260822_1927__NZSCCM__PANEL1_14_21_TWO_SLOPE_FULL2D_SECTION_DIAGNOSTIC.py`

Current result card:

`current/results/NZ_SCCM_RC_TWO_SLOPE_FULL2D_3PANEL_CURRENT_20260822.md`

Governing observed-waveform interpretation:

`semantic_v2/20_theory/20260822_1740__NZSCCM__RC_OBSERVED_WAVEFORM_AS_EXOGENOUS_IMPERFECTION_INPUT.md`

## Main structural-interface result

The previous one-slope section interface has now been replaced for this diagnostic by

\[
\boxed{\lambda_x(z)=a_x+b_xz,\qquad \lambda_y(z)=a_y+b_yz}
\]

without changing any NC material function. The frozen source waveform therefore transmits both normal bending resultants into the section material state. Concrete force/moment primitives and the section Jacobian are evaluated analytically from the same scalar material branches; no through-thickness numerical quadrature is introduced.

## Main material inference

The full equilibrium materially changes the earlier qualitative diagnosis.

1. **Panel21 TT is not governing.** The earlier elastic-recovery diagnostic suggested `CC -> TC -> TT`, but the equilibrated terminal is `TC -> CC`; TT disappears from the controlling state.
2. **Panel1 identifies a TC timing/coupling gap.** The Nguyen/Foster source TC transition is already exceeded at the measured failure state while current TC-R2 compression softening remains exactly inactive because its activation threshold is `lambda_t>10/17`.
3. **Panel21 identifies a tension-stiffening gap.** Its current-map fold is overwhelmingly transverse-tension tangent controlled and occurs far below experiment. The source audit records Foster `alpha2` as reinforcement-dependent, whereas the current project uses universal `alpha2=0.3`; this dependence is now the first tension-side mechanism to reopen without fitting to `Pf`.
4. **Panel14 is currently steel-controlled.** Its first terminal is a lower longitudinal rebar compression-yield active-set kink, so it is not a clean NC CC/TC discriminator under the current reduced perfect-plastic steel law.
5. **No current evidence demands reopening NC CC first.** Panels1/21 are tension-controlled; Panel14 is steel-active-set controlled.

## Next RC task

Do not globally retune NC. Perform two source-only mechanism audits, with no structural-load calibration:

1. recover the source reinforcement/bond dependence of Foster tension stiffening and determine a transferable material-input rule for `alpha2` or its equivalent;
2. re-examine TC-R2 compression weakening activation so that cracked-TC interaction is not absent throughout the entire experimentally relevant Panel1 state.

Treat Panel14 rebar active-set admissibility separately from the concrete-material audit.

```text
NEXT_RC_TASK = SOURCE_AUDIT_FOSTER_REINFORCEMENT_DEPENDENCE_PLUS_TC_POSTCRACK_ACTIVATION
```
