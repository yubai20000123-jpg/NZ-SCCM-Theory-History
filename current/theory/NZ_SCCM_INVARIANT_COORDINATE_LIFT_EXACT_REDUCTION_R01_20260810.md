# NZ-SCCM 不变量坐标升维/降维解析化审计 R01

**日期：2026-08-10**  
**身份：CURRENT MATHEMATICAL ROUTE / EXACT TRANSFORMATION CANDIDATE**

## 0. 背景

用户提出：既然原三重空间积分对强非线性材料很困难，是否可以通过四重甚至更高重积分，从更高维度把复杂复合关系变简单。

本文件正式把这一想法纳入 NZ-SCCM 数学主线。核心判断不是“积分维数越高越先进”，而是：

> 是否存在**辅助变量 / 不变量坐标 / pushforward measure**，使原本难处理的材料非线性在更高维表示中变成低阶代数、可分离核或可精确消元的积分。

正式边界不变：

```text
NO ELEMENT INTEGRATION
NO SPATIAL QUADRATURE
NO MATERIAL-POINT GRID
ONE CONTINUOUS COMPLETE HALFWAVE
```

允许临时引入辅助积分变量，但最终 production formula 必须满足：

```text
AUXILIARY INTEGRALS = ANALYTICALLY ELIMINATED OR FINITE CLOSED SPECIAL FUNCTIONS
NUMERICAL QUADRATURE OVER AUXILIARY VARIABLES = PROHIBITED IN FORMAL OPERATOR
```

---

## 1. “升维”在数学上能做什么

### 1.1 Laplace / Gamma lift

对正量 Q，可用 Gamma/Laplace integral representation 把负幂变成辅助参数积分，例如

\[
Q^{-\alpha}=\frac1{\Gamma(\alpha)}\int_0^\infty t^{\alpha-1}e^{-tQ}\,dt.
\]

这会把一个含分母的三重积分变成四重积分。

优点：分母消失。

缺点：若 Q 是 Case21 的三角—厚度多项式，空间 integrand 变成 `exp(-t Q)`，通常不再属于有限 D15 polynomial moment algebra。因此**仅仅增加 t 维并没有自动解决问题**。

### 1.2 auxiliary-field / Hubbard-Stratonovich 类 lift

平方非线性可通过 Gaussian auxiliary field 线性化。这类变换在多体理论中非常有效，因为升维后可利用 Gaussian structure。

对 NZ-SCCM 的必要条件是：升维后的空间变量依赖必须变成可精确解析积分的 Gaussian/Bessel/hypergeometric kernel；否则只把原困难移到了新变量。

### 1.3 algebraic variable + delta constraint

例如对

\[
r=\sqrt{g(X,Y,z)}
\]

可引入独立 r 并写成带 `delta(r^2-g)` 的四重积分。形式上根号从 integrand 中消失，但约束曲面仍携带原来的代数复杂度；若 level-set geometry 没有变简单，这种 lift 是同义改写而不是求解。

### 1.4 coarea / pushforward representation

对材料不变量映射

\[
\Phi:\Omega^3\to\mathbb R^2,
\qquad
\Phi=(I_1,I_2),
\]

定义 joint pushforward density

\[
\rho_{D,q}(s,t)
=\int_{\Omega}
\delta(s-I_1)\delta(t-I_2)\,dV.
\]

于是任意只依赖材料不变量的积分可写成

\[
\boxed{
\int_\Omega F(I_1,I_2)\,dV
=\iint F(s,t)\rho_{D,q}(s,t)\,dsdt
}.
\]

这可以理解为先写成五重 delta-lift，再利用 coarea/pushforward 消元到二维材料空间。

潜在优势：**强材料非线性 F 与几何/运动学密度 rho 分离**。

真正困难：一般 analytic/polynomial map 的 pushforward density 存在 Jacobian singularities 和复杂 fiber geometry；现代数学可研究其 integrability/regularity，但一般没有自动的初等闭式。

---

## 2. Case21 出现一个比一般 coarea 更强的特殊结构

从当前已证明的不变量：

令

\[
u=\sin X,\qquad v=\sin Y,\qquad z=\zeta,
\]

\[
H=u^2+v^2-2u^2v^2,
\qquad
K=\nu u^2-v^2+(1-\nu)u^2v^2,
\]

\[
M=C_m(q),\qquad B=C_b(q).
\]

则

\[
I_1=(\nu-1)D+MH+2Buvz.
\]

定义

\[
\boxed{
a(u,v)=(\nu-1)D+MH
}
\]

所以

\[
\boxed{I_1=a+2Buvz}.
\]

**因此 I1 对厚度坐标 z 是严格 affine。**

这使我们不需要先做一般五维 coarea，而可以直接把第三个空间坐标换成材料坐标：

\[
\boxed{s=I_1}.
\]

当 `Buv != 0`：

\[
\boxed{
z=\frac{s-a}{2Buv},
\qquad
dz=\frac{ds}{2Buv}.
}
\]

区间端点：

\[
\boxed{s_\pm=a\pm2Buv}.
\]

`u=0` 或 `v=0` 是 measure-zero 退化边界；生产公式取连续极限。`B=0` 对应 q=0 的独立退化状态，应单独取极限而不是数值除零。

---

## 3. I2 在新坐标 s=I1 下只变成二次多项式

原式：

\[
\begin{aligned}
I_2={}&-\nu D^2+DMK+BD(\nu-1)uvz\\
&+BMuvz(2-u^2-v^2)\\
&+B^2z^2(u^2+v^2-1).
\end{aligned}
\]

利用

\[
uvz=\frac{s-a}{2B}
\]

和

\[
B^2z^2=\frac{(s-a)^2}{4u^2v^2},
\]

得到**严格恒等式**：

\[
\boxed{
\begin{aligned}
I_2(s;u,v)={}&-\nu D^2+DMK\\
&+\frac{D(\nu-1)}2(s-a)\\
&+\frac M2(2-u^2-v^2)(s-a)\\
&+\frac{u^2+v^2-1}{4u^2v^2}(s-a)^2.
\end{aligned}
}
\]

所以固定 `(u,v,D,q)` 时：

\[
\boxed{I_2=\alpha_0(u,v)+\alpha_1(u,v)s+\alpha_2(u,v)s^2}.
\]

这一步已经用独立 SymPy substitution 做 exact identity check。

### 3.1 一个重要现象

显式 `B` 从 `I2(s;u,v)` 的系数中消失；B 只通过积分区间

\[
[s_-,s_+]
\]

控制当前厚度扫过的 I1 范围。

这说明弯曲幅值的一个主要作用可以被解释为：

> 在固定 `(u,v)` 上改变材料不变量 I1 的穿越区间，而 I2 沿该区间按固定二次轨道演化。

这是新的材料—结构几何解释。

---

## 4. 原三重积分的精确材料坐标变换

因为当前所有目标 integrand 在 X/Y 方向只依赖 `u=sin X,v=sin Y`，有

\[
\int_0^\pi f(\sin X)dX
=2\int_0^1\frac{f(u)}{\sqrt{1-u^2}}du.
\]

因此

\[
\mathscr M[F]
=4\int_0^1\int_0^1
\frac{du\,dv}{\sqrt{1-u^2}\sqrt{1-v^2}}
\int_{-1}^{1}F\,dz.
\]

再换元 `s=I1`：

\[
\boxed{
\mathscr M[F]
=\frac{2}{B}
\int_0^1\int_0^1
\frac{1}{uv\sqrt{1-u^2}\sqrt{1-v^2}}
\left[
\int_{s_-}^{s_+}
F\big(s,I_2(s;u,v),u,v\big)\,ds
\right]du\,dv
}
\]

（对 `B>0`；一般写 `|B|` 并保持方向一致）。

这不是 numerical integration proposal，而是一个 exact coordinate transformation。

形式上的 `1/(uv)` 在 u/v->0 时由 `[s_-,s_+]` 同时收缩而消去，需在最终公式中使用连续极限。

---

## 5. 为什么这一变换对强非线性 rational material 特别重要

假设新材料 scalar functions 使用有限低参数有理形式：

\[
A(I_1,I_2)=\frac{P_A(I_1,I_2)}{Q_A(I_1,I_2)},
\qquad
B_m(I_1,I_2)=\frac{P_B(I_1,I_2)}{Q_B(I_1,I_2)}.
\]

由于 `I2(s;u,v)` 对 s 只有二次，而所有 structural weights `Xyy, I1_q, Gq` 在换元后也是 s 的有限有理/多项式表达，因此固定 `(u,v)` 时：

\[
\boxed{
P\text{ 和 }Rq\text{ 的材料方向 integrand 是 }s\text{ 的 rational function}
}
\]

有限有理函数对 s 可通过 Hermite reduction / partial fractions **精确积分**，结果为有限代数项、log、atan/atanh 等，不需要 s-quadrature。

因此：

\[
\boxed{
\text{strong rational material nonlinearity does not automatically require high-degree polynomial expansion}
}
\]

至少有一整个“厚度/材料不变量方向”可以精确消去。

---

## 6. 一个具体强非线性例子：Saenz 型 rational primitive

考虑

\[
R(s)=\frac{\kappa s}{1+a s+s^2},
\qquad a=\kappa-2.
\]

当 `4-a^2>0`，一个显式原函数为

\[
\boxed{
\mathcal R(s)
=\frac\kappa2\ln(s^2+a s+1)
-\frac{\kappa a}{\sqrt{4-a^2}}
\arctan\left(\frac{2s+a}{\sqrt{4-a^2}}\right)
}
\]

且

\[
\mathcal R'(s)=R(s).
\]

因此若某一材料 primitive 直接作用于 affine invariant `s=I1`，则

\[
\boxed{
\int_{-1}^{1}R(a+c z)\,dz
=\frac{\mathcal R(a+c)-\mathcal R(a-c)}{c}
}
\]

完全闭式；`c->0` 连续极限为 `2R(a)`。

这说明“强峰值/峰后 rational curve”与“解析积分”并不天然冲突。

---

## 7. 这是不是已经解决全部三重积分？

**没有。**

当前只证明：

1. material nonlinear direction 可利用 `s=I1` 精确消去一维；
2. rational `A/B` 在该方向不需要高阶 polynomial surrogate；
3. 剩余是 `(u,v)` 二维 weighted analytic integral，其中会出现 s-antiderivative 在 `s_±=a±2Buv` 的边界值。

这些边界值可能包含：

- algebraic roots；
- log；
- atan/atanh；
- 更一般情况下的 elliptic / hypergeometric functions。

所以后续仍必须证明**剩余二维积分也能解析闭合**。

---

## 8. 更高维方法的正式 Gate

今后任何 4D/5D/auxiliary-integral 路线都按以下规则审计。

### H4-PASS 条件

升维后必须至少满足一种：

1. 辅助变量可在符号上完全消元；
2. 每一维都能按 Beta/Gamma/elementary/specified special-function closed form 完成；
3. 最终只有有限 named special functions，且可解析求导形成 tangent；
4. 不存在 auxiliary numerical quadrature；
5. 不依赖空间 sampling / cells / material points。

### H4-FAIL 条件

若只是

```text
3D hard integral
-> introduce t
-> 4D integral
-> numerical quadrature in t
```

则对 NZ-SCCM 正式理论没有意义，判 FAIL。

---

## 9. 解析函数复杂度分级

为兼顾可计算性与人工审计，建议：

### Class A — 首选

- finite polynomial/rational algebra；
- Beta/Gamma；
- log / atan / atanh；
- finite radicals with explicit real branch control。

### Class B — 可研究

- elliptic integrals；
- Appell / generalized hypergeometric；
- Meijer-G / GKZ-hypergeometric periods；

前提是有限、可稳定求值、可解析求导、来源明确。

### Class C — 不允许作为正式闭合

- unevaluated auxiliary integrals；
- black-box CAS Integral object；
- adaptive quadrature；
- Monte Carlo / sparse grid / cubature。

---

## 10. 与现代多重积分理论的关系

多维积分本身并不是近年才出现；现代进展主要是把复杂积分识别为 integral transforms、periods、hypergeometric/GKZ systems、coarea/pushforward measures，并通过 auxiliary parameters、symmetry 与 algebraic geometry 改写其结构。

本路线后续参考：

- NIST DLMF §1.14 integral transforms；§5.9 Gamma/Laplace-type integral representations；§16.15 two-variable Appell integral representations；
- Panzer (2015), *Feynman integrals and hyperlogarithms*：Schwinger parameters 与多变量解析积分算法；
- de la Cruz (2019), *Feynman integrals as A-hypergeometric functions*：parametric integrals 与 GKZ systems；
- Negro (2021), *Sample distribution theory using Coarea Formula*：coarea 下 pushforward density；
- Glazer, Hendel, Sodin (2022), *Integrability of pushforward measures by analytic maps*：analytic-map pushforward density 的 integrability/singularity structure。

这些文献只作为数学工具来源，不改变 NZ-SCCM 的结构或材料物理。

---

## 11. 当前推荐路线

M1-R01 simple additive polynomial 已 FAIL-screen。新的最高优先级改为：

\[
\boxed{
\text{M1R rational/algebraic source-shaped material}
+\text{ invariant coordinate }s=I_1
+\text{ exact inner elimination}
}
\]

下一步不是直接做四维数值积分，而是：

1. 选择一个真正具有 compression peak/postpeak + tension + TC/CC 的低参数 rational/invariant material prototype；
2. 对 `P`、`Rq` 分别执行 `s=I1` 的 exact rational integration；
3. 检查剩余 `(u,v)` 二维 integrals 是否落入 Class A 或有限 Class B；
4. 若能闭合，再做材料级 Gate B；
5. 若剩余二维仍不可接受，再测试 joint pushforward/coarea 或 GKZ/Appell special-function route；
6. 全过程禁止用结构 Pu 反标材料。
