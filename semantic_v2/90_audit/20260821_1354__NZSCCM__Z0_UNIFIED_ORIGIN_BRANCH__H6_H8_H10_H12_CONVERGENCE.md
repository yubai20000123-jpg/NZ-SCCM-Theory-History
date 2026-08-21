# NZ-SCCM — Z0 H6/H8/H10/H12 unified origin-connected full-panel convergence

时间：2026-08-21 13:54 +08:00
状态：`CURRENT_UNIFIED_BRANCH_CONVERGENCE_LEDGER`
材料：`NC-M6 FROZEN`

## 1. 本次清理的唯一目的

把此前 H6/H8/H10 中不同 continuation 口径彻底统一。所有阶次现在严格使用同一规则：

1. 从 `D=q=eta=all Ritz amplitudes=0` 的零荷载状态出发；
2. 用连续增量建立 origin-connected equilibrium branch；
3. 在接近极限处统一使用 pseudo-arclength continuation，不用“高荷载最近根”代替；
4. representative sector 的第一可达荷载极值作为候选控制点；
5. 在同一状态检查 full-panel complementary tangent `J_perp,N`，若 complementary rank loss 更早则由其控制；
6. 最终得到 full-panel first control point `Pu,N`；
7. 用预冻结的 consecutive-order gate 比较 N 与 N+1。

本次不使用 FE/试验荷载选根、选阶或修改门槛。

## 2. 为什么旧的 30+ MN Z0 峰值不再是 Pu

此前 H6/H8 曾沿同一或相关 equilibrium manifold 继续追踪到约 30–33 MN 的后续高荷载区，并把后续局部峰值写作 `Pu`。统一 branch/control 定义后发现：在从零状态出发的同一条 representative equilibrium path 上，更早已经存在第一可达荷载极值。因此后续高荷载峰不再具备“first control point”身份。

这不是修改物理理论，而是把所有阶次统一到同一个极限承载力定义：

`Pu = first reachable full-panel control event along the origin-connected path`。

所以旧 Z0 30+ MN H6/H8 peak ledgers 仅保留为历史 continuation 轨迹，不再用于 consecutive-order production convergence。

## 3. common 40x40x20 audit localizer 的统一结果

以下 direct-current quadrature 仅用于 AUDIT/DECIMAL LOCALIZER；正式理论空间积分身份仍为零。

| Order | N | Representative amplitudes | D at first control | q | eta | Pu (MN) |
|---|---:|---:|---:|---:|---:|---:|
| H6 | 3 | 24 | 0.370474418 | 0.000752739 | 0.075455619 | 18.948987805 |
| H8 | 4 | 40 | 0.359720801 | 0.000737096 | 0.073177762 | 18.633192591 |
| H10 | 5 | 60 | 0.353071904 | 0.000727954 | 0.071773288 | 18.425511505 |
| H12 | 6 | 84 | 0.349211066* | 0.000722842* | 0.070957879* | 18.296452361* |

`*` H12 最终 decimal localizer 使用 44x44x22；40x40x20 给出 Pu=18.294951623 MN，40→44 变化约 0.0082%，满足 <0.05% 的 marginal audit-localizer criterion。

## 4. audit-localizer independence

### H6
- 28x28x14: Pu ≈ 18.94793 MN
- 32x32x16: Pu ≈ 18.95066 MN
- 40x40x20: Pu ≈ 18.94899 MN
- final refinement change comfortably <0.05%

### H8
- 28x28x14: Pu ≈ 18.63031 MN
- 32x32x16: Pu ≈ 18.63419 MN
- 40x40x20: Pu ≈ 18.63319 MN
- final refinement change comfortably <0.05%

### H10
- 28x28x14: Pu ≈ 18.42497 MN
- 32x32x16: Pu ≈ 18.42272 MN
- 40x40x20: Pu ≈ 18.42551 MN
- final refinement change comfortably <0.05%

### H12
- 28x28x14: Pu ≈ 18.29702 MN
- 32x32x16: Pu ≈ 18.29251 MN
- 36x36x18: Pu ≈ 18.30234 MN
- 40x40x20: Pu ≈ 18.29495 MN
- 44x44x22: Pu ≈ 18.29645 MN
- 40→44 marginal change ≈ 0.0082% < 0.05%

## 5. full-panel complementary-sector control audit

Full-panel mother space is the already locked `F_N`; representative sector is `r=0 mod 4`, all other residue classes are complementary sectors. `J_perp,N` is assembled from the same source-consistent, unsymmetrized current tangent.

At each representative first peak, complementary tangent remains nonsingular.

Consistent normalized singular diagnostics near the peak:

- H6, 40x40x20: `sigma_min(J_perp) ≈ 21.65`, determinant sign positive.
- H8, 40x40x20: `sigma_min(J_perp) ≈ 13.42`, determinant sign positive.
- H10, 40x40x20: `sigma_min(J_perp) ≈ 8.71`, determinant sign positive. Independent earlier dedicated H10 audit also showed the first complementary rank loss occurs only after the representative load maximum on the descending branch.
- H12, 44x44x22: `sigma_min(J_perp) ≈ 2.90`, determinant sign positive at the representative peak. At 40x40x20 the determinant sign flips only immediately after the peak on the descending branch, so complementary instability again does not precede the representative first control point.

Therefore for H6/H8/H10/H12:

`FULL_PANEL_FIRST_CONTROL = REPRESENTATIVE_FIRST_LOAD_MAXIMUM`。

No omitted complementary halfwave-difference mode controls earlier in these four orders.

## 6. consecutive-order convergence metrics

Frozen gates:

- delta_P <= 0.5%
- delta_D <= 0.5%
- delta_w <= 1.0%
- delta_epsilon <= 2.0%

Definitions:

`delta_P = |Pu,N+1 - Pu,N| / |Pu,N+1|`.

`delta_D = |D_N+1-D_N|/|D_N+1|`.

`delta_w` uses total out-of-plane amplitude `q0+q`.

`delta_epsilon` uses the representative midsurface membrane-tensor L2 norm with engineering shear weight 1/2:

`||e||^2 = integral [ex^2 + ey^2 + 0.5 gamma^2] dA`.

### H6 -> H8
- delta_P ≈ 1.6948%  FAIL
- delta_D ≈ 2.9894%  FAIL
- delta_w ≈ 0.3302%  PASS
- delta_epsilon ≈ 4.1584%  FAIL

Decision: `H6_PRODUCTION_FREEZE = NO`.

### H8 -> H10
- delta_P ≈ 1.1271%  FAIL
- delta_D ≈ 1.8832%  FAIL
- delta_w ≈ 0.1933%  PASS
- delta_epsilon ≈ 2.6319%  FAIL

Decision: `H8_PRODUCTION_FREEZE = NO`.

### H10 -> H12
Using H10 40x40x20 and refined H12 44x44x22:
- delta_P ≈ 0.7054%  FAIL
- delta_D ≈ 1.1056%  FAIL
- delta_w ≈ 0.1082%  PASS
- delta_epsilon ≈ 1.4907%  PASS

Decision: `H10_PRODUCTION_FREEZE = NO`.

H12 becomes the next minimum candidate; `H12_PRODUCTION_FREEZE = NOT_AUTHORIZED` until H12->H14 is evaluated under a pre-frozen gate.

## 7. convergence pattern after cleanup

The cleaned first-control loads are monotone:

`18.94899 -> 18.63319 -> 18.42551 -> 18.29645 MN`

and consecutive load changes decrease:

`1.6948% -> 1.1271% -> 0.7054%`.

Likewise deformation/field corrections generally decrease. This is now a normal finite-N Ritz convergence sequence; no separate theoretical layer is introduced.

## 8. formal status

- `RITZ_THEORY_ENDPOINT = LOCKED`
- `FULL_PANEL_SPACE = F_N`
- `IDEAL_W_MODE = TWO_COMPLETE_HALFWAVES`
- `NC_M6 = FROZEN`
- `M7 = PROHIBITED`
- `H6 = REJECTED`
- `H8 = REJECTED`
- `H10 = REJECTED`
- `H12 = NEXT_MINIMUM_CANDIDATE`
- `H12_PRODUCTION_FREEZE = NOT_AUTHORIZED`

No FE/test load was used to obtain these decisions.