# START HERE

## 先读 semantic_v2，不按 legacy 文件树/文件名猜身份

本仓库存在历史/当前工件混放和旧命名遗留。目录名、文件名及其中的 `current`、`fresh`、`production`、`PASS`、日期等只具有**定位作用**，不自动决定文件是否当前有效。

新的首选入口已经重建为：

`semantic_v2/00_index/README.md`

新对话或中断恢复时，按下面顺序读取：

1. `semantic_v2/00_index/README.md`
2. `semantic_v2/00_index/20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`
3. `semantic_v2/00_index/20260813_1328__NZSCCM__REPOSITORY__CONTENT_SEMANTIC_TREE__SEMANTIC_MANIFEST.md`
4. `semantic_v2/00_index/20260813_1328__NZSCCM__REPOSITORY__AUDITED_ARTIFACTS__SEMANTIC_MANIFEST.csv`
5. `semantic_v2/00_index/20260813_1328__NZSCCM__REPOSITORY__ARTIFACT_SUPERSESSION__SUPERSESSION_MAP.csv`
6. `semantic_v2/00_index/20260813_1328__NZSCCM__REPOSITORY__LEGACY_TO_CANONICAL__RENAME_MAP.csv`
7. `current/CURRENT_STATE.md`
8. `governance/SOURCE_OF_TRUTH_POLICY.md`
9. `governance/RECOVERY_PROTOCOL.md`
10. 根据当前任务沿 semantic_v2 locator 回到 legacy 原文件正文，并以**正文内容 + supersession/revocation 链**判定身份。

```text
PATH_NAME_ONLY_CLASSIFICATION = PROHIBITED
LEGACY_CURRENT_DIRECTORY_SEMANTIC_PURITY = FALSE
CONTENT_AUDIT_BEFORE_USE = REQUIRED
```

## 当前核心入口

- NC + Rebar production contract：沿 `semantic_v2/20_theory/nc_rebar_panel/` 的 20260812_2245 canonical locator。
- Case21 production execution：沿 `semantic_v2/30_workflows/case21/` 的 20260812_1734 canonical locator。
- Case21 current input/coefficient：沿 `semantic_v2/40_execution/case21/`。
- Case21 current result：沿 `semantic_v2/50_results/case21/`。
- Swartz24 current result：沿 `semantic_v2/50_results/swartz24/`。
- superseded direct-N48 等旧执行结果：沿 `semantic_v2/80_history/`，不得因旧文件仍在 `current/` 而复活。

## Audit levels

- `A_DIRECT_CONTENT_AUDIT`：本轮已直接打开正文并按内容/时间链确定身份。
- `B_CONTENT_DERIVED_REGISTRY_OR_LEDGER`：通过已读 source registry / history ledger 确认稳定 source/history 角色；真正引用其技术内容时仍需打开 leaf 原件。
- `C_NOT_YET_DIRECT_CONTENT_AUDITED`：只知道 locator，禁止从文件名推断当前身份。

## 迁移纪律

当前 semantic_v2 是非破坏性重构。旧文件不因为已有 canonical 名就立刻移动/删除；先完成内容分类和 rename/supersession map，再进行可追溯迁移。任何 legacy 文件移动后必须留下 locator 或保证 Git 历史/映射能够无歧义恢复。

## 来源与历史

- 原始 PDF/正式来源 > 有 provenance 的有效摘录 > 历史全文镜像 > 项目解释 > 总结。
- 原始用户—助手对话/原始执行工件 > recovery summary。
- 文件名和所在目录不属于 source-of-truth 层级。
- 查上传来源：`evidence/catalog/SOURCE_REGISTRY.md` + `MASTER_SOURCE_INVENTORY.csv`，但具体技术结论仍回原件核对。
- pre-clean 资产：`history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md`。
- 不用 Case21、Swartz24、UCFT 的结构 Pu 反标材料。
