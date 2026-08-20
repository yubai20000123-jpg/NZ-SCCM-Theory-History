# NZ-SCCM — NC-M4 实际被积函数的解析积分闭合与最终三方程组

时间：2026-08-20 16:36 +08:00

状态：`ACTIVE_DERIVATION / EXACT_ANALYTIC_REPRESENTATION / ZERO_SPATIAL_QUADRATURE`

## 0. 目标

本节点直接从已展开的三个实际被积函数出发：

\[
R_m=\iiint_V\sigma_x\,dV,
\]

\[
P=-\frac1\ell\iiint_V\sigma_y\,dV,
\]

\[
R_A=\iiint_V(\sigma_xG_x+\sigma_yG_y+\tau_{xy}G_\gamma)\,dV,
\]

其中 `sigma` 来自唯一 NC-M4 九宫格 current operator，theta 为局部派生主方向，膜力和弯矩均已保留。

本节点不重新构造材料函数，不引入 I1/I2 作为正式理论变量，不采用任何空间数值积分或材料点网格。

---

## 1. 归一化空间变量

令

\[
X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{\ell},\qquad \zeta=\frac{2z}{h},
\]

则

\[
dV=J_V\,dX\,dY\,d\zeta,
\qquad
J_V=\frac{b\ell h}{2\pi^2}.
\]

定义

\[
S=A_0A+\frac12A^2,\qquad H=A_0+A.
\]

再定义六个结构系数

\[
a_x=\frac{\pi^2S}{b^2},\quad
a_y=\frac{\pi^2S}{\ell^2},\quad
a_g=\frac{2\pi^2S}{b\ell},
\]

\[
b_x=\frac{hA\pi^2}{2b^2},\quad
b_y=\frac{hA\pi^2}{2\ell^2},\quad
b_g=\frac{hA\pi^2}{b\ell}.
\]

于是

\[
\varepsilon_x=\varepsilon_m+a_x\cos^2X\sin^2Y+b_x\zeta\sin X\sin Y,
\]

\[
\varepsilon_y=-\frac{\Delta}{\ell}+a_y\sin^2X\cos^2Y+b_y\zeta\sin X\sin Y,
\]

\[
\gamma_{xy}=a_g\cos X\sin X\sin Y\cos Y-b_g\zeta\cos X\cos Y.
\]

A 方向虚应变核为

\[
G_x=\frac{\pi^2H}{b^2}\cos^2X\sin^2Y+\frac{h\pi^2}{2b^2}\zeta\sin X\sin Y,
\]

\[
G_y=\frac{\pi^2H}{\ell^2}\sin^2X\cos^2Y+\frac{h\pi^2}{2\ell^2}\zeta\sin X\sin Y,
\]

\[
G_\gamma=\frac{2\pi^2H}{b\ell}\cos X\sin X\sin Y\cos Y-\frac{h\pi^2}{b\ell}\zeta\cos X\cos Y.
\]

---

## 2. theta 的理论身份与 CAS 消元身份

正式理论仍采用

\[
\tan 2\theta=\frac{\gamma_{xy}}{\varepsilon_x-\varepsilon_y}.
\]

方向1/2按连续方向标签保持，不按大小排序。为在 CAS 内部消去 theta，允许引入一个只记录方向1标签的离散符号 `varsigma=±1`；它不是结构未知量，只在连续方向 patch 内固定。

定义

\[
D_\varepsilon=\sqrt{(\varepsilon_x-\varepsilon_y)^2+\gamma_{xy}^2}.
\]

则

\[
\varepsilon_1=\frac{\varepsilon_x+\varepsilon_y+\varsigma D_\varepsilon}{2},
\qquad
\varepsilon_2=\frac{\varepsilon_x+\varepsilon_y-\varsigma D_\varepsilon}{2},
\]

\[
\cos^2\theta=\frac12\left(1+\varsigma\frac{\varepsilon_x-\varepsilon_y}{D_\varepsilon}\right),
\]

\[
\sin^2\theta=\frac12\left(1-\varsigma\frac{\varepsilon_x-\varepsilon_y}{D_\varepsilon}\right),
\]

\[
\sin\theta\cos\theta=\varsigma\frac{\gamma_{xy}}{2D_\varepsilon}.
\]

这只是 theta 的恒等消元，不建立新的物理层。

---

## 3. 半角有理化后，整个 NC-M4 只有一个平方根生成元

令

\[
u=\tan\frac X2,\qquad v=\tan\frac Y2,
\]

\[
U=1+u^2,\qquad V=1+v^2.
\]

有

\[
\sin X=\frac{2u}{U},\quad \cos X=\frac{1-u^2}{U},
\]

\[
\sin Y=\frac{2v}{V},\quad \cos Y=\frac{1-v^2}{V},
\]

\[
dX\,dY=\frac{4\,du\,dv}{UV}.
\]

取共同分母

\[
D_0=U^2V^2.
\]

则可写成

\[
\varepsilon_x=\frac{E_x(u,v,\zeta)}{D_0},
\qquad
\varepsilon_y=\frac{E_y(u,v,\zeta)}{D_0},
\qquad
\gamma_{xy}=\frac{G(u,v,\zeta)}{D_0},
\]

其中

\[
E_x=\varepsilon_mD_0+4a_xv^2(1-u^2)^2+4b_x\zeta\,uvUV,
\]

\[
E_y=-\frac{\Delta}{\ell}D_0+4a_yu^2(1-v^2)^2+4b_y\zeta\,uvUV,
\]

\[
G=4a_guv(1-u^2)(1-v^2)-b_g\zeta(1-u^2)(1-v^2)UV.
\]

注意：`E_x,E_y,G` 对 `zeta` 均为一次式。

定义唯一代数根

\[
Q(u,v,\zeta)=(E_x-E_y)^2+G^2.
\]

由于 `E_x,E_y,G` 对 `zeta` 一次，故

\[
Q=q_2(u,v)\zeta^2+q_1(u,v)\zeta+q_0(u,v)
\]

严格是二次式。

并且

\[
D_\varepsilon=\frac{\sqrt Q}{D_0}.
\]

因此主应变、theta 的三角因子以及四个 NC-M4 实体区的全部应力都属于同一二次代数扩张

\[
\boxed{
\mathbb K=\mathbb Q(u,v,\zeta,\sqrt Q).
}
\]

因为 NC-M4 的 `C,T4,beta,eta` 均为有理函数，任一局部实际积分核都可唯一压缩为

\[
\boxed{
K_{j,s}(u,v,\zeta)
=\frac{A_{j,s}(u,v,\zeta)+B_{j,s}(u,v,\zeta)\sqrt Q}
{C_{j,s}(u,v,\zeta)},
}
\]

其中

\[
j\in\{m,P,A\},\qquad s\in\{CC,TC,CT,TT\},
\]

且 `A,B,C` 均为有限多项式。高次 `sqrt(Q)` 通过 `Q` 归约；分母中的 `a+b sqrt(Q)` 通过共轭有理化，永远不产生第二个独立根式。

---

## 4. 厚度方向解析积分：全部初等闭合

固定 `(u,v)` 后，所有三类实际积分核均属于

\[
\mathbb Q(\zeta,\sqrt{q_2\zeta^2+q_1\zeta+q_0}).
\]

这是 genus-0 二次代数函数域，全部不定积分都是初等函数。

当 `q2 != 0` 时采用 Euler 有理化：

\[
w=\sqrt Q+\sqrt{q_2}\,\zeta.
\]

则

\[
\boxed{
\zeta=\frac{w^2-q_0}{2\sqrt{q_2}w+q_1}
}
\]

且

\[
\sqrt Q=w-\sqrt{q_2}\,\zeta
\]

也成为 `w` 的有理函数；`d zeta` 同样为有理函数。因此

\[
\int K_{j,s}(u,v,\zeta)\,d\zeta
=\int \frac{P_{j,s}(w;u,v)}{R_{j,s}(w;u,v)}\,dw.
\]

有限部分分式后得到

\[
\boxed{
F_{j,s}(u,v,\zeta)
=R^{(0)}_{j,s}(u,v,\zeta)
+\sum_r a_{r}\log L_r
+\sum_t b_t\arctan M_t,
}
\]

其中 `R^(0)` 为有理/代数项，`L_r,M_t` 为有限代数函数。也可以全部统一写为复对数形式。

### 厚度状态切换

状态切换只发生在 `epsilon1=0` 或 `epsilon2=0`。不引入 I1/I2；直接由

\[
4E_xE_y-G^2=0
\]

求精确厚度根。该式对 `zeta` 至多二次，所以厚度区间最多有两个内部状态前沿，最多形成三个连续材料区间。

令有效端点排序为

\[
-1=\zeta_0<\zeta_1<\cdots<\zeta_N=1,\qquad N\le3,
\]

第 `k` 段唯一材料状态为 `s_k`，则厚度解析凝聚后

\[
\boxed{
\mathcal T_j(u,v)
=\sum_{k=0}^{N-1}
\left[
F_{j,s_k}(u,v,\zeta_{k+1})-F_{j,s_k}(u,v,\zeta_k)
\right],
}
\]

其中 `j=m,P,A`。

这一步已经没有任何厚度积分符号。

---

## 5. 板面二维积分的精确标准函数身份

经过厚度闭合，`T_j(u,v)` 是有限个以下对象的组合：

- 有理函数；
- 有限代数根；
- 对数；
- arctan（等价于复对数）；
- 由状态根带来的代数端点函数。

把 `u=r/(1-r)`, `v=s/(1-s)` 映射到单位方形。每一项均可化为有限线性组合

\[
C\,r^{\alpha_0}(1-r)^{\alpha_1}s^{\beta_0}(1-s)^{\beta_1}
\prod_{k=1}^M P_k(r,s)^{\lambda_k}
\]

及其对参数 `lambda_k` 的有限阶导数（用于 `log P_k` 项）。

因此每个板面积分都是有限的 **relative/incomplete Aomoto-Gelfand / GKZ A-hypergeometric period**。记标准精确评价对象为

\[
\boxed{
\mathfrak A[\mathbf a,\boldsymbol\lambda;\mathcal C](\mathbf c),
}
\]

其中 `a` 是单项幂指数，`lambda` 是有限多项式因子指数，`c` 为由 `(Delta,A,epsilon_m,b,ell,h,material parameters)` 确定的多项式系数，`C` 表示由九宫格状态条件确定的相对积分链。对数项写成参数导数

\[
\boxed{
\log P_k\;P_k^{\lambda}
=\frac{\partial}{\partial\lambda}P_k^{\lambda}.
}
\]

因此不需要保留任何外层数值积分。Appell/Lauricella 是某些低因子数特例；一般情况下统一由 relative GKZ period 表示。

---

## 6. 三个已解析积分后的全局函数

令

\[
\mathfrak A_{j\nu}(\Delta,A,\varepsilon_m)
\]

表示第 `j` 类积分中第 `nu` 个由上述有限因式分解得到的 exact relative-GKZ 标准函数值。所有系数均由 NC-M4 的固定数字

`2, 1.07515, 0.09, -0.83, 1.04, 0.14, 0.15, 0.16`

以及 `fc,ft,eps_c0,eps_t0,b,ell,h,A0` 和当前 `(Delta,A,epsilon_m)` 恒等产生；没有拟合系数。

于是

\[
\boxed{
R_m(\Delta,A,\varepsilon_m)
=4J_V\sum_{\nu=1}^{N_m}c_{m\nu}\,\mathfrak A_{m\nu}=0,
}
\]

\[
\boxed{
P(\Delta,A,\varepsilon_m)
=4J_V\sum_{\nu=1}^{N_P}c_{P\nu}\,\mathfrak A_{P\nu},
}
\]

这里 `c_P` 已包含轴力定义中的 `-1/ell`。

\[
\boxed{
R_A(\Delta,A,\varepsilon_m)
=4J_V\sum_{\nu=1}^{N_A}c_{A\nu}\,\mathfrak A_{A\nu}=0.
}
\]

这三个式子已经没有 `x,y,z,X,Y,zeta,u,v` 空间积分变量。

---

## 7. 同源一阶导数

对任一广义变量

\[
g\in\{\Delta,A,\varepsilon_m\},
\]

直接对同一个 exact-period 表示求导：

\[
R_{m,g}=4J_V\sum_\nu
\left(c_{m\nu,g}\mathfrak A_{m\nu}
+c_{m\nu}\mathfrak A_{m\nu,g}\right),
\]

\[
P_{,g}=4J_V\sum_\nu
\left(c_{P\nu,g}\mathfrak A_{P\nu}
+c_{P\nu}\mathfrak A_{P\nu,g}\right),
\]

\[
R_{A,g}=4J_V\sum_\nu
\left(c_{A\nu,g}\mathfrak A_{A\nu}
+c_{A\nu}\mathfrak A_{A\nu,g}\right).
\]

等价地可在原 current operator 上先求同源切线再积分；二者是同一数学对象。

---

## 8. 最终三元极限联立方程组

未知量：

\[
\boxed{
\mathbf q=(\Delta,A,\varepsilon_m)^T.
}
\]

平衡方程：

\[
\boxed{R_A(\Delta,A,\varepsilon_m)=0,}
\]

\[
\boxed{R_m(\Delta,A,\varepsilon_m)=0.}
\]

在平衡流形上以 `Delta` 为路径参数，普通荷载极大条件可写为 Schur 导数

\[
L=P_{,\Delta}-[P_{,A}\ P_{,m}]
\begin{bmatrix}
R_{A,A}&R_{A,m}\\
R_{m,A}&R_{m,m}
\end{bmatrix}^{-1}
\begin{bmatrix}
R_{A,\Delta}\\R_{m,\Delta}
\end{bmatrix}=0.
\]

为避免对 `2x2` 子矩阵可逆性的额外假设，正式采用等价 bordered determinant：

\[
\boxed{
\det J_{\lim}=0,
}
\]

其中

\[
\boxed{
J_{\lim}=
\begin{bmatrix}
P_{,\Delta}&P_{,A}&P_{,m}\\
R_{A,\Delta}&R_{A,A}&R_{A,m}\\
R_{m,\Delta}&R_{m,A}&R_{m,m}
\end{bmatrix}.
}
\]

所以最终必须直接求解

\[
\boxed{
\mathbf F_{\lim}(\Delta,A,\varepsilon_m)=
\begin{bmatrix}
R_A\\
R_m\\
\det J_{\lim}
\end{bmatrix}
=\mathbf0.
}
\]

得到

\[
(\Delta_u,A_u,\varepsilon_{m,u}),
\]

最终极限承载力

\[
\boxed{
P_u=P(\Delta_u,A_u,\varepsilon_{m,u}).
}
\]

---

## 9. 当前完成度

- 三个实际三重积分已在数学类别上完全闭合：厚度为初等 Euler/Hermite 积分，板面为有限 relative-GKZ/A-hypergeometric exact periods。
- 正式表示中不存在空间 Gauss/Simpson/adaptive quadrature/material-point grid。
- NC-M4 不需要再次改写为多项式或材料级数。
- theta 保留理论身份；CAS 消元只产生一个二次根式生成元。
- 最终三未知量、两平衡方程与一个极限 determinant 已固定。
- 尚未代入具体 Case21 参数求数值根；本节点只完成一般矩形板的 exact analytic equation closure。
