# NZ-SCCM PF1-R06：endpoint-compatible master reduction 与 tau connection

**日期：2026-08-10**  
**身份：CURRENT PF1 ANALYTIC PROGRESS — FINITE MASTER REDUCTION PASS ON ACTUAL DRIVER / GENERIC PRODUCTION EVALUATOR STILL HOLD**

## 0. 目标相关性与边界

本轮严格继承：

- `governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`
- `governance/PF1_R05_GOAL_RELEVANCE_CHECKPOINT_20260810.md`

不建立新的结构理论，不计算 Case21 Pu，不进入 Swartz24，不重新拟合材料，不引入空间积分点、空间子域、材料点或数值 quadrature。

唯一处理对象仍是 R05 已得到的 actual common rational driver：

\[
\boxed{
\mathscr D_r(\tau)=E_r(\tau)^2-\tau xy\ell_r^2,
\qquad \tau=B(q)^2
}
\]

目的仅是判断它能否形成服务 `P(D,q), R_q(D,q), L(D,q)` 的 finite analytic differential system。

正式身份继续保持：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
MATERIAL_POINT_GRID = 0
```

---

## 1. R05 的 19 个 standard monomials 不是最终 period basis

R05 在 exact rational witness

```text
D=1, M=1, nu=1/5, r=2, tau=symbolic
```

上得到 endpoint-compatible twisted critical quotient 的 19 个 standard monomials。

R06 不把“19”直接冒充 connection dimension，而是实际建立物理积分的 integration-by-parts reduction。

定义：

\[
h_x=x(1-x),\qquad h_y=y(1-y),
\]

以及 rational period：

\[
\boxed{
I[N]
=
\int_0^1\!\!\int_0^1
\frac{N(x,y)}
{\sqrt{h_xh_y}\,\mathscr D_r}
\,dx\,dy.
}
\]

对参数 \(\theta\)：

\[
\partial_\theta I[N]
=
\int\!\!\int
\frac{N_{,\theta}\mathscr D_r-N\mathscr D_{r,\theta}}
{\sqrt{h_xh_y}\,\mathscr D_r^2}
\,dx\,dy.
\]

因此真正需要的是把 `D_r^{-2}` numerator 精确降回 `D_r^{-1}` master periods。

---

## 2. endpoint-compatible exact IBP identity

取 polynomial certificates \(A(x,y)\)、\(B(x,y)\)。由于

\[
\sqrt{h_x}\to0\quad(x\to0,1),
\qquad
\sqrt{h_y}\to0\quad(y\to0,1),
\]

下式的边界项在同一 analytic branch 上严格消失：

\[
\int\!\!\int
\partial_x
\left[
\frac{\sqrt{h_x/h_y}\,A}{\mathscr D_r}
\right]dxdy=0,
\]

\[
\int\!\!\int
\partial_y
\left[
\frac{\sqrt{h_y/h_x}\,B}{\mathscr D_r}
\right]dxdy=0.
\]

因此若 numerator \(Q\) 满足 polynomial identity：

\[
\boxed{
\begin{aligned}
Q={}&\mathscr D_r R\\
&+\mathscr D_r
\left(
 h_xA_{,x}+\frac{h_x'}2A
+h_yB_{,y}+\frac{h_y'}2B
\right)\\
&-h_xA\mathscr D_{r,x}
-h_yB\mathscr D_{r,y},
\end{aligned}
}
\]

则严格有：

\[
\boxed{
\int\!\!\int
\frac{Q}{\sqrt{h_xh_y}\,\mathscr D_r^2}
dxdy
=
I[R].
}
\]

这一步不需要 endpoint cell，也不需要 x/y quadrature。

正式状态：

```text
PF1_R06_ENDPOINT_COMPATIBLE_IBP_IDENTITY = PASS_EXACT
```

---

## 3. 19 → 15：实际 period relations 被显式找出

在 R05 的 19 monomial space 上，使用 total-degree <=5 的 endpoint-compatible certificates，exact coefficient matching 得：

```text
polynomial coefficient equations = 62
unknowns = 57
```

进一步求 homogeneous relation：

\[
\mathscr D_r R+\text{IBP certificate}=0
\]

得到 **4 个独立 period relations**。

该关系秩在三个不同 rational parameter witnesses 上保持为 4；R05 的 19 项 therefore 是 overcomplete quotient screen，而不是最终 master period basis。

R06 选择保留以下 15 个 master monomials：

```text
1
y
y^2
y^3
y^4
y^5
x
xy
xy^2
xy^3
xy^4
x^2
x^2 y
x^2 y^2
x^3 y
```

并消去：

```text
x^2 y^3
x^3
x^4
x^5
```

所以 witness master dimension 为：

\[
\boxed{15}.
\]

正式状态：

```text
PF1_R06_R05_19_MONOMIAL_QUOTIENT = OVERCOMPLETE_FOR_PERIOD_BASIS
PF1_R06_PERIOD_RELATION_RANK_WITNESS = 4
PF1_R06_MASTER_PERIOD_DIMENSION_WITNESS = 15
```

这里仍谨慎使用 `WITNESS` 身份；没有偷换成 generic theorem。

---

## 4. explicit symbolic tau connection 已实际生成

对 15 个 master periods：

\[
\mathbf I
=
[I_1,\ldots,I_{15}]^{\mathsf T},
\]

逐列取：

\[
Q_j=-m_j\,\mathscr D_{r,\tau},
\]

并用第 2 节的固定 endpoint-compatible polynomial identity exact reduction。

在 witness：

```text
D=1
M=1
nu=1/5
r=2
tau=symbolic
```

下，每一列均得到唯一的 15 个 master coefficients；certificate 本身允许一个 gauge 自由度，但 **master coefficients 不含该自由参数**。

因此实际得到：

\[
\boxed{
\frac{d\mathbf I}{d\tau}
=
\Omega_\tau(\tau)\mathbf I,
\qquad
\Omega_\tau\in\mathbb Q(\tau)^{15\times15}.
}
\]

矩阵已完整存入：

`NZ_SCCM_PF1_ENDPOINT_IBP_MASTER_CONNECTION_R06_results.json`

其规模：

```text
shape = 15 x 15
nonzero entries = 211 / 225
total symbolic entry characters ≈ 2.68e5
max single entry characters = 1699
```

并用：

```text
tau=1/7
```

对 symbolic matrix 与独立 exact rational coefficient matching 做逐元素复核：

```text
225/225 entries identical exactly
```

正式状态：

```text
PF1_R06_TAU_CONNECTION_MATRIX_WITNESS = PASS_EXACT_SYMBOLIC_15X15
```

---

## 5. connection singular-locus audit

该 witness connection 全部 entry denominator 的 LCM 为一个有限 polynomial product。候选非负 real singular values 包括：

```text
tau = 0
9/5
261/95
3
16/5
81/25
~3.5729339662
69/19
19/5
45/11
27/5
1137/200
144/25
8
~8.0081012411
9
~10.2100963368
...
```

其中必须严格区分：

1. physical period / driver 的真实 singularity；
2. 当前 15-master gauge/basis 的 apparent singularity；
3. `tau=0` 的 regular-singular initial point。

本轮只完成 **connection candidate singular locus**，没有把这些候选全部宣判为物理奇点。

物理路径始终是：

\[
\boxed{
\tau(q)=B(q)^2
=
\left[
\frac{\pi^2}{2\varepsilon_0}\frac tb\,q
\right]^2
\ge0.
}
\]

因此生产 evaluator 后续必须沿真实 `q` path 做 branch/basis patch audit，而不能把 witness matrix denominator 的零点直接当作结构事件。

---

## 6. D、M、B、q derivatives 使用同一 finite system

R06 进一步把 numerator source 改为：

\[
Q_j^{(D)}=-m_j\mathscr D_{r,D},
\qquad
Q_j^{(M)}=-m_j\mathscr D_{r,M},
\]

在同一 15-master / degree-5 certificate system 上进行 exact reduction。

在：

```text
D=1, M=1, nu=1/5, r=2, tau=1/7
```

处，15 列全部获得唯一 master coefficients：

```text
Omega_D : 15 x 15, PASS_EXACT witness point
Omega_M : 15 x 15, PASS_EXACT witness point
```

由于 `B` 只通过：

\[
\tau=B^2
\]

进入 common driver：

\[
\boxed{
\Omega_B=2B\,\Omega_\tau.
}
\]

Case21 又有：

\[
M_q=\alpha(q_0+q),
\qquad
B_q=\beta,
\qquad
\tau_q=2BB_q,
\]

所以：

\[
\boxed{
\Omega_q
=
M_q\Omega_M
+
2BB_q\Omega_\tau.
}
\]

这说明 `D/M/B/q` analytic derivatives 不需要新空间积分器，也不需要 material-point differentiation。

正式状态：

```text
PF1_R06_D_CONNECTION_WITNESS_POINT = PASS_EXACT_15X15
PF1_R06_M_CONNECTION_WITNESS_POINT = PASS_EXACT_15X15
PF1_R06_B_Q_CHAIN_RULE = PASS_ANALYTIC
```

---

## 7. 对工程目标的裁决：有明显进展，但 Gate A 仍不能提前 PASS

本轮已经把 R05 的“19 monomial scale screen”推进为真正的 finite period system witness：

```text
19 critical quotient monomials
-> 4 exact IBP period relations
-> 15 master periods
-> explicit symbolic 15x15 tau connection
-> same-system D/M derivative reduction
```

这条线仍直接服务 actual common driver，因此**没有偏离 NZ-SCCM 目标**。

但仍缺三件 production-level 闭合：

1. generic/current `(D,M,nu,r)` connection generator 的完整 singular-locus audit；
2. `tau=0` 或其他 safe base point 的 branch-consistent analytic initial values；
3. 能沿 physical `tau=B(q)^2` 稳定推进、并对 current 27 pole / pair-block family复用的 no-x/y-quadrature evaluator。

因此：

```text
PF1_R06_GENERIC_DMRT_CONNECTION = HOLD
PF1_R06_BRANCH_INITIAL_VALUE_EVALUATOR = HOLD
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

这不是 route failure；但按照 `PF1_R05_GOAL_RELEVANCE_CHECKPOINT`，下一步不得扩展 generic hypergeometric/GKZ 理论。只允许继续做**实际 production evaluator closure**。

---

## 8. 下一任务锁定：PF1-R07

唯一允许的下一任务：

```text
R07 = actual production evaluator closure
```

只做：

1. 把 R06 coefficient-matching connection generator 参数化到 actual `(D,M,nu,r)`；
2. 选择并证明 safe analytic initial-value prescription；
3. 对 physical `tau=B(q)^2` 给出 branch/basis patch rule；
4. 用同一 finite master system返回 actual rational-driver periods及 `D,q` derivatives；
5. 验证 27 single-pole / 106 pair-block 组装不需要 x/y numerical quadrature；
6. 只有以上全部通过，才讨论 `FORMAL_WHOLE_HALFWAVE_GATE_A = PASS_CLASS_B`。

禁止转去：

```text
generic GKZ expansion
new material fit
Case21 Pu solve
Swartz24
UHPC production fit
shell/Y
spatial quadrature
auxiliary quadrature
```
