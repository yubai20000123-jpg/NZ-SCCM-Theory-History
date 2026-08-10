# PF1-R06 生产复杂度自检与路线纠偏 — 2026-08-10

**Status:** CURRENT GOVERNANCE CORRECTION / PF1-R07 CANCELLED

## 0. 用户质疑

用户指出：R06 已形成 `15×15` connection，225 个位置中 211 个非零，且仍缺 initial values、branch patch、generic connection、production evaluator。若继续推进，很可能只是把积分包装成“解析矩阵”，并产生明显数值/符号膨胀。

本文件对此做正式自检。

## 1. 先区分一个事实：R06 本身不是空间数值积分

R06 代码没有调用 Gauss/Simpson/adaptive quadrature、空间采样、材料点积分，也没有数值 ODE 求解。它在 witness

```text
D=1, M=1, nu=1/5, r=2
```

上，以 `Q(tau)` 为系数字段，利用 polynomial coefficient matching + SymPy `linsolve` 求出 rational-function connection coefficients。

因此：

```text
R06_15X15_MATRIX != spatial numerical quadrature
R06_15X15_MATRIX != material-point integration
```

但这只说明它是一个 **exact symbolic differential representation witness**，并不说明它是可接受的 production analytic operator。

## 2. 用户的核心判断成立：R06 已越过工程可接受复杂度边界

### 2.1 15×15 / 211 nonzero 已是明显的辅助状态膨胀

R06 witness：

```text
master periods = 15
connection entries = 225
nonzero entries = 211
symbolic entry characters ≈ 2.68e5
max entry characters = 1699
```

并且当前 M1R 有：

```text
27 scalar poles
106 pair-pole blocks
```

pair block 虽可复用 single-pole period family，但仅 single-pole bookkeeping 已达到：

```text
27 pole families × 15 master periods = 405 master-period components
```

再叠加 `P/Rq` weights、`D/M/q` derivatives、branch/basis patch 与 pair assembly，已经明显违背项目原先追求的：

```text
small finite analytic operator
cost grows with a small number of named analytic terms
not with a large hidden auxiliary state system
```

### 2.2 R06 只有 witness connection，不是 actual production closed form

当前 explicit symbolic `Omega_tau` 只在：

```text
D=1, M=1, nu=1/5, r=2
```

的 rational witness 上生成。

它没有给出 current actual `(D,M,nu,r)` 的统一显式 closed form；`D/M` 也仅在 `tau=1/7` witness point 验证 reduction。

因此不能把：

```text
PASS_EXACT_SYMBOLIC_15X15_WITNESS
```

解释为：

```text
PRODUCTION_ANALYTIC_OPERATOR_CLOSED
```

### 2.3 canonical result artifact 甚至没有逐项冻结完整矩阵

R06 result artifact 只冻结：

```text
shape
nonzero count
common denominator
cross-check
```

而完整 15×15 symbolic matrix 仅“由脚本可重新生成”，没有逐项作为可读公式列入 canonical theory/result。

这与项目的“公式本身透明、可手工审计”目标不一致。

### 2.4 initial-value problem 是真正的隐藏数值积分风险

即使 connection equation 写成：

```text
dI/dtau = Omega_tau(tau) I
```

生产 evaluator 仍必须知道：

1. analytic initial values `I(tau0)`；
2. branch continuation；
3. singular-point crossing / basis patch；
4. how to evaluate the system along physical `tau=B(q)^2`.

如果后续通过：

```text
original x/y numerical integral -> initialize I
```

则直接违反 zero-quadrature 目标。

如果后续通过：

```text
numerical ODE stepping in tau
```

虽然它不再是“空间 quadrature”，但对本项目的实际目的而言，本质上仍变成一个需要步进、误差控制、奇点绕行和状态传播的数值积分器。它不符合用户要求的紧凑直接解析计算路线。

因此从本文件开始，production gate 进一步收紧：

```text
N_auxiliary_ODE_steps = 0
N_auxiliary_numerical_integration = 0
```

finite differential systems 只可作为数学存在性/分类工具，不再自动获得 production 身份。

## 3. 真正出错的位置

错误不在 R06 的 polynomial IBP algebra；该 algebra 作为数学 audit 可以成立。

真正的路线错误发生在更早一层：

```text
先选择高精度 rational primitive representation
-> 再试图把它强行编译成 whole-halfwave exact operator
```

R01 rational primitives 的材料拟合表现很好，但其 denominator 产生：

```text
27 scalar poles
resolvent denominators Delta_r
common driver D_r(x,y;tau)
finite algebraic periods
Picard-Fuchs / master connections
```

也就是说，我们在选择材料 compiler representation 时，只把“材料空间精度”作为强门槛，却没有把：

```text
最终 whole-halfwave contraction 的直接可积性 + operator complexity
```

同时作为硬门槛。

结果是：材料函数变简单了，结构积分却变得比原问题更重。

这是当前最关键的自检结论。

## 4. 对 R03-R06 的重新定级

R03-R06 不删除，也不判为数学错误；它们保留为：

```text
ANALYTIC_FEASIBILITY_AUDIT / NON-PRODUCTION
```

具体：

```text
PF1_R03_GENUS2_GAUSS_MANIN = RETAIN_AUDIT_ONLY
PF1_R04_PHI_ENDPOINT_REDUCTION = RETAIN_AUDIT_ONLY
PF1_R05_COMMON_RATIONAL_DRIVER = RETAIN_AUDIT_ONLY
PF1_R06_15X15_CONNECTION_WITNESS = RETAIN_AUDIT_ONLY
PF1_R06_PRODUCTION_ACCEPTANCE = FAIL_COMPLEXITY_GATE
PF1_R07 = CANCELLED
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

这里 `FAIL_COMPLEXITY_GATE` 不是说 exact identities 错，而是说该表示不满足项目的 production simplicity / transparency / no-hidden-stepping 要求。

## 5. 新增 production analytic complexity gate

以后任何材料 compiler 表示，除了 Gate A / Gate B，还必须先过 Gate C：

```text
Gate C = production analytic complexity
```

Gate C 最低要求：

```text
1. original x/y/z numerical quadrature = 0
2. auxiliary numerical quadrature = 0
3. auxiliary ODE stepping = 0
4. no hidden initial-value integration
5. no branch-by-branch spatial/material state propagation
6. final P, Rq and derivatives must be direct finite formulas
7. named special functions are allowed only as direct evaluable functions
8. any auxiliary matrix > 3x3 is presumptive FAIL unless analytically eliminated to a named scalar/small function family
9. formula complexity must scale with finite material basis terms, not with spatial points, ODE steps, poles×master states, or singular patches
10. canonical theory must expose the actual formulas, not merely a script that regenerates a very large matrix
```

## 6. 当前应该回退到哪一层

不回退结构运动学、不回退 invariants、不回退 source-shaped biaxial physics。

保留：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
I1/I2 exact invariant foundation
source-shaped U/C/C2/T/V material algebra
D15 / exact moment philosophy
Gate B nonlinear material target
```

只回退 **material compiler representation**：

```text
RATIONAL_PRIMITIVE_PRODUCTION_COMPILER = HOLD / NOT ACCEPTED
```

下一步不再做 PF1-R07，而是先进行一个小规模、fail-fast 的 integrability-first screen：

```text
M1R-P2 = source-shaped finite 1D polynomial / orthogonal-polynomial primitive compiler screen
```

目的不是恢复旧 M1 simple 2D polynomial fit，而是保持同一 source-shaped algebra：

```text
U(lambda), C(lambda), C2(lambda), T(lambda), V(lambda)
```

分别使用有限一维 polynomial / orthogonal-polynomial analytic representation，然后再组成同一二维 source algebra。

如果这些一维 primitive 在合理阶次下可以达到材料误差门槛，则其与 Case21 finite invariant field 复合后直接回到有限 polynomial exact moments，不再需要 poles、resolvent period systems 或 parameter ODE。

如果合理阶次下仍失败，则立即停，不用更高阶/更大矩阵强行救活。

## 7. 当前正式下一任务

```text
CURRENT_RECOMMENDED_NEXT_TASK = M1R_P2_INTEGRABILITY_FIRST_PRIMITIVE_COMPILER_SCREEN
PF1_R07 = CANCELLED
```

本文件只完成路线自检和治理纠偏，不在同一轮偷偷开始 P2 拟合或 Case21 计算。
