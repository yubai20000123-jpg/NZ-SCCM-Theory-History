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

允许 finite named special functions、finite algebraic covers、finite de-Rham bases、finite coefficient matrices、finite Gauss–Manin/Picard–Fuchs/holonomic differential systems；这些对象只能解析表示同一个完整半波积分，不得变成隐藏的空间/材料点离散。

用户在 PF1 执行前再次明确：**基础限制不能变，路径不能偏离。** 当前唯一治理锁：

`governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`

PF1 若必须违反任一条件，必须停在 FAIL/HOLD；不得静默切换结构问题、积分身份或材料路线。

## 2. 已闭合结构—不变量基础

当前 foundation：

- `current/theory/NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`
- `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`

Case21 Nguyen 二阶单完整半波已写成有限 analytic strain field；`I1=tr(X)`、`I2=det(X)` 显式闭合，且 `I2` 中 `M^2` 项严格抵消。

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

其 182 coefficients 时 global P95≈0.10869、TC P95≈0.37460、condition number≈1.8e8。

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

## 4. `s=I1` inner exact elimination 已闭合

Case21：

```text
I1 = a(u,v;D,q)+2Buvz
s = I1
z = (s-a)/(2Buv)
s± = a±2Buv
```

`I2(s;u,v)` 对 s 严格二次。M1R rational material 在固定 `(u,v)` 下进入 finite rational functions of `s`。

```text
M1R_R01_S_INNER_INTEGRATION = PASS_CLASS_A
N_s_quadrature = 0
```

## 5. R02：actual M1R resolvent canonicalization = PASS_EXACT

当前文件：

- `current/theory/NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_CLASSIFICATION_R02_20260810.md`
- `current/theory/nz_sccm_m1r_outer_resolvent_hyperelliptic_r02.py`
- `current/theory/NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_R02_results.json`

五个 primitive 均可写成 finite simple scalar resolvents，总 scalar poles=27。

```text
R_r=(X-rI)^(-1)=[(I1-r)I-X]/Delta_r
Delta_r=I2-r I1+r^2
R_r^oth=(X-rI)/Delta_r
```

pair source block：

```text
R_r R_t^oth
=
{[I2-t(I1-r)]I+(t-r)X}/(Delta_r Delta_t)
```

stress 最多为：

```text
1 constant + 27 consolidated single-pole + 106 pair-pole blocks
```

这是 finite analytic block count，不是空间离散。

```text
M1R_R02_RESOLVENT_CANONICALIZATION = PASS_EXACT
M1R_R02_ACTUAL_S_FACTORS = QUADRATIC_ONLY
```

## 6. R02：generic unsymmetrized outer family 是 genus-2 hyperelliptic-relative period

令 `x=u^2,y=v^2`。对 single pole：

```text
Gamma_r=4xy*disc_s[Delta_r(s)]
```

exact audit：

```text
degree_x Gamma_r = 3
degree_y Gamma_r = 3
total_degree Gamma_r = 4
```

固定 generic interior `y`：

```text
w^2=P5(x)=x(1-x)Gamma_r(x,y)
```

R02 exact witness 为 square-free degree 5，因此存在 nondegenerate genus-2 specialization。

```text
M1R_R02_GENERIC_OUTER_CLASS_A = FAIL
M1R_R02_GENERIC_ORDINARY_ELLIPTIC = INSUFFICIENT
M1R_R02_GENERIC_SIMPLE_APPELL = NOT_GENERAL
M1R_R02_OUTER_PERIOD_CLASS = HYPERELLIPTIC_RELATIVE / PICARD_FUCHS
```

这里 FAIL 的仅是 generic Class-A 假设，M1R 主线没有失败。R04 后续又证明：对**实际 symmetric s-endpoint contraction**，该 unsymmetrized genus-2/log 表达存在更强的 exact cancellation；因此 R02 classification 保留为数学分类/audit，不再是 production kernel 的最紧表示。

## 7. PF1-R03：absolute genus-2 x Gauss–Manin = PASS_EXACT

canonical R03：

- `current/theory/NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_ABSOLUTE_X_CLOSURE_R03_20260810.md`
- `current/theory/nz_sccm_pf1_genus2_gauss_manin_r03.py`
- `current/theory/NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_R03_results.json`

对 `w^2=P5(x)` 采用 4 维 basis：

```text
omega0=dx/w
omega1=x dx/w
omega2=x^2 dx/w
omega3=x^3 dx/w
```

参数导数以固定 9×9 Sylvester/Bezout reduction：

```text
N=A P+B P'
N/w^3 dx=(A+2B')/w dx-2 d(B/w)
```

一次 exact reduction 直接回同一 4 维 basis。

```text
PF1_R03_GENUS2_ABSOLUTE_DERHAM_BASIS = PASS_EXACT
PF1_R03_FIXED_9X9_GRIFFITHS_HERMITE_REDUCTION = PASS_EXACT
PF1_R03_ABSOLUTE_X_GAUSS_MANIN = PASS_EXACT
```

R03 没有提前删除 physical relative endpoint term，因此当时保持 endpoint HOLD 是正确的保守门禁。

## 8. PF1-R04A：physical algebraic `[0,1]` endpoint = PASS_EXACT

已有 endpoint-compatible R04：

- `current/theory/NZ_SCCM_PF1_RELATIVE_X_ENDPOINT_COMPATIBLE_REDUCTION_R04_20260810.md`
- `current/theory/nz_sccm_pf1_relative_x_endpoint_r04.py`
- `current/theory/NZ_SCCM_PF1_RELATIVE_X_ENDPOINT_R04_results.json`

Case21/R02 curve 固定：

```text
h=x(1-x)
P=h Gamma
P_,theta=h Gamma_,theta
```

endpoint-compatible 7×7 reduction 可使：

```text
B_rel=h C
B_rel/w=C sqrt[h/Gamma] -> 0 at x=0,1
```

所以 physical `[0,1]` chain：

```text
integral d(B_rel/w)=0 exactly
```

不需要 endpoint cells、tangential subtraction 或 numerical endpoint integration。

```text
PF1_R04_ENDPOINT_COMPATIBLE_7X7_REDUCTION = PASS_EXACT
PF1_R04_PHYSICAL_ALGEBRAIC_X_ENDPOINT = PASS_EXACT
```

## 9. PF1-R04B：actual symmetric log/atanh endpoint 已压缩为单一 finite `2F1` kernel

新增 canonical advance：

- `current/theory/NZ_SCCM_PF1_RELATIVE_ENDPOINT_HYPERGEOMETRIC_CLOSURE_R04_20260810.md`
- `current/theory/nz_sccm_pf1_relative_endpoint_hypergeometric_r04.py`
- `current/theory/NZ_SCCM_PF1_RELATIVE_ENDPOINT_HYPERGEOMETRIC_R04_results.json`

关键不是继续对 unsymmetrized `1/sqrt(Gamma) × log/atanh` 建第三类 divisor basis，而是先保持真实 physical symmetric s-endpoint divided difference：

```text
D_F(a,c)=[F(a+c)-F(a-c)]/(2c)
c=2B sqrt(xy)
```

定义统一 special function：

```text
Phi(z)=atanh(sqrt(z))/sqrt(z)
      = 2F1(1/2,1;3/2;z)
Phi(0)=1
```

并满足有限二阶 ODE：

```text
z(1-z) Phi'' + (3/2-5z/2) Phi' - Phi/2 = 0
```

对 general quadratic：

```text
Delta(s)=alpha s^2+beta s+gamma
A0=Delta(a)
L=2 alpha a+beta
delta=beta^2-4 alpha gamma
E=A0+alpha c^2
Kbar=A0-alpha c^2
```

exact identities：

```text
[log Delta(a+c)-log Delta(a-c)]/(2c)
= (L/E) Phi(c^2 L^2/E^2)
```

以及若 `J'(s)=1/Delta(s)`：

```text
[J(a+c)-J(a-c)]/(2c)
= (1/Kbar) Phi(c^2 delta/Kbar^2)
```

对 actual M1R `Delta_r`：

```text
ell_r=D(nu-1)+M(2-x-y)-2r
L_r=ell_r/2
```

得到：

```text
L_kernel_r
= ell_r/(2 E_r)
  Phi(B^2 x y ell_r^2/E_r^2)
```

和：

```text
J0_r
= 1/Kbar_r
  Phi(B^2 Gamma_r/Kbar_r^2)
```

即 actual physical symmetric endpoint kernel 的 `Phi` argument 都是 finite rational functions；不再需要裸 `sqrt(Gamma_r)` 或空间 log-divisor partition。

配套 exact audit：

```text
reciprocal_endpoint_derivative_identity = TRUE
log_endpoint_derivative_identity = TRUE
Phi_hypergeometric_ode_identity = TRUE
```

另外，proper linear numerator 只需 `J0,J1`；`alpha=(x+y-1)/(4xy)=0` 的内部直线只形成 removable analytic limit，不允许成为 spatial subdomain front。

pair-resolvent 通过 factor-aware partial fractions / confluent analytic limit 仍只产生同一 finite `Phi` family。

正式升级：

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

因此此前：

```text
PF1_R04_LOG_RELATIVE_EXTENDED_CONNECTION = HOLD
PF1_R04_PAIR_BLOCK_EXTENSION = NOT_YET_CLOSED
```

在 **s-endpoint kernel 层** 已被上述更强 symmetric identity supersede；不再把“为每个 log divisor 扩大 relative basis”作为当前唯一生产路线。

## 10. 当前真正 blocker：whole `(x,y)` hypergeometric pullback 仍未消元

R04B 后，真实剩余 whole-halfwave family 可统一写成有限项：

```text
Beta(x) Beta(y)
× rational R(x,y;D,q,r,...)
× Phi(chi(x,y;D,q,r,...))
```

即：

\[
\int_0^1\int_0^1
\frac{R(x,y)\,\Phi(\chi(x,y))}
{\sqrt{x(1-x)y(1-y)}}\,dx\,dy.
\]

这仍然不能留成 numerical x/y quadrature，也不能通过 endpoint cells、material points 或空间分区求值。

当前状态：

```text
PF1_R04_WHOLE_XY_PUSHFORWARD = NOT_YET_ELIMINATED
PF1_R04_DQ_WHOLE_TANGENT = NOT_YET_CLOSED
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

Gate A 继续 HOLD；绝不因 `Phi` 已是 named special function 就提前宣布 whole-halfwave PASS。

## 11. 当前唯一下一任务：PF1-R05

继续严格保持 `PF1_PATH_INVARIANTS_LOCK`：

```text
PF1-R05
= finite holonomic / Picard-Fuchs creative telescoping
  for actual M1R Beta-weighted rational × Phi(rational pullback) blocks
```

必须实际完成：

1. 利用 `Phi` 的二阶 hypergeometric ODE 构造有限 derivative basis；
2. 对 x 变量进行 exact creative telescoping / holonomic pushforward，消除 physical x integral；
3. 再对 y 做 exact telescoping / pushforward；
4. 最终只保留 external parameters `D,q,r,...` 的 finite differential-system / named special-function object；
5. 显式处理 `chi=1`、denominator/resultant/discriminant singular loci与 finite monodromy/analytic-continuation data；
6. `D,q` derivatives 必须在同一 finite system 内闭合，供 analytic tangent 与 `L` 使用；
7. 不允许用 numerical x/y integration 代替 telescoper。

若 R05 需要 spatial/auxiliary numerical quadrature、cells、material points、改变 `P/Rq/L`、降低材料非线性或 route switch，则停止并报告 HOLD/FAIL。

coarea/pushforward 只有 PF1 真正失败并形成新 checkpoint 后才可打开；当前不并行展开。

## 12. steel semi-analytical reference lane

钢结构 non-discretization / Rayleigh–Ritz / semi-analytical postbuckling 文献继续保留为 structural-method reference only：

`evidence/stability/STEEL_NONDISCRETIZATION_SEMIANALYTIC_REFERENCE_MAP_20260810.md`

它可以支持连续场/有限 generalized-coordinate、变分、平衡路径、imperfection sensitivity、shell/Y 后续参考；不覆盖 NC/UHPC material authority，也不允许带回 formal spatial quadrature/material points。

## 13. NC / reinforcement / UHPC / shell 当前边界

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

## 14. 当前明确未执行

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

## 15. 后续恢复优先读取

1. `current/CURRENT_STATE.md`；
2. `governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`；
3. `current/theory/NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`；
4. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`；
5. `current/theory/NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`；
6. `current/theory/NZ_SCCM_M1R_SOURCE_SHAPED_RATIONAL_PRIMITIVE_SCREEN_R01_20260810.md`；
7. `current/theory/NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_CLASSIFICATION_R02_20260810.md`；
8. `current/theory/NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_ABSOLUTE_X_CLOSURE_R03_20260810.md`；
9. `current/theory/NZ_SCCM_PF1_RELATIVE_X_ENDPOINT_COMPATIBLE_REDUCTION_R04_20260810.md`；
10. `current/theory/NZ_SCCM_PF1_RELATIVE_ENDPOINT_HYPERGEOMETRIC_CLOSURE_R04_20260810.md`；
11. `current/theory/nz_sccm_pf1_relative_endpoint_hypergeometric_r04.py`；
12. `current/theory/NZ_SCCM_PF1_RELATIVE_ENDPOINT_HYPERGEOMETRIC_R04_results.json`；
13. `evidence/mathematics/PF1_GRIFFITHS_HYPERELLIPTIC_DERHAM_SOURCE_MAP_20260810.md`；
14. `evidence/stability/STEEL_NONDISCRETIZATION_SEMIANALYTIC_REFERENCE_MAP_20260810.md`。
