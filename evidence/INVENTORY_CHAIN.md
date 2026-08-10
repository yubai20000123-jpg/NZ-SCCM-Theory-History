# Inventory Chain

为避免在 GitHub connector 无法安全读取/替换超长 CSV 全文时破坏既有总账，本仓库采用**append-only inventory chain**。

读取顺序：

1. `MASTER_SOURCE_INVENTORY.csv` — 2026-08-10 第一轮 89 条基线；
2. `inventory_append/20260810_P1_D16_D18_R16_R20.csv` — D16–D18 与 R16–R20 新恢复条目；
3. 后续 `inventory_append/YYYYMMDD_*.csv` — 发现即追加，不删除前序记录。

## 规则

- 原始行永不因后续 supersession 被删除；
- 同一文件若出现新副本/新 SHA/新 File Library ID，新增一行并标明 duplicate/version/superseded identity；
- `github_copy_status` 描述的是迁移状态，不代表理论身份；
- 理论身份必须结合 `history/...RECOVERY_BOUNDARY.md`、decision ledger 和 current governance 判断；
- `FULL_TEXT_MIRROR_MIGRATED_TO_GITHUB` 不等于 `BYTE_EXACT_ORIGINAL`；
- PDF/ZIP byte-exact 原件尚未通过当前 connector 上传时，继续保留 locator + SHA + public source URL。

以后若获得本地 git clone / proper binary push 通道，可生成一个新的 consolidated inventory，但不得删除这条 append-only chain，以保留迁移本身的审计历史。
