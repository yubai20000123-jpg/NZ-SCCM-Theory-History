# NZ-SCCM / BH050 C1-PBL 力流机理、理论修正与当前诊断状态备份 R01

- 日期：2026-09-03 11:32 +08:00
- 仓库：`yubai20000123-jpg/NZ-SCCM-Theory-History`
- 分支：`diagnostic/bh032-bh050-mode-projection-20260827`
- 目标目录：`semantic_v2/40_execution/steel_shell/`
- 本文件性质：**diagnostic / theory-development backup，非 production 冻结稿**
- 写入前 branch head：`3892188275ebfdfd7286d7d9dabef9b9951b189f`
- production/main：**不修改**

---

## 0. 本次备份要解决的历史断点

本节点备份 2026-09-03 当前对 BH050 的最新认识：

1. 不再把 FE 中的 UHPC/steel/web “受力占比”作为局部机理正确性的主判据；整体合力平衡仍然必须保留，但百分比分担会把局部空间信息平均掉。
2. 用户人工检查 BH050 FE 后发现：UHPC 与钢壳的应力场在峰值附近具有明显不同的空间尺度与力流机制。
3. 因此此前提出的 **PBL full-curvature-following / C2 强约束**（`w, w_n, w_nn` 同时跟随 UHPC）被降级为待否证假设；当前优先路线改为 **C1-PBL：位移 + 转角相容，曲率由边界力/弯矩平衡决定**。
4. 每个 steel bay 保留独立 local bubble amplitude `A_b`；相邻 bay 不再要求同步鼓波或共享相位。
5. 原 R14 的 global Marguerre–Airy demand、UHPC operator、web operator、steel material/yield architecture、四个 global N-M balance 不重建；只改 steel-face current operator 的运动学/局部凝聚层。

---

## 1. 用户最新 FE 人工观察：BH050 的真实应力场长什么样

用户在整体鼓波最大横截面进行人工检查，发现：

### 1.1 UHPC

- 整体凹面节点纵向应力大约：
  `-75 ~ -111 MPa`；
- 整体凸面大约：
  `-20 ~ -75 MPa`；
- UHPC 厚度方向呈**连续、渐进的应力梯度**，总体表现为低波数整体弯曲 + 轴压背景。

### 1.2 钢壳

- 钢壳横向局部鼓波**不是连续同步波列**：某一格室在同一纵向坐标处明显鼓起时，相邻格室可能几乎不鼓。
- 除局部子鼓波的波峰区域可出现拉应力外，大部分钢壳区域均维持强压应力：
  `-200 ~ -300 MPa` 左右。
- 这一强压应力在整体凹面与整体凸面钢壳上都存在；并未呈现简单的 UHPC 表面应力乘 `E_s/E_c` 的对应关系。

### 1.3 当前必须保留的解释边界

这些 FE 观察是**机理诊断证据**，不能直接拿来反标理论参数，也不能把局部 shell section-point 的 SPOS/SNEG 应力直接当作 steel membrane resultant。

---

## 2. 当前物理解释：为什么钢壳可以长期保持 -200 ~ -300 MPa 强膜压

### 2.1 并行纵向力流，而非“UHPC 先承载、再把力给钢壳”

把结构看成并行纵向受力通道：

`上钢壳 || UHPC 核心 || 下钢壳`。

钢壳和 UHPC 都从加载端形成直接轴向力路径；PBL/界面不断通过轴向剪力、法向力和局部弯矩调节各通道之间的相对位移和力流。

钢壳局部膜平衡可概念写为：

\[
\frac{\partial N_z^s}{\partial z}
+\frac{\partial N_{xz}^s}{\partial x}
+t_z^{int}=0,
\]

其中 `t_z^{int}` 为 UHPC/PBL 对钢壳的轴向界面传力。

### 2.2 为什么 steel longitudinal stress 不必等于 UHPC longitudinal stress

界面相容要求的是位移连续/连接相容；界面平衡要求的是 traction continuity。若界面法向为 `y`，连续的是 `sigma_yy, tau_xy, tau_zy` 等牵引分量，不要求平行界面的 `sigma_zz` 在钢-UHPC 两侧相等。

因此：

`steel sigma_zz ≈ -250 MPa` 与相邻 `UHPC sigma_zz ≈ -60 MPa`

并不违反界面平衡。

同时 BH050 已进入：UHPC 非线性压缩 + steel 局部大挠度 + steel 二维 Mises 应力状态，所以即便某处轴向应变近似相容，也不存在简单 `sigma_s/sigma_c = E_s/E_c` 的普遍关系。

### 2.3 钢壳强压背景 + 局部弯曲为何可同时产生波峰拉应力

钢壳 shell 表面应力应拆成：

\[
\sigma_z^{SPOS}=\sigma_z^m+\sigma_z^b,
\qquad
\sigma_z^{SNEG}=\sigma_z^m-\sigma_z^b.
\]

局部波峰处 `|sigma_z^b|` 很大时，一侧表面可以转为拉应力；但中面膜应力 `sigma_z^m` 仍可保持约 `-200 ~ -300 MPa`。

因此：

**局部波峰出现拉应力 != 该格室整体转为轴向拉力。**

后续 FE 审计应优先比较 shell membrane-like quantity，例如同一 element 的 SPOS/SNEG 平均，而不是只看最大表面值。

---

## 3. 为什么相邻格室会“一个鼓、一个不鼓”

当前解释为 **symmetry breaking / localization / bay competition**：

1. 某 bay 因初始缺陷、膜力、局部边界状态等先进入后屈曲；
2. 其 local amplitude `A_b` 增长，局部切线下降；
3. 该 bay 对公共 PBL 的轴力、剪力、弯矩边界反力改变；
4. 相邻 bay 的边界状态随之改变，可能被稳定化而不是同步屈曲；
5. 因此允许：

\[
A_1 \gg A_2,\qquad A_3\approx 0,\qquad A_4\neq A_1.
\]

这说明整个钢壳 local field 不应被预设为单一幅值、统一相位的规则周期波。

---

## 4. 理论修正：从 C2 full-curvature following 降到 C1-PBL

### 4.1 撤回复审的旧强约束

旧 proposal：在每条 PBL 上强制

\[
w_s=w_c,\qquad
w_{s,n}=w_{c,n},\qquad
w_{s,nn}=w_{c,nn}.
\]

第三个条件 `w_nn` 被认为过强：曲率不是一般连接的基本 kinematic continuity variable；左右 bay 可以保持位移与转角连续，而具有不同曲率，通过 PBL 边界弯矩实现平衡。

### 4.2 当前优先最小模型：C1-PBL

只保留：

\[
\boxed{w_s(x_i,z)=W_c(x_i,z)}
\]

\[
\boxed{w_{s,n}(x_i,z)=W_{c,n}(x_i,z)}
\]

不再规定：

\[
\boxed{w_{s,nn}=W_{c,nn}}.
\]

即 PBL 给 steel bay 提供低频位移/转角骨架；local curvature 由 steel bay 自身能量和平衡决定。

---

## 5. C1-PBL bay 形函数

设 bay `b` 位于 `x_i <= x <= x_{i+1}`，宽度：

\[
b_i=x_{i+1}-x_i,
\qquad r=(x-x_i)/b_i.
\]

低阶骨架采用 cubic Hermite：

\[
H_1=1-3r^2+2r^3,
\]
\[
H_2=b_i(r-2r^2+r^3),
\]
\[
H_3=3r^2-2r^3,
\]
\[
H_4=b_i(-r^2+r^3).
\]

于是：

\[
\begin{aligned}
w_b(x,z)=&H_1w_i(z)+H_2\theta_i(z)\\
&+H_3w_{i+1}(z)+H_4\theta_{i+1}(z)\\
&+A_b\psi_b(x,z).
\end{aligned}
\]

最小 C1 bubble 只需要满足边界位移和转角为零，例如：

\[
\boxed{\psi_b=r^2(1-r)^2g_b(z)}.
\]

它满足：

\[
\psi_b=0,\qquad \psi_{b,n}=0
\]

但允许：

\[
\psi_{b,nn}\neq 0.
\]

这正是让相邻 bay 可以共享 PBL 位移/转角，但独立发展局部曲率的关键。

### 5.1 与原 R02 局部模态的关系

原 R02 型：

\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta)
\]

本身在支承边界满足位移和一阶斜率为零，但二阶导数非零。因此它与 C1 运动学相容，而与 C2 `w_nn=0` 不相容。

当前重要认识：

**C1 路线可能允许继续复用原 R02 的主要几何/材料架构，不需要为满足 C2 而全面重编一个更高阶 bubble。**

---

## 6. PBL line displacement / rotation / force coupling 的完整含义

若最小 C1 模型不足，再升级为 finite-PBL line DOF。第 `i` 条 PBL 线可定义：

\[
\mathbf d_i(z)=
\begin{bmatrix}
u_i(z)\\w_i(z)\\\theta_i(z)
\end{bmatrix},
\]

其能量共轭线力：

\[
\mathbf f_i(z)=
\begin{bmatrix}T_i\\V_i\\M_i\end{bmatrix}.
\]

相邻左右 bay 对 PBL 给出边界力：

\[
\mathbf f_i^L,\qquad \mathbf f_i^R,
\]

PBL/core 子系统给：

\[
\mathbf f_i^{PBL/core}.
\]

线平衡：

\[
\boxed{
\mathbf f_i^L+\mathbf f_i^R+\mathbf f_i^{PBL/core}=0
}.
\]

即：

\[
T_i^L+T_i^R+T_i^{PBL}=0,
\]
\[
V_i^L+V_i^R+V_i^{PBL}=0,
\]
\[
M_i^L+M_i^R+M_i^{PBL}=0.
\]

其中 PBL line stiffness 应由真实 PBL 几何和材料能量推导，不允许经验弹簧、FEM 回标刚度。

---

## 7. 为什么 C1 反而比 C2 简化

C2 需要 PBL 边界同时匹配：

`w, w_n, w_nn`，

相当于更强的 C2/second-jet constraint，迫使使用 quintic lifting 或 `r^3(1-r)^3` 类高阶 bubble，并重编大量 geometry-dependent coefficient。

C1 只匹配：

`w, theta`，

因此：

- boundary kinematic conditions：3 -> 2；
- quintic Hermite -> cubic Hermite；
- `r^3(1-r)^3` -> `r^2(1-r)^2`；
- 不再需要 q-dependent curvature lifting；
- 原 R02 boundary-compatible mode 可能直接复用；
- local curvature 由 energy/force equilibrium 决定，而不是 kinematic 强制给定。

虽然显式保留多个 `A_b`，但每个 amplitude 仅局部耦合左右 PBL，Jacobian 为局部块/带状结构，可做 exact Schur condensation；外层仍可维持原 R14 的低维 N-M equilibrium。

---

## 8. 全局理论层保持不变

继续冻结 R14：

\[
Q=q(q+2q_0),
\]

\[
P(q)=P_{cr}\frac{q}{q+q_0}+CQ,
\]

\[
N_x^d=K_xQ,\qquad M_x^d=J_xq,
\]

\[
N_y^d=-\left[\frac{P(q)}B-GQ\right],\qquad M_y^d=J_yq.
\]

UHPC：连续厚度 current material operator 原样保留。

web/PBL longitudinal steel：原 ideal-EP exact operator 原样保留。

steel material/yield：R06 material architecture、plane-stress/von-Mises、first-radial-yield、finite harmonic Airy 思想保留；仅 kinematic boundary contract 从 C2 改为 C1。

四个 global balance 仍是：

\[
R_1=N_x-N_x^d=0,
\]
\[
R_2=M_x-M_x^d=0,
\]
\[
R_3=N_y-N_y^d=0,
\]
\[
R_4=M_y-M_y^d=0.
\]

禁止引入：effective width、effective area、FEM back-calibration、stored Pu root selection、经验 reduction factor。

---

## 9. 当前 chat-execution 的 C1/qU provisional numerical diagnostic

以下数字为本聊天中的 **provisional diagnostic execution**，用于记录当前推理节点；它们还未完成 source-grade 独立复现，因此不得升级成 production result。

### 9.1 trial registration

由于 BH050 exact face-specific `(x0,y0,s_f)` registration 仍未冻结，本轮沿用 deterministic 5/4 stagger diagnostic：

- one face 4 PBL -> bay widths roughly `[406.25, 562.5, 562.5, 562.5, 406.25] mm`；
- opposite face 5 PBL -> `[125, 562.5, 562.5, 562.5, 562.5, 125] mm`；
- axial cell `L_y=555.5556 mm = 5000/9`；
- independent local cells：99；
- local initial imperfection diagnostic：`A0_b=b_b/1600`。

此 registration 只是 diagnostic，不是 source lock。

### 9.2 在旧 R14 q 处重新平衡

固定旧 R14：

\[
q=0.00493091069216,
\qquad P=13.52478\ \mathrm{MN},
\]

但重新求四个 section generalized variables，chat diagnostic 得到约：

\[
\varepsilon_x^0=3.52910\times10^{-4},
\]
\[
\kappa_x=2.57553\times10^{-5}/\mathrm{mm},
\]
\[
\varepsilon_y^0=-1.544995\times10^{-3},
\]
\[
\boxed{\kappa_y=2.63515\times10^{-5}/\mathrm{mm}}.
\]

相对旧 R14：

\[
\kappa_y^{R14}=6.56100\times10^{-5}/\mathrm{mm},
\]

即 diagnostic 中约下降 60%。

对应 chat diagnostic whole-face mean longitudinal steel stress：

\[
\bar\sigma_y^{top}\approx-149.30\ \mathrm{MPa},
\]
\[
\bar\sigma_y^{bottom}\approx-404.38\ \mathrm{MPa}.
\]

纵向 resultants 约：

\[
N_y^{UHPC}\approx-2817.12\ \mathrm{N/mm},
\]
\[
N_y^{steel}\approx-2214.73\ \mathrm{N/mm},
\]
\[
N_y^{web}\approx-162.60\ \mathrm{N/mm},
\]

总和闭合至原 demand：

\[
N_y^A\approx-5194.44\ \mathrm{N/mm}.
\]

对应比例约：UHPC 54.2%，steel 42.6%，web 3.1%。**这些比例只作为 equilibrium bookkeeping，不作为 FE calibration target。**

### 9.3 provisional structural fold

沿 C1/qU diagnostic R4 branch 继续，chat execution 报告最小 singular value 快速下降，并通过转弯 continuation 得到 provisional fold：

\[
\boxed{q_{fold}^{C1,diag}\approx0.00702570}
\]

代回冻结 `P(q)`：

\[
\boxed{P_{fold}^{C1,diag}\approx15.36\ \mathrm{MN}}.
\]

fold 附近 UHPC longitudinal compression endpoint 约 `-2.8e-3`，尚未到 `-0.0035`，因此该 diagnostic 中事件顺序由旧 R14 的 UHPC material boundary first 改为 J4/structural fold first。

### 9.4 当前数值身份

\[
\boxed{15.36\ \mathrm{MN}\ \text{只能叫 C1-PBL/qU registration diagnostic}}
\]

不能称为 new-theory Pu。

至少存在两项未过门禁：

1. exact BH050 face-specific PBL registration `(x0,y0,s_f)` 尚未 source-lock；
2. 当前 multi-cell Mises maximum evaluator 尚未恢复到旧 R06 的完整 finite stationary-root / edge / corner algebraic certification 等级。

此外，上下钢面 mean stress 仍高度不对称，因此还不能说明 C1 已经完全抓到 FE 局部力流。

---

## 10. 当前最重要的理论判断

### 10.1 已经撤回/降级

- `PBL full curvature equality` 不再作为默认正确边界；
- 不再以 “steel/UHPC force share 是否接近 FE 某个百分比” 判断理论成功；
- 不再把整体凹面/凸面等同于 steel local 压面/拉面；
- 不再把 steel shell surface stress 当成 membrane resultant；
- 不再假定邻近 bay 必须同步鼓波。

### 10.2 当前保留

- steel bay 必须具有 independent local amplitude；
- PBL 首先是 displacement/rotation/force transfer line；
- steel 的高膜压与局部波峰 tensile surface stress 可同时存在；
- UHPC 是低频、平滑、连续厚度场；steel 是高膜压背景 + 高频 local shell-bending/postbuckling field；
- 全局 N-M balance 仍然是必须满足的平衡条件；只是不能用一个 force-share scalar 代替空间机理审计。

---

## 11. CURRENT_RECOMMENDED_NEXT_TASK

下一步不得重新打开 global P(q)、UHPC material、effective-width 路线。优先级如下：

### NEXT-1：source-lock BH050 real PBL registration

恢复/确认上下钢面真实：

- PBL 数量；
- face ownership；
- `x_i^+`, `x_i^-`；
- axial phase / `y0`；
- outer edge bay actual boundary operator；
- any stagger `s_f` convention。

### NEXT-2：FE membrane-vs-bending direct audit

在用户人工观察的相同波峰/非波峰/相邻 bay 位置，对 shell 同一 element 同时读取 SPOS/SNEG，构造：

\[
\sigma_m=(\sigma^{SPOS}+\sigma^{SNEG})/2,
\]

\[
\sigma_b=(\sigma^{SPOS}-\sigma^{SNEG})/2.
\]

目标：直接验证 `-200~-300 MPa` 是否主要为 membrane background，以及 tensile zone 是否主要由 local bending term 产生。

### NEXT-3：C1 source-grade local operator rebuild

在 exact registration 下：

- 复用/重编 C1-compatible R02 mode；
- 保留 exact finite LL/GL harmonics；
- 恢复 complete Mises stationary candidate certification；
- 每 bay 独立 `A_b`；
- local variables exact Schur condensation；
- 重新生成 whole-face steel current N-M operator。

### NEXT-4：只在 C1 仍不足时升级 finite-PBL line DOF

如果 FE 证明 PBL line 的 `w` 或 `theta` 本身相对 UHPC 有不可忽略偏差，再引入有限刚 PBL line DOF；line stiffness 必须从真实 PBL 几何/材料能量推导，不得经验拟合。

### NEXT-5：J4 fold decomposition

对 provisional C1 branch：

- 拆每个 bay 的 `U_b, lambda_b, mean sigma_y,b`；
- 拆 upper/lower face contribution；
- 计算 local Jacobian / condensed global Jacobian；
- 确认哪个 steel face、哪些 bay 造成 `s_min(J4)` 崩塌；
- 判断 fold 是否在 source-grade evaluator 下仍存在。

---

## 12. 下一对话恢复口令

下一聊天应从本文件继续，不能重开已排除路线。

推荐开场：

> 读取 `20260903_1132__NZSCCM__BH050_C1_PBL_FORCE_FLOW_PHYSICS_AND_CURRENT_DIAGNOSTIC_BACKUP_R01.md`，从 NEXT-1 source-lock BH050 real PBL registration 继续。保留 C1-PBL 位移/转角相容、bay 独立 amplitude、R14 global demand 和 N-M 四平衡；不要重新启用 PBL full-curvature equality、effective width、force-share calibration 或 common local-wave phase。

---

## 13. 状态标签

- `R14_GLOBAL_DEMAND`: FROZEN
- `UHPC_CURRENT_OPERATOR`: FROZEN
- `WEB_OPERATOR`: FROZEN
- `STEEL_MATERIAL_R06_ARCHITECTURE`: PRESERVE
- `PBL_FULL_CURVATURE_EQUALITY`: DOWNGRADED / NOT DEFAULT
- `C1_PBL_W_THETA_COMPATIBILITY`: CURRENT PRIMARY HYPOTHESIS
- `BAY_INDEPENDENT_AMPLITUDE`: REQUIRED
- `FORCE_SHARE_AS_CALIBRATION_TARGET`: PROHIBITED
- `FE_MEMBRANE_VS_BENDING_AUDIT`: REQUIRED NEXT DIAGNOSTIC
- `C1_Q_U_15.36_MN`: PROVISIONAL DIAGNOSTIC ONLY
- `PRODUCTION`: UNCHANGED
