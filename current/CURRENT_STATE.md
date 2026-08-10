# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10  
**Purpose:** 唯一当前工作入口；历史 PASS、旧路线和迁移期文件不得覆盖本文件。

## 1. 正式主线与不可改变的基础边界

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

formal identity 永久保持：

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

允许 finite named special functions、finite algebraic covers、finite de-Rham/twisted bases、finite coefficient matrices、finite Gauss–Manin/Picard–Fuchs/holonomic differential systems；这些对象只能解析表示同一个完整半波积分，不得变成隐藏的空间/材料点离散。

当前路径锁：

- `governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`
- `governance/PF1_R05_GOAL_RELEVANCE_CHECKPOINT_20260810.md`

后者进一步要求：数学工作必须直接减少 actual M1R `P/Rq/L` whole-halfwave kernel；不得为 generic mathematics 本身继续扩张。

## 2. 结构—不变量基础已闭合

当前 foundation：

- `current/theory/NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`
- `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`

Case21 Nguyen 二阶单完整半波已经写成有限 analytic strain field；`I1=tr(X)`、`I2=det(X)` 显式闭合，且 `I2` 中 `M^2` 项严格抵消。

材料架构必须同时通过：

```text
Gate A = exact analytic / finite special-function closure
Gate B = concrete nonlinear adequacy
```

低阶 generic material 只允许作 algebra unit test。

## 3. M1 已淘汰；M1R 为当前材料解析架构

M1 simple structured polynomial：

```text
M1_R01_SIMPLE_ADDITIVE_STRUCTURED_POLYNOMIAL = FAIL_SCREEN
```

M1R-R01 保留 frozen-NC source-shaped biaxial algebra，只编译五个一维 rational primitives：

```text
U
C
C2=C^2
T
V=T^8
```

53 个 material-only rational coefficients，二维 fitted interaction coefficients=0；同一 frozen-NC material screen：

```text
global P95 = 0.018261
global max = 0.036742
TC P95     = 0.023137
```

当前身份：

```text
M1R_R01_FROZEN_NC_ORACLE_REGRESSION = PASS_SCREEN
FINAL_NC_SOURCE_CALIBRATION = NOT_YET_DONE
FINAL_GATE_B = NOT_YET_FROZEN
```

frozen NC 仍是 material oracle/regression benchmark，不是最终普通混凝土材料真理。

## 4. `s=I1` inner exact elimination 与 resolvent canonicalization 已闭合

Case21：

```text
I1 = a(u,v;D,q)+2Buvz
s = I1
z = (s-a)/(2Buv)
s± = a±2Buv
```

`I2(s;u,v)` 对 `s` 严格二次。

```text
M1R_R01_S_INNER_INTEGRATION = PASS_CLASS_A
N_s_quadrature = 0
```

R02 对 actual M1R rational primitives 做 scalar-pole / Cayley-Hamilton canonicalization：

```text
R_r=(X-rI)^(-1)=[(I1-r)I-X]/Delta_r
Delta_r=I2-r I1+r^2
R_r^oth=(X-rI)/Delta_r
```

全部 current primitive 共 27 scalar poles；stress 最多为 1 constant + 27 consolidated single-pole + 106 pair-pole analytic blocks。

```text
M1R_R02_RESOLVENT_CANONICALIZATION = PASS_EXACT
M1R_R02_ACTUAL_S_FACTORS = QUADRATIC_ONLY
```

这些 block counts 是解析项数，不是空间点、材料点或结构 DOF。

## 5. R03 genus-2 system：保留为正确 analytic audit，不再是 physical production bottleneck

R02 的 unsymmetrized outer radical generically 可产生 genus-2 hyperelliptic period。R03 已建立 absolute genus-2 4D de-Rham / Gauss–Manin reduction：

```text
PF1_R03_GENUS2_ABSOLUTE_DERHAM_BASIS = PASS_EXACT
PF1_R03_FIXED_9X9_GRIFFITHS_HERMITE_REDUCTION = PASS_EXACT
PF1_R03_ABSOLUTE_X_GAUSS_MANIN = PASS_EXACT
```

R03 仍作为 independent analytic audit 保留。

但 physical production kernel 不能停在 unsymmetrized `1/sqrt(Gamma) × log` 形式，因为 R04 找到了更强的 symmetric-endpoint cancellation。

## 6. R04 latest：physical symmetric endpoint 已统一为一个 finite `Phi` kernel

当前 canonical R04：

- `current/theory/NZ_SCCM_PF1_RELATIVE_ENDPOINT_HYPERGEOMETRIC_CLOSURE_R04_20260810.md`

定义：

```text
Phi(z)=atanh(sqrt(z))/sqrt(z)=2F1(1/2,1;3/2;z)
Phi(0)=1
```

R04 已 exact 证明：

```text
PF1_R04_PHYSICAL_RELATIVE_X_EXACT_TERM = PASS_EXACT
PF1_R04_ENDPOINT_B_OVER_W = VANISHES_EXACTLY
PF1_R04_LOG_ATANH_SYMMETRIC_KERNEL = PASS_EXACT
PF1_R04_CANONICAL_SPECIAL_FUNCTION = 2F1(1/2,1;3/2;z)
PF1_R04_ALPHA_ZERO = REMOVABLE_ANALYTIC_LIMIT
PF1_R04_PAIR_S_ENDPOINT_KERNEL_FAMILY = FINITE_PHI_FAMILY
PF1_R04_SPATIAL_SUBDOMAINS_ADDED = 0
PF1_R04_SPATIAL_QUADRATURE = 0
```

实际 quadratic `s` block 只需要 finite polynomial endpoint moments + `J0/J1`，pair block 也经 exact partial fraction / confluent limit 落回同一个 `Phi` family。

因此旧 R04 `log relative extended connection HOLD` 已被这个更强 physical symmetric-endpoint identity supersede；不再需要继续扩大 generic log-divisor basis。

## 7. R05：`Phi` pullback 已进一步压缩为同一个 common rational driver

当前新增：

- `current/theory/NZ_SCCM_PF1_HYPERGEOMETRIC_DRIVER_REDUCTION_R05_20260810.md`
- `current/theory/nz_sccm_pf1_hypergeometric_driver_r05.py`
- `current/theory/NZ_SCCM_PF1_HYPERGEOMETRIC_DRIVER_R05_results.json`

R05 首先 exact 利用：

```text
2 z Phi'(z)+Phi(z)=1/(1-z)
```

并把 physical `B(q)^2` 暂时作为一个**纯解析系数参数** `tau`；`tau` 不是结构 DOF、加载路径或材料变量，物理终值始终为：

```text
tau = B(q)^2
```

令：

```text
h = x+y-1
E_tau = E0 + tau h
K_tau = E0 - tau h
ell = D(nu-1)+M(2-x-y)-2r
```

则获得关键 exact identity：

```text
D_r(tau)
= E_tau^2 - tau*x*y*ell^2
= K_tau^2 - tau*Gamma_r
```

所以 R04 的 log 与 reciprocal 两种 `Phi` pullback 共享同一个 rational denominator。

两个 actual kernel 均满足同一个 first-order tau operator：

```text
(2 tau d/dtau + 1) F_L = ell*K_tau/(2 D_r)
(2 tau d/dtau + 1) F_J = E_tau/D_r
```

配套 SymPy exact remainder 全为 0。

正式状态：

```text
PF1_R05_PHI_FIRST_ORDER_IDENTITY = PASS_EXACT
PF1_R05_COMMON_TAU_DRIVER_IDENTITY = PASS_EXACT
PF1_R05_LOG_KERNEL_TAU_ODE = PASS_EXACT
PF1_R05_RECIPROCAL_KERNEL_TAU_ODE = PASS_EXACT
```

这意味着 current `Phi` transcendental layer 的 inhomogeneous driver 已全部变成同一个 **ordinary rational Beta-weighted period family**。

## 8. R05：actual common driver 规模固定且 x integral 已 Class-A 精确消掉

common driver：

```text
D_r(tau)=E_tau^2-tau*x*y*ell^2
```

exact generic expansion：

```text
degree_x = 3
degree_y = 3
total_degree = 4
monomial count = 11
```

对 fixed `(y,tau)`，其 `x` degree <=3。利用：

```text
Integral_0^1 dx/[sqrt(x(1-x)) (x-rho)]
= -pi/sqrt(rho(rho-1))
```

每个 rational driver 的 physical `x` integral 可通过至多三个 algebraic roots 的 finite trace 精确消去；重根使用 analytic confluent limit，不建立空间 cell。

```text
PF1_R05_X_ARCSINE_RESOLVENT_ELIMINATION = PASS_CLASS_A
N_x_quadrature = 0
```

为了不显式列 cubic roots，定义：

```text
R_r(Z,y;tau)=Res_x(D_r(x,y;tau), Z-x(x-1))
```

在 exact rational witness `D=1,M=1,nu=1/5,r=2`、保留 `tau` symbolic 时：

```text
degree_Z = 3
degree_y = 6
total_degree = 7
term_count = 19
```

因此 x 消元后的 y dependence 已被压成固定 finite algebraic trace family：

```text
PF1_R05_Y_ALGEBRAIC_TRACE_RESULTANT = PASS_FINITE_ALGEBRAIC
```

但 finite algebraic cover 仍不是 y integral 的最终 evaluator，因此不能提前宣布 whole Gate A PASS。

## 9. R05 practical scale gate：actual twisted critical quotient witness = 19

对 common driver 定义 endpoint-compatible twisted critical polynomials：

```text
hx=x(1-x)
hy=y(1-y)
Gx=2 hx D_,x + hx' D
Gy=2 hy D_,y + hy' D
```

在同一个 exact rational witness、field `Q(tau)` 上，Groebner leading monomials：

```text
x^6
x^2 y^4
x y^5
y^6
x^4 y
x^3 y^2
```

standard monomial quotient 恰有 19 项。

正式身份只能写：

```text
PF1_R05_TWISTED_CRITICAL_QUOTIENT = PASS_WITNESS_DIMENSION_19
```

不能偷换成 final generic connection dimension，因为 full parameter-derivative connection matrix 还没有实际输出。

## 10. 当前准确停点

已完成：

```text
actual R04 Phi kernel
-> exact first-order Phi identity
-> common rational driver
-> exact x elimination
-> finite y algebraic trace
-> exact witness scale screen (19 monomials)
```

仍未完成：

```text
actual finite master connection matrix
tau / D / M / q chain derivatives
connection singular-locus audit
branch/analytic-continuation rules
a stable no-x/y-quadrature evaluator
```

因此当前必须保持：

```text
PF1_R05_FULL_GENERIC_CONNECTION_MATRIX = HOLD
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

这不是 PF1 route failure；它是明确的 final analytic-system gate。

## 11. 当前唯一下一任务：PF1-R06

R06 只允许继续处理同一个 actual common driver：

```text
D_r(tau)=E_tau^2-tau*x*y*ell^2
```

必须实际完成：

1. endpoint-compatible finite master numerator basis；
2. explicit `tau` Gauss–Manin / Picard–Fuchs connection matrix；
3. exact matrix identity audit；
4. singular loci 与 physical `tau=B(q)^2` path；
5. same-system `D,M,B(q),q` derivatives；
6. no-x/y-quadrature evaluator route。

若 R06 只能得到一个过度庞大、无稳定 evaluator、无法服务 `P/Rq/L` 的 abstract system，应按 `PF1_R05_GOAL_RELEVANCE_CHECKPOINT` 停止并记录 practical HOLD/FAIL；不得为了数学存在性继续偏离项目目标。

## 12. old NC / reinforcement / UHPC / shell 边界不变

旧 NC + reinforcement current operator仍仅为 regression/reference：

- `current/theory/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`

钢筋必须在 root solve 前进入：

```text
P=Pc+Ps
Rq=Rq,c+Rq,s
```

禁止事后 `Pu=Pu,c+As fy`。

UHPC：仅 `fc=141.1 MPa` 为用户强制冻结值；final strong multiaxial production operator 尚未闭合。

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

1. `current/CURRENT_STATE.md`；
2. `governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`；
3. `governance/PF1_R05_GOAL_RELEVANCE_CHECKPOINT_20260810.md`；
4. `current/theory/NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`；
5. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`；
6. `current/theory/NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`；
7. `current/theory/NZ_SCCM_M1R_SOURCE_SHAPED_RATIONAL_PRIMITIVE_SCREEN_R01_20260810.md`；
8. `current/theory/NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_CLASSIFICATION_R02_20260810.md`；
9. `current/theory/NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_ABSOLUTE_X_CLOSURE_R03_20260810.md`；
10. `current/theory/NZ_SCCM_PF1_RELATIVE_ENDPOINT_HYPERGEOMETRIC_CLOSURE_R04_20260810.md`；
11. `current/theory/NZ_SCCM_PF1_HYPERGEOMETRIC_DRIVER_REDUCTION_R05_20260810.md`；
12. `evidence/mathematics/PF1_GRIFFITHS_HYPERELLIPTIC_DERHAM_SOURCE_MAP_20260810.md`；
13. `evidence/stability/STEEL_NONDISCRETIZATION_SEMIANALYTIC_REFERENCE_MAP_20260810.md`。
