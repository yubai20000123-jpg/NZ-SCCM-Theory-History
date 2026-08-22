# NZ-SCCM — NC/UHPC 七门禁显式材料重组 V1

**Date:** 2026-08-22 11:51 +08:00  
**Status:** `MATERIAL_REORGANIZATION_7GATE = EXECUTED_PARTIAL / STRUCTURAL_BACKBONE_UNCHANGED / Pu_RERUN_NOT_AUTHORIZED`

## 0. 本轮治理边界

本轮只重组普通混凝土 NC 与 UHPC 的二维材料来源/容量判据，不修改当前 Marguerre–Airy 显式结构骨架，不重算 Case21、BH050 或任何试件 Pu。

```text
STRUCTURAL_BACKBONE_CHANGED = FALSE
NEW_PU_CALCULATION = FALSE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
```

当前主线仍为：

\[
\boxed{
\text{1D explicit structural/capacity root}
\to
\text{Airy 2D membrane demand}
\to
\text{finite 2D material-capacity judgment}
}
\]

完整增量型材料模型可以作为 source oracle，但不得作为第二套结构/材料点求解器进入生产主线。

## 1. 七门禁

\[
\begin{array}{ll}
G_1:&\text{单轴压缩退化正确且参数身份清楚}\\
G_2:&\text{单轴拉伸退化正确}\\
G_3:&CC/TC/CT/TT\text{ 均有来源支持}\\
G_4:&\text{plane-stress / Poisson 架构自洽}\\
G_5:&\text{采用关系及其同源导数/切线闭合}\\
G_6:&\text{有限直接代数计算；无材料点、历史场、空间求积}\\
G_7:&\text{材料参数不由结构 Pu 反标}
\end{array}
\]

其中 `G6` 为硬门槛。

---

# Part A — Ordinary concrete (NC)

## 2. Nguyen/Foster–Kupfer source envelope

Nguyen Chapter 3 明确说明其预屈曲普通混凝土二维强度包络是 Kupfer et al. (1969) 的修改形式，并采用 Foster & Gilbert (1990)/Foster (1992) 版本。完整 Nguyen 状态机仍包含 equivalent-uniaxial secant/tangent iteration、cracking/crushing/history，因此继续只作为 oracle；本轮只提取其显式峰值包络作为有限 capacity gate。

### 2.1 CC — Nguyen Eq. (3.17)

源式：

\[
\sigma_{2p}
=
\left[\frac{1+3.65\alpha}{(1+\alpha)^2}\right]f'_c,
\qquad
\alpha=\frac{\sigma_1}{\sigma_2}.
\]

转为压应力正幅值并排序

\[
0\le p_1\le p_2,\qquad a=\frac{p_1}{p_2}\in[0,1],
\]

得到

\[
\boxed{
K_{CC}^{NC}(a)=\frac{1+3.65a}{(1+a)^2}
}
\]

和容量边界

\[
\boxed{
p_{2,\max}=f_c K_{CC}^{NC}(a),\qquad
p_{1,\max}=a p_{2,\max}.}
\]

轴退化：

\[
K(0)=1.
\]

等双压：

\[
K(1)=1.1625.
\]

最大增强位于

\[
a_*=\frac{1.65}{3.65}=0.4520547945,
\qquad
K(a_*)=1.2568396226.
\]

同源导数：

\[
\boxed{
K'(a)=\frac{1.65-3.65a}{(1+a)^3}.}
\]

对任意当前 CC demand \((p_1^d,p_2^d)\)，固定应力射线比例 \(a=p_1^d/p_2^d\)，有限直接 re-cut factor 为

\[
\boxed{
\lambda_{CC}^{NC}
=
\frac{f_cK(a)}{p_2^d}.}
\]

其导数也直接闭合：

\[
\frac{\partial\lambda}{\partial p_1}
=
\frac{f_cK'(a)}{(p_2^d)^2},
\]

\[
\frac{\partial\lambda}{\partial p_2}
=-\frac{f_c[K(a)+aK'(a)]}{(p_2^d)^2}.
\]

因此：`NC_CC_SOURCE_CAPACITY_GATE = PASS_G6`。

### 2.2 TC/CT — Nguyen Eq. (3.18)–(3.19)

令

\[
t\ge0,\qquad p\ge0,\qquad F=f_c>0,\qquad T=f_t>0.
\]

将 Nguyen 的 signed source equations 精确换成物理幅值后，得到两条直线。

压轴侧：

\[
\boxed{
\frac{p}{F}+\frac{t}{3T}=1
}
\]

直到

\[
\boxed{
(p/F,t/T)=(0.8,0.6).
}
\]

拉轴侧：

\[
\boxed{
\frac{p}{2F}+\frac{t}{T}=1.
}
\]

两段严格在 \((0.8,0.6)\) 相交，故 capacity 值 C0 连续；源关系本身在该点存在有限 tangent kink。

定义

\[
\Phi_A=\frac{p}{F}+\frac{t}{3T},
\qquad
\Phi_B=\frac{p}{2F}+\frac{t}{T}.
\]

则沿固定当前 demand 射线的 re-cut factor 为

\[
\boxed{
\lambda_{TC}^{NC}=\frac1{\Phi_A}
\quad\text{or}\quad
\frac1{\Phi_B},
}
\]

由源分支条件有限判定。

轴退化严格成立：

\[
t=0\Rightarrow p=F,
\qquad
p=0\Rightarrow t=T.
\]

两段梯度为常数，因此同源 capacity derivative 完全闭合；不需要数值微分、材料点或加载步。

因此：`NC_TC_CT_SOURCE_CAPACITY_GATE = PASS_G6`。

### 2.3 对旧 NC reduction 的裁决

旧项目低参数式

\[
c_i^*=c_i(1+a_{cc}c_1c_2),
\qquad
c^*=c(1-\tau)
\]

不再作为二维 source identity。它们保留历史 provenance，但当前材料容量判断优先使用上面的 Nguyen/Foster–Kupfer source envelope。

单轴 Saenz backbone 与 T5 暂时不因本轮 capacity gate 自动改变；是否最终替换属于另一项 source/backbone 决策。

---

# Part B — UHPC

## 3. Liu 2024 CC exact proposed family recovered

Liu et al. 2024 的完整预印本已恢复 CC 原式。论文先给出 Kupfer 型候选族：

parabolic:

\[
(x+a y)^2+x+b y=0,
\]

elliptic:

\[
x^2-cxy+y^2-1=0,
\]

其中 \(x=f_1/f_{c,r},\ y=f_2/f_{c,r}\)。Table 5 的独立拟合参数为

\[
a=1.85,\qquad b=7.98,\qquad c_{Table5}=1.33.
\]

但是最终 proposed piecewise Eq. (4) 的机器可读正文明确显示 elliptic coefficient 为

\[
\boxed{c_{Eq4}=1.49},
\]

并采用：

\[
\boxed{
x^2-1.49xy+y^2-1=0}
\]

for

\[
\frac{f_1}{f_2}\le0.5
\quad\text{or}\quad
\frac{f_1}{f_2}\ge2.0,
\]

以及

\[
\boxed{
(x+1.85y)^2+x+7.98y=0
}
\]

for

\[
0.5\le\frac{f_1}{f_2}\le2.0.
\]

这里必须保留 source distinction：

```text
LIU2024_CC_TABLE5_FITTED_ELLIPSE_C = 1.33
LIU2024_CC_FINAL_EQ4_ELLIPSE_COEFFICIENT_AS_EXTRACTED = 1.49
```

当前不把两者强行改成同一个数。最合理的读取是：Table 5 报告独立拟合曲线参数，而 Eq. (4) 给出最终保守 piecewise proposed criterion；但论文正文没有在当前机器可读文本中解释 1.33 -> 1.49 的转换，因此 provenance 中保留警告。

### 3.1 G6 finite ray reduction

对 CC demand 的压应力幅值排序

\[
0\le p_m\le p_M,
\qquad
r=p_m/p_M\in[0,1].
\]

若 literal Eq. (4) 采用 elliptic branch \(r\le0.5\)，则

\[
\boxed{
\lambda_E
=
\frac{f_{c,r}}
{\sqrt{(p_m^d)^2-1.49p_m^dp_M^d+(p_M^d)^2}}.
}
\]

若采用 parabolic branch \(0.5\le r\le1\)，则

\[
\boxed{
\lambda_P
=
f_{c,r}
\frac{p_m^d+7.98p_M^d}
{(p_m^d+1.85p_M^d)^2}.
}
\]

因此 Liu CC 在 algebraic complexity 上明确满足 G6：只需要排序、比例判定、平方根/有理式和一个有限标量 re-cut。

### 3.2 当前阻断：piece join 的 literal C0 审计

在 \(r=0.5\) 处：

- Eq. (4) elliptic(1.49) 给 \(p_M/f_{c,r}=1.40719509\)；
- parabolic(1.85,7.98) 给 \(p_M/f_{c,r}=1.53553644\)。

两者相差约 9.12%（以 elliptic 值为分母）。因此按当前可读 Eq. (4) literal form，内部 join 不能直接宣告 C0 连续。

```text
UHPC_CC_SOURCE_FORM = RECOVERED
UHPC_CC_G6_FINITE_REDUCTION = PASS
UHPC_CC_INTERNAL_JOIN_C0 = PENDING_SOURCE_RECONCILIATION
```

不得为了消除该差异自行拟合新系数，也不得用 BH050/Abaqus/Pu 选择系数。若后续正式期刊版 Eq. (4) 或清晰原版证明当前预印本存在排版/OCR问题，则按 source 更正；否则保留 literal source kink/gap 并评估其作为 capacity gate 的有限分支处理。

## 4. UHPC TT exact conservative capacity

Liu 2024 明确说明双轴拉伸下 UHPC 峰值拉强度总体接近单轴拉强度，并保守取

\[
\boxed{f_1=f_2=f_{t,r}.}
\]

因此 capacity gate 可写为

\[
0\le t_1,t_2\le f_t,
\]

以及固定 demand 射线上的

\[
\boxed{
\lambda_{TT}^{UHPC}
=
\frac{f_t}{\max(t_1^d,t_2^d)}.
}
\]

该式是 capacity boundary，不假装定义完整双向 tensile stress–strain coupling。Hiew 2024 继续作为单调 fibre-bridged tensile backbone source。

`UHPC_TT_CAPACITY_GATE = PASS_G6`。

## 5. UHPC TC/CT exact capacity source + current softening role

Liu 2024 明确指出：

- sequential loading 比 proportional loading 更不利；
- conservative TC envelope 由 sequential path 控制；
- proposed envelope 为两段式：低压区 tensile strength 保持常值，之后下降至 uniaxial compression point。

正文给出 break at normalized compression \(p/f_c=0.352\) 和 slope coefficient 1.542。结合论文对两段的文字定义，容量关系可恢复为：

第一段：

\[
\boxed{
\frac{t}{f_t}=1,
\qquad
0\le\frac{p}{f_c}\le0.352.
}
\]

第二段：

\[
\boxed{
\frac{t}{f_t}+1.542\frac{p}{f_c}-1.542=0,
\qquad
0.352\le\frac{p}{f_c}\le1.
}
\]

系数舍入下，在 break point 第二段给 \(t/f_t=0.999216\)，与第一段的 1 仅有约 \(7.84\times10^{-4}\) 的舍入差；物理意图是同一点连接。

固定 demand 射线 \((t^d,p^d)\) 的两个有限 candidate 为：

\[
\lambda_1=\frac{f_t}{t^d},
\]

并检查

\[
\lambda_1\frac{p^d}{f_c}\le0.352,
\]

或

\[
\boxed{
\lambda_2
=
\frac{1.542}
{t^d/f_t+1.542p^d/f_c}
}
\]

并检查 scaled compression 位于第二段。

因此 Liu 2024 TC/CT **capacity gate** 本身满足 G6。

与此同时，若需要在 1D backbone evaluation 中体现 current TC compressive softening，Diab/Ferche 型 current-strain component 仍可作为候选：

\[
\beta_{TC}(\varepsilon_t)
=
\max\left[0.55,(1+2500\varepsilon_t)^{-0.20}\right],
\]

\[
\beta(0)=1,
\qquad
\beta'(\varepsilon_t)
=-500(1+2500\varepsilon_t)^{-1.20
}
\]

(active branch)。它不得扩张为材料点 crack-slip/history solver。

Liu 2023 的 \(\zeta_\sigma=0.8\) entry relation继续作为 source oracle，不直接作为 \(\varepsilon_t\to0^+\) 的 memoryless production entry，因为它会造成 1 -> 0.8 的立即跳变。

---

# Part C — nine-grid / seven-gate judgment

## 6. NC current material judgment

| Sector | source/candidate | axis/origin | derivative | boundedness | G6 | status |
|---|---|---|---|---|---|---|
| C | Saenz temporary backbone | PASS | analytic | PASS | PASS | retained temporarily |
| T | T5 temporary backbone | PASS | analytic | PASS | PASS | retained temporarily |
| CC | Nguyen Eq.3.17 source capacity | exact C axis; symmetric by ordering | analytic branch derivative; diagonal ordering kink | bounded finite | PASS | PASS as capacity gate |
| TC | Nguyen Eq.3.18 | exact C axis | constant gradient | bounded finite | PASS | PASS |
| CT | symmetric TC | exact C axis | constant gradient | bounded finite | PASS | PASS |
| TC internal join | Eq.3.18/3.19 | C0 exact at (0.8,0.6) | finite kink | PASS | PASS | PASS_WITH_SOURCE_KINK |
| TT | existing NC tensile capacity form provisional | axes preserved | analytic | PASS | PASS | not current blocker |

NC conclusion:

```text
NC_CC_SOURCE_CAPACITY_GATE = PASS
NC_TC_CT_SOURCE_CAPACITY_GATE = PASS
NC_OLD_CC_TC_HEURISTICS = DEMOTED_FROM_SOURCE_IDENTITY
NC_FULL_INCREMENTAL_NGUYEN = ORACLE_ONLY
```

## 7. UHPC current material judgment

| Sector | source/candidate | axis/origin | derivative | boundedness | G6 | status |
|---|---|---|---|---|---|---|
| C | UHPC compression backbone final selection | source candidates exist | source derivative exists for Zhang-type law | finite | potentially PASS | FINAL SELECTION OPEN |
| T | Hiew 2024 | uniaxial source | analytic branch derivatives | finite material range | PASS | PASS component |
| CC | Liu 2024 final Eq.4 | uniaxial axis exact through ellipse | analytic finite branch derivative | finite | PASS | JOIN C0 SOURCE AUDIT OPEN |
| TC/CT capacity | Liu 2024 sequential conservative envelope | exact T and C endpoints | piecewise constant derivative | finite | PASS | PASS capacity gate |
| TC current softening | Diab/Ferche component candidate | beta(0)=1 | analytic | beta>=0.55 | PASS | PASS component |
| TT capacity | Liu 2024 conservative uniaxial cap | exact T axes | piecewise max gate | bounded | PASS | PASS capacity gate |
| C3 | Wang/Zhou/Zhang | outside current 2D plane-stress production | — | — | oracle only | qualification only |

UHPC conclusion:

```text
UHPC_CC_SOURCE_FORM = RECOVERED
UHPC_CC_G6_FINITE_REDUCTION = PASS
UHPC_CC_INTERNAL_JOIN_C0 = PENDING_SOURCE_RECONCILIATION
UHPC_TC_CT_CAPACITY_GATE = PASS_G6
UHPC_TT_CAPACITY_GATE = PASS_G6
UHPC_TC_CURRENT_SOFTENING = PASS_COMPONENT
UHPC_COMPRESSION_BACKBONE_FINAL_SELECTION = OPEN
UHPC_FULL_7GATE = NOT_YET_LOCKED
```

## 8. Seven-gate summary

| Gate | NC | UHPC |
|---|---|---|
| G1 compression | PASS_WITH_STRENGTH_IDENTITY_CAVEAT | OPEN final source selection |
| G2 tension | PASS temporary T5 | PASS Hiew component |
| G3 CC/TC/CT/TT source | PASS | PASS at capacity-source level |
| G4 plane stress / Poisson | unchanged / PASS | unchanged / PASS |
| G5 same-source derivative | PASS piecewise; source kinks explicit | PASS for recovered branches; CC join C0 open |
| G6 finite direct algebraic | PASS | PASS for all adopted capacity components |
| G7 no Pu backfit | PASS | PASS |

## 9. Current stop/go decision

This stage does **not** authorize structural Pu rerun.

The explicit architecture has not been damaged: all newly admitted 2D capacity gates reduce to a finite number of ratios, algebraic/rational/square-root evaluations and scalar branch checks. No spatial/material discretization has been introduced.

The next material-only tasks are:

1. reconcile Liu 2024 final CC Eq. (4) internal join / `1.33 vs 1.49` provenance using the clearest authoritative final source available;
2. freeze one UHPC uniaxial compression backbone and verify its source derivative and parameter identity for the project UHPC family;
3. rerun the full material nine-grid certificate after 1–2, still without structural Pu;
4. only after `UHPC_FULL_7GATE = PASS` may the structural 1D->2D acceptance tables be regenerated.

```text
MATERIAL_REORGANIZATION_7GATE = EXECUTED_PARTIAL
STRUCTURAL_BACKBONE_CHANGED = FALSE
STRUCTURAL_PU_RERUN = NOT_AUTHORIZED
```
