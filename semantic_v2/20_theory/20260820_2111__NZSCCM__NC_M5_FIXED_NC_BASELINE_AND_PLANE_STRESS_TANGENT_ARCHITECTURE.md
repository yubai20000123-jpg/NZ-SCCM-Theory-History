# NZ-SCCM — NC-M5：固定 NC-基准本构上的低复杂度二维 current material operator

时间：2026-08-20 21:11 +08:00

状态：`NC_M5_ARCHITECTURE_CANDIDATE / PLANE_STRESS_TANGENT_GATE_PASS / FULL_MATERIAL_GATE_OPEN`

## 0. 治理边界

从本节点起，普通混凝土唯一比较对象命名为：

`NC-基准本构`

它就是此前 G21 已冻结的 ordinary-concrete low-parameter physical target，不再按 Nguyen/Foster/Saenz 等作者名切换参考。

冻结物理目标：

\[
CC:\quad c_i^*=c_i(1+a_{cc}c_1c_2),\qquad a_{cc}=0.1072329249362415,
\]

\[
TC/CT:\quad c^*=c(1-\tau),\qquad \text{tensile component unchanged},
\]

\[
TT:\quad \tau_i^*=\tau_i(1-a_t\tau_j^8),\qquad a_t=1-2^{-1/8}=0.08299595679532878.
\]

这些是材料级物理目标，不允许由 Case21/Swartz Pu 反标。

## 1. 材料原始输入与内部派生

允许进入 NC-M5 的 specimen/material inputs：

\[
E_0,\quad \nu,\quad f_c,\quad \varepsilon_{c0},\quad f_t.
\]

若来源缺失 `f_t`：

\[
f_t=0.1f_c.
\]

内部派生：

\[
\kappa=\frac{E_0\varepsilon_{c0}}{f_c},\qquad
\rho=\frac{f_t}{f_c},\qquad
x_{cr}=\frac{\rho}{\kappa}=\frac{f_t}{E_0\varepsilon_{c0}}.
\]

`a_cc`, `a_t`, tension-stiffening residual target `alpha2=0.3` 属于 NC-基准本构的 model-level constants，不是试件反标参数。

## 2. 物理应变与 NC 材料坐标张量

物理面内应变：

\[
\mathbf E=
\begin{bmatrix}
\varepsilon_x&\gamma_{xy}/2\\
\gamma_{xy}/2&\varepsilon_y
\end{bmatrix}.
\]

NC-M5 不采用 R3 的 state-dependent equivalent strain/dilation，也不采用 additive Pi stress correction。只保留一个固定、线性的 NC material-coordinate transform：

\[
\boxed{
\mathbf X=
\frac{(1-\nu)\mathbf E+\nu\,\mathrm{tr}(\mathbf E)\mathbf I}
{(1-\nu^2)\varepsilon_{c0}}
}
\]

即

\[
X_{11}=\frac{\varepsilon_x+\nu\varepsilon_y}{(1-\nu^2)\varepsilon_{c0}},
\]

\[
X_{22}=\frac{\nu\varepsilon_x+\varepsilon_y}{(1-\nu^2)\varepsilon_{c0}},
\]

\[
X_{12}=\frac{\gamma_{xy}}{2(1+\nu)\varepsilon_{c0}}.
\]

该变换不是新增材料未知量，不需 Newton，不含 history。由于 `X=aE+bI`，严格有

\[
\mathbf X\mathbf E=\mathbf E\mathbf X,
\]

所以二者主方向完全相同；不增加第二套 theta。

在物理主应变基底中：

\[
\lambda_1=\frac{\varepsilon_1+\nu\varepsilon_2}{(1-\nu^2)\varepsilon_{c0}},
\qquad
\lambda_2=\frac{\varepsilon_2+\nu\varepsilon_1}{(1-\nu^2)\varepsilon_{c0}}.
\]

NC-M5 的 CC/TC/CT/TT 是这一唯一 NC material-coordinate grid 的四区，不再额外维护 raw/equivalent 两套状态格。

## 3. 单轴 NC 基准 primitive

压缩：

\[
\boxed{
C_{NC}(c)=\frac{\kappa c}{1+(\kappa-2)c+c^2}
}
\]

满足

\[
C_{NC}(0)=0,\quad C'_{NC}(0)=\kappa,\quad C_{NC}(1)=1.
\]

拉伸定义为固定 NC-基准本构的 dimensionless tensile utilization

\[
\tau=T_{NC}(r),\qquad r=\lambda/x_{cr}\ge0,
\]

其材料目标为：开裂前真实弹性、peak utilization 1、post-cracking tension-stiffening 最终 residual 0.3；正式 C1/C2 regularization 属于 NC baseline。本节点不重新选择另一作者曲线，也不以 T4 替换 reference。

关键原点性质：

\[
T_{NC}(r)=r+O(r^2).
\]

所以 tensile normalized stress

\[
\rho T_{NC}(\lambda/x_{cr})
=\kappa\lambda+O(\lambda^2),
\]

因为 `rho/xcr=kappa`。

## 4. NC-M5 四区显式物理目标

### 4.1 CC

若

\[
\lambda_1<0,\qquad\lambda_2<0,
\]

定义

\[
c_1=-\lambda_1,\qquad c_2=-\lambda_2,
\]

\[
c_1^*=c_1(1+a_{cc}c_1c_2),
\qquad
c_2^*=c_2(1+a_{cc}c_1c_2).
\]

无量纲主应力：

\[
\boxed{s_1^{CC}=-C_{NC}(c_1^*)},
\qquad
\boxed{s_2^{CC}=-C_{NC}(c_2^*)}.
\]

### 4.2 TC

若

\[
\lambda_1>0,\qquad\lambda_2<0,
\]

定义

\[
r_1=\lambda_1/x_{cr},\qquad
\tau_1=T_{NC}(r_1),\qquad
c_2=-\lambda_2.
\]

G21/NC baseline target 直接采用

\[
c_2^*=c_2(1-\tau_1).
\]

于是

\[
\boxed{s_1^{TC}=\rho\tau_1},
\qquad
\boxed{s_2^{TC}=-C_{NC}(c_2^*)}.
\]

不引入 `k_tc`。

### 4.3 CT

严格交换方向：

\[
\lambda_1<0,\qquad\lambda_2>0,
\]

\[
c_1=-\lambda_1,\qquad
r_2=\lambda_2/x_{cr},\qquad
\tau_2=T_{NC}(r_2),
\]

\[
c_1^*=c_1(1-\tau_2),
\]

\[
\boxed{s_1^{CT}=-C_{NC}(c_1^*)},
\qquad
\boxed{s_2^{CT}=\rho\tau_2}.
\]

### 4.4 TT

若

\[
\lambda_1>0,\qquad\lambda_2>0,
\]

定义

\[
r_i=\lambda_i/x_{cr},\qquad \tau_i=T_{NC}(r_i).
\]

\[
\tau_1^*=\tau_1(1-a_t\tau_2^8),
\qquad
\tau_2^*=\tau_2(1-a_t\tau_1^8).
\]

\[
\boxed{s_1^{TT}=\rho\tau_1^*},
\qquad
\boxed{s_2^{TT}=\rho\tau_2^*}.
\]

### 4.5 物理应力

\[
\sigma_i=f_c s_i.
\]

由于 X 与 E 共轴，直接用同一 theta 旋回：

\[
\sigma_x=p^2\sigma_1+q^2\sigma_2,
\quad
\sigma_y=q^2\sigma_1+p^2\sigma_2,
\quad
\tau_{xy}=pq(\sigma_1-\sigma_2).
\]

## 5. 原点 plane-stress tangent 证明

在任意方向趋近原点：

压缩 primitive

\[
C_{NC}(c)=\kappa c+O(c^2).
\]

拉伸 primitive

\[
\rho T_{NC}(\lambda/x_{cr})=\kappa\lambda+O(\lambda^2).
\]

三类 interaction 的首个修正阶次分别是：

CC：

\[
c_i^*-c_i=a_{cc}c_i^2c_j=O(\|\lambda\|^3),
\]

TC/CT：

\[
c^*-c=-c\tau=O(\|\lambda\|^2),
\]

TT：

\[
\tau_i^*-\tau_i=-a_t\tau_i\tau_j^8=O(\|\lambda\|^9).
\]

因此四区统一满足

\[
s_i=\kappa\lambda_i+O(\|\lambda\|^2).
\]

张量形式：

\[
\mathbf S=\kappa\mathbf X+O(\|\mathbf E\|^2).
\]

物理应力

\[
\boldsymbol\sigma=f_c\mathbf S
= f_c\kappa\mathbf X+O(E^2)
=E_0\varepsilon_{c0}\mathbf X+O(E^2).
\]

代入 X：

\[
\boxed{
\boldsymbol\sigma
=
\frac{E_0}{1-\nu^2}
\left[(1-\nu)\mathbf E+\nu\,\mathrm{tr}(\mathbf E)\mathbf I\right]
+O(E^2)
}
\]

所以 engineering tangent：

\[
\boxed{
\mathbf D_0=
\frac{E_0}{1-\nu^2}
\begin{bmatrix}
1&\nu&0\\
\nu&1&0\\
0&0&(1-\nu)/2
\end{bmatrix}
}
\]

且

\[
D_{CC}(0)=D_{TC}(0)=D_{CT}(0)=D_{TT}(0)=D_0.
\]

`PLANE_STRESS_ORIGIN_TANGENT_GATE = PASS`。

## 6. 与结构 Poisson 基线的一致性

三变量结构运动学应恢复：

\[
\varepsilon_x=\nu\Delta/\ell+\varepsilon_m+\text{Nguyen second-order terms},
\]

\[
\varepsilon_y=-\Delta/\ell+\text{Nguyen second-order terms}.
\]

未屈曲 `A=0` 且 `epsilon_m=0` 时：

\[
X_{11}=0,
\qquad
X_{22}=-\frac{\Delta}{\ell\varepsilon_{c0}}.
\]

所以材料状态严格退化为单轴压缩轴，而不是 fake-TC。小应变时 `R_m=0` 自然给 `epsilon_m=0`。因此结构中的 Poisson baseline 与材料中的 plane-stress transform 不是重复计入：前者规定基础 admissible deformation，后者规定 stress-strain coupling。

## 7. 复杂度门禁

NC-M5 相对 NC-M4 不增加结构/材料未知量：

- 无 R3 `hat-epsilon_i` state-dependent dilation；
- 无 additive Pi；
- 无 `k_tc`；
- 无 `k_eta`；
- X 是物理应变的固定线性变换；
- X 与 E 共轴，不增加第二套 theta；
- 仍只需一个 2x2 symmetric eigenvalue radical；
- CC/TC/TT interaction 只含有限乘法和 8 次幂；
- compression primitive 仍是二次分母 rational；
- 若 tensile baseline 后续编译为低阶 rational，整个 NC-M5 可继续进入此前 half-angle -> algebraic/residue -> relative-GKZ 解析积分框架。

因此：

`POISSON_FIX_WITHOUT_COMPLEXITY_INCREASE = PASS`。

## 8. 当前仍需审计的问题

1. `T_NC` 的低复杂度单式实现尚未重构；reference 已固定，后续只允许对 NC-基准拉伸目标做解析简化，不再更换 comparison model。
2. G21 TC target `c*=c(1-tau)` 本身在 sector boundary 上可能产生有限 compression 下的一阶 tangent jump；这属于已知 C1/C2 transition-regularization 问题，不影响原点 tangent。是否需要窄材料级正则化，后续单独审计。
3. TT target 要求 tensile utilization `tau_i` 不应出现大于 1 的数值 overshoot；后续 tensile single-form 必须以 `[0,1]` boundedness 为硬门禁。
4. CC/TC/TT full-domain boundedness 与 consistent tangent 仍需同时审计；G21 已明确 stress-only certificate 不充分。
5. 当前 NC-M5 sector grid 明确定义在唯一 NC material coordinates `(lambda1,lambda2)` 上。物理 strain eigenvectors 与该 grid 共轴，但不再另设 raw-strain sector grid，避免重新制造 R3 的双网格冲突。

## 9. 当前结论

建议当前身份：

`NC-M5 = ACTIVE_MATERIAL_CANDIDATE`

已通过：

- fixed NC baseline governance；
- specimen/material parameter internal closure；
- no extra k_tc/k_eta；
- uniaxial-axis degeneration；
- common 2D plane-stress tangent at origin；
- no extra radical / no material Newton / no new state unknown；
- compatibility with exact analytic integration architecture at operator-class level。

尚未 production lock：必须先完成 `T_NC -> T5` 单式解析简化、transition tangent、full-domain boundedness 和 stress+tangent joint gate。
