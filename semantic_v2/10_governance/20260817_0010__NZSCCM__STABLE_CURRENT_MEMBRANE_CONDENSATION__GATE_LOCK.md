# NZ-SCCM governance lock — stable current membrane condensation

**时间：2026-08-17 00:10 +08:00**

## 1. 保留项

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = RETAIN
Nguyen second-order continuous kinematics = RETAIN
R10 physical current material law = FROZEN
reinforcement before coupled solve = RETAIN
five-term leading compatible membrane subspace = RETAIN
General-D15 exact structural moments = RETAIN
outer global topology = (D,q)
zero formal spatial/thickness numerical quadrature = RETAIN
```

## 2. 被撤回的实现资格

```text
20260816_2136 LEGACY_N48 + FIVE_FREE_Rm_ROOT PRODUCTION OVERRIDE = RETRACTED
Rm=0 ALONE AS INTERNAL CONDENSATION QUALIFICATION = PROHIBITED
Krr INVERTIBLE ALONE AS SCHUR QUALIFICATION = PROHIBITED
```

理由：19:12 已经对 legacy N48 current five-coordinate solve 做过 fail-fast rejection；21:36 anti-loop pivot 没有新的 mechanics/fidelity 证明来推翻这一结论。

## 3. 新的内部膜稳定门禁

对五项内部坐标 `r`，current equilibrium 仍必须满足

\[
R_m(D,q,r)=0.
\]

但正式静力凝聚之前，还必须确认当前内部块属于稳定响应支。

最低实现门：

\[
K_{rr}=\partial R_m/\partial r,
\]

\[
K_{rr}^{sym}=\frac12(K_{rr}+K_{rr}^T),
\]

\[
\boxed{\lambda_{min}(K_{rr}^{sym})>0}.
\]

如果最终从同一势能/一致切线严格得到对称 `Krr`，则直接使用 `lambda_min(Krr)>0`。

只有通过该门，才允许：

\[
r_{,g}=-K_{rr}^{-1}R_{m,g}
\]

和

\[
K_{gg}^{cond}=K_{gg}-K_{gr}K_{rr}^{-1}K_{rg}.
\]

## 4. 内部稳定丧失不是“换根”信号

首次出现

\[
\lambda_{min}(K_{rr}^{sym})=0
\]

必须定义为：

```text
INTERNAL_MEMBRANE_STABILITY_EVENT
```

此时：

```text
DO_NOT_CONTINUE_TO_ANOTHER_Rm_ROOT = YES
DO_NOT_SCHUR_CONDENSE_UNSTABLE_INTERNAL_ROOT = YES
DO_NOT_INTERPRET_NEW_ROOT_AS_MEMBRANE_REDISTRIBUTION = YES
```

必须转入 full coupled tangent / mixed-event 判断，决定它与外层荷载峰值、Zhou/Navier KZ 等事件的先后关系。

## 5. 经典退化与尺度门必须同时通过

每次 current membrane implementation 都必须满足：

```text
ELASTIC_AIRY_FVK_DEGENERATION = EXACT
CLASSICAL_POSTBUCKLING_SIGN = POSITIVE
EDGEWARD_AXIAL_STRESS_REDISTRIBUTION = RECOVERED
CASE21_SMALL-M_DRIVER -> SMALL-PERTURBATION EXPECTATION
Z6_LARGE-M / HIGH-b/t -> MUCH STRONGER MEMBRANE EFFECT
```

这些是理论资格门，不是试验校准目标。

## 6. Z6 边界不得共享 Case21 简单场

Z6 historical boundary evidence requires:

```text
loaded ends ux=0
lateral sides in-plane free
```

所以 Z6 必须使用 boundary-admissible Airy/homogeneous biharmonic family，再进入 current-material internal stability/condensation；不得直接复制 Case21 free-Poisson five-term closure。

## 7. capacity status

```text
Case21 320.749185 kN = RETRACTED / unstable-overrelaxation diagnostic
Z6 43.762840 MN = RETRACTED / boundary+stability diagnostic
NEW_CORRECTED_MEMBRANE_Pu = NOT RELEASED
```

## 8. anti-loop

```text
DO_NOT_REOPEN_R10 = YES
DO_NOT_CALIBRATE_TO_EXPERIMENT = YES
DO_NOT_OPEN_ANOTHER_UNBOUNDED_INTEGRATION_BACKEND = YES
DO_NOT_USE_GAUSS_ORACLE_AS_FORMAL_PRODUCTION = YES
```

## 9. 唯一下一门禁

`STABLE_CURRENT_MEMBRANE_CONDENSATION_AND_MIXED_EVENT_GATE`

先在 Case21 上定位 origin-connected stable `Rm=0` branch 的首次 internal-stability event，并判断它与 retained support peak 的先后关系；之后再进入 Z6 mixed-boundary family。
