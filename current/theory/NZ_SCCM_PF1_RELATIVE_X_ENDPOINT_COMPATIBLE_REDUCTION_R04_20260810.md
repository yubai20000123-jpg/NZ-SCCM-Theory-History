# NZ-SCCM PF1-R04：physical relative-x endpoint compatible reduction

**日期：2026-08-10**  
**身份：CURRENT PF1 ANALYTIC PROGRESS — ALGEBRAIC RELATIVE ENDPOINT PASS / LOG EXTENSION HOLD**

## 0. 基础限制再次核对

本轮严格继承：

`governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`

没有改变：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order current Case21 kinematics
P(D,q), Rq(D,q), L(D,q)
M1R source-shaped rational -> resolvent -> s=I1 route
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
NO element integration
NO material-point grid
NO spatial cells
NO route switch
```

本轮唯一目标是处理 R03 留下的 physical `[0,1]` relative-x endpoint 问题；不能通过删除 exact differential、endpoint cell 或数值积分绕过。

---

## 1. R03 的 apparent endpoint obstruction

R03 对：

\[
w^2=P(x),
\qquad
\omega_k=\frac{x^kdx}{w}
\]

得到：

\[
\partial_\theta\omega_k
=\frac{Q_{k\theta}(x)}{w}dx
-2d\left(\frac{B_{k\theta}(x)}w\right).
\]

closed cycle 上 exact term 消失；但 physical chain 是：

\[
x\in[0,1]
\]

且 `x=0,1` 是 branch endpoints，所以 R03 正确地没有直接丢掉 boundary term。

R04 首先检查：**对当前特殊 `P=x(1-x)Gamma` family，是否存在比一般 genus-2 reduction 更强的 endpoint-compatible identity。**

---

## 2. Case21/R02 curve 的固定 branch-factor structure

定义：

\[
\boxed{h(x)=x(1-x)}
\]

和：

\[
\boxed{P(x;\theta)=h(x)\Gamma(x;\theta)}.
\]

对：

\[
\theta\in\{D,M,y,\nu,r\}
\]

branch endpoints `x=0,1` 不随参数移动，因此：

\[
\boxed{P_{,\theta}=h\Gamma_{,\theta}.}
\]

于是：

\[
N_{k\theta}
=-\frac12x^kP_{,\theta}
=h\widetilde N_{k\theta},
\]

其中：

\[
\boxed{
\widetilde N_{k\theta}
=-\frac12x^k\Gamma_{,\theta}.
}
\]

这一个固定 `h=x(1-x)` 因子是 physical endpoint compatibility 的关键。

---

## 3. 从一般 9×9 reduction 降为 endpoint-compatible 7×7 reduction

直接寻找：

\[
\widetilde A(x)=\sum_{i=0}^3\tilde a_ix^i,
\qquad
C(x)=\sum_{j=0}^2c_jx^j
\]

满足：

\[
\boxed{
\widetilde N
=\widetilde A\Gamma+C\,h\Gamma'.
}
\]

未知量：

```text
4 coefficients of Atilde
+ 3 coefficients of C
= 7
```

右侧最高次数 6，所以得到固定 7×7 coefficient system。

其 determinant 为：

\[
\boxed{
\det\mathsf S_{\rm rel}
=\operatorname{Res}(\Gamma,h\Gamma').
}
\]

利用 resultant 的乘法性：

\[
\boxed{
\operatorname{Res}(\Gamma,h\Gamma')
=
\operatorname{Res}(\Gamma,h)
\operatorname{Res}(\Gamma,\Gamma').
}
\]

如果：

\[
P=h\Gamma
\]

是 square-free，则：

1. `Gamma` 自身 square-free，所以 `Res(Gamma,Gamma') != 0`；
2. `Gamma(0) != 0`、`Gamma(1) != 0`，所以 `Res(Gamma,h) != 0`。

因此 physical regular state 下 7×7 system 唯一可逆。

---

## 4. exact term 自动带 h=x(1-x)

由 7×7 solution 定义：

\[
\boxed{B_{\rm rel}=hC}
\]

和：

\[
\boxed{A=\widetilde A-Ch'}.
\]

因为：

\[
P'=h'\Gamma+h\Gamma',
\]

有：

\[
\begin{aligned}
AP+B_{\rm rel}P'
&=(\widetilde A-Ch')h\Gamma
+hC(h'\Gamma+h\Gamma')\\
&=h(\widetilde A\Gamma+Ch\Gamma')\\
&=h\widetilde N\\
&=N.
\end{aligned}
\]

所以它严格属于 R03 同一个 Griffiths/Hermite identity，不是新结构方程。

但现在 exact term 具有额外结构：

\[
\boxed{
\frac{B_{\rm rel}}w
=
\frac{hC}{\sqrt{h\Gamma}}
=C\sqrt{\frac h\Gamma}.
}
\]

当 physical regular state 满足：

\[
\Gamma(0)\ne0,
\qquad
\Gamma(1)\ne0,
\]

则：

\[
\boxed{
\lim_{x\to0^+}\frac{B_{\rm rel}}w=0,
\qquad
\lim_{x\to1^-}\frac{B_{\rm rel}}w=0.
}
\]

因此：

\[
\boxed{
\int_0^1d(B_{\rm rel}/w)=0
}
\]

是 physical chain 上的**真实 endpoint identity**，不是“closed cycle 才能扔掉 exact differential”的假定。

这修正了 R03 的 HOLD：对于当前 algebraic compact derivative family，physical `[0,1]` endpoint obstruction 实际上可以严格消去。

正式升级：

```text
PF1_R04_ENDPOINT_COMPATIBLE_7X7_REDUCTION = PASS_EXACT
PF1_R04_PHYSICAL_ALGEBRAIC_X_ENDPOINT = PASS_EXACT
```

---

## 5. exact executable audit

配套：

- `current/theory/nz_sccm_pf1_relative_x_endpoint_r04.py`
- `current/theory/NZ_SCCM_PF1_RELATIVE_X_ENDPOINT_R04_results.json`

采用三个完全有理 regular states A/B/C。

### State A

```text
D=1, M=1, nu=1/5, r=2, y=1/3
```

\[
\det S_{rel}
=\frac{635871426510848}{1037970703125}\ne0.
\]

### State B

```text
D=4/5, M=3/2, nu=1/4, r=-1/2, y=2/5
```

\[
\det S_{rel}
=-\frac{716684980401}{488281250000}\ne0.
\]

### State C

```text
D=6/5, M=2/3, nu=1/6, r=3/2, y=3/5
```

\[
\det S_{rel}
=\frac{652911093504}{30517578125}\ne0.
\]

三个状态均 exact 验证：

```text
det(7x7) = Res(Gamma,h Gamma')
```

并对：

```text
theta = D,M,y
k = 0,1,2,3
```

共 36 个 reduction：

```text
identity N=A P+Brel P' = TRUE exactly
Brel(0)=0 exactly
Brel(1)=0 exactly
```

因此这个 PASS 不是仅靠局部渐近推断。

---

## 6. R04 第二部分：actual direct-log endpoint divisor 已定位

algebraic endpoint pass 并不等于 actual M1R 已完全闭合，因为 `s` antiderivative 还含 log/atanh。

R02 已有：

\[
\boxed{
\Delta_r(s_\pm)
=E_r(x,y)\pm\sqrt{xy}\,O_r(x,y).
}
\]

其中固定 `y` 时：

\[
\deg_xE_r\le1,
\qquad
\deg_xO_r\le1.
\]

因此 direct logarithm：

\[
\log\frac{\Delta_r(s_+)}{\Delta_r(s_-)}
\]

可以用 global algebraic cover：

\[
\boxed{x=t^2,\qquad \eta^2=y}
\]

写成：

\[
\boxed{
\log\frac{\Phi_+(t)}{\Phi_-(t)},
\qquad
\Phi_\pm(t)
=E_r(t^2,y)\pm\eta t\,O_r(t^2,y).
}
\]

因为 `E(t^2)` degree <=2 in `t`，而 `t O(t^2)` degree <=3：

\[
\boxed{
\deg_t\Phi_\pm\le3.
}
\]

并且：

\[
\boxed{
\Phi_+\Phi_-
=E_r(t^2,y)^2-y t^2 O_r(t^2,y)^2.
}
\]

所以 direct-log branch data 不需要连续空间 state-front 或 cell；它由**两个有限 cubic algebraic divisors**控制。

### 6.1 exact witness

取：

```text
D=1
M=1
nu=1/5
r=2
y=1/4
eta=1/2
B=1/3
```

得到：

\[
\Phi_+
=-\frac{60t^3+176t^2+183t-1644}{360},
\]

\[
\Phi_-
=\frac{60t^3-176t^2+183t+1644}{360}.
\]

exact audit：

```text
gcd(Phi_plus,Phi_minus)=1
disc(Phi_plus)=disc(Phi_minus)=-9482483/559872 != 0
```

所以 witness 上两个 divisor 都是 finite square-free cubic sets，彼此无共同零点。

正式身份：

```text
PF1_R04_DIRECT_LOG_DIVISOR_IDENTIFICATION = PASS_EXACT
```

---

## 7. atanh / quadratic-root log 也可化为有限 algebraic divisor

对固定 `(x,y)` 的 quadratic：

\[
\Delta(s)=\alpha s^2+\beta s+\gamma,
\qquad
\delta=\beta^2-4\alpha\gamma,
\]

令：

\[
s_\pm=a\pm c,
\qquad
c=2B\sqrt{xy}.
\]

quadratic roots 写成：

\[
m\pm h_q,
\qquad
m=-\frac\beta{2\alpha},
\qquad
h_q=\frac{\sqrt\delta}{2\alpha}.
\]

endpoint antiderivative 的 root cross-ratio 可严格整理成：

\[
\boxed{
\frac{F+2ch_q}{F-2ch_q},
\qquad
F=(a-m)^2-c^2-h_q^2.
}
\]

而 R02 定义：

\[
\Gamma_r=4xy\,\delta,
\]

所以：

\[
2ch_q
=\frac{c\sqrt\delta}{\alpha}
=\frac{B\sqrt{\Gamma_r}}{\alpha}.
\]

因此：

\[
\boxed{
\text{cross-ratio}
=
\frac{\alpha F+B\sqrt{\Gamma_r}}
     {\alpha F-B\sqrt{\Gamma_r}}.
}
\]

这说明 atanh/root-log 的 branch data 同样不是无限状态前沿，而是落在 finite algebraic cover：

\[
z^2=\Gamma_r(x,y)
\]

上的有限 divisor：

\[
\boxed{
\Psi_\pm=\alpha F\pm Bz.
}
\]

当 `alpha=0`（即 `x+y=1`）出现 linear-quadratic degeneration 时，production formula 必须使用同一解析表达的连续极限；**不得把该 locus 转成 spatial subdomain/cell。**

本轮把 divisor family 识别出来，但尚未建立 `Psi` family 的完整 extended connection matrix，所以不把 log relative stage 标 PASS。

---

## 8. R04 当前取得了什么、还缺什么

现在 physical-x 问题已经比 R03 明确很多：

```text
absolute genus-2 4D Gauss-Manin             = PASS_EXACT
physical algebraic branch endpoints [0,1]  = PASS_EXACT
endpoint-compatible 7x7 reduction           = PASS_EXACT
direct log divisor Phi_plus/Phi_minus       = PASS_EXACT
atanh/root-log finite divisor form Psi±     = IDENTIFIED
```

但仍缺：

```text
finite relative/twisted de-Rham generator set
parameter derivative reduction for log-weighted periods
third-kind meromorphic reduction at divisor points
finite monodromy/branch data
pair-resolvent relative extension
```

所以：

```text
PF1_R04_LOG_RELATIVE_EXTENDED_CONNECTION = HOLD
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

这里绝不能把“divisor 是有限的”偷换成“完整 log period 已闭合”。

---

## 9. 下一唯一执行任务：PF1-R05

保持全部路径限制，下一步只进入：

```text
single-resolvent log family
-> choose finite algebraic cover for Phi/Psi divisors
-> compact + third-kind/relative generators
-> differentiate log-weighted generators
-> Hermite/Griffiths reduce back to finite extended basis
-> exact matrix identity audit
```

一个优先结构是利用：

\[
\partial_\theta(\omega\log\Phi)
=(\partial_\theta\omega)\log\Phi
+\omega\,\partial_\theta\log\Phi,
\]

其中：

\[
\partial_\theta\log\Phi=\Phi_{,\theta}/\Phi
\]

只产生对应有限 divisor 上的 meromorphic differential；R04 已证明 direct-log divisor 由有限 cubic factors 控制。

但 R05 必须真正给出 finite basis 和 exact reduction matrix后才能 PASS，不能只引用“relative cohomology 有限维”。

R05 PASS 后才处理 pair-resolvent relative layer，再进入 y-direction whole-halfwave closure。

---

## 10. 本轮 formal counts

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_material_point_grid = 0
absolute de-Rham basis dimension = 4
R03 coefficient matrix dimension = 9
R04 endpoint-compatible coefficient matrix dimension = 7
```

4、9、7 全是 finite analytic coefficient/function-space dimensions，不是空间节点、材料点或积分点。

---

## 11. 本轮明确未执行

```text
NO Case21 Pu
NO Swartz24
NO UHPC production fit
NO shell/Y production solve
NO structural calibration
NO spatial numerical quadrature
NO endpoint cells
NO material-point integration
NO coarea route switch
```
