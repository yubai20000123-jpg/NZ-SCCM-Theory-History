# NZ-SCCM — NC-M6 同源九导数、极限行列式与最终三元联立 V8

时间：2026-08-21 01:37 +08:00

状态：
`NC_M4_SAME_ROUTE_CONFIRMED / NC_M6_EXACT_THREE_FUNCTIONS / SAME_SOURCE_9_DERIVATIVES / LIMIT_DETERMINANT_READY / FINAL_3EQ_READY / CASE21_NOT_RUN`

## 0. 与 NC-M4 的关系

本节点严格复制 NC-M4 在 exact-period 三函数之后的最后两步：

1. 对同一 exact 三函数做同源一阶导数；
2. 构造 bordered determinant 极限条件并与两个平衡残量联立。

不重新打开积分形式，不新增材料理论，不增加空间数值积分。

---

## 1. 当前三个 exact functions

沿用 V7：

\[
P(D,q,\alpha)
=
C_P^{(0)}
\sum_{\nu\in I_P}
C_{P\nu}
\partial_{\boldsymbol\lambda}^{\mathbf m_{P\nu}}
\mathfrak A_{P\nu},
\]

\[
R_q(D,q,\alpha)
=
C_q^{(0)}
\sum_{\nu\in I_q}
C_{q\nu}
\partial_{\boldsymbol\lambda}^{\mathbf m_{q\nu}}
\mathfrak A_{q\nu},
\]

\[
R_\alpha(D,q,\alpha)
=
C_\alpha^{(0)}
\sum_{\nu\in I_\alpha}
C_{\alpha\nu}
\partial_{\boldsymbol\lambda}^{\mathbf m_{\alpha\nu}}
\mathfrak A_{\alpha\nu}.
\]

其中

\[
C_P^{(0)}=-\frac{f_cb t_r}{\pi^2},
\qquad
C_q^{(0)}=C_\alpha^{(0)}
=\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}.
\]

这些 prefactor 与 \(D,q,\alpha\) 无关。

---

## 2. exact-period 层的统一一阶导数规则

令

\[
g\in\{D,q,\alpha\}.
\]

定义简写

\[
\mathcal A_{j\nu}
=
\partial_{\boldsymbol\lambda}^{\mathbf m_{j\nu}}
\mathfrak A_{j\nu}.
\]

则对任一

\[
F_j=
C_j^{(0)}
\sum_{\nu\in I_j}
C_{j\nu}\mathcal A_{j\nu}
\]

有

\[
\boxed{
F_{j,g}
=
C_j^{(0)}
\sum_{\nu\in I_j}
\left[
C_{j\nu,g}\mathcal A_{j\nu}
+
C_{j\nu}\mathcal A_{j\nu,g}
\right].
}
\]

这里 \(\mathcal A_{j\nu,g}\) 是同一个 relative/incomplete exact-period 对象相对于结构变量 \(g\) 的同源导数；没有新增积分理论。

---

## 3. 九个导数逐个写出

### 3.1 轴力三导数

\[
\boxed{
P_D
=
C_P^{(0)}
\sum_{\nu\in I_P}
\left[
C_{P\nu,D}\mathcal A_{P\nu}
+
C_{P\nu}\mathcal A_{P\nu,D}
\right].
}
\]

\[
\boxed{
P_q
=
C_P^{(0)}
\sum_{\nu\in I_P}
\left[
C_{P\nu,q}\mathcal A_{P\nu}
+
C_{P\nu}\mathcal A_{P\nu,q}
\right].
}
\]

\[
\boxed{
P_\alpha
=
C_P^{(0)}
\sum_{\nu\in I_P}
\left[
C_{P\nu,\alpha}\mathcal A_{P\nu}
+
C_{P\nu}\mathcal A_{P\nu,\alpha}
\right].
}
\]

### 3.2 \(R_q\) 三导数

\[
\boxed{
R_{q,D}
=
C_q^{(0)}
\sum_{\nu\in I_q}
\left[
C_{q\nu,D}\mathcal A_{q\nu}
+
C_{q\nu}\mathcal A_{q\nu,D}
\right].
}
\]

\[
\boxed{
R_{q,q}
=
C_q^{(0)}
\sum_{\nu\in I_q}
\left[
C_{q\nu,q}\mathcal A_{q\nu}
+
C_{q\nu}\mathcal A_{q\nu,q}
\right].
}
\]

\[
\boxed{
R_{q,\alpha}
=
C_q^{(0)}
\sum_{\nu\in I_q}
\left[
C_{q\nu,\alpha}\mathcal A_{q\nu}
+
C_{q\nu}\mathcal A_{q\nu,\alpha}
\right].
}
\]

### 3.3 \(R_\alpha\) 三导数

\[
\boxed{
R_{\alpha,D}
=
C_\alpha^{(0)}
\sum_{\nu\in I_\alpha}
\left[
C_{\alpha\nu,D}\mathcal A_{\alpha\nu}
+
C_{\alpha\nu}\mathcal A_{\alpha\nu,D}
\right].
}
\]

\[
\boxed{
R_{\alpha,q}
=
C_\alpha^{(0)}
\sum_{\nu\in I_\alpha}
\left[
C_{\alpha\nu,q}\mathcal A_{\alpha\nu}
+
C_{\alpha\nu}\mathcal A_{\alpha\nu,q}
\right].
}
\]

\[
\boxed{
R_{\alpha,\alpha}
=
C_\alpha^{(0)}
\sum_{\nu\in I_\alpha}
\left[
C_{\alpha\nu,\alpha}\mathcal A_{\alpha\nu}
+
C_{\alpha\nu}\mathcal A_{\alpha\nu,\alpha}
\right].
}
\]

---

## 4. current-operator 层的同源审计式

定义 engineering strain/stress vectors

\[
\boldsymbol e=
\begin{bmatrix}
\varepsilon_x\\
\varepsilon_y\\
\gamma_{xy}
\end{bmatrix},
\qquad
\boldsymbol s=
\begin{bmatrix}
\sigma_x\\
\sigma_y\\
\tau_{xy}
\end{bmatrix}.
\]

NC-M6 physical consistent tangent

\[
\boxed{
\mathbf D_c=
\frac{\partial\boldsymbol s}{\partial\boldsymbol e}.
}
\]

注意：NC-M6 不假定 hyperelastic major symmetry，因此一般不强制 \(\mathbf D_c=\mathbf D_c^T\)。

定义三个广义应变导数

\[
\boldsymbol e_D
=
\frac{\partial\boldsymbol e}{\partial D},
\qquad
\boldsymbol e_q
=
\frac{\partial\boldsymbol e}{\partial q},
\qquad
\boldsymbol e_\alpha
=
\frac{\partial\boldsymbol e}{\partial\alpha}.
\]

以及

\[
\boldsymbol e_{qq}
=
\frac{\partial^2\boldsymbol e}{\partial q^2}.
\]

当前运动学给

\[
\boxed{
\boldsymbol e_D
=
\varepsilon_0
\begin{bmatrix}
\nu\\-1\\0
\end{bmatrix}.
}
\]

\[
\boxed{
\boldsymbol e_\alpha
=
\frac{\varepsilon_0}{\mathscr D}
\begin{bmatrix}
A_x^\#\\
A_y^\#\\
A_\gamma^\#
\end{bmatrix}.
}
\]

\[
\boxed{
\boldsymbol e_q
=
\frac{\varepsilon_0}{\mathscr D}
\begin{bmatrix}
Q_x^\#\\
Q_y^\#\\
Q_\gamma^\#
\end{bmatrix}.
}
\]

而

\[
\boxed{
\boldsymbol e_{qq}
=
\begin{bmatrix}
\pi^2F_x\\
\pi^2k^2F_y\\
2\pi^2k\sin X\sin Y\cos X\cos Y
\end{bmatrix}.
}
\]

其中

\[
F_x=\sin^2Y-\sin^2X\sin^2Y,
\qquad
F_y=\sin^2X-\sin^2X\sin^2Y.
\]

并且

\[
\boldsymbol e_{qD}=\boldsymbol0,
\qquad
\boldsymbol e_{q\alpha}=\boldsymbol0,
\]

\[
\boldsymbol e_{\alpha D}
=
\boldsymbol e_{\alpha q}
=
\boldsymbol e_{\alpha\alpha}
=
\boldsymbol0.
\]

令轴向应力 selector

\[
\boldsymbol m_y=
\begin{bmatrix}
0\\1\\0
\end{bmatrix}.
\]

则九个导数也可直接写为同一个 current operator 的积分：

\[
\boxed{
P_D
=
-\frac1\ell
\iiint_V
\boldsymbol m_y^T
\mathbf D_c
\boldsymbol e_D
\,dV,
}
\]

\[
\boxed{
P_q
=
-\frac1\ell
\iiint_V
\boldsymbol m_y^T
\mathbf D_c
\boldsymbol e_q
\,dV,
}
\]

\[
\boxed{
P_\alpha
=
-\frac1\ell
\iiint_V
\boldsymbol m_y^T
\mathbf D_c
\boldsymbol e_\alpha
\,dV.
}
\]

\[
\boxed{
R_{q,D}
=
\iiint_V
\boldsymbol e_q^T
\mathbf D_c
\boldsymbol e_D
\,dV,
}
\]

\[
\boxed{
R_{q,q}
=
\iiint_V
\left(
\boldsymbol e_q^T
\mathbf D_c
\boldsymbol e_q
+
\boldsymbol s^T
\boldsymbol e_{qq}
\right)
\,dV,
}
\]

\[
\boxed{
R_{q,\alpha}
=
\iiint_V
\boldsymbol e_q^T
\mathbf D_c
\boldsymbol e_\alpha
\,dV.
}
\]

\[
\boxed{
R_{\alpha,D}
=
\iiint_V
\boldsymbol e_\alpha^T
\mathbf D_c
\boldsymbol e_D
\,dV,
}
\]

\[
\boxed{
R_{\alpha,q}
=
\iiint_V
\boldsymbol e_\alpha^T
\mathbf D_c
\boldsymbol e_q
\,dV,
}
\]

\[
\boxed{
R_{\alpha,\alpha}
=
\iiint_V
\boldsymbol e_\alpha^T
\mathbf D_c
\boldsymbol e_\alpha
\,dV.
}
\]

由于 \(\mathbf D_c\) 一般不强制 major symmetric，正式理论不得预先令 \(R_{q,\alpha}=R_{\alpha,q}\)。二者必须各自按上式保留。

这些 current-operator 积分不是重新打开空间数值积分；它们只是对 V7 exact-period 导数的同源物理审计式。正式实现仍使用 V7 的 exact-period 三函数直接求导。

---

## 5. 内部材料 front 的移动边界项

若先从 branchwise 厚度积分求导，

\[
F(g)
=
\sum_b
\int_{\zeta_b^-(g)}^{\zeta_b^+(g)}
K_b(\zeta,g)\,d\zeta,
\]

Leibniz 规则会产生内部 front 速度项。

但相邻 branch 在同一个物理 front 上满足应力连续；且 \(\boldsymbol e_q,\boldsymbol e_\alpha\) 是 branch-independent kinematic kernels，所以

\[
K_b(\zeta_f,g)
=
K_{b+1}(\zeta_f,g)
\]

对 \(P,R_q,R_\alpha\) 均成立。

因此相邻内部 front 项严格 telescopic cancellation：

\[
K_b\zeta_f'
-
K_{b+1}\zeta_f'
=0.
\]

外层厚度端点 \(\zeta=\pm1\) 固定。

所以同源一阶导数不需要新增“front correction force”。这与直接对已经闭合的 exact-period 三函数求导一致。

---

## 6. 极限 Jacobian

定义

\[
\boxed{
J_{\lim}(D,q,\alpha)
=
\begin{bmatrix}
P_D&P_q&P_\alpha\\
R_{q,D}&R_{q,q}&R_{q,\alpha}\\
R_{\alpha,D}&R_{\alpha,q}&R_{\alpha,\alpha}
\end{bmatrix}.
}
\]

极限函数

\[
\boxed{
\mathcal L(D,q,\alpha)
=
\det J_{\lim}.
}
\]

将 \(3\times3\) 行列式直接展开：

\[
\boxed{
\begin{aligned}
\mathcal L
={}&
P_D
\left(
R_{q,q}R_{\alpha,\alpha}
-
R_{q,\alpha}R_{\alpha,q}
\right)
\\
&-
P_q
\left(
R_{q,D}R_{\alpha,\alpha}
-
R_{q,\alpha}R_{\alpha,D}
\right)
\\
&+
P_\alpha
\left(
R_{q,D}R_{\alpha,q}
-
R_{q,q}R_{\alpha,D}
\right).
\end{aligned}
}
\]

该式不需要假定任何 \(2\times2\) 子矩阵可逆。

---

## 7. 与沿 \(D\) 平衡路径求峰值的等价性

若局部平衡子 Jacobian

\[
K_{q\alpha}
=
\begin{bmatrix}
R_{q,q}&R_{q,\alpha}\\
R_{\alpha,q}&R_{\alpha,\alpha}
\end{bmatrix}
\]

可逆，则

\[
\begin{bmatrix}
dq/dD\\
d\alpha/dD
\end{bmatrix}
=
-
K_{q\alpha}^{-1}
\begin{bmatrix}
R_{q,D}\\
R_{\alpha,D}
\end{bmatrix}.
\]

沿平衡路径

\[
\frac{dP}{dD}
=
P_D
+
P_q\frac{dq}{dD}
+
P_\alpha\frac{d\alpha}{dD}.
\]

因此极限条件

\[
\frac{dP}{dD}=0
\]

等价于 bordered determinant

\[
\det J_{\lim}=0.
\]

正式理论采用 determinant 形式，因为它不需要额外假设 \(K_{q\alpha}\) 可逆。

---

## 8. 最终三元极限联立

最终未知量

\[
\boxed{
(D_u,q_u,\alpha_u).
}
\]

直接求解

\[
\boxed{
\begin{cases}
R_q(D,q,\alpha)=0,\\
R_\alpha(D,q,\alpha)=0,\\
\mathcal L(D,q,\alpha)=0.
\end{cases}
}
\]

得到

\[
(D_u,q_u,\alpha_u),
\]

最终

\[
\boxed{
P_u=P(D_u,q_u,\alpha_u).
}
\]

---

## 9. 当前门禁状态

\[
\boxed{
\texttt{NC\_M6\_FULL\_EXACT\_INTEGRATION\_REPRESENTATION = PASS}
}
\]

\[
\boxed{
\texttt{SAME\_SOURCE\_9\_DERIVATIVES = PASS}
}
\]

\[
\boxed{
\texttt{MOVING\_FRONT\_FIRST\_DERIVATIVE\_CANCELLATION = PASS}
}
\]

\[
\boxed{
\texttt{LIMIT\_DETERMINANT = READY}
}
\]

\[
\boxed{
\texttt{FINAL\_3EQ\_SYSTEM = READY}
}
\]

\[
\boxed{
\texttt{CASE21 = NOT\ RUN}
}
\]

下一步已不再是理论推导；若用户批准，可把 Case21 的几何/材料输入作为材料实例代入这套三函数，执行三元极限联立并与试验值比较。
