# NZ-SCCM — 五项膜内凝聚 / RC1-D15 门禁审计

**时间：2026-08-16 19:12 +08:00**

## A. 理论身份审计

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = PRESERVED
GLOBAL_COORDINATES = (D,q) PRESERVED
NGUYEN_SECOND_ORDER = PRESERVED
R10_SOURCE_OPERATOR = UNCHANGED
REBAR_CURRENT_LAW = UNCHANGED
GENERAL_D15 = PRESERVED
P_Rq_L_TOPOLOGY = PRESERVED
SAME_STATE_TANGENT = REQUIRED
FREE_p20_p02 = NOT REINTRODUCED
```

五个 `r` 是有限内部膜响应坐标，不是五条独立承载力路径，也不是把外层 Pu 求解改成七维 root cloud。

## B. exact elastic limit audit

解析矩阵：

```text
K/pi^2 =
[1,
  1/2,
  2x2 block ((3-nu)/8,(1+nu)/8),
  1/2]
```

精确性质：

```text
detK = pi^10*(1-nu)/32
eigen(K/pi^2) = {1,1/2,1/2,1/2,(1-nu)/4}
fD = 0
r/M = [-(1+nu)/4,-(1-nu)/4,1/4,-(1-nu)/4,1/4]
```

对 `nu=.18`：

```text
min eigen=.205
max eigen=1
cond2=4.87805
```

没有 classical membrane mechanism singularity。

代回得到：

```text
sigma_x/(E eps0)=-M cos2Y/4
sigma_y/(E eps0)=-D+M sin^2X/2
tau_xy=0
```

因此：

```text
ELASTIC_AIRY_FVK_EQUIVALENCE = PASS_EXACT
```

## C. compatibility / D15 audit

五个基全部来自显式相容面内位移。

Normal kernels 使用：

```text
cos2X=1-2 sin^2X
cos2Y=1-2 sin^2Y
```

`22` shear work 中两个 `cosX cosY` 因子相乘为偶次方，故可精确化为 `1-sin^2`。

所以最终 scalar target integrands 都属于已有 General-D15 finite integer-trigonometric/thickness polynomial family。

```text
FIVE_TERM_GENERAL_D15_FUNCTION_SPACE = PASS
NEW_SPATIAL_QUADRATURE_NEEDED = NO
```

## D. current-material formulation audit

正式 nonlinear residual 必须是

```text
Rm_j=sum_p int sigma_p(current strain):B_j dV
```

一致切线：

```text
Krr=dRm/dr
```

凝聚：

```text
r_g=-Krr^-1 Rm_g
Pbar_g=P_g+P_r r_g
Rqbar_g=Rq_g+Rq_r r_g
Kgg_cond=Kgg-Kgr Krr^-1 Krg
```

这与 current stress / consistent tangent 规则一致。

```text
CURRENT_MATERIAL_CONDENSATION_FORM = PASS_FORMAL
```

## E. legacy N48 diagnostic audit

旧 N48-C1 CH/D15 被临时用于历史 Case21 状态的 current residual 诊断。其目的只验证：classical elastic coefficients 不能硬塞给 nonlinear current material。

在 classical r 处残量明显非零；一次 generalized-coordinate Jacobian diagnostic 给出 `cond~8.53e2` 和很大的首步更新。该 route 非当前 RC1，故按 fail-fast 停止。

```text
LEGACY_N48_DIAGNOSTIC_USED_FOR_NEW_Pu = NO
LEGACY_N48_DIAGNOSTIC_USED_TO_TUNE_RC1 = NO
FAIL_FAST = PASS
```

## F. RC1 backend audit

`R10-MSAC-RC1` 当前已通过 Z0-Z6 material source-fidelity gate，但其 nested factor graph 尚无经本轮实际验证的

```text
arbitrary target kernel
 -> adjoint-Clenshaw/Qnm
 -> General-D15 exact contraction
```

高阶 runtime。

本轮仅把 target API 和理论闭合固定为：

```text
contract(state,target_kernel)
```

并证明五个膜残量属于该接口。

因此：

```text
RC1_NESTED_TARGET_FUNCTIONAL_THEORY_INTERFACE = PASS
RC1_NESTED_TARGET_FUNCTIONAL_EXECUTION = OPEN
```

不得将 formal interface 冒充 completed production backend。

## G. zero-integration audit

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Gauss = 0
Simpson = 0
adaptive = 0
collocation = 0
material-point grid = 0
```

## H. capacity audit

```text
Case21 368.189 kN = historical/current-support reference only
Z6 51.30 MN = retained engineering baseline only
NEW_MEMBRANE_REDISTRIBUTED_CASE21_Pu = NOT_RUN
NEW_MEMBRANE_REDISTRIBUTED_Z0_Z6_Pu = NOT_RUN
```

## I. final verdict

```text
FIVE_TERM_ELASTIC_CONDENSATION = PASS_EXACT
FIVE_TERM_AIRY_FVK_RECOVERY = PASS_EXACT
FIVE_TERM_GENERAL_D15_TARGET_CLOSURE = PASS
CURRENT_MATERIAL_CONDENSATION_FORM = PASS_FORMAL
RC1_TARGET_FUNCTIONAL_RUNTIME = OPEN
OVERALL_GATE = PARTIAL_PASS_TO_IMPLEMENTATION_BOUNDARY
```

唯一下一门禁：

```text
UNIFIED_V1_RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_FUNCTIONAL_EXECUTION_GATE
```
