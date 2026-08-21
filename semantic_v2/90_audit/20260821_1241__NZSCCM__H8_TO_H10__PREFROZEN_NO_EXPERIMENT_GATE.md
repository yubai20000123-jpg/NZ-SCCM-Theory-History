# NZ-SCCM — H8→H10 无试验值连续阶收敛门禁（结果前冻结）

时间：2026-08-21 12:41 +08:00

## 1. 理论边界继续冻结

- NC-M6：FROZEN；禁止 M7、重新拟合或经验系数。
- ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE。
- H_{2N} 为同一 nested boundary-compatible Ritz/Galerkin 母空间；H8=N=4，H10=N=5。
- 正式理论空间 sampling/quadrature/material points = 0；高阶 direct-current quadrature 只允许作为 AUDIT/DECIMAL LOCALIZER。
- 不允许试验 failure load、Zhou/Winter comparator 参与求根、选支、阶次选择或容差设置。

## 2. H8 production acceptance gate

对同一物理平衡支的 H8 与 H10 极限状态，定义连续阶差异：

- δP = |P10-P8|/|P10|
- δD = |D10-D8|/|D10|
- δw：峰值新增/总面外幅值的连续阶相对差
- δε：同一连续域内归一化膜应变场差异的预冻结 field metric

门槛保持与 H4→H6、H6→H8 完全相同：

- δP ≤ 0.5%
- δD ≤ 0.5%
- δw ≤ 1.0%
- δε ≤ 2.0%
- same origin-connected physical branch
- audit-localizer marginal peak-load refinement < 0.05%

任何决定性单项失败即可判 `H8_GLOBAL_PRODUCTION_FREEZE=NO`，并允许 fail-fast，不需要为了改变已经不可逆的裁决继续全部样本。

若要判 `H8_GLOBAL_PRODUCTION_FREEZE=YES`，则必须完成当前要求的全部结构族验证；不得只凭单个代表算例通过。

## 3. 验证顺序

鉴于 H6→H8 已由 Z0 明确 field FAIL，而 Swartz24 全部通过，H8→H10 按成本最小且不降低严格性的顺序执行：

1. 先计算 Z0 的真实 H8→H10；
2. 若 Z0 决定性失败：H8 全局冻结立即 NO，停止无意义的 Swartz24 H10 全批；下一候选 H10，且必须在任何 H12 结果出现以前预冻结 H10→H12 门禁；
3. 若 Z0 通过：继续 Z1–Z5；
4. 若 Z0–Z5 全部通过：再完成 Swartz24 H8→H10 全批，才能考虑 H8 global production freeze。

## 4. tail/bordered diagnostics

可以并行记录 H10-only shell residual、conditioned tail predictor、bordered/null-space predictor和 coefficient-ring norms；这些只作诊断，不能在本 H8→H10 validation pair 中替代真实 H10 解，也不能事后改变以上门槛。
