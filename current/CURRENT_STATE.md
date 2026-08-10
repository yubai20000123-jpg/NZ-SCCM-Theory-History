# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10  
**Purpose:** 唯一当前工作入口；历史 PASS/旧路线不得覆盖本文件。

## 1. 正式主线与固定边界

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
```

允许 finite named special functions / finite differential systems，但不得把原空间积分用数值 quadrature 重新定义。

## 2. 已闭合基础

Case21 Nguyen 二阶单半波的 invariant/exact-moment foundation 已闭合：

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

新增：

- `current/theory/NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_CLASSIFICATION_R02_20260810.md`
- `current/theory/nz_sccm_m1r_outer_resolvent_hyperelliptic_r02.py`
- `current/theory/NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_R02_results.json`

五个 primitive 的 numerator/denominator degree 相同，当前 denominator roots simple，因此：

```text
primitive = constant + finite simple scalar resolvents
```

总 scalar poles = 27。

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

因此 stress 最多为：

```text
1 constant + 27 consolidated single-pole + 106 pair-pole blocks
```

这是 finite analytic block count，不是空间离散。

```text
M1R_R02_RESOLVENT_CANONICALIZATION = PASS_EXACT
M1R_R02_ACTUAL_S_FACTORS = QUADRATIC_ONLY
N_s_quadrature = 0
```

actual s-antiderivative 不需要 quartic roots；每个 `Delta_r(s)` 仅二次，pair block 保留两个 quadratic factors。

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

## 7. outer family 已定位为 generic genus-2 hyperelliptic-relative period

R01 outer weight 为 `dx dy/sqrt[x(1-x)y(1-y)]`。固定 generic interior y 后，single-resolvent algebraic radical对应：

```text
w^2=x(1-x)Gamma_r(x,y)
```

`Gamma_r` generically cubic in x，因此右侧 generically degree 5。

R02 exact witness：

```text
D=1, M=1, nu=1/5, r=2, y=1/3
Gamma=(225x^3+1950x^2-10031x+7920)/675
P5=-x(x-1)(225x^3+1950x^2-10031x+7920)/675
degree(P5)=5
gcd(P5,P5')=1
discriminant(P5)=7162455748218191872/3503151123046875 != 0
```

故存在 nondegenerate genus-2 specialization。generic outer family不能假定全部落入 elementary/Beta、ordinary elliptic 或一个简单 Appell family；log/atanh endpoint 项属于 relative algebraic-log periods。

正式分类：

```text
M1R_R02_GENERIC_OUTER_CLASS_A = FAIL
M1R_R02_GENERIC_ORDINARY_ELLIPTIC = INSUFFICIENT
M1R_R02_GENERIC_SIMPLE_APPELL = NOT_GENERAL
M1R_R02_OUTER_PERIOD_CLASS = HYPERELLIPTIC_RELATIVE / PICARD_FUCHS
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

这里 FAIL 的只是“generic outer Class A”假设，M1R 路线本身未失败。

## 8. 当前唯一下一任务：PF1

```text
PF1 = finite Gauss-Manin / Picard-Fuchs closure
      for canonical M1R outer resolvent periods
```

顺序：single-resolvent algebraic kernel -> genus-2 de-Rham basis -> Griffiths/Hermite derivative reduction -> log relative periods -> pair blocks -> 闭合 y 方向 -> whole-halfwave finite differential system。

只有形成 finite analytic system、branch/initial-value specification、稳定 special-function evaluator，以及 analytic D/q derivatives，Gate A 才能从 HOLD 改为 `PASS_CLASS_B`。

coarea/pushforward 仅在 PF1 真正失败后进入；当前不并行展开。

## 9. 其他模块边界

钢结构 non-discretization / semi-analytical 文献继续作为 structural-method reference only；不覆盖 NC/UHPC material authority，也不改变 formal integration identity。

old NC+reinforcement 仅作 regression/reference；钢筋仍必须在 root solve 前进入 `P` 与 `Rq`，禁止事后 `Pu=Pu,c+As fy`。

UHPC 仅 `fc=141.1 MPa` 为强制保留值；final UHPC operator 未闭合。final shell operator 仍：

```text
M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE
```

PBL 继续作为强局部边界/子板分隔，不自动作为独立轴向承载项或显式 spring energy。

## 10. 本阶段未执行

```text
NO new Case21 Pu solve
NO Swartz24 solve
NO UHPC production fit
NO shell/Y production solve
NO structural Pu calibration
```

## 11. 后续恢复优先读取

1. 本文件；
2. `NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`；
3. `NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`；
4. `NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`；
5. `NZ_SCCM_INVARIANT_COORDINATE_LIFT_EXACT_REDUCTION_R01_20260810.md`；
6. `NZ_SCCM_M1R_SOURCE_SHAPED_RATIONAL_PRIMITIVE_SCREEN_R01_20260810.md`；
7. `NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_CLASSIFICATION_R02_20260810.md`；
8. `evidence/stability/STEEL_NONDISCRETIZATION_SEMIANALYTIC_REFERENCE_MAP_20260810.md`。
