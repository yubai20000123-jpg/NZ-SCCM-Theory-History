# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10  
**Purpose:** 唯一当前工作入口。历史 PASS、旧路线和迁移期文件不得覆盖本文件。

## 1. 当前主线

当前工作分成两个层级：

1. 旧 Case21 Nguyen/Foster benchmark 只做短收口，不再继续扩展 theorem-level strict remainder 工具链；
2. 新正式主线是：

```text
finite analytic kinematics
-> finite strain invariants
-> strong nonlinear material law
-> exact analytic material/structural contraction
-> P, Rq, analytic tangent, L
```

结构目标继续保留：

```text
P(D,q)
Rq(D,q)=0
L(D,q)=P_,D Rq_,q-P_,q Rq_,D=0
```

不因旧 integrand 难积分而改变结构力学问题。

## 2. 不可退让的积分身份

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT
ELEMENT_INTEGRATION = PROHIBITED
MATERIAL_POINT_GRID = PROHIBITED
```

允许引入辅助积分变量或更高维 representation，但 production formula 必须把辅助变量解析消元，或最终只保留有限、明确、可解析求导的 closed special functions。对辅助变量做 numerical quadrature 仍然不具有正式理论身份。

## 3. Case21 不变量/精确矩层已经闭合

当前推导：

- `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`
- `current/theory/nz_sccm_case21_invariant_exact_moments_v1.py`

对冻结 Nguyen 二阶运动学，令

```text
u = sin X
v = sin Y
z = zeta
M = Cm(q)
B = Cb(q)
```

则：

- `I1=tr(X)` 是有限 `u,v,z` 多项式；
- `I2=det(X)` 中全部 `M^2` 项严格抵消；
- `I1,I2` 均可消去显式 `cos X, cos Y`；
- polynomial material law 时，P/Rq 可归结为 `sin^a X sin^b Y zeta^h` 的有限 Beta/Gamma/有理精确矩。

四族基本结构矩仍为：

```text
J_P^A(m,n) = Mcal[I1^m I2^n]
J_P^B(m,n) = Mcal[I1^m I2^n Xyy]
J_q^A(m,n) = Mcal[I1^m I2^n I1,q]
J_q^B(m,n) = Mcal[I1^m I2^n (I1 I1,q-I2,q)]
```

其中 `Mcal` 是完整连续半波上的解析积分泛函，不是 quadrature。

## 4. 混凝土强非线性是硬门禁

当前材料架构必须同时通过：

```text
Gate A = exact analytic integration
Gate B = concrete nonlinear adequacy
```

低阶 generic material 只能做 algebra unit test，不能证明极限承载力材料架构可行。

材料级至少应覆盖：初始刚度、压缩非线上升、峰值、峰后、拉伸峰值及软化/硬化、CC 增强、TC coupling，以及同一 law 的解析 tangent；若材料证据最终要求 history，必须采用有限全局 internal-variable representation，不能回到材料点状态机。

门禁文件：

`current/theory/NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`

## 5. M1 simple structured matrix polynomial 已首轮 FAIL-screen

新增：

- `current/theory/NZ_SCCM_M1_STRUCTURED_MATRIX_POLYNOMIAL_SCREEN_R01_20260810.md`
- `current/theory/nz_sccm_m1_structured_matrix_polynomial_screen_r01.py`

测试形式：

`s_i = p(e_i) + A_c(mu,r^2) + B_c(mu,r^2)e_i`

其中 `p(e)` 用高阶单变量 polynomial 表达强 tension/compression 主形状，`A_c/B_c` 表达多轴 interaction。

在 frozen NC material oracle 的宽材料域 `[-2,0.6]^2` 上，单变量主曲线不能显著降低 TC interaction 所需二维复杂度。`p-degree=12`、interaction degree 从 4 提到 12 时，95% `sigma/fc` 绝对误差约从 0.245 降到 0.109，但 independent coefficients 从 38 增到 182，condition number 从约 `1.2e3` 恶化到 `1.8e8`；TC ratio path 仍明显最差。

正式身份：

```text
M1_R01_SIMPLE_ADDITIVE_STRUCTURED_POLYNOMIAL = FAIL_SCREEN
```

这不等于所有 structured analytic law 失败；它否定的是“强一维曲线 + 很弱低阶二维修正”这一简单架构。

## 6. 新数学突破：s=I1 不变量坐标精确变换

新增：

- `current/theory/NZ_SCCM_INVARIANT_COORDINATE_LIFT_EXACT_REDUCTION_R01_20260810.md`
- `current/theory/nz_sccm_invariant_coordinate_lift_r01.py`

Case21 有特殊结构：

```text
I1 = a(u,v;D,q) + 2 B u v z
```

所以 I1 对厚度坐标 z 严格 affine。可精确换元：

```text
s = I1
z = (s-a)/(2Buv)
ds = 2Buv dz
s± = a ± 2Buv
```

代入后 `I2(s;u,v)` 对 s 仅为二次多项式。该恒等式已经用 SymPy exact check。

因此，对 rational invariant material law

```text
A(I1,I2)=P_A/Q_A
B(I1,I2)=P_B/Q_B
```

固定 `(u,v)` 后，P/Rq 的“材料方向” integrand 成为 s 的有限 rational function，可用 partial fractions/Hermite reduction 精确积分；不需要在材料强非线性上先做高阶全局 polynomial surrogate。

这一步只消去一维，尚未证明剩余 `(u,v)` 二维积分全部闭合。

## 7. 高维/辅助变量路线的当前身份

用户提出通过 4D/更高维 representation 简化原三重积分。该方向正式纳入当前数学路线，但原则是：

```text
higher dimension is useful only if it lowers algebraic complexity
and the added variables can be analytically eliminated.
```

当前比较：

- Laplace/Gamma lift：可消除分母，但通常产生 `exp(-t Q(u,v,z))`，不自动进入有限 moment algebra；仅升维不足以 PASS；
- auxiliary-field / algebraic-delta lift：只有 level-set/fiber geometry 变简单时才有价值；
- coarea/pushforward：可把 `F(I1,I2)` 与 kinematic density 分离，是值得保留的后续路线；
- Case21 `s=I1` exact coordinate transform：目前比一般 4D/5D lift 更直接，已得到实质性解析降维。

正式禁止：

```text
3D hard integral -> add auxiliary t -> numerical quadrature in t
```

## 8. 当前最高优先级材料候选

M1-R01 simple polynomial 不再继续堆阶。新的优先候选为：

```text
M1R = source-shaped rational/algebraic material primitives
      + invariant/tensor basis
      + s=I1 exact inner elimination
```

原因：Saenz 型压缩本身已经证明强非线性可以由低阶 rational primitive 表达；若 tension、CC/TC/TT interaction 也能构造为材料来源约束的低参数 rational/algebraic law，则有机会同时满足强非线性与解析积分，而不需要几百个二维自由 polynomial coefficients。

下一执行任务：选取一个材料级、非结构反标的 rational/invariant prototype，分别对 P 与 Rq 完成 `s=I1` exact inner integration，再检查剩余 `(u,v)` integrals 是 Class A（elementary/Beta/Gamma/log/atan）还是有限 Class B（elliptic/Appell/hypergeometric/GKZ）。

## 9. 旧 NC + reinforcement benchmark

仍保留用于 regression/reference：

- `current/theory/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`
- `current/theory/nz_sccm_current_operator_explicit_v1.py`

它是 benchmark，不再是永久 final material law。钢筋仍必须在 root solve 前进入 P 与 Rq；禁止 `Pu=Pu,concrete+As fy`。

## 10. UHPC / shell 当前边界

UHPC 不能只替换 NC 的 `fc`；仅 `fc=141.1 MPa` 为用户强制冻结值。UHPC 与 NC 可共享 invariant/tensor-basis + exact analytic architecture，但 scalar laws、内部变量和参数必须使用各自材料证据。

最终 production shell operator 仍未冻结：

`M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE`。

PBL 继续作为强局部边界/子板分隔，不自动作为独立轴向承载项或显式弹簧能量。

## 11. 后续恢复读取

新对话优先读取：

1. 本文件；
2. `NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`；
3. `NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`；
4. `NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`；
5. `NZ_SCCM_M1_STRUCTURED_MATRIX_POLYNOMIAL_SCREEN_R01_20260810.md`；
6. `NZ_SCCM_INVARIANT_COORDINATE_LIFT_EXACT_REDUCTION_R01_20260810.md`。

历史只在追溯 provenance/路线裁决时进入 `history/`。
