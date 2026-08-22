# RC CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 23:06 +08:00

```text
RC_PRIORITY = EXACT_NONLINEAR_POSTCRACK_TENSION_SHAPE_ACROSS_TC_TT
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

PANEL21_GEOMETRY_AUDIT = PASS
PANEL21_FULL_LENGTH = 2440 mm
PANEL21_WIDTH = 1220 mm
PANEL21_REFERENCE_HALFWAVES = 2
PANEL21_NOMINAL_HALFWAVE_LENGTH = 1220 mm
PANEL21_SOURCE_WAVEFORM_AXIS_MAPPING = PASS
NGUYEN_FIG5_6_PANEL21_BT_64P3 = SOURCE_CAPTION_TYPO
PANEL21_TABLE_AND_DIRECT_GEOMETRY_BT = 63.2

REINFORCEMENT_MAPPING_AUDIT = FAIL_PREVIOUS_DOUBLE_COUNT
NGUYEN_p_ROLE = NOMINAL_TOTAL_STEEL_RATIO
CORRECT_RHO_DIRECTION_LAYER = p/(2*n_layers)
PANEL21_CORRECT_RHO_X = 0.00375
PANEL21_CORRECT_RHO_Y = 0.00375
PANEL21_STEEL_LAYER_Z = 0

SOURCE_WAVE_1751_REBAR_MAPPING = SUPERSEDED
FULL2D_1927_NUMBERS = QUANTITATIVELY_SUPERSEDED_PENDING_RERUN
NC_M6_2130_PANEL1_PANEL14_NUMBERS = QUANTITATIVELY_SUPERSEDED_PENDING_RERUN
NC_M6_2130_PANEL21_180P159 = QUANTITATIVELY_SUPERSEDED
BOND_2205_TARGETS_AND_NUMBERS = QUANTITATIVELY_SUPERSEDED

NC_M6_2D_TC_CRACK_FRONT = RETAIN
EXACT_SECTION_PRIMITIVE = RETAIN
SAME_LAW_JACOBIAN = RETAIN
VC_GAMMA_10_OVER_17 = SOURCE_CORRECT
TC_ENVELOPE_ROLE = CRACKING_STATE_TRANSITION_NOT_TERMINAL_Pu
NC_CC_REOPEN = NO

PANEL21_CORRECTED_M6_F03_EVENT = CURRENT_MAP_SECTION_FOLD
PANEL21_CORRECTED_M6_F03_u = 0.3559087784
PANEL21_CORRECTED_M6_F03_q = 0.00134759
PANEL21_CORRECTED_M6_F03_LOAD = 173.209915 kN
PANEL21_CORRECTED_M6_F03_CONTROL = TRANSVERSE_POSTCRACK_TENSION_TANGENT

PANEL21_CORRECT_BENTZ_m = 180.0 mm
PANEL21_B99_ALPHA2_TARGET = 0.5486090032
PANEL21_B03_ALPHA2_TARGET = 0.6107497582

CONTINUOUS_TC_TT_ALPHA2_DIAGNOSTIC = EXECUTED
PANEL21_CONTINUOUS_TC_TT_B99_LOAD = 180.549929 kN
PANEL21_CONTINUOUS_TC_TT_B03_LOAD = 183.318982 kN
PANEL21_CONTINUOUS_TC_TT_CONTROL = TRANSVERSE_POSTCRACK_TENSION_TANGENT
PANEL21_STEEL_YIELD_CONTROL = NO
PANEL21_TT_ZONE_AT_TERMINAL = NO

ALPHA2_ONLY_CLOSURE = FAIL_AS_PRODUCTION_EXPLANATION
PANEL21_PRIMARY_REMAINING_GAP = NONLINEAR_POSTCRACK_TENSION_TANGENT_SHAPE
BH04_FIXED_FRONT_DIAGNOSTIC = HISTORICAL_SHAPE_EVIDENCE_ONLY
BH04_COUPLED_TC_EXACT_PRIMITIVE = REQUIRED_BEFORE_EXECUTION
BH04_NUMERICAL_THICKNESS_QUADRATURE = PROHIBITED

NEXT_RC_TASK = DERIVE_EXACT_NONLINEAR_POSTCRACK_TENSION_SHAPE_ACROSS_TC_TT
NEXT_CANDIDATE_FAMILY = BELARBI_HSU_0P4_OR_EQUIVALENT_SOURCE_BASED_NONLINEAR_SHAPE
NEXT_GATE = MOVING_NC_M6_CRACK_FRONT + TC_TT_CONTINUITY + SAME_LAW_TANGENT + ZERO_QUADRATURE
```

Latest Panel21 geometry/input/material-shape audit:

`semantic_v2/40_execution/20260822_2256__NZSCCM__PANEL21_GEOMETRY_REBAR_MAPPING_AND_TC_TT_TENSION_AUDIT_R02.md`

Reproduction driver:

`semantic_v2/40_execution/rc/20260822_2256__NZSCCM__PANEL21_CORRECTED_REBAR_AND_TC_TT_TENSION_EXACT.py`

Previous NC-M6 execution retained for method history but its three-panel numerical values used the source-wave reinforcement double-counting input and are therefore not current quantitative evidence:

`semantic_v2/40_execution/20260822_2130__NZSCCM__NC_M6_2D_TC_CRACK_FRONT_EXECUTION_R01.md`

Previous bond-dependent TC-only audit is likewise retained only as historical mechanism evidence; its Panel21 `m`, alpha targets and loads are superseded:

`semantic_v2/40_execution/20260822_2205__NZSCCM__NC_M6_REINFORCEMENT_DEPENDENT_POSTCRACK_TENSION_SOURCE_CLOSURE_R01.md`

## Current corrected interpretation

The Panel21 low prediction is not caused by a wrong wall length, wrong halfwave count or x/y axis swap. Nguyen's source geometry is `a=2440 mm`, `b=1220 mm`; Panels17–24 have two longitudinal halfwaves, so the nominal representative halfwave length is `1220 mm`. The current source-wave finite series is defined over the full physical length solely to retain the unequal two-lobe observed shape; its dominant `n=2` component is consistent with the two-halfwave source mode.

A genuine implementation error was found elsewhere: the source-wave front end assigned Nguyen's nominal total reinforcement ratio `p` independently to both orthogonal directions. The source-correct mapping is `rho_direction_layer=p/(2*n_layers)`. Panel21 therefore has `rho_x=rho_y=0.00375`, not `0.0075` in each direction.

The old doubled-steel implementation was first reproduced exactly, recovering the reported NC-M6 Panel21 fold near `180.159 kN`; this verifies that the correction is applied to the same explicit calculation path. With the source-correct steel mapping, the NC-M6/F03 fold is `173.210 kN`.

Correcting the directional reinforcement also changes the Bentz spacing parameter from the previous erroneous `90 mm` to `180 mm`. The corresponding source-anchored diagnostic alpha targets are about `0.54861` and `0.61075` for the Bentz and modified-Bentz variants.

The authorized next diagnostic then used the same bond-dependent Foster alpha2 on both TC and TT sides, retaining the M6 moving TC crack front and the exact finite section primitives. The resulting Panel21 connected folds are only `180.550 kN` and `183.319 kN`. Both singular modes remain overwhelmingly transverse-tension controlled, while the mid-plane reinforcement remains far from yield and the terminal section remains `TC -> CC`.

Therefore the earlier working interpretation `TC-only correction is suppressed because TT was locked` is no longer sufficient. Even after the TC/TT postcrack level is made continuous and reinforcement-dependent, Panel21 still folds prematurely. The remaining deficiency is localized more specifically to the **shape of the postcrack tensile tangent**: the present Foster branch carries a constant negative softening slope over the active interval.

## Next material layer

Keep the corrected steel mapping and all explicit structural equations frozen. Do not perform another global alpha2 sweep and do not modify the waveform, CC or VC gamma. Derive a source-based nonlinear postcrack tensile shape across TC and TT, beginning with the Belarbi–Hsu `0.4` family or an equivalent source-supported nonlinear law. It must be composed with the moving NC-M6 TC crack front and must retain a finite exact/analytic section primitive and same-law tangent. Numerical thickness quadrature remains prohibited.
