# NZ-SCCM — Swartz 原始试验材料来源、养护与 0.85 强度身份审计

**Date:** 2026-08-21 22:35 +08:00  
**Scope:** 只审计 Swartz 24板原始试验材料来源与当前 ultimate-capacity 解释；不修改 `D/Pcr/C/G/J/q0/Ppb`，不使用试验 `Pf` 反标任何理论参数。

## 1. Primary-source evidence newly recovered

当前账户资料中已直接找到两篇 Swartz 试验同期原始文献：

1. Swartz, Rosebraugh & Berman (1974), *Buckling Tests on Rectangular Concrete Panels*, ACI Journal, 71(1), 33–39.
2. Swartz, Rosebraugh & Rogacki (1974), *A Method for Determining the Buckling Strength of Concrete Panels*, Experimental Mechanics, 14(4), 138–144.

这两篇原始来源使此前“Swartz 的每板混凝土强度是否只是名义/批次值”的疑问基本闭合。

## 2. Casting / curing / companion-cylinder chain

ACI 试验论文明确说明：

- 每块板在 plywood form 上浇筑；
- 约3天湿养后转入 100% humidity curing room；
- 板在试验前2天移出养护室并放入试验框架；
- **每块板均配套浇筑2个圆柱体**；
- 两个圆柱体在对应板试验当天测试；
- 板试验日为浇筑后第28天；
- Table 1 给出的 `f'_c` 和对应峰值应变 `eps0` 是该板2个圆柱体的平均值。

Experimental Mechanics 同期方法论文给出更具体的配套试件信息：

- companion cylinders 为 **6 in × 12 in**；
- plates and cylinders 均先留在模具内，文中写为4天后一起进入 100% humidity curing room；
- 试验前2天一起移至 test area，先干燥约1天再布置应变计/进入试验框架；
- 最大骨料粒径约 1/4 in；
- 3/4 in 与1 in板的28 d设计强度为3000 psi，1-1/4 in板为2500 psi。

两篇同期论文对“转入湿养室”的天数存在 **3 d vs 4 d** 的一日表述差异，不能擅自消去；但二者一致支持：板和 companion cylinders 属于同一试验计划、采用高湿养护，并在28 d阶段用于材料/板试验。

### 2.1 What is now ruled out

因此以下旧假设不再可用于解释 Case9/10 或其他重复对的差异：

```text
GENERIC_DESIGN_STRENGTH_ONLY = REJECTED
UNCONTROLLED_TEST_AGE_DIFFERENCE = REJECTED
ONE_COMMON_STRENGTH_ASSIGNED_TO_MANY_PANELS = REJECTED
```

每块板都有自己的 companion-cylinder average，故 `fcyl` 与 `eps0` 是 **panel-specific measured material anchors**。

严格措辞：原文写的是“two cylinders for each panel/plate”；未找到逐浇筑 batch ID，因此不把“同一搅拌批次编号”写成已证实事实。

## 3. No additional strength-test family found yet

在已找到的两篇 Swartz 原始论文、Nguyen 复述以及当前公开网络检索中，尚未找到 Swartz 24板对应的：

- cube strength；
- prism strength；
- core / direct in-situ compressive strength；
- splitting/direct tensile strength `ft`；
- 每板单独的静力弹性模量实测值。

因此 TC gate 的 `ft` 仍未 source-close。

Rogacki (1972) thesis 被原论文列为：

`Design of Casting and Testing Apparatus for Reinforced Concrete Panels`

Berman (1973) thesis 被原论文列为：

`The Determination of the Buckling Strength of Reinforced Concrete Plates`

本轮针对 K-State / repository / general web 的精确题名检索未找到可直接取得的全文。不得用未取得论文内容补写材料参数。

## 4. Important correction: E0 is not an independent measured modulus

当前 Swartz 输入中的 `E0` 来自 Nguyen/Swartz parabola relation 的近似，而不是 Table 1 独立弹模试验：

\[
E_0\approx\frac{2 f_c^{analysis}}{\varepsilon_0},
\qquad f_c^{analysis}=0.85f'_{cyl}.
\]

例如 Case9/10 的 `E0≈15480/17656 MPa` 的差异主要由 panel-specific `fcyl` 与 `eps0` 推导而来，不能把它当成第三项独立材料实测证据。

## 5. Trusted-pair source matrix

以下只使用原始 Table 1 / Table 2 量：

| pair | fcyl1→fcyl2 | Δfcyl | eps0 change | Pcr identified change | Pf change | Pf/Pcr |
|---|---:|---:|---:|---:|---:|---:|
| 1→2 | 26.84→26.20 MPa | -2.38% | -8.57% | -19.74% | +3.36% | 0.881→1.134 |
| 9→10 | 17.67→18.28 MPa | +3.45% | -9.28% | +20.69% | +11.23% | 1.213→1.118 |
| 19→20 | 23.76→24.43 MPa | +2.82% | +5.32% | +7.42% | -1.30% | 1.211→1.113 |
| 21→22 | 24.98→24.74 MPa | -0.96% | -5.26% | -7.41% | -3.38% | 1.095→1.143 |

### 5.1 Case1/4 Pcr identification warning

ACI Table 2 确实列 Case1：`Pcr=125.1 kip`, `Pf=110.2 kip`；Case4 同样 `Pf<Pcr`。

这不是当前数据库列名颠倒。原文明确说明 Case1/4 的 Pcr 来自 **Southwell plots**，并同时指出该方法对非线性材料会高估实际屈曲荷载；作者说明视觉观察到的实际屈曲更低。

因此：

```text
TABLE2_PCR_PF_COLUMN_SWAP = FALSE
CASE1_CASE4_SOUTHWELL_PCR_OVERIDENTIFICATION = SOURCE_ACKNOWLEDGED
EXPERIMENTAL_PCR_AS_UNIFORM_CALIBRATION_TARGET = PROHIBITED
```

这进一步支持当前项目“不为实验Pcr修改稳定刚度”的治理边界。

## 6. Reinterpretation of the 0.85 factor

Nguyen 对 Swartz 理论来源的复述明确写出：

\[
\sigma_c=0.85f'_{cyl}(2\xi-\xi^2),\qquad \xi=\varepsilon/\varepsilon_0.
\]

Nguyen 自己第5章 Swartz FE 也采用 `0.85 fcyl`，用于表示 panel in-situ strength 与 standard cylinder strength 的差异。

因此 `0.85` 不是当前项目任意加入的经验修正；它属于历史 Swartz/Nguyen **initial-buckling constitutive lineage**。

但是当前显式理论求的是 postbuckling + section ultimate capacity。必须把三个强度身份分开：

\[
\boxed{
 f'_{cyl,28}
 \neq
 f_{c,\,buckling-law}=0.85f'_{cyl,28}
 \neq
 f_{c,\,ultimate-section}\;\text{(尚需来源闭合)}
}
\]

- `f'cyl,28`：每板2个 companion cylinders 的实测28 d ultimate strength；
- `0.85 f'cyl,28`：历史初始屈曲 parabola / Nguyen FE 的分析强度身份；
- `fc,ultimate-section`：当前后屈曲截面容量应采用的极限材料身份，**不能直接由 Pf 反标，也不能未经来源证明自动等于前两者之一**。

因此此前“把0.85统一改成1.0是否改善 Pu”的计算只能保留为 capacity sensitivity，不得升级为 source correction。

## 7. Implication for current anomalous pairs

### Case1/2

panel-specific fcyl 很接近，而当前未加 TC gate 的显式 Pu 成对偏高。TC gate 在临时 `ft=0.10fc` 下选择性地下修1/2，而9/10不触发，故：

```text
CASE1_2_PRIMARY_WORKING_MECHANISM = TC_CAPACITY_SIDE
FT_SOURCE_CLOSURE = STILL_BLOCKING
```

### Case9/10

Case10 的 companion-cylinder strength 只比 Case9 高约3.45%，峰值应变低约9.3%，而实验 Pf 高约11.2%。因为这些材料量已经是 panel-specific measured anchors，“只是未知混凝土批次不同”不再是足够解释。

Case9 可由 capacity-strength sensitivity + small CC 接近试验；Case10仍残留约8–9%的差距。当前应保留：

```text
CASE10 = CREDIBLE_RESIDUAL_ANOMALY_OR_UNMODELLED_SPECIMEN_EFFECT
DO_NOT_BACKFIT_CASE10 = TRUE
```

### Case19/20 and Case21/22

两组 companion-cylinder properties 和 Pf 均具有较好重复性；19/20 对 `0.85→1.0` capacity-only sensitivity 极敏感且恰好接近试验，而21/22反而会被抬高过头。这证明不存在一个由当前24板结果直接支持的全局 `0.85→constant` replacement。

## 8. Current decision

```text
SWARTZ_PANEL_SPECIFIC_FCYL28 = SOURCE_CLOSED
SWARTZ_PANEL_SPECIFIC_EPS0 = SOURCE_CLOSED
SWARTZ_PANEL_SPECIFIC_FT = OPEN
SWARTZ_CUBE_PRISM_CORE_STRENGTH = NOT_FOUND
SWARTZ_E0_INDEPENDENT_MEASUREMENT = NO_EVIDENCE; CURRENT E0 DERIVED
SWARTZ_0P85_IDENTITY = HISTORICAL_BUCKLING_ANALYSIS_STRENGTH
UNIVERSAL_0P85_REMOVAL_FOR_ULTIMATE = NOT_AUTHORIZED
STRUCTURE_LAYER_MODIFICATION = NONE
EXPERIMENTAL_PF_BACKFIT = PROHIBITED
```

## 9. Next recommended calculation

下一步不再继续猜测养护/龄期，而应固定这条已闭合材料来源链，做一个 **source-native ultimate identity audit**：

1. 保持 `Ppb(q)` 结构层完全不动；
2. 以 `f'cyl,28`、`eps0` 作为每板直接实测锚点；
3. 将 `0.85 fcyl` 只保留其已证明的 buckling-law 身份；
4. 对当前 section-capacity law 逐项识别哪些项实际继承了 `0.85`，哪些项理论上属于 ultimate material limit；
5. 不引入新经验系数、不使用 Pf 选根；
6. 再把 TC/CC gate 与该 material-identity split 合并，先检查可信重复对 1/2、9/10、19/20、21/22。

该步骤的目的不是“找到一个更好的系数”，而是消除 **buckling constitutive peak 与 ultimate section strength 被混用** 的理论身份错误。