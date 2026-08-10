# NZ-SCCM PF1：genus-2 x-fiber Gauss–Manin closure R03

**日期：2026-08-10**  
**身份：CURRENT ANALYTIC ADVANCE — X-FIBER GAUSS–MANIN PASS / WHOLE-HALFWAVE GATE A STILL HOLD**

## 0. 执行边界

本轮严格继承 `governance/PF1_EXECUTION_BOUNDARY_LOCK_20260810.md`。PF1 只做 R02 hyperelliptic-relative outer period 的有限解析闭合，不修改任何基础结构身份：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT
ELEMENT_INTEGRATION = PROHIBITED
MATERIAL_POINT_GRID = PROHIBITED
SPATIAL_CELLS = PROHIBITED
```

结构目标仍为 `P(D,q), Rq(D,q)=0, L(D,q)=0`；材料主线仍为 M1R source-shaped analytic compiler。若 PF 路线失败，只报告 blocker，不改用空间 quadrature/cells/material points。

---

## 1. R02 的 canonical single-resolvent x-fiber

对一个 scalar pole `r`，R02 已得到：

```text
Gamma_r(x,y) = 4 x y disc_s[Delta_r(s)]
```

固定 `y,D,M,nu,r` 后，single-resolvent algebraic radical对应 genus-2 曲线：

\[
\boxed{\mathcal C_r:\quad w^2=P_r(x)=x(1-x)\Gamma_r(x,y)}.
\]

`Gamma_r` generically cubic in x，所以 `P_r` generically degree 5。只要 `Disc_x(P_r) != 0`，`C_r` 是 smooth genus-2 hyperelliptic curve。

采用 de-Rham basis：

\[
\boxed{\omega_k=\frac{x^k\,dx}{w},\qquad k=0,1,2,3.}
\]

其中 `omega_0,omega_1` 为 holomorphic 类；`omega_2,omega_3` 作为 second-kind representatives。absolute de-Rham rank 为 `2g=4`。

---

## 2. PF1 的核心有限 Hermite reduction

令一般 square-free degree-5 polynomial：

\[
P(x)=p_0+p_1x+\cdots+p_5x^5,
\qquad p_5\ne0,
\qquad w^2=P(x).
\]

对任一参数 `theta`（后续可取 `y,D,M,B,q` 等），

\[
\partial_\theta\omega_k
=-\frac12\frac{x^kP_{,\theta}}{w^3}\,dx.
\]

定义：

\[
Q_k^{(\theta)}=-\frac12x^kP_{,\theta}.
\]

寻找：

\[
S_k(x)=\sum_{j=0}^3 A_{kj}^{(\theta)}x^j,
\qquad
R_k(x)=\sum_{j=0}^4 b_{kj}^{(\theta)}x^j,
\]

满足精确 polynomial identity：

\[
\boxed{
Q_k
=S_kP+R_k'P-\frac12R_kP'.
}
\]

因为：

\[
d\left(\frac{R_k}{w}\right)
=\frac{R_k'P-\frac12R_kP'}{w^3}\,dx,
\]

所以：

\[
\boxed{
\partial_\theta\omega_k
=\sum_{j=0}^3A_{kj}^{(\theta)}\omega_j
+d\left(\frac{R_k}{w}\right).
}
\]

在闭 cycle `gamma` 上 exact term 消失：

\[
\boxed{
\partial_\theta\Pi=A_\theta\Pi,
\qquad
\Pi_k=\oint_\gamma\omega_k,
\qquad
\Pi=(\Pi_0,\Pi_1,\Pi_2,\Pi_3)^T.
}
\]

因此 single-resolvent **absolute algebraic x-fiber 已闭合为 rank-4 finite Gauss–Manin system**。

---

## 3. 为什么这个 9×9 reduction generically 一定可逆

未知量为：

```text
4 coefficients of S_k
+ 5 coefficients of R_k
= 9
```

匹配 `x^0 ... x^8` 的 9 个系数，形成有限矩阵 `H(P)`。

对 general degree-5 polynomial 直接计算可得：

\[
\boxed{
\det H(P)
=-\frac{p_5}{32}\operatorname{Disc}_x(P).
}
\]

因此：

```text
p5 != 0 and Disc_x(P) != 0
<=> Hermite/Gauss-Manin reduction is nonsingular.
```

这把 PF1 的 singular locus 精确定位为 hyperelliptic curve 的 discriminant locus，而不是空间积分点或数值网格问题。

正式判定：

```text
PF1_HERMITE_REDUCTION_MATRIX = PASS_EXACT
PF1_ABSOLUTE_X_FIBER_RANK = 4
PF1_GAUSS_MANIN_SINGULAR_LOCUS = Disc_x(P_r)=0
```

---

## 4. `0<x<1` 原积分如何对应闭 cycle

原 outer x 积分在一个 branch sheet 上沿 `x=0 -> 1`。由于 `0`、`1` 本身就是 `P_r=x(1-x)Gamma_r` 的 branch points，可在 hyperelliptic Riemann surface 上取绕 `[0,1]` branch cut 的闭 cycle `gamma_[0,1]`。

在 branch 不穿越且 `Gamma_r` 在路径上不触发 curve degeneration 的区域：

```text
closed-cycle period = 2 × one-sheet [0,1] integral
```

因此使用闭 cycle 不是改变结构域，更不是引入新空间子域；它只是同一个 definite integral 的解析延拓表示。它同时消除了 Hermite reduction exact-differential 的 endpoint ambiguity。

---

## 5. R02 exact witness 的完整 y-connection

继续采用 R02 的 exact rational witness：

```text
D=1
M=1
nu=1/5
r=2
```

保留 y 为连续参数。此时：

\[
\Gamma(x,y)=\frac1{25}\{
25x^3y+50x^2y^2-340x^2y+180x^2
+25xy^3-340xy^2+1156xy-720x
+300y^2-840y+540
\}.
\]

\[
P(x,y)=x(1-x)\Gamma(x,y).
\]

其 x-discriminant 精确为：

\[
\boxed{
\operatorname{Disc}_xP
=\frac{6912}{244140625}
 y^2(y-1)^3(5y-9)^4(5y+1)^4Q_5(y)
}
\]

其中：

\[
Q_5(y)=1000y^5-21150y^4+68295y^3-128087y^2+120480y-43200.
\]

`Q5` 的唯一实根约为：

```text
17.67462830261443
```

其余 4 根为两对 complex conjugates；另外 algebraic singularities `-1/5` 与 `9/5` 均不在 `(0,1)`。

所以在这个 nondegenerate witness 中：

\[
\boxed{
\operatorname{Disc}_xP(y)\ne0\quad\forall y\in(0,1).
}
\]

即整个 interior y-path 上 genus-2 x-fiber 不发生 degeneration。

由 4 次 exact Hermite reduction 得到 rational `4×4` connection：

\[
\boxed{\frac{d\Pi}{dy}=A_y(y)\Pi.}
\]

16 个 entry 的共同 denominator 可取：

\[
\boxed{
10y(y-1)(5y-9)(5y+1)Q_5(y).
}
\]

因此 witness 的 `A_y` 在 `(0,1)` interior 无 pole；`y=0,1` 是原 Beta/branch endpoints，不是新增空间 subdivision front。

在 `y=1/3`，exact connection matrix 为：

\[
A_y(1/3)=
\begin{bmatrix}
-38132487/7289728 & 6258486309/641496064 & -3839490225/1282992128 & -700895025/1282992128\\
-46726335/7289728 & 7173049869/641496064 & -365375115/116635648 & -771413625/1282992128\\
-51427575/7289728 & 8179278645/641496064 & -515763747/116635648 & -229036545/1282992128\\
-15269103/7289728 & -37429324783/3207480320 & 13065912729/583178240 & -9659333577/1282992128
\end{bmatrix}.
\]

配套脚本对四个 basis derivative 的 polynomial identity 全部 exact check 为 `True`。

正式判定：

```text
PF1_WITNESS_Y_GAUSS_MANIN = PASS_EXACT
PF1_WITNESS_INTERIOR_Y_DEGENERATION = NONE
PF1_WITNESS_CONNECTION_DIMENSION = 4
```

---

## 6. log/atanh endpoint 项：有限 relative extension，不需要改路线

R02 的 quadratic s-antiderivative 除 algebraic part 外还出现：

```text
coefficient / sqrt(Gamma_r)
× log(algebraic endpoint function F_r)
```

定义 log-weighted periods：

\[
\Lambda_k=\oint_\gamma \omega_k\log F_r.
\]

由 absolute reduction：

\[
\partial_\theta\omega_k
=\sum_jA_{kj}\omega_j+d\phi_k,
\qquad \phi_k=R_k/w,
\]

可得：

\[
\boxed{
\partial_\theta\Lambda_k
=\sum_jA_{kj}\Lambda_j
+\oint_\gamma\omega_k\,\partial_\theta\log F_r
-\oint_\gamma\phi_k\,d_x\log F_r
+\text{finite monodromy data}.
}
\]

后两项都是同一 genus-2 curve 上、只在 `F_r` 的有限 zero/pole divisor 及已有 discriminant divisor 处有 pole 的 meromorphic algebraic differentials。

因此它们属于有限维 punctured/relative de-Rham space；不会重新产生无限材料点状态，也不需要空间分区。log branch 的变化由有限 monodromy/branch data 管理。

当前只允许判定：

```text
PF1_RELATIVE_LOG_EXTENSION = FINITE-STRUCTURE PASS
PF1_RELATIVE_LOG_PRODUCTION_EVALUATOR = NOT_YET_COMPLETE
```

即：已证明不会因 log 项导致无限维或改变主线，但还没有把所有 actual M1R log divisors 编译成最终统一 connection matrix。

---

## 7. pair-resolvent 不提高 genus

R02 已有：

\[
\frac{N(s)}{\Delta_r(s)\Delta_t(s)}
=\frac{A_r(s)}{\Delta_r(s)}+\frac{A_t(s)}{\Delta_t(s)}
\]

（resultant 非零；退化时取 confluent analytic limit）。

所以 pair block 的 transcendental part 只是 `r`、`t` 两个 single quadratic families 的有限和。Bezout/resultant coefficients 只增加 rational meromorphic divisors，不产生 quartic-root curve，也不形成新的 genus >2 root family。

正式判定：

```text
PF1_PAIR_BLOCK_GENUS_ESCALATION = NO
PF1_PAIR_TO_SINGLE_RELATIVE_FAMILIES = PASS_EXACT
```

---

## 8. PF1 到这里解决了什么、还没解决什么

已经完成：

```text
R02 genus-2 classification
-> rank-4 de-Rham basis
-> finite 9x9 Hermite reduction
-> Gauss-Manin connection in any parameter off discriminant locus
-> exact y-connection witness
-> finite relative-log extension proof
-> pair blocks do not increase root genus
```

因此“hyperelliptic 太复杂，所以必须回到数值空间积分”这一担忧被排除：至少 x-fiber 已严格形成有限解析 differential system。

但 whole-halfwave Gate A 仍不能提前 PASS，因为原二维 period 还有最后一层：

```text
y-weighted pushforward / elimination
```

必须把：

\[
\int_0^1 \frac{\Pi(y)}{\sqrt{y(1-y)}}\,dy
\]

以及 relative-log extension 对 y 的积分，进一步消成 **不再保留空间 y-integral 的有限 Picard–Fuchs/creative-telescoping object**。不能把“数值求解 y-ODE”直接当作原空间积分的替代物。

因此：

```text
PF1_ABSOLUTE_X_FIBER = PASS_EXACT
PF1_RELATIVE_STRUCTURE = PASS_FINITE_STRUCTURE
PF1_PAIR_GENUS_CONTROL = PASS_EXACT
PF1_Y_PUSHFORWARD = NOT_YET_ELIMINATED
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

---

## 9. 下一唯一任务：PF2 whole-halfwave pushforward

下一步保持同一主线：

```text
PF2
= y-direction creative telescoping / relative Gauss-Manin pushforward
```

目标：

1. 以 current x-fiber finite connection 为输入；
2. 加入 Beta weight `y^(-1/2)(1-y)^(-1/2)`；
3. 对 actual single/log/pair canonical families 构造 finite telescoper；
4. 把 y 定积分消成 external parameters `(D,q,r,...)` 的有限 differential system/period object；
5. 明确 endpoint/branch/monodromy initial data；
6. 证明 `D,q` derivative 可在同一 finite system 内获得；
7. 只有这一步成功后，才讨论 `FORMAL_WHOLE_HALFWAVE_GATE_A = PASS_CLASS_B`。

Fail-fast：若 PF2 无法在锁定边界下闭合，则停止并报告 exact blocker；不允许更换为空间 numerical quadrature/cells/material points，也不允许修改 `P,Rq,L` 或降低材料非线性。

---

## 10. 本轮未执行

```text
NO Case21 Pu solve
NO Swartz24 solve
NO material refit
NO UHPC production fit
NO shell/Y production solve
NO spatial numerical quadrature
NO material-point integration
```
