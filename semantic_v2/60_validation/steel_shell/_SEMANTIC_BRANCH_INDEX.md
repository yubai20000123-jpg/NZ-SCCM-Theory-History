# Steel-shell validation semantic branch

## Zero-quadrature shell validation — PASS

Primary validation:

- `20260813_1854__NZSCCM__STEEL_SHELL__ZERO_QUADRATURE_SSSS_NAVIER_ZHOU_ABAQUS__VALIDATION.md`

Reproducible execution:

- `semantic_v2/40_execution/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__ZERO_QUADRATURE_SSSS_EXACT_MOMENT_TEST.py`

Result table:

- `semantic_v2/50_results/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__SSSS_EXACT_VS_ABAQUS__RESULT_TABLE.csv`

```text
FINITE_THICKNESS_STEEL_SHELL_EXACT_MOMENTS = PASS
ZERO_NUMERICAL_SPATIAL_QUADRATURE = PASS
ZERO_NUMERICAL_THICKNESS_QUADRATURE = PASS
SSSS_NAVIER_ELASTIC_DEGENERATION = PASS
OFFICIAL_ABAQUS_BENCHMARK = PASS
ZHOU_FOUR_EDGE_SSSS_ARCHITECTURE_COMPATIBILITY = PASS
```

For the square SSSS benchmark:

```text
Ncr exact-moment = 90.38099268396850
Ncr classical    = 90.38099268396849
```

## Yun-Lu Chapter-2 exact compilation — PASS

See:

- `semantic_v2/20_theory/nc_steel_shell_panel/20260813_1919__NZSCCM__YUN_LU__CH2_GENERAL_D15_EXACT_COMPILATION_AND_DQ_COUPLING__THEORY_AUDIT.md`
- `semantic_v2/40_execution/steel_shell/20260813_1919__NZSCCM__YUN_LU__CH2_D15_EXACT_SYMBOLIC_AUDIT.py`

`Table 2-1`, `k_crx`, `k_p`, Eq.2-32 and Eq.2-37 are recovered exactly with finite general-D15 moments and zero spatial quadrature.

## 2026-08-13 20:05 postbuckling / event-ordering audit

Current audit:

- `20260813_2005__NZSCCM__SUN_A5__LOCAL_BUCKLING_YIELD_POSTBUCKLING_ORDERING__AUDIT.md`

Execution checkpoint:

- `semantic_v2/40_execution/steel_shell/20260813_2005__NZSCCM__SUN_A5__YUN_LOCAL_INSTANTIATION_AND_GLOBAL_PU_PREFLIGHT__EXECUTION_CHECKPOINT.md`

Current governing interpretation:

```text
YUN_LU_PREDICTS_POSTBUCKLING = YES
LOCAL_BUCKLING_IS_GLOBAL_STOP = NO
GLOBAL_D_q_PATH_MAY_CONTINUE_PAST_LOCAL_BUCKLING = YES
LOCAL_AMPLITUDE = FINITE INTERNAL GENERALIZED COORDINATE
PRESCRIBED_A(q)_WITHOUT_DERIVATION = REJECTED
POSTBUCKLING_KZ = CURRENT CONDENSED TANGENT
```

For an elastic-buckling-first local panel:

```text
S0 -> B_s -> Yun-Lu S1 elastic large-deflection postbuckling -> Y_s -> continued global ideal-EP response
```

Yun Lu does not by itself supply the detailed expanding plastic-zone/local-shape evolution after first yield; the global structure may nevertheless continue because local yield is not the global ultimate condition.

## Sun A5 real-source preflight

A5 local geometry and material give:

```text
b=256 mm
t_s=6 mm
s_h=520 mm
m=2
ell=260 mm
r=1.015625
E_s=208000 MPa
fy=423 MPa
nu_s=0.30
k_crx=10.670513051651874
k_p=42.654436695417374
sigma_cr_el=1101.9155543017378 MPa
sigma_cr_el/fy=2.6050013104059992
```

Thus A5 is yield-first under ideal elastic-perfectly-plastic steel. It is not admissible to force the elastic Yun-Lu S1 branch before yield.

Sun's experiment reports local buckling earlier than global ultimate (`Nlo=6210 kN`, `Nu=7065 kN`), which independently confirms that local buckling is not a global stop; it also shows that A5's real local mechanism includes inelasticity outside Yun Lu Chapter-2's purely elastic S1 range.

Current status:

```text
SUN_A5_LOCAL_D15_INSTANTIATION = PASS
SUN_A5_YIELD_FIRST_CLASSIFICATION = PASS
SUN_A5_FULL_Du_qu_Pu = PENDING
NO_FAKE_ROOT = YES
```

Pending items for a full A5 production root are source closure of the A5 R10 peak-strain input and a yield-first local-shell closure consistent with the adopted ideal-EP steel rule.
