# NZ-SCCM — NC-M2 单轴拉伸骨架审计：有限耗能门禁

时间：2026-08-20 14:41 +08:00

状态：`NC_M2_REMAINS_ACTIVE_MATERIAL_CANDIDATE / TENSION_BACKBONE_NOT_ACCEPTED_FOR_PRODUCTION_LOCK`

## 1. GitHub 启动核验

本轮启动时实际查询 `main`，确认 NC-M2 已经真实同步。启动 HEAD 为：

`0dc3a634807d3c1eaa15b833fdef8bcb86977538`

其父链包含：

- `8103eefa581e19893773cda65936a6b1cc41bfff`：NC-M2 单公式九宫格候选；
- `adc92b96785da15d06cb17b009c0e7e6d84aed74`：NC-M2 曲线审计；
- `0dc3a634807d3c1eaa15b833fdef8bcb86977538`：semantic tree 更新。

因此上一聊天曾声称但未取得工具回执的三条 SHA，现已由 GitHub 实际查询确认。

NC-M1 继续保持：`REJECTED_DIAGNOSTIC_CANDIDATE`。

NC-M2 继续保持：`ACTIVE_MATERIAL_CANDIDATE / NOT_YET_PRODUCTION_LOCK`。

## 2. 为什么本轮先审查 T(t)，而不是 CC eta

当前 NC-M2：

\[
T(t)=\frac{t}{1-t+t^2},\qquad t=\varepsilon_t/\varepsilon_{cr}\ge0.
\]

它同时进入 TT 两个主方向、TC/CT 的拉向分量，并通过虚功密度进入结构积分。因此若一维拉伸骨架本身存在物理/能量问题，该问题会直接传播到三个实体象限。

相比之下，CC 的 `eta` 当前主要问题是双压增强量级是否偏保守；其基本边界条件和对称性尚未发现同等级的结构性缺陷。因此先审查 T(t)。

## 3. 当前 T(t) 的局部性质

\[
T(0)=0,\quad T'(0)=1,\quad T(1)=1,\quad T'(1)=0.
\]

导数为

\[
T'(t)=\frac{1-t^2}{(1-t+t^2)^2}.
\]

所以：

- `0<t<1` 单调上升；
- `t=1` 唯一峰值；
- `t>1` 单调下降。

就“单式、无阈值、光滑峰值”而言，这一结构是合格的。

## 4. 峰后曲线的两个相反问题

### 4.1 中等应变区下降偏快

代表值：

| t | NC-M2 T(t) |
|---:|---:|
| 1.0 | 1.000000 |
| 1.5 | 0.857143 |
| 2.0 | 0.666667 |
| 3.0 | 0.428571 |
| 5.0 | 0.238095 |
| 10.0 | 0.109890 |

若仅以 Nguyen/Foster 的轻配筋 tension-stiffening 参考（`a1=10, a2=0.3`）作诊断标尺，则其归一化参考可写成：

\[
T_F(t)=t,\quad 0\le t\le1,
\]

\[
T_F(t)=1-\frac{1-0.3}{10-1}(t-1),\quad 1<t<10,
\]

\[
T_F(t)=0.3,\quad t\ge10.
\]

该参考在 `t=1.5,2,3,5,10` 分别约为 `0.9611, 0.9222, 0.8444, 0.6889, 0.3`。因此 NC-M2 在 `1<t<5` 的确明显更软。

但该 Foster 曲线的物理来源是钢筋—混凝土粘结引起的 tension stiffening，不能直接视为素混凝土裂缝软化真值。因此这里只能得出“NC-M2 相对该 RC 参考下降更快”，不能据此要求 M2 拟合 Foster。

### 4.2 远尾却衰减过慢，导致无限耗能

更关键的是：

\[
T(t)=\frac{t}{1-t+t^2}\sim\frac1t\qquad (t\to\infty).
\]

于是

\[
\int_1^{\infty}T(t)\,dt=\infty.
\]

如果把该式作为局部应力—应变 current law，并用 `sigma d epsilon` 理解拉伸耗能，则它具有对数发散的无限拉伸耗能。

因此当前问题不能简单概括为“峰后太软”：

- 中等应变区：相对 Foster tension-stiffening 参考偏软；
- 远尾：`1/t` 尾巴反而过长，积分耗能发散。

这构成 NC-M2 拉伸骨架不能直接 production lock 的明确数学/物理门禁。

## 5. 文献物理锚点

普通混凝土拉伸断裂文献（Cornelissen–Hordijk–Reinhardt 系列）将峰后行为描述为应力—变形/裂缝张开软化关系，并用有限 fracture energy 表征耗能。Hordijk 型关系通常以应力—裂缝张开量表示，而不是直接以局部应变 `epsilon/epsilon_cr` 表示。

因此，文献给出的直接约束是：

\[
\boxed{\text{峰后拉伸耗能应当有限}}
\]

但若要把 Hordijk 曲线逐点投影到当前 `t=epsilon/epsilon_cr` 横坐标，必须额外指定 crack-band / localization length。当前材料审查尚未引入这个长度，因此本轮不伪造 Hordijk 与 T(t) 的同横坐标重合比较。

## 6. 非候选的单式有限耗能诊断族

为检验“单公式 + 光滑峰值 + 有限耗能”是否可以同时实现，构造以下数学诊断族：

\[
T_{FE,p}(t)
=\frac{t+p t^2}
{1+(p-\tfrac12)t^2+\tfrac12 t^4},\qquad p>0.
\]

它满足：

\[
T_{FE,p}(0)=0,\quad T'_{FE,p}(0)=1,
\]

\[
T_{FE,p}(1)=1,\quad T'_{FE,p}(1)=0,
\]

且

\[
T_{FE,p}(t)\sim\frac{2p}{t^2},\qquad t\to\infty,
\]

因此：

\[
\int_1^{\infty}T_{FE,p}(t)dt<\infty.
\]

其导数分子可因式分解为：

\[
-\frac{t-1}{2}
\left[
2pt^4+2pt^3+2pt^2+4pt+3t^3+3t^2+2t+2
\right],
\]

所以对 `p>0`，`t=1` 是唯一光滑峰值。

特别强调：这只是“存在性/形状”诊断族，不是新的 NC-M3，也没有选定参数。`p=3` 仅用于绘图比较，不具有材料标定身份，更没有使用 Case21 Pu 反标。

## 7. p=3 的诊断值

| t | NC-M2 | T_FE,3 |
|---:|---:|---:|
| 0.5 | 0.666667 | 0.754717 |
| 1.0 | 1.000000 | 1.000000 |
| 1.5 | 0.857143 | 0.901023 |
| 2.0 | 0.666667 | 0.736842 |
| 3.0 | 0.428571 | 0.468750 |
| 5.0 | 0.238095 | 0.212766 |
| 10.0 | 0.109890 | 0.059041 |

面积诊断：

- `0<=t<=3`：M2 ≈ `1.98962`，FE,p=3 ≈ `2.13507`；
- `0<=t<=5`：M2 ≈ `2.62169`，FE,p=3 ≈ `2.77229`；
- `0<=t<=10`：M2 ≈ `3.41214`，FE,p=3 ≈ `3.33652`；
- FE,p=3 的 `0<=t<infinity` 总面积 ≈ `3.93654`，有限；
- M2 的总面积发散。

这说明不需要重新引入分段或阈值，就能消除 M2 的 `1/t` 无限耗能尾巴，同时略提高峰后初段保留能力。

## 8. 本轮判定

1. `C(c)` 暂不动。
2. `beta(t)` 暂不动。
3. `eta(c1,c2)` 暂不动，留到拉伸骨架审查之后。
4. 当前 `T(t)=t/(1-t+t^2)` 保留在 NC-M2 历史定义中，但标记为：

`TENSION_BACKBONE_UNDER_REVIEW / FAILS_FINITE_ENERGY_GATE`

5. NC-M2 整体身份仍为：

`ACTIVE_MATERIAL_CANDIDATE / NOT_YET_PRODUCTION_LOCK`

6. 本轮不建立 NC-M3，不选定 `p`，不进行 Case21 承载力计算。

下一材料动作应先确定普通混凝土拉伸软化采用哪一种物理尺度：继续使用无长度的 total-strain current law，还是显式引入 fracture-energy / crack-band 尺度。只有该点明确后，才应选定新的单式 T(t) 并按项目规定绘制完整五图，再进入 CC eta 审查。
