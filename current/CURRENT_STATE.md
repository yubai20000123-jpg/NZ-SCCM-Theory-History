# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10  
**Purpose:** 唯一当前工作入口。历史 PASS、旧路线、迁移期文件不得覆盖本文件。

## 1. 不可改变的结构目标与空间边界

```text
finite analytic kinematics
-> finite strain invariants
-> strong nonlinear material law
-> direct exact analytic material/structural contraction
-> P, Rq, analytic tangent, L
```

结构目标固定：

```text
P(D,q)
Rq(D,q)=0
L(D,q)=P_,D Rq_,q-P_,q Rq_,D=0
```

formal identity：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
KINEMATICS = NGUYEN_SECOND_ORDER / CURRENT CASE21 FINITE ANALYTIC KINEMATICS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT
ELEMENT_INTEGRATION = PROHIBITED
MATERIAL_POINT_GRID = PROHIBITED
SPATIAL_CELLS = PROHIBITED
GAUSS_SIMPSON_ADAPTIVE = PROHIBITED_IN_FORMAL_OPERATOR
COLLOCATION_AS_FORMAL_OPERATOR = PROHIBITED
```

2026-08-10 自检后进一步冻结：

```text
N_auxiliary_numerical_quadrature = 0
N_auxiliary_ODE_steps = 0
NO hidden initial-value integration
NO large connection system as production operator
```

finite differential / Gauss-Manin / Picard-Fuchs systems仍可作为数学分类或可行性审计，但不再因为“有限维”自动获得 production 身份。

当前治理锁：

- `governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`
- `governance/PF1_R05_GOAL_RELEVANCE_CHECKPOINT_20260810.md`
- `governance/PF1_R06_PRODUCTION_COMPLEXITY_SELF_AUDIT_20260810.md`

## 2. Case21 结构—不变量基础继续有效

保留：

- `current/theory/NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`
- `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`

Case21：

```text
q=A/b
M=Cm(q)=pi^2/eps0*(q0*q+q^2/2)
B=Cb(q)=pi^2/(2 eps0)*(t/b)*q
```

归一化二维不变量：

```text
I1=(nu-1)D+M H+2B W
I2=-nu D^2 + D M K + B D(nu-1)W
   + B M W(2-u^2-v^2)+B^2 z^2(u^2+v^2-1)
```

`I2` 中 `M^2` 项严格抵消；`I1,I2` 为有限 analytic polynomial field。

这部分没有被本次纠偏否定。

## 3. 三个材料/解析门禁

以后材料 compiler 必须同时通过：

```text
Gate A = exact analytic direct closure
Gate B = concrete nonlinear adequacy
Gate C = production analytic complexity
```

### Gate C 当前硬要求

```text
1. original x/y/z numerical quadrature = 0
2. auxiliary numerical quadrature = 0
3. auxiliary ODE stepping = 0
4. no hidden numerical initialization
5. no branch-by-branch spatial/material state propagation
6. P, Rq and derivatives must reduce to direct finite formulas
7. named special functions are allowed only as direct evaluable functions
8. auxiliary matrix >3x3 is presumptive FAIL unless analytically eliminated
9. complexity may scale with a finite material basis only
10. canonical theory must expose actual formulas, not only a script regenerating a huge symbolic object
```

## 4. M1 与 M1R-R01 的当前身份

旧 M1 simple additive structured polynomial：

```text
M1_R01_SIMPLE_ADDITIVE_STRUCTURED_POLYNOMIAL = FAIL_SCREEN
```

该失败只针对旧 M1 的具体二维结构，不代表所有 source-shaped finite polynomial primitive representation 都失败。

M1R-R01 保留 frozen-NC source-shaped biaxial algebra：

```text
U
C
C2=C^2
T
V=T^8
```

53 个 material-only rational coefficients，二维 fitted interaction coefficients=0。

frozen-NC material screen：

```text
global P95 = 0.018261
global max = 0.036742
TC P95     = 0.023137
```

身份继续保持：

```text
M1R_R01_FROZEN_NC_ORACLE_REGRESSION = PASS_SCREEN
FINAL_NC_SOURCE_CALIBRATION = NOT_YET_DONE
FINAL_GATE_B = NOT_YET_FROZEN
```

但经过 PF1-R06 自检，必须新增：

```text
M1R_RATIONAL_PRIMITIVE_PRODUCTION_COMPILER = HOLD_NOT_ACCEPTED
```

原因不是材料拟合误差，而是 whole-halfwave production complexity。

## 5. R02-R06：保留为数学可行性审计，不再作为 production mainline

R02 rational resolvent audit：

```text
27 scalar poles
1 constant + 27 consolidated single-pole + 106 pair-pole analytic blocks
M1R_R02_RESOLVENT_CANONICALIZATION = PASS_EXACT
M1R_R02_ACTUAL_S_FACTORS = QUADRATIC_ONLY
```

R03-R05 找到的 genus-2 / Phi / common rational driver exact identities仍然有效；它们说明 rational primitive representation 的解析结构可以被系统研究。

R06 又在 exact witness：

```text
D=1
M=1
nu=1/5
r=2
tau=symbolic
```

得到：

```text
19 critical monomials
-> 4 exact IBP period relations
-> 15 master periods
-> 15x15 symbolic tau connection
-> 211/225 nonzero entries
-> symbolic entry characters about 2.68e5
```

R06 代码使用 exact polynomial coefficient matching / rational-function linear algebra；它本身不是空间数值积分。

但是当前正式重新定级为：

```text
PF1_R03_GENUS2_GAUSS_MANIN = RETAIN_AUDIT_ONLY
PF1_R04_PHI_ENDPOINT_REDUCTION = RETAIN_AUDIT_ONLY
PF1_R05_COMMON_RATIONAL_DRIVER = RETAIN_AUDIT_ONLY
PF1_R06_15X15_CONNECTION_WITNESS = RETAIN_AUDIT_ONLY
PF1_R06_PRODUCTION_ACCEPTANCE = FAIL_COMPLEXITY_GATE
PF1_R07 = CANCELLED
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

## 6. 为什么 R06 不再继续生产化

### 6.1 它不是 current actual generic closed form

15x15 symbolic connection 只在一个 rational witness 上生成；`D/M` connection也只在 witness point 验证。

### 6.2 公式透明度不合格

完整 symbolic matrix 总规模约 2.68e5 字符；canonical result 只冻结 shape、density、common denominator和cross-check，没有把全部可读公式逐项冻结。

### 6.3 隐藏 numerical propagation 风险

若继续用：

```text
dI/dtau = Omega_tau I
```

做 production evaluator，则仍需：

```text
analytic initial values
branch continuation
singular/basis patch
physical tau=B(q)^2 propagation
```

如果 initial values 来自 x/y numerical integration，则直接违反零数值积分；如果沿 tau 做 numerical ODE stepping，则虽然不是空间 quadrature，也已经偏离本项目要求的直接解析、低维、可手算审计路线。

### 6.4 复杂度已经失控

仅 single-pole bookkeeping 就有潜在：

```text
27 pole families x 15 master periods = 405 master-period components
```

pair block虽然可复用 single-pole families，但仍有106个assembly couplings，再叠加 D/M/q derivative 与 branch patch。继续R07预计只会放大该问题。

## 7. 真正的路线错误位置

问题不是 R06 的 IBP 恒等式错误，而是更早的 compiler 设计顺序：

```text
先按材料拟合精度选 rational primitives
-> 再试图救 whole-halfwave exact integration
```

正确顺序应改为：

```text
source-shaped material physics
-> choose material primitive basis under BOTH material-accuracy and direct-integrability constraints
-> only then compile to exact moments
```

也就是说，**whole-halfwave direct integrability / production complexity 必须与材料精度同时成为硬门禁**。

## 8. 当前回退范围

不回退：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
I1/I2 invariant foundation
source-shaped biaxial material algebra
D15/exact-moment philosophy
Gate B nonlinear material target
```

只回退：

```text
rational primitive representation as production compiler
```

## 9. 当前唯一建议下一任务

```text
CURRENT_RECOMMENDED_NEXT_TASK = M1R_P2_INTEGRABILITY_FIRST_PRIMITIVE_COMPILER_SCREEN
```

P2 只允许做一个小规模 fail-fast screen：

```text
same source-shaped U/C/C2/T/V algebra
+ finite 1D polynomial or orthogonal-polynomial primitive representations
+ direct composition with Case21 finite invariants
+ direct D15/Beta exact moments
```

这不是恢复旧 M1 2D polynomial fit，也不是重开材料物理；只是在同一 source-shaped physics 下重新选择 compiler basis。

P2 的硬停止条件：

```text
如果合理一维阶次仍无法同时满足材料误差和 Gate C，立即 FAIL/STOP；
不得再通过更高维 master systems、parameter ODE 或 large matrices 强行救活。
```

本轮纠偏不自动开始 P2 计算。

## 10. 其他材料/结构边界不变

旧 NC + reinforcement operator 仍仅为 regression/reference。钢筋必须在 root solve 前进入：

```text
P=Pc+Ps
Rq=Rq,c+Rq,s
```

不得事后 `Pu=Pu,c+As fy`。

UHPC：仅 `fc=141.1 MPa` 为用户强制冻结；final strong multiaxial production operator 尚未闭合。

shell/Y：

```text
M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE
```

PBL 继续作为强局部边界/子板分隔，不自动作为独立轴向承载项或显式 spring energy。

## 11. 当前明确未执行

```text
NO PF1-R07
NO new Case21 Pu solve
NO Swartz24 solve
NO UHPC production fit
NO shell/Y production solve
NO structural Pu calibration
NO spatial numerical quadrature
NO auxiliary numerical quadrature
NO auxiliary ODE stepping
NO endpoint cells
NO material-point integration
NO route switch
```

## 12. 后续恢复优先读取

1. `current/CURRENT_STATE.md`
2. `governance/PF1_R06_PRODUCTION_COMPLEXITY_SELF_AUDIT_20260810.md`
3. `governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`
4. `governance/PF1_R05_GOAL_RELEVANCE_CHECKPOINT_20260810.md`
5. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`
6. `current/theory/NZ_SCCM_M1R_SOURCE_SHAPED_RATIONAL_PRIMITIVE_SCREEN_R01_20260810.md`
7. `current/theory/NZ_SCCM_PF1_ENDPOINT_IBP_MASTER_CONNECTION_R06_20260810.md`
