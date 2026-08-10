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

允许 finite named special functions、finite algebraic covers、finite de-Rham bases、finite coefficient matrices、finite Gauss–Manin/Picard–Fuchs differential systems；这些对象只能解析表示同一个完整半波积分，不得变成隐藏的空间/材料点离散。

用户在 PF1 执行前再次明确：**基础限制不能变，路径不能偏离。** 当前唯一治理锁：

`governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`

PF1 若必须违反任一条件，必须停在 FAIL/HOLD；不得静默切换结构问题或积分身份。

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

正式状态：

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

对 pole `r`：

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

## 6. R02：outer family 已定位为 generic genus-2 hyperelliptic-relative period

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

正式分类：

```text
M1R_R02_GENERIC_OUTER_CLASS_A = FAIL
M1R_R02_GENERIC_ORDINARY_ELLIPTIC = INSUFFICIENT
M1R_R02_GENERIC_SIMPLE_APPELL = NOT_GENERAL
M1R_R02_OUTER_PERIOD_CLASS = HYPERELLIPTIC_RELATIVE / PICARD_FUCHS
```

这里 FAIL 的仅是 generic Class-A 假设，M1R 主线没有失败。

## 7. PF1-R03：absolute genus-2 x Gauss–Manin = PASS_EXACT

当前 canonical R03：

- `current/theory/NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_ABSOLUTE_X_CLOSURE_R03_20260810.md`
- `current/theory/nz_sccm_pf1_genus2_gauss_manin_r03.py`
- `current/theory/NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_R03_results.json`

对 square-free degree-5 curve `w^2=P5(x)`，采用：

```text
omega0=dx/w
omega1=x dx/w
omega2=x^2 dx/w
omega3=x^3 dx/w
```

对 parameter derivative `theta`，R03 以固定 9×9 Sylvester/Bezout system 求：

```text
N=A P+B P'
N/w^3 dx=(A+2B')/w dx-2 d(B/w)
```

一次 exact reduction 直接回 4-dimensional de-Rham basis。

```text
PF1_R03_GENUS2_ABSOLUTE_DERHAM_BASIS = PASS_EXACT
PF1_R03_FIXED_9X9_GRIFFITHS_HERMITE_REDUCTION = PASS_EXACT
PF1_R03_ABSOLUTE_X_GAUSS_MANIN = PASS_EXACT
```

R03 没有提前删除 physical relative endpoint term，因此当时保持 endpoint HOLD 是正确的保守门禁。

## 8. PF1-R04：physical algebraic `[0,1]` endpoint 已进一步 PASS_EXACT

新增：

- `current/theory/NZ_SCCM_PF1_RELATIVE_X_ENDPOINT_COMPATIBLE_REDUCTION_R04_20260810.md`
- `current/theory/nz_sccm_pf1_relative_x_endpoint_r04.py`
- `current/theory/NZ_SCCM_PF1_RELATIVE_X_ENDPOINT_R04_results.json`

Case21/R02 curve 具有比一般 hyperelliptic family 更强的固定 branch-factor：

```text
h=x(1-x)
P=h Gamma
P_,theta=h Gamma_,theta
```

对 `N=-1/2 x^k P_,theta=h Ntilde`，R04 改写为固定 7×7 endpoint-compatible reduction：

```text
Ntilde=Atilde Gamma + C h Gamma'
B_rel=h C
A=Atilde-C h'
N=A P+B_rel P'
```

其 determinant：

```text
Res(Gamma,h Gamma')
=Res(Gamma,h) Res(Gamma,Gamma')
```

在 `P=h Gamma` square-free 时非零。

关键 endpoint identity：

```text
B_rel/w
= C sqrt[h/Gamma]
-> 0 at x=0 and x=1
```

所以 physical `[0,1]` chain 上：

```text
integral d(B_rel/w) = 0 exactly
```

不需要 endpoint cells、tangential subtraction 或 numerical endpoint integration。

三个 exact rational states、`theta=D,M,y`、`k=0..3` 共 36 个 reductions 全部满足：

```text
N=A P+B_rel P' exactly
B_rel(0)=0 exactly
B_rel(1)=0 exactly
```

正式升级：

```text
PF1_R04_ENDPOINT_COMPATIBLE_7X7_REDUCTION = PASS_EXACT
PF1_R04_PHYSICAL_ALGEBRAIC_X_ENDPOINT = PASS_EXACT
```

## 9. PF1-R04：single-resolvent log divisor 已显式定位，但 extended connection 仍 HOLD

R02 endpoint：

```text
Delta_r(s±)=E_r±sqrt(xy) O_r
```

固定 `y` 时 `degree_x(E_r)<=1`、`degree_x(O_r)<=1`。

令：

```text
x=t^2
eta^2=y
Phi±(t)=E_r(t^2)±eta t O_r(t^2)
```

则：

```text
degree_t Phi± <= 3
Phi+ Phi- = E_r(t^2)^2-y t^2 O_r(t^2)^2
```

exact witness：

```text
D=1, M=1, nu=1/5, r=2, y=1/4, eta=1/2, B=1/3
Phi+=-(60t^3+176t^2+183t-1644)/360
Phi-=(60t^3-176t^2+183t+1644)/360
gcd(Phi+,Phi-)=1
disc(Phi+)=disc(Phi-)=-9482483/559872 != 0
```

因此 direct `log[Delta(s+)/Delta(s-)]` 的 branch data 由两个 finite cubic divisors 控制，不需要 TT/TC/CC 空间前沿或 cells。

对 quadratic-root/atanh endpoint cross-ratio，若：

```text
Delta=alpha s^2+beta s+gamma
delta=beta^2-4 alpha gamma
s±=a±c, c=2B sqrt(xy)
```

则可严格写成：

```text
(F+2 c hq)/(F-2 c hq)
hq=sqrt(delta)/(2 alpha)
```

并利用 `Gamma_r=4xy delta` 化为：

```text
(alpha F+B sqrt(Gamma_r))/(alpha F-B sqrt(Gamma_r))
```

故 atanh/root-log 也落在 finite algebraic divisor family 上。

当前正式身份：

```text
PF1_R04_DIRECT_LOG_DIVISOR_IDENTIFICATION = PASS_EXACT
PF1_R04_LOG_RELATIVE_EXTENDED_CONNECTION = HOLD
PF1_R04_PAIR_BLOCK_EXTENSION = NOT_YET_CLOSED
PF1_R04_Y_WHOLE_HALFWAVE_CLOSURE = NOT_YET_CLOSED
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

“divisor finite”不能偷换成“log period 已闭合”。

## 10. 当前唯一下一任务：PF1-R05

继续严格保持 `PF1_PATH_INVARIANTS_LOCK`。下一步只做：

```text
single-resolvent log family
-> choose finite algebraic cover for Phi/Psi divisors
-> compact + third-kind/relative generators
-> differentiate log-weighted generators
-> Hermite/Griffiths reduce back to finite extended basis
-> exact matrix identity audit
```

必须实际给出 finite basis 和 exact reduction matrix，不能只引用“relative/twisted cohomology 理论上有限维”。

R05 PASS 后才允许：

```text
pair-resolvent relative extension
-> y-direction closure
-> whole-halfwave finite analytic system
```

若 R05 需要 spatial/auxiliary numerical quadrature、endpoint cells、material points、改变 P/Rq/L 或 route switch，则停止并报告 HOLD/FAIL。

coarea/pushforward 只有 PF1 真正失败并形成新 checkpoint 后才可打开。

## 11. steel semi-analytical reference lane

钢结构 non-discretization / Rayleigh–Ritz / semi-analytical postbuckling 文献继续保留为 structural-method reference only：

`evidence/stability/STEEL_NONDISCRETIZATION_SEMIANALYTIC_REFERENCE_MAP_20260810.md`

它可以支持连续场/有限 generalized-coordinate、变分、平衡路径、imperfection sensitivity、shell/Y 后续参考；不覆盖 NC/UHPC material authority，也不允许带回 formal spatial quadrature/material points。

## 12. NC / reinforcement / UHPC / shell 当前边界

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
3. `current/theory/NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`；
4. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`；
5. `current/theory/NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`；
6. `current/theory/NZ_SCCM_M1R_SOURCE_SHAPED_RATIONAL_PRIMITIVE_SCREEN_R01_20260810.md`；
7. `current/theory/NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_CLASSIFICATION_R02_20260810.md`；
8. `current/theory/NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_ABSOLUTE_X_CLOSURE_R03_20260810.md`；
9. `current/theory/NZ_SCCM_PF1_RELATIVE_X_ENDPOINT_COMPATIBLE_REDUCTION_R04_20260810.md`；
10. `evidence/mathematics/PF1_GRIFFITHS_HYPERELLIPTIC_DERHAM_SOURCE_MAP_20260810.md`；
11. `evidence/stability/STEEL_NONDISCRETIZATION_SEMIANALYTIC_REFERENCE_MAP_20260810.md`。
