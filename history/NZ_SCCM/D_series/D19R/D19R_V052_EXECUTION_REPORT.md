# NZ-SCCM D19R v0.5.2：冻结材料可积性与状态前沿手算审计

## 1. 本轮任务边界

本轮从 v0.5.1 回退基线直接复制建立审计分支，未修改 `src/` 与 `tests/` 中任何理论代码。逐文件 SHA-256 比较结果为 **9/9 完全一致**。

本轮没有：

- 新增普通混凝土或 UHPC 材料机制；
- 改写 U、TC、TT、CC、TCX 或 CCX 状态关系；
- 恢复 Source-U、Darwin–Pecknold、Chebyshev 板级代理或伪弧长；
- 运行 Swartz 24 板承载力计算；
- 调整任何材料参数。

实际执行内容只有两项：

1. 对冻结的 NSC/UHPC 各材料分支逐项检查，判断其能否进入 D19 当前的有限 Beta 状态矩基底；
2. 选取 D19 原测试中的一个明确状态前沿，给出可人工复核的根、前沿导数、内层不完全 Beta 积分及完整状态矩审计。

## 2. 回归测试

```text
D19 tests: PASS
178 topology intervals
45 analytic root derivatives
80 Liu tangent checks
1 full front-moment derivative

D19R tests: PASS
12 material tangents
2 full matrix Jacobians
6 UHPC path states
```

这些结果只证明原 D19/D19R 代码未被破坏，不等于完整零求积解析矩已经闭合。

## 3. D19 当前真正实现到哪一步

固定厚度坐标 `z` 后，主应变阈值前沿写为：

\[
F(u,v)=P_0(u,v)+\sqrt{uv}\,P_1(u,v)=0,
\]

平方后为关于 `v` 的三次代数方程。D19 能够精确求出：

- `v=0`、`v=1` 边界事件；
- 三次方程降阶事件；
- 判别式事件；
- 物理根与平方伪根相交事件；
- 各拓扑区间内的物理前沿根；
- 前沿速度 `dv/dq=-F_q/F_v`。

对固定 `u`，`v` 方向的状态矩可写成不完全 Beta 函数，因此**内层积分已经解析闭合**。

但是，源码 `state_front_moment_audit()` 随后仍调用一维自适应积分，对 `u` 方向积分：

\[
M_{pqrs}^{(S)}
=\int_{u_a}^{u_b}w_u(u)
\left[
B_{v_+(u)}(a_y,b_y)-B_{v_-(u)}(a_y,b_y)
\right]du.
\]

因此当前准确身份是：

\[
\boxed{\text{精确拓扑分区 + 解析内层 Beta 积分 + 一维外层数值积分}}
\]

不是完全零数值积分的闭式状态矩。

此外，当前 `branch_event_system.py` 的状态矩模块针对**固定 z**工作。完整厚度状态前沿的统一积分并未在该模块中实现，所以整板矩阵还存在厚度闭合缺口。

## 4. 冻结材料逐项可积性结论

完整清单见 `results/D19R_FROZEN_MATERIAL_INTEGRABILITY_AUDIT.csv`。

### 4.1 可以进入当前有限矩基底的范围

仅有少数子区域可以严格化为有限几何/状态矩：

1. NSC 与 UHPC 的双主方向共同线弹性拉伸区：
   \[
   \sigma_i=E\varepsilon_i.
   \]
   因两个特征值使用同一个线性函数，主方向投影中的根式相消，回到：
   \[
   \boldsymbol\sigma=E\boldsymbol\varepsilon.
   \]

2. NSC 两个主方向同时位于同一条仿射拉伸软化段时：
   \[
   \sigma_i=a\varepsilon_i+b,
   \]
   可化为：
   \[
   \boldsymbol\sigma=a\boldsymbol\varepsilon+b\mathbf I.
   \]
   但必须进一步划分两个主应变是否确实位于同一子段。

### 4.2 不能进入当前有限矩基底的冻结分支

NSC 主要障碍：

- Saenz 型压缩有理式；
- TC 折减系数与压缩曲线的乘积；
- CC 中主压应变比控制的双压增强；
- 不同主方向位于不同材料子段时保留的谱投影根式。

UHPC 主要障碍：

- Hu 压缩有理式；
- 纤维拉伸峰后的广义指数函数；
- Liu 分支中的 `x^1.8`、有理分母与拉向软化平方根；
- 拉伸损伤与指数曲线的组合；
- W-W 面中的应力不变量、Lode 角和嵌套根式。

这些都不是 D19 当前有限 Beta 矩表中的有限线性组合。

### 4.3 W-W 状态边界的额外问题

D19 当前前沿表示的是：

\[
\varepsilon_i=\lambda,
\]

即固定主应变阈值。

W-W 激活边界则是：

\[
F_{WW}(\sigma_1,\sigma_2,0)=1,
\]

并且 `sigma_i` 已经是非线性材料函数。它不是当前固定主应变阈值前沿，现有 D19 三次前沿系统不能直接表示该边界。

所以 UHPC CC/CCX 若启用 W-W 活动截断，当前不仅缺少积分闭式，还缺少对应的状态前沿方程。

## 5. 手算审计样例

### 5.1 输入

采用 D19 原测试中的几何和路径点：

\[
b=\ell=1220\ \mathrm{mm},\quad t=19.3\ \mathrm{mm},\quad m=1,
\]

\[
A_0=6.1\ \mathrm{mm},\quad
A=0.020736941436b=25.29906855192\ \mathrm{mm},
\]

\[
\delta=1.155541949276\times0.00209
=0.00241508267398684,
\]

\[
S=A_0A+\frac12A^2
=474.345752964086\ \mathrm{mm^2},
\]

\[
k_x=k_y=\frac{\pi}{1220}
=0.00257507594556540\ \mathrm{mm^{-1}},
\]

选择下表面：

\[
z=-t/2=-9.65\ \mathrm{mm},
\]

并检查主压应变阈值：

\[
\lambda=-0.00209.
\]

### 5.2 精确拓扑事件

程序由事件多项式直接求得：

| `u` | 事件 |
|---:|---|
| 0 | DISCRIMINANT + LEADING + U0 |
| 0.0403240169270 | V1 |
| 0.135073430436 | DISCRIMINANT + PHYSICAL_SIGN |
| 0.358923433277 | V0 |
| 1 | U1 |

在最后一个区间 `u in (0.358923433277,1)` 内物理根数恒为 1。

### 5.3 在 `u=0.6` 处手算前沿根

物理根为：

\[
v_f=0.0785103095331149.
\]

此时：

\[
P_0=2.08057970305603\times10^{-6},
\]

\[
P_1=-9.58617576104612\times10^{-6},
\]

\[
\sqrt{uv_f}=0.217039594820551.
\]

代回未平方物理方程：

\[
F=P_0+\sqrt{uv_f}P_1
\]

\[
=2.08057970305603\times10^{-6}
-2.08057970305604\times10^{-6}
\approx-2.12\times10^{-21}.
\]

主应变为：

\[
\varepsilon_1=0.000810047047968861,
\]

\[
\varepsilon_2=-0.002090000000000001\approx\lambda.
\]

因此该根确实是物理主压应变阈值前沿，而不是平方伪根。

### 5.4 前沿导数手算

由源码中的解析偏导：

\[
F_v=-1.38777879406427\times10^{-5},
\]

\[
F_\delta=-0.001837419501395879.
\]

所以：

\[
\frac{dv_f}{d\delta}
=-\frac{F_\delta}{F_v}
=-132.400027241718.
\]

中心差分独立校核：

\[
\frac{v_f(\delta+10^{-8})-v_f(\delta-10^{-8})}{2\times10^{-8}}
=-132.400027252205.
\]

两者相对差约：

\[
7.92\times10^{-11}.
\]

### 5.5 内层 Beta 状态矩手算

在 `u=0.6` 处，`F<=0` 的区域为：

\[
v\in[v_f,1].
\]

对最低阶状态矩：

\[
I_v=\int_{v_f}^{1}\frac{dv}{\sqrt{v(1-v)}}.
\]

利用：

\[
\int\frac{dv}{\sqrt{v(1-v)}}=2\arcsin\sqrt v,
\]

得到：

\[
I_v=\pi-2\arcsin\sqrt{v_f}
=2.573594189420771.
\]

其对 `delta` 的形状导数为：

\[
\frac{dI_v}{d\delta}
=-\frac{1}{\sqrt{v_f(1-v_f)}}\frac{dv_f}{d\delta}
=492.242932415506.
\]

程序的前沿形状导数结果完全一致。

### 5.6 完整状态矩仍需一维积分

完整最低阶状态矩为：

\[
M_{0000}
=\int_0^1\frac{I_v(u)}{\sqrt{u(1-u)}}du.
\]

令：

\[
u=\sin^2\theta,
\]

则：

\[
M_{0000}=2\int_0^{\pi/2}I_v(\sin^2\theta)d\theta.
\]

D19 当前一维自适应积分结果：

\[
M_{0000}=8.084905072841787.
\]

占全域 Beta 测度 `pi^2` 的比例：

\[
\frac{M_{0000}}{\pi^2}=0.819172151616271.
\]

用可人工复算的 32 等分复合 Simpson 公式：

\[
M_{0000}^{S32}=8.08634061078544,
\]

相对差：

\[
1.77558\times10^{-4}=0.017756\%.
\]

完整 33 个 Simpson 节点和权重见：
`results/D19_FRONT_SIMPSON_N32_TABLE.csv`。

这个结果直接证明：**D19 当前已经消除了二维网格和内层 v 积分，但没有消除外层一维积分。**

## 6. 本轮裁决

```text
FROZEN_SOURCE_IDENTITY                  = PASS_9_OF_9
NEW_MATERIAL_MECHANISM                  = NONE
FIXED_M1                                = PASS
D19_EXACT_TOPOLOGY_EVENTS               = PASS
D19_FRONT_ROOT_DERIVATIVE_HANDCHECK      = PASS
D19_INNER_INCOMPLETE_BETA_HANDCHECK      = PASS

D19_FULL_STATE_MOMENT                    = SEMI_ANALYTIC_OUTER_1D_QUADRATURE
D19_THICKNESS_COMPLETION                 = NOT_IMPLEMENTED_IN_CURRENT_MODULE
NSC_FULL_FROZEN_MATERIAL_FINITE_MOMENT   = NOT_CLOSED
UHPC_FULL_FROZEN_MATERIAL_FINITE_MOMENT  = NOT_CLOSED
WW_ACTIVATION_FRONT                      = NOT REPRESENTED

CHEBYSHEV_PROXY                          = PROHIBITED
PANEL_GAUSS_PRODUCTION                   = PROHIBITED
SWARTZ24                                 = PAUSED
```

## 7. 结论

此前提出的“直接把 D19 状态前沿接入完整 NSC/UHPC 残量和 Jacobian，并同时实现完全零数值积分”，在冻结现有材料公式的条件下，**不能作为单纯的代码接线任务完成**。

原因不是程序能力不足，而是当前数学对象存在三层未闭合：

1. 状态区域矩仍有一维外层积分；
2. 完整厚度状态积分未在当前 D19 模块中闭合；
3. 大多数冻结材料分支不是有限 Beta 矩的线性组合，W-W 甚至缺少相应前沿。

本轮因此在完整矩阵组装前停止，没有用多项式、Chebyshev、Gauss 材料点或临时材料假定掩盖缺口。
