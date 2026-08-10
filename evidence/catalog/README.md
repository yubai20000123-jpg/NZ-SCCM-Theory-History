# SOURCE CATALOG

这里的 catalog 用于回答：**某个原始文件是否存在、叫什么、File Library ID / SHA / DOI / URL 是什么、历史上处于什么阶段。**

## 文件

- `MASTER_SOURCE_INVENTORY.csv`：2026-08-10 第一轮来源总账基线；
- `INVENTORY_CHAIN.md` + `inventory_append/`：后续追加发现；
- `SOURCE_REGISTRY.md`：核心文献/原件 locator。

## 重要边界

这些总账是在仓库重构之前逐步形成的，其中个别 `github_copy_status`、旧目录 path 或 migration 状态记录的是**当时的迁移历史**，不代表当前工作目录。

当前文件位置与当前理论身份必须按：

1. `START_HERE.md`
2. `current/CURRENT_STATE.md`
3. 当前 Git tree

判断。

不要为了修正目录移动而改写历史 inventory 行；否则会破坏“当时发生了什么”的审计价值。新来源继续 append-only 登记即可。
