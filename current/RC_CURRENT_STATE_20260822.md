# RC CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 21:30 +08:00

```text
RC_PRIORITY = NC_M6_REINFORCEMENT_DEPENDENT_POSTCRACK_TENSION
EXPLICIT_STRUCTURAL_PATH = LOCKED_UNCHANGED
OBSERVED_NONSTANDARD_WAVEFORM = PRESCRIBED_INPUT / NOT_PREDICTED
SELF_GROWN_WAVEFORM = OFF
WAVEFORM_COEFFICIENTS_FROM_GEOMETRY_EVIDENCE = ALLOWED
WAVEFORM_COEFFICIENTS_FROM_Pf = PROHIBITED

TWO_INDEPENDENT_AFFINE_SLOPE_SECTION_INTERFACE = PASS
FULL_NORMAL_BENDING_Nx_Ny_Mx_My = INCLUDED
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
Pf_IN_ROOT_SELECTION = 0

NC_M6_2D_TC_CRACK_FRONT = EXECUTED_DIAGNOSTIC_PASS
EXACT_SECTION_PRIMITIVE = PASS
SAME_LAW_JACOBIAN = PASS
VC_GAMMA_10_OVER_17 = SOURCE_CORRECT
VC_GAMMA_ACTIVE_AT_M6_F03_TERMINALS = NO_ALL_3
TC_ENVELOPE_ROLE = CRACKING_STATE_TRANSITION_NOT_TERMINAL_Pu
CURRENT_FIXED_UNIAXIAL_TC_CRACK_FRONT = SUPERSEDED_FOR_M6_DIAGNOSTIC

PANEL1_M6_F03_EVENT = CURRENT_MAP_SECTION_FOLD
PANEL1_M6_F03_EVENT_LOAD = 462.6313 kN
PANEL1_M6_F03_ERROR_VS_Pf = -5.623%
PANEL1_M6_INTERPRETATION = 2D_TC_CRACK_FRONT_CORRECTION_MATERIAL_AND_NECESSARY

PANEL14_M6_F03_EVENT = LOWER_Y_REBAR_COMPRESSION_YIELD_ACTIVESET_TERMINAL
PANEL14_M6_F03_EVENT_LOAD = 770.7674 kN
PANEL14_M6_F03_ERROR_VS_Pf = +7.624%
PANEL14_STEEL_ACTIVESET = STILL_OPEN

PANEL21_M6_F03_EVENT = CURRENT_MAP_SECTION_FOLD
PANEL21_M6_F03_EVENT_LOAD = 180.1593 kN
PANEL21_M6_F03_ERROR_VS_Pf = -51.085%
PANEL21_M6_INTERPRETATION = REINFORCEMENT_DEPENDENT_POSTCRACK_TENSION_STILL_MISSING
PANEL21_TT_AT_EQUILIBRATED_TERMINAL = NO

FOSTER_ALPHA2_DEPENDENCE = SOURCE_REAL_BUT_NO_DETERMINISTIC_RHO_RULE_RECOVERED
ALPHA2_M6_F03_PANEL1 = 462.631 kN
ALPHA2_M6_F05_PANEL1 = 475.216 kN
ALPHA2_M6_F07_PANEL1 = 494.749 kN
ALPHA2_M6_PANEL14 = APPROX_770.76 kN_ALL
PANEL21_CONNECTED_FOLD_CONTINUATION = SMOOTH_TO_ALPHA2_APPROX_0.464
PANEL21_CONNECTED_FOLD_LOST_OR_TOPOLOGY_CHANGED_BY_ALPHA2_APPROX_0.466
ALPHA2_SELECTION_BY_Pf = PROHIBITED

BH04_FIXED_FRONT_DIAGNOSTIC = HISTORICAL_ONLY
BH04_COUPLED_TC_EXACT_PRIMITIVE = NOT_YET_DERIVED
BH04_NUMERICAL_THICKNESS_QUADRATURE = PROHIBITED

NC_CC_REOPEN = NO_FIRST_PRIORITY
NC_TT_REOPEN = NO_FIRST_PRIORITY
Z6_ACTIVESET_PROOF = DEPRIORITIZED_BY_USER

NEXT_RC_TASK = SOURCE_CLOSE_REINFORCEMENT_DEPENDENT_POSTCRACK_TENSION_WITHIN_NC_M6_EXACT_PRIMITIVE
```

Latest NC-M6 execution:

`semantic_v2/40_execution/20260822_2130__NZSCCM__NC_M6_2D_TC_CRACK_FRONT_EXECUTION_R01.md`

Reproduction script:

`semantic_v2/40_execution/rc/20260822_2130__NZSCCM__NC_M6_2D_TC_CRACK_FRONT_EXACT_SECTION.py`

Previous source/material audit:

`semantic_v2/40_execution/20260822_2004__NZSCCM__NC_TC_CRACK_TRIGGER_AND_TENSION_STIFFENING_SOURCE_AUDIT_R01.md`

Previous full two-slope execution:

`semantic_v2/40_execution/20260822_1927__NZSCCM__PANEL1_14_21_TWO_SLOPE_FULL2D_MATERIAL_LIMIT_DIAGNOSTIC.md`

## Current interpretation

The NC-M6 2D TC crack front has now been inserted without modifying the frozen explicit source-wave structural operator or the full two-slope section kinematics. The active Foster-type TC branch remains exactly integrable through thickness and its cross-coupled Jacobian is derived from the same current law.

The correction materially improves Panel1: the previous fixed-front fold at 589.08 kN moves to 462.63 kN, leaving a post-solution difference of -5.62% relative to the measured failure load. This occurs without structural-path change or Pf-based material identification.

Panel14 remains controlled by the lower longitudinal reinforcement compression-yield active-set boundary at about 770.77 kN, so it is still not a clean concrete-material discriminator.

Panel21 moves in the opposite direction: its tension-controlled fold decreases from 192.69 kN to 180.16 kN. The corrected early TC cracking therefore reinforces rather than removes the evidence that the current universal postcrack tension-stiffening representation is too weak for the Panel21 reinforcement state.

Foster alpha2 sensitivity on the coupled crack-front map cannot be converted into a calibrated rule. Panel1 rises from about 462.6 to 475.2 and 494.7 kN as alpha2 goes from 0.3 to 0.5 and 0.7, while the Panel21 connected stationary fold changes topology and is no longer continuously recovered beyond alpha2 approximately 0.466. No alternative root is selected by proximity to Pf.

The earlier BH04 fixed-anchor diagnostic is not promoted into NC-M6 because the coupled current crack front makes fcr vary with compression through thickness. The direct BH04 composition therefore leaves the present finite rational/affine primitive family; numerical thickness quadrature remains prohibited.

## Next material layer

Keep the explicit structural path locked. The next task is source closure of the reinforcement-dependent postcrack tensile branch inside NC-M6 while preserving finite exact section primitives and the same-law Jacobian. Do not reopen CC or TT first and do not identify coefficients from the Swartz failure loads.
