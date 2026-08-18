# NZ-SCCM Case21 concrete：厚度代数场到有限 Lauricella 闭合 R10

**日期：2026-08-19**  
**身份：EXACT-INTEGRATION BACKEND STEP / NO DISCRETIZATION / NO NEW MATERIAL THEORY**

## 0. 范围纪律

本文件不改变 R09 主线，不建立新材料函数，不重做 Nguyen、不重做极限联立。

唯一目标：对 R09 中 exact finite R10 连续积分，先处理 Case21 `k=1` 时固定 `(r,s)` 的**厚度积分**，证明它可以从有限代数 integrand 直接变成有限个成熟 Lauricella `F_D` 标准函数值，而不需要 Chebyshev 无穷材料级数，也不需要 Picard–Fuchs 作为第一选择。

---

# 1. R09 后的固定对象

R10 current operator 直接取 finite R10：

\[
\mathbf S=\mathcal M_{R10}(\mathbf E).
\]

Case21 `k=1` 对固定 `(r,s)`，厚度坐标 `zeta` 下有

\[
\mu_E=\mu_0+\mu_1\zeta,
\qquad
 d_E=d_0,
\qquad
E_{12}=h_0+h_1\zeta.
\]

因此

\[
r_E=\sqrt{d_0^2+(h_0+h_1\zeta)^2}.
\]

令

\[
y=h_0+h_1\zeta,
\qquad
t=y+\sqrt{y^2+d_0^2},
\]

则

\[
y=\frac{t^2-d_0^2}{2t},
\qquad
\sqrt{y^2+d_0^2}=\frac{t^2+d_0^2}{2t}.
\]

两个主材料坐标成为 Laurent-rational：

\[
\lambda_\pm
=\frac{A_\pm t^2+2c_0t+B_\pm}{2t}.
\]

R10 projector 中唯一剩余的标量根式满足

\[
\lambda_\pm^2+\eta^2
=\frac{Q_\pm(t)}{4t^2},
\]

其中 `Q_+`,`Q_-` 为至多四次多项式。

因此固定 `(r,s)`、固定原始材料分支后，任一厚度 integrand 属于

\[
\mathcal K
=K(t,\sqrt{Q_+(t)},\sqrt{Q_-(t)}).
\]

---

# 2. 有限基底，而不是无穷级数

由于两个 radical generator 都是二次扩张，任意 `F in K` 可有限表示成

\[
\boxed{
F(t)=R_0(t)
+R_+(t)\sqrt{Q_+(t)}
+R_-(t)\sqrt{Q_-(t)}
+R_{+-}(t)\sqrt{Q_+(t)Q_-(t)}
}
\]

其中 `R_*` 均为有理函数。

这已经给出厚度方向的固定四分量代数基；没有 `N`、没有 prefix、没有收敛问题。

---

# 3. 每一个代数微分都可有限归约为 Lauricella 型 Euler 积分

考虑上述四类中任一项。把其分子分母在复数域有限因式分解并做有限部分分式后，每一项均可写成有限线性组合：

\[
\boxed{
G(t)=C\,t^m\prod_{j=1}^{M}(t-\rho_j)^{\beta_j}
}
\]

其中：

- `m` 为整数；
- 来自 `sqrt(Q_+)`, `sqrt(Q_-)` 或 `sqrt(Q_+Q_-)` 的 `beta_j` 为半整数 `±1/2`；
- 来自有理分母极点的 `beta_j` 为负整数；
- 重根只改变有限指数，不引入无穷结构。

厚度区间的两个精确端点由 `zeta=-1,+1` 通过 rationalizing map 得到 `t0,t1`。令

\[
t=t_0+\Delta t\,u,
\qquad
\Delta t=t_1-t_0,
\qquad 0\le u\le1.
\]

则

\[
t-\rho_j=(t_0-\rho_j)\left(1-x_ju\right),
\qquad
x_j=-\frac{\Delta t}{t_0-\rho_j}.
\]

若 `t^m` 留作同类线性因子，亦写为

\[
t^m=t_0^m\left(1-x_0u\right)^m,
\qquad
x_0=-\frac{\Delta t}{t_0},
\]

特殊 `t0=0` 情形则直接并入 `u^m` 幂。

所以每一个厚度项都落到

\[
\boxed{
C_*\int_0^1
u^{a-1}(1-u)^{c-a-1}
\prod_{j=1}^{M_*}(1-x_ju)^{-b_j}
\,du
}
\]

的 Euler–Lauricella 形式。对通常的仿射厚度映射可取 `c=a+1`；若端点或分子产生额外 `(1-u)` 幂，则相应改变 `c-a-1`，仍属同一标准形式。

Lauricella 第四函数的 Euler 表示为

\[
\boxed{
\int_0^1
u^{a-1}(1-u)^{c-a-1}
\prod_{j=1}^{M}(1-x_ju)^{-b_j}\,du
=
B(a,c-a)
F_D^{(M)}(a;b_1,\ldots,b_M;c;x_1,\ldots,x_M)
}
\]

在基本收敛域成立，并由标准解析延拓定义其他参数域。

因此每一个固定 `(r,s)` 的厚度 exact integral 都是**有限个 Lauricella `F_D` 值的有限线性组合**。

---

# 4. 四类厚度项分别落在哪一层

## 4.1 `R0(t)`：纯有理项

有限部分分式后是：

- 多项式；
- `1/(t-rho)^k`；

所以直接得到初等函数（有理函数、对数），不需要 Lauricella。

## 4.2 `R+(t)sqrt(Q+)` 与 `R-(t)sqrt(Q-)`

`Q_±` 最多 quartic。因式分解后出现最多四个半整数指数因子，所以一般可写成有限个

\[
F_D^{(m)},\qquad m\le 4+N_{pole}
\]

的值；在 quartic genus-1 可约情形可进一步降为 Legendre/Carlson elliptic integrals。

## 4.3 `R+-(t)sqrt(Q+Q-)`

`Q_+Q_-` 最多 octic。一般出现最多八个半整数 branch factors，再加有限个有理极点，因此仍是有限维 Lauricella `F_D^{(m)}` Euler integral，不需要自造 hyperelliptic series。

该表达也可被称为标准 hyperelliptic Abelian integral；Lauricella 是其一种固定标准函数表示。

---

# 5. 这一步对 NZ-SCCM 的意义

原先厚度方向的概念是：

```text
finite R10
-> invent Chebyshev stream
-> n-th term D15
-> N->infinity
```

现在替换为：

```text
finite R10
-> exact rationalizing substitution
-> finite biquadratic algebraic basis
-> finite factorization / partial fractions
-> finite Lauricella / elliptic standard-function combination
```

因此厚度方向没有任何材料级数收敛门槛。

---

# 6. 不夸大当前完成度

本 R10 只关闭**固定 `(r,s)` 的厚度积分结构**。

执行厚度闭合后，`P_c(D,q,alpha)` 仍需对 `(r,s)` 做剩余的连续二维精确积分。由于 Lauricella 的参数/argument 本身依赖 `(r,s)`，不能未经证明就宣称外层二维积分也自动是同一个 `F_D`。

所以当前状态严格为：

```text
MATERIAL_SERIES_LAYER = REMOVED
THICKNESS_EXACT_STANDARD_FUNCTION_CLOSURE = PASS AT STRUCTURAL FORM LEVEL
OUTER_RS_EXACT_CLOSURE = OPEN
PICARD_FUCHS_REQUIRED_AT_THICKNESS_LEVEL = NO
```

---

# 7. 下一步保持窄范围

下一步只研究剩余 `(r,s)` 二维 exact integral 是否可通过：

1. Beta/Gamma；
2. Appell/Lauricella；
3. Carlson/elliptic symmetry；

直接关闭。

只有这三层均不能形成固定标准函数组合时，才考虑更一般 Abelian/GKZ/holonomic 后端。

不得因此改变 R10、Nguyen、极限联立，也不得恢复任何有限材料级数或离散验证。
