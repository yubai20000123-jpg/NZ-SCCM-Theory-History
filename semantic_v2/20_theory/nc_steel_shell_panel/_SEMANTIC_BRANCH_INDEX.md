# Concrete + steel-shell semantic branch

## Parent theory — LOCKED

Parent governance:

- `semantic_v2/10_governance/20260813_1834__NZSCCM__NC_PANEL__ENERGY_MINIMUM_HALFWAVE_R10_N48C1MM_D15_DIRECT_LIMIT__LOCKED_BASELINE.md`

Locked identities:

```text
ONE theoretical energy-minimum complete halfwave
GLOBAL coordinates = D,q
NGUYEN second-order kinematics; membrane terms included
R10 ordinary-concrete current target frozen
N48-C1/MM compiler
Cayley-Hamilton 2D lift
full directional current tangent
general-D15 exact multiple moments
formal spatial quadrature = 0
direct primary-branch limit: Rq=0 + L=0, first +->- maximum
same-branch Zhou/Navier current-tangent control check
```

## Continuous steel-shell replacement

Structural extension:

- `20260813_1834__NZSCCM__NC_STEEL_SHELL_PANEL__REBAR_REPLACEMENT_GENERAL_D15__THEORY_EXTENSION_CONTRACT.md`

The rebar module is replaced by continuous finite-thickness shell contributions; the concrete parent is unchanged.

## Zero-quadrature shell gate — PASS

Validation:

- `semantic_v2/60_validation/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__ZERO_QUADRATURE_SSSS_NAVIER_ZHOU_ABAQUS__VALIDATION.md`

Execution:

- `semantic_v2/40_execution/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__ZERO_QUADRATURE_SSSS_EXACT_MOMENT_TEST.py`

```text
FINITE_THICKNESS_SHELL_EXACT_MOMENTS = PASS
ZERO_SPATIAL_QUADRATURE = PASS
ZERO_THICKNESS_QUADRATURE = PASS
SSSS_NAVIER_ELASTIC_DEGENERATION = PASS
Ncr exact-moment = 90.38099268396850
Ncr classical    = 90.38099268396849
```

## Yun Lu Chapter 2 -> general-D15 — EXACT PASS

Primary audit:

- `20260813_1919__NZSCCM__YUN_LU__CH2_GENERAL_D15_EXACT_COMPILATION_AND_DQ_COUPLING__THEORY_AUDIT.md`

Reproducible symbolic audit:

- `semantic_v2/40_execution/steel_shell/20260813_1919__NZSCCM__YUN_LU__CH2_D15_EXACT_SYMBOLIC_AUDIT.py`

Exact gates:

```text
ONE_COMPLETE_HALFWAVE_REDUCTION = PASS
TABLE_2_1_FROM_D15 = PASS
KCRX_FROM_D15 = PASS
KP_FROM_D15 = PASS
EQ_2_32_FROM_D15 = PASS
EQ_2_37_FROM_TABLE_2_1 = PASS
MINIMUM_LOCAL_HALFWAVE_r=1 = PASS
FORMAL_SPATIAL_QUADRATURE = 0
```

With `r=ell/b`:

\[
k_{crx}(r)=\frac{4(3r^4+2r^2+3)}{3r^2},
\]

\[
k_p(r)=\frac{272r^{16}+2856r^{14}+11273r^{12}+23146r^{10}+31506r^8+23146r^6+11273r^4+2856r^2+272}{r^2(r^2+1)^2(r^2+4)^2(4r^2+1)^2}.
\]

At `r=1`, `k_crx=32/3` and `k_p=1066/25=42.64`.

Yun Lu Eq.2-36 contains a source-internal inconsistency in its final printed cross harmonic; production regeneration follows Table 2-1 + Eq.2-27 and is cross-checked by Eq.2-37.

## Steel rule for the Yun branch

Current user-approved closure:

```text
STEEL = ideal elastic-perfectly-plastic
Yun-Lu elastic large-deflection path = valid before first local yield
strain hardening = 0
```

Yun Lu Chapter 2 is explicitly a postbuckling theory. A local buckling event does not terminate the global solution.

Clean elastic-buckling-first ordering:

```text
S0 pre-buckling
-> B_s local buckling
-> S1 Yun-Lu elastic large-deflection postbuckling
-> Y_s first local yield
-> global path may continue with ideal-EP strength cap
```

Detailed expanding plastic-zone/local-shape evolution after first yield is not supplied by Yun Lu Chapter 2 and is not invented.

## Correct local-amplitude coupling — INTERNAL COORDINATE + EXACT CONDENSATION

**Correction to the earlier index wording:** production does **not** prescribe an empirical/design-side `A=A(q)` map.

Each active local Yun-Lu amplitude is a finite internal coordinate with exact local residual

\[
R_A(D,q,A)=0.
\]

When `R_A,A != 0`, implicit differentiation gives

\[
A_D=-R_{A,D}/R_{A,A},\qquad A_q=-R_{A,q}/R_{A,A}.
\]

The local variable is then exactly condensed from the global derivatives:

\[
\widetilde P_D=P_D+P_AA_D,\qquad
\widetilde P_q=P_q+P_AA_q,
\]

\[
\widetilde R_{q,D}=R_{q,D}+R_{q,A}A_D,\qquad
\widetilde R_{q,q}=R_{q,q}+R_{q,A}A_q.
\]

The parent global limit identity is retained:

\[
\widetilde L=\widetilde P_D\widetilde R_{q,q}-\widetilde P_q\widetilde R_{q,D}.
\]

For multiple local amplitudes, use the finite local Jacobian block inverse. This is exact algebraic condensation, not a spatial discretization or modal deletion.

## Postbuckling current tangent

After local-mode activation, same-branch stability uses the current condensed tangent:

\[
\boxed{K_{gg}^{cond}=K_{gg}-K_{gA}K_{AA}^{-1}K_{Ag}},\qquad g=(D,q).
\]

Thus `KZ` after local buckling includes local-mode relaxation; the pre-buckling shell tangent may not be frozen and reused.

## First real-source NC+PBL preflight — Sun A5

Execution checkpoint:

- `semantic_v2/40_execution/steel_shell/20260813_2005__NZSCCM__SUN_A5__YUN_LOCAL_INSTANTIATION_AND_GLOBAL_PU_PREFLIGHT__EXECUTION_CHECKPOINT.md`

Mechanism audit:

- `semantic_v2/60_validation/steel_shell/20260813_2005__NZSCCM__SUN_A5__LOCAL_BUCKLING_YIELD_POSTBUCKLING_ORDERING__AUDIT.md`

A5 local source geometry:

```text
b=256 mm; t_s=6 mm; s_h=520 mm; m=2
ell=260 mm; r=1.015625
E_s=208000 MPa; fy=423 MPa; nu_s=0.30
```

Exact Yun coefficients:

```text
k_crx = 10.670513051651874
k_p   = 42.654436695417374
sigma_cr_el = 1101.9155543017378 MPa
sigma_cr_el/fy = 2.6050013104059992
```

Therefore A5 is `YIELD-FIRST` under the adopted ideal-EP model. Its elastic Yun-Lu S1 branch must not be forced before yield.

```text
SUN_A5_LOCAL_D15 = PASS
SUN_A5_YIELD_FIRST_CLASSIFICATION = PASS
SUN_A5_FULL_Du_qu_Pu = NOT RELEASED
```

The full root is withheld because A5 still lacks a source-frozen R10 `eps0` input and a source-consistent yield-first local-buckling closure under ideal EP; no experimental load is used to fill either gap.

## Zhou Table 5.1 source screen — COMPLETE / EMPTY >=56 SET

Validation:

- `semantic_v2/60_validation/steel_shell/20260814_1405__NZSCCM__ZHOU_TABLE5_1__BS_TS_SCREEN_AND_FORMULA_COMPARISON__VALIDATION.md`

Execution checkpoint:

- `semantic_v2/40_execution/steel_shell/20260814_1405__NZSCCM__ZHOU_TABLE5_1__SCREEN_AND_COMPARISON__EXECUTION_CHECKPOINT.md`

Result table:

- `semantic_v2/50_results/steel_shell/20260814_1405__NZSCCM__ZHOU_TABLE5_1__SCREEN_AND_FORMULA_COMPARISON__RESULT_TABLE.csv`

Zhou Table 5.1 fixes `l_s=200 mm` and `t_s=4 mm` in all four parameter groups. Therefore every Table-5.1 point has

\[
b_s/t_s=l_s/t_s=50,
\]

and the requested `b_s/t_s >= ~56` source screen is empty.

```text
ZHOU_TABLE5_1_BS_TS_GE56_SCREEN = EMPTY
ZHOU_TABLE5_1_MAX_BS_TS = 50
NO_SOURCE_POINT_IN_TABLE5_1_CAN_SATISFY_REQUESTED_SCREEN = YES
NEW_YUN_RUN_WITH_TABLE5_1_BS_TS_GE56 = NOT_PERFORMED_NO_SOURCE_CASE
SYNTHETIC_SOURCE_GEOMETRY = NO
```

The missing Zhou formula comparison for the preceding reduced `a=b=6000 mm, h=130 mm, ts=4 mm, fy=355 MPa, fcu=40 MPa` reference was repaired using Zhou Eq.(3-2)/(3-3) on the **same reduced two-shell object**:

```text
Pyth_reduced_Zhou_Eq3_2 = 39.2928 MN
previous_NZ_branch_peak_diagnostic = 26.1085 MN
NZ_over_Zhou_reduced_strength = 0.6644601556
relative_difference = -33.55398444 percent
```

Identity boundary: `Pyth_reduced` is not the original full multi-cell Zhou section value because internal web steel remains removed by the current project reduction. The prior `26.1085 MN` value is still a diagnostic first-load-maximum neighbourhood, not a frozen production `Rq=0 + L=0` root.

Zhou Eq.(5-79) remains registered as the elastic four-edge `Dx-Dy-H` comparator. Original MCFSTW `Dy/Dxy/Dmu/H` terms must not be mixed into the reduced double-shell object.

## Current next gate

Two distinct next calculations remain:

1. **Clean Yun postbuckling benchmark:** Table 5.1 cannot supply it. Search another real-source panel whose source geometry directly satisfies `sigma_cr_el < fy` (the `b_s/t_s >= ~56` rule is only a screen), then execute `B_s -> S1 -> Y_s -> global L/KZ` using the unchanged analytic branch.
2. **Sun A5 production benchmark:** close the yield-first local branch plus the missing A5 R10 material input, then solve A5 without forcing an elastic Yun branch.

No reopening of the locked ordinary-concrete mother theory is authorized.
