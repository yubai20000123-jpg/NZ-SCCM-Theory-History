# NZ-SCCM — FULL AR2 complementary full-panel tangent gate at H10

时间：2026-08-21 13:35 +08:00
状态：`COMPLEMENTARY_GATE_PASS_AT_H10_FIRST_CONTROL_POINT`
材料：`NC-M6 FROZEN`

## 1. 目的

在已证明的理想 `a=2b` 两完整半波代表子空间基础上，检查 full-panel boundary-compatible in-plane Ritz space 中未被单代表半波显式求解的纵向 Fourier sectors，是否会在 H10 representative origin-connected branch 的第一控制点之前先发生 rank loss。

本门禁只检查结构空间完整性；不使用 FE/试验荷载，不修改 NC-M6，不改变既有 H10 equilibrium branch。

## 2. full-panel completion

全板长度 `A=2 ell=2b`，定义

`X = pi x / b`, `Ybar = pi y / A`。

固定理想面外两半波：

`w = b(q0+q) sin(X) sin(2 Ybar)`。

在面内位移上，对当前 representative H_{2N} 的物理最高纵向波数做 full-panel completion。H10 对应 N=5，取纵向 full-panel Fourier index `r=0..4N=20`：

u = eps0 [ eta x + sum_{m=1..N} sum_{r=0..4N} b/(2m pi) a_{m r} sin(2mX) cos(r Ybar) ],

v = eps0 [ -D y + sum_{m=0..N} sum_{r=1..4N} A/(r pi) b_{m r} cos(2mX) sin(r Ybar) ].

其 normalized strain basis 为：

u-mode:
- ex = cos(2mX) cos(rYbar)
- ey = 0
- gamma = - (b/A) r/(2m) sin(2mX) sin(rYbar)

v-mode:
- ex = 0
- ey = cos(2mX) cos(rYbar)
- gamma = - 2m/[r(b/A)] sin(2mX) sin(rYbar)

当前 representative subspace 恰对应 `r = 0 mod 4`。其余 `r=1,2,3 mod 4` 构成 full-panel complementary space。

H10 维数：
- full-panel in-plane Ritz amplitudes = 225
- representative amplitudes = 60
- complementary amplitudes = 165

## 3. exact sector structure

Representative base state 的厚度积分 stress/tangent coefficients 沿 y 具有半波重复周期 ell，因此 full-panel Fourier projection 按 `r mod 4` 分 sector。正式连续积分下：

- representative residual block = r=0 mod 4;
- complementary residuals = 0 at the representative equilibrium state;
- representative/complementary cross blocks vanish;
- complementary tangent is the direct block of the full source-consistent Jacobian.

不强迫 NC-M6 tangent major symmetry；稳定门禁采用 rank/singular-value/determinant ordering，而不是人为对称化特征值。

## 4. audit evaluator

使用 frozen direct-current NC-M6 + symmetric Z0 multiphase section：

- concrete core: 0.98 tc
- equal upper/lower steel faces
- distributed longitudinal web phase
- no material modification

full-panel quadrature只作 AUDIT/DECIMAL LOCALIZER，不获得正式理论身份。

为了避免高频 basis alias，complementary audit 使用高于旧 28x28x14 的局部分辨率，并做 40/48/52/56 in-plane localizer ordering check。

## 5. H10 origin-connected representative first control point

32x32x16 representative pseudo-arclength branch：

- D=0.35266510, P=18.41539147 MN
- D=0.35301690, P=18.42296971 MN
- D=0.35309582, P=18.41991945 MN

所以 first load maximum 位于 step 7 与 step 8 之间，约 `P_u,H10 ~= 18.423 MN`。该 branch 从零荷载连续追踪，不是高荷载最近根。

## 6. J_perp at and around the representative peak

在 D=0.35301690、P=18.42296971 MN 这一峰值邻近点：

40x20 localizer:
- sigma_min(J_perp) ~= 8.60

48x24:
- sigma_min(J_perp) ~= 8.34

52x26:
- sigma_min(J_perp) ~= 8.56

56x28:
- sigma_min(J_perp) ~= 8.68

所有 localizer 均为 strictly nonsingular；determinant sign 尚未改变。

## 7. first complementary rank loss ordering

继续沿同一 H10 branch 进入 post-peak 后，J_perp 才发生首次 determinant sign change / real eigenvalue crossing。

采用相同 pseudo-arclength path parameter，在 peak 后 step8 -> step9 区间做 localizer refinement，得到 complementary rank-loss load 约：

| localizer | estimated P at J_perp rank loss |
|---|---:|
| 40x20 | 18.41684 MN |
| 48x24 | 18.41585 MN |
| 52x26 | 18.41613 MN |
| 56x28 | 18.41581 MN |

40 -> 56 spread ~0.00103 MN，约 0.0056%，小于 0.05% audit-localizer criterion。

关键不是该 post-peak load 比 peak 数值低，而是 path ordering：

`representative load maximum -> descending branch -> complementary rank loss`。

因此 complementary instability 不会抢先控制 H10 的第一极限承载力。

## 8. 裁决

`FULL_AR2_COMPLEMENTARY_HALFWAVE_DIFFERENCE_TANGENT_GATE_AT_H10 = PASS`

`ONE_REPRESENTATIVE_HALFWAVE_IS_SUFFICIENT_UP_TO_H10_FIRST_CONTROL_POINT = YES`

此裁决只说明：对当前理想两半波、对称截面、H10 截断，full-panel omitted membrane sectors 不会在 representative first control point 前先失稳。

它不把 representative subspace 宣称为完整 full-panel function space；完整空间定义仍保留，production 可通过 sector decomposition 低成本审计互补 block。

## 9. 对后续的固定规则

此后不再新增新的“空间层级”。Ritz 空间结构一次固定为：

`FULL boundary-compatible Ritz space -> exact Fourier residue sectors -> representative sector + complementary tangent sectors -> N truncation convergence`。

每个候选 N 只需：
1. 求 representative nonlinear branch；
2. 同源组装 J_perp；
3. 比较 first representative control point 与 first complementary rank loss 的 path ordering；
4. 在同一 full-space definition 下做 N -> N+1 收敛。

不得再通过临时修改 halfwave count、空间基、材料或误差门槛处理结果。
