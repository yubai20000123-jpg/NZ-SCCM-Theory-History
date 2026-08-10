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

## 5. M1 simple structured matrix polynomial 已 FAIL-screen

- `current/theory/NZ_SCCM_M1_STRUCTURED_MATRIX_POLYNOMIAL_SCREEN_R01_20260810.md`
- `current/theory/nz_sccm_m1_structured_matrix_polynomial_screen_r01.py`

测试形式：

`s_i = p(e_i) + A_c(mu,r^2) + B_c(mu,r^2)e_i`

在 frozen NC material oracle 的宽材料域 `[-2,0.6]^2` 上，即使 `p-degree=12`、interaction degree=12，仍需要 182 个 independent coefficients；P95 `|Delta sigma/fc|≈0.10869`，max≈0.41314，TC ratio path P95≈0.37460，且 condition number 约 `1.8e8`。

正式身份：

```text
M1_R01_SIMPLE_ADDITIVE_STRUCTURED_POLYNOMIAL = FAIL_SCREEN
```

这否定的是“强一维曲线 + 很弱低阶二维自由 polynomial 修正”这一简单架构，不是否定全部 structured analytic material laws。

## 6. `s=I1` 不变量坐标精确变换已经成立

- `current/theory/NZ_SCCM_INVARIANT_COORDINATE_LIFT_EXACT_REDUCTION_R01_20260810.md`
- `current/theory/nz_sccm_invariant_coordinate_lift_r01.py`

Case21 有：

```text
I1 = a(u,v;D,q) + 2 B u v z
```

所以可严格换元：

```text
s = I1
z = (s-a)/(2Buv)
ds = 2Buv dz
s± = a ± 2Buv
```

代入后 `I2(s;u,v)` 对 s 仅为二次多项式。该恒等式已 exact check。

因此 rational invariant material law 在固定 `(u,v)` 后，对 P/Rq 的材料/厚度方向 integrand 是有限 rational function of `s`。

## 7. M1R source-shaped rational primitive 已获得正材料筛选结果

新增：

- `current/theory/NZ_SCCM_M1R_SOURCE_SHAPED_RATIONAL_PRIMITIVE_SCREEN_R01_20260810.md`
- `current/theory/nz_sccm_m1r_source_shaped_rational_r01.py`
- `current/theory/NZ_SCCM_M1R_SOURCE_SHAPED_RATIONAL_PRIMITIVE_SCREEN_R01_results.json`

M1R-R01 不再拟合自由二维 `A/B` surface，而保留 frozen-NC benchmark 的 source-shaped biaxial algebra，仅把五个一维 scalar primitives 编译为有限 rational functions：

```text
U(lambda)
C(lambda)
C2(lambda)=C(lambda)^2
T(lambda)
V(lambda)=T(lambda)^8
```

重构：

```text
s_i = U_i - a_cc C2_i C_j + C_i T_j - rho a_t T_i V_j
```

共 53 个一维 material-only rational coefficients，二维 fitted interaction coefficients = 0。

与旧 M1-R01 在同一 frozen-NC physical principal-strain domain `[-2,0.6]^2` 上比较：

| architecture | coefficients | global P95 | global max | TC P95 |
|---|---:|---:|---:|---:|
| M1-R01 | 182 | 0.10869 | 0.41314 | 0.37460 |
| **M1R-R01** | **53** | **0.018261** | **0.036742** | **0.023137** |

R01 诊断材料域内五个 rational primitives 均无实极点。

当前身份：

```text
M1R_R01_FROZEN_NC_ORACLE_REGRESSION = PASS_SCREEN
FINAL_NC_SOURCE_CALIBRATION = NOT_YET_DONE
FINAL_GATE_B = NOT_YET_FROZEN
```

这是 architecture-level 正结果，不得把 frozen benchmark 的误差阈值直接升级为最终材料来源验收标准。

## 8. M1R 的 `s=I1` 内层 exact integration 已 PASS Class A

对 scalar quadratic denominator factor

```text
d(lambda)=1+p lambda+q lambda^2
```

二维 Cayley-Hamilton 后，其 matrix denominator determinant 为

```text
Delta = 1+p I1+q I1^2
      +(p^2-2q) I2
      +pq I1 I2
      +q^2 I2^2
```

由于 `I2(s)` 对 `s` 二次，故每个 quadratic scalar denominator factor 在 `s` 中至多四次；linear scalar factor 至多二次。

同时 Case21 结构权重：

```text
Xyy(s)   degree <= 1
I1,q(s)  degree <= 1
Gq(s)    degree <= 2
```

因此真实 M1R 的 P/Rq material blocks 在固定 `(u,v)` 后均为 `s` 的 finite rational functions，可用 factor-aware Hermite reduction / partial fractions 精确积分。

正式身份：

```text
M1R_R01_S_INNER_INTEGRATION = PASS_CLASS_A
N_s_quadrature = 0
```

实现时禁止先把全部 primitive denominators 暴力相乘成巨型多项式；必须保留 factor structure。

## 9. 表观 `1/(uv)` 已解析消除；outer `(x,y)` 仍是当前唯一主门禁

对精确 s-antiderivative `calF`，令

```text
s± = a ± c
c = 2Buv
D_calF(a,c) = [calF(a+c)-calF(a-c)]/(2c)
```

则 endpoint difference 与变换 Jacobian 中的 `1/(uv)` 精确抵消：

```text
Mcal = 8 int_0^1 int_0^1
       D_calF(a,2Buv)
       /[sqrt(1-u^2)sqrt(1-v^2)] du dv
```

再令 `x=u^2,y=v^2`：

```text
Mcal = 2 int_0^1 int_0^1
       D_calF(a(x,y),2B sqrt(xy))
       /sqrt[x(1-x)y(1-y)] dx dy
```

因此剩余问题已规范化成 **Beta-weighted two-variable algebraic/logarithmic period**，但尚未逐 actual M1R factor family 证明有限 special-function closure。

当前正式身份：

```text
M1R_R01_OUTER_XY = CLASS_B_CANDIDATE / NOT_YET_CLOSED
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

这就是当前新的准确停点。

## 10. 当前下一唯一执行任务

不是 Case21 Pu，也不是 Swartz24。下一步为：

```text
actual M1R factor blocks
-> exact s antiderivatives
-> symmetric endpoint divided differences
-> x=u^2, y=v^2
-> classify and close outer families
```

优先分类：

1. Beta / elementary / algebraic-log Class A；
2. Appell / Horn；
3. elliptic / generalized hypergeometric；
4. GKZ / Picard-Fuchs periods。

PASS 条件：最终只保留有限 named special functions/finite analytic objects，可稳定求值并对 `D,q` 解析求导形成 tangent 和 `L`，且无 auxiliary/spatial numerical quadrature。

若这一步 FAIL，再测试 joint pushforward/coarea；仍不得回到空间 Gauss/cells/material points。

## 11. 钢结构 non-discretization / semi-analytical 稳定方法正式纳入参考路线

新增 evidence：

`evidence/stability/STEEL_NONDISCRETIZATION_SEMIANALYTIC_REFERENCE_MAP_20260810.md`

已确认钢板稳定/极限强度文献中存在：

- Rayleigh–Ritz based **non-discretization** inelastic plate buckling；
- large-deflection + incremental Rayleigh–Ritz postbuckling/ultimate strength；
- analytical Airy stress function + trigonometric displacement series + variational amplitude solution；
- Koiter nonlinear postbuckling / imperfection-sensitivity framework。

其当前身份：

```text
REFERENCE_LANE_STEEL_NONDISCRETIZATION = RETAIN
ROLE = STRUCTURAL_METHOD_REFERENCE_ONLY
CURRENT_NC_MATERIAL_AUTHORITY = NONE
CURRENT_UHPC_MATERIAL_AUTHORITY = NONE
CURRENT_FORMAL_INTEGRATION_OVERRIDE = NONE
```

可用于后续：连续场/有限 generalized-coordinate 构造、变分核验、平衡路径/极限点/分岔解释、imperfection sensitivity、modal interaction、shell/Y 模块、analytic basis enrichment convergence。

不得据此引入：spatial quadrature、material-point incremental integration、topological FEM、von-Mises cutoff 替代 NC/UHPC 材料、或 effective-width empirical closure。

创新边界同步修正：**“不用 FEM、用连续假定场+积分”本身已有钢结构先例，不能单独作为核心创新。** NZ-SCCM 更应把创新性放在 `strong multiaxial NC/UHPC + source-shaped analytic compiler + invariant/tensor reduction + exact whole-halfwave contraction + zero formal spatial quadrature/material points + analytic tangent + P/Rq/L ultimate system + compatible shell/Y coupling` 这一组合架构上。

## 12. 高维/辅助变量路线的当前身份

更高维 representation 仍保留，但原则不变：

```text
higher dimension is useful only if it lowers algebraic complexity
and the added variables can be analytically eliminated.
```

- Laplace/Gamma lift：仅升维不足以 PASS；
- auxiliary-field/algebraic-delta：只有 fiber geometry 真正变简单才有价值；
- coarea/pushforward：作为 M1R outer closure 失败后的后续候选；
- 当前 `s=I1` exact coordinate transform 优先于一般 4D/5D lift。

禁止：

```text
3D hard integral -> add auxiliary t -> numerical quadrature in t
```

## 13. 旧 NC + reinforcement benchmark

仍保留用于 regression/reference：

- `current/theory/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`
- `current/theory/nz_sccm_current_operator_explicit_v1.py`

它是 benchmark，不是永久 final material law。钢筋仍必须在 root solve 前进入 `P` 与 `Rq`；禁止 `Pu=Pu,concrete+As fy`。

## 14. UHPC / shell 当前边界

UHPC 不能只替换 NC 的 `fc`；仅 `fc=141.1 MPa` 为用户强制冻结值。UHPC 与 NC 可共享 invariant/tensor-basis + exact analytic architecture，但 scalar laws、内部变量和参数必须使用各自材料证据。

最终 production shell operator 仍未冻结：

```text
M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE
```

PBL 继续作为强局部边界/子板分隔，不自动作为独立轴向承载项或显式弹簧能量。

## 15. 本阶段明确未执行

```text
NO new Case21 Pu solve
NO Swartz24 solve
NO UHPC production fit
NO shell/Y production solve
NO structural Pu calibration
```

## 16. 后续恢复读取

新对话优先读取：

1. 本文件；
2. `current/theory/NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`；
3. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`；
4. `current/theory/NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`；
5. `current/theory/NZ_SCCM_M1_STRUCTURED_MATRIX_POLYNOMIAL_SCREEN_R01_20260810.md`；
6. `current/theory/NZ_SCCM_INVARIANT_COORDINATE_LIFT_EXACT_REDUCTION_R01_20260810.md`；
7. `current/theory/NZ_SCCM_M1R_SOURCE_SHAPED_RATIONAL_PRIMITIVE_SCREEN_R01_20260810.md`；
8. `evidence/stability/STEEL_NONDISCRETIZATION_SEMIANALYTIC_REFERENCE_MAP_20260810.md`。

历史只在追溯 provenance/路线裁决时进入 `history/`。
