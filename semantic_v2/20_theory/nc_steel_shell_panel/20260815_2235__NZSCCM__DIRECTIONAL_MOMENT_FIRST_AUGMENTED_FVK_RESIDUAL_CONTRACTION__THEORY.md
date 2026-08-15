# NZ-SCCM — 增广 FvK 的 directional moment-first 残量收缩理论

**Timestamp:** 2026-08-15 22:35 +08:00

## 1. 物理系统不变

固定单一完整面外半波、Nguyen 二阶运动学以及当前面内最小补全：

\[
\mathbf m=[c,p_{20},p_{02}]^T,
\qquad
R_q=R_c=R_{20}=R_{02}=0.
\]

本轮不增加任何新自由度，不修改 R10/N48/Cayley-Hamilton，不修改 General D15。

## 2. 旧实现为什么慢

冻结 current-map 可写成 Cayley-Hamilton 形式

\[
\mathbf S=A(K_1,K_2)\mathbf I+B(K_1,K_2)\mathbf Y.
\]

旧实现先构造

\[
S_{xx}=A+B Y_{xx},\qquad S_{yy}=A+B Y_{yy},
\]

再对每一个广义方向 `r` 构造完整系数场

\[
S_{xx}e_{x,r}+S_{yy}e_{y,r}+\cdots
\]

最后才调用 D15 moment contraction。

在 augmented state 中，N48 高阶尾项使 `A,B` 的 dense bounding box 已经较大；继续把它们逐个乘上 `Yxx,Yyy,e_r` 会产生不必要的额外 dense arrays 和 FFT/Laurent workspace。

## 3. directional moment-first 恒等重排

对任意 retained direction `r`，正应变部分为

\[
I_r=\int [S_{xx}e_{x,r}+S_{yy}e_{y,r}]\,dV.
\]

代入 `S=A I+B Y`：

\[
I_r=
\int A(e_{x,r}+e_{y,r})\,dV
+
\int B(Y_{xx}e_{x,r}+Y_{yy}e_{y,r})\,dV.
\]

因此不需要先生成 `Sxx,Syy`。只需要直接计算三个线性泛函：

\[
\mathcal M[A,W]=\int A W\,dV,
\]

\[
\mathcal M[B,Y_{xx}e_{x,r}],
\qquad
\mathcal M[B,Y_{yy}e_{y,r}].
\]

对于 q 方向再加 frozen Nguyen shear-square directional term

\[
\frac{1}{2(1+\nu)\,l_h}
\mathcal M[B,(\gamma^2)_{,q}].
\]

于是 concrete residual 统一为

\[
R_r=C_c\left\{
\mathcal M[A,e_{x,r}+e_{y,r}]
+
\mathcal M[B,Y_{xx}e_{x,r}+Y_{yy}e_{y,r}]
+
\delta_{rq}\frac{\mathcal M[B,(\gamma^2)_{,q}]}{2(1+\nu)l_h}
\right\},
\]

其中

\[
C_c=\frac{f_c\varepsilon_0 b\ell t_c}{2\pi^2}.
\]

轴力同理直接写为

\[
P_c=-\frac{f_cbt_c}{2\pi^2}
\left[\int A\,dV+\mathcal M[B,Y_{yy}]\right].
\]

## 4. Chebyshev coefficient exact product moment

若

\[
A=\sum a_{ijk}T_i(x_s)T_j(y_s)T_k(\eta),
\]

\[
W=\sum w_{pqr}T_p(x_s)T_q(y_s)T_r(\eta),
\]

使用

\[
T_m T_n=\tfrac12[T_{m+n}+T_{|m-n|}],
\]

则可以直接形成

\[
\mathcal M[A,W]
=\sum a_{ijk}w_{pqr}
M^{(x)}_{ip}M^{(y)}_{jq}M^{(z)}_{kr},
\]

其中

\[
M^{(x)}_{ip}=\tfrac12\left(\mu^{(x)}_{i+p}+\mu^{(x)}_{|i-p|}\right),
\]

其他方向同理，而 `mu` 正是 General D15 已采用的解析 Chebyshev moments。

因此该重排没有空间节点，也没有数值积分。

## 5. 为什么这属于同一 D15

Directional moment-first 只是利用线性积分泛函与乘法结合律：

```text
old: material pair -> full stress field -> multiply each virtual strain -> exact moment
new: material pair -> contract each low-order virtual strain directly -> exact moment
```

两者在代数上等价。改变的是求值顺序和中间表示，不是积分定义。

## 6. 当前边界

`DIRECTIONAL_MOMENT_FIRST_V1` 仍然保留 dense `buildS(K1,K2)`，因此并没有彻底消除 N48 的高阶 dense fill-in；它首先消除了 final stress materialization 和逐 residual 的 full-field multiplication。

这一步已经足以把 augmented D=.50、`tol=7e-7` 的单次求值带回当前执行窗口，并得到 parent-tolerance equilibrium certificate。

后续若 D continuation 再出现 runtime growth，可以继续把 `buildS` 内部改成 directional/streaming contraction；但不得为性能原因删掉 `p20,p02` 或改成空间 Gauss/points。