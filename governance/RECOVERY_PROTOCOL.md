# RECOVERY PROTOCOL — 跨对话按需恢复协议

本文件规定新 ChatGPT / Work / Codex 对话如何从本仓库恢复 NZ-SCCM，而不是一次性加载全部历史或全部文献全文。

## 0. 每次恢复固定前置

先读：
1. `START_HERE.md`
2. `SOURCE_OF_TRUTH_POLICY.md`
3. `EFFECTIVE_SOURCE_EXCERPT_POLICY.md`
4. `evidence/INVENTORY_CHAIN.md`
5. `evidence/SOURCE_REGISTRY.md`
6. `history/RAW_HISTORY_REGISTRY.md`

然后根据任务读取对应 `sources_excerpt/`、原始响应/代码/历史工件；只有证据不足时才回到全文镜像或原 PDF/File Library。

## 1. 普通混凝土 / Nguyen / Foster

优先恢复：
- Nguyen 原件 locator；
- `sources_excerpt/NC/` 中与 Chapter 3 材料、Chapter 4 稳定、Chapter 6 二阶/耦合、Appendix B 来源程序直接相关的有效摘录；
- `MATERIAL_RECOVERY_EXECUTION_REPORT.md`；
- `equation_to_code_registry_R19.csv`；
- 当前 NC operator 合同与其历史身份。

已经存在的 Ch3/Ch4/Ch6 全文镜像可以辅助搜索，但不是每次恢复的必读项，也不再继续为完整率扩张。

不得把当前 current operator 等同于 Nguyen 全历史本构；不得把 Chapter 4 数值路径冒充当前零空间积分正式路径。

## 2. UHPC 材料

优先从 `sources_excerpt/UHPC/` 和 source locator 恢复：
- Hiew tensile；
- Liu biaxial / sequential TC；
- Lee UHPFRC biaxial TC；
- Leutbecher TC；
- 周俊三轴；
- 王淑楠三轴/W-W；
- 胡文旭；
- `UHPC_STATE_EQUATION_LEDGER.csv`；
- `D19_LIU_TC_CLOSURE_MATRIX.csv`；
- G16R。

只保留项目需要的原始公式、参数、表格、试验路径、状态/破坏准则和关键上下文；不要求整篇全文迁入 GitHub。

若只读取 G31 UHPC-C0，则恢复不完整。UHPC-C0 是历史可计算基线，不是最终 production material operator。

## 3. Case21 / Pu / moment-first D15

优先恢复：
- `CURRENT_STATE.md`；
- current operator contract；
- moment-first D15 锁定流程；
- Case21 global audit handoff；
- NEXTSTEP execution report；
- 2026-08-10 priority reset；
- 必要时回溯 nested D15 / CAS / piecewise analytic 历史工件。

338/342 kN 等数值验证结果只能作 audit/reference，不得用于选择材料系数、解析阶次或根。

## 4. 历史路线裁决

若问题是“当时为什么改路线/废止什么”，必须优先读取原始对话/原始执行证据：
- TURN 0001–0148 原始导出 locator；
- raw conversation dumps；
- R04/R05；
- historical decision/component ledgers；
- rollback reports。

不得只从最新 handoff 反推历史。

## 5. UCFT Layer-0 / Path A / v5

历史追溯时读取：
- `路径A与极限承载力.txt`；
- v4/B1 principle boundary；
- v5 shell/material/global/integration modules；
- Layer-0 locked DOCX locator；
- UCFT V3 progress/raw analysis。

Airy-2c、路径A、B1/B2、S0/S1/S2 等只能按历史身份恢复，不得静默升格为当前 NZ-SCCM 正式主线。

## 6. Y / steel shell / PBL

优先恢复 `sources_excerpt/shell_Y/` 中真正被项目使用的内容：
- 云露：大挠度/薄膜效应、单侧约束、应力函数、Galerkin、后屈曲与有效宽度来源边界；
- 张宁：PBL 局部屈曲及边界/支撑来源；
- 孙立鹏：当前 Y/PBL 理论需要的弹塑性、局部屈曲、设计/理论公式片段；
- 必要时回到 UCFT v5 shell modules。

不再默认上传孙立鹏整本全文。当前 NZ-SCCM 尚未冻结最终 shell production operator，因此不得根据旧 v5 模块自动填补当前空缺。

## 7. 证据冲突

文献事实：原始 PDF > 有 provenance 的有效摘录 > 全文检索镜像 > evidence note > summary。

项目历史：原始 user-assistant dialogue / 原始用户指示 > 原始执行工件 > machine audit / decision ledger > handoff/summary > memory。

如果找不到原件：明确写 `SOURCE_BYTES_NOT_RECOVERED`，保留 File Library ID / 文件名 / DOI / URL，不允许从摘要补写原文。
