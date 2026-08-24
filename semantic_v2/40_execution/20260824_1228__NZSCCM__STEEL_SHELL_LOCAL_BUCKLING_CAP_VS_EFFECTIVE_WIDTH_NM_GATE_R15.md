# NZ-SCCM — steel-shell local-buckling cap vs effective-width `Ny-My` gate R15

**Time:** 2026-08-24 12:28 +08:00  
**Status:** `EXECUTED / TC_NEXT_WITHDRAWN / STATIC_ULTIMATE_FACE_CAP_EQUIVALENCE_PROVED / PRECAP_EVOLUTION_NOT_EQUIVALENT / R07_R14_UNCHANGED / PROGRESSIVE_STEEL_SHELL_RESULTANT_GATE_OPEN`

## 0. Scope

This gate implements the corrected next task after the cross-family observation that the large/slender end of both steel-shell ordinary-concrete and steel-shell UHPC families retains positive-bias signals. It does **not** reopen UHPC `TC/CC/TT` material states.

Frozen identities:

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
Nx_Mx_IN_STRUCTURAL_FIELD = YES
Nx_Mx_HARD_TERMINAL_ON_Y_CUT = NO
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
POINTWISE_MATERIAL_STATE_MACHINE = OFF_MAINLINE
```

Question:

> Can steel-face local buckling be represented more completely inside the finite `Ny-My` resultant envelope, without changing Marguerre–Airy and without returning to material-point constitutive mechanics?

Result: **yes in principle, but not by treating a single static effective-width number as if it were automatically a new mechanism.** At the ultimate reference stress it belongs to the same external-face resultant-capacity class as a scalar face cap; its pre-cap/postbuckling evolution can be different and is precisely where a richer law must enter.

---

## 1. Source evidence

### Yun Lu

Source: 云露, *考虑薄膜效应的钢箱混凝土壁板局部屈曲行为研究*.

Yun identifies large-width-thickness one-side-constrained steel plates as a large-deflection/postbuckling problem with stress redistribution and postbuckling reserve. For the reviewed Bridge et al. data (`b/t=37.3–130.7`), Yun Eq. (5-13) reports, with

\[
\lambda=\sqrt{f_y/\sigma_{cr}},
\]

\[
\boxed{
\rho_e=\frac{b_e}{b}
=\lambda^{-1.2}\left(1-0.25\lambda^{-1.2}\right).
}
\]

Yun also derives a large-deflection effective-width equation and later applies a fitted coefficient `0.74`. The `0.74` coefficient is not imported into the current families.

### Sun Lipeng

Source: 孙立鹏, *PBL加劲型薄壁钢管混凝土桥塔的计算理论与设计方法研究*.

For one-side-constrained flat plates, Sun Eq. (3.25) gives

\[
\rho(\lambda)=
\begin{cases}
1,&\lambda\le0.500,\\
0.66\lambda^{-0.6},&0.500<\lambda\le1.348,\\
0.64\lambda^{-0.5},&\lambda>1.348.
\end{cases}
\]

For PBL-stiffened walls, the source assembles the effective width and effective steel area from actual subpanels/stiffeners:

\[
\boxed{b_e=\sum_i\rho_i b_i},
\qquad
\boxed{A_e=b_e t+\sum A_{se}}.
\]

These are Eqs. (3.44)–(3.45). Sun later carries the locally reduced effective steel section into axial and compression-bending calculations and explicitly gives an `N-M` interaction treatment. This is direct source precedent for a **resultant-level** local-buckling extension.

---

## 2. Static ultimate face-cap equivalence — exact, but limited in meaning

Consider one external steel face of gross width `b`, thickness `t_s`, ordinate `z_f`, and reference compressive stress `f_y`.

A static effective-width ultimate capacity is

\[
N_{s,e}^{max}=b_e t_s f_y,
\qquad
M_{s,e}^{max}=z_f b_e t_s f_y.
\]

Writing

\[
\eta_e=b_e/b,
\]

per unit gross wall width gives

\[
\bar N_{s,e}^{max}=\eta_e t_s f_y,
\qquad
\bar M_{s,e}^{max}=z_f\eta_e t_s f_y.
\]

A scalar compressive face cap `f_{c,s}` has maximum face resultant

\[
\bar N_{s,cap}^{max}=t_s f_{c,s},
\qquad
\bar M_{s,cap}^{max}=z_f t_s f_{c,s}.
\]

Hence the **ultimate face-resultant capacities** are exactly equal when

\[
\boxed{\eta_e=f_{c,s}/f_y}.
\]

Therefore a constant effective width used only as an ultimate face-cap number does not, by itself, add a new capacity coordinate.

Important limitation:

```text
STATIC ULTIMATE CAP EQUIVALENCE = EXACT
FULL PRE-CAP / POSTBUCKLING FORCE-DEFORMATION EVOLUTION = NOT IDENTICAL
```

The current R14 stress clip retains full gross width until its stress cap is reached. A progressive effective-width/effective-area law can instead reduce the **average compressive face resultant as local buckling develops**. That evolving law can change the shape of the strain-compatible `Ny-My` envelope and is the non-redundant object to investigate.

---

## 3. Static effective-width loss already implicit in the R14 ultimate face caps

With `f_y=355 MPa`, the frozen R14 caps have the following ultimate-cap equivalents:

|Case|`f_c,s` / MPa|equivalent ultimate `b_e/b=f_c,s/f_y`|equivalent ultimate face loss|R14 error|
|---|---:|---:|---:|---:|
|T120|355.00|1.0000|0.0%|−3.051%|
|T360|301.871|0.85034|14.97%|+1.499%|
|BH005|355.00|1.0000|0.0%|+2.826%|
|BH010|355.00|1.0000|0.0%|+3.665%|
|BH020|355.00|1.0000|0.0%|+1.845%|
|BH032|295.42|0.83217|16.78%|+1.570%|
|BH050|250.07|0.70442|29.56%|+11.708%*|

`*` BH050 comparator remains lower-confidence.

Thus BH050 already has an ultimate steel-face force cap equal to only `70.44%` of the full-yield gross-face capacity, yet the R14 result remains high. Merely selecting a still smaller **constant** `b_e/b` would remain the same ultimate-cap model class and would amount to fitting unless separately sourced.

---

## 4. Cross-family large/slender-end diagnostic

The accompanying CSV records gross width, root amplitude, current cap equivalent and post-solution error.

### UHPC BH sequence

Gross structural `b/t_s` grows as

\[
62.5,\ 125,\ 250,\ 400,\ 625.
\]

R14 incremental amplitudes `bq_u` are

\[
0.0078,\ 0.0594,\ 0.4977,\ 2.2734,\ 12.6143\ \mathrm{mm},
\]

and total normalized amplitudes `b(q+q0)/t_s` are

\[
0.158,\ 0.327,\ 0.749,\ 1.568,\ 4.716.
\]

R08 had a strong monotone high-bias trend before the UHPC compression terminal was repaired. R14 removes most of that bias; the remaining BH005–BH032 errors are not monotone, but the extreme BH050 point separates again at the largest gross width and deepest postbuckling amplitude.

### Ordinary-concrete Z6

R07 gives

\[
q_u=0.0138074,
\qquad bq_u=165.689\ \mathrm{mm},
\qquad \frac{b(q_u+q_0)}{t_s}=53.42.
\]

Its nonlinear postbuckling load term is

\[
Cq(q+2q_0)=25.9165\ \mathrm{MN},
\]

and its final R07 result is `+13.93%` relative to Zhou.

The cross-family residual signal is therefore compatible with a **deep-postbuckling steel-shell effectiveness** deficiency, not merely a missing constant width-thickness reduction.

---

## 5. Gross wall `b/t` is not the local effective-width slenderness

The Marguerre–Airy `b` is the gross wall/panel width. Local effective-width theory requires the unsupported subpanel width `b_i` between actual restraints/stiffeners.

They cannot be identified automatically.

The archived Zhou Table-5.1 source screen fixes the local spacing at `200 mm` with `t_s=4 mm`, giving local ratio `50`, despite current Z gross widths of 2000–12000 mm. Sun's PBL theory likewise requires each actual `b_i`, local mode and stiffener effectiveness before calculating `rho_i`, `b_e` and `A_e`.

```text
USE_GROSS_MARGUERRE_AIRY_b_AS_LOCAL_EFFECTIVE_WIDTH_bi = PROHIBITED
```

Thus the user's gross large-width trend is retained as an important validation observation, but it is not yet proof that the same local subpanel `b_i/t_s` variable controls both families.

---

## 6. Non-redundant resultant extension

A source-supported next law should modify the **current compression-effective steel force**, not merely replace one constant ultimate cap by another. At the current section level the generic finite form is

\[
\boxed{
N_f^{eff}=\int_{face}\left[\rho_e\sigma_f^+ + \sigma_f^-\right]dy,
}
\]

\[
\boxed{
M_f^{eff}=\int_{face}z\left[\rho_e\sigma_f^+ + \sigma_f^-\right]dy,
}
\]

with

\[
\rho_e=\rho_e(\lambda_{local},\text{current local postbuckling demand}).
\]

For a stiffened wall, Sun supplies the finite assembly precedent

\[
A_e=b_e t+\sum A_{se},
\qquad b_e=\sum_i\rho_i b_i.
\]

This remains compatible with

```text
MATERIAL_POINTS = 0
CC_TC_TT = 0
THICKNESS_QUADRATURE = 0
FINITE_RESULTANT_TERMINAL = YES
```

but can alter the `Ny-My` envelope because the effective compressive face force evolves rather than being represented by one fixed terminal cap.

R15 does not freeze a specific `rho_e(q)` law. The local subpanel geometry/restraint must be source-closed first and double counting with the gross Marguerre–Airy mode must be excluded.

---

## 7. Next source gate

Before changing any production `Pu`, recover for each steel-shell family:

1. actual external-face unsupported subpanel widths `b_i`;
2. local plate longitudinal lengths/aspect ratios and `k_cr`;
3. restraint identity/stiffness of webs/PBL/studs/core contact;
4. mother-plate overall vs between-stiffener subpanel buckling identity;
5. source-supported `rho_i(lambda)` / effective-area law;
6. proof that the local plate mechanism is distinct from the frozen gross Marguerre–Airy mode.

Only then regenerate the steel contribution of the **same** `Ny-My` envelope and rerun source-closed NC/UHPC cases.

---

## 8. Decision

```text
R15_EXECUTION = COMPLETE
TC_ACTIVATION_AUDIT_NEXT = WITHDRAWN

MARGUERRE_AIRY_STRUCTURAL_FRONT = RETAIN
Ny_My_TERMINAL_IDENTITY = RETAIN
POINTWISE_MATERIAL_OPERATOR = DO_NOT_REOPEN

STATIC_EFFECTIVE_WIDTH_ULTIMATE_FACE_CAP = SAME RESULTANT-CAP CLASS AS fcs
STATIC_EFFECTIVE_WIDTH_PRECAP_EVOLUTION = NOT IDENTICAL TO STRESS CLIP
STATIC_EFFECTIVE_WIDTH_AS_COMPLETE_NEW_LAW = REJECT

R14_ULTIMATE_CAP_EQUIVALENTS:
  T360 = 0.85034
  BH032 = 0.83217
  BH050 = 0.70442

BH050_REMAINS_HIGH_DESPITE_29P56_PERCENT_ULTIMATE_FACE_CAP_LOSS = YES
Z6_DEEP_POSTBUCKLING_SIGNAL = RETAIN
GROSS_b_OVER_t_AS_LOCAL_SUBPANEL_SLENDERNESS = NOT_AUTHORIZED

SUN_EFFECTIVE_AREA_AND_NM_PRECEDENT = SOURCE_SUPPORTED
YUN_EFFECTIVE_WIDTH_AND_LARGE_DEFLECTION_PRECEDENT = SOURCE_SUPPORTED
YUN_0P74_FITTED_CORRECTION = NOT_IMPORTED

R07_STEEL_SHELL_NC_BASELINE = RETAIN_UNCHANGED
R14_STEEL_SHELL_UHPC_BASELINE = RETAIN_UNCHANGED

NEXT_TASK = STEEL_SHELL_LOCAL_SUBPANEL_GEOMETRY_AND_PROGRESSIVE_EFFECTIVE_AREA_NM_SOURCE_GATE
NEW_FITTED_FACTOR = NO
PRODUCTION_Pu_CHANGED_IN_R15 = NO
USER_ACCEPTANCE = PENDING
```
