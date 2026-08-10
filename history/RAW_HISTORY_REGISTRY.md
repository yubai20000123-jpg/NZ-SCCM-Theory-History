# RAW HISTORY REGISTRY — 原始对话/TXT/响应工件登记

本文件防止后续只剩阶段总结，而丢失用户原始指示、助手原始响应与历史执行输出。

## 1. 已重新确认的原始共享对话/恢复文件

| history_id | 文件名 | File Library / 本地身份 | 证据角色 |
|---|---|---|---|
| CHAT_TURN_1_148 | `chat_export_2026-08-05T20-29-31-447Z_part_01_turn_1-148.txt` | File Library ID `file_00000000b7788209a161cd5ec2db852a` | NZ-SCCM-U v0.2 共享页面 TURN 0001—0148 原始正文基线；TURN 0148 连接中断，不得用后期工件补写 D20 final |
| RAW_EVOLUTION | `{titleNZ-SCCM思想演化恢复,create_time1786(1).txt` | 当前本地 `/mnt/data`；4,609,510 bytes；SHA-256 `43a032115c4010a2f590aeeec4f6fa8335b95a4b229ee0bc0bd57daac62394b6` | 大体量 Conversation JSON/思想恢复证据；含历史 web 搜索、工件、分支线索；不等于共享正文 |
| RAW_EVOLUTION_FL | `{titleNZ-SCCM思想演化恢复,create_time1786.txt` | File Library ID `file_000000001c58820b8d0057693a2cb762`（另有重复/后续副本） | 用于恢复 D/G 系列、材料检索与分支历史 |
| TASK_EXECUTION_RAW | `{title任务执行与核验,create_time1785996157.txt` | File Library 至少存在 `file_00000000db8c81f780f4a4ea9a48b2fa`、`file_00000000566c820690274d576ccbd77c` | 包含材料文献文本镜像、执行/响应上下文；必须保留原始身份，不只抽取结论 |
| PASTED_RAW_20260809 | `粘贴的文本 (1).txt` | File Library ID `file_00000000fbe081faabfe9ca371a41a86` | 包含 2026-08-09 材料/网络检索及对话机器记录片段 |

## 2. 当前本地可直接校验的历史 TXT

| 文件名 | bytes | SHA-256 | 当前身份 |
|---|---:|---|---|
| `路径A与极限承载力.txt` | 22210 | `c1862e55076732361094c4ea99bae1a341b0ddd8580882a2a1b7a58093ef5edb` | 历史路线与 UHPC Layer-0 等内容的原始阶段文件；只作历史追溯，不恢复为当前正式主线 |
| `UCFT V3工程进展.txt` | 1761 | `b72083561889782ceacf0b2b415f61799516c61e10e9161280c7588a91186bd9` | UCFT V3 历史进展原始 TXT |
| `UCFT V3工程进展分析.txt` | 23424 | `931bb423875e84c8b573e74dce0ae89c804f49f04528b02e8592d3c156a51b38` | UCFT V3 历史分析原始 TXT |

## 3. “响应文件”也必须保存

以下类型不应只在阶段总结中出现：

- gate report / execution report；
- CSV state ledger；
- equation-to-code registry；
- exact input hashes；
- source registry；
- prompt / instruction file；
- solver response / calculation transcript；
- one-shot closure / rollback report；
- active branch machine audit JSON。

后续恢复时优先按文件名关键词搜索：

`D6`, `D8`, `D9`, `D10`, `D11`, `D12`, `D13`, `D14`, `D15`, `D18`, `D19`, `D19R`, `D19C`, `D20`, `G15`, `G16R`, `G30`, `G31`, `ONE_SHOT_CLOSURE`, `ACTIVE_BRANCH`, `equation_to_code_registry`, `STATE_EQUATION_LEDGER`。

## 4. 不允许的历史压缩

不得把：

`原始对话 → 若干 gate 报告 → 一个最新 handoff`

当作完整历史。

正确恢复顺序应为：

`原始 user/assistant 文本 + 原始附件/响应工件 → 可复现实验 → decision ledger → handoff`。

## 5. GitHub 迁移状态

- 当前先登记所有已发现原件和 File Library ID。
- 文本原件将分批直接复制到 `history/raw/`。
- 大 PDF 二进制若当前 connector 不便直接复制，则至少保留 File Library locator、SHA（若本地可得）和机械提取文本镜像。
- File Library pointer 不是公开 URL；若原始资料有 DOI/公开来源，后续应在独立 evidence note 中补正式链接。
