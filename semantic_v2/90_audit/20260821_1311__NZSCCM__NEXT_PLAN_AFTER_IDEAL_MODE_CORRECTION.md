# NZ-SCCM — 理想模态修正后的下一步规划

时间：2026-08-21 13:18 +08:00
状态：`CURRENT_NEXT_PLAN_AFTER_STEP1`

## 总体目标

在不改变 NC-M6、不引入 M7、不使用试验/FE荷载选阶的前提下，先保证所有连续阶比较都发生在同一个理想全板两半波问题内，再继续 H2N 截断误差收敛；最后才进入 Z0–Z5 确定性 FE 误差和 Swartz24 物理试验误差分析。

## STEP 0 — 继续暂停机械升阶

H10→H12 预冻结门槛保留；已执行 H12 初步数值只保留工作痕迹，不升级为 production 裁决。在 full-panel complementary-mode gate 完成以前，不继续 H14。

## STEP 1 — FULL AR2 TWO-HALFWAVE ↔ ONE REPRESENTATIVE HALFWAVE

状态：`COMPLETED_WITH_CONDITIONAL_PASS`。

完整证明见：

`20260821_1318__NZSCCM__FULL_AR2_TWO_HALFWAVE_TO_ONE_REPRESENTATIVE_HALFWAVE__EQUIVALENCE_AUDIT.md`

已经严格证明：

- 全板 `a=2ell` 的理想 `m*=2` 面外场在两个半波间反号复制；
- H2N `u,v` 可以连续延拓；
- von-Karman 膜应变逐半波重复；
- bending strain 的半波反号严格等价于 `z->-z`；
- 当前 Swartz RC 截面与 Z steel-shell/core/web 组装满足中面对称；
- 不需要修改 NC-M6，也不要求 M6 tangent major symmetry；
- 在 repeated two-halfwave subspace 内：`R_full=2R_half`、`J_full=2J_half`、`P_full=P_half`。

因此：

`REPEATED_TWO_HALFWAVE_SUBSPACE_EQUIVALENCE = EXACT_PASS`。

但 full `a=2b` admissible membrane space 还包含 longitudinal harmonics 不属于 representative `r=4n` family；这些可以描述两个半波之间的膜内差异扰动。因此：

`UNRESTRICTED_FULL_PANEL_EQUIVALENCE = NOT_YET_PROVED`。

代表半波是全板方程的严格 invariant equilibrium subspace，但还不能自动保证它给出 unrestricted full-panel 的 first instability / ultimate state。

## STEP 1B — 当前唯一下一任务：互补半波差异模态 tangent gate

任务名：

`FULL_AR2_COMPLEMENTARY_HALFWAVE_DIFFERENCE_TANGENT_GATE`

不先建立第二套完整 nonlinear full-panel solver。先在 full `a=2b` 域定义代表 family 的互补 admissible membrane sector `V_perp`，然后沿每个 representative origin-connected equilibrium state 计算 source-consistent complementary tangent block：

`J_perp(D,q,eta,c)`。

必须检查：

1. representative state 嵌入 full panel 后，所有 complementary residual 为零；
2. representative/complementary tangent cross-block 按周期/正交性为零；
3. `J_perp` 在 representative 第一可达极限以前是否先失去 rank；
4. 不强迫 tangent 对称；判据使用 source-consistent rank/singular condition；
5. 不使用 Z FE 或 Swartz 试验荷载决定 gate。

判定：

- 若 `J_perp` 到 representative first limit 始终 regular：`ONE_REPRESENTATIVE_HALFWAVE_GLOBAL_MODE_GATE = PASS`，进入 STEP 2；
- 若 `J_perp` 更早 singular：单代表半波 production identity FAIL，必须激活 full two-halfwave complementary generalized coordinates，并以较早 full-panel instability 为控制状态。

## STEP 2 — H6/H8/H10 模态/支路严格嵌套

只有 STEP1B PASS 后执行：

- H6 ⊂ H8 ⊂ H10 严格代数嵌套；
- 同一 q0、同一 ideal full-panel two-halfwave sector；
- H8 嵌入 H10 后旧坐标 residual 与 H8 解一致，新坐标 residual 仅为 tail forcing；
- origin-connected continuation；
- fold 使用同一 pseudo-arclength/KKT 极限定义。

## STEP 3 — Z0 H8→H10 巨跳复核

STEP1B 与 STEP2 均 PASS 后，重新判断 representative-sector 的约 `31+ MN -> 18.42 MN`：

- H8/H10 first reachable limit；
- bordered tail forcing；
- H10 ring strain-weighted norm；
- localization width / high-frequency energy。

若巨跳仍复现且 localizer independent，则才恢复 H8 production rejection；若消失，则旧 rejection 被 supersede；若持续向窄区集中，则进入 softening well-posedness 诊断。

## STEP 4 — 恢复连续阶收敛

若 H10 仍是下一候选，完成 H10→H12。门槛保持：

- delta_P ≤ 0.5%
- delta_D ≤ 0.5%
- delta_w ≤ 1.0%
- delta_epsilon ≤ 2.0%
- same ideal mode / same origin branch
- audit-localizer marginal peak-load change <0.05%

任何 H14 结果以前必须先冻结 H12→H14 gate。

## STEP 5 — Z0–Z5 理想确定性 FE 基准误差

仅在结构阶数冻结后打开 FE 结果。逐板报告 signed error、systematic bias、detrended residual scatter 及物理参数趋势。Z 系列不得用 specimen randomness 解释无规律散差。

## STEP 6 — Swartz24 物理试验误差

Case1–24 全部按理想 `a/b=2` 两完整半波理论计算。实测半波偏离只作为后验 `SPECIMEN_REALIZATION_DEVIATION` 标签解释试验随机性，不用于改理论模态、删样、选阶或调材料。

## 当前唯一下一任务

`STEP1B: FULL_AR2_COMPLEMENTARY_HALFWAVE_DIFFERENCE_TANGENT_GATE`
