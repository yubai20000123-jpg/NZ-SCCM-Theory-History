# START HERE

新对话或中断恢复时，只按下面顺序读取：

1. `current/CURRENT_STATE.md`
2. `governance/SOURCE_OF_TRUTH_POLICY.md`
3. `governance/RECOVERY_PROTOCOL.md`
4. 根据当前任务再进入 `current/`、`evidence/` 或 `history/`。

## 任务最小读取集

- Case21 / Pu：`current/CURRENT_STATE.md` + `current/case21/` + `current/theory/`
- 普通混凝土：再读 `evidence/materials/NC/`
- UHPC：再读 `evidence/materials/UHPC/`
- 钢壳 / Y / PBL：再读 `evidence/steel_shell/`
- “为什么当时改路线”：读 `history/README.md`，然后查对应 D/G/R/UCFT 路线；必要时回到 `history/raw/` 与 `history/recovery/`
- 查某个上传文件是否存在：读 `evidence/catalog/SOURCE_REGISTRY.md` 和 `evidence/catalog/MASTER_SOURCE_INVENTORY.csv`

## 迁移期旧资产

迁移期全文镜像、旧 checkpoint、R2 snapshot 已从当前 `main` 移除，不参与默认搜索。极少数情况下确需找回时，读取：

`history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md`

然后只从历史 commit 恢复当前问题需要的片段。

## 核心边界

- 原始 PDF/正式来源 > 有 provenance 的有效摘录 > 历史全文镜像 > 项目解释 > 总结。
- 原始用户—助手对话/原始执行工件 > recovery summary。
- 旧路线文件存在不代表当前有效；先看 `current/CURRENT_STATE.md`。
- 不用 Case21、Swartz24、UCFT 的结构 Pu 反标材料。
