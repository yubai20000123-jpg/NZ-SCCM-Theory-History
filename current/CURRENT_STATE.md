# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10  
**Purpose:** 唯一当前工作入口。历史 PASS、旧路线、迁移期文件不得覆盖本文件。

## 1. 不可改变的正式目标与边界

```text
finite analytic kinematics
-> finite strain invariants
-> strong nonlinear material law
-> exact analytic material/structural contraction
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

允许 finite named special functions、finite algebraic covers、finite de-Rham/twisted bases、finite coefficient matrices、finite Gauss–Manin/Picard–Fuchs/holonomic systems；这些对象只能解析表示同一个完整半波积分，不得成为隐藏空间/材料点离散。

当前治理锁：

- `governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`
- `governance/PF1_R05_GOAL_RELEVANCE_CHECKPOINT_20260810.md`

后者要求：所有数学工作必须直接减少 actual M1R `P/Rq/L` whole-halfwave kernel。若只得到脱离物理 kernel 的 generic mathematics，应停在 HOLD/FAIL。

## 2. 结构—不变量基础

当前 foundation：

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

`I2` 中 `M^2` 项严格抵消。材料架构必须同时通过：

```text
Gate A = exact analytic / finite special-function closure
Gate B = concrete nonlinear adequacy
```

## 3. M1 淘汰；M1R 为当前解析材料架构

```text
M1_R01_SIMPLE_ADDITIVE_STRUCTURED_POLYNOMIAL = FAIL_SCREEN
```

M1R-R01 保留 frozen-NC source-shaped biaxial algebra，只编译：

```text
U
C
C2=C^2
T
V=T^8
```

53 个 material-only rational coefficients；二维 fitted interaction coefficients=0。

frozen-NC screen：

```text
global P95 = 0.018261
global max = 0.036742
TC P95     = 0.023137
```

身份：

```text
M1R_R01_FROZEN_NC_ORACLE_REGRESSION = PASS_SCREEN
FINAL_NC_SOURCE_CALIBRATION = NOT_YET_DONE
FINAL_GATE_B = NOT_YET_FROZEN
```

frozen NC 仅为 regression/material oracle，不是 final NC truth。

## 4. s-inner 与 resolvent canonicalization

Case21 exact coordinate：

```text
s=I1
z=(s-a)/(2Buv)
s±=a±2Buv
```

`I2(s;u,v)` 对 `s` 严格二次。

```text
M1R_R01_S_INNER_INTEGRATION = PASS_CLASS_A
N_s_quadrature = 0
```

R02：

```text
R_r=(X-rI)^(-1)=[(I1-r)I-X]/Delta_r
Delta_r=I2-rI1+r^2
R_r^oth=(X-rI)/Delta_r
```

当前 five primitives 共 27 scalar poles；stress 最多：

```text
1 constant
+ 27 consolidated single-pole
+ 106 pair-pole analytic blocks
```

```text
M1R_R02_RESOLVENT_CANONICALIZATION = PASS_EXACT
M1R_R02_ACTUAL_S_FACTORS = QUADRATIC_ONLY
```

这些是解析 block counts，不是空间点/材料点/DOF。

## 5. R03/R04：数学分类已收敛到 physical Phi kernel

R03 对 unsymmetrized genus-2 family 建立 4D de-Rham/Gauss–Manin exact audit：

```text
PF1_R03_GENUS2_ABSOLUTE_DERHAM_BASIS = PASS_EXACT
PF1_R03_FIXED_9X9_GRIFFITHS_HERMITE_REDUCTION = PASS_EXACT
PF1_R03_ABSOLUTE_X_GAUSS_MANIN = PASS_EXACT
```

R03 只保留为 independent analytic audit，不再是 production bottleneck。

R04 对 physical symmetric s-endpoint 得到：

```text
Phi(z)=atanh(sqrt(z))/sqrt(z)=2F1(1/2,1;3/2;z)
```

并 exact 证明：

```text
PF1_R04_PHYSICAL_RELATIVE_X_EXACT_TERM = PASS_EXACT
PF1_R04_ENDPOINT_B_OVER_W = VANISHES_EXACTLY
PF1_R04_LOG_ATANH_SYMMETRIC_KERNEL = PASS_EXACT
PF1_R04_ALPHA_ZERO = REMOVABLE_ANALYTIC_LIMIT
PF1_R04_PAIR_S_ENDPOINT_KERNEL_FAMILY = FINITE_PHI_FAMILY
PF1_R04_SPATIAL_QUADRATURE = 0
```

因此不再扩张 generic third-kind/log-divisor basis。

## 6. R05：Phi layer → common rational driver

R05 exact identity：

```text
2 z Phi'(z)+Phi(z)=1/(1-z)
```

令纯解析系数参数：

```text
tau=B(q)^2
```

`tau` 不是结构 DOF、加载变量或材料变量。

定义：

```text
h=x+y-1
E_tau=E0+tau h
K_tau=E0-tau h
ell=D(nu-1)+M(2-x-y)-2r
```

得到：

```text
D_r(tau)=E_tau^2-tau*x*y*ell^2
        =K_tau^2-tau*Gamma_r
```

两个 physical Phi kernel：

```text
(2 tau d/dtau+1) F_L = ell*K_tau/(2 D_r)
(2 tau d/dtau+1) F_J = E_tau/D_r
```

```text
PF1_R05_PHI_FIRST_ORDER_IDENTITY = PASS_EXACT
PF1_R05_COMMON_TAU_DRIVER_IDENTITY = PASS_EXACT
PF1_R05_LOG_KERNEL_TAU_ODE = PASS_EXACT
PF1_R05_RECIPROCAL_KERNEL_TAU_ODE = PASS_EXACT
```

actual common driver：

```text
degree_x = 3
degree_y = 3
total_degree = 4
monomial count = 11
```

固定 `(y,tau)` 的 x integral 由 arcsine resolvent identity 精确消去：

```text
Integral_0^1 dx/[sqrt(x(1-x))(x-rho)]
= -pi/sqrt(rho(rho-1))
```

```text
PF1_R05_X_ARCSINE_RESOLVENT_ELIMINATION = PASS_CLASS_A
N_x_quadrature = 0
PF1_R05_Y_ALGEBRAIC_TRACE_RESULTANT = PASS_FINITE_ALGEBRAIC
```

R05 twisted critical quotient witness 为 19 monomials，但当时未宣称 final master dimension。

## 7. R06 latest：endpoint-compatible IBP 实际把 19 降为 15 masters

当前 canonical R06：

- `current/theory/NZ_SCCM_PF1_ENDPOINT_IBP_MASTER_CONNECTION_R06_20260810.md`
- `current/theory/nz_sccm_pf1_endpoint_ibp_master_connection_r06.py`
- `current/theory/NZ_SCCM_PF1_ENDPOINT_IBP_MASTER_CONNECTION_R06_results.json`

定义：

```text
hx=x(1-x)
hy=y(1-y)
I[N]=∫∫ N/[sqrt(hx hy) D_r] dxdy
```

endpoint-compatible exact IBP identity：

```text
Q =
D_r R
+ D_r(hx A_x + hx'/2 A + hy B_y + hy'/2 B)
- hx A D_r,x
- hy B D_r,y
```

则：

```text
∫∫ Q/[sqrt(hx hy) D_r^2] dxdy = I[R]
```

边界 certificate 因 `sqrt(hx)` / `sqrt(hy)` 在 0,1 消失，不需要 endpoint cells。

```text
PF1_R06_ENDPOINT_COMPATIBLE_IBP_IDENTITY = PASS_EXACT
```

使用 total-degree<=5 certificates：

```text
coefficient equations = 62
unknowns = 57
```

R05 的 19 monomial quotient 存在 4 个独立 exact period relations；三组 rational parameter witnesses 上 relation rank 都为 4。

选择 15-master basis：

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

消去：

```text
x^2 y^3
x^3
x^4
x^5
```

正式身份：

```text
PF1_R06_R05_19_MONOMIAL_QUOTIENT = OVERCOMPLETE_FOR_PERIOD_BASIS
PF1_R06_PERIOD_RELATION_RANK_WITNESS = 4
PF1_R06_MASTER_PERIOD_DIMENSION_WITNESS = 15
```

## 8. R06：explicit symbolic tau connection 已生成

在 exact rational witness：

```text
D=1
M=1
nu=1/5
r=2
tau=symbolic
```

15 master periods满足：

```text
dI/dtau = Omega_tau(tau) I
Omega_tau in Q(tau)^(15x15)
```

实际 connection：

```text
shape = 15x15
nonzero = 211/225
```

脚本生成全部 symbolic entries；其 symbolic output 总字符量约 `2.68e5`。`tau=1/7` 时与独立 exact rational coefficient matching 做 225/225 逐元素一致校验。

```text
PF1_R06_TAU_CONNECTION_MATRIX_WITNESS = PASS_EXACT_SYMBOLIC_15X15
```

chosen witness basis 的 denominator LCM 给出有限 candidate singular locus；这些候选必须继续区分 physical singularities 与 apparent/gauge singularities。物理路径始终：

```text
tau(q)=B(q)^2=[pi^2/(2 eps0)*(t/b)*q]^2 >=0
```

## 9. R06：D/M/B/q derivatives 仍落在同一个 system

对：

```text
Q_D=-m_j D_r,D
Q_M=-m_j D_r,M
```

同一 15-master / degree-5 certificate system 在 exact witness point `tau=1/7` 对全部 15 列均唯一闭合：

```text
PF1_R06_D_CONNECTION_WITNESS_POINT = PASS_EXACT_15X15
PF1_R06_M_CONNECTION_WITNESS_POINT = PASS_EXACT_15X15
```

因为 `B` 只通过 `tau=B^2`：

```text
Omega_B = 2 B Omega_tau
```

Case21：

```text
M_q=alpha(q0+q)
B_q=beta
tau_q=2 B B_q
```

所以：

```text
Omega_q=M_q Omega_M+2 B B_q Omega_tau
```

```text
PF1_R06_B_Q_CHAIN_RULE = PASS_ANALYTIC
```

没有新增空间积分器或材料点 differentiation。

## 10. 当前准确停点与 Gate

R06 已证明：R05 的 common rational driver 不是“只存在抽象 finite system”，而是已经能在 actual endpoint-compatible IBP 架构下形成 15-master explicit tau connection witness。

但 production-level 仍缺：

```text
generic/current (D,M,nu,r) connection generator audit
branch-consistent analytic initial values
physical tau=B(q)^2 branch/basis patch rules
stable no-x/y-quadrature evaluator
27 single-pole / 106 pair-block production reuse audit
```

因此必须保持：

```text
PF1_R06_GENERIC_DMRT_CONNECTION = HOLD
PF1_R06_BRANCH_INITIAL_VALUE_EVALUATOR = HOLD
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

这不是 route failure，也不能据此转向 generic GKZ mathematics。

## 11. 当前唯一下一任务：PF1-R07

```text
R07 = actual production evaluator closure
```

只允许：

1. 参数化 R06 coefficient-matching generator 到 actual `(D,M,nu,r)`；
2. 选择并证明 safe analytic initial-value prescription；
3. 建立 physical `tau=B(q)^2` branch/basis patch rule；
4. 同一 master system 返回 rational-driver periods 与 `D,q` derivatives；
5. 审计 27 single-pole / 106 pair-block 组装；
6. 全部通过后才讨论 `FORMAL_WHOLE_HALFWAVE_GATE_A = PASS_CLASS_B`。

禁止：

```text
generic GKZ detour
new material fit
Case21 Pu
Swartz24
UHPC production fit
shell/Y production solve
spatial numerical quadrature
auxiliary numerical quadrature as formal operator
material-point integration
route switch
```

## 12. 其他材料/结构边界不变

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

## 13. 当前明确未执行

```text
NO new Case21 Pu solve
NO Swartz24 solve
NO UHPC production fit
NO shell/Y production solve
NO structural Pu calibration
NO spatial numerical quadrature
NO auxiliary numerical quadrature as formal operator
NO endpoint cells
NO material-point integration
NO route switch
```

## 14. 后续恢复优先读取

1. `current/CURRENT_STATE.md`
2. `governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`
3. `governance/PF1_R05_GOAL_RELEVANCE_CHECKPOINT_20260810.md`
4. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`
5. `current/theory/NZ_SCCM_M1R_SOURCE_SHAPED_RATIONAL_PRIMITIVE_SCREEN_R01_20260810.md`
6. `current/theory/NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_CLASSIFICATION_R02_20260810.md`
7. `current/theory/NZ_SCCM_PF1_RELATIVE_ENDPOINT_HYPERGEOMETRIC_CLOSURE_R04_20260810.md`
8. `current/theory/NZ_SCCM_PF1_HYPERGEOMETRIC_DRIVER_REDUCTION_R05_20260810.md`
9. `current/theory/NZ_SCCM_PF1_ENDPOINT_IBP_MASTER_CONNECTION_R06_20260810.md`
10. `evidence/stability/STEEL_NONDISCRETIZATION_SEMIANALYTIC_REFERENCE_MAP_20260810.md`
