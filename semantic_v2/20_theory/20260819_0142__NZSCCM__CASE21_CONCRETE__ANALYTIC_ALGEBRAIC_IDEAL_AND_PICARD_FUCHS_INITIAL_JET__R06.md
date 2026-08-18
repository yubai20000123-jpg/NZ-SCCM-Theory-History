# NZ-SCCM Case21 concrete：全解析零离散代数理想与 Picard–Fuchs 初始 Jet R06

**时间：2026-08-19 01:42 +08:00**  
**身份：CURRENT ANALYTIC-CLOSURE CHECKPOINT / NO DISCRETIZATION / NO NEW MATERIAL THEORY**  
**对象：Case21 concrete-only；建立 finite R10 → finite algebraic/semialgebraic integrand → holonomic/Picard–Fuchs 的严格输入，并完成 `tau=0` 的前三级解析初始 jet。**

---

## 0. 本轮决定

本文件 supersede R05 中所有涉及离散 oracle、有限 prefix 或“用数值离散侧面核验”的执行内容。保留 R05 的有限矩阵函数、三角到代数域、algebraic-period / holonomic / Picard–Fuchs 分类，但执行边界进一步收紧：

```text
DISCRETIZATION_DEFAULT = PROHIBITED
DISCRETE_AUDIT_ORACLE = PROHIBITED
FINITE_PREFIX_CONVERGENCE_AS_EVIDENCE = PROHIBITED
SPATIAL_QUADRATURE = PROHIBITED
MATERIAL_POINT_GRID = PROHIBITED
CHEBYSHEV_COLLOCATION = PROHIBITED
CONTINUUM_GRID_ORACLE = PROHIBITED
```

除非用户在某一次具体任务中明确授权离散化，否则不得使用任何离散形式作为正式计算、辅助验证、oracle、定位器、回归器或“先看答案”的手段。任务级授权不自动延续到后续任务。

本轮正式候选链为：

\[
\boxed{
\text{finite Nguyen kinematics}
\to\text{finite R10 current map}
\to\text{finite algebraic/semialgebraic period}
\to\text{finite holonomic/Picard--Fuchs system}
\to\text{finite-dimensional coupled limit solve}
}
\]

不存在生产层 `N=32,48,64,...`，也不存在离散空间 oracle。

---

# 1. 撤销事项

以下内容自本文件起不得再作为任何目标、校验或证据：

1. 上一轮由离散连续积分给出的 Case21 非均匀状态数值 `Pc ~= 401.58558 kN`：**WITHDRAWN / INVALID AS EVIDENCE**。
2. R04 的 prefix schedule / hard cap / oracle localization：仅保留为历史路径，不再进入当前解析主线。
3. R05 §20 P4 “independent numerical oracle regression”：**REVOKED**。
4. 任何以有限 Chebyshev prefix 的稳定性来证明 true-infinite material representation 的做法：**REVOKED AS FORMAL CONVERGENCE MECHANISM**。

冻结的历史 Case21/Z6 released Pu 只作为历史结果保留；本轮不使用它们选择参数、判断解析结果或构造当前 operator。

---

# 2. Case21 连续二阶运动学保持不变

代表半波：

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad b=\ell=1220\ \mathrm{mm}.
\]

材料/截面：

\[
t=19.30\ \mathrm{mm},\quad
f_c=21.23\ \mathrm{MPa},\quad
\varepsilon_0=0.00209,\quad
\nu=0.18,\quad q_0=0.0025.
\]

定义

\[
H_s=\sin X\sin Y,
\]

\[
M(q)=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\qquad
B(q)=\frac{\pi^2tq}{2\varepsilon_0b}.
\]

\[
e_x=\nu D+MF_x+\alpha A_x+BH_s\zeta,
\]

\[
e_y=-D+MF_y+\alpha A_y+BH_s\zeta,
\]

\[
\gamma=2\cos X\cos Y[(M-\alpha)H_s-B\zeta],
\]

其中

\[
F_x=\sin^2Y-\sin^2X\sin^2Y,
\qquad
F_y=\sin^2X-\sin^2X\sin^2Y,
\]

\[
A_x=-\frac14-\frac\nu2\sin^2X-\frac12\sin^2Y+\sin^2X\sin^2Y,
\]

\[
A_y=\frac\nu4-\frac12\sin^2X-\frac\nu2\sin^2Y+\sin^2X\sin^2Y.
\]

等效材料矩阵

\[
\mathbf E=
\begin{bmatrix}
(e_x+\nu e_y)/(1-\nu^2) & \gamma/[2(1+\nu)]\\
\gamma/[2(1+\nu)] & (\nu e_x+e_y)/(1-\nu^2)
\end{bmatrix}.
\]

---

# 3. 完整 R10 不再通过无穷级数定义

R10 平滑投影

\[
\Pi_\eta(z)=\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)}
\]

本身满足二次代数方程

\[
\boxed{
4(z^2+\eta^2)^2y^2
-4z^3(z^2+\eta^2)y
-\eta^2z^4=0,
\qquad y=\Pi_\eta(z).
}
\]

对 `2×2` 对称矩阵 `E`，令

\[
\mathbf A=\mathbf E^2+\eta^2\mathbf I,
\]

引入两个 algebraic generators

\[
\boxed{\Delta_A^2-\det\mathbf A=0},
\]

\[
\boxed{s_A^2-(\operatorname{tr}\mathbf A+2\Delta_A)=0}.
\]

选 principal real branch 后

\[
\boxed{
\mathbf R=\mathbf A^{1/2}=\frac{\mathbf A+\Delta_A\mathbf I}{s_A}
}.
\]

于是

\[
\boxed{
\mathbf t
=\frac12\mathbf E^2(\mathbf R+\mathbf E)\mathbf A^{-1}
},
\]

\[
\boxed{
\mathbf c
=\frac12\mathbf E^2(\mathbf R-\mathbf E)\mathbf A^{-1}
}.
\]

压缩 primitive：

\[
\boxed{
\mathbf C
=\kappa\mathbf c\,[\mathbf I+(\kappa-2)\mathbf c+\mathbf c^2]^{-1}
}.
\]

因此 projector 与 compression 全部是**有限 algebraic matrix functions**。

---

# 4. 拉伸三段 law 的全局有限 spectral 表示

设 `theta_+ >= theta_- >= 0` 为矩阵 `t` 的两个实特征值。定义

\[
\delta_t^2=(\operatorname{tr}\mathbf t)^2-4\det\mathbf t,
\qquad \delta_t\ge0,
\]

\[
\theta_\pm=\frac{\operatorname{tr}\mathbf t\pm\delta_t}{2}.
\]

对应 spectral projectors

\[
\mathbf P_+=\frac{\mathbf t-\theta_-\mathbf I}{\theta_+-\theta_-},
\qquad
\mathbf P_-=\frac{\theta_+\mathbf I-\mathbf t}{\theta_+-\theta_-},
\]

在重复特征值处取连续 Hermite 极限。

令原 R10 三段标量函数为 `p1(theta)`, `p2(theta)`, `p3(theta)=U_R`，阈值

\[
a_1=x_{cr},\qquad a_2=10x_{cr}.
\]

对每个特征值定义固定分段函数

\[
\mathfrak u(\theta)=
 p_1(\theta)
 +H(\theta-a_1)[p_2(\theta)-p_1(\theta)]
 +H(\theta-a_2)[U_R-p_2(\theta)].
\]

于是完整矩阵拉伸 law 是

\[
\boxed{
\mathbf u_R
=\mathfrak u(\theta_+)\mathbf P_+
+\mathfrak u(\theta_-)\mathbf P_-.
}
\]

这不是 spatial-cell 分区。`H` 只编码原材料 law 的固定 semi-algebraic 条件。

R10 特意满足阈值匹配：

在 `r=t/xcr=1`：

\[
p_1(1)=p_2(1)=H_R,
\]

\[
p_1'(1)=p_2'(1)=0,
\]

\[
p_1''(1)=p_2''(1)=0.
\]

在 `r=10`：

\[
p_2(10)=U_R,\qquad p_2'(10)=0,\qquad p_2''(10)=0.
\]

因此 first tangent 与当前所需的二阶运动学一致导数不会因为 Heaviside 写法产生未抵消的 delta 项。材料分段可作为 holonomic distribution / semi-algebraic inequality 精确处理，而不需要 numerical cells。

随后

\[
\mathbf T=\mathbf u_R/\rho,
\]

\[
\mathbf U=\kappa\mathbf E-\mathbf C+\kappa\mathbf c+\mathbf u_R-\kappa\mathbf t,
\]

\[
\boxed{
\mathbf S
=\mathbf U
-a_{cc}\det(\mathbf C)\mathbf C
+\mathbf C\operatorname{adj}(\mathbf T)
-\rho a_t\det(\mathbf T)\operatorname{adj}(\mathbf T^7)
}.
\]

`T^7` 是有限矩阵幂。

---

# 5. 三角半波到固定代数域：P0 完成

令

\[
r=\sin^2(X/2),\qquad s=\sin^2(Y/2),
\]

并引入

\[
\boxed{\omega^2-r(1-r)s(1-s)=0},\qquad \omega\ge0.
\]

则

\[
\sin X=2\sqrt{r(1-r)},\quad
\sin Y=2\sqrt{s(1-s)},
\]

\[
\cos X=1-2r,\quad \cos Y=1-2s,
\]

\[
H_s=4\omega,
\]

\[
\boxed{dX\,dY=\frac{dr\,ds}{\omega}}.
\]

整个结构域严格变为一个固定 semi-algebraic domain：

\[
0\le r\le1,\quad0\le s\le1,\quad-1\le\zeta\le1,
\]

配合 algebraic relation `omega^2=r(1-r)s(1-s)`。

因此 concrete axial target 是固定 period：

\[
\boxed{
P_c(D,q,\alpha)
=-\frac{f_cbt}{2\pi^2}
\int_0^1\int_0^1\int_{-1}^{1}
\frac{S_{yy}(r,s,\zeta;D,q,\alpha)}{\omega}
\,d\zeta\,ds\,dr.
}
\]

这一定义不含任何离散化或自造无穷材料级数。

---

# 6. 可交给 creative telescoping 的有限 algebraic / semi-algebraic ideal：P1 完成

取纯数学辅助参数

\[
q(\tau)=\tau q,\qquad \alpha(\tau)=\tau\alpha,
\]

\[
M(\tau)=m_1\tau+m_2\tau^2,
\]

\[
m_1=\frac{\pi^2q_0q}{\varepsilon_0},
\qquad
m_2=\frac{\pi^2q^2}{2\varepsilon_0},
\]

\[
B(\tau)=B_1\tau,
\qquad
B_1=\frac{\pi^2tq}{2\varepsilon_0b}.
\]

对 `P_c(tau)` 的 finite algebraic generators 至少可取

\[
\mathcal G=
\{\omega,\Delta_A,s_A,\delta_t,\theta_+,\theta_-\}
\]

以及矩阵 `E,A,R,t,c,C,T,U,S` 的有限有理定义。

核心 polynomial relations 为

\[
\boxed{g_1=\omega^2-r(1-r)s(1-s)=0},
\]

\[
\boxed{g_2=\Delta_A^2-\det(\mathbf E^2+\eta^2\mathbf I)=0},
\]

\[
\boxed{g_3=s_A^2-[\operatorname{tr}(\mathbf E^2+\eta^2\mathbf I)+2\Delta_A]=0},
\]

\[
\boxed{g_4=\delta_t^2-[(\operatorname{tr}\mathbf t)^2-4\det\mathbf t]=0},
\]

\[
\boxed{2\theta_+-(\operatorname{tr}\mathbf t+\delta_t)=0},
\]

\[
\boxed{2\theta_--(\operatorname{tr}\mathbf t-\delta_t)=0}.
\]

阈值条件只需附加固定 algebraic inequalities

\[
\theta_\pm-a_1\gtreqless0,
\qquad
\theta_\pm-a_2\gtreqless0,
\]

或等价 Heaviside distributions。没有引入任何 spatial numerical subdivision。

所以 P0/P1 的结论是：

```text
FINITE_R10_EXACT_INTEGRAND = CONSTRUCTIBLE
FINITE_ALGEBRAIC_IDEAL = CONSTRUCTIBLE
MATERIAL_BRANCHES = FINITE_SEMIALGEBRAIC_CONDITIONS
CHEBYSHEV_INFINITY_REQUIRED_FOR_DEFINITION = NO
SPATIAL_DISCRETIZATION_REQUIRED_FOR_DEFINITION = NO
```

---

# 7. `tau=0` exact base point

当 `tau=0`：

\[
M=B=\alpha=0,
\]

\[
\boxed{\mathbf E_0=\operatorname{diag}(0,-D)}.
\]

设

\[
g_0=u(-D)
\]

是此时 `y` 主方向 normalized R10 stress，其中

\[
u(\lambda)
=\kappa\lambda-C[\Pi_\eta(-\lambda)]
+\kappa\Pi_\eta(-\lambda)
+u_R[\Pi_\eta(\lambda)]
-\kappa\Pi_\eta(\lambda).
\]

则整个半波材料场均匀，因此无需任何积分近似：

\[
\boxed{P_c(0)=-f_cbt\,g_0}.
\]

---

# 8. exact first jet：`P_c'(0)`

展开

\[
\mathbf E(\tau)=\mathbf E_0+\tau\mathbf E_1+\tau^2\mathbf E_2.
\]

在 `(lambda_1,lambda_2)=(0,-D)`，由于

\[
\Pi_\eta'(0)=0,
\]

且 `C_1,T_1=O(lambda_1^2)`，得到

\[
\left.\frac{\partial s_2}{\partial\lambda_1}\right|_0=0.
\]

令

\[
g_2=u'(-D).
\]

精确连续 moments 为

\[
\iiint E_{11}^{(1)}\,d\Omega
=\frac{\pi^2}{2(1-\nu)}(m_1-\alpha),
\]

\[
\iiint E_{22}^{(1)}\,d\Omega
=\frac{\pi^2}{2(1-\nu)}(m_1-\nu\alpha).
\]

于是

\[
\boxed{
P_c'(0)
=-\frac{f_cbt}{4(1-\nu)}
\,g_2\,(m_1-\nu\alpha).
}
\]

注意 `B_1` 的一阶厚度项因 `zeta` 奇对称精确消失；这不是数值近似。

---

# 9. exact second jet：`P_c''(0)`

在基点处定义

\[
g_{22}=u''(-D),
\]

并令 `C_2=C(Pi_eta(D))`。由于

\[
\Pi_\eta''(0)=1/\eta,
\]

得到与 transverse principal coordinate 有关的精确二阶材料系数

\[
\boxed{
g_{11}
=\frac{\kappa C_2}{\eta}
\left(\frac1\rho-a_{cc}C_2\right).
}
\]

同时

\[
g_{12}=0.
\]

定义四个 exact continuous moments：

\[
I_{11}=\iiint (E_{11}^{(1)})^2d\Omega,
\quad
I_{22}=\iiint (E_{22}^{(1)})^2d\Omega,
\]

\[
I_{12}=\iiint (E_{12}^{(1)})^2d\Omega,
\quad
I_2=\iiint E_{22}^{(2)}d\Omega.
\]

它们全部由 Beta/Gamma 初等矩精确得到：

\[
I_2=\frac{m_2\pi^2}{2(1-\nu)}.
\]

\[
I_{12}
=\frac{\pi^2}{(1+\nu)^2}
\left[
\frac{(m_1-\alpha)^2}{32}
+\frac{B_1^2}{6}
\right].
\]

令

\[
\mathcal A_{11}=\frac{\pi^2}{64}\Big[
 m_1^2(9\nu^2+2\nu+9)
+m_1\alpha(4\nu^3-22\nu^2-8\nu-14)
+\alpha^2(2\nu^4-4\nu^3+9\nu^2+6\nu+7)
\Big],
\]

\[
\mathcal A_{22}=\frac{\pi^2}{64}\Big[
 m_1^2(9\nu^2+2\nu+9)
+m_1\alpha(-4\nu^3-30\nu^2-6)
+\alpha^2(6\nu^4+4\nu^3+9\nu^2-2\nu+3)
\Big].
\]

则

\[
I_{11}
=\frac{2\mathcal A_{11}}{(1-\nu^2)^2}
+\frac{\pi^2B_1^2}{6(1-\nu)^2},
\]

\[
I_{22}
=\frac{2\mathcal A_{22}}{(1-\nu^2)^2}
+\frac{\pi^2B_1^2}{6(1-\nu)^2}.
\]

利用非重复主值的二阶谱扰动恒等式，`S_yy''(0)` 的完整体积分为

\[
\boxed{
\iiint S_{yy}''(0)d\Omega
=
2g_2I_2
+g_{11}I_{11}
+g_{22}I_{22}
-\frac{2g_2}{D}I_{12}
-\frac{2g_0}{D^2}I_{12}.
}
\]

所以

\[
\boxed{
P_c''(0)
=-\frac{f_cbt}{2\pi^2}
\left[
2g_2I_2
+g_{11}I_{11}
+g_{22}I_{22}
-\frac{2g_2}{D}I_{12}
-\frac{2g_0}{D^2}I_{12}
\right].
}
\]

这已经给出 finite Picard–Fuchs ODE 所需 initial jet 的前三项，全部来自 exact R10 point derivatives + exact continuous moments，没有任何空间离散、数值求积或有限材料级数。

---

# 10. 一个不使用历史根的 Case21 解析 jet 实例

仅用于确认上述解析公式可执行，任选 generalized state：

\[
D=0.600,\qquad q=0.000600,\qquad \alpha=0.000500.
\]

这不是历史极限根，也不使用试验荷载。

此时

\[
m_1=\frac{\pi^2q_0q}{\varepsilon_0}
=0.007083448134753128\ldots,
\]

\[
m_2=\frac{\pi^2q^2}{2\varepsilon_0}
=0.0008500137761703754\ldots,
\]

\[
B_1=\frac{\pi^2tq}{2\varepsilon_0b}
=0.02241156540995662\ldots.
\]

对 `lambda=-0.6` 直接评价 finite R10 及其解析导数：

\[
g_0=u(-0.6)=-0.8823897770417121\ldots,
\]

\[
g_2=u'(-0.6)=0.6919084556657561\ldots,
\]

\[
g_{22}=u''(-0.6)=2.518616267739352\ldots,
\]

\[
g_{11}=6995.788498844974\ldots.
\]

得到

\[
\boxed{P_c(0)=441.090395923459\ \mathrm{kN}},
\]

\[
\boxed{P_c'(0)=-0.737451199873438\ \mathrm{kN}},
\]

\[
\boxed{P_c''(0)=-243.048322761774\ \mathrm{kN}}.
\]

这些数值是**有限点函数 + 闭式矩公式的直接评价**，不是任何离散积分结果。

严禁把

\[
P_c(0)+P_c'(0)+\tfrac12P_c''(0)
\]

当作 `tau=1` 的有限 Taylor 截断答案；这些 jet 只能作为未来**有限 Picard–Fuchs differential system** 的 exact initial conditions。

---

# 11. 当前 Picard–Fuchs gate

本轮完成：

```text
P0_FINITE_R10_GLOBAL_INTEGRAND = PASS
P1_FINITE_ALGEBRAIC_SEMIALGEBRAIC_IDEAL = PASS
TAU0_INITIAL_JET_P0_P1_P2 = PASS
DISCRETE_ORACLE = REMOVED
CHEBYSHEV_PREFIX_PRODUCTION = REMOVED
```

尚未完成：

```text
FULL_Pc_TAU_TELESCOPER_GENERATED = NO
FULL_Pc_FINITE_PICARD_FUCHS_OPERATOR = OPEN
Pc_TAU1_ANALYTIC_EVALUATION = OPEN
```

因此当前唯一下一任务是：

\[
\boxed{
\text{从 §6 的 finite algebraic/semi-algebraic ideal 生成 }P_c(\tau)
\text{ 的有限 telescoper / Picard--Fuchs operator。}
}
\]

如果当前符号后端无法完成，应停止并报告

```text
ANALYTIC_CLOSURE_BACKEND_BLOCK = YES
```

不得退回 Gauss、grid、finite prefix、collocation 或其他离散形式。

---

# 12. 对现有理论文件的身份调整

```text
R03 = HISTORICAL FULL-CHAIN BLIND LEDGER; not current execution contract
R04 = HISTORICAL; finite-prefix/oracle execution layer superseded
R05 = HISTORICAL CANDIDATE; algebraic classification retained, discrete P4 revoked
R06 = CURRENT ANALYTIC-CLOSURE CHECKPOINT
```

历史 released Case21/Z6 Pu 不在本轮重算，也不被删除；它们与当前“如何把连续积分闭合为固定数学对象”的研究问题分开保存。
