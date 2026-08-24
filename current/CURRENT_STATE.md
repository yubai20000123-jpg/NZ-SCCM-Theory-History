# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-24 12:28 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / Ny_My_RESULTANT_TERMINAL / R14_ZHANG_PHYSICAL_PEAK_COMPLETE / R15_STATIC_EFFECTIVE_WIDTH_EQUIVALENCE_CLOSED / TC_ROUTE_WITHDRAWN / STEEL_SHELL_PROGRESSIVE_EFFECTIVE_AREA_SOURCE_GATE_NEXT / USER_ACCEPTANCE_PENDING`

> This entry supersedes the 2026-08-24 11:51 R14 entry only in the **next-task governance**. R07 ordinary-concrete results and R14 steel-shell UHPC results remain numerically unchanged. R15 is a steel-shell local-buckling/resultant source gate; it does not introduce a fitted correction and does not alter any production `Pu`.

## 0. Governing architecture — frozen

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
Nx_Mx_IN_STRUCTURAL_FIELD = YES
Nx_Mx_HARD_TERMINAL_ON_Y_CUT = NO
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
RITZ_ORDER = NONE
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
\rightarrow
P_u.
}
\]

`TC/CC/TT` concrete-state classification is not part of the current `Pu` solver.

---

## 1. Current cross-family numerical baselines

### RC — Swartz8 R05

```text
mean signed = +3.1777 percent
MAE = 9.2835 percent
RMSE = 9.7233 percent
```

### Steel-shell ordinary concrete — Z0–Z6 R07

Against Zhou:

```text
mean signed = +3.877 percent
MAE = 4.973 percent
```

Current R07 `Pu` / MN:

```text
Z0 37.825706787
Z1 24.714128548
Z2 42.959011131
Z3 46.495651955
Z4 70.265718566
Z5 14.118193577
Z6 56.379421090
```

Z6 remains the visible high-end outlier at `+13.93%` vs Zhou.

### Steel-shell UHPC — Zhang R14 physical peak terminal

Current R14 `Pu` / MN:

```text
T120  12.252164525   error -3.051 percent
T360  11.133264739   error +1.499 percent
BH005  2.422372923   error +2.826 percent
BH010  4.462040087   error +3.665 percent
BH020  8.155351621   error +1.845 percent
BH032 11.163055965   error +1.570 percent
BH050 13.650448214   error +11.708 percent  [lower-confidence comparator]
```

Primary six:

```text
mean signed = +1.392 percent
MAE = 2.409 percent
RMSE = 2.544 percent
```

R14 remains the current physical steel-shell UHPC terminal. FHWA R11/R12 remains a design baseline, not the physical production terminal.

---

## 2. R15 — steel-shell local-buckling cap vs effective-width gate

Report:

`semantic_v2/40_execution/20260824_1228__NZSCCM__STEEL_SHELL_LOCAL_BUCKLING_CAP_VS_EFFECTIVE_WIDTH_NM_GATE_R15.md`

Reproducer:

`semantic_v2/40_execution/steel_shell/20260824_1228__NZSCCM__STEEL_SHELL_STATIC_EFFECTIVE_WIDTH_EQUIVALENCE_R15.py`

Diagnostic CSV:

`semantic_v2/40_execution/steel_shell/20260824_1228__NZSCCM__STEEL_SHELL_STATIC_EFFECTIVE_WIDTH_EQUIVALENCE_R15_RESULTS.csv`

### 2.1 Exact static-equivalence result

For one external steel face on the current y-normal through-thickness cut, a static effective width

\[
\eta_e=b_e/b
\]

at reference stress `fy` gives per unit gross width

\[
N_{s,e}=\eta_e t_s f_y,
\qquad
M_{s,e}=z_f\eta_e t_s f_y.
\]

The current scalar face compression cap gives

\[
N_{s,cap}=t_s f_{c,s},
\qquad
M_{s,cap}=z_f t_s f_{c,s}.
\]

Therefore they are exactly identical when

\[
\boxed{\eta_e=f_{c,s}/f_y}.
\]

Hence:

```text
STATIC_EFFECTIVE_WIDTH = SAME Ny-My FORCE-CAP CLASS AS STATIC fcs
STATIC_EFFECTIVE_WIDTH_BY_ITSELF = NOT NEW TERMINAL PHYSICS
```

### 2.2 Effective-width loss already implicit in R14

With `fy=355 MPa`:

```text
T120   fcs=355.00    eta=1.00000   loss= 0.00 percent
T360   fcs=301.87133 eta=0.85034   loss=14.97 percent
BH005  fcs=355.00    eta=1.00000   loss= 0.00 percent
BH010  fcs=355.00    eta=1.00000   loss= 0.00 percent
BH020  fcs=355.00    eta=1.00000   loss= 0.00 percent
BH032  fcs=295.42    eta=0.83217   loss=16.78 percent
BH050  fcs=250.07    eta=0.70442   loss=29.56 percent
```

BH050 therefore remains high despite a current steel-face cap already equivalent to nearly 30% static effective-width loss. Merely choosing another constant `be/b` would be a stronger scalar cap, not a new mechanism.

---

## 3. Source-supported direction after R15

### Yun Lu

The source supports large-deflection/postbuckling membrane redistribution and effective-width treatment for one-side-constrained steel plates. Yun reports Bridge et al. Eq. (5-13) and derives a large-deflection effective-width expression. Yun's later fitted `0.74` correction is **not imported** into the current families.

### Sun Lipeng

Sun gives a source-supported effective-width/effective-area framework for one-side-constrained and PBL-stiffened steel walls:

\[
\rho(\lambda)=
\begin{cases}
1,&\lambda\le0.500,\\
0.66\lambda^{-0.6},&0.500<\lambda\le1.348,\\
0.64\lambda^{-0.5},&\lambda>1.348,
\end{cases}
\]

\[
\boxed{b_e=\sum_i\rho_i b_i},
\qquad
\boxed{A_e=b_e t+\sum A_{se}}.
\]

Sun also explicitly carries the local-buckling-reduced effective steel section into axial/compression-bending `N-M` capacity calculations. This is the correct source family for a **resultant-level** extension; it does not require concrete material-state classification.

---

## 4. Critical geometry guard

The Marguerre–Airy structural `b` is the **gross wall/panel width**. A local effective-width law requires the **unsupported steel subpanel width** `b_i` between actual restraints/stiffeners.

```text
GROSS_MARGUERRE_AIRY_b == LOCAL_EFFECTIVE_WIDTH_bi  -> NOT ASSUMED
```

For the archived Zhou Table-5.1 screen, local spacing is `200 mm` with `t_s=4 mm`, giving local ratio `50`, despite much larger gross wall widths in the Z calculations. Therefore the Z6 gross width cannot be inserted directly into a local effective-width equation.

Likewise, PBL/web/stud/core restraint must be source-closed before generating `rho_i` for the current UHPC cases.

---

## 5. Deep-postbuckling diagnostic retained

The current residual outliers also coincide with deep postbuckling amplitudes:

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
  current eta_cap = 0.70442
  error = +11.708 percent [lower-confidence comparator]
```

This does not prove a new law, but it makes a **progressive postbuckling steel-shell effectiveness law** a more relevant next object than another static cap.

---

## 6. Withdrawn next task

The previous entry's

```text
NEXT_TASK = TRANSVERSE_AIRY_STATE_TO_TC_ACTIVATION_AUDIT
```

is formally withdrawn.

Reason: it would reopen a material-state route inconsistent with the current resultant-only architecture, and the new cross-family signal points first to the steel-shell local/postbuckling resultant representation.

---

## 7. Current next task

```text
NEXT_TASK = STEEL_SHELL_LOCAL_SUBPANEL_GEOMETRY_AND_PROGRESSIVE_EFFECTIVE_AREA_NM_SOURCE_GATE
```

Required before any new production rerun:

1. close actual external-face subpanel widths `b_i`;
2. close local plate aspect ratios and buckling coefficient `k_cr`;
3. close restraint identity/stiffness of webs, PBL, studs and core contact;
4. classify mother-plate overall buckling vs between-stiffener subpanel buckling;
5. select the source-supported `rho_i(lambda)` / effective-area law without comparator fitting;
6. prove no double counting with the gross Marguerre–Airy mode;
7. regenerate only the steel contribution of the same `Ny-My` envelope and rerun source-closed NC/UHPC cases.

```text
TC_ACTIVATION_AUDIT_NEXT = WITHDRAWN
MARGUERRE_AIRY = RETAIN
Ny_My = RETAIN
R07_NC = RETAIN
R14_UHPC = RETAIN
STATIC_EFFECTIVE_WIDTH_AS_NEW_LAW = REJECT
PROGRESSIVE_EFFECTIVE_AREA_RESULTANT_LAW = OPEN_SOURCE_GATE
NEW_FITTED_FACTOR = NO
PRODUCTION_Pu_CHANGED_IN_R15 = NO
USER_ACCEPTANCE = PENDING
```
