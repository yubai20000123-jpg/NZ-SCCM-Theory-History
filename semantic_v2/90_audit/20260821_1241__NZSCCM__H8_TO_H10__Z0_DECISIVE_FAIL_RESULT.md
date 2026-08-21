# NZ-SCCM — H8→H10 Z0 已执行结果（理想两半波修正后暂定状态）

时间：2026-08-21
当前状态：`EXECUTED_WARNING_RESULT_PENDING_IDEAL_MODE_EQUIVALENCE_AUDIT`

> 重要修正：本文件原题为“Z0 决定性失败结果”，并据此直接写出 `H8_GLOBAL_PRODUCTION_FREEZE = NO`。2026-08-21 13:11 用户进一步锁定：所有 `a/b=2` 理想板的理论基准必须是全板两个完整半波；Z0–Z5 为理想化 FE 基准。故在证明 `FULL_AR2_TWO_HALFWAVE ↔ ONE_REPRESENTATIVE_HALFWAVE` 对 H2N 的 u/v/w、材料积分、边界与残量完全等价以前，本文件中的 31+ MN→18.42 MN 数值跳变只保留为已执行警告证据，不再具有最终 production rejection 身份。

新的治理入口：

- `20260821_1311__NZSCCM__IDEAL_MODE_AND_VALIDATION_CLASSIFICATION__CORRECTED.md`
- `20260821_1311__NZSCCM__NEXT_PLAN_AFTER_IDEAL_MODE_CORRECTION.md`

## 1. 原执行门槛

计算使用已经在 H10 结果出现以前冻结的 H8→H10 gate：

- δP ≤ 0.5%
- δD ≤ 0.5%
- δw ≤ 1.0%
- δε ≤ 2.0%
- same origin-connected branch
- audit-localizer marginal peak-load refinement < 0.05%

NC-M6、钢面、web、多相组装和当时的 H2N 母空间均未修改。direct-current quadrature 仅为 AUDIT/DECIMAL LOCALIZER。

## 2. 已执行支路追踪

当时 H10 从 `D=0, q=0, eta=0, all H10 membrane coefficients=0` 开始连续追踪 origin-connected branch；随后使用伪弧长穿过 D-fold。

## 3. 已执行 H10 数值

24×24×12 localizer：第一荷载极值约 18.44 MN。

28×28×14 localizer：局部峰值约 18.42567 MN。

32×32×16 localizer：

- D≈0.3527–0.3531
- P≈18.415–18.423 MN
- 局部峰值估计 `P_u,H10 ≈ 18.42321 MN`

28→32 变化约 0.0133% < 0.05%。

## 4. 已执行 H8 数值

32×32×16 下，当时使用的 H8 origin-connected continuation 在

- D≈0.880338
- P_H8≈31.318110 MN

时仍在上升。因此在当时的代表半波实现下，H8 与 H10 产生极大差异。

## 5. 修正后的身份

现在不再正式写：

`H8_REJECTION = DECISIVE_BY_Z0_DELTA_P`。

当前只能写：

`H8_TO_H10_Z0_LARGE_JUMP = EXECUTED_AND_NUMERICALLY_LOCALIZER_STABLE`

`H8_PRODUCTION_DECISION = SUSPENDED_PENDING_FULL_AR2_TWO_HALFWAVE_EQUIVALENCE`

若等价性审计 PASS，且在同一理想两半波扇区重新复核后仍得到该巨跳，则恢复 H8 rejection；若等价性 FAIL 或巨跳消失，则旧 rejection 正式 supersede。

## 6. 当前唯一下一动作

停止机械推进 H12/H14 production 裁决，先执行：

`FULL_AR2_TWO_HALFWAVE_TO_ONE_REPRESENTATIVE_HALFWAVE_EQUIVALENCE_AUDIT`。
