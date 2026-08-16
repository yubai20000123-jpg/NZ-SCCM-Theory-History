# NZ-SCCM — 五项膜内凝聚 + RC1/D15 门禁执行报告

**时间：2026-08-16 19:12 +08:00**

## 1. 执行对象

本轮执行门禁：

```text
UNIFIED_V1_CURRENT_MATERIAL_FIVE_TERM_MEMBRANE_CONDENSATION_PLUS_RC1_D15_GATE
```

继承：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order
R10 source operator frozen
reinforcement current adapter
General-D15 exact moments
P,Rq,L connected branch
same-state tangent/KZ
zero formal spatial/thickness quadrature
```

没有调用试验值、Zhou、Winter 或历史 Pu 做求解/调参。

## 2. exact elastic five-coordinate solve

采用内部坐标

```text
r = [r0,r20,r22,s02,s22]
```

并对平面应力双线性型进行解析积分。

得到

```text
K/pi^2 =
[[1, 0, 0, 0, 0],
 [0, 1/2, 0, 0, 0],
 [0, 0, (3-nu)/8, 0, (1+nu)/8],
 [0, 0, 0, 1/2, 0],
 [0, 0, (1+nu)/8, 0, (3-nu)/8]]

fM/pi^2 = [(1+nu)/4,(1-nu)/8,-1/8,(1-nu)/8,-1/8]
fD = [0,0,0,0,0]

det(K)=pi^10*(1-nu)/32
```

精确求解

```text
r/M = [-(1+nu)/4, -(1-nu)/4, 1/4, -(1-nu)/4, 1/4]
```

与 18:48 Airy/FvK closed-form delta 完全一致。

对 `nu=.18`：

```text
Kbar eigenvalues = [.205,.5,.5,.5,1]
cond2(Kbar) = 4.878048780487805
```

因此五项基在线弹性基准中条件良好，不存在此前 free-p20/p02 那种人为松弛奇异性。

## 3. exact Airy stress recovery

代回应变后得到

```text
sigma_x/(E*eps0) = -M/4*cos(2Y)
sigma_y/(E*eps0) = -D + M/2*sin(X)^2
tau_xy             = 0
```

即 exact classical Airy/FvK membrane redistribution。

判定：

```text
FIVE_TERM_ELASTIC_CONDENSATION = PASS_EXACT
FIVE_TERM_AIRY_FVK_RECOVERY = PASS_EXACT
```

## 4. current-material condensation contract

正式 nonlinear RC 方程固定为

```text
e(D,q,r,zeta)=e_Nguyen_old(D,q,zeta)+sum_j r_j B_j
sigma_c=M_R10(e)
sigma_s=M_s(n^T E n)
Rm_j=sum_p int sigma_p:B_j dV = 0
```

一致切线及凝聚：

```text
Krr = dRm/dr
r_,g = -Krr^-1 Rm_,g, g=(D,q)
Pbar_,g = P_,g + P_,r r_,g
Rqbar_,g = Rq_,g + Rq_,r r_,g
Lbar = Pbar_D Rqbar_q - Pbar_q Rqbar_D
Kgg_cond = Kgg-Kgr Krr^-1 Krg
```

所以 outer production root 仍然只有 `(D,q)`。

判定：

```text
CURRENT_MATERIAL_RESIDUAL_FORM = PASS_FORMAL
CURRENT_MATERIAL_CONSISTENT_CONDENSATION = PASS_FORMAL
GLOBAL_STRUCTURAL_ROOT_TOPOLOGY = UNCHANGED
```

## 5. General-D15 target-kernel closure

五个 concrete membrane target 被写为

```text
T0   = D15[Sxx]
T20  = D15[Sxx*cos2X]
Tu22 = D15[Sxx*cos2X*cos2Y - Sxy*sin2X*sin2Y]
T02  = D15[Syy*cos2Y]
Tv22 = D15[Syy*cos2X*cos2Y - Sxy*sin2X*sin2Y]
```

其中

```text
cos2X = 1-2 sin^2 X
cos2Y = 1-2 sin^2 Y
```

而 shear work 中的 `cosX*cosY` 因子成对出现，可用 `cos^2=1-sin^2` 精确消去。因此最终 scalar target integrand 属于现有 General-D15 integer trigonometric/thickness polynomial family。

判定：

```text
FIVE_TERM_GENERAL_D15_TARGET_CLOSURE = PASS
NEW_SPATIAL_BASIS_REQUIRING_QUADRATURE = NO
```

## 6. benchmark amplitudes

### Case21 historical/current-support state

```text
M=.02869338081034484
nu=.18
r0  =-.008464547339051727
r20 =-.0058821430661206925
r22 =+.00717334520258621
s02 =-.0058821430661206925
s22 =+.00717334520258621
```

physical compatible displacement scales:

```text
u0(full-width)=-.0215829028051 mm
u20 amplitude =-.00238705173519 mm
u22 amplitude =+.00291103870145 mm
v02 amplitude =-.00238705173519 mm
v22 amplitude =+.00291103870145 mm
```

### Z6 retained engineering-baseline state

```text
M=1.6948726156196714
r0  =-.499987421607803
r20 =-.347448886202033
r22 =+.423718153904918
s02 =-.347448886202033
s22 =+.423718153904918
```

physical compatible displacement scales:

```text
u0(full-width)=-11.2272117891 mm
u20 amplitude =-1.24172061675 mm
u22 amplitude =+1.51429343506 mm
v02 amplitude =-1.24172061675 mm
v22 amplitude =+1.51429343506 mm
```

这些只是 classical elastic benchmark coordinates，不是 nonlinear R10 solution。

## 7. legacy N48 current-material fail-fast diagnostic

为了验证上句，本轮把五项 basis 临时接入历史 Case21 的 N48-C1 coefficient-space CH/D15 kernel；该 route 明确不是当前 RC1 production。

使用：

```text
Case21 D=.8359179831666168
q=.0017897894751107222
compiler interval=[-1.01,.105]
N=48
classical r as initial diagnostic state
```

定义

```text
Rhat = pi^2/(eps0*b*ell*t) * Rm
```

得到

```text
Rhat_total = [
 +2.69233687,
 +.13819441,
 -.31339370,
 -15.52815375,
 +3.00791537]

Rhat_concrete = [
 +.38452432,
 +.12820657,
 -.31339370,
 -15.53814159,
 +3.00791537]

Rhat_rebar = [
 +2.30781255,
 +.009987839,
 ~0,
 +.009987839,
 ~0]
```

因此 `r_classical` 在 nonlinear R10+rebar current state 下并非 `Rm=0`，符合理论预期。

随后以 generalized-coordinate perturbation `2e-4` 形成一次 5x5 diagnostic Jacobian：

```text
J ≈
[[ 448.483939,  16.366324, -16.407897,   1.448734,  -2.781585],
 [  16.464411, 223.457600,   2.909393,  -3.059928,   .555910],
 [ -29.372389,  -.411754, 131.031918,   1.413017,  39.744523],
 [-602.844440,-272.711727,  25.354833, 117.628140,   6.391122],
 [-286.584350,-327.662779, 270.294124,   4.492820,  78.413268]]

cond2(J) ≈ 8.53e2
```

首个 Newton diagnostic increment：

```text
delta_r ≈ [-.01434073,+.00398039,-.48827257,+.08583724,+1.60404024]
```

如此大的增量说明不能把旧 N48 route 当当前 five-term production 求解器继续推进；其 material compiler 也不是当前 RC1。故立即停止，没有继续找 root，更没有计算 Pu。

判定：

```text
LEGACY_N48_FIVE_TERM_DIAGNOSTIC = EXECUTED
LEGACY_N48_AS_CURRENT_PRODUCTION = REJECTED
FAIL_FAST = APPLIED
```

## 8. RC1 implementation boundary

当前 `R10-MSAC-RC1` 只在材料层完成 source-fidelity gate。其 nested graph 为

```text
lambda
 -> beta-lens gate
 -> c(lambda),t(lambda)
 -> C(c)
 -> uR(t),T7(t)
 -> T
 -> U
 -> R10 interactions
```

不能把这张图 full-expand 成普通多项式。

本轮已经固定 target-functional API：

```text
contract(state, target_kernel)
```

其中 `target_kernel` 可以是 `P,Rq,Rm1...Rm5,KZ` 所需任一有限核。

但尚未完成：

```text
nested RC1 -> adjoint Clenshaw/Qnm -> General-D15 target value
```

的真实高阶运行实现。

所以：

```text
RC1_NESTED_TARGET_FUNCTIONAL_EXECUTION = OPEN
NEW_R_SOLVE = NOT_AUTHORIZED
NEW_Pu = NOT_RUN
```

## 9. formal counters

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
spatial_Gauss = 0
spatial_Simpson = 0
spatial_adaptive = 0
spatial_collocation = 0
material_point_grid = 0
```

## 10. gate result and unique next gate

```text
OVERALL_GATE = PARTIAL_PASS_TO_IMPLEMENTATION_BOUNDARY
```

当前唯一下一门禁：

```text
UNIFIED_V1_RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_FUNCTIONAL_EXECUTION_GATE
```

目标是让 RC1 nested graph 在不 full-expand stress field 的条件下，直接返回 `P,Rq,Rm1...Rm5,KZ` 的 General-D15 exact contractions；低阶 direct-expansion identity gate 通过后，再进入 five-current-coordinate root + Schur condensation + 新 Pu。
