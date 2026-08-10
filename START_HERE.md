# NZ-SCCM Theory History — START HERE

本仓库是“轴压稳定矩阵理论推导 / NZ-SCCM”项目的长期证据库、推导历史库和跨对话恢复入口。

## 新对话读取顺序

1. 先读 `SOURCE_OF_TRUTH_POLICY.md`。
2. 读 `EFFECTIVE_SOURCE_EXCERPT_POLICY.md`：默认只恢复/上传有效原文片段，不再追求 PDF 全文镜像。
3. 读 `evidence/INVENTORY_CHAIN.md`，然后按顺序读取 `evidence/MASTER_SOURCE_INVENTORY.csv` 及 `evidence/inventory_append/`，确认原件/工件是否存在以及在哪里恢复。
4. 读 `evidence/SOURCE_REGISTRY.md`：确认核心原始文献、File Library locator、SHA 与证据角色。
5. 读 `history/RAW_HISTORY_REGISTRY.md`：确认原始对话/TXT/JSON/阶段报告的存在与历史身份。
6. 读 `RECOVERY_PROTOCOL.md`：根据当前任务只恢复必要证据集，不要一次加载全部仓库或全部文献全文。
7. 再读 `CURRENT_STATE.md` 和当前任务对应的阶段文件；不得以总结覆盖原始证据。
8. 涉及具体材料或历史争议时，先读对应 `sources_excerpt/`；若证据不足，再回原始 PDF、File Library、原始 TXT、代码/响应文件或 user-assistant dialogue。

## 核心原则

- 文献事实：原始 PDF/正式公开原文最高。
- 项目历史：原始用户—助手对话、原始上传指示词/TXT/JSON 最高。
- 有 provenance 的有效摘录优先于无目标的全文镜像。
- 可复现实验、源码、计算报告是关键项目证据。
- evidence note / decision ledger / stage summary 只作检索和解释，不可冒充原始证据。
- 原始资料不静默覆盖；新版本另存并登记 SHA-256。
- 如果二进制原件尚未复制进 GitHub，必须保留精确文件名、ChatGPT File Library ID、公开来源 URL（如有）、原始 SHA（若可得）和复制状态。
- File Library ID 是恢复 locator，不是公开链接。
- 已经上传的全文镜像保留，但不再继续为了全文完整率扩张。

## 当前归档策略

2026-08-10 起，项目迁移目标从“尽量全文镜像”改为“**原件定位完整 + 有效证据片段完整 + 历史裁决可恢复**”。

因此 Nguyen Appendix B、孙立鹏整本等不再按块全量上传；只有当前理论真正需要的公式、程序片段、试验数据、状态定义、边界条件、历史关键论述才进入 `sources_excerpt/`。

同步规则见 `SYNC_PROTOCOL.md`。
