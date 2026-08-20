# TREE DELTA — 2026-08-20 14:32

新增当前前沿文件：

- `semantic_v2/20_theory/20260820_1432__NZSCCM__NC_M1_NINE_GRID_CONSTITUTIVE__AUDIT_AND_REJECTION.md`

当前状态修正：

- `NC-M1` 九宫格材料候选：`REJECTED_DIAGNOSTIC_CANDIDATE`。
- 撤回原因：虽然曲线形式直观，但 compression / tension / TC 均增加人为分段与阈值；CC 又引入 `min/max` 比值，未降低真正 current-operator / integration-kernel complexity。
- 九宫格主应变分类框架保留。
- 后续材料简化指标从“曲线看起来简单”改为 operator complexity：branch count、threshold count、min/max/abs/positive-part、根号/主方向、有理分母、额外状态、代入连续应变后的积分复杂度。
- 不再以 Nguyen 原式为唯一拟合目标；允许选择其他经典或新构造的低复杂度关系。
- 603 kN 的 full-domain CC+TC+TT 直接叠加诊断继续保持撤销状态。
- GitHub 治理更新：实质理论/计算/否决/当前状态检查点默认在本轮直接同步，不再等待用户另行确认。
