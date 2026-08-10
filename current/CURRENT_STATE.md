# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10  
**Purpose:** 唯一当前工作入口；历史 PASS/旧路线不得覆盖本文件。

## 1. 正式主线与不可改变的基础边界

```text
finite analytic kinematics
-> finite strain invariants
-> strong nonlinear material law
-> exact analytic material/structural contraction
-> P, Rq, analytic tangent, L
```

```text
P(D,q)
Rq(D,q)=0
L(D,q)=P_,D Rq_,q-P_,q Rq_,D=0
```

formal identity：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT
ELEMENT_INTEGRATION = PROHIBITED
MATERIAL_POINT_GRID = PROHIBITED
SPATIAL_CELLS = PROHIBITED
```

允许 finite named special functions / finite differential systems / finite analytic coefficient matrices，但不得把原空间积分用数值 quadrature、material points、cells 或新的结构问题重新定义。

用户在 PF1 开始前再次明确：**基础限制不能变，路径不能偏离。** 已形成独立硬门禁：

`governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`

PF1 若需要违反上述任一条件，必须停在 FAIL/HOLD，不得通过替代路线静默绕过。

## 2. 已闭合基础

Case21 Nguyen 二阶单半波 invariant/exact-moment foundation 已闭合：

- `NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`
- `NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`

`I1=tr(X)`、`I2=det(X)` 已显式化；`I2` 中 `M^2` 项严格抵消。polynomial material 时 P/Rq 可归结为 finite Beta/Gamma moments。

材料架构必须同时通过：

```text
Gate A = exact analytic / finite special-function closure
Gate B = concrete nonlinear adequacy
```

## 3. M1 -> M1R

M1 simple structured polynomial 已 `FAIL_SCREEN`：182 coefficients 时 global P95≈0.10869，TC P95≈0.37460，且条件数约 1.8e8。

M1R-R01 保留 source-shaped biaxial algebra，只编译 5 个一维 rational primitives：

```text
U, C, C2=C^2, T, V=T^8
```

53 个 material-only coefficients；二维 fitted interaction coefficients=0。同一 frozen-NC material screen：

```text
global P95 = 0.018261
global max = 0.036742
TC P95     = 0.023137
```

```text
M1R_R01_FROZEN_NC_ORACLE_REGRESSION = PASS_SCREEN
FINAL_NC_SOURCE_CALIBRATION = NOT_YET_DONE
FINAL_GATE_B = NOT_YET_FROZEN
```

## 4. `s=I1` inner reduction

Case21：

```text
I1 = a(u,v;D,q)+2Buvz
s = I1
z = (s-a)/(2Buv)
s± = a±2Buv
```

`I2(s;u,v)` 对 s 严格二次。R01 已证明 rational material 的 s-inner 可 exact integrate；R02 进一步把 actual M1R canonicalize 为 pole-resolvent。

## 5. R02：actual M1R resolvent canonicalization = PASS_EXACT

当前文件：

- `current/theory/NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_CLASSIFICATION_R02_20260810.md`
- `current/theory/nz_sccm_m1r_outer_resolvent_hyperelliptic_r02.py`
- `current/theory/NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_R02_results.json`

五个 primitive 具有 finite simple scalar resolvent decomposition，总 scalar poles = 27。

对 pole r：

```text
R_r=(X-rI)^(-1)=[(I1-r)I-X]/Delta_r
Delta_r=I2-r I1+r^2
R_r^oth=(X-rI)/Delta_r
```

source-shaped pair block：

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
N_s_quadrature = 0
```

## 6. R02 endpoint algebra = PASS_EXACT

令 `x=u^2,y=v^2`，`H=x+y-2xy`，`K=nu*x-y+(1-nu)xy`，`a=(nu-1)D+MH`。

```text
s±=a±2B sqrt(xy)
Delta_r(s±)=E_r±sqrt(xy) O_r
```

其中：

```text
E_r=-nu D^2+DMK+B^2(x+y-1)-r a+r^2
O_r=B[D(nu-1)+M(2-x-y)-2r]
```

所以 `degree(E_r)<=2`、`degree(O_r)<=1`，且 `Delta_r(s+)Delta_r(s-)=E_r^2-xy O_r^2` 总阶 <=4。

定义：

```text
Gamma_r=4xy*disc_s[Delta_r(s)]
```

exact audit：

```text
degree_x Gamma_r = 3
degree_y Gamma_r = 3
total_degree Gamma_r = 4
[x^3]Gamma_r = M^2 y
[y^3]Gamma_r = M^2 x
```

## 7. R02 outer classification：generic genus-2 hyperelliptic-relative period

固定 generic interior y 后：

```text
w^2=P5(x)=x(1-x)Gamma_r(x,y)
```

`Gamma_r` generically cubic in x，所以 P5 generically degree 5。R02 exact witness：

```text
D=1, M=1, nu=1/5, r=2, y=1/3
Gamma=(225x^3+1950x^2-10031x+7920)/675
P5=-x(x-1)(225x^3+1950x^2-10031x+7920)/675
degree(P5)=5
gcd(P5,P5')=1
discriminant(P5)=7162455748218191872/3503151123046875 != 0
```

故存在 nondegenerate genus-2 specialization。generic outer family不能假定全部落入 elementary/Beta、ordinary elliptic 或一个简单 Appell family；log/atanh endpoint 项属于 relative algebraic-log periods。

```text
M1R_R02_GENERIC_OUTER_CLASS_A = FAIL
M1R_R02_GENERIC_ORDINARY_ELLIPTIC = INSUFFICIENT
M1R_R02_GENERIC_SIMPLE_APPELL = NOT_GENERAL
M1R_R02_OUTER_PERIOD_CLASS = HYPERELLIPTIC_RELATIVE / PICARD_FUCHS
```

这里 FAIL 的只是“generic Class A”假设，M1R 主线本身未失败。

## 8. PF1-R03：genus-2 absolute x Gauss–Manin 已闭合

新增：

- `current/theory/NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_ABSOLUTE_X_CLOSURE_R03_20260810.md`
- `current/theory/nz_sccm_pf1_genus2_gauss_manin_r03.py`
- `current/theory/NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_R03_results.json`
- `evidence/mathematics/PF1_GRIFFITHS_HYPERELLIPTIC_DERHAM_SOURCE_MAP_20260810.md`

对 square-free degree-5 curve `w^2=P5(x)`，固定 4 维 absolute de-Rham basis：

```text
omega0 = dx/w
omega1 = x dx/w
omega2 = x^2 dx/w
omega3 = x^3 dx/w
```

对任意 parameter theta：

```text
d_theta omega_k = N_kθ dx/w^3
N_kθ = -1/2 x^k P_,θ
```

`deg N<=8`。寻找：

```text
A degree <=3
B degree <=4
N = A P + B P'
```

恰好形成固定 9×9 coefficient system `S(P)`；其 determinant 等于 `Res(P,P')`。因此 P square-free 时唯一可逆。

关键 exact identity：

```text
N/w^3 dx
= (A+2B')/w dx - 2 d(B/w)
```

且 `degree(A+2B')<=3`，所以参数导数一次 reduction 就直接回到同一个 4 维 basis，不需要第二级 degree reduction。

对 closed absolute periods：

```text
d_theta Pi = C_theta Pi
```

其中 `C_theta` 是 4×4 finite rational matrix；所有 coefficient 只来自 P 的解析系数，不存在空间积分点。

R02 exact witness 上：

```text
rank S = 9
det S = Res(P,P')
      = -7162455748218191872/10509453369140625 != 0
```

对 `theta=D,M,y` 和四个 basis forms 的 reduction identities 全部 exact TRUE，并已保存 4×4 rational connection matrices。

正式升级：

```text
PF1_PATH_INVARIANTS = LOCKED
PF1_R03_GENUS2_ABSOLUTE_DERHAM_BASIS = PASS_EXACT
PF1_R03_FIXED_9X9_GRIFFITHS_HERMITE_REDUCTION = PASS_EXACT
PF1_R03_ABSOLUTE_X_GAUSS_MANIN = PASS_EXACT
```

## 9. 当前真正停点：physical relative x endpoint 不能被删除

真实 NZ-SCCM outer x integral 是 `[0,1]` relative chain，且 `x=0,1` 为 Beta branch endpoints；s-antiderivative 还含 algebraic-log / atanh terms。

R03 reduction 保留：

```text
-2 d(B/w)
```

closed cycle 上该项积分为 0，但 physical relative chain 上不能直接扔掉。`B/w` 在 branch endpoint 的单项 representation 可能奇异，必须使用：

```text
t0=sqrt(x)
t1=sqrt(1-x)
```

的局部 branch coordinates 或等价 relative de-Rham/tangential endpoint basis，把 boundary functional 与 log terms 一起闭合。

所以当前仍是：

```text
PF1_R03_PHYSICAL_RELATIVE_X_ENDPOINT = HOLD
PF1_R03_LOG_RELATIVE_EXTENSION = NOT_YET_CLOSED
PF1_R03_PAIR_BLOCK_EXTENSION = NOT_YET_CLOSED
PF1_R03_Y_WHOLE_HALFWAVE_CLOSURE = NOT_YET_CLOSED
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

**不能因为 absolute Gauss–Manin 已 PASS 就提前宣布 whole-halfwave Gate A PASS。**

## 10. 当前下一唯一任务：PF1-R04

```text
physical x-relative chain
-> local branch coordinates x=0,1
-> retain exact-differential boundary functional
-> algebraic-log / third-kind relative generators
-> finite extended connection
-> exact identity audit
```

R04 PASS 后才允许继续 pair-resolvent relative extension，再闭合 y direction。

若 R04 需要 numerical x integration、endpoint cells、material points、改变 P/Rq/L 或切换结构路线，则按 `PF1_PATH_INVARIANTS_LOCK` 停止并报告 FAIL/HOLD。coarea/pushforward 只有 PF1 真正失败并形成新 checkpoint 后才能打开。

## 11. 其他模块边界

钢结构 non-discretization / semi-analytical 文献继续作为 structural-method reference only；不覆盖 NC/UHPC material authority，也不改变 formal integration identity。

old NC+reinforcement 仅作 regression/reference；钢筋仍必须在 root solve 前进入 `P` 与 `Rq`，禁止事后 `Pu=Pu,c+As fy`。

UHPC 仅 `fc=141.1 MPa` 为强制保留值；final UHPC operator 未闭合。final shell operator 仍：

```text
M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE
```

PBL 继续作为强局部边界/子板分隔，不自动作为独立轴向承载项或显式 spring energy。

## 12. 本阶段明确未执行

```text
NO new Case21 Pu solve
NO Swartz24 solve
NO UHPC production fit
NO shell/Y production solve
NO structural Pu calibration
NO spatial quadrature
NO material-point integration
NO route switch
```

## 13. 后续恢复优先读取

1. 本文件；
2. `governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`；
3. `current/theory/NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`；
4. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`；
5. `current/theory/NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`；
6. `current/theory/NZ_SCCM_M1R_SOURCE_SHAPED_RATIONAL_PRIMITIVE_SCREEN_R01_20260810.md`；
7. `current/theory/NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_CLASSIFICATION_R02_20260810.md`；
8. `current/theory/NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_ABSOLUTE_X_CLOSURE_R03_20260810.md`；
9. `evidence/mathematics/PF1_GRIFFITHS_HYPERELLIPTIC_DERHAM_SOURCE_MAP_20260810.md`；
10. `evidence/stability/STEEL_NONDISCRETIZATION_SEMIANALYTIC_REFERENCE_MAP_20260810.md`。
