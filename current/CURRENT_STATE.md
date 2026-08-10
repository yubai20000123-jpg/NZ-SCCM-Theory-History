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

finite differential / Gauss-Manin / Picard-Fuchs systems可保留为数学审计，但不再因为“有限维”自动获得 production 身份。

当前治理锁：

- `governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`
- `governance/PF1_R05_GOAL_RELEVANCE_CHECKPOINT_20260810.md`
- `governance/PF1_R06_PRODUCTION_COMPLEXITY_SELF_AUDIT_20260810.md`
- `governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md`

以后任何“执行/PASS/闭合”必须在聊天中公开实际公式、实际系数/中间表达、实际误差表和复杂度；脚本只是复现器，不能代替公式本身。

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

`I2` 中 `M^2` 项严格抵消；`I1,I2` 是有限 analytic polynomial field。这部分没有被后续 compiler 失败否定。

## 3. 三个材料/解析门禁

以后材料 compiler 必须同时通过：

```text
Gate A = exact analytic direct closure
Gate B = concrete nonlinear adequacy
Gate C = production analytic complexity
```

Gate C 硬要求：

```text
1. original x/y/z numerical quadrature = 0
2. auxiliary numerical quadrature = 0
3. auxiliary ODE stepping = 0
4. no hidden numerical initialization
5. no branch-by-branch spatial/material state propagation
6. P, Rq and derivatives must reduce to direct finite formulas
7. named special functions are allowed only as direct evaluable functions
8. auxiliary matrix >3x3 is presumptive FAIL unless analytically eliminated
9. complexity may scale only with a small finite material basis
10. canonical theory must expose actual formulas, not only scripts that regenerate huge objects
```

## 4. M1、M1R-R01 与 PF1-R02~R06 当前身份

旧 M1 simple additive structured polynomial：

```text
M1_R01_SIMPLE_ADDITIVE_STRUCTURED_POLYNOMIAL = FAIL_SCREEN
```

M1R-R01 source-shaped rational material screen 仍作为 material regression evidence：

```text
U, C, C2=C^2, T, V=T^8
53 material-only rational coefficients
global P95 = 0.018261
global max = 0.036742
TC P95     = 0.023137
```

身份：

```text
M1R_R01_FROZEN_NC_ORACLE_REGRESSION = PASS_SCREEN
FINAL_NC_SOURCE_CALIBRATION = NOT_YET_DONE
FINAL_GATE_B = NOT_YET_FROZEN
M1R_RATIONAL_PRIMITIVE_PRODUCTION_COMPILER = HOLD_NOT_ACCEPTED
```

R02-R06 的 exact mathematics 保留为 audit only：

```text
R02: 27 scalar poles; 106 pair-pole blocks; quadratic s factors
R03: genus-2 de-Rham/Gauss-Manin audit
R04: symmetric Phi endpoint reduction
R05: common rational driver
R06: 15x15 witness connection, 211/225 nonzero, ~2.68e5 symbolic chars
```

正式定级：

```text
PF1_R03_GENUS2_GAUSS_MANIN = RETAIN_AUDIT_ONLY
PF1_R04_PHI_ENDPOINT_REDUCTION = RETAIN_AUDIT_ONLY
PF1_R05_COMMON_RATIONAL_DRIVER = RETAIN_AUDIT_ONLY
PF1_R06_15X15_CONNECTION_WITNESS = RETAIN_AUDIT_ONLY
PF1_R06_PRODUCTION_ACCEPTANCE = FAIL_COMPLEXITY_GATE
PF1_R07 = CANCELLED
```

## 5. P2-A 已实际执行：single-global-polynomial primitive compiler FAIL

当前 canonical P2-A：

- `current/theory/NZ_SCCM_M1R_P2A_INTEGRABILITY_FIRST_PRIMITIVE_SCREEN_20260810.md`
- `current/theory/nz_sccm_m1r_p2a_integrability_first_primitive_screen.py`
- `current/theory/NZ_SCCM_M1R_P2A_INTEGRABILITY_FIRST_PRIMITIVE_SCREEN_results.json`

### 5.1 P2-A 使用的是真正 source primitives

没有用 R01 rational coefficients 二次拟合。直接恢复 frozen source：

```text
Pi_eta(z)
H(r;r0)
c=Pi_eta(-lambda)
t=Pi_eta(lambda)
C=kappa*c/[1+(kappa-2)c+c^2]
r=t/xcr
T=r+(mt-1)H(r;1)-mt H(r;10)
U=kappa*lambda-C+kappa*c+rho*T-kappa*t
C2=C^2
V=T^8
```

区间：

```text
lambda in [-2.4390243902439024, 0.7317073170731706]
xi=(lambda-lambda_c)/lambda_s in [-1,1]
```

### 5.2 实际 screen

对每个 primitive 逐阶测试：

```text
degree n = 2,...,16
one global polynomial p_n(xi)
```

为了避免 ordinary least-squares 造成假失败，实际采用 discrete minimax LP：

```text
screen fit:       4001 material-coordinate points
screen validation:100001 independent material-coordinate points
n=16 confirm fit: 20001 material-coordinate points
n=16 validation:  200001 independent material-coordinate points
```

这些点只用于离线 material coefficient identification，不是结构空间积分点，也不进入 production operator。

### 5.3 n=16 最强候选的独立验证结果

```text
primitive   normalized max error
U           0.0242932
C           0.0243528
C2          0.00513371
T           0.325779
V           0.432821
```

使用非常宽松的 fail-fast 门：

```text
normalized max error <= 10%
```

T 与 V 仍分别为 32.58% 与 43.28%，因此结论不依赖 2%/5% 之类较严阈值。

形状也失败。source 在 lambda=0 要求：

```text
C=C2=T=V=0
```

但 degree-16 minimax 给出：

```text
C16(0)   = 0.0238393
C2_16(0) = -0.000356689
T16(0)   = 0.319174
V16(0)   = 0.250138
```

且非负 source primitives 的 degree-16 候选出现：

```text
min C16   = -0.024345
min C2_16 = -0.005134
min T16   = -0.321430
min V16   = -0.388948
```

### 5.4 P2-A 正式状态

```text
M1R_P2A_GLOBAL_POLYNOMIAL_PRIMITIVE_COMPILER = FAIL_COMPLEXITY_ACCURACY_GATE
P2B_SOURCE_SHAPED_2D_RECONSTRUCTION = NOT_AUTHORIZED
P2C_CAYLEY_HAMILTON = NOT_EXECUTED
P2D_EXACT_MOMENT_TERM_COUNT = NOT_EXECUTED
P2E_P_RQ_FORMULA_GENERATION = NOT_EXECUTED
```

按治理要求，P2-A 在 n=16 停止；不提高到 17/20/30 阶，不用新 large special-function/master system 救活。

## 6. P2-A 失败根因

核心不是 U/C/C2，而是 narrow tension activation：

```text
T(0)     = 0
T(0.025) = 0.495752
T(0.05)  = 0.972971
T(0.10)  = 0.922256
T(0.20)  = 0.767075
```

整个 lambda 区间宽度约 3.17073，而 tension transition characteristic coordinate：

```text
xcr ~= 0.0499872
```

single global low-degree polynomial 无法同时解析宽全域和这一窄激活尺度；V=T^8 又进一步放大该困难。

因此不能把“提高 global polynomial degree”作为下一路线。

## 7. 当前回退范围

不回退：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
I1/I2 invariant foundation
source-shaped biaxial material algebra
D15/exact-moment philosophy
Gate B nonlinear material target
```

已排除/停止作为 production compiler：

```text
M1 old 2D simple polynomial
M1R rational primitive + PF1 large auxiliary system
degree<=16 one-global-polynomial primitives
```

## 8. 当前唯一建议下一任务

```text
CURRENT_RECOMMENDED_NEXT_TASK = M1R_P2R_SOURCE_AWARE_LOW_COMPLEXITY_BASIS_PRECHECK
```

P2R 不是继续拟合，而是先做 integrability-first 候选基函数预检。只允许研究能够保留 T/V narrow activation、同时有希望直接回到小型 whole-halfwave formula 的 source-aware basis。

执行顺序必须是：

```text
candidate primitive basis
-> write its actual closed formula
-> compose symbolically with Case21 invariant scalar coordinate
-> count radicals/denominators/branches/terms BEFORE fitting coefficients
-> Gate C precheck
-> only a Gate-C-plausible family may enter material fit
```

禁止：

```text
raise global polynomial degree
piecewise spatial/material cells
large PF/Gauss-Manin systems
auxiliary ODE propagation
hidden numerical integration
new material physics
Case21/Swartz calibration
```

若所有 source-aware candidates都需要大 auxiliary systems或空间/material partition，P2R 应直接 HOLD/FAIL，而不是继续数学扩张。

## 9. 其他材料/结构边界不变

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

## 10. 当前明确未执行

```text
NO P2-B/P2-C/P2-D/P2-E
NO P2R execution yet
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

## 11. 后续恢复优先读取

1. `current/CURRENT_STATE.md`
2. `governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md`
3. `governance/PF1_R06_PRODUCTION_COMPLEXITY_SELF_AUDIT_20260810.md`
4. `current/theory/NZ_SCCM_M1R_P2A_INTEGRABILITY_FIRST_PRIMITIVE_SCREEN_20260810.md`
5. `current/theory/NZ_SCCM_M1R_P2A_INTEGRABILITY_FIRST_PRIMITIVE_SCREEN_results.json`
6. `current/theory/nz_sccm_m1r_p2a_integrability_first_primitive_screen.py`
7. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`
8. `current/theory/NZ_SCCM_M1R_SOURCE_SHAPED_RATIONAL_PRIMITIVE_SCREEN_R01_20260810.md`
9. `current/theory/NZ_SCCM_PF1_ENDPOINT_IBP_MASTER_CONNECTION_R06_20260810.md`
