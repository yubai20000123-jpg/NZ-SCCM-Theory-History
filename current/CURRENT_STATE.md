# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-24 12:28 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / Ny_My_RESULTANT_TERMINAL / R14_ZHANG_PHYSICAL_PEAK_COMPLETE / R15_STATIC_ULTIMATE_CAP_EQUIVALENCE_CLOSED / PRECAP_EVOLUTION_OPEN / TC_ROUTE_WITHDRAWN / STEEL_SHELL_PROGRESSIVE_EFFECTIVE_AREA_SOURCE_GATE_NEXT / USER_ACCEPTANCE_PENDING`

> This entry supersedes the 2026-08-24 11:51 R14 entry only in next-task governance. R07 ordinary-concrete results and R14 steel-shell UHPC results remain numerically unchanged. R15 introduces no fitted correction and changes no production `Pu`.

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

`TC/CC/TT` concrete-state classification is not part of the current `Pu` solver.

---

## 1. Current numerical baselines

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

Against Zhou: mean `+3.877%`, MAE `4.973%`. Z6 remains the visible high-end outlier at `+13.93%`.

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

R14 remains the current physical steel-shell UHPC terminal.

---

## 2. R15 — local-buckling cap vs effective-width/resultant gate

Report:

`semantic_v2/40_execution/20260824_1228__NZSCCM__STEEL_SHELL_LOCAL_BUCKLING_CAP_VS_EFFECTIVE_WIDTH_NM_GATE_R15.md`

Reproducer:

`semantic_v2/40_execution/steel_shell/20260824_1228__NZSCCM__STEEL_SHELL_STATIC_EFFECTIVE_WIDTH_EQUIVALENCE_R15.py`

Diagnostic CSV:

`semantic_v2/40_execution/steel_shell/20260824_1228__NZSCCM__STEEL_SHELL_STATIC_EFFECTIVE_WIDTH_EQUIVALENCE_R15_RESULTS.csv`

### 2.1 Exact boundary of the static-equivalence result

For one external steel face, at the ultimate reference stress `fy`, a static effective width gives

\[
N_{s,e}^{max}=b_e t_s f_y,
\qquad M_{s,e}^{max}=z_f b_e t_s f_y.
\]

A scalar compressive face cap gives

\[
N_{s,cap}^{max}=b t_s f_{c,s},
\qquad M_{s,cap}^{max}=z_f b t_s f_{c,s}.
\]

Thus the **ultimate face-resultant capacities** are identical when

\[
\boxed{b_e/b=f_{c,s}/f_y}.
\]

But the full evolution is not identical:

```text
STATIC ULTIMATE FACE-CAP EQUIVALENCE = EXACT
PRE-CAP / PROGRESSIVE POSTBUCKLING EVOLUTION = NOT IDENTICAL
```

The existing R14 stress clip retains the gross face until its cap is reached; a progressive effective-area law can reduce the average compressive face resultant as local buckling develops and can therefore change the shape of the strain-compatible `Ny-My` envelope.

### 2.2 R14 cap-equivalent ultimate effective-width fractions

With `fy=355 MPa`:

```text
T120   eta=1.00000   ultimate face loss= 0.00 percent
T360   eta=0.85034   ultimate face loss=14.97 percent
BH005  eta=1.00000   ultimate face loss= 0.00 percent
BH010  eta=1.00000   ultimate face loss= 0.00 percent
BH020  eta=1.00000   ultimate face loss= 0.00 percent
BH032  eta=0.83217   ultimate face loss=16.78 percent
BH050  eta=0.70442   ultimate face loss=29.56 percent
```

BH050 remains high despite an ultimate face force cap already equivalent to nearly 30% effective-width loss. A still smaller constant `be/b` would remain the same static-cap class and cannot be adopted from the comparator.

---

## 3. Source-supported direction

### Yun Lu

Yun supports large-deflection/postbuckling membrane redistribution and effective-width treatment for one-side-constrained steel plates. The source reports Bridge et al. Eq. (5-13) and derives a large-deflection effective-width equation. Yun's later fitted `0.74` correction is not imported.

### Sun Lipeng

Sun gives a one-side-constrained effective-width law and, for PBL-stiffened walls,

\[
\boxed{b_e=\sum_i\rho_i b_i},
\qquad
\boxed{A_e=b_e t+\sum A_{se}}.
\]

The thesis explicitly carries the local-buckling-reduced effective steel section into axial and compression-bending `N-M` capacity calculations. This supports a resultant-level extension without reopening concrete material states.

---

## 4. Geometry guard

The Marguerre–Airy `b` is the **gross wall/panel width**. Local effective-width theory requires the **unsupported subpanel width** `b_i` between actual restraints/stiffeners.

```text
GROSS_MARGUERRE_AIRY_b == LOCAL_EFFECTIVE_WIDTH_bi -> NOT ASSUMED
```

The archived Zhou Table-5.1 screen has local spacing `200 mm` and `t_s=4 mm`, i.e. local ratio `50`, despite gross Z widths of 2000–12000 mm. Therefore gross Z width cannot be inserted into a local effective-width equation.

The same source closure is required for web/PBL/stud/core restraint in the UHPC family.

---

## 5. Deep-postbuckling signal retained

```text
Z6:
  q_u = 0.0138074
  b*q_u = 165.689 mm
  b*(q_u+q0)/ts = 53.42
  postbuckling P term = 25.9165 MN
  error vs Zhou = +13.93 percent

BH050:
  q_u = 0.00504574
  b*q_u = 12.614 mm
  b*(q_u+q0)/ts = 4.716
  current ultimate eta_cap = 0.70442
  error = +11.708 percent [lower-confidence comparator]
```

This is a validation signal, not a fitted threshold. It makes a progressive postbuckling steel-shell effectiveness law a more relevant next object than another constant cap.

---

## 6. Withdrawn route

The former

```text
NEXT_TASK = TRANSVERSE_AIRY_STATE_TO_TC_ACTIVATION_AUDIT
```

is formally withdrawn. It is inconsistent with the current resultant-only route and is not the first-priority explanation of the cross-family steel-shell residuals.

---

## 7. Current next task

```text
NEXT_TASK = STEEL_SHELL_LOCAL_SUBPANEL_GEOMETRY_AND_PROGRESSIVE_EFFECTIVE_AREA_NM_SOURCE_GATE
```

Required before changing production `Pu`:

1. actual external-face subpanel widths `b_i`;
2. local plate aspect ratios and `k_cr`;
3. restraint identity/stiffness of webs, PBL, studs and core contact;
4. mother-plate overall vs between-stiffener subpanel buckling identity;
5. source-supported `rho_i(lambda)` / effective-area law;
6. proof of no double counting with gross Marguerre–Airy;
7. regeneration of only the steel contribution of the same `Ny-My` envelope.

```text
TC_ACTIVATION_AUDIT_NEXT = WITHDRAWN
MARGUERRE_AIRY = RETAIN
Ny_My = RETAIN
R07_NC = RETAIN
R14_UHPC = RETAIN
STATIC_EFFECTIVE_WIDTH_ULTIMATE_CAP = SAME CAPACITY CLASS AS fcs
PRECAP_PROGRESSIVE_EFFECTIVE_AREA = OPEN SOURCE GATE
NEW_FITTED_FACTOR = NO
PRODUCTION_Pu_CHANGED_IN_R15 = NO
USER_ACCEPTANCE = PENDING
```
