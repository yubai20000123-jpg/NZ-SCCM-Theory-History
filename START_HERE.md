# START HERE

## 先读语义索引，不按文件名猜身份

本仓库当前存在历史/当前工件混放和旧命名遗留。目录名、文件名及其中的 `current`、`fresh`、`production`、`PASS`、日期等只具有**定位作用**，不自动决定文件是否当前有效。

新对话或中断恢复时，按下面顺序读取：

1. `current/CONTENT_INDEX.md`
2. `current/CONTENT_SEMANTIC_MANIFEST_20260813.csv`
3. `current/CURRENT_STATE.md`
4. `governance/CONTENT_SEMANTIC_IDENTITY_RULE_20260813.md`
5. `governance/SOURCE_OF_TRUTH_POLICY.md`
6. `governance/RECOVERY_PROTOCOL.md`
7. 根据当前任务再进入 `current/`、`evidence/` 或 `history/`，并以**文件正文内容 + supersession/revocation 链**判定身份。

```text
PATH_NAME_ONLY_CLASSIFICATION = PROHIBITED
CURRENT_DIRECTORY_SEMANTIC_PURITY = FALSE
CONTENT_AUDIT_BEFORE_USE = REQUIRED
```

## 任务最小读取集

- Case21 / Pu：先读上述语义索引，再按 manifest 指向读取当前 production contract、Case21 current closure 与所需执行工件；不得仅凭 `current/case21/` 或文件名选择。
- 普通混凝土：再读 `evidence/materials/NC/`。
- UHPC：再读 `evidence/materials/UHPC/`。
- 钢壳 / Y / PBL：再读 `evidence/steel_shell/`。
- “为什么当时改路线”：读 `history/README.md`，然后查对应 D/G/R/UCFT 路线；必要时回到 `history/raw/` 与 `history/recovery/`。
- 查某个上传文件是否存在：读 `evidence/catalog/SOURCE_REGISTRY.md` 和 `evidence/catalog/MASTER_SOURCE_INVENTORY.csv`，但最终仍需核对正文内容。

## 迁移期旧资产

迁移期全文镜像、旧 checkpoint、R2 snapshot 已从部分当前目录移除，但仓库仍存在 legacy/current 混合工件。极少数情况下确需找回 pre-clean 资产时，读取：

`history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md`

然后只从历史 commit 恢复当前问题需要的片段。

## 核心边界

- 原始 PDF/正式来源 > 有 provenance 的有效摘录 > 历史全文镜像 > 项目解释 > 总结。
- 原始用户—助手对话/原始执行工件 > recovery summary。
- **文件名和所在目录不属于 source-of-truth 层级。**
- 旧路线文件存在不代表当前有效；所谓 `current` 文件也可能已被后续正文明确替代或仅保留为 lineage/audit。
- 不用 Case21、Swartz24、UCFT 的结构 Pu 反标材料。
