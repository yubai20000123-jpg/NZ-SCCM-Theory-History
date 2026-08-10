# SOURCE MIGRATION STATUS — 2026-08-10

## 1. 本轮已完成

已建立 `evidence/MASTER_SOURCE_INVENTORY.csv`，当前第一轮项目级清点共登记 **89 条**来源/历史工件。

类型分布：
- MD: 37
- PDF: 18
- TXT: 13
- CSV: 10
- JSON: 6
- DOCX: 2
- PY: 1
- XLSX: 1
- ZIP: 1

证据级别分布：
- L1_PRIMARY_SOURCE: 18
- L1_PROJECT_HISTORY: 12
- L2_MACHINE_EVIDENCE: 44
- L2_PROJECT_ARTIFACT: 11
- L2_CURRENT_BENCHMARK: 2
- L2_CURRENT_GOVERNANCE: 1
- L3_HISTORICAL_DERIVED: 1

当前至少 **31 条**登记对象在本地运行环境有原始/副本字节可用；大量其余对象已保存 File Library ID，可在后续会话中按 ID/文件名恢复。

## 2. 已确认的核心原始 PDF

### NC/RC
- Nguyen thesis
- Attard reinforced-concrete wall buckling

### UHPC
- Hiew 2024 unified tensile constitutive model
- Liu 2024 biaxial UHPC
- Leutbecher 2020 UHPFRC TC + Data S1
- Lee 2017 UHPFRC biaxial TC
- Shen 2020 equi-biaxial tension
- FHWA HRT-23-077
- 周俊 UHPC 三轴受压
- 王淑楠 UHPC 三轴受压/破坏准则
- 胡文旭钢-UHPC相关硕士论文
- Diab/Ferche 2026 compression-softening synthesis

### shell / PBL
- 云露
- 张宁
- 孙立鹏

这些原文不得被后续 evidence note 或 summary 替代。

## 3. 已确认的核心原始历史

- TURN 1–148 原始共享对话导出；
- 对应 manifest；
- 多份 Conversation JSON / raw text 恢复 dump；
- 路径A历史 TXT；
- UCFT V3 工程进展原始 TXT；
- active-branch machine audit / visible dialogue / decision ledger；
- D11–D19R、G16/G16R、G31、moment-first D15、Case21 多后端解析、global one-domain 等阶段工件。

## 4. 当前 GitHub 二进制迁移状态

本轮重点是先建立不可丢失的 locator 层：

`精确文件名 + File Library ID + 本地 SHA（若可得）+ 外部 DOI/URL（若已核验）+ 历史身份`

当前 GitHub connector 的通用文本写接口适合直接写 MD/TXT/CSV/JSON/PY；对几十 MB PDF/ZIP 原件不应通过聊天正文进行 base64 搬运。因此：

- 小型文本原件：后续优先直接复制入 GitHub；
- PDF/ZIP：当前先保留完整 locator / SHA / source URL，并在可用文件上传通道或人工 Git push 时迁入；
- File Library 中但当前 `/mnt/data` 无二进制副本的原件：保持 `REGISTERED_FILE_LIBRARY_POINTER`，不得伪称已复制。

## 5. 下一批迁移优先级

P0：
1. TURN 1–148 原始对话 TXT；
2. G16R、UHPC state ledger、D19 Liu TC closure；
3. current operator MD/PY；
4. priority reset / Case21 global handoff / NEXTSTEP report；
5. 路径A、UCFT V3 raw analysis。

P1：
- D11–D19R 原始 gate/test/rollback artifacts；
- G31 artifacts；
- Case21 direct analytic / CAS / piecewise / nested packages的可读报告与代码。

P2：
- 大型 PDF/ZIP 原件正式迁入；
- extracted text mirrors；
- DOI / publisher URLs 的逐篇复核。

## 6. 完整性声明

`MASTER_SOURCE_INVENTORY.csv` 是当前第一轮全项目清点基线，不声称 File Library 中已经不存在其他历史副本或外围项目文件。后续发现新文件时采用 append / supersede 方式增加，不删除旧行。
