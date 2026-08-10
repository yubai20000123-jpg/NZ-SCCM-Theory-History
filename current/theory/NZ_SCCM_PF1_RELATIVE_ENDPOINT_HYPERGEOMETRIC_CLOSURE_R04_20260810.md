# NZ-SCCM PF1 physical-relative endpoint / hypergeometric closure R04

**日期：2026-08-10**  
**身份：CURRENT PF1 ANALYTIC PROGRESS — PHYSICAL x-ENDPOINT PASS / LOG-ATANH CANONICAL KERNEL PASS / WHOLE GATE A HOLD**

## 0. 硬边界不变

本轮严格服从：

`governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`

因此没有改变，也无权改变：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
KINEMATICS = NGUYEN_SECOND_ORDER
P(D,q), Rq(D,q), L(D,q)
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT
NO element integration
NO material-point grid
NO spatial cells
M1R source-shaped rational -> resolvent -> s=I1 route
```

R04 只处理 R03 留下的 physical relative x-chain / endpoint / log-atanh 闭合问题。若失败则 HOLD；不得切换为空间 quadrature、材料点、FE、结构反标或其他结构残量。

---

## 1. R03 的 endpoint HOLD 可以进一步解除

R03 对 genus-2 compact algebraic basis 的参数导数得到：

\[
\frac{N}{w^3}dx
=
\frac{A+2B_x}{w}dx
-2d\left(\frac{B}{w}\right),
\]

其中：

\[
w^2=P(x)=x(1-x)\Gamma(x;\theta).
\]

R03 当时谨慎保留：physical chain `x in [0,1]` 上 `B/w` 的 endpoint contribution 可能非零/奇异。

R04 发现：对 NZ-SCCM 当前 family，这个担忧可以用结构本身严格消掉。

因为所有 current 参数 `theta` 只改变 `Gamma`，而 `x=0,1` 两个 endpoint factor 固定：

\[
P_{,\theta}=x(1-x)\Gamma_{,\theta}.
\]

于是：

\[
N_{k\theta}=-\frac12x^kP_{,\theta}
\]

严格满足：

\[
N_{k\theta}(0)=N_{k\theta}(1)=0.
\]

另一方面 reduction identity：

\[
N=A P+B P'.
\]

在 regular endpoint：

\[
P'(0)=\Gamma(0)\ne0,
\qquad
P'(1)=-\Gamma(1)\ne0.
\]

代入 `x=0,1`：

\[
\boxed{B(0)=B(1)=0.}
\]

由于 `deg B<=4`，因此：

\[
\boxed{B=x(1-x)\widetilde B_2(x),\qquad \deg\widetilde B_2\le2.}
\]

所以：

\[
\frac{B}{w}
=
\frac{\sqrt{x(1-x)}\,\widetilde B_2(x)}{\sqrt{\Gamma(x)}}
\longrightarrow0
\quad(x\to0,1).
\]

因此 physical relative chain 上：

\[
\boxed{
\left[\frac{B}{w}\right]_{0}^{1}=0.
}
\]

即 R03 的 exact differential 在真实 `[0,1]` chain 上也不产生 boundary correction。

这不是忽略 endpoint，而是由固定 branch endpoints `x(1-x)` 自动保证 exact boundary vanishing。

配套 exact witness 对 `theta=D,M,y`、`k=0..3` 共 12 个 reductions 全部得到：

```text
B(0)=0 exactly
B(1)=0 exactly
B mod x(1-x)=0 exactly
deg[B/(x(1-x))]=2
```

正式升级：

```text
PF1_R04_PHYSICAL_RELATIVE_X_EXACT_TERM = PASS_EXACT
PF1_R04_ENDPOINT_LOCAL_CELL = NOT_NEEDED
PF1_R04_X_SPATIAL_SUBDIVISION = 0
```

---

## 2. 关键新简化：不要把 symmetric s-endpoint log 拆成裸 `1/sqrt(Gamma) × log`

R02 把 quadratic s-antiderivative 展开后，单项可看到：

```text
1/sqrt(Gamma_r) × log / atanh(algebraic endpoint expression)
```

这使 generic unsymmetrized representation 暴露 genus-2 radical。

但 physical thickness contraction 从来不是单独的上端或下端，而是固定的 symmetric endpoint divided difference：

\[
\mathcal D_{\mathcal F}(a,c)
=\frac{\mathcal F(a+c)-\mathcal F(a-c)}{2c},
\qquad c=2B\sqrt{xy}.
\]

R04 对这个**真实 physical combination**先做 algebraic recombination，发现 log/atanh 可以统一进入一个无显式 square-root branch 的 normalized kernel。

定义：

\[
\boxed{
\Phi(z)
=\frac{\operatorname{atanh}\sqrt z}{\sqrt z}
={}_2F_1\left(\frac12,1;\frac32;z\right),
\qquad \Phi(0)=1.
}
\]

`Phi` 通过 `z=0` 的解析延拓定义，不需要对 `sqrt(z)` 选空间 branch cell。

它满足有限二阶 Gauss hypergeometric ODE：

\[
\boxed{
z(1-z)\Phi''+\left(\frac32-\frac52z\right)\Phi'-\frac12\Phi=0.}
\]

所以 `Phi` 是允许的 finite named special-function object；它不是 numerical quadrature。

---

## 3. general quadratic denominator 的两个 physical endpoint kernel

对：

\[
\Delta(s)=\alpha s^2+\beta s+\gamma,
\]

定义 center：

\[
A_0=\Delta(a),
\qquad
L=2\alpha a+\beta,
\qquad
\delta=\beta^2-4\alpha\gamma,
\]

以及：

\[
E=A_0+\alpha c^2,
\qquad
\mathcal K=A_0-\alpha c^2.
\]

则：

\[
\Delta(a\pm c)=E\pm cL.
\]

### 3.1 log endpoint divided difference

由 `2 atanh z = log[(1+z)/(1-z)]` 的解析延拓：

\[
\boxed{
\frac{\log\Delta(a+c)-\log\Delta(a-c)}{2c}
=\frac{L}{E}\,
\Phi\left(\frac{c^2L^2}{E^2}\right).
}
\]

### 3.2 reciprocal quadratic primitive

若 `J'(s)=1/Delta(s)`，则：

\[
\boxed{
\frac{J(a+c)-J(a-c)}{2c}
=\frac1{\mathcal K}\,
\Phi\left(\frac{c^2\delta}{\mathcal K^2}\right).
}
\]

配套 SymPy exact audit 不通过不定积分黑箱，而通过微分恒等式验证：

```text
d/dc [2c * reciprocal_kernel]
= 1/Delta(a+c) + 1/Delta(a-c)
```

严格为 0 remainder；`c->0` 自动回到 `1/Delta(a)`。

因此 physical symmetric endpoint contraction 已不需要保留裸：

```text
sqrt(delta)
log branch
atanh branch
```

而统一保留 `Phi(rational argument)` 及有限 monodromy/analytic-continuation data。

---

## 4. 代回 actual M1R `Delta_r` 后，两个 Phi argument 都是 rational

R02：

\[
\Delta_r(s_\pm)=E_r\pm\sqrt{xy}\,O_r,
\]

其中：

\[
E_r=-\nu D^2+DMK+B^2(x+y-1)-ra+r^2,
\]

\[
O_r=B\ell_r,
\qquad
\ell_r=D(\nu-1)+M(2-x-y)-2r.
\]

由 `c=2B sqrt(xy)` 可得：

\[
L_r=\frac{\ell_r}{2}.
\]

所以 log kernel 直接化为：

\[
\boxed{
\mathcal L_r
=\frac{\ell_r}{2E_r}
\Phi\left(
\frac{B^2xy\ell_r^2}{E_r^2}
\right).
}
\]

没有 `sqrt(x)`、`sqrt(y)` 或 `sqrt(Gamma)` 出现在 argument 外部。

又因为 R02：

\[
\delta_r=\operatorname{disc}_s\Delta_r
=\frac{\Gamma_r}{4xy},
\]

而：

\[
\mathcal K_r
=E_r-2B^2(x+y-1),
\]

所以 reciprocal kernel：

\[
\boxed{
\mathcal J_{0,r}
=\frac1{\mathcal K_r}
\Phi\left(
\frac{B^2\Gamma_r}{\mathcal K_r^2}
\right).
}
\]

再次没有裸 radical。

这说明 R02 的 genus-2 classification 对**展开后的 unsymmetrized algebraic factor**仍然正确，但 actual physical symmetric endpoint combination 存在更强 cancellation；production relative kernel 不必把 `1/sqrt(Gamma)` 和 log 分开处理。

---

## 5. linear numerator 也可以保持有限且跨 `alpha=0` 连续

任意 proper quadratic block 最终只需：

\[
\frac{m_0+m_1(s-a)}{\Delta(s)}.
\]

定义：

\[
\mathcal J_0
=\frac1{2c}\int_{a-c}^{a+c}\frac{ds}{\Delta(s)},
\]

\[
\mathcal J_1
=\frac1{2c}\int_{a-c}^{a+c}\frac{s-a}{\Delta(s)}ds.
\]

上节已经给出 `J0` 的 closed `Phi` 形式。再由：

\[
\frac{d}{ds}\log\Delta
=\frac{L+2\alpha(s-a)}{\Delta},
\]

得到：

\[
\boxed{
\mathcal J_1
=\frac{\mathcal L-L\mathcal J_0}{2\alpha}
}
\]

其中 numerator 在 `alpha->0` 时具有 removable zero。为了禁止把 `x+y=1` 变成 spatial branch front，正式定义使用**解析延拓值**而不是空间分区：

当 `alpha=0`：

\[
\boxed{
\mathcal J_1
=\frac{1-\Phi(z)}{L},
\qquad
z=\frac{c^2L^2}{A_0^2},
}
\]

并在 `L->0` 再取连续极限 `J1->0`。

这与 `sinc(0)=1` 类似，是 removable-singularity evaluation，不是把结构域切成 `alpha>0/alpha<0/alpha=0` 三个空间子域。

因此：

\[
\boxed{
\frac1{2c}\int_{a-c}^{a+c}
\frac{m_0+m_1(s-a)}{\Delta(s)}ds
=m_0\mathcal J_0+m_1\mathcal J_1
}
\]

属于 finite rational + `Phi` kernel family。

若原 numerator degree >=2，先做 exact polynomial division；polynomial part 由 finite endpoint moments 完全闭式，proper part仍只需要 `J0,J1`。

---

## 6. pair-resolvent 也不再要求独立 log-relative divisor machinery

R02 已证明：

\[
\frac{N(s)}{\Delta_r\Delta_t}
=\frac{A_r(s)}{\Delta_r}
+\frac{A_t(s)}{\Delta_t}
\]

（resultant 非零；退化时使用 analytic confluent limit）。

因此 pair block 在 s 方向最终只产生：

```text
finite polynomial endpoint moments
+ J0_r / J1_r
+ J0_t / J1_t
```

每一个 `J0/J1` 都属于上一节同一个 `Phi` family。

所以：

```text
PF1_R04_PAIR_S_ENDPOINT_KERNEL_FAMILY = SAME_FINITE_PHI_FAMILY
NO quartic-root special function
NO separate spatial log divisor partition
```

pair resultant 只作为有限 rational coefficient singular locus，需要后续 branch/confluent audit，但不改变 formal path。

---

## 7. R03 genus-2 absolute system 的新身份

R03 的 absolute Gauss–Manin closure仍然是正确且有价值的：

- 它严格证明 unsymmetrized `1/sqrt(Gamma)` algebraic factor属于 finite genus-2 period system；
- 可用于 independent analytic audit；
- 对未来其他非对称 endpoint functional 仍可直接使用。

但对当前 physical symmetric s-endpoint contraction，R04 给出更紧凑的生产表示：

```text
unsymmetrized genus-2 radical × log
-> symmetric endpoint recombination
-> rational coefficients × Phi(rational argument)
```

这是同一路线内部的 exact reduction，不是切换理论，不改变 M1R、s=I1、P/Rq/L 或空间域。

---

## 8. R04 正式状态

```text
PF1_PATH_INVARIANTS = LOCKED
PF1_R04_PHYSICAL_RELATIVE_X_EXACT_TERM = PASS_EXACT
PF1_R04_ENDPOINT_B_OVER_W = VANISHES_EXACTLY
PF1_R04_LOG_ATANH_SYMMETRIC_KERNEL = PASS_EXACT
PF1_R04_CANONICAL_SPECIAL_FUNCTION = 2F1(1/2,1;3/2;z)
PF1_R04_ALPHA_ZERO = REMOVABLE_ANALYTIC_LIMIT
PF1_R04_PAIR_S_ENDPOINT_KERNEL_FAMILY = FINITE_PHI_FAMILY
PF1_R04_SPATIAL_SUBDOMAINS_ADDED = 0
PF1_R04_SPATIAL_QUADRATURE = 0
```

这意味着 R03 的：

```text
PF1_R03_PHYSICAL_RELATIVE_X_ENDPOINT = HOLD
PF1_R03_LOG_RELATIVE_EXTENSION = NOT_YET_CLOSED
```

已由 R04 的更强 symmetric-endpoint identity supersede。

但 whole-halfwave Gate A **仍然 HOLD**，因为现在剩余的真实问题是：

\[
\int_0^1\int_0^1
\frac{R(x,y)\,\Phi(\chi(x,y))}
{\sqrt{x(1-x)y(1-y)}}dxdy,
\]

其中 `R,chi` 为 actual M1R block 给出的 finite rational functions。

不能把这个二维 integral 留作 numerical quadrature。

---

## 9. 下一唯一任务：PF1-R05 hypergeometric pullback creative telescoping

下一步不再建立 spatial relative cells，也不需要继续扩大 genus-2 log divisor basis；而是直接对 R04 得到的 actual canonical kernel：

```text
Beta(x) Beta(y)
× rational coefficient
× Phi(rational pullback chi)
```

执行：

```text
R05
= finite holonomic / Picard-Fuchs creative telescoping
  for actual M1R Phi-pullback blocks
```

必须完成：

1. 利用 `Phi` 的二阶 hypergeometric ODE 构造有限 derivative basis；
2. 对 x derivative 做 exact telescoping，消去 physical x integral；
3. 再对 y 做 exact telescoping/pushforward；
4. 最终只保留 external parameters `D,q,r,...` 的 finite differential-system / special-function object；
5. 显式处理 `chi=1`、denominator/resultant/discriminant singular loci及 monodromy；
6. `D,q` derivatives 必须在同一 finite system 内闭合；
7. 不允许以 numerical x/y integration 代替 telescoper。

只有 R05/后续 actual whole-domain pushforward 真正形成 finite evaluator，才允许把：

```text
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

改成 `PASS_CLASS_B`。

---

## 10. 本轮没有做什么

```text
NO Case21 Pu solve
NO Swartz24 solve
NO material refit
NO UHPC production fit
NO shell/Y production solve
NO numerical x/y quadrature
NO material-point integration
NO route switch
```
