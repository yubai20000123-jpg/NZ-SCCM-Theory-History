# NZ-SCCM — NC-M6 普适系数编译原则与“板面双重解析积分”术语修正 V6

时间：2026-08-21

状态：
`PARAMETRIC_COEFFICIENT_RULES / NO_HARDCODED_MATERIAL_DECIMALS / NC_M6_PATH_UNCHANGED / THICKNESS_EXACT / SURFACE_DOUBLE_INTEGRAL_REMAINS`

## 1. 本节点纠正

此前 V5 的 exact-thickness engine 为了忠实保持当前冻结 NC-M6，将 T2/T4 的有限十进制直接写入代码。该做法适用于“当前固定材料实例”，但不适合作为普适理论编译器。

V6 将正式规则改为：

\[
\boxed{
\text{材料常数和分段曲线系数作为输入参数；程序只保存系数生成原则。}
}
\]

因此不在 universal compiler 内硬编码：

- \(a_{cc}\)；
- \(a_t\)；
- T2/T4 的具体小数；
- Case21 的任何材料数值；
- 任一板的几何数值。

当前冻结 NC-M6 的具体数字以后应作为“material instance / data contract”单独输入，而不是写死在解析引擎里。

## 2. 分段多项式的统一系数生成原则

对任意材料分段，采用局部变量

\[
\xi_T=\frac{r-a}{h},
\]

局部多项式

\[
T(r)=\sum_{n=0}^{N}c_n\xi_T^n.
\]

若希望展开成

\[
T(r)=\sum_{m=0}^{N}t_m r^m,
\]

则所有全局系数统一由

\[
\boxed{
t_m=
\sum_{n=m}^{N}
c_n
\binom{n}{m}
\frac{(-a)^{n-m}}{h^n}.
}
\]

产生。

这就是 T1/T2/T3/T4/T5 各段“巨大展开系数”的普适来源。

因此正式解析引擎只需要保存：

\[
(a,h,c_0,\ldots,c_N)
\]

以及上面的变换规则。

具体 NC-M6 当前冻结值属于材料实例层，不属于公式编译层。

## 3. 材料派生参数也只保存计算规则

由原始材料输入

\[
E_0,\quad f_c,\quad f_t,\quad \varepsilon_{c0}
\]

计算

\[
\boxed{
\kappa=\frac{E_0\varepsilon_{c0}}{f_c},
\qquad
\rho=\frac{f_t}{f_c},
\qquad
x_{cr}=\frac{f_t}{E_0\varepsilon_{c0}}.
}
\]

不存某个算例的数值。

## 4. 二次扩张的普适规则

所有材料 branch 最终都在

\[
R^2=Q
\]

下写成

\[
A+BR.
\]

乘法统一为

\[
\boxed{
(A+BR)(C+DR)
=
(AC+BDQ)+(AD+BC)R.
}
\]

任意多项式、八次 interaction、compression 共轭有理化均由此规则生成，不保存 branch-specific 数字表。

## 5. “二维”术语的纠正

此前所说“二维 exact-period”容易被理解成：

- 二维材料本构；
- 二维有限元；
- 二维网格。

都不是。

原始结构积分是三重空间积分：

\[
\int_0^b\int_0^\ell\int_{-t_r/2}^{t_r/2}
(\cdots)\,dz\,dy\,dx.
\]

厚度 \(z\) 或 \(\zeta\) 已经通过 Euler 有理化精确积分后，剩下的是板中面两个空间方向 \(x,y\) 的双重积分：

\[
\boxed{
\int_0^b\int_0^\ell
\mathcal T(x,y;D,q,\alpha)\,dy\,dx.
}
\]

或者无量纲形式

\[
\boxed{
\int_0^\pi\int_0^\pi
\mathcal T(X,Y;D,q,\alpha)\,dY\,dX.
}
\]

半角变换后则是

\[
\boxed{
\int_0^\infty\int_0^\infty
\mathcal T(\xi,\eta;D,q,\alpha)\,d\eta\,d\xi.
}
\]

所以以后不再简称“二维积分”，统一称为：

\[
\boxed{\text{板面双重解析积分}}
\]

或

\[
\boxed{\text{remaining surface double integral}}.
\]

它仍然发生在一个连续完整半波上：

\[
N_{\text{formal spatial sampling}}=0,
\]

\[
N_{\text{formal spatial quadrature}}=0,
\]

\[
N_{\text{formal spatial subdomains}}=1.
\]

## 6. 当前积分进度的准确表述

厚度方向：

\[
\boxed{
\int d\zeta
\ \text{已经被精确 Euler 有理化并可构造原函数。}
}
\]

剩余：

\[
\boxed{
\int\!\!\int dX\,dY
}
\]

即板面双重解析积分。

它不是新的理论层，而只是原三重积分在先消去厚度变量后的剩余两个空间积分变量。

只有板面双重解析积分也变成可直接评价的 closed function 后，才真正得到

\[
P(D,q,\alpha),\quad
R_q(D,q,\alpha),\quad
R_\alpha(D,q,\alpha),
\]

随后才进入极限条件和联立求解。
