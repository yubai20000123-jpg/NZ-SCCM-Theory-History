# NZ-SCCM R14 COMPLETE MULTISHEET EXCEL — CURRENT STATE / HANDOFF R01

**Date:** 2026-09-02  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged.

## 1. Current practical Excel baseline

Current practical workbook:

`20260902__NZSCCM__R14_COMPLETE_MULTISHEET_EXCEL_R01.xlsx`

Source artifact SHA-256:

`d7cae9208642f3744083ffb9c7891376b491c6cefdd14322a17d0130e8a20040`

It supersedes the earlier R14 R4/J4 helper **as the practical standalone workbook**. It does not supersede the R14 central technical ledger.

The workbook is intentionally multi-sheet and no longer depends on a separate one-page R13 workbook.

Sheets:

```text
00_说明
01_输入全局
02_UHPC材料
03_状态R4
04_R06上
05_R06下
06_R4推荐
07_q路径终点
08_BH回归
09_使用说明
10_Solver设置
```

## 2. Theory identity

The workbook implements the current R14 minimal terminal correction:

\[
\mathbf R_4(\mathbf x;q)=0,
\qquad
\mathbf x=(\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y)^T
\]

on the equilibrium branch connected to

\[
q=0,\qquad \mathbf x=0.
\]

The former mandatory universal condition

\[
\varepsilon_y^-=-\varepsilon_{c0}
\]

is removed as an outer fifth equation.

UHPC material-domain boundaries remain competing events, and

\[
J_4=\partial\mathbf R_4/\partial\mathbf x
\]

is monitored for the first admissible structural fold.

The following R13 constituent mechanics remain unchanged:

```text
initial A/D
positive-integer global mode
Marguerre–Airy P(q), Kx, G, C, Jx, Jy
R04
R02 minimum-energy U*
R06 finite-harmonic current operator
UHPC six-degree compression
Hiew five-anchor cubic-Hermite tension
UHPC F0/F1 exact thickness resultants
web ideal-EP exact crossing
total section N/M assembly
```

## 3. Default open-box verification

The workbook is prefilled with the BH050 current material-boundary terminal only as an opening calculation-chain check.

Expected default evaluation:

```text
P ≈ 13.5247819548 MN
R4_norm ≈ 2.359075E-8
upper_local_norm ≈ 1.575912E-17
lower_local_norm ≈ 4.287431E-12
material_domain = PASS
current_state_status = CURRENT_EQUILIBRIUM_PASS
root_objective ≈ 5.565236E-16
```

`08_BH回归` is audit-only. Runtime formulas do not read stored q/Pu values from that sheet.

## 4. Important numerical-use boundary

The workbook is a transparent calculation sheet, not a hidden all-roots software backend.

For R06:
- `lambda,u,v` are finite-dimensional local mathematical variables;
- the workbook exposes the current stationary-point equations and local Newton helper;
- formal `Phi_max` identity still requires systematic multi-start over the finite interior / edge / corner candidate families and comparison of converged candidates;
- a single Solver stationary point must not automatically be treated as the global maximum.

For the outer branch:
- `06_R4推荐` exposes the finite-difference 4x4 J4 and Newton correction;
- `det(J4)` is a locating diagnostic;
- formal fold refinement should satisfy `R4=0, J4*v=0, v^T*v=1`.

## 5. Current corrected BH terminal picture

Under the current R14 material/operator:

```text
BH005–BH070 : current UHPC material-domain boundary controls
BH085–BH100 : J4 fold controls
```

The old outputs

```text
BH085/BH100 = NO_ADMISSIBLE_COMPRESSION_CONTACT_ROOT_FOUND
```

and the artificial `B/H≈74.6` root-existence ceiling are withdrawn.

## 6. Next-chat entry

Use the R14 central technical ledger as the formal theory source and this complete multisheet workbook as the practical Excel calculation baseline.

Do not reopen, without new independent evidence:
- mandatory universal compression-contact terminal;
- artificial B/H cutoff;
- alternative R04/R02/R06 mechanics;
- alternative UHPC material law.

Do not use FEM/test/stored Pu to select roots or terminals.
