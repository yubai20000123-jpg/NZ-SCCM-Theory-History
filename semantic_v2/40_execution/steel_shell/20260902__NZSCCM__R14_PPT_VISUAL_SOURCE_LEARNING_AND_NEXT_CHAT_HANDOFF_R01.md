# NZ-SCCM R14 — PPT VISUAL SOURCE LEARNING / CURRENT STATE / NEXT-CHAT HANDOFF R01

**Date:** 2026-09-02  
**Repository:** `yubai20000123-jpg/NZ-SCCM-Theory-History`  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged.  

---

## 1. Purpose of this handoff

This file backs up the most recent work completed after the R14 theory/Excel synchronization. The immediate task has shifted from changing mechanics to preparing a technically faithful theory-introduction PPT.

The current priority is **not** to modify R14 mechanics. It is to build a visual communication layer that follows the R14 central technical ledger and uses geometrically faithful figures.

The key user correction is:

> The PPT must use the R14 technical ledger as the governing narrative: first give the technical route, then explain every theoretical step and formula with its reference basis and physical meaning. Excel and worked examples are only auxiliary tools for understanding how formulas are applied.

A second hard correction is:

> Figures must be highly consistent with the actual steel-shell–UHPC / PBL geometry and the theoretical object being explained. Do not use visually plausible but geometrically wrong AI-generated engineering figures.

---

## 2. Formal theory baseline remains R14

Formal mechanics baseline remains:

`semantic_v2/20_theory/20260902__NZSCCM__STEEL_SHELL_UHPC_CENTRAL_TECHNICAL_LEDGER_R14_MINIMAL_TERMINAL_CORRECTION.md`

R14 only corrects the universal terminal regression from R13:

- remove mandatory universal `eps_y^- = -eps_c0` as a fifth outer equation;
- restore the connected four-equilibrium branch `R4(x;q)=0`;
- monitor competing current material-domain terminal and admissible `J4` fold;
- define `Pu=P(q_u)` at the first admissible terminal on the `q=0`-connected branch.

The following R13 mechanics remain unchanged in R14:

```text
A/D full-composite initialization
positive-integer global mode selection
Pcr
Marguerre–Airy global demand
R04 steel face
R04/R06 automatic gate
R02 condensed local amplitude
R06 finite-harmonic local stress reconstruction / first-radial-yield search
UHPC scalar through-thickness operator and F0/F1 primitives
longitudinal web resultant
section Nx,Ny,Mx,My
```

Hard boundaries remain:

```text
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
COMPARATOR_IN_ROOT_SELECTION = 0
no FEM/test root selection
no FEM/test material calibration
no effective width/effective area
no artificial B/H cutoff
```

---

## 3. Current practical Excel baseline recovered and verified

Exact workbook identity:

`NZSCCM_R14_多页完整人工计算Excel_R01_20260902.xlsx`

Exact SHA-256:

`d7cae9208642f3744083ffb9c7891376b491c6cefdd14322a17d0130e8a20040`

The binary is a current chat artifact, not stored in the Git tree.

Workbook sheets:

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

Important interpretation:

- the Excel is a transparent finite-dimensional evaluator / calculation paper;
- it is not the theory itself;
- a Python R14 runner is not required for Pu calculation;
- no complete R14 Python runner is currently part of the synchronized repository baseline.

---

## 4. PPT narrative correction now locked

The PPT must no longer be organized primarily around workbook sheets or regression examples.

The governing narrative is the R14 ledger sequence:

```text
physical object / scope
→ independent inputs and coordinates
→ initial full-composite A/D
→ positive integer global mode and Pcr
→ Marguerre–Airy global demand and P(q)
→ section generalized strains / curvatures
→ R04/R06 automatic steel-face event gate
→ R04 yield-controlled face response OR R02/R06 local-postbuckling face response
→ UHPC through-thickness resultants
→ longitudinal web resultants
→ total section Nx,Ny,Mx,My
→ four-resultant closure R4=0
→ q=0-connected branch
→ material-domain event versus J4 fold
→ first admissible terminal
→ Pu=P(q_u)
```

Excel and BH examples should appear only after the associated formulas have been explained.

---

## 5. Visual-source audit: core doctrine

The current visual doctrine is:

```text
G0 current UCFT exact geometry
> G1 direct theoretical-source figures
> figures directly generated from R14 equations
> strict 2D reduced-mechanics diagrams
> G2/G3 external analogous mechanisms
```

### G0 — current exact UCFT / PBL geometry

Highest priority for explaining the physical object.

Use the current UCFT manuscript / project figures that accurately show:

- outer steel plate;
- inner steel plate;
- UHPC core;
- longitudinal PBL rib;
- PBL openings / UHPC dowel relation when shown in the source;
- correct loading / longitudinal direction.

Do not replace this with a generic steel–concrete sandwich or invented 3D rendering.

### G1 — direct theory/source figures

Use source figures from the papers that directly support a mechanics step, especially:

- PBL stiffened steel wall / local buckling figures from Zhang Ning and related PBL work;
- simply supported plate / large-deflection / membrane-effect and Kármán–Airy figures from Yun Lu;
- UHPC compression and failure figures from Zhou Jun / Wang Shunan;
- other directly relevant source figures only when their geometry and boundary conditions match the point being made.

### Equation-generated figures

Preferred for R14-specific content that does not have an exact external figure:

- `Pcr,m` versus integer `m`;
- `P(q)`;
- R02 `Pi(U)` and finite candidate roots;
- R04 plane-stress von-Mises proportional projection;
- R06 `(u,v)∈[-1,1]^2` constrained maximization candidate map;
- UHPC stress–strain law from the current R14 anchors;
- connected branch / terminal competition / fold mathematical illustration.

### Strict reduced diagrams

Allowed only when geometry is explicitly labeled as a reduced mechanical representation, not as the exact physical PBL geometry.

Example: a through-thickness section diagram may show upper steel face / UHPC core / lower steel face / mid-surface and `z_f`, but must not invent several physical ribs to represent the equivalent longitudinal web area `A_w`.

---

## 6. Naming / interpretation for internal R04/R02/R06 codes in external presentation

The PPT should not introduce the internal codes without a mechanics description.

### R04

Recommended external description:

`plane-stress von-Mises proportional yield projection`

or in Chinese:

`平面应力 von Mises 理想弹塑性比例投影 / yield-first steel-face branch`.

Important distinction: current R04 is not an incremental plasticity history algorithm; it is a current-state proportional projection of the plane-stress trial state.

### R02

Recommended external description:

`energy-stationary reduced local-postbuckling amplitude model`

Chinese:

`基于总势能驻值的低维局部屈后幅值模型`.

Visual sequence should show:

`physical local cell → amplitude U → Pi(U) → cubic candidates + U=0 → minimum-energy U*`.

### R06

Recommended external description:

`finite-harmonic local-postbuckling stress reconstruction + constrained von-Mises maximization + first-yield scaling`.

Chinese:

`有限谐波局部屈后应力场重构 + 有界域 Mises 全局极值 + 首次比例屈服搜索`.

Visual sequence should show:

`physical local steel-face cell → normalized (u,v) domain → interior/edge/corner candidate sets → Phi_max → radial lambda_y`.

This makes clear why the formal spatial grid is still zero.

---

## 7. Airy / terminal visual rules

### Airy

Do not use a decorative 3D surface as the main explanation.

The main explanation should begin from the membrane-resultant stress potential relations, e.g. the relevant Kármán–Airy representation, and then map directly into R14 quantities:

```text
F(x,y)
→ membrane-resultant field
→ Kx, G, C, Jx, Jy
→ P(q), Nx^A, Ny^A, Mx^A, My^A
```

External Airy/Föppl–von Kármán figures whose loading or boundary conditions do not match R14 may be used only as secondary visual-learning references, not as direct R14 geometry.

### terminal / J4 fold

Do not represent terminal using an invented structural-deformation picture.

Terminal is a branch event, so it must be shown as a mathematical path-selection graphic:

```text
q=0-connected equilibrium branch
→ current material-domain boundary candidate
overlaid with
→ J4 fold candidate
→ whichever admissible event is reached first controls Pu
```

A generic fold/limit-point curve may be used only if explicitly labeled as a mathematical prototype, not as a computed BH specimen response.

Formal fold condition remains:

`R4=0, J4 v=0, v^T v=1`.

---

## 8. Locked visual assets / learning outputs from the current chat

Two current working documents were produced as local chat artifacts:

1. `NZSCCM_R14_理论介绍图示来源学习清单_R01_20260902.md`
2. `NZSCCM_R14_PPT页面图示映射表_R01_20260902.md`

They contain the visual-source learning rules and the proposed page-by-page visual mapping.

Representative source-page screenshots / visual-audit assets were also created locally from the currently available papers, including pages from:

- Sun Lipeng PBL thin-wall concrete-filled steel tube dissertation;
- Zhang Ning PBL-stiffened rectangular CFST local-buckling paper;
- Yun Lu steel-box concrete plate local-buckling / membrane-effect work.

These image assets are not yet committed as a formal PPT asset package in GitHub.

---

## 9. Proposed PPT page architecture currently locked at the planning level

The next PPT revision should be approximately 32 core slides plus optional appendices, with the following logical blocks:

```text
A. problem / exact UCFT physical object
B. three-scale map: GLOBAL / LOCAL / SECTION
C. global simply-supported plate, A/D, m*, Pcr
D. Airy stress potential and global postbuckling demand P(q)
E. section generalized kinematics
F. steel-face gate → R04 or R02/R06
G. UHPC and web exact resultants
H. total Nx,Ny,Mx,My and R4 closure
I. connected equilibrium branch and terminal competition
J. Pu definition
K. Excel transparency demonstration
L. BH example only as formula application / audit
M. boundaries and current open issues
```

No slide should be justified primarily by aesthetics; every visual must support an explicit mechanics statement.

---

## 10. Current status of the already-generated PPT

Earlier PPT versions exist as local artifacts, but they are **not current visual baselines** because the user identified mismatched or weakly matched figures.

Therefore:

```text
PPT_FORMULA_NARRATIVE = needs detailed re-review but generally closer to technical-ledger order in R02
PPT_VISUAL_LAYER = NOT_ACCEPTED / requires rebuild
CURRENT_NEXT_TASK = prepare the locked visual asset package first, then rebuild PPT
```

Do not resume by polishing the previous generated visuals.

---

## 11. Recommended next-chat execution order

The next conversation should start from this file plus the R14 latest sync index and central technical ledger.

Recommended sequence:

1. Read R14 central technical ledger.
2. Read this current-state / PPT-visual handoff.
3. Read the visual-source learning checklist and PPT page mapping if available locally / re-create from this handoff if not.
4. Build a `VISUAL_ASSET_REGISTER` before rebuilding slides.
5. For each slide, assign exactly one of:
   - exact current-geometry figure;
   - direct-source figure;
   - equation-generated figure;
   - strict reduced-mechanics diagram;
   - clearly labeled analogous mechanism figure.
6. Reject any figure that changes the physical topology, loading direction, boundary conditions, PBL relation, or scale meaning.
7. Only after the visual asset register passes, regenerate the theory PPT.

---

## 12. Current open issues that must not be silently closed

- `DISCRETE_PBL_HANDLED = NO`: current R14 uses longitudinal web steel area `A_w` as the frozen equivalent treatment; no new discrete-PBL mechanics should be introduced during PPT work.
- No complete R14 Python runner is part of the synchronized baseline; this does not block Pu computation because the Excel is the practical evaluator.
- The exact R14 `.xlsx` binary is not in Git tree; its filename and SHA are locked above.
- The current PPT visual layer remains pending acceptance.

---

## 13. One-line continuation rule

**Do not modify R14 mechanics while rebuilding the PPT. First lock geometrically faithful visual assets that follow the technical-ledger sequence; Excel and BH cases are explanatory examples only.**
