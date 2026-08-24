# NZ-SCCM — steel-shell local-buckling cap vs effective-width `Ny-My` gate R15

**Time:** 2026-08-24 12:28 +08:00  
**Status:** `EXECUTED / TC_NEXT_WITHDRAWN / STATIC_EFFECTIVE_WIDTH_EQUIVALENCE_PROVED / R07_R14_UNCHANGED / PROGRESSIVE_STEEL_SHELL_RESULTANT_GATE_OPEN`

## 0. Trigger and scope

This gate implements the corrected next task after the cross-family observation that the large/slender end of both steel-shell ordinary-concrete and steel-shell UHPC families retains positive-bias signals. It explicitly does **not** reopen UHPC `TC/CC/TT` material states.

Frozen identities remain:

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

The question is narrower:

> Can steel-face local buckling be represented more completely inside the finite `Ny-My` resultant envelope, without changing Marguerre–Airy and without returning to material-point constitutive mechanics?

The answer from this gate is **yes in principle, but not by merely replacing the current scalar steel-face compression cap with a static effective-width number**. That replacement is algebraically the same terminal object.

---

## 1. Source evidence recovered

### 1.1 Yun Lu — one-side-constrained steel plate

Source: 云露, *考虑薄膜效应的钢箱混凝土壁板局部屈曲行为研究*.

The source states that when `b/t` becomes large (the thesis identifies about `b/t > 80` as the range where membrane effects become important), local buckling is followed by stress redistribution and appreciable postbuckling reserve. The difference between buckling stress and ultimate average stress increases with plate slenderness.

For effective width, Yun defines the ultimate resultant equivalence through the widthwise average stress. In the reviewed Bridge et al. form, for `b/t = 37.3–130.7`, with

\[
\lambda=\sqrt{f_y/\sigma_{cr}},
\]

Yun Eq. (5-13) reports

\[
\boxed{
\rho_e=\frac{b_e}{b}
=\frac{1}{\lambda^{1.2}}
\left(1-\frac{0.25}{\lambda^{1.2}}\right).
}
\]

Yun also derives its own large-deflection effective-width expression in Eq. (5-23), and later multiplies it by an experimentally fitted coefficient `0.74` in Eq. (5-25). The `0.74` correction is **not** adopted here because this project does not import a fitted coefficient into a different structural family without a source-transfer gate.

### 1.2 Sun Lipeng — resultant/effective-area precedent

Source: 孙立鹏, *PBL加劲型薄壁钢管混凝土桥塔的计算理论与设计方法研究*.

Sun defines the normalized plate slenderness in Eq. (3.13) and gives a one-side-constrained flat-plate effective-width coefficient in Eq. (3.25):

\[
\rho(\lambda)=
\begin{cases}
1,&\lambda\le0.500,\\
0.66\lambda^{-0.6},&0.500<\lambda\le1.348,\\
0.64\lambda^{-0.5},&\lambda>1.348.
\end{cases}
\]

For a PBL-stiffened wall, Sun does **not** use the gross wall width blindly. The effective width and effective steel area are assembled by subpanels and stiffeners:

\[
\boxed{b_e=\sum_i\rho_i b_i},
\]

\[
\boxed{A_e=b_e t+\sum A_{se}}.
\]

These are Sun Eqs. (3.44)–(3.45). The same thesis later uses the local-buckling-reduced effective steel section in axial and compression-bending capacity calculations and explicitly gives an `N-M` interaction treatment in Chapter 7. This is direct source precedent that steel-plate local buckling can enter a **resultant-level capacity law**; no `TC/CC/TT` concrete state machine is required for that purpose.

---

## 2. Static effective-width equivalence theorem for the current `Ny-My` cut

Consider one external steel face of gross width `b`, thickness `t_s`, and through-thickness ordinate `z_f`. A classical static effective width gives, at the reference compressive stress `f_y`,

\[
N_{s,e}=b_e t_s f_y.
\]

Write

\[
\eta_e=\frac{b_e}{b}.
\]

Per unit gross wall width,

\[
\bar N_{s,e}=\eta_e t_s f_y.
\]

Because all widthwise strips of the same external face have the same ordinate `z_f` in the current y-normal through-thickness section,

\[
\bar M_{s,e}=z_f\bar N_{s,e}.
\]

Now compare this with the current scalar compressive face cap `f_{c,s}`:

\[
\bar N_{s,cap}=t_s f_{c,s},
\qquad
\bar M_{s,cap}=z_f t_s f_{c,s}.
\]

They are exactly identical when

\[
\boxed{
\eta_e=\frac{f_{c,s}}{f_y}.
}
\]

Therefore:

\[
\boxed{
\text{STATIC EFFECTIVE WIDTH ON ONE FACE}
\equiv
\text{STATIC COMPRESSIVE FACE FORCE CAP}
}
\]

for the present `Ny-My` terminal.

This is not an approximation. It is an exact resultant identity. Merely renaming `f_{c,s}` as `b_e/b` cannot add missing physics to the current `N-M` envelope.

---

## 3. What effective width is already implicit in R14

Using the frozen `f_y=355 MPa`, the existing R14 steel-face caps translate exactly to:

|Case|current `f_c,s` / MPa|equivalent `b_e/b=f_c,s/f_y`|equivalent compressive face loss|R14 error|
|---|---:|---:|---:|---:|
|T120|355.00|1.0000|0.0%|−3.051%|
|T360|301.871|0.85034|14.97%|+1.499%|
|BH005|355.00|1.0000|0.0%|+2.826%|
|BH010|355.00|1.0000|0.0%|+3.665%|
|BH020|355.00|1.0000|0.0%|+1.845%|
|BH032|295.42|0.83217|16.78%|+1.570%|
|BH050|250.07|0.70442|29.56%|+11.708%*|

`*` BH050 retains its lower-confidence comparator identity.

The key result is BH050. Its current local steel treatment is **already equivalent to discarding almost 30% of the compressive external-face effective width at the reference yield stress**, yet the current physical R14 prediction still remains high by `+11.7%` against the lower-confidence comparator.

Hence a new constant `b_e/b` number cannot be assumed to cure the remaining large-slenderness discrepancy. Doing so would simply be choosing a stronger scalar cap reduction, i.e. fitting the same model class.

---

## 4. Cross-family large/slender-end diagnostic

The accompanying R15 CSV records the frozen gross-width indicator, current root amplitude, equivalent cap ratio, and post-solution error for both families.

### 4.1 Steel-shell UHPC

For the BH sequence, gross structural width divided by `t_s=4 mm` grows as

\[
62.5,\ 125,\ 250,\ 400,\ 625.
\]

The R14 incremental physical amplitudes `b q_u` are

\[
0.0078,\ 0.0594,\ 0.4977,\ 2.2734,\ 12.6143\ \mathrm{mm}.
\]

After adding the frozen imperfection `q_0=0.0025`, the normalized total amplitudes `(b(q+q_0))/t_s` are

\[
0.158,\ 0.327,\ 0.749,\ 1.568,\ 4.716.
\]

R08 showed a strong monotone high-bias trend before the UHPC compression block was repaired. R14 removes most of that material-capacity bias; what remains is no longer monotone across BH005–BH032, but the extreme BH050 point again separates sharply at the largest gross width and deepest postbuckling amplitude.

### 4.2 Steel-shell ordinary concrete

R07 gives for Z6

\[
q_u=0.0138074,
\qquad
bq_u=165.689\ \mathrm{mm},
\]

and, with `q_0=0.004`,

\[
\frac{b(q_u+q_0)}{t_s}=53.42.
\]

Its postbuckling contribution to the axial load is already

\[
Cq(q+2q_0)=25.9165\ \mathrm{MN},
\]

while the final R07 result is `+13.93%` above Zhou. Z6 therefore sits far deeper in the postbuckling regime than the other Z baselines.

This is important: the common residual signal is at least as consistent with a **deep-postbuckling steel-shell effectiveness problem** as with a single fixed width-thickness correction.

---

## 5. Gross wall `b/t` is not automatically the local effective-width slenderness

A critical source guard is required here.

The current structural `b` in Marguerre–Airy is the **gross wall/panel width**. The `b_i` entering a local steel-plate effective-width law is the **unsupported subpanel width between actual restraints/stiffeners**.

They are not interchangeable.

For the Zhou source screen already archived in

`semantic_v2/40_execution/steel_shell/20260814_1405__NZSCCM__ZHOU_TABLE5_1__SCREEN_AND_COMPARISON__EXECUTION_CHECKPOINT.md`,

Table 5.1 fixes the local spacing at `200 mm` and `t_s=4 mm`, giving the local screen ratio `50`, even though the current Z global wall widths range from 2000 to 12000 mm.

Likewise, Sun's PBL theory explicitly requires each subpanel width `b_i`, local buckling mode, and stiffener effectiveness before forming `b_e` and `A_e`.

Therefore:

```text
USE_GROSS_MARGUERRE_AIRY_b_AS_LOCAL_EFFECTIVE_WIDTH_bi = PROHIBITED
```

The observed global large-width trend is real as a validation signal, but it does **not** by itself authorize plugging gross `b/t_s` into a local plate effective-width formula.

---

## 6. What a genuinely richer resultant law would have to do

A static cap has the form

\[
\sigma_{s,c}\le f_{c,s}=\text{constant}.
\]

A genuinely new local-buckling resultant law must instead allow the steel face's effective force to evolve with the current local plate buckling demand. At the resultant level a candidate structure is

\[
\boxed{
N_{f}^{eff}=\int_{face}
\left[\rho_e\,\sigma_f^{+}+\sigma_f^{-}\right]dy,
}
\]

\[
\boxed{
M_{f}^{eff}=\int_{face}z
\left[\rho_e\,\sigma_f^{+}+\sigma_f^{-}\right]dy,
}
\]

where compression is denoted by `+`, tension by `−`, and

\[
\rho_e=\rho_e(\lambda_{local},\text{current local postbuckling demand}).
\]

For a PBL/stiffened wall, Sun gives the finite assembly precedent

\[
A_e=b_e t+\sum A_{se},
\qquad
b_e=\sum_i\rho_i b_i.
\]

This still has:

```text
MATERIAL_POINTS = 0
CC_TC_TT = 0
THICKNESS_QUADRATURE = 0
FINITE_RESULTANT_UNKNOWN_SET = YES
```

but it is richer than a constant face cap because the compression-effective steel force can change as local plate buckling develops.

This R15 gate does **not** yet freeze a specific `rho_e(q)` formula. Doing that requires the local subpanel geometry and restraint identity to be source-closed first, otherwise the same local-buckling effect could be double-counted with the gross Marguerre–Airy mode.

---

## 7. Exact next source gate

Before changing any production `Pu`, recover for each steel-shell family:

1. the actual external-face unsupported subpanel widths `b_i`;
2. the longitudinal local plate lengths/aspect ratios entering `k_cr`;
3. the effective restraint identity of webs/PBL/studs/core contact;
4. whether the controlling local event is mother-plate overall buckling or between-stiffener subpanel buckling;
5. the corresponding source-supported `rho_i(lambda)` / effective-area law;
6. proof that this local plate mode is distinct from, rather than a duplicate of, the already frozen gross Marguerre–Airy structural mode.

Only then should the finite steel contribution to the same `Ny-My` envelope be regenerated and R07/R14 rerun.

---

## 8. R15 decision

```text
R15_EXECUTION = COMPLETE
TC_ACTIVATION_AUDIT_NEXT = WITHDRAWN

MARGUERRE_AIRY_STRUCTURAL_FRONT = RETAIN
Ny_My_TERMINAL_IDENTITY = RETAIN
POINTWISE_MATERIAL_OPERATOR = DO_NOT_REOPEN

STATIC_EFFECTIVE_WIDTH_ON_EXTERNAL_FACE = EXACTLY_EQUIVALENT_TO_STATIC_FACE_FORCE_CAP
STATIC_EFFECTIVE_WIDTH_AS_NEW_TERMINAL_PHYSICS = REJECT

R14_CURRENT_CAP_EQUIVALENT_EFFECTIVE_WIDTH:
  T360 = 0.85034
  BH032 = 0.83217
  BH050 = 0.70442

BH050_REMAINS_HIGH_DESPITE_29P56_PERCENT_STATIC_FACE_LOSS = YES
Z6_DEEP_POSTBUCKLING_SIGNAL = RETAIN
GROSS_b_OVER_t_AS_LOCAL_SUBPANEL_SLENDERNESS = NOT_AUTHORIZED

SUN_EFFECTIVE_AREA_AND_NM_PRECEDENT = SOURCE_SUPPORTED
YUN_EFFECTIVE_WIDTH_AND_LARGE_DEFLECTION_PRECEDENT = SOURCE SUPPORTED
YUN_0P74_FITTED_CORRECTION = NOT_IMPORTED

R07_STEEL_SHELL_NC_BASELINE = RETAIN_UNCHANGED
R14_STEEL_SHELL_UHPC_BASELINE = RETAIN_UNCHANGED

NEXT_TASK = STEEL_SHELL_LOCAL_SUBPANEL_GEOMETRY_AND_PROGRESSIVE_EFFECTIVE_AREA_NM_SOURCE_GATE
NEW_FITTED_FACTOR = NO
PRODUCTION_Pu_CHANGED_IN_R15 = NO
USER_ACCEPTANCE = PENDING
```

The negative result is deliberate and useful: **"effective width" is not automatically a new solution. A constant effective width is only another notation for the cap already present. The next non-redundant theory object is a source-closed progressive effective-area/resultant law tied to the actual local steel-plate geometry.**
