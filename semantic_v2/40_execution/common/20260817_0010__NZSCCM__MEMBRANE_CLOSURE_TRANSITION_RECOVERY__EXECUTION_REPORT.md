# NZ-SCCM — 18:48→19:12→21:36 膜力闭合转换恢复执行报告

**时间：2026-08-17 00:10 +08:00**  
**门禁：`RECOVER_COMPATIBILITY_COUPLED_CURRENT_MEMBRANE_CLOSURE_FROM_1848_1912_TRANSITION`**

## 1. 本轮只检查什么

本轮不计算新 Pu，不修改 R10，不开发新积分后端。只追踪：

```text
18:48 historical RC backbone + classical compatibility-coupled membrane delta
-> 19:12 five-term elastic/current-material formulation
-> 21:36 anti-loop N48 production pivot
-> 22:xx/23:xx five-coordinate continuation and false Pu
```

目标是找出为什么一个在线弹性退化极限中严格恢复 Airy/FvK 正屈后刚度的五项基，最终会被算成 Case21/Z6 的大幅降载。

---

## 2. 18:48 的正确基线

18:48 已固定：旧 Nguyen 场本身含完整 von-Karman 二阶几何膜应变，新增项只是面内应力/应变重分布修正。

square complete halfwave 下，定义

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right).
\]

经典兼容修正可由五项位移分量表示，线弹性精确方向为

\[
\boxed{
\mathbf a(\nu)=
\left[-\frac{1+\nu}{4},-\frac{1-\nu}{4},\frac14,-\frac{1-\nu}{4},\frac14\right]^T
}
\]

即

\[
\mathbf r_{Airy}=M\mathbf a.
\]

对 `nu=.18`：

```text
a = [-.295,-.205,+.25,-.205,+.25]
```

历史尺度诊断：

```text
Case21 M=.02869338081, (M/4)/D=.85814%
Z6     M=1.69487261562, (M/4)/D=26.7275%
M_Z6/M_Case21=59.0684
```

所以 Case21 应是小修正，而 Z6/high-b/t 应是强膜效应对象。

---

## 3. 19:12：五项基在线弹性极限本身没有错

五个基为

```text
B0   =(1,0,0)
B20  =(cos2X,0,0)
Bu22 =(cos2X cos2Y,0,-sin2X sin2Y)
B02  =(0,cos2Y,0)
Bv22 =(0,cos2X cos2Y,-sin2X sin2Y)
```

线弹性内能矩阵

\[
K/\pi^2=
\begin{bmatrix}
1&0&0&0&0\\
0&1/2&0&0&0\\
0&0&(3-\nu)/8&0&(1+\nu)/8\\
0&0&0&1/2&0\\
0&0&(1+\nu)/8&0&(3-\nu)/8
\end{bmatrix}.
\]

`nu=.18` 时特征值

```text
[.205,.5,.5,.5,1]
```

全部为正，且精确解

```text
r/M=[-.295,-.205,+.25,-.205,+.25]
```

逐项恢复经典 Airy/FvK 应力：

```text
sigma_x/(E eps0) = -M/4 cos2Y
sigma_y/(E eps0) = -D + M/2 sin^2X
tau_xy            = 0
```

所以：

```text
FIVE_TERM_SHAPE_SPACE = RETAIN
FIVE_TERM_ELASTIC_AIRY_LIMIT = PASS_EXACT
```

---

## 4. 找到第一个明确断点：19:12 已经拒绝 legacy N48 继续求五坐标 root

19:12 执行报告曾把五项基临时接入 legacy Case21 N48-C1 kernel。在历史 Case21 状态

```text
D=.8359179831666168
q=.0017897894751107222
M=.02869338081034484
r=r_Airy
```

得到

```text
Rhat_total=[+2.69233687,+.13819441,-.31339370,-15.52815375,+3.00791537]
```

5x5 diagnostic Jacobian 条件数约 `8.53e2`，Newton 增量为

```text
delta_r≈[-.01434,+.00398,-.48827,+.08584,+1.60404]
```

因此 19:12 已明确锁定：

```text
LEGACY_N48_AS_CURRENT_PRODUCTION = REJECTED
NEW_R_SOLVE = NOT_AUTHORIZED
RC1_NESTED_TARGET_FUNCTIONAL_EXECUTION = OPEN
NEW_Pu = NOT_RUN
```

这一步非常关键：当时并没有授权用 legacy N48 继续追五膜变量 root。

---

## 5. 真正的治理回归发生在 21:36

21:36 的 anti-loop governance 为停止 exact-backend 循环，直接重新激活：

```text
N48-C1/MM
+ five current membrane coordinates
+ solve Rm=0
+ Schur condensation
+ outer (D,q) Pu
```

但它没有新增任何新的 mechanics/fidelity gate 去推翻 19:12 的

```text
LEGACY_N48_AS_CURRENT_PRODUCTION = REJECTED
NEW_R_SOLVE = NOT_AUTHORIZED
```

也没有证明五项 current root 在强材料非线性下仍属于稳定、物理解支。

因此本轮确认：

```text
FIRST_GOVERNANCE_REGRESSION = 20260816_2136 anti-loop production pivot
```

其错误不是“停止 exact-backend”本身；错误是把“避免后端循环”误等价成“legacy N48 five-coordinate root 已自动获得物理生产资格”。

---

## 6. 第二个缺口：只检查 Rm=0 和 Krr 可逆，没有检查内部膜模态稳定性

19:12/21:36 的 Schur 公式使用

\[
K_{gg}^{cond}=K_{gg}-K_{gr}K_{rr}^{-1}K_{rg}.
\]

这个公式要作为稳定分支的静力凝聚使用，不能只要求 `Krr` 可逆；至少必须保证当前内部膜模态没有已经失稳。对具有非对称 current tangent 的实现，最低门禁应检查二阶增量功对应的对称部分

\[
\boxed{K_{rr}^{sym}=\frac12(K_{rr}+K_{rr}^T)}
\]

是否保持正定。

近期 continuation 没有这个门禁，因此求解器可以继续沿 `Rm=0` 的 saddle/unstable internal branch 前进，并把该 branch Schur-condense 成看似正常的外层 `(D,q)` 路径。

---

## 7. Airy-direction 投影证明 branch 是怎样跑偏的

定义 `Kbar=K/pi^2`，以及 K-内积投影系数

\[
\lambda_A=\frac{a^TK_{bar}r}{M\,a^TK_{bar}a},
\qquad a^TK_{bar}a=0.19155.
\]

并定义 K-正交剩余

\[
r_\perp=r-\lambda_A M a.
\]

### 低 q point1

```text
M=.00120418618
lambda_A=1.13729089
||r_perp||K/||r||K=.1624
```

### 低 q point2

```text
M=.00245559535
lambda_A=1.09794176
||r_perp||K/||r||K=.2198
```

它们仍大致沿正 Airy 方向。

### 后来错误发布的 Case21 320.75 kN 状态

```text
M=.02957505323
lambda_A=-1.14600789
||r_perp||K/||r||K=.97188
```

也就是说，该状态的五坐标不仅不再是“Airy 正向重分布的非线性修正”，而且 K-投影主方向已经翻成负号，约 97% 的幅值落在 Airy 方向之外。

这和 `Case21 M/4D~0.86%` 的“小扰动”历史尺度完全不相称。

---

## 8. direct frozen-R10 独立 oracle：不是单纯 N48 数值误差

为区分“legacy N48 错”与“五坐标 nonlinear equilibrium 本身进入不稳定支”，本轮用 frozen direct R10 做了 audit-only 高阶 Gauss-Legendre oracle。该 oracle 不进入正式零积分生产理论，只用于判断残量和 tangent 符号。

在同一历史 Case21 `D,q` 下：

### 8.1 只允许 Airy 一个耦合方向

令

\[
r=\lambda M a.
\]

沿该方向的 generalized residual

\[
R_A=a^T R_m
\]

有一个正根

```text
lambda=0.06773338661
```

并且

```text
dR_A/dlambda=+4.13439792
```

所以 direct R10 并不要求把 Airy 方向反号；正向膜重分布仍可成立。

但是该 scalar root 上其余正交膜残量很大：

```text
Rm=[+6.54350,+1.56063,-1.72449,-20.97978,-6.47789]
||Rm||2=23.02913
```

因此“只保留一个 Airy scalar amplitude”不足以作为最终 nonlinear closure。

### 8.2 放开全部五坐标

在同一 `D,q` 下 direct R10 五残量确实可以求到 root：

```text
r≈[-.01530,-.00518,-.03837,+.06693,+.16261]
```

但其 K-投影：

```text
lambda_A≈2.49499
||r_perp||K/||r||K≈.95204
```

且 direct-R10 finite-difference internal tangent 的对称部分特征值约为

```text
[-238.65,-28.05,+281.46,+492.27,+733.27]
```

存在两个明确负方向；原始 Jacobian 本身也有一个负实特征值约

```text
-14.15
```

所以这个 `Rm=0` root 是内部膜模态不稳定/鞍点型状态，不能作为稳定 Schur-condensation state。

作为对照，低 q point1/point2 的 direct-R10 `Krr_sym` 特征值全部为正：

```text
point1 min eig ≈ +91.24
point2 min eig ≈ +87.79
```

这解释了为什么 continuation 最初看起来完全正常，而到后面才逐渐偏离物理主支。

---

## 9. 本轮恢复后的 current-material 膜力闭合资格

因此不能简单地说“五项基错了”，也不能简单退回“固定 Airy 系数”。正确结论是：

```text
FIVE_TERM_BASIS = RETAIN
FULL_Rm=0_EQUILIBRIUM = NECESSARY_BUT_NOT_SUFFICIENT
Krr_INVERTIBLE_ONLY = INSUFFICIENT
INTERNAL_MEMBRANE_STABILITY_GATE = MANDATORY
SCHUR_CONDENSATION_REQUIRES_STABLE_INTERNAL_BLOCK = MANDATORY
```

正式静力凝聚必须同时满足：

\[
\boxed{R_m=0}
\]

以及

\[
\boxed{\lambda_{min}(K_{rr}^{sym})>0}
\]

（或其与最终一致 tangent/二阶功严格等价的稳定性判据）。

一旦该内部块首次失稳：

```text
DO_NOT_CONTINUE_TO_ANOTHER_Rm_ROOT
DO_NOT_SCHUR_CONDENSE_THE_UNSTABLE_ROOT
TREAT_AS_INTERNAL_MEMBRANE_STABILITY_EVENT
```

并应回到完整 `(D,q,r)` tangent / mixed membrane equilibrium 判断，而不是把不稳定内部模态消掉。

---

## 10. Z6 还多一个独立问题

Z6 00:16 boundary gate 已确认实际 mixed in-plane boundary：loaded ends 有 `ux=0`，lateral sides in-plane free。

简单 free-Poisson five-term `u0,u20,u22` 并不完整满足该 loaded-edge essential condition；00:16 已要求 biharmonic boundary correction。

因此近期 `43.762840 MN` direct-R10 five-free-coordinate Z6 诊断同时存在：

1. 非正式空间 Gauss oracle 身份；
2. 采用了不完整的 Z6 in-plane boundary class；
3. 未执行 internal membrane stability gate。

它不能代表正确 Z6 膜效应。

---

## 11. 本轮门禁结果

```text
1848_CLASSICAL_MEMBRANE_DELTA = RETAIN
1912_FIVE_TERM_ELASTIC_LIMIT = RETAIN / PASS_EXACT
1912_LEGACY_N48_FAIL_FAST = RESTORED AS CONTROLLING EVIDENCE
2136_N48_FIVE_COORDINATE_PRODUCTION_OVERRIDE = RETRACTED
MISSING_INTERNAL_Krr_STABILITY_GATE = IDENTIFIED
CASE21_320P75 = REMAINS RETRACTED / UNSTABLE-RELAXATION DIAGNOSTIC
Z6_43P76 = REMAINS RETRACTED / BOUNDARY+STABILITY DIAGNOSTIC
SCALAR_AIRY_ONLY_CURRENT_CLOSURE = INSUFFICIENT
OVERALL_GATE = PASS_TO_CORRECTED_STABILITY-CONTROLLED MEMBRANE CLOSURE
```

## 12. 唯一下一门禁

`STABLE_CURRENT_MEMBRANE_CONDENSATION_AND_MIXED_EVENT_GATE`

执行内容限定为：

1. 保留五项 leading subspace；
2. current `Rm=0` 解必须同时通过 `Krr_sym>0`；
3. 只在内部块稳定时允许 Schur condensation；
4. 第一次 `Krr` 内部稳定丧失必须作为显式结构事件进入 full tangent，不得继续松弛；
5. Case21 先定位该 internal-stability event 与旧 368.189 kN support peak 的先后关系；
6. Z6 必须先使用其 mixed-boundary admissible Airy/biharmonic family，不能直接复用 Case21 free-Poisson five-term field；
7. 不开发新积分后端，不调 R10，不用试验 Pu 选事件。
