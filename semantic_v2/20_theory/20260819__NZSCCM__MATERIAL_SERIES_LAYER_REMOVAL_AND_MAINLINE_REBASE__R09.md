# NZ-SCCM：无穷材料级数层删除与主线回正 R09

**日期：2026-08-19**  
**身份：MAINLINE CORRECTION / SERIES-LAYER-ONLY REFACTOR / ZERO DISCRETIZATION**

## 0. 本文件只改一件事

用户本轮要求不是重建一套新的 Picard–Fuchs 理论，也不是重做 Case21/Z6 全部力学模块；唯一目标是：

> 删除“把有限 current material operator 人为展开成 NZ-SCCM 自有无穷材料级数，再靠有限前缀或另行收敛证明恢复原函数”的生产层。

因此，本文件只替换旧链中的：

```text
current material operator
-> true-infinite material-coordinate series
-> finite-prefix convergence / N->infinity execution
```

其余保持：

```text
raw specimen
-> controlling complete representative halfwave
-> Nguyen/von-Karman continuous second-order kinematics
-> current material operator
-> exact continuous generalized integrals
-> P,Rq,Ralpha and same-source derivatives
-> direct solve Rq=0, Ralpha=0, det(J_lim)=0
-> Pu
```

R06-R08 中关于 algebraic / holonomic / Picard–Fuchs 的内容保留为**积分后端探索证据**，不再拥有主理论身份，也不得因为某个 holonomic backend 不可用而宣布材料理论或极限承载力理论失败。

---

# 1. 项目级硬边界

```text
ZERO_DISCRETIZATION_DEFAULT = LOCKED
DISCRETE_AUDIT_ORACLE = PROHIBITED
FINITE_PREFIX_CONVERGENCE_AS_EVIDENCE = PROHIBITED
SPATIAL_QUADRATURE = PROHIBITED
MATERIAL_POINT_GRID = PROHIBITED
CHEBYSHEV_COLLOCATION = PROHIBITED
```

除非用户对某一次任务明确授权，否则上述规则适用于正式计算、辅助验证、oracle、回归、定位和侧面检查。

---

# 2. 无穷级数层的正式删除

旧生产表达：

\[
F(\lambda)=\sum_{n=0}^{\infty}a_nT_n(\hat\lambda)
\]

及其 `N=32,48,64,...` 有限前缀，不再定义 current material operator，也不再承担生产计算身份。

对于普通混凝土，正式对象始终是原始有限 R10 映射：

\[
\boxed{\boldsymbol\sigma=\mathcal M_{R10}(\boldsymbol\varepsilon)}.
\]

“级数收敛回原函数”被直接替换为恒等关系：

\[
\boxed{\mathcal M_{\text{formal}}\equiv\mathcal M_{R10}}.
\]

因此不存在新的材料级数函数、最终阶次 `N`、prefix stop gate 或 `N\to\infty` 生产步骤。

---

# 3. R10 保持为固定有限函数组合

设等效应变矩阵为

\[
\mathbf E=
\begin{bmatrix}
E_{11}&E_{12}\\
E_{12}&E_{22}
\end{bmatrix}.
\]

定义

\[
\mathbf A=\mathbf E^2+\eta^2\mathbf I,
\qquad
\Delta_A=\sqrt{\det\mathbf A},
\qquad
s_A=\sqrt{\operatorname{tr}\mathbf A+2\Delta_A}.
\]

由 2x2 Cayley–Hamilton，正定平方根直接为

\[
\boxed{
\mathbf R=\mathbf A^{1/2}
=\frac{\mathbf A+\Delta_A\mathbf I}{s_A}
}.
\]

R10 正、负平滑 projector 直接写成

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
=\kappa\mathbf c
[\mathbf I+(\kappa-2)\mathbf c+\mathbf c^2]^{-1}
}.
\]

拉伸 primitive 保持来源冻结的原始三段有限函数 `u_R(theta)`；矩阵值由标准 spectral functional calculus 定义：

\[
\boxed{
\mathbf u_R=u_R(\mathbf t)
}.
\]

这不是新函数，而是把已冻结标量 `u_R` 作用到 2x2 对称矩阵 `t` 上。若特征值不同，

\[
u_R(\mathbf t)
=u_R(\theta_+)\mathbf P_+
+u_R(\theta_-)\mathbf P_-;
\]

重根处取标准 Hermite 极限。

随后

\[
\mathbf T=\mathbf u_R/\rho_R,
\]

\[
\mathbf U
=\kappa\mathbf E-\mathbf C+\kappa\mathbf c
+\mathbf u_R-\kappa\mathbf t,
\]

最终 R10 current stress matrix 仍是原冻结有限表达：

\[
\boxed{
\mathbf S
=\mathbf U
-a_{cc}\det(\mathbf C)\mathbf C
+\mathbf C\operatorname{adj}(\mathbf T)
-\rho_Ra_t\det(\mathbf T)\operatorname{adj}(\mathbf T^7)
}.
\]

这里所有矩阵幂、行列式、伴随、平方根和分段标量函数均为有限对象。

---

# 4. Nguyen 二阶运动学完全不改

在一个连续完整代表半波上

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad \zeta=2z/t.
\]

\[
M(q)=\frac{\pi^2}{\varepsilon_0}
\left(q_0q+\frac12q^2\right),
\qquad
B(q)=\frac{\pi^2t}{2\varepsilon_0b}q.
\]

\[
e_x=\nu D+MF_x+\alpha A_x+B\sin X\sin Y\,\zeta,
\]

\[
e_y=-D+MF_y+\alpha A_y+B\sin X\sin Y\,\zeta,
\]

\[
\gamma=2\cos X\cos Y
[(M-\alpha)\sin X\sin Y-B\zeta].
\]

由此得到连续应变向量

\[
\boldsymbol\varepsilon(X,Y,\zeta;D,q,\alpha).
\]

不存在空间材料点。

---

# 5. 极限承载力所需连续积分保持原定义

定义固定连续积分域

\[
\Omega=[0,\pi]\times[0,\pi]\times[-1,1].
\]

混凝土轴力：

\[
\boxed{
P_c(D,q,\alpha)
=-\frac{f_cbt}{2\pi^2}
\iiint_\Omega S_{yy}(\boldsymbol\varepsilon)
\,d\zeta\,dY\,dX
}.
\]

对广义变量 `z in {q,alpha}`，

\[
\boxed{
R_z^c
=\frac{f_c\varepsilon_0b\ell t}{2\pi^2}
\iiint_\Omega
\mathbf s^T\boldsymbol\varepsilon_{,z}
\,d\zeta\,dY\,dX
}.
\]

这里 `s` 为与工程剪应变约定一致的 normalized stress vector。

定义同源 material tangent

\[
\boxed{
\mathbf C_t
=\frac{\partial\mathbf s}{\partial\boldsymbol\varepsilon}
}
\]

直接由同一个有限 R10 映射解析求导得到；不允许另拟合 tangent。

于是任意 `a in {D,q,alpha}`：

\[
\boxed{
\partial_a R_z^c
=\frac{f_c\varepsilon_0b\ell t}{2\pi^2}
\iiint_\Omega
\left[
\boldsymbol\varepsilon_{,a}^{T}\mathbf C_t\boldsymbol\varepsilon_{,z}
+\mathbf s^T\boldsymbol\varepsilon_{,za}
\right]
\,d\Omega
}.
\]

同理

\[
\boxed{
\partial_a P_c
=-\frac{f_cbt}{2\pi^2}
\iiint_\Omega
\left(\mathbf C_t\boldsymbol\varepsilon_{,a}\right)_y
\,d\Omega
}.
\]

因此 `P,Rq,Ralpha,J_lim` 的定义全部保持有限、连续、同源；删除级数不会改变极限条件。

---

# 6. 积分后端与材料理论分离

上述三重积分是正式连续数学对象。其**评价后端**按以下优先级使用已有数学对象，不创造新的 NZ-SCCM 材料函数：

1. 初等闭式；
2. Beta/Gamma；
3. Gauss hypergeometric / Appell / Lauricella；
4. Legendre/Carlson elliptic integrals；
5. Abelian / hyperelliptic standard integrals；
6. holonomic / Picard–Fuchs finite system。

这些只是同一精确连续积分的不同标准表示。

若某个后端暂时不可用，只能标记

```text
ANALYTIC_INTEGRATION_BACKEND_BLOCK = YES
```

不得重新引入有限材料级数、离散空间积分或数值 oracle。

特别说明：R06-R08 的 Picard–Fuchs 探索属于第 6 类后端研究，不是新的主理论，更不是无穷级数替换成功与否的必要条件。

---

# 7. 极限联立完全不改

总量组装完成后，定义

\[
J_{\lim}=
\begin{bmatrix}
P_D&P_q&P_\alpha\\
R_{q,D}&R_{q,q}&R_{q,\alpha}\\
R_{\alpha,D}&R_{\alpha,q}&R_{\alpha,\alpha}
\end{bmatrix}.
\]

正式生产方程仍唯一为

\[
\boxed{R_q=0},\qquad
\boxed{R_\alpha=0},\qquad
\boxed{\det J_{\lim}=0}.
\]

求得

\[
(D_u,q_u,\alpha_u)
\]

后

\[
\boxed{P_u=P(D_u,q_u,\alpha_u)}.
\]

本 R09 不修改任何历史 released root，也不使用 comparator 参与求解。

---

# 8. 本轮唯一结论

```text
MATERIAL_TRUE_INFINITE_SERIES_PRODUCTION_LAYER = REMOVED
FINITE_PREFIX_N_AS_MODEL_OR_CONVERGENCE_GATE = REMOVED
FINITE_R10_CURRENT_OPERATOR = RESTORED AS DIRECT FORMAL OBJECT
NGUYEN_SECOND_ORDER_KINEMATICS = UNCHANGED
P_RQ_RALPHA_DEFINITIONS = UNCHANGED
DIRECT_3_VARIABLE_LIMIT_SYSTEM = UNCHANGED
PICARD_FUCHS = OPTIONAL EXACT-INTEGRATION BACKEND, NOT MAIN THEORY
ZERO_DISCRETIZATION = LOCKED
```

因此这次“无穷级数改造”到此为止，不再扩张成新的材料理论分支。

---

# 9. 唯一下一步

只处理一个问题：

> 在不改变 R10、不改变 Nguyen、不改变极限联立的前提下，为上述 exact continuous integrals 建立最简成熟标准函数评价后端。

优先从 Case21 concrete 的 `P_c(D,q,alpha)` 开始；若初等/Beta/elliptic/hypergeometric 可以闭合，就停在该层，不主动升级到 Picard–Fuchs。只有较低层标准函数无法闭合时，才使用更高层 exact backend。

不得再打开“无穷材料级数是否收敛”的问题，因为该生产层已被删除。
