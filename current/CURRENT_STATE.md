# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-24 13:10 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / Ny_My_RESULTANT_TERMINAL / R14_ZHANG_PHYSICAL_PEAK_COMPLETE / R15_STATIC_CAP_EQUIVALENCE_CLOSED / R16_LOCAL_SUBPANEL_SOURCE_GATE_COMPLETE / Z_200MM_YUN_ELASTIC_ROUTE_INACTIVE / T360_BH032_BH050_PROGRESSIVE_CANDIDATE / BH_GEOMETRY_PROVENANCE_OPEN / R07_R14_UNCHANGED / TC_ROUTE_WITHDRAWN / USER_ACCEPTANCE_PENDING`

> R16 executes the R15 local-subpanel geometry/progressive-effective-area source gate. It changes no production `Pu`. Its main new result is a mechanism separation: the Z family cannot activate the same **pre-yield Yun elastic local-subpanel** mechanism as T360/BH032/BH050 because Zhou's source-closed local chamber width is only 200 mm at `t_s=4 mm`.

## 0. Frozen architecture

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
Nx_Mx_IN_STRUCTURAL_FIELD = YES
Nx_Mx_HARD_TERMINAL_ON_Y_CUT = NO
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
POINTWISE_MATERIAL_OPERATOR = DO_NOT_REOPEN
TC_CC_TT_ROUTE = OFF_MAINLINE
STRUCTURAL_BACKBONE_CHANGED = FALSE
```

Current chain:

\[
\boxed{
\text{full 2D Marguerre--Airy demand}
\rightarrow
(N_y,M_y)\text{ on the axial y-normal cut}
\rightarrow
\text{family-specific resultant capacity envelope}
\rightarrow P_u.
}
\]

Material/local-buckling source laws may be used only to construct the finite section/resultant envelope. They do not reintroduce a pointwise material-state solver.

---

## 1. Current production numerical baselines — unchanged

### RC — Swartz8 R05

```text
mean signed = +3.1777 percent
MAE = 9.2835 percent
RMSE = 9.7233 percent
```

### Steel-shell ordinary concrete — R07

```text
Z0 37.825706787 MN
Z1 24.714128548 MN
Z2 42.959011131 MN
Z3 46.495651955 MN
Z4 70.265718566 MN
Z5 14.118193577 MN
Z6 56.379421090 MN
```

Against Zhou: mean `+3.877%`, MAE `4.973%`; Z6 remains the visible high-end residual at `+13.93%`.

### Steel-shell UHPC — Zhang R14 physical peak terminal

```text
T120  12.252164525 MN   error -3.051 percent
T360  11.133264739 MN   error +1.499 percent
BH005  2.422372923 MN   error +2.826 percent
BH010  4.462040087 MN   error +3.665 percent
BH020  8.155351621 MN   error +1.845 percent
BH032 11.163055965 MN   error +1.570 percent
BH050 13.650448214 MN   error +11.708 percent [lower-confidence comparator]
```

Primary six: mean `+1.392%`, MAE `2.409%`, RMSE `2.544%`.

```text
R07_NC_PRODUCTION = RETAIN
R14_UHPC_PRODUCTION = RETAIN
PRODUCTION_Pu_CHANGED_IN_R16 = NO
```

---

## 2. R15 retained result — static cap is not the missing progressive law

R15 report:

`semantic_v2/40_execution/20260824_1228__NZSCCM__STEEL_SHELL_LOCAL_BUCKLING_CAP_VS_EFFECTIVE_WIDTH_NM_GATE_R15.md`

At the ultimate reference stress,

\[
\boxed{b_e/b=f_{c,s}/f_y}
\]

makes a static effective width exactly equivalent to a static face force cap in the present `Ny-My` cut.

Thus another constant `b_e/b` would remain the same capacity class. The only potentially non-redundant extension is the **pre-cap/progressive local-postbuckling evolution** of the steel resultant.

---

## 3. R16 report and reproducibility files

Report:

`semantic_v2/40_execution/20260824_1310__NZSCCM__STEEL_SHELL_LOCAL_SUBPANEL_SOURCE_CLOSURE_AND_PROGRESSIVE_NM_GATE_R16.md`

Reproducer:

`semantic_v2/40_execution/steel_shell/20260824_1310__NZSCCM__LOCAL_SUBPANEL_YUN_ELASTIC_GATE_R16.py`

Diagnostic CSV:

`semantic_v2/40_execution/steel_shell/20260824_1310__NZSCCM__LOCAL_SUBPANEL_YUN_ELASTIC_GATE_R16_RESULTS.csv`

---

## 4. R16 geometry provenance

### 4.1 Z0--Z6 — source closed

Zhou Table 5.3 gives

\[
\boxed{B_s=l_s=200\ \mathrm{mm}},\qquad
\boxed{t_s=4\ \mathrm{mm}},\qquad
\boxed{f_y=355\ \mathrm{MPa}}.
\]

The repeated chamber relation is `b=n_s l_s`, so the local chamber/subpanel width is not the gross Marguerre--Airy wall width.

```text
Z_LOCAL_Bs = 200 mm
Z_LOCAL_Bs_OVER_ts = 50
Z_LOCAL_GEOMETRY_PROVENANCE = PRIMARY_SOURCE_CLOSED
```

### 4.2 T120 / T360 — current project contract, provenance partial

```text
T120 local B_s = 120 mm
T360 local B_s = 360 mm
```

These are retained as the current project geometry contract. Native CAE audits independently close the gross 1600 x 50 x 3000 mm steel shell and the T120/T360 topology difference, but do not yet fully reconstruct the original feature-selection causality that independently proves the 120/360-mm local widths.

### 4.3 BH — working geometry, primary provenance open

Current working relation:

\[
\boxed{B_s=0.225B}
\]

produces `56.25, 112.5, 225, 360, 562.5 mm` for BH005--BH050. This remains a conditional working geometry until independent primary geometry provenance closes it.

```text
BH_LOCAL_WIDTH_PRIMARY_SOURCE_PROVENANCE = OPEN
OLD_32MM_WEB_HEIGHT = NOT_REINTRODUCED
```

---

## 5. R16 absolute Yun elastic pre-yield gate

For the current one-side-constrained elastic local-plate family,

\[
\boxed{k_{cr,\min}=32/3}.
\]

Hence

\[
\sigma_{cr,\min}
=
\frac{32}{3}
\frac{\pi^2E_s}{12(1-\nu_s^2)}
\left(\frac{t_s}{B_s}\right)^2.
\]

With `E_s=206000 MPa`, `nu_s=0.30`, `f_y=355 MPa`,

\[
\boxed{(B_s/t_s)_{transition}=74.79496253}.
\]

Therefore, if `B_s/t_s < 74.79496253`, **no local aspect ratio in this Yun elastic family can buckle before steel yield**.

|Case|`B_s/t_s`|`sigma_cr,min` MPa|Elastic local before yield?|
|---|---:|---:|---|
|Z0--Z6|50.000|794.389|NO|
|T120|30.000|2206.635|NO|
|T360|90.000|245.182|POSSIBLE|
|BH005|14.0625|10042.642|NO, conditional on working geometry|
|BH010|28.125|2510.660|NO, conditional|
|BH020|56.250|627.665|NO, conditional|
|BH032|90.000|245.182|POSSIBLE, conditional|
|BH050|140.625|100.426|POSSIBLE, conditional|

`POSSIBLE` is only a necessary-condition pass. Actual local longitudinal length/aspect ratio and restraint identity remain to be closed.

---

## 6. Major mechanism split after R16

### Z6

Because the primary-source local chamber is `200 x 4 mm`, even the minimum Yun elastic local-buckling stress is

\[
\boxed{794.389\ \mathrm{MPa}>355\ \mathrm{MPa}}.
\]

Therefore:

```text
Z6_YUN_ELASTIC_PROGRESSIVE_LOCAL_AREA_ROUTE = CLOSED_INACTIVE
Z6_COMMON_PREYIELD_YUN_MECHANISM_WITH_BH050 = REJECT
```

This does not reject local instability in general. Any relevant Z6 local mechanism would have to be an elastoplastic/yield-interaction local mechanism or another sectional/global resultant mechanism. No choice between those alternatives is made yet.

### T360 / BH032 / BH050

The current local widths pass the lower-bound eligibility gate for elastic local buckling before yield. These remain the only current candidates for a Yun amplitude-dependent progressive steel resultant.

T120 and BH005--BH020 are robustly outside that pre-yield elastic-local route under their current local-width contracts.

---

## 7. Candidate progressive resultant kernel — not yet production

The current Yun-type average-stress path is amplitude dependent:

\[
\widehat\sigma_Y(A)=
\left[
 k_{crx}\frac{A}{A+A_0}
 +k_p(1-\nu_s^2)\frac{2A_0A+A^2}{t_s^2}
\right]
\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)B_s^2}.
\]

The project formula-mapping register also contains

\[
\widehat\varepsilon_\ell(A)
=
\frac{\widehat\sigma_Y(A)}{E_s}
+C_\varepsilon(2A_0A+A^2),
\qquad
C_\varepsilon=\frac{3m^2\pi^2}{2a_\ell^2}.
\]

The architecture-compatible candidate is therefore an algebraic elimination:

\[
\widehat\varepsilon_\ell(A)=\varepsilon_f
\Rightarrow A=A(\varepsilon_f)
\Rightarrow \bar\sigma_f(\varepsilon_f)=\widehat\sigma_Y[A(\varepsilon_f)].
\]

Then the local steel contribution can in principle enter

\[
N_{s,f}=\sum_iB_{s,i}t_s\bar\sigma_{f,i},
\qquad
M_{s,f}=\sum_i z_{f,i}B_{s,i}t_s\bar\sigma_{f,i}.
\]

`A` would be a finite current algebraic internal coordinate, not a tracked material history and not a new gross structural Ritz mode.

Production use is still blocked because:

```text
T_BH_LOCAL_LONGITUDINAL_LENGTHS = NOT FULLY SOURCE_CLOSED
BH_Bs_PROVENANCE = OPEN
A(eps_f)_MONOTONE_UNIQUE_BRANCH = NOT YET PROVED
R14_4MM_FACE_EXACT_THICKNESS_MAPPING_TO_LOCAL_AVERAGE_LAW = NOT YET CLOSED
LOCAL_GLOBAL_DOUBLE_COUNTING_PROOF = NOT YET COMPLETE FOR T_BH
```

No centroidal thin-face replacement or ad-hoc width multiplier is authorized.

---

## 8. Current decisions

```text
R16_EXECUTION = COMPLETE

MARGUERRE_AIRY = RETAIN
Ny_My_RESULTANT_TERMINAL = RETAIN
TC_ACTIVATION_ROUTE = WITHDRAWN
POINTWISE_MATERIAL_STATE_CLASSIFICATION = OFF_MAINLINE

Z_LOCAL_GEOMETRY_SOURCE_GATE = PASS
Z_YUN_ELASTIC_PREYIELD_GATE = INACTIVE
Z6_YUN_PROGRESSIVE_ELASTIC_AREA = REJECT

T120_YUN_ELASTIC_PREYIELD_GATE = INACTIVE
T360_YUN_ELASTIC_PREYIELD_GATE = POSSIBLE
BH005_BH020_YUN_ELASTIC_PREYIELD_GATE = INACTIVE_CONDITIONAL
BH032_BH050_YUN_ELASTIC_PREYIELD_GATE = POSSIBLE_CONDITIONAL

YUN_AMPLITUDE_TO_NM_ALGEBRAIC_ELIMINATION = CANDIDATE_ONLY
YUN_PROGRESSIVE_NM_PRODUCTION = NOT_YET_AUTHORIZED
NEW_FITTED_FACTOR = NO
PRODUCTION_Pu_CHANGED = NO
```

---

## 9. Next task

Primary next task:

```text
NEXT_TASK = T360_BH032_BH050_LOCAL_GEOMETRY_PROVENANCE_AND_ALGEBRAIC_YUN_TO_NM_CLOSURE
```

Required deliverables:

1. source-close local longitudinal lengths/aspect ratios and restraint identities for T360/BH032/BH050;
2. close or reject the BH `B_s=0.225B` provenance;
3. prove the current branch `A(eps_f)` exists uniquely/monotonically over the relevant domain;
4. map the local average steel law into the exact 4-mm external-face `Ny-My` resultant without thickness quadrature;
5. prove no double counting with the gross Marguerre--Airy mode;
6. only then rerun T360/BH032/BH050.

Z6 is now on a separate mechanism track:

```text
Z6_NEXT = ELASTOPLASTIC_LOCAL_OR_OTHER_RESULTANT_MECHANISM_DIAGNOSIS
Z6_DO_NOT_USE_YUN_ELASTIC_PROGRESSIVE_AREA = TRUE
```

```text
USER_ACCEPTANCE = PENDING
```
