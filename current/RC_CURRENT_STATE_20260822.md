# RC CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 20:04 +08:00

```text
RC_PRIORITY = NC_M6_2D_TC_CRACK_FRONT_CURRENT_MAP
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

VC_GAMMA_10_OVER_17 = SOURCE_CORRECT
REPLACE_GAMMA_ONLY = NOT_JUSTIFIED
TC_ENVELOPE_ROLE = CRACKING_STATE_TRANSITION_NOT_TERMINAL_Pu
CURRENT_FIXED_UNIAXIAL_TC_CRACK_FRONT = INCOMPLETE

PANEL1_FIRST_SOURCE_TC_CRACK_TRANSITION = 341.912 kN
PANEL14_FIRST_SOURCE_TC_CRACK_TRANSITION = 476.375 kN
PANEL21_FIRST_SOURCE_TC_CRACK_TRANSITION = 128.249 kN

FOSTER_ALPHA2_DEPENDENCE = SOURCE_REAL_BUT_NO_DETERMINISTIC_RHO_RULE_RECOVERED
ALPHA2_0P3_TO_0P7_SWEEP = SENSITIVITY_ONLY
BH04_POSTCRACK_SHAPE = PROMISING_DIAGNOSTIC_NOT_PRODUCTION
BH04_PLUS_BARE_STEEL_PANEL1 = 529.948 kN
BH04_PLUS_BARE_STEEL_PANEL21 = 375.039 kN
BH04_PLUS_EMBEDDED_STEEL_PANEL1 = 528.582 kN
BH04_PLUS_EMBEDDED_STEEL_PANEL21 = 303.412 kN

NC_CC_REOPEN = NO_FIRST_PRIORITY
NC_TT_REOPEN = NO_FIRST_PRIORITY
PANEL14_STEEL_ACTIVESET = STILL_OPEN
Z6_ACTIVESET_PROOF = DEPRIORITIZED_BY_USER

NEXT_NC_CANDIDATE = NC_M6_2D_TC_CRACK_FRONT
NEXT_RC_TASK = BUILD_EXACT_COUPLED_TC_CURRENT_MAP_AND_RERUN_PANEL1_14_21
```

Detailed source/material audit:

`semantic_v2/40_execution/20260822_2004__NZSCCM__NC_TC_CRACK_TRIGGER_AND_TENSION_STIFFENING_SOURCE_AUDIT_R01.md`

Previous full two-slope execution:

`semantic_v2/40_execution/20260822_1927__NZSCCM__PANEL1_14_21_TWO_SLOPE_FULL2D_MATERIAL_LIMIT_DIAGNOSTIC.md`

Reproduction baseline:

`semantic_v2/40_execution/rc/20260822_1927__NZSCCM__PANEL1_14_21_TWO_SLOPE_FULL2D_SECTION_DIAGNOSTIC.py`

## Current corrected interpretation

The 19:27 diagnosis `TC compression degradation begins too late because gamma does not activate` was too coarse. Nguyen/Vecchio–Collins Eq. (3.43) itself implies the `10/17` tensile-strain threshold after the cap `gamma<=1`; that part of the current formula is source-correct.

The more fundamental omission is earlier in the material architecture. Nguyen's biaxial TC envelope defines the tensile peak at which an undamaged element changes to the cracked TC branch. Under simultaneous compression this cracking stress can be substantially below the uniaxial `ft`. The current scalar reduction instead keeps a fixed crack front `eps_cr=ft/E0` independent of simultaneous compression.

Direct source-wave/full-section calculations locate the first TC-envelope crossings at approximately 341.9 kN for Panel1, 476.4 kN for Panel14 and 128.25 kN for Panel21. These are not ultimate loads. Treating them as terminal capacities would grossly underpredict the tests. They must therefore be represented as explicit current-branch transition events followed by continued cracked-TC response.

Foster `alpha2` sensitivity confirms that reinforcement dependence matters: raising `alpha2` from 0.3 to 0.5/0.7 delays the premature Panel21 tensile fold from 192.7 kN to about 324.1/333.5 kN, but simultaneously increases the Panel1 event from 589.1 kN to about 607.9/637.3 kN. No source-closed unique `alpha2(rho)` law has been recovered, so a Swartz-based interpolation is not promoted.

A Belarbi–Hsu `0.4` postcrack power-shape diagnostic, attached to the present source anchors, gives about 529.95 kN for Panel1 and 375.04 kN for Panel21 with bare EPP steel. This is promising but cannot be promoted while the TC crack-trigger layer is still wrong. A paired embedded-steel diagnostic lowers Panel21 to about 303.4 kN, so the apparently excellent bare-steel match must not be selected merely by closeness to experiment.

## Next material layer

Build `NC-M6` as a genuinely coupled memoryless TC current map while preserving the explicit structural path. The source TC envelope supplies the current biaxial crack front. For undamaged compressive stress magnitude `p0`, use the source-equivalent tensile peak

\[
f_{cr}^{TC}(p_0)=
\begin{cases}
f_t(1-p_0/(2f_c)),&0\le p_0/f_c\le0.8,\\
3f_t(1-p_0/f_c),&0.8<p_0/f_c\le1.
\end{cases}
\]

and `eps_cr_TC=f_cr_TC/E0`. Retain the literal Vecchio–Collins gamma first, then compare finite postcrack tension families without using `Pf` to identify coefficients. The new TC stress field and its same-law Jacobian must still admit finite exact section primitives with zero formal quadrature.
