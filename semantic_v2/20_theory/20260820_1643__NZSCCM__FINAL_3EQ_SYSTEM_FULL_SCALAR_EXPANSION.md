# NZ-SCCM — 最终三元极限方程组的标量展开

时间：2026-08-20 16:43 +08:00

状态：`ACTIVE_DERIVATION / SCALAR_EXPANSION / NO_MATRIX_SHORTHAND`

## 0. 目的

将上一节点的最终系统

\[
R_A=0,\qquad R_m=0,\qquad \det J_{\lim}=0
\]

展开为无行列式缩写的三个标量方程，并进一步把 exact-period 有限和及其导数显式代入。

重要边界：本节点只是把已得到的 exact-period 形式代数展开。上一节点尚未把每个 `c_{j\nu}` 与每个 relative-GKZ 参数数组逐项编译成完整有限清单，因此本节点不能伪造不存在的逐项系数表。真正的“系数级完全展开”需要下一步对 CC/TC/CT/TT 的 exact integrands 做一次有限符号编译。

---

## 1. 去掉公共几何常数

定义

\[
K=4J_V=\frac{2b\ell h}{\pi^2}.
\]

写成

\[
R_A=K\,\widehat R_A,
\qquad
R_m=K\,\widehat R_m,
\qquad
P=K\,\widehat P.
\]

其中

\[
\widehat R_A=\sum_{\nu=1}^{N_A}a_\nu\,\mathfrak A_\nu,
\]

\[
\widehat R_m=\sum_{\nu=1}^{N_m}m_\nu\,\mathfrak M_\nu,
\]

\[
\widehat P=\sum_{\nu=1}^{N_P}p_\nu\,\mathfrak P_\nu.
\]

因为 `K` 对三个未知量 `(Delta,A,epsilon_m)` 为常数，所以平衡方程和极限条件中的公共 `K` 可全部约掉。

---

## 2. 第一方程：面外幅值平衡

\[
\boxed{
\sum_{\nu=1}^{N_A}a_\nu(\Delta,A,\varepsilon_m)\,
\mathfrak A_\nu(\Delta,A,\varepsilon_m)=0.
}
\]

这里的 `a_nu mathfrak A_nu` 是厚度 Euler 初等闭合后、板面 relative-GKZ exact-period 的有限项。

---

## 3. 第二方程：横向膜力平衡

\[
\boxed{
\sum_{\nu=1}^{N_m}m_\nu(\Delta,A,\varepsilon_m)\,
\mathfrak M_\nu(\Delta,A,\varepsilon_m)=0.
}
\]

---

## 4. 荷载函数

\[
\boxed{
P(\Delta,A,\varepsilon_m)
=K\sum_{\nu=1}^{N_P}p_\nu\,\mathfrak P_\nu.
}
\]

最终根求出后

\[
P_u=K\sum_{\nu=1}^{N_P}p_\nu(\mathbf q_u)\mathfrak P_\nu(\mathbf q_u).
\]

---

## 5. 所有一阶导数逐项展开

对任意 `g in {Delta,A,m}`，其中 `m` 代表 `epsilon_m`，定义

\[
\widehat R_{A,g}
=\sum_{\nu=1}^{N_A}
\left(a_{\nu,g}\mathfrak A_\nu+a_\nu\mathfrak A_{\nu,g}\right),
\]

\[
\widehat R_{m,g}
=\sum_{\nu=1}^{N_m}
\left(m_{\nu,g}\mathfrak M_\nu+m_\nu\mathfrak M_{\nu,g}\right),
\]

\[
\widehat P_{,g}
=\sum_{\nu=1}^{N_P}
\left(p_{\nu,g}\mathfrak P_\nu+p_\nu\mathfrak P_{\nu,g}\right).
\]

由于 `R_A=K Rhat_A`, `R_m=K Rhat_m`, `P=K Phat`，它们的实际导数都是上述量乘 `K`。

---

## 6. 第三方程：极限条件完全展开成六项

原 `det J_lim=0` 精确展开为

\[
\boxed{
\begin{aligned}
0={}&
P_{,\Delta}R_{A,A}R_{m,m}
-P_{,\Delta}R_{A,m}R_{m,A}\\
&-P_{,A}R_{A,\Delta}R_{m,m}
+P_{,A}R_{A,m}R_{m,\Delta}\\
&+P_{,m}R_{A,\Delta}R_{m,A}
-P_{,m}R_{A,A}R_{m,\Delta}.
\end{aligned}
}
\]

三个导数各自带 `K`，整体有公共 `K^3`，约掉以后：

\[
\boxed{
\begin{aligned}
0={}&
\widehat P_{,\Delta}\widehat R_{A,A}\widehat R_{m,m}
-\widehat P_{,\Delta}\widehat R_{A,m}\widehat R_{m,A}\\
&-\widehat P_{,A}\widehat R_{A,\Delta}\widehat R_{m,m}
+\widehat P_{,A}\widehat R_{A,m}\widehat R_{m,\Delta}\\
&+\widehat P_{,m}\widehat R_{A,\Delta}\widehat R_{m,A}
-\widehat P_{,m}\widehat R_{A,A}\widehat R_{m,\Delta}.
\end{aligned}
}
\]

---

## 7. 第三方程继续把所有 finite sums 代进去

令

\[
\mathcal P_g=\sum_{\nu=1}^{N_P}
\left(p_{\nu,g}\mathfrak P_\nu+p_\nu\mathfrak P_{\nu,g}\right),
\]

\[
\mathcal A_g=\sum_{\nu=1}^{N_A}
\left(a_{\nu,g}\mathfrak A_\nu+a_\nu\mathfrak A_{\nu,g}\right),
\]

\[
\mathcal M_g=\sum_{\nu=1}^{N_m}
\left(m_{\nu,g}\mathfrak M_\nu+m_\nu\mathfrak M_{\nu,g}\right).
\]

则第三式只是便于阅读地写成

\[
\mathcal P_\Delta\mathcal A_A\mathcal M_m
-\mathcal P_\Delta\mathcal A_m\mathcal M_A
-\mathcal P_A\mathcal A_\Delta\mathcal M_m
+\mathcal P_A\mathcal A_m\mathcal M_\Delta
+\mathcal P_m\mathcal A_\Delta\mathcal M_A
-\mathcal P_m\mathcal A_A\mathcal M_\Delta=0.
\]

完全不使用这些三字母缩写时，第一项例如是

\[
\left[\sum_{i=1}^{N_P}(p_{i,\Delta}\mathfrak P_i+p_i\mathfrak P_{i,\Delta})\right]
\left[\sum_{j=1}^{N_A}(a_{j,A}\mathfrak A_j+a_j\mathfrak A_{j,A})\right]
\left[\sum_{k=1}^{N_m}(m_{k,m}\mathfrak M_k+m_k\mathfrak M_{k,m})\right],
\]

第二项是

\[
-\left[\sum_{i=1}^{N_P}(p_{i,\Delta}\mathfrak P_i+p_i\mathfrak P_{i,\Delta})\right]
\left[\sum_{j=1}^{N_A}(a_{j,m}\mathfrak A_j+a_j\mathfrak A_{j,m})\right]
\left[\sum_{k=1}^{N_m}(m_{k,A}\mathfrak M_k+m_k\mathfrak M_{k,A})\right],
\]

第三项是

\[
-\left[\sum_{i=1}^{N_P}(p_{i,A}\mathfrak P_i+p_i\mathfrak P_{i,A})\right]
\left[\sum_{j=1}^{N_A}(a_{j,\Delta}\mathfrak A_j+a_j\mathfrak A_{j,\Delta})\right]
\left[\sum_{k=1}^{N_m}(m_{k,m}\mathfrak M_k+m_k\mathfrak M_{k,m})\right],
\]

第四项是

\[
+\left[\sum_{i=1}^{N_P}(p_{i,A}\mathfrak P_i+p_i\mathfrak P_{i,A})\right]
\left[\sum_{j=1}^{N_A}(a_{j,m}\mathfrak A_j+a_j\mathfrak A_{j,m})\right]
\left[\sum_{k=1}^{N_m}(m_{k,\Delta}\mathfrak M_k+m_k\mathfrak M_{k,\Delta})\right],
\]

第五项是

\[
+\left[\sum_{i=1}^{N_P}(p_{i,m}\mathfrak P_i+p_i\mathfrak P_{i,m})\right]
\left[\sum_{j=1}^{N_A}(a_{j,\Delta}\mathfrak A_j+a_j\mathfrak A_{j,\Delta})\right]
\left[\sum_{k=1}^{N_m}(m_{k,A}\mathfrak M_k+m_k\mathfrak M_{k,A})\right],
\]

第六项是

\[
-\left[\sum_{i=1}^{N_P}(p_{i,m}\mathfrak P_i+p_i\mathfrak P_{i,m})\right]
\left[\sum_{j=1}^{N_A}(a_{j,A}\mathfrak A_j+a_j\mathfrak A_{j,A})\right]
\left[\sum_{k=1}^{N_m}(m_{k,\Delta}\mathfrak M_k+m_k\mathfrak M_{k,\Delta})\right].
\]

六项之和等于零。

---

## 8. 最终三标量方程组

\[
\boxed{
\begin{cases}
\displaystyle
\sum_{\nu=1}^{N_A}a_\nu\mathfrak A_\nu=0,\\[4mm]
\displaystyle
\sum_{\nu=1}^{N_m}m_\nu\mathfrak M_\nu=0,\\[4mm]
\displaystyle
\widehat P_{,\Delta}\widehat R_{A,A}\widehat R_{m,m}
-\widehat P_{,\Delta}\widehat R_{A,m}\widehat R_{m,A}
-\widehat P_{,A}\widehat R_{A,\Delta}\widehat R_{m,m}
+\widehat P_{,A}\widehat R_{A,m}\widehat R_{m,\Delta}
+\widehat P_{,m}\widehat R_{A,\Delta}\widehat R_{m,A}
-\widehat P_{,m}\widehat R_{A,A}\widehat R_{m,\Delta}=0.
\end{cases}
}
\]

未知量严格只有

\[
(\Delta,A,\varepsilon_m).
\]

---

## 9. 当前尚未完成的唯一层级

必须区分：

1. `空间积分已表示为 exact standard-function sums`：已完成；
2. `最终三方程的标量结构展开`：本节点已完成；
3. `把每个 a_nu,m_nu,p_nu 与每个 mathfrak A/M/P 的具体参数逐项枚举出来`：尚未执行。

第三层不是新的理论问题，而是一次有限符号编译任务。只有完成该编译后，才能把上述 `Sigma_nu` 进一步替换成一条真正无求和号、无抽象 period 标签的长公式。不得在未编译前假装已经得到这份系数级公式。