# NZ-SCCM：其余三份上传资料的理论/试验补充审阅

**日期：2026-08-11**  
**身份：SOURCE REVIEW / DIAGNOSTIC EVIDENCE**  
**边界：本文件只补充来源证据，不修改当前 R10、N48、Nguyen 连续半波、D15 或任何板件参数。**

---

## 1. Swartz, Rosebraugh & Rogacki (1974) — *A Method for Determining the Buckling Strength of Concrete Panels*

### 1.1 来源身份

这是 24 块板试验计划的**试验装置与屈曲判定方法原始论文**，重点不是预测公式，而是：

- 四边简支如何在试验中近似实现；
- 荷载如何分配；
- 位移与应变如何布置；
- 初始屈曲荷载如何从试验数据识别。

### 1.2 对当前项目最有用的试验补充

#### A. 四边“简支”是有限刚度试验装置的近似，不是数学上无限刚度的理想边界

侧边用离散夹具和圆杆支承；上下边夹具通过滚轮在槽形承压板上运动；离散夹具的目的之一是允许板在屈曲时翘曲。加载头运动使侧向立柱不能与上边支承形成完全刚性的闭合框架。

**意义**：当前理论的四边简支是理想边界。试验中支架存在有限刚度，且作者明确认为“侧支承刚度相对于板弯曲刚度”会影响实际鼓曲形态。因此支承系统是三种厚度组之间不可忽视的实验系统变量。

#### B. 厚度改变时，实际鼓曲区数并不固定

作者原先依据理想弹性 a/b=2 板预期两个近似方形鼓曲区，但实际：

- 3/4 in 板出现两个鼓曲区；
- 1 in 板既有两个鼓曲区，也有一个近似方形主鼓曲区；
- 1-1/4 in 板也出现单主鼓曲区。

作者认为这种差异与**侧支承相对板弯曲刚度**有关。

**项目解释**：不能再把 Case17–24=固定双半波、Case1–16=固定单半波当成原始试验事实。`ONE_CONTINUOUS_COMPLETE_HALFWAVE` 仍可作为代表半波计算原则，但完整试件中重复半波数量和鼓曲区位置应作为试验诊断量，而不是模型内固定分类输入。

#### C. 试验在高荷载时出现膜应变重新分配

对 1-1/4 in 板，作者指出初期跨板宽膜应变分布较均匀，高荷载时一些位置明显偏离，并将其部分归因于**板超过屈曲荷载后的应变重新分配**。

**项目意义**：这直接支持当前 Case9–16 系统低估应优先检查“屈曲后的膜内重分布/后屈曲承载储备”，而不是立即回调 R10 抗压强度。

#### D. 不可避免的加载偏心存在，但总体较小

两表面应变曲线显示加载偏心总体不大；边角应变也显示夹边诱导弯矩较小。但“较小”不等于数学上严格为零。

**项目意义**：Swartz 24 板仍适合作为近同心轴压主验证组；但若以后追求极小百分比误差，实际偏心与支架柔度会成为实验误差下限，不能用材料参数吸收。

#### E. Southwell 法对非线性混凝土不可靠

作者明确指出 Southwell 法严格适用于线弹性材料；混凝土在较高应力下越来越非线性，因此厚板适用性更差，Southwell 结果常明显高于实际 collapse load。作者最终推荐使用**屈曲区中心附近两表面应变的分叉/反向变化**判断初始屈曲。

这与后续 24板原始 Table 2 一致：

- Case1、4 的 Pcr 来自 Southwell；
- Case5、6 来自 deflection profiles；
- 其余主要来自表面应变判据。

因此所有 `Pf/Pcr`、`fcr/fc` 机制统计必须保留 `Pcr_method` 字段。

### 1.3 可用于理论的内容

本论文不提供应直接替代现有 current-map 的新材料本构；其价值主要在**边界条件、模态和试验识别误差**。

推荐未来只做以下诊断，而不改正式理论：

1. 理想四边简支 vs 有限侧支承刚度的敏感性边界研究；
2. 单主鼓曲区与两个重复鼓曲区对完整试件观察量的映射；
3. Pcr 测定方法不确定性与理论误差的分离。

---

## 2. Mario M. Attard (1994) — *Buckling of Reinforced Concrete Walls*

### 2.1 来源身份

这是四边简支钢筋混凝土墙在均匀轴压下的**正交异性切线模量解析稳定理论**，并非 Swartz 试验报告。

### 2.2 核心理论补充

#### A. 正交异性切线板平衡方程

Attard 写出

\[
D_{xt}w_{,xxxx}+2D_{xyt}w_{,xxyy}+D_{yt}w_{,yyyy}
=-N_xw_{,xx}.
\]

其中弯曲切线刚度由加载方向与非加载方向切线模量控制。

**对 NZ-SCCM 的意义**：这提供了一个非常干净的、独立于当前实现的“切线稳定骨架”基准，可以用于检查当前 current-map 在某一均匀应力状态下导出的方向切线是否给出合理的屈曲趋势。

#### B. Attard 的方向切线假设

Attard 取

\[
E_{xt}=E_t,
\qquad
E_{yt}\approx0.4E_c.
\]

其中加载方向使用混凝土当前切线模量；非加载方向 0.4Ec 是基于横向弯曲可能开裂、且横向弯矩小于屈服弯矩的近似。

**治理边界**：`Eyt=0.4Ec` 是 Attard 的特定近似，不是当前 R10/Nguyen 多轴 current-map 的来源，不能直接移植为正式材料参数。但它非常适合作为**方向切线下界/敏感性诊断**。

#### C. 切线模量接近峰值迅速降为零

Attard 给出一套 20–120 MPa 普通/高强混凝土单轴曲线及其导数，强调：

- 割线模量在比例极限前接近弹性模量；
- 到峰值附近仍约为 0.6Ec；
- **切线模量下降远快于割线模量，并在峰值应力处降到零**。

**对当前24板误差的意义**：本次原始数据统计显示 `fcr/fcyl` 与当前 Pu 有符号误差的相关最强。Attard 的理论从另一条独立来源说明：越靠近峰值，稳定问题对“当前切线”极端敏感，而不是只对峰值强度敏感。

#### D. 正弦模态与半波数 m

Attard 采用

\[
w=C_1\sin\frac{m\pi x}{a}\sin\frac{\pi y}{b},
\]

并由正交异性刚度得到 Ncr、buckling coefficient k 及其最小值。

**项目意义**：Attard 可以作为 `m/半波数` 的独立解析检查工具，但不能用其最优 m 直接取代当前项目已经锁定的“一个连续完整代表半波”计算域。合理做法是：完整物理板允许重复代表半波；每个代表半波仍采用同一连续基本单元。

#### E. 初始缺陷与弯矩放大

Attard 后半部分用与临界模态相似的初始缺陷形状，通过 magnification factor 估算两个方向放大弯矩。

这说明：**初始缺陷、稳定荷载和屈后弯矩放大应当是同一条稳定链上的量，而不是相互独立的经验修正。** 这一思想与当前 Nguyen 二阶运动学保留 q0 的方向一致。

### 2.3 推荐用途

Attard 应作为：

- `TANGENT_STABILITY_INDEPENDENT_BENCHMARK`；
- `DIRECTIONAL_TANGENT_SENSITIVITY_DIAGNOSTIC`；
- `MODE_NUMBER / SLENDERNESS TREND CHECK`。

暂不授权：

- 用 Attard 单轴材料替换 R10；
- 把 Eyt=0.4Ec 写入 current-map；
- 用 Attard Ncr 作为当前 Pu 的校准目标。

---

## 3. Doh, Fragomeni & Kim — *Brief Review of Studies on Concrete Wall Panels in One and Two Way Action*

### 3.1 来源身份

这是**二级综述**，价值在于整理试验/理论范围，而不是优先于 Swartz、Attard 等原始来源。

### 3.2 有用内容

#### A. 明确区分 one-way 与 two-way wall action

综述将侧边支承、轴压下发生二维板屈曲的墙板单独归为 two-way action；指出该领域研究远少于 one-way wall，现行规范/经验式覆盖有限。

#### B. 汇总不同试验组的关键边界差异

特别有用的是不同研究的：

- slenderness/thinness；
- aspect ratio；
- concrete strength；
- eccentricity；
- reinforcement；
- support condition。

这为后续建立“外部验证矩阵”非常有用。

例如综述明确提醒：

- Swartz：高 slenderness、近同心加载；
- Saheb & Desayi：存在 t/6 偏心；
- Attard：理论分析；
- Fragomeni/Maheswaran-Sanjayan：更高强混凝土、不同试验控制条件。

因此不同数据库不能混在一起用一个误差平均值评价模型。

#### C. Saheb & Desayi 的 ultimate-strength 规律

综述转述其结论：two-way wall 的极限强度随 thinness/slenderness 增大而非线性降低，竖向钢筋增加可提高极限强度，而横向钢筋影响较小。

这与 Swartz“钢筋对初始 Pcr 小、对总 capacity 重要”形成互补：**初始稳定与最终 Pu 的钢筋敏感性可以不同。**

#### D. Attard 对 Swartz 与 Saheb 的不同适配性

综述指出 Attard 的切线模量方法与 Swartz 的近同心试验较吻合，但与 Saheb & Desayi 的偏心试验不吻合，原因与加载偏心条件不同。

**项目意义**：这是一个很重要的治理提醒——未来扩展验证时，必须先按 `eccentricity / boundary / load control` 分类，不能看到同样是“RC wall”就直接混算。

#### E. 试验加载控制方式也是变量

综述提到 Maheswaran & Sanjayan 使用一系列千斤顶维持近 constant loading，与常规试验机的 displacement-controlled 加载不同，且不同经验公式对这些试验可能出现大幅高估或低估。

**项目意义**：Pu 验证数据库未来应增加 `load_control` 字段。

### 3.3 推荐用途

该综述适合作为：

- `LITERATURE_SCOPE_MAP`；
- `FUTURE_VALIDATION_MATRIX_GUIDE`；
- `BOUNDARY/ECCENTRICITY/LOAD_CONTROL CLASSIFICATION`。

不适合作为：

- 当前材料公式的一级来源；
- 经验系数校准来源；
- 替代 Swartz/Attard 原文的精确公式证据。

---

## 4. 三份资料共同形成的新证据链

三份补充资料放在一起，当前最值得锁定的不是“再改材料”，而是以下诊断结构：

\[
\boxed{
\text{current material tangent state}
\;\times\;
\text{ideal/real support stiffness}
\;\times\;
\text{post-buckling membrane redistribution}
\;\times\;
\text{reinforcement post-buckling contribution}
}
\]

具体而言：

1. **Swartz 原始数据**：`fcr/fcyl` 越高，当前 Pu 越倾向低估；
2. **Attard**：材料靠近峰值时 tangent modulus 快速降到零，稳定对切线极端敏感；
3. **A Method**：高荷载发生膜应变重新分配，且侧支承相对刚度改变一/双鼓曲区；
4. **Swartz Buckling Tests**：钢筋对初始 Pcr 小，但对 total capacity 和 post-buckling ductility 重要；
5. **综述**：偏心、边界、加载控制不同会显著改变外部验证结果。

因此后续优先级建议为：

```text
P1 = tangent-state / fcr-fc regime audit
P2 = post-buckling membrane redistribution audit
P3 = support-stiffness / observed-mode sensitivity audit
P4 = reinforcement-postbuckling interaction audit
P5 = external validation matrix segmented by eccentricity/boundary/load-control
```

上述均为机制诊断，不授权试验反标。
