# NZ-SCCM — Cedolin–Mulas 1984 与 Bažant–Tsubaki 1980 显式材料候选公式级筛选 R01

**Time:** 2026-08-23 20:43 +08:00  
**Status:** `CEDOLIN_MULAS = PARTIAL_PASS_NOT_PRODUCTION / BAZANT_TSUBAKI = FAIL_PRODUCTION_EXPLICITNESS / NGUYEN_CC_TC_TT_REPLACEMENT = NOT_FOUND_YET`

## 0. 本轮唯一问题

目标不是泛泛综述，而是检查两篇候选能否真正替代 Nguyen 的 `CC/TC/TT/TCX` 生产材料状态机，使材料层可写成

\[
(\varepsilon_x,\varepsilon_y,\gamma_{xy})
\mapsto
(\sigma_x,\sigma_y,\tau_{xy})
\]

并满足：

1. 当前应变唯一决定当前应力；
2. 不依赖历史/加载步；
3. 有一致切线；
4. 覆盖达到极限所需的峰后域；
5. 与锁定 Airy 有限三角应变场复合后，不重新制造难以闭合的空间积分。

Airy/Marguerre 结构层本轮完全不修改。

---

# 1. Cedolin–Mulas 1984

论文：L. Cedolin & M. G. Mulas, *Biaxial Stress-Strain Relation for Concrete*, J. Eng. Mech. 110(2), 187–206, 1984.

## 1.1 来源明确支持的模型身份

原文摘要明确：

- 单调双轴加载；
- **up to peak stress**；
- total、explicit stress–strain relation；
- secant bulk/shear moduli 是应变张量前两个不变量的非线性函数；
- plane stress 中第三主应变本来会导致隐式方程，作者专门用一个高精度经验显式式把第三应变写成面内主应变的函数，从而保留显式性；
- 只需要初始弹性参数和抗压强度等少量参数。

因此其生产接口可以恢复成以下结构。

## 1.2 从面内应变到主应变

对 plane-stress 面内应变张量

\[
\mathbf E_2=
\begin{bmatrix}
\varepsilon_x & \gamma_{xy}/2\\
\gamma_{xy}/2 & \varepsilon_y
\end{bmatrix},
\]

显式求面内主应变

\[
\varepsilon_{1,2}
=\frac{\varepsilon_x+\varepsilon_y}{2}
\pm
\sqrt{\left(\frac{\varepsilon_x-\varepsilon_y}{2}\right)^2
+\left(\frac{\gamma_{xy}}2\right)^2}.
\]

作者的 plane-stress 显式化可抽象为

\[
\boxed{\varepsilon_3=F_3(\varepsilon_1,\varepsilon_2)}
\]

其中 `F3` 是论文拟合得到的显式经验函数，而非每个材料点再解 `sigma_3=0` 的非线性方程。

## 1.3 不变量与应力映射

定义体积应变

\[
\varepsilon_v=\varepsilon_1+\varepsilon_2+\varepsilon_3,
\]

平均应变

\[
\varepsilon_m=\frac{\varepsilon_v}{3},
\]

偏应变

\[
e_i=\varepsilon_i-\varepsilon_m,
\]

以及论文采用的第二应变不变量/应变强度 `gamma`。其核心 secant law 为

\[
K_s=K_s(\varepsilon_v,\gamma),
\qquad
G_s=G_s(\varepsilon_v,\gamma).
\]

论文中 `K_s` 与 `G_s` 不是常数；尤其 `K_s` 明确依赖体积与剪切/偏应变强度，以描述临近峰值时的非弹性体积变化。其经验式包含 `gamma/gamma_c(epsilon_v)` 等有理组合；`gamma_c` 本身又是体积应变的拟合函数。

于是主应力直接为

\[
\boxed{
\sigma_i
=K_s\,\varepsilon_v+2G_s e_i,
\qquad i=1,2,3.
}
\]

再按面内主方向旋转回全局坐标，得到

\[
\boxed{
(\varepsilon_x,\varepsilon_y,\gamma_{xy})
\to
(\sigma_x,\sigma_y,\tau_{xy})
}
\]

且全过程没有 `CC/TC/TT/TCX` 状态标签作为生产变量。

## 1.4 一致切线

因为 `F3`, `Ks`, `Gs` 都是当前应变的显式函数，除经验分段/峰值边界外，一致切线可直接链式求导：

\[
\mathbf C_t
=\frac{\partial\boldsymbol\sigma}{\partial\boldsymbol\varepsilon}.
\]

例如主坐标中

\[
\frac{\partial\sigma_i}{\partial\varepsilon_j}
=
K_s\frac{\partial\varepsilon_v}{\partial\varepsilon_j}
+\varepsilon_v\frac{\partial K_s}{\partial\varepsilon_j}
+2G_s\frac{\partial e_i}{\partial\varepsilon_j}
+2e_i\frac{\partial G_s}{\partial\varepsilon_j}.
\]

所以 `CONSISTENT_TANGENT = PASS_IN_PRINCIPLE`。

## 1.5 关键硬失败 1：峰后覆盖

论文自己的适用范围就是 `up to peak stress`。因此它不能单独覆盖：

- 压缩峰后软化；
- 拉裂后的长期软化/残余；
- RC 壁板达到极限前若已跨过局部峰值的状态。

故

```text
POSTPEAK_COVERAGE = FAIL
```

不能把另一篇峰后曲线任意拼接到 Cedolin–Mulas 上，否则会成为项目自创 hybrid，需要重新证明边界连续、一致切线和参数身份。

## 1.6 关键硬失败 2：与 Airy 复合后的零空间积分

锁定 Airy 应变场是有限三角场，但 Cedolin–Mulas 需要

\[
\gamma
=\sqrt{Q_2(\varepsilon_x,\varepsilon_y,\gamma_{xy})},
\]

其中 `Q2` 是应变分量的二次型。代入有限三角 Airy 场后，`gamma` 一般成为

\[
\sqrt{\text{finite trigonometric polynomial}}.
\]

随后 `Ks,Gs` 又含 `gamma/gamma_c` 等有理/经验函数，因此

\[
\sigma(x,y,z)
\]

一般不再是有限三角多项式，也不能直接落入现有 D15 finite-moment algebra。

这与此前 Airy conic/quartic 分区遇到的困难同源：它消除了 `CC/TC/TT` 状态机，却没有消除非多项式不变量函数。

因此

```text
DIRECT_CURRENT_MAP = PASS
HISTORY_FREE_MONOTONIC = PASS
PLANE_STRESS_EXPLICIT = PASS
CONSISTENT_TANGENT = PASS_IN_PRINCIPLE
POSTPEAK = FAIL
D15_FINITE_TRIG_CLOSURE = FAIL_GENERIC
PRODUCTION_REPLACEMENT_OF_NGUYEN = FAIL
```

它最适合的身份是：`PREPEAK_UNIFIED_CURRENT-MAP REFERENCE/CANDIDATE`，不是当前最终生产材料。

---

# 2. Bažant–Tsubaki 1980

论文：Z. P. Bažant & T. Tsubaki, *Total Strain Theory and Path-Dependence of Concrete*, J. Eng. Mech. Div. 106(6), 1151–1173, 1980.

## 2.1 优点：它确实覆盖峰值和软化

论文明确针对无连续裂缝 plain concrete，采用 total-strain / deformation-theory 型代数关系，并覆盖：

- peak stress points；
- failure envelopes；
- strain softening；
- inelastic dilatancy/compaction；
- monotonic loading；
- 不处理 unloading。

并给出用于结构分析的 tangential incremental form。

因此与 Cedolin–Mulas 相比：

```text
POSTPEAK_COVERAGE = PASS
TANGENT_FORM = PASS
```

## 2.2 但它不是我们要求的“计算显式 current operator”

论文开头虽然在单调加载的一一性意义上写出

\[
\sigma_{ij}=F_{ij}(\varepsilon_{km}),
\]

但作者随后非常明确地区分“存在代数 total relation”与“实际可显式计算”。为覆盖软化和非弹性体积变化，他们采用的实际广域关系允许写成

\[
\boxed{f_{ij}(\boldsymbol\sigma,\boldsymbol\varepsilon)=0},
\]

而不是一个可直接逐点代值的闭式

\[
\boldsymbol\sigma=\mathbf M(\boldsymbol\varepsilon).
\]

作者明确说明：实际非显式关系用于结构分析时需要先微分成增量形式；他们甚至指出若强行保持 explicitness，会牺牲对真实混凝土行为的描述能力。

所以对本项目最关键的门：

```text
DIRECT_EXPLICIT_EPS_TO_SIGMA = FAIL
```

数学上“给定 strain 对应唯一 stress”并不等于程序上无需局部非线性求解即可得到 stress。

## 2.3 历史/路径问题也没有真正消失

基础 total-strain law 是 path-independent 的，但作者为了非比例加载加入 path-dependent corrections；这些修正在 proportional loading 下消失。

Airy 后屈曲局部应变路径一般并非严格比例。原因是同一点的不同来源项随 `q` 的尺度不同：

\[
\varepsilon^{m}
\sim P(q)\;\text{和}\;q(q+2q_0),
\]

而弯曲项

\[
z\kappa\sim q.
\]

因此一般可写成

\[
\boldsymbol\varepsilon(q)
=
\mathbf a P(q)+\mathbf b q(q+2q_0)+\mathbf c q,
\]

三个系数向量通常不共线，故

\[
\boldsymbol\varepsilon(q_2)
\not\parallel
\boldsymbol\varepsilon(q_1)
\]

是 generic 情况。

因此若把 Bažant–Tsubaki 的 path-dependent correction 全部删掉，只能作为本项目主动选择的 `NO_HISTORY APPROXIMATION`，不能声称是论文在 Airy 路径下的严格退化。

## 2.4 连续裂缝域不匹配

论文摘要明确限定 `plain concrete free of continuous cracks`。RC 壁板极限附近若存在连续拉裂区，该限定不能忽略。

所以：

```text
RC_CRACKED_DOMAIN_SUPPORT = FAIL/UNSUPPORTED
```

## 2.5 Airy 解析闭合

由于实际模型本身是 `f(sigma,epsilon)=0` 型非显式代数关系，若放到 Airy 全场，首先需要对每个连续位置求局部应力；然后其 nonlinear invariant/softening relation 再进入空间投影。

这不仅没有形成 finite trigonometric stress field，反而在积分前增加了一层局部代数隐式求解。

故

```text
D15_FINITE_TRIG_CLOSURE = FAIL_GENERIC
ZERO_SPATIAL_INTEGRATION_CURE = FAIL
```

总判：

```text
POSTPEAK = PASS
TANGENT = PASS
NO_UNLOADING = PASS
DIRECT_EXPLICIT_CURRENT_MAP = FAIL
PATH_FREE_FOR_GENERIC_AIRY = FAIL_SOURCE_EXACTNESS
CONTINUOUS_CRACKED_RC_DOMAIN = FAIL/UNSUPPORTED
PRODUCTION_REPLACEMENT_OF_NGUYEN = FAIL
```

---

# 3. 两篇不能直接拼接

一种表面上诱人的做法是：

- Cedolin–Mulas 用峰前；
- Bažant–Tsubaki 用峰后。

本轮拒绝把它当作当前路线。原因：

1. 两篇的状态变量、参数化和 plane-stress 消元不同；
2. 峰值面上的 stress continuity 不自动成立；
3. tangent continuity 更不自动成立；
4. Bažant–Tsubaki 的实际关系不是 direct explicit；
5. 拼接后仍没有证明与 Airy 复合可有限解析积分。

没有独立来源支持这种 hybrid 时，它会成为新的项目材料模型，而不是“采用已有文献模型”。

---

# 4. 本轮最终矩阵

| Gate | Cedolin–Mulas 1984 | Bažant–Tsubaki 1980 |
|---|---|---|
| 当前应变唯一决定当前状态 | PASS（单调峰前） | 概念上一一；实际非显式 |
| 直接 `eps -> sigma` 计算显式 | **PASS** | **FAIL** |
| 无历史 | PASS（单调峰前） | 基础式近似 PASS；一般非比例需 path correction |
| plane stress | **显式经验消元 PASS** | 可处理，但非 direct explicit 主优势 |
| 一致/切线刚度 | PASS_IN_PRINCIPLE | PASS（增量切线） |
| 峰值 | PASS | PASS |
| 峰后软化 | **FAIL** | **PASS** |
| 连续裂缝 RC 域 | 不足 | **论文明确不覆盖 continuous cracks** |
| 避开 `CC/TC/TT` 标签 | PASS | PASS |
| 与 Airy 复合后有限 D15 闭合 | **FAIL_GENERIC** | **FAIL_GENERIC** |
| 替代 Nguyen production | **NO** | **NO** |

因此目前没有一篇同时满足

\[
\boxed{
\text{explicit} + \text{history-free} + \text{postpeak}
+ \text{RC-relevant} + \text{Airy finite-integrable}
}
\]

五个条件。

---

# 5. 初步向外扩展筛选

既然两个主候选均未通过，按当前治理允许继续检索“避开 CC/TC/TT 状态机”的材料家族，但优先检查其数学结构，而不是先比较预测误差。

## 5.1 Gerstle 1981 — 当前最值得下一步恢复

*Simple Formulation of Biaxial Concrete Behavior* 采用 isotropic nonlinear octahedral representation，变量 tangent bulk/shear moduli；关键简化是 biaxial 状态下 tangent moduli 采用**线性变化**，参数只需常规强度与刚度数据。

它值得优先检查的原因不是“精度一定更好”，而是：若这些线性 tangent-modulus 关系能在当前单调加载假设下解析积分成 total law，则最终 stress 可能降到低阶代数函数，显著比 Cedolin–Mulas 的根式/有理 invariant map 更适合 Airy。

但目前只能标记：

```text
GERSTLE_1981 = NEXT_FORMULA_RECOVERY_CANDIDATE
```

不能提前宣称它是 current-state、path-independent 或 postpeak-complete；摘要只明确 tangent formulation。

## 5.2 Pekau–Zhang–Liu 1992 — 排除为主线

虽然名称就是 `strain-space model`，但其完整理论属于 strain-space plasticity，含：

- loading criterion；
- hardening/softening functions；
- initial yield/failure surfaces；
- cracking/crushing/mixed failure mode 判断；
- mixed iterative structural implementation。

它只是把状态空间改写到 strain space，并没有消除状态演化/活动面，故不解决当前核心问题。

## 5.3 He–Wu–Liew–Wu 2006 — 排除为简洁主线

属于 2D total-strain family，但使用 equivalent principal strains、current strength、current fracture energy、rotating crack 和 fracture-energy regularization。虽然理论完整，仍带有裂化/软化机制和 characteristic-length/FE regularization 身份，不适合当前无空间材料点解析板理论。

## 5.4 Chinnasamy et al. 2019 — 作为“统一但隐式”备选

其 non-dissipative implicit constitutive theory 能统一拟合 compression-compression、compression-tension、tension-tension，多组实验平均拟合表现良好，并故意不采用传统 discrete CC/TC/TT 状态机作为结构算法。

但其身份就是 **implicit constitutive relation**。除非后续证明 plane-stress 下可有限代数消元为低阶 direct map，否则与 Bažant–Tsubaki 一样会把状态判断问题换成局部隐式求解。

---

# 6. 当前 recommended next gate

不是回 Nguyen `CC/TC/TT`，也不是开始拼接 Cedolin/Bažant。

下一步只做两个数学问题：

1. 完整恢复 **Gerstle 1981** 的 biaxial linearly-varying tangent bulk/shear modulus 公式，检查在单调加载下能否解析积分成 current total law，并检查峰后范围；
2. 同时恢复 **Chinnasamy et al. 2019** 的 implicit algebraic equation，计算 plane-stress 消元后的代数次数，判断它是否可一次有限全根求解，而无需 material-point history/iteration。

只有候选首先通过

\[
\boxed{\text{NO DISCRETE STATE MACHINE} + \text{FINITE LOCAL ALGEBRA}}
\]

才继续检查 Airy 复合可积性。

本轮不得因 Cedolin–Mulas “显式”而忽略其峰后缺失，也不得因 Bažant–Tsubaki “total strain”而误称其实际广域模型为 direct explicit。