# NZ-SCCM — “不要陷入循环”含义二次校正：保留紧致精确闭合方向，禁止高阶逐项枚举

**时间：2026-08-17 00:36 +08:00**

## 1. 用户原意恢复

项目此前已明确：

- 可以把理论写成无限项或很高阶的解析级数；
- 可以逐项展开若干项用于理论解释、来源审计与手算说明；
- 但生产计算不能真的去生成、存储、求解或逐项收缩上千/几千/更多解析系数；
- 因而“不要陷入循环”不是否定 exact / holonomic / closed-moment 方向，而是要求该方向最终必须收口成一个紧致、固定维度或有明确有限复杂度上界的可执行算子。

历史 18:41 锁定：

```text
FORMAL_INFINITE_SERIES = ALLOWED_AS_REPRESENTATION
TERM_BY_TERM_EXPANSION_FOR_AUDIT = ALLOWED
expand-all-then-solve-thousands-of-orders = PROHIBITED
preferred implementation = formal/nested series + exact recurrence or target-functional moment contraction
```

因此 00:28 将主线改写成“source-faithful finite analytic material representation / specimen-derived order”仍然不够准确，容易重新滑向 N=1000/3000/5000 的直接高阶枚举。该表述现在撤回。

## 2. 正确恢复点不是 19:12，而是 21:18 前后的 compact exact branch

19:12 完成五项膜内物理闭合与 General-D15 target 定义。

19:32 证明普通 polynomial/nested-Chebyshev flattening 即使转为 adjoint Clenshaw，仍然传播巨大次数；这一失败说明“高阶逐项表示”不应成为生产实现。

20:59 随后的 quadratic-tower 路线取得了关键突破：

```text
THREE_GENERATOR_QUADRATIC_TOWER = PASS_EXACT_PARAMETRIC
FULL_COMPOSITUM_STATE_DIMENSION = 64
FULL_DERIVATIVE_OPERATOR_NONZEROS = 159 / 4096
FULL_64_STATE_VECTOR_MOMENT_FORM = PASS_EXACT
NO_POLYNOMIAL_DEGREE_GROWTH_PATH = YES
```

每次乘法/微分都约回同一个固定 64-state algebraic field，因此它第一次真正满足“形式上可无限/复杂，但生产计算不逐项算几千项”的项目目标。

21:18 又进一步锁定：

```text
T7_MATRIX_POWER_PRODUCTION_NODE = ELIMINATED_EXACT_BY_2X2_CH
T7_MATRIX_DERIVATIVE_PRODUCTION_NODE = ELIMINATED_TO_SCALAR_CH_RECURRENCE
FULL_R10_COMPACT_STRESS_TARGET = PASS_EXACT
FIELD_PRODUCT_ADJOINT_PULLBACK = PASS_EXACT
FINAL_64_COEFFICIENT_CANONICALIZATION = PROHIBITED
```

因此当前正确主线应从 21:18 compact target DAG + 64-state exact field 继续，而不是回退到 high-order finite compiler。

## 3. 当时为什么仍让用户产生“循环不出结果”的感觉

方向本身并没有错，执行治理出了问题。

每个 gate 都证明了一个局部数学对象，但没有预先规定一个“终点复杂度合同”。于是：

```text
nested target
 -> adjoint Clenshaw
 -> quartic algebraic period
 -> holonomic thickness
 -> 64-state compositum
 -> adjoint CH
 -> dual-holonomic gauge
 -> apparent-pole regularization
 -> ...
```

每解决一层都可以再产生下一层，且没有在进入下一 gate 前证明：

1. 剩余 open layers 数量严格减少；
2. 最终 runtime state dimension 不再增长；
3. 不需要 materialize 1000+ coefficients；
4. 下一步完成后能够直接返回 `P,Rq,Rm,L,KZ` 中至少一个真实 target；
5. 最多还剩多少个数学闭合步骤。

所以问题不是“方向循环错了”，而是“循环没有收敛指标和终止证明”。

## 4. 21:36 apparent-pole 的正确身份

21:36 发现 rationalized local basis 在 `x=21/260` 有 apparent pole，而 physical algebraic atom 正则，并且 `c0+c1*q` 极限有限。

这说明：

```text
64_STATE_COMPACT_FIELD = NOT REJECTED
PHYSICAL_R10_ATOM = REGULAR
RATIONALIZED_LOCAL_CONNECTION_BASIS = NEEDS REGULARIZATION
```

不应该由此退回 N48；也不应自动开启无限层的新 symbolic backend。

正确任务是：只对这个 fixed-state algebraic connection 做一次全局正则化，使其保持固定有限状态，然后继续完成 target contraction。

## 5. 新的“收口合同”

从现在起，compact exact branch 只有两个尚未完成的生产层：

```text
OPEN_LAYER_1 = globally regular fixed-state thickness target contraction
OPEN_LAYER_2 = beta-weighted X,Y exact target contraction
```

不得再把它们拆成无限个自动派生的“下一代 backend”。

每一层必须满足：

```text
A. formal infinite/high-order representation may remain symbolic
B. runtime must NOT enumerate thousands of coefficients/terms
C. runtime state dimension/order must have an explicit finite bound before implementation
D. bound must be independent of requested Chebyshev/truncation order because no such high-order truncation is the production mechanism
E. result must directly contract actual P/Rq/Rm/L/KZ kernels
F. if the proposed regularization makes state dimension/order start growing without a proven cap, FAIL immediately
```

## 6. 当前推荐执行路线

```text
21:18 compact R10 stress/tangent target DAG + fixed 64-state quadratic tower
 -> regularize the local algebraic connection at removable apparent poles WITHOUT spatial subdivision and WITHOUT coefficient enumeration
 -> close exact thickness target moments in the same fixed/bounded state
 -> close beta-weighted X,Y target moments with a finite recurrence/creative-telescoping operator
 -> evaluate actual P,Rq,Rm,L,KZ
 -> Case21 low-effect control
 -> Z6 mixed-boundary high-effect decisive case
```

形式理论可继续写为无限项/逐项展开；实际程序只操作固定状态、有限递推、端点量和少量广义坐标。

## 7. 禁止回归

```text
DIRECT_N1000_N3000_N5000_COEFFICIENT_ENUMERATION = PROHIBITED
HIGH_ORDER_CHEBYSHEV_AS_PRODUCTION_ESCAPE = PROHIBITED
FULL_SERIES_FLATTENING = PROHIBITED
FULL_64_COEFFICIENT_CANONICALIZATION = PROHIBITED
SPATIAL_QUADRATURE/COLLOCATION/MATERIAL_POINT_GRID = PROHIBITED
N48_LEGACY_FALLBACK = PROHIBITED_AS_FIX_FOR_COMPACT_BRANCH_BLOCKER
```

## 8. 当前唯一下一任务

`FIXED_STATE_GLOBAL_REGULARIZATION_AND_THICKNESS_TARGET_CLOSURE`

它不是“再开发一个通用积分后端”，而是把已经存在的 64-state compact exact field 从局部 rationalized connection 改写成 globally regular fixed-state connection，并立即对一个实际 `P/Rm` thickness target 完成 end-to-end contraction。

若无法在预先证明的固定有限状态内完成，则停止并报告该 compact route 的具体数学阻断；不得改成几千项直接枚举来“算出结果”。
