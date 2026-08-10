# HISTORY

这里保存已经发生过、但**不能自动视为当前有效理论**的路线、工件、回滚和来源重构。

## 目录

- `NZ_SCCM/`：D/G/R 系列、moment-first、direct-analytic、nested-D15、material-recovery 等历史路线。
- `Case21/`：Case21 旧 route/history。
- `UCFT/`：Layer-0、Path-A、v5 等前期路线。
- `materials/`：历史材料 baseline/operator（例如 UHPC-C0）。
- `raw/`：原始历史文本/工程原件镜像。
- `recovery/`：TURN 0001–0148、G15、R04/R05 等恢复 locator。
- `ledgers/`：历史组件/决策台账。

## 规则

看到 PASS/HOLD/READY 等历史标签时，先检查它所属阶段和 supersession 边界。旧 PASS 不覆盖 `current/CURRENT_STATE.md`。

历史追溯优先：原始 user-assistant dialogue / 原始执行工件 > machine audit / ledger > handoff / summary。
