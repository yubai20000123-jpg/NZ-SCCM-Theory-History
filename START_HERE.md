# NZ-SCCM Theory History — START HERE

本仓库是“轴压稳定矩阵理论推导 / NZ-SCCM”项目的长期证据库、推导历史库和跨对话恢复入口。

## 新对话读取顺序

1. 先读 `SOURCE_OF_TRUTH_POLICY.md`。
2. 读 `evidence/INVENTORY_CHAIN.md`，然后按顺序读取 `evidence/MASTER_SOURCE_INVENTORY.csv` 及 `evidence/inventory_append/`：这是文件级总索引链，先确认原件/工件是否存在以及在哪里恢复。
3. 读 `evidence/SOURCE_REGISTRY.md`：确认核心原始文献、File Library locator、SHA 与证据角色。
4. 读 `history/RAW_HISTORY_REGISTRY.md`：确认原始对话/TXT/JSON/阶段报告的存在与历史身份。
5. 读 `RECOVERY_PROTOCOL.md`：根据当前任务只恢复必要的证据集，不要一次加载全部仓库。
6. 再读 `CURRENT_STATE.md` 和当前任务对应的阶段文件；不得以总结覆盖原始证据。
7. 涉及具体材料或历史争议时，必须回到对应原始 PDF、原始 TXT、原始代码/响应文件或原始 user-assistant dialogue。

## 核心原则

- 文献事实：原始 PDF/正式公开原文最高。
- 项目历史：原始用户—助手对话、原始上传指示词/TXT/JSON 最高。
- 可复现实验、源码、计算报告次之。
- evidence note / decision ledger / stage summary 只作检索和解释，不可冒充原始证据。
- 原始资料不静默覆盖；新版本另存并登记 SHA-256。
- 如果二进制原件尚未复制进 GitHub，必须保留：精确文件名、ChatGPT File Library ID、原始附件事件、公开来源 URL（如有）和 `BINARY_COPY_STATUS`。
- File Library ID 是恢复 locator，不是公开链接；有 DOI/出版社/公开下载地址时应另外登记 URL。
- `FULL_TEXT_MIRROR_MIGRATED` 不等于 `BYTE_EXACT_ORIGINAL`；PDF/ZIP/原始导出的 byte identity 必须由原 SHA 控制。

## 当前来源清点状态

2026-08-10 第一轮项目级清点形成 `evidence/MASTER_SOURCE_INVENTORY.csv`，基线登记 89 条。随后采用 append-only inventory chain 继续登记 D16–D18、R16–R20 等新恢复项目；不能把“89条基线”误解为仓库永久只有 89 项。

当前迁移 checkpoint：`checkpoints/2026-08-10_GITHUB_MIGRATION_P0_P1.md`。

迁移状态见 `evidence/MIGRATION_STATUS_20260810.md`。

同步规则见 `SYNC_PROTOCOL.md`。
