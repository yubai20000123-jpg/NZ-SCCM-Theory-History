# NZ-SCCM — 膜力闭合转换与内部稳定性审计

**时间：2026-08-17 00:10 +08:00**

## 审计结论

本轮确认此前 `Case21 Pu=320.749185 kN` 与 `Z6 Pu~=43.762840 MN` 的下降不能解释为正确膜力重分布的物理结果。错误由两层叠加造成：

1. **治理层回归**：2026-08-16 19:12 已明确判定 legacy N48 five-coordinate current root `REJECTED / NOT_AUTHORIZED`；21:36 为反循环而重新激活该 route 时，没有完成新的物理/切线资格证明。
2. **力学门禁缺失**：后续仅要求 `Rm=0` 和 `Krr` 可逆，即直接 Schur 凝聚；没有要求内部膜模态本身保持稳定。因此求解器可以从原点附近的稳定 root 连续漂移到 saddle/unstable `Rm=0` root，再把它凝聚成表面上正常的 `(D,q)` 路径。

## 证据链

### A. 18:48 / 19:12 elastic degeneration

五项基在线弹性平面应力下具有正定内能矩阵，并精确恢复 Airy/FvK：

```text
r/M=[-.295,-.205,+.25,-.205,+.25]  for nu=.18
Kbar eig=[.205,.5,.5,.5,1]
```

因此 basis 本身保留。

### B. 19:12 legacy N48 fail-fast 已经预警

历史 Case21 state + Airy-leading r 下：

```text
Rhat_total=[+2.69233687,+.13819441,-.31339370,-15.52815375,+3.00791537]
cond2(J)≈8.53e2
delta_r≈[-.01434,+.00398,-.48827,+.08584,+1.60404]
```

19:12 当时正确停止并锁定：

```text
LEGACY_N48_AS_CURRENT_PRODUCTION = REJECTED
NEW_R_SOLVE = NOT_AUTHORIZED
```

### C. Case21 continuation 的 Airy-direction 漂移

K-投影：

```text
point1: lambda_A=+1.1373, K-perp ratio=.1624
point2: lambda_A=+1.0979, K-perp ratio=.2198
retracted 320.75-kN state: lambda_A=-1.1460, K-perp ratio=.9719
```

说明 origin-connected branch 起初具有正确正向特征，随后被允许进入几乎完全脱离 Airy leading direction 的 relaxation root。

### D. direct frozen-R10 oracle 排除“仅 N48 误差”解释

在历史 Case21 D,q 上，直接 R10：

- scalar Airy manifold `r=lambda*M*a` 的 projected equilibrium 有**正根** `lambda=.0677334`，且 projected derivative 为正；所以物理膜效应方向没有反号。
- 但 scalar manifold 不能令五个正交 residual 同时为零，因此不能冻结为最终 nonlinear closure。
- 放开完整五坐标可得到 `Rm≈0`，但 `sym(Krr)` 特征值出现两个负值：

```text
[-238.65,-28.05,+281.46,+492.27,+733.27]
```

所以该 full `Rm=0` root 是内部不稳定/鞍点，不具备稳定静力凝聚资格。

低 q point1/point2 对照的 `sym(Krr)` 全正，最小值约 `+91.24`、`+87.79`，说明真正的问题是**稳定主支在推进中丧失内部正定性后，算法仍继续寻找别的 Rm root**。

## 正确的 Schur 资格

`Rm=0` 只是内平衡条件，不是稳定性条件。

在当前 conservative/consistent second-work 解释下，正式内部凝聚至少必须要求

\[
K_{rr}^{sym}=\frac12(K_{rr}+K_{rr}^T),
\qquad
\lambda_{min}(K_{rr}^{sym})>0.
\]

若最终 current tangent 能严格证明对称，则直接退化为 `Krr>0`。

只有同时满足

```text
Rm=0
internal membrane block stable
```

才允许

\[
K_{gg}^{cond}=K_{gg}-K_{gr}K_{rr}^{-1}K_{rg}.
\]

若 `lambda_min` 首次到零：

```text
INTERNAL_MEMBRANE_STABILITY_EVENT = ACTIVE
DO_NOT_RELAX_THROUGH_EVENT = YES
DO_NOT_CONDENSE_UNSTABLE_R_ROOT = YES
```

该事件必须进入 full coupled tangent/stability 判断。

## Z6 独立边界审计

Z6 不能简单共享 Case21/free-Poisson five-term field。历史 00:16 已确认 Zhou/Z6 loaded-end `ux=0` + free lateral sides 需要额外 homogeneous biharmonic boundary family。

因此未来 Z6 current-material 膜力闭合必须在该 mixed-boundary admissible family 上执行稳定凝聚。

## Gate verdict

```text
FIVE_TERM_SHAPE_SPACE = PASS / RETAIN
ELASTIC_AIRY_DEGENERATION = PASS_EXACT
Rm_ZERO_ONLY_AS_CLOSURE = FAIL
Krr_INVERTIBLE_ONLY_AS_SCHUR_GATE = FAIL
INTERNAL_MEMBRANE_STABILITY_GATE = REQUIRED
LEGACY_N48_FIVE_COORDINATE_OVERRIDE_2136 = RETRACTED
CASE21_320P75 = RETRACTED_DIAGNOSTIC
Z6_43P76 = RETRACTED_DIAGNOSTIC
NEW_CORRECTED_Pu = NOT_RUN
OVERALL = PASS_TO_STABLE_CURRENT_MEMBRANE_CONDENSATION_GATE
```

## 唯一下一步

`STABLE_CURRENT_MEMBRANE_CONDENSATION_AND_MIXED_EVENT_GATE`
