# NZ-SCCM M1R outer resolvent / hyperelliptic classification R02

**日期：2026-08-10**  
**身份：CURRENT ANALYTIC CLASSIFICATION — EXACT RESOLVENT REDUCTION PASS / WHOLE-HALFWAVE GATE A STILL HOLD**

## 0. 本轮任务

承接 R01 的当前停点：

```text
M1R_R01_S_INNER_INTEGRATION = PASS_CLASS_A
M1R_R01_OUTER_XY = CLASS_B_CANDIDATE / NOT_YET_CLOSED
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

本轮不计算 Case21 Pu，不重新拟合材料；唯一任务是对 **actual M1R factor family** 做进一步精确结构化：

```text
actual 1D rational primitives
-> scalar pole / resolvent decomposition
-> invariant matrix resolvent blocks
-> exact s-factor classification
-> exact endpoint algebra
-> outer (x,y) algebraic-period genus classification
```

正式边界不变：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
NO element integration
NO material-point grid
```

---

## 1. R01 五个 rational primitive 有一个更强的共同结构

R01 的五个 scalar primitives：

```text
U, C, C2, T, V
```

其 numerator degree 与 denominator degree 相同：

| primitive | denominator degree |
|---|---:|
| U | 4 |
| C | 4 |
| C2 | 4 |
| T | 10 |
| V | 5 |

所以每个 primitive 都可严格写成：

\[
\boxed{
r_f(\lambda)=c_f+\sum_{j=1}^{d_f}\frac{\rho_{fj}}{\lambda-r_{fj}}
}
\]

其中 `r_fj` 是 scalar denominator 的根。

R01 固定系数的 pole audit：

- U：4 个 simple complex poles；
- C：4 个 simple complex poles；
- C2：4 个 simple complex poles；
- T：10 个 simple complex poles；
- V：4 个 complex poles + 1 个 real pole；
- 唯一 real pole 为 `1.9861419915007628`，仍高于当前材料诊断区间上界 `0.731707317...`；
- 各 primitive 内部最小 pole separation 均非零。

因此 actual R01 primitive 不需要按高阶 denominator 整体进入矩阵函数；可先做 **finite scalar partial-fraction decomposition**。

---

## 2. 单 pole 的二维 matrix resolvent 完全闭式

令归一化二维应变张量为 \(\mathbf X\)，不变量：

\[
I_1=\operatorname{tr}\mathbf X,\qquad
I_2=\det\mathbf X.
\]

对一个 scalar pole \(r\)，定义：

\[
\mathbf R_r=(\mathbf X-r\mathbf I)^{-1}.
\]

二维 Cayley–Hamilton 给出：

\[
\boxed{
\mathbf R_r
=
\frac{(I_1-r)\mathbf I-\mathbf X}
{\Delta_r}
}
\]

其中：

\[
\boxed{
\Delta_r=I_2-rI_1+r^2.
}
\]

“交换主方向”的 `oth` operator 同样有极简式：

\[
\boxed{
\mathbf R_r^{\rm oth}
=
\frac{\mathbf X-r\mathbf I}{\Delta_r}.
}
\]

这两个式子完全避免在结构域逐点求 principal eigenvectors。

---

## 3. source-shaped interaction 只产生二体 resolvent block，不产生三体及更高乘积

R01 source algebra：

\[
\widehat{\boldsymbol\sigma}
=
U(\mathbf X)
-a_{cc}C_2(\mathbf X)C^{\rm oth}(\mathbf X)
+C(\mathbf X)T^{\rm oth}(\mathbf X)
-\rho a_t T(\mathbf X)V^{\rm oth}(\mathbf X).
\]

由于每个 primitive 是：

```text
constant + finite sum of single resolvents
```

所以整个 M1R stress 精确落到：

```text
constant block
+ single-resolvent blocks
+ pair-resolvent blocks
```

不存在 triple-resolvent / higher product。

对一对 poles \(r,t\)：

\[
\boxed{
\mathbf R_r\mathbf R_t^{\rm oth}
=
\frac{
[I_2-t(I_1-r)]\mathbf I+(t-r)\mathbf X
}{
\Delta_r\Delta_t
}.
}
\]

该恒等式已由 Cayley–Hamilton basis multiplication 独立 exact check。

R01 的 raw pair counts：

```text
C2 x C^oth : 4 x 4   = 16
C  x T^oth : 4 x 10  = 40
T  x V^oth : 10 x 5  = 50
TOTAL PAIR BLOCKS     = 106
```

五个 primitive 总 scalar poles = 27。把同一 pole 上不同 single contributions 合并后，整个 stress 最多为：

```text
1 constant
+ 27 consolidated single-pole blocks
+ 106 pair-pole blocks
= 134 finite complex blocks
```

共轭项可在 real implementation 中成对合并；134 是解析分类计数，不是空间自由度，也不是材料点数。

---

## 4. 这使 R01 的 s-inner 结论进一步加强

Case21 exact coordinate：

\[
s=I_1.
\]

对每个 pole：

\[
\Delta_r(s)=I_2(s)-rs+r^2.
\]

因为 `I2(s)` 对 s 严格二次，所以：

\[
\boxed{\deg_s\Delta_r=2.}
\]

因此：

### single block

\[
\frac{N(s)}{\Delta_r(s)}
\]

### pair block

\[
\frac{N(s)}{\Delta_r(s)\Delta_t(s)}
\]

其中：

- P 的 single numerator 至多一次；
- Rq 的 single numerator 至多二次；
- P 的 pair numerator 至多二次；
- Rq 的 pair numerator 至多三次。

所以 pair block 虽然总 denominator degree 为 4，但 **无需求 quartic roots**。它保持两个已知 quadratic factors；可用 factor-aware Bezout / partial fraction：

\[
\frac{N}{\Delta_r\Delta_t}
=
\frac{A_r(s)}{\Delta_r}
+
\frac{A_t(s)}{\Delta_t},
\]

或在 resultant 接近退化时使用解析 confluent limit。

因此 R01 中“quadratic scalar factor 可能形成 quartic s denominator”的上界虽然正确，但 actual pole-resolvent canonicalization 给出更强结论：

\[
\boxed{
\text{actual transcendental s-antiderivatives only require quadratic factors.}
}
\]

正式升级：

```text
M1R_R02_RESOLVENT_CANONICALIZATION = PASS_EXACT
M1R_R02_S_ROOT_COMPLEXITY = QUADRATIC_ONLY
N_s_quadrature = 0
```

---

## 5. endpoint algebra 比 R01 预期更简单

令：

\[
x=u^2,\qquad y=v^2,
\]

\[
H=x+y-2xy,
\]

\[
K=\nu x-y+(1-\nu)xy,
\]

\[
a=(\nu-1)D+MH,
\]

以及：

\[
s_\pm=a\pm 2B\sqrt{xy}.
\]

对单 pole determinant：

\[
\Delta_r=I_2-rI_1+r^2,
\]

直接从原 Case21 invariants 可得到：

\[
\boxed{
\Delta_r(s_\pm)
=
E_r(x,y)\pm\sqrt{xy}\,O_r(x,y)
}
\]

其中：

\[
\boxed{
E_r
=
-\nu D^2
+DMK
+B^2(x+y-1)
-ra+r^2
}
\]

以及：

\[
\boxed{
O_r
=
B\left[D(\nu-1)+M(2-x-y)-2r\right].
}
\]

因此：

```text
degree_xy(E_r) <= 2
degree_xy(O_r) <= 1
```

并且：

\[
\boxed{
\Delta_r(s_+)\Delta_r(s_-)
=
E_r^2-xy\,O_r^2
}
\]

是总阶不超过 4 的普通 polynomial。

这比直接对高阶 M1R denominator 展开明显更紧凑。

---

## 6. s-quadratic discriminant 的精确 polynomial 结构

定义：

\[
\boxed{
\Gamma_r(x,y)
=
4xy\,\operatorname{disc}_s[\Delta_r(s)].
}
\]

配套 SymPy exact audit 得到：

```text
degree_x Gamma_r = 3
degree_y Gamma_r = 3
total_degree Gamma_r = 4
number_of_terms = 11
```

并且最高单变量项满足：

\[
[x^3]\Gamma_r=M^2y,\qquad
[y^3]\Gamma_r=M^2x.
\]

所以只要 finite-amplitude membrane coefficient \(M\neq0\)，在 interior \(x,y\in(0,1)\) 上，\(\Gamma_r\) **generically 是 cubic in x and cubic in y**。

同时：

\[
\operatorname{disc}_s[\Delta_r]
=
\frac{\Gamma_r(x,y)}{4xy}.
\]

因此所有 single-resolvent log/atanh coefficient 的 algebraic radical 都可以统一为：

\[
\sqrt{\Gamma_r(x,y)}.
\]

没有 quartic-in-s root family。

---

## 7. outer x-family generically 已经不是 elementary / ordinary elliptic

R01 outer weight：

\[
\frac{dx\,dy}{\sqrt{x(1-x)y(1-y)}}.
\]

单 resolvent antiderivative 的非有理部分包含：

\[
\Gamma_r(x,y)^{-1/2}
\times
\log/\operatorname{atanh}(\text{algebraic endpoint ratio}).
\]

固定一个 generic interior \(y\) 后，纯 algebraic radical 对 x 对应曲线：

\[
\boxed{
w^2=x(1-x)\Gamma_r(x,y).
}
\]

由于：

```text
degree_x Gamma_r = 3
```

所以右侧 generically 是 degree-5 polynomial。

配套脚本给出一个完全有理的 exact specialization：

\[
D=1,\quad M=1,\quad \nu=\frac15,\quad r=2,\quad y=\frac13.
\]

此时：

\[
\Gamma_r(x,1/3)
=
\frac{225x^3+1950x^2-10031x+7920}{675},
\]

故：

\[
P_5(x)
=
-\frac{x(x-1)(225x^3+1950x^2-10031x+7920)}{675}.
\]

exact checks：

```text
degree(P5) = 5
gcd(P5,P5') = 1
discriminant(P5)
= 7162455748218191872 / 3503151123046875
!= 0
```

因此该 specialization 是 square-free degree-5 hyperelliptic curve，genus：

\[
\boxed{g=2.}
\]

既然存在一个非退化 genus-2 specialization，generic family 不能被认定为 genus 0/1。

所以当前可以正式排除以下错误期望：

```text
all actual M1R outer blocks -> elementary/Beta only
all actual M1R outer blocks -> ordinary elliptic only
all actual M1R outer blocks -> one simple Appell F1/F2 family
```

某些退化参数状态可能降阶，但 **generic finite-amplitude state 已进入 hyperelliptic / higher period class**。

---

## 8. log endpoint term 的身份：relative hyperelliptic / algebraic-log period

quadratic s-factor 的原函数可统一写为：

```text
rational part
+ coefficient / sqrt(Gamma_r)
  * log(algebraic expression)
```

或等价 `atan/atanh` 形式。

代入 `s±` 后，log arguments 只依赖：

```text
E_r(x,y)
O_r(x,y)
sqrt(xy)
sqrt(Gamma_r(x,y))
```

因此 outer integrand 属于 finite **algebraic-logarithmic period** family。

在固定 y 的 genus-2 curve 上：

- algebraic part 对应 first/second-kind hyperelliptic differentials；
- log endpoint part 对应 relative / third-kind logarithmic periods；
- pair blocks只增加第二个 \(\Delta_t\) 与对应 resultant/pole divisor，不引入更高 s-root degree。

所以 actual M1R 的正确 Class-B 目标应从：

```text
Appell / elliptic maybe
```

收窄为：

\[
\boxed{
\text{Gauss–Manin / Picard–Fuchs system for hyperelliptic-relative periods}
}
\]

必要时再把该 system 与 GKZ/Aomoto representation 对照。

---

## 9. 当前 outer 分类正式判定

本轮不是 Gate A 最终闭合，但已经完成“actual factor family 的正确数学分类”。

正式状态：

```text
M1R_R02_RESOLVENT_CANONICALIZATION = PASS_EXACT
M1R_R02_ACTUAL_S_FACTORS = QUADRATIC_ONLY
M1R_R02_ENDPOINT_ALGEBRA = PASS_EXACT
M1R_R02_GENERIC_OUTER_CLASS_A = FAIL
M1R_R02_GENERIC_ORDINARY_ELLIPTIC = INSUFFICIENT
M1R_R02_GENERIC_SIMPLE_APPELL = NOT_GENERAL
M1R_R02_OUTER_PERIOD_CLASS = HYPERELLIPTIC_RELATIVE / PICARD_FUCHS
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

这里 `FAIL` 的是 **“outer integrals generically 都可落入 Class A”**，不是 M1R 路线失败。

相反，本轮把未知的 `CLASS_B_CANDIDATE` 进一步定位到一个有限、结构明确的 period family。

---

## 10. 下一唯一执行任务：PF1

下一步不再泛搜特殊函数，也不进入 Case21 Pu。

启动：

```text
PF1 = finite Gauss-Manin / Picard-Fuchs closure
      for canonical M1R outer resolvent periods
```

执行顺序：

1. 先处理 single-resolvent **algebraic** kernel；
2. 对固定 y 的 genus-2 curve 建立 de-Rham basis；
3. 用 Griffiths/Hermite reduction 把 D/q derivative 降回有限 basis；
4. 扩展到 log endpoint 的 relative-period basis；
5. 再处理 pair-resolvent blocks；
6. 最后消去/闭合 y 方向，形成 whole-halfwave finite differential system；
7. 只有得到 finite analytic system + branch/initial-value specification + analytic D/q derivatives 后，才把 Gate A 从 HOLD 改为 PASS_CLASS_B。

PF1 仍必须满足：

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

数值求值未来可以作为“特殊函数 / differential system evaluator”，但不得把原 x-y 空间积分重新用 adaptive quadrature 作为 formal definition。

---

## 11. 本轮未执行

```text
NO Case21 Pu solve
NO Swartz24 solve
NO UHPC production fit
NO shell/Y solve
NO structural calibration
NO coarea fallback activation
```

coarea/pushforward 仍保留为 PF1 真正失败后的下一候选，而不是现在并行展开。
