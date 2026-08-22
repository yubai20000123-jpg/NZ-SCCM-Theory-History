# NZ-SCCM — Swartz RC 分组波形与当前显式模态审计

**Date:** 2026-08-22 15:20 +08:00  
**Status:** `EXECUTED / RC_WAVEFORM_AUDIT / MATERIAL_FROZEN / NO_MODE_BACKFIT`

## 0. 本轮目标

本轮停止继续修改普通混凝土材料关系，只检查 Swartz 24 块 RC 板的屈曲波形：

1. 同一厚度/宽厚比分组内，试验/Nguyen 重构的波形是否一致；
2. 当前 Marguerre–Airy 显式前端选择的半波数是否与来源波形一致；
3. 波形一致/不一致与当前承载力误差之间是否存在值得继续检查的结构规律。

不使用试验承载力反选半波数，不修改材料参数。

---

## 1. Swartz 原始试验对波形的直接证据

Swartz–Rosebraugh–Berman (1974) 的 24 块板均为四边简支、单向轴压。原论文明确指出所有板均以双向曲率鼓包的形式屈曲，但实际鼓包位置和形状并非严格统一：

- 原论文说明，一部分板的变形类似 Plate 21；
- 但“in general” 试件更常见的是类似 Plate 6 的**单个 panel 内鼓包**；
- Table 2 甚至逐板列出了 bulge location，说明实际鼓包存在位置离散性；
- 因而原始试验不能被简化成“同一组每一块板都有完全相同的正弦波形”。

所以需要区分：

```text
RAW_EXPERIMENTAL_BULGE_MORPHOLOGY = NOT STRICTLY IDENTICAL WITHIN GROUP
GROSS HALF-WAVE CLASSIFICATION = CAN STILL BE USED AS A GROUP-LEVEL IDEALIZATION
```

---

## 2. Nguyen 对 Swartz24 的组级波形分类

Nguyen Chapter 5 对同一批 24 块板作了 FE 稳定分析，并给出了非常清楚的组级结论。

### Group 1: Panels 1–8

- b/t ≈ 48；
- Nguyen：`approximate one half sinusoidal wave`。

### Group 2: Panels 9–16

- b/t ≈ 38.3；
- Nguyen：与 Group 1 同类，`approximate one half sinusoidal wave`；
- Figure 5.8 的 Panel 14 是代表例。

### Group 3: Panels 17–24

- b/t ≈ 63.1；
- Nguyen：`two sinusoidal half waves`；
- Figure 5.6 的 Panel 21 是代表例；
- Nguyen 还指出 Panel 21 的 FE 波形与 Swartz 实验记录的波形相似。

因此 Nguyen 的**理想化组级模式**为：

```text
PANELS_1_8   ≈ m=1
PANELS_9_16  ≈ m=1
PANELS_17_24 ≈ m=2
```

这里 m 表示沿 2.44 m 长边/加载方向的半波数。

必须保留来源层级差异：Nguyen 给的是 FE 模态分类；Swartz 原始试验形态更离散，通常表现为局部单 panel 鼓包，同时存在 Plate21 类多波/双波形态。

---

## 3. 当前 Marguerre–Airy 前端实际上把全部 24 块板选成 m*=2

当前整数半波选择公式：

\[
P_{cr,j}=b\frac{D_x\alpha^4+2H\alpha^2\beta_j^2+D_y\beta_j^4}{\beta_j^2},
\]

\[
\alpha=\frac{\pi}{b},\qquad
\beta_j=\frac{j\pi}{a}.
\]

Swartz 所有板均有

\[
a=2b.
\]

当前 RC 配筋在 x/y 两方向相同，因此

\[
D_x=D_y=D.
\]

故

\[
\beta_j=\frac{j}{2}\alpha,
\]

从而

\[
P_{cr,j}=b\alpha^2
\left[
D\left(\frac{4}{j^2}+\frac{j^2}{4}\right)+2H
\right].
\]

其中 `2H` 与 j 无关，因此只需最小化

\[
f(j)=\frac{4}{j^2}+\frac{j^2}{4}.
\]

正整数上：

\[
f(1)=4.25,
\qquad
f(2)=2,
\qquad
f(3)=2.69444\ldots
\]

故当前初始弹性前端对所有 Swartz 板都严格得到

\[
\boxed{m_*=2}.
\]

这不是 Case21 偶然结果，而是由 `a/b=2 + Dx=Dy` 直接决定。

Case21 的实际候选再次验证：

|j|ell=a/j / mm|Pcr / kN|
|---:|---:|---:|
|1|2440|636.150436|
|2|1220|407.136279|
|3|813.333|477.819661|
|4|610|636.150436|

即 `m*=2`。

---

## 4. 三组波形一致性结论

|分组|板号|Swartz 原始试验形态|Nguyen FE 理想化|当前显式计算|判断|
|---|---|---|---|---|---|
|Group 1|1–8|一般以单 panel 鼓包为主，逐板位置有离散|≈1 half-wave|2 half-waves|**组级明显不一致**|
|Group 2|9–16|一般仍以单 panel 鼓包为主，形态并非逐板完全相同|≈1 half-wave|2 half-waves|**组级明显不一致**|
|Group 3|17–24|存在 Plate21 类双波形态，但原试验总体仍有鼓包位置/形态离散|2 half-waves|2 half-waves|**粗粒度半波数一致；逐板精细形态不保证一致**|

因此：

```text
NGUYEN_GROUP_MODE_INTERNAL_CLASS = 1-16 APPROX M1 / 17-24 M2
CURRENT_EXPLICIT_MODE_CLASS = M2 FOR ALL 24
CURRENT_MODE_MISMATCH = GROUP1 + GROUP2
CURRENT_MODE_MATCH_GROSS = GROUP3
```

---

## 5. 与当前选定重复/准重复板承载力结果对照

当前材料/二维工作值保持不变，本轮只叠加波形判断：

|Case|组|Nguyen 波形|当前波形|2D working / kN|Pf / kN|误差|波形判断|
|---:|---|---|---|---:|---:|---:|---|
|1|G1|≈m1|m2|495.989|490.194|+1.182%|mismatch|
|2|G1|≈m1|m2|501.025|506.652|−1.111%|mismatch|
|9|G2|≈m1|m2|515.424|625.865|−17.646%|mismatch|
|10|G2|≈m1|m2|534.711|696.147|−23.190%|mismatch|
|19|G3|m2|m2|339.177|377.654|−10.188%|gross match|
|20|G3|m2|m2|335.013|372.761|−10.127%|gross match|
|21|G3|m2|m2|350.460|368.313|−4.847%|gross match|
|22|G3|m2|m2|351.679|355.858|−1.174%|gross match|

### 5.1 Case1/2

尽管波形是 `m1 source-class vs m2 current` 的明显不一致，当前 2D 荷载却与试验非常接近。

因此不能用 Case1/2 的良好荷载误差反过来证明当前 m=2 正确。更合理的当前判断是：

```text
CASE1_2_GOOD_LOAD_MATCH_DOES_NOT_VALIDATE_MODE
POSSIBLE_ERROR_COMPENSATION = OPEN / NOT PROVEN
```

二维 TC re-cut 与错误的结构半波选择之间存在补偿的可能，但目前不能把补偿当成已证明事实。

### 5.2 Case9/10

这两块同时出现：

- source/Nguyen ≈ m1；
- current = m2；
- 2D TC criterion 不活动；
- 仍低估约 17.6% 和 23.2%。

因此 Case9/10 是目前最值得优先检查的**结构模态问题样本**。此前把其偏差主要理解成材料问题是不完整的。

### 5.3 Case19/20、21/22

这些板属于 Group 3，Nguyen 和当前计算都为两半波，因此大尺度波数一致。

残余误差仍从约 −10% 到 −1%，说明：

```text
GROSS_MODE_MATCH != GUARANTEE_OF LOAD MATCH
```

这里误差不能再简单归因于“半波数选错”。

---

## 6. 根因：当前模式搜索是初始弹性对称刚度搜索，而 Nguyen 的模式受加载方向非线性切线影响

当前前端使用初始 `Dx,Dy,H` 做整数 m 搜索。对 Swartz：

\[
D_x=D_y
\]

使 `a/b=2` 自动锁定 `m=2`。

但 Nguyen 对 Group1/2 的解释恰恰指出：屈曲时加载方向混凝土已经接近峰值，应使用明显降低的加载方向 tangent modulus，而非两个方向相同的初始弹性模量；其 FE/STRAND6 比较中，采用 unloaded direction 的初始模量和 loaded direction 的当前 tangent modulus 后，能得到与 Panel1/14 类似的一半波形。

因此当前模式选择的潜在结构缺口可明确写成：

\[
\boxed{
\text{INITIAL-ELASTIC }D_x=D_y\text{ MODE SEARCH}
\neq
\text{NONLINEAR TANGENT-ORTHOTROPIC MODE AT BUCKLING}
}
\]

这与二维材料容量约束是否可计算是两个不同问题。

---

## 7. 当前裁决与下一步

本轮不修改材料关系，也不根据试验波形直接指定某块板的 m。

当前结论：

```text
RC_WAVEFORM_AUDIT = EXECUTED
RAW_SWARTZ_WITHIN_GROUP_WAVEFORM = NOT STRICTLY IDENTICAL
NGUYEN_GROUP_MODE_CLASS = PANELS1_16 APPROX M1 / PANELS17_24 M2
CURRENT_MARGUERRE_MODE = M2 ALL 24
RC_MODE_MISMATCH = GROUP1_GROUP2
MATERIAL_REOPEN = NO
```

下一步优先级转为 RC 结构模式：固定当前材料体系，对 `m=1` 与 `m=2` 两个有限候选分别进行显式计算，首先检查 Case1/2、9/10、19/20、21/22。

重要规则：

1. `m=1/m=2` 是有限理论候选，不是按试验荷载选根；
2. 试验波形仅用于事后验证；
3. 不允许“哪个 Pu 更接近试验就选哪个 m”；
4. 最终需要建立一个由当前切线刚度/稳定条件自身决定的 finite mode gate；
5. 在 mode gate 完成前，不再将 `m=2 all 24` 视为已验证的 RC 结构事实。

```text
NEXT_RC_TASK = FINITE_M1_M2_STRUCTURAL_CANDIDATE_AUDIT_WITH_MATERIAL_FIXED
Z_GENERAL_S_TASK = DEPRIORITIZED_BY_USER
```
