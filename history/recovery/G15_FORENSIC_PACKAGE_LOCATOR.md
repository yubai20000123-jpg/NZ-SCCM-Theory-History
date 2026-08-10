# G15 / active-main-branch Conversation JSON 法证包定位器

## 原始审计文件

`01_RAW_ACTIVE_BRANCH_MACHINE_AUDIT.json`

ChatGPT File Library ID:
`file_00000000df348211abafbcd65759a6c3`

该审计的 authoritative conversation source 在工件中登记为：

`{title任务执行与核验,create_time1785996157(1).txt`

conversation id:
`6a742376-07f4-83e8-a85b-4b6a3b1cb0b7`

机器审计记录：

```text
TOTAL_MAPPING_NODES = 1033
TOTAL_MESSAGE_NODES = 1032
ROOT_NODES = 1
LEAF_NODES = 1
BRANCHING_NODES = 0
SIDE_BRANCH_COUNT = 0
ACTIVE_MAIN_BRANCH_RESOLVED = YES
ACTIVE_MAIN_BRANCH_NODE_COUNT = 1033
```

## 配套文件及 SHA-256

来自 `MANIFEST_SHA256.json`：

```text
01_RAW_ACTIVE_BRANCH_MACHINE_AUDIT.json
2536baa3a38b517d64046439680a10e8716b97caae1e0ce3f005d51596bdc3c1

02_USER_VISIBLE_MAIN_DIALOGUE.md
5a7071abe2a65e0077ca37cc45f0fc8a2931ffa83ca94175d3719a07c5881955

03_DIALOGUE_GROUP_INDEX.csv
70849ffc9ae6b3c093ba5fca21b5aa7dfb5fd8eabe1109cdced26b77dc0b2140

04_D4_TO_G15_STAGE_INDEX.csv
42ef9fc2c13c5be4fb13b139963c6b35e4faf89838d8bacf00715f7e4b426b33

05_D20_TO_G15_FULL_EVOLUTION.md
207b1ba6162fc8c20eac68ebc8aecfe691f98a8df61a74cf2dadcada7eea3936

06_HISTORICAL_DECISION_LEDGER.csv
2949b6968537dccb2e60c20f75fda6640bf6ef281c11ddd6ce8e182074851d18

07_BRANCH_AUDIT.csv
c55296d3a8a234d77cdc69698fe8c93552c32ca87452a1ccaeee815aefe8690c

08_G14_FORENSIC_REPORT.md
ffe3ebaafa0216e690cf156e41d37d6f9b0dff701057bf502f7f26ee22ab06cf

09_G15_INTERRUPTION_FORENSIC_REPORT.md
6e427833a2854c5b5f603617c6474033ca3524a5bc6465eb8ddc58a73639df1d

10_RECOVERY_COMPLETENESS_REPORT.md
e042a39b7a7b9ebb77a3ec17c423dac31a1e21b6fac072c927b82ba582ed32cf
```

## 历史边界

该 Conversation JSON 法证包的真实 active-main-branch 终点被审计为 G15 interruption：最后一个 assistant code/tool-call 节点仍为 `in_progress`，随后 tool execution output 已成功返回并成为唯一 leaf，但其后没有 assistant final、没有新 user、没有 G16。

因此这个 JSON 法证包本身不能证明更晚阶段存在于该 conversation 的真实主分支。更晚 G16/G31 等内容应按它们各自的来源/对话/工件身份记录，不能倒填进入这份 JSON 的主分支。

## GitHub 迁移状态

当前保存 locator + hashes；完整 JSON 体量较大，原始 File Library 对象仍是 authoritative source。取得可直接上传的本地文件通道后，应将法证包各原件原样复制到 `history/recovery/G15_forensic_package/`，不得从摘要重建。
