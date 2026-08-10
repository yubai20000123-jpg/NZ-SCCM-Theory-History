# RECOVERY PROTOCOL — 跨对话按需恢复协议

本文件规定新 ChatGPT / Work / Codex 对话如何从本仓库恢复 NZ-SCCM，而不是一次性加载全部历史。

## 0. 每次恢复固定前置

先读：
1. `START_HERE.md`
2. `SOURCE_OF_TRUTH_POLICY.md`
3. `evidence/MASTER_SOURCE_INVENTORY.csv`
4. `evidence/SOURCE_REGISTRY.md`
5. `history/RAW_HISTORY_REGISTRY.md`

然后根据任务选取下述最小证据集。

## 1. 普通混凝土 / Nguyen / Foster

优先恢复：
- `Nguyen-011325526.pdf` 原文；
- Nguyen Chapter 3 / Appendix B 材料关系；
- Chapter 4 稳定骨架；
- Chapter 6 完整路径历史材料；
- `MATERIAL_RECOVERY_EXECUTION_REPORT.md`；
- `equation_to_code_registry_R19.csv`；
- 当前 NC operator 合同与其历史身份。

不得把当前 current operator 等同于 Nguyen 全历史本构；不得把 Chapter 4 数值路径冒充当前零空间积分正式路径。

## 2. UHPC 材料

至少检索：
- Hiew 2024 tensile；
- Liu 2024 biaxial；
- Lee 2017 UHPFRC biaxial TC；
- Leutbecher 2020 TC；
- 周俊三轴；
- 王淑楠三轴/W-W；
- 胡文旭；
- `UHPC_STATE_EQUATION_LEDGER.csv`；
- `D19_LIU_TC_CLOSURE_MATRIX.csv`；
- `NZ_SCCM_G16R_signed_excess坐标_材料参数重审_U候选_D可识别性门禁.md`。

若只读取 G31 UHPC-C0，则恢复不完整。UHPC-C0 是历史可计算基线，不是最终 production material operator。

## 3. Case21 / Pu / moment-first D15

优先恢复：
- 当前 `CURRENT_STATE.md`（建立后）；
- current operator contract；
- moment-first D15 锁定流程；
- Case21 global audit handoff；
- NEXTSTEP execution report；
- 2026-08-10 priority reset；
- 必要时再回溯 nested D15 / CAS / piecewise analytic 历史工件。

注意：338/342 kN 等数值验证结果只能作 audit/reference，不得用于选择材料系数、解析阶次或根。

## 4. 历史路线裁决

若问题是“当时为什么改路线/废止什么”，必须先读取原始对话：
- `chat_export_2026-08-05T20-29-31-447Z_part_01_turn_1-148.txt`；
- raw conversation dumps；
- R04/R05 recovery audit；
- historical component ledger；
- rollback reports。

不得只从最新 handoff 反推历史。

## 5. UCFT Layer-0 / Path A / v5

历史追溯时读取：
- `路径A与极限承载力.txt`；
- v4/B1 principle boundary；
- v5 shell/material/global/integration modules；
- Layer-0 locked DOCX；
- UCFT V3 progress/raw analysis。

Airy-2c、路径A、B1/B2、S0/S1/S2 等只能按其历史身份恢复，不得静默升格为当前 NZ-SCCM 正式主线。

## 6. Y / steel shell / PBL

从原始文献开始：
- 云露；
- 张宁；
- 孙立鹏；
- 必要时回到 UCFT v5 shell modules。

当前 NZ-SCCM 尚未冻结最终 shell production operator，因此不得根据旧 v5 模块自动填补当前空缺。

## 7. 证据冲突

文献事实冲突：原始 PDF > 可检索文本镜像 > evidence note > summary。

项目历史冲突：原始 user-assistant dialogue / 原始用户指示 > 原始执行工件 > machine audit / decision ledger > handoff/summary > memory。

如果找不到原件：明确写 `SOURCE_BYTES_NOT_RECOVERED`，保留 File Library ID / 文件名 / DOI / URL，不允许从摘要补写原文。
