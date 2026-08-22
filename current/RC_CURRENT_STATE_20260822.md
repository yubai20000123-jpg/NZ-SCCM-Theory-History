# RC CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-23 01:08 +08:00

```text
RC_PRIORITY = PANEL21_GLOBAL_VS_LOCAL_LIMIT_REGRESSION
MATERIAL_SHAPE_ENRICHMENT = PAUSED_PENDING_STRUCTURAL_REGRESSION
EXPLICIT_ANALYTIC_PHILOSOPHY = RETAIN
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

NGUYEN_p_ROLE = NOMINAL_TOTAL_STEEL_RATIO
CORRECT_RHO_DIRECTION_LAYER = p/(2*n_layers)
PANEL21_CORRECT_RHO_X = 0.00375
PANEL21_CORRECT_RHO_Y = 0.00375
PANEL21_STEEL_LAYER_Z = 0
SOURCE_WAVE_1751_REBAR_MAPPING = SUPERSEDED_DOUBLE_COUNT

A_GLOBAL_IDEAL_M2_STATUS = HISTORICAL_BLIND_BASELINE_CONFIRMED
A_GLOBAL_IDEAL_M2_HALFWAVE = 1220 mm
A_GLOBAL_IDEAL_M2_RHO_DIRECTION = 0.00375
A_GLOBAL_IDEAL_M2_LIMIT = Rq_EQ_0_AND_L_EQ_0
A_GLOBAL_IDEAL_M2_Pu = 368.189337 kN
A_GLOBAL_IDEAL_M2_ERROR_VS_Pf_POSTCHECK = -0.0335 percent
A2_INDEPENDENT_GLOBAL_CASE21_Pu = 365.607776 kN

B_LOCAL_IDEAL_M2_STATUS = EXECUTED_CURRENT_NC_M6_F03
B_LOCAL_IDEAL_M2_CRITERION = SECTION_EQUILIBRIUM_PLUS_detJsec_EQ_0
B_LOCAL_IDEAL_M2_u = 0.25 / 0.75_SYMMETRIC
B_LOCAL_IDEAL_M2_q = 0.001531925676
B_LOCAL_IDEAL_M2_P = 160.778280 kN
B_LOCAL_IDEAL_M2_ERROR_VS_Pf_POSTCHECK = -56.3473 percent

D_LOCAL_SOURCE_WAVE_STATUS = REPRODUCED
D_LOCAL_SOURCE_WAVE_CRITERION = SECTION_EQUILIBRIUM_PLUS_detJsec_EQ_0
D_LOCAL_SOURCE_WAVE_u = 0.3559087784
D_LOCAL_SOURCE_WAVE_q = 0.001347589965
D_LOCAL_SOURCE_WAVE_P = 173.209915 kN
D_LOCAL_SOURCE_WAVE_ERROR_VS_Pf_POSTCHECK = -52.9721 percent

B_TO_D_SOURCE_WAVE_EFFECT = +12.431635 kN / +7.732 percent
A_TO_B_COLLAPSE = -207.411057 kN / -56.333 percent
A_TO_D_COLLAPSE = -194.979422 kN / -52.956 percent

WAVELENGTH_ERROR_AS_PANEL21_CAUSE = REJECTED
SOURCE_WAVEFORM_DETAIL_AS_PRIMARY_COLLAPSE_CAUSE = REJECTED
LOCAL_SECTION_FOLD_ARCHITECTURE = PRIMARY_STRUCTURAL_REGRESSION_SUSPECT
A_MINUS_B_100_PERCENT_ATTRIBUTABLE_TO_CRITERION = NOT_YET_PROVEN
A_VS_B_MATERIAL_REPRESENTATION_CONFOUND = PRESENT

C_GLOBAL_SOURCE_WAVE_STATUS = NOT_YET_OPERATOR_CLOSED
C_NUMERICAL_VALUE = NOT_INVENTED
C_REQUIREMENT = GENERALIZE_OLD_GLOBAL_Rq_L_OPERATOR_TO_FINITE_Phi_WITH_OLD_MATERIAL_UNCHANGED

NC_M6_2D_TC_CRACK_FRONT = RETAIN_AS_MATERIAL_DIAGNOSTIC
EXACT_SECTION_PRIMITIVE = RETAIN
SAME_LAW_JACOBIAN = RETAIN
VC_GAMMA_10_OVER_17 = SOURCE_CORRECT
NC_CC_REOPEN = NO
BH04_OR_OTHER_POSTCRACK_TUNING = PAUSED

NEXT_RC_TASK = DERIVE_AND_EXECUTE_CELL_C_GLOBAL_FINITE_WAVE_Rq_L
NEXT_GATE_1 = RECOVER_GLOBAL_WORK_CONJUGATE_IDENTITY_WITH_FINITE_Phi
NEXT_GATE_2 = ZERO_SPATIAL_QUADRATURE
NEXT_GATE_3 = OLD_GLOBAL_MATERIAL_UNCHANGED
NEXT_GATE_4 = NO_Pf_IN_OPERATOR_OR_ROOT_SELECTION
NEXT_DECISION = LOCAL_detJsec_MAY_ONLY_BE_SECONDARY_GATE_UNLESS_EQUIVALENCE_TO_GLOBAL_LIMIT_IS_PROVEN
```

## Latest regression audit

`semantic_v2/40_execution/20260823_0058__NZSCCM__PANEL21_GLOBAL_VS_LOCAL_LIMIT_REGRESSION_AUDIT_R01.md`

Controlled B/D reproduction driver:

`semantic_v2/40_execution/rc/20260823_0058__NZSCCM__PANEL21_ABCD_REGRESSION_BD_DRIVER.py`

## Current interpretation

Panel21 already had a fresh blind global prediction of `368.189337 kN` using the same `1220 mm` ideal two-halfwave scale and the correct `0.00375` directional steel ratio, with experiment read only afterward. An independent fresh Case21 run gave `365.607776 kN`. Therefore the later approximately 50% low result cannot be blamed on halfwave selection.

The controlled B/D calculation now holds current NC-M6/F03 material, corrected steel mapping, full two-slope section kinematics and the local `det Jsec=0` criterion fixed while changing only the longitudinal waveform. Returning from the prescribed multi-harmonic source waveform to the ideal pure `m=2` waveform does not recover capacity; it lowers the local fold from `173.209915 kN` to `160.778280 kN`. The source-wave detail therefore is not the mechanism that produced the historical-to-current collapse.

The main unresolved change is the replacement of the old plate-level global limit definition `Rq=0, L=0` by a local section-equilibrium singularity `det Jsec=0`, together with a material-representation change. Because A and B do not yet use the same material map, the full `207.4 kN` A-to-B loss cannot be assigned solely to the criterion. Nevertheless the local-fold architecture is now the primary structural regression suspect and material tuning is paused.

Cell C is intentionally not assigned a value. It requires the old global work-conjugate `Rq,L` operator to be generalized to the prescribed finite `Phi(y)` without replacing it by the later local section system. The next task is to derive that generalized finite-wave global operator with the old global material law unchanged and zero formal spatial quadrature.