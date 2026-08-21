# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-21 22:05 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1 = CURRENT ACTIVE LINE`

## 0. Supersession

本文件正式 supersede 2026-08-19 的 `R15_Z1_EXECUTION_AUDIT_CORRECTED = ACTIVE` 入口状态。

R15 / exact-special-function 相关文件仍保留为历史/旁支证据，但当前主线已经转为低阶显式：

\[
\boxed{\text{Marguerre–Airy 后屈曲}+\text{显式 }N-M\text{ 截面容量}+\text{有限代数根选择}}
\]

当前不再要求 Ritz 阶数、加载路径追踪、正式空间数值积分或材料点网格。

---

## 1. Canonical explicit theory

主理论：

`semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`

关键状态：

```text
GEOMETRIC_POSTBUCKLING_EXPLICIT = PASS
RC_SECTION_CAPACITY_EXPLICIT = PASS
Z_SECTION_CAPACITY_EXPLICIT = PASS
FINITE_CONTROL_LOCATION_CANDIDATES = PASS
ULTIMATE_ROOT_RULE = FINITE_ALGEBRAIC_MIN_POSITIVE_q
PATH_TRACKING = PROHIBITED_NOT_NEEDED
RITZ_ORDER = NONE
FORMAL_SPATIAL_QUADRATURE = 0
EXPERIMENT_IN_ROOT_SELECTION = 0
```

核心结构关系：

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\]

\[
m(s;q)=Jqs.
\]

---

## 2. Mandatory Swartz source correction

附录：

`semantic_v2/20_theory/20260821_2205__NZSCCM__SWARTZ_SOURCE_RATIO_AND_MULTIAXIAL_CAPACITY_ADDENDUM.md`

原 V1 中 Swartz 专属

\[
\rho_x=\rho_y=\rho_{table}/2
\]

的解释已 **SUPERSEDED**。

Swartz 原表配筋率应解释为：

\[
\boxed{\rho_x=\rho_y=\rho_{table}}
\]

即每方向、跨全部钢筋层合计配筋率；若有多层，只按层数分配，不再在两个方向间除2。

一般 RC 相体积守恒公式本身不变：两个方向钢筋均替代混凝土体积，只有加载方向钢筋直接承担加载方向轴力。

---

## 3. Swartz ultimate-load diagnostic policy

用户已明确：

```text
DO_NOT_MODIFY_STIFFNESS_TO_MATCH_EXPERIMENTAL_PCR = TRUE
DO_NOT_MODIFY_PCR_TO_MATCH_EXPERIMENTAL_PCR = TRUE
INITIAL_IMPERFECTION_PRESENT_FROM_LOAD_START = TRUE
EXPERIMENTAL_PCR_METHODS_NOT_UNIFORM = TRUE
```

因此实验 Pcr 只作历史/现象信息，不是当前极限承载力理论的校准目标。

误差诊断顺序改为：

1. 参数完全相同/高度接近的可信重复对；
2. 控制变量对；
3. 最后才看24块总体统计。

最新完整诊断：

`current/diagnostics/NZ_SCCM_SWARTZ24_SOURCE_CORRECTION_PAIR_MATRIX_TC_CAPACITY_AUDIT_20260821.md`

---

## 4. Current trusted Swartz design points

正确配筋率映射后的当前未加TC/CC capacity gate 显式结果：

|Case|Pu kN|Pf kN|status|
|---:|---:|---:|---|
|1|567.712|490.194|trusted pair 1/2; theory high|
|2|561.638|506.652|trusted pair 1/2; theory high|
|9|515.424|625.865|trusted pair 9/10; theory low|
|10|534.711|696.147|trusted pair 9/10; theory low|
|19|339.177|377.654|strong repeat pair 19/20; theory low|
|20|335.013|372.761|strong repeat pair 19/20; theory low|
|21|350.460|368.313|near-repeat 21/22; near experiment|
|22|351.679|355.858|near-repeat 21/22; near experiment|

重复性事实：

- 1/2 实验只差约3.36%，理论只差约1.07%，但理论成对整体偏高约13%。
- 9/10 同结构设计、主要材料批次差异；实验和理论均给 Case10>Case9，但理论两块均明显低估，成对约低20%。
- 19/20 实验变化约-1.30%，理论约-1.23%，是最强重复性证据之一，但理论整体约低10%。
- 21/22 亦表现为相近承载水平，整体偏差较小。

Case18/23 等控制配筋对说明 Swartz 单板极限荷载含有表内参数无法完全解释的离散，不允许用个别板反标钢筋模型。

---

## 5. Swartz CC/TC diagnostic status

Airy二维膜力是显式理论直接结果；厚度 `sigma_x(z),sigma_y(z)` 当前只采用最小 plane-stress recovery 做**诊断**，未获得正式二维 material-operator 身份。

当前根处：

- Case1/2：CC厚度约36–38%，受压面横向压约0.40 MPa，另一侧横向拉约2.4–2.6 MPa；
- Case9/10：CC厚度约49%，但受压面横向压仅约0.30 MPa，净 Nx 仍为横向拉；
- Nguyen/Foster CC 包络只支持约3%局部压强增强。

因此：

```text
STRONG_BIAXIAL_CONFINEMENT_AS_PRIMARY_CASE9_10_EXPLANATION = REJECTED
SMALL_CC_ENHANCEMENT = RETAINED
```

### TC gate

Nguyen/Foster TC 包络形式有来源，但 Swartz 表没有逐板实测 `ft`。

历史临时诊断：

\[
f_t=0.10f_c
\]

不是 source-closed production input。

保持 `D,Pcr,C,G,J,Ppb` 冻结，以该临时值联立 TC capacity gate：

- Case1: `Pu_TCdiag≈495.989 kN`, 对 Pf `+1.18%`；
- Case2: `Pu_TCdiag≈501.025 kN`, 对 Pf `-1.11%`。

原根 TC utilization：Case1/2 >1，Case9/10 <1，因此 TC gate 具有选择性地下修1/2而不先截断9/10的正确方向。

但 `Pu_TCdiag` 对 `ft/fc=0.08–0.12` 高度敏感，所以：

```text
TC_GATE_DIRECTION_AND_SELECTIVITY = SUPPORTED
TC_GATE_EXACT_SWARTZ_PU = DIAGNOSTIC_ONLY
BLOCKER = SWARTZ_SPECIMEN_FT_NOT_SOURCE_CLOSED
```

---

## 6. 0.85 fcyl capacity conversion diagnostic

Nguyen 对 Swartz 分析采用：

\[
f_c^{analysis}=0.85f_{cyl}.
\]

当前不允许据此修改稳定刚度/Pcr，只做最终 section-capacity 敏感性。

若容量层用完整 `fcyl`：

- Case1/2 大幅变得更高，明显恶化；
- Case9 `595.578 kN`，误差约-4.84%；
- Case10 `619.458 kN`，误差约-11.02%；
- Case19/20 分别 `376.766/370.522 kN`，几乎闭合；
- Case21/22 被抬高到约 +5%/+9%。

因此：

```text
UNIVERSAL_0P85_TO_NEW_CONSTANT_CORRECTION = REJECTED
```

若诊断地再叠加小CC增强：

- Case9 `Pu≈612.407 kN`, 误差约-2.15%；
- Case10 `Pu≈636.653 kN`, 误差约-8.55%。

Case10仍有明显剩余异常。

当前工作机制分解：

\[
\boxed{\text{base-strength conversion}+\text{TC weakening}+\text{small CC enhancement}}.
\]

不是统一全局强度系数。

---

## 7. Steel-shell UHPC current baseline

当前同步文件：

`current/results/NZ_SCCM_STEEL_SHELL_UHPC_T120_T360_BH005_BH050_CURRENT_SUMMARY_20260821.md`

### T120/T360

`20260821_1824__...T120_T360.md` 中无内部腹板结果 `11.7073 / 11.0538 MN` 已 superseded。

当前 web-corrected 工作值：

\[
\boxed{P_{u,T120}=12.34799984\rm\ MN},
\]

\[
\boxed{P_{u,T360}=11.29784021\rm\ MN}.
\]

二者当前通过第一版二维 CC/TC 预检查；正式 full-multiaxial closure 尚未完成。

### BH005–BH050

当前 BH 几何：`B/H=5,10,20,32,50`, `L=2B`, `H=50`, `ts=4`, `tc=42`, 9道无孔纵向 PBL/web，上5下4，当前直接拓扑 web height=32mm。

第一版 web-corrected N-M Pu：

- BH005 `2.382928 MN`；
- BH010 `4.417320 MN`；
- BH020 `8.139798 MN`；
- BH032 `11.110053 MN`；
- BH050 `13.594607 MN`。

状态：

```text
BH005_BH050 = FIRST-PASS WEB-CORRECTED
FULL_MULTIAXIAL_GATE = PENDING
BH050_MULTIAXIAL_PRIORITY = HIGH
```

---

## 8. Mandatory governance

```text
ZERO_FORMAL_SPATIAL_QUADRATURE = LOCKED
LOAD_PATH_TRACKING = NOT REQUIRED
RITZ_ORDER = NONE
EXPERIMENT_IN_ROOT_SELECTION = 0
STRUCTURAL_PU_BACKFIT_TO_MATERIAL = PROHIBITED
SWARTZ_REINFORCEMENT_SOURCE_CORRECTION = ACTIVE
D_PCR_PPB_MODIFICATION_FOR_SWARTZ_PCR_MATCH = PROHIBITED
TC_NUMERICAL_CORRECTION_REQUIRES_FT_SOURCE_CLOSURE
OLD_NO_WEB_T120_T360_RESULTS = SUPERSEDED
```

## 9. Recommended next task

在不动结构层的前提下，优先继续两条容量来源审计：

1. 查清 Swartz 普通混凝土 `ft` 是否可由原始批次材料试验或可靠来源闭合，从而把 TC gate 从 diagnostic 晋升为 source-grounded；
2. 继续审计 `fcyl -> in-situ panel strength -> current section capacity` 来源链，尤其 Case9/10 与 Case19/20 为什么对0.85转换表现不同；不得用 Pf 反标统一系数。
