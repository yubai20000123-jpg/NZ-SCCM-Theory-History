# START HERE

## 先读 CURRENT_STATE，不按 legacy 文件树/文件名猜身份

本仓库存在历史/当前工件混放和旧命名遗留。目录名、文件名及其中的 `current`、`fresh`、`production`、`PASS`、日期等只具有**定位作用**，不自动决定文件是否当前有效。

新对话或中断恢复时，按下面顺序读取：

1. `current/CURRENT_STATE.md`
2. `semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`
3. `semantic_v2/20_theory/20260821_2205__NZSCCM__SWARTZ_SOURCE_RATIO_AND_MULTIAXIAL_CAPACITY_ADDENDUM.md`
4. `current/diagnostics/NZ_SCCM_SWARTZ24_SOURCE_CORRECTION_PAIR_MATRIX_TC_CAPACITY_AUDIT_20260821.md`
5. `current/results/NZ_SCCM_STEEL_SHELL_UHPC_T120_T360_BH005_BH050_CURRENT_SUMMARY_20260821.md`
6. `semantic_v2/00_index/20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`
7. `semantic_v2/00_index/20260813_1328__NZSCCM__REPOSITORY__ARTIFACT_SUPERSESSION__SUPERSESSION_MAP.csv`
8. `governance/SOURCE_OF_TRUTH_POLICY.md`
9. `governance/RECOVERY_PROTOCOL.md`
10. 根据当前任务回到原始来源/legacy正文，并以**正文内容 + supersession/revocation 链**判定身份。

```text
PATH_NAME_ONLY_CLASSIFICATION = PROHIBITED
LEGACY_CURRENT_DIRECTORY_SEMANTIC_PURITY = FALSE
CONTENT_AUDIT_BEFORE_USE = REQUIRED
```

## 2026-08-21 当前主线

当前主线已经从 R15 / high-special-function exact-integral 分支转为：

\[
\boxed{\text{Marguerre–Airy显式后屈曲}+\text{显式N-M截面容量}+\text{有限代数最小正根}}
\]

```text
PATH_TRACKING = PROHIBITED_NOT_NEEDED
RITZ_ORDER = NONE
FORMAL_SPATIAL_QUADRATURE = 0
EXPERIMENT_IN_ROOT_SELECTION = 0
```

### Swartz mandatory correction

Swartz 表中钢筋率应为**每一方向、跨全部层合计**：

\[
\boxed{\rho_x=\rho_y=\rho_{table}}
\]

旧 `rho_table/2` 解释已 superseded。

用户已明确：不得为了 Swartz 不统一的实验起屈荷载修改 `D/Pcr/Ppb`。Swartz Pu 误差诊断先使用参数相同/高度接近的可信试件对，不先对24块整体拟合。

### Steel-shell UHPC mandatory correction

`20260821_1824__...T120_T360.md` 中 T120/T360 的无内部纵向腹板结果仅作历史 provenance。当前 web-corrected 工作值和 BH005–BH050 第一版结果以：

`current/results/NZ_SCCM_STEEL_SHELL_UHPC_T120_T360_BH005_BH050_CURRENT_SUMMARY_20260821.md`

为准。

## 来源与历史

- 原始 PDF/正式来源 > 有 provenance 的有效摘录 > 历史全文镜像 > 项目解释 > 总结。
- 原始用户—助手对话/原始执行工件 > recovery summary。
- 文件名和所在目录不属于 source-of-truth 层级。
- 结构 Pu 不得用于反标材料参数。
- Swartz TC 数值校正当前仍受 `ft` 未 source-closed 限制；临时 `ft=0.10fc` 仅为 diagnostic。
- pre-clean 资产仍由 `history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md` 定位。
