# SOURCE MIGRATION STATUS — 2026-08-10

## 1. 索引基线

已建立 `evidence/MASTER_SOURCE_INVENTORY.csv`。当前第一轮项目级清点登记 **89 条**来源/历史工件；该数字是第一轮核心项目清点基线，不声称 File Library 中已不存在其他历史副本或外围文件。

类型初始分布：
- MD: 37
- PDF: 18
- TXT: 13
- CSV: 10
- JSON: 6
- DOCX: 2
- PY: 1
- XLSX: 1
- ZIP: 1

后续发现新来源采用 append / supersede，不删除旧行。

## 2. 本轮 P0 已实际复制到 GitHub 的文本工件

### 当前治理 / 当前理论

- `CURRENT_STATE.md`
- `theory/current/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`
- `theory/current/nz_sccm_current_operator_explicit_v1.py`
- `governance/NZ_SCCM_PRIORITY_RESET_MATERIAL_OPERATOR_ARCHITECTURE_REVIEW_20260810.md`

### Case21

- `cases/Case21/NZ_SCCM_CASE21_GLOBAL_AUDIT_HANDOFF_20260809.md`
- `cases/Case21/NEXTSTEP_EXECUTION_REPORT.md`
- `cases/Case21/history/G31_ARTIFACT_LOCATOR.md`

### UHPC 原始研究工件 / 历史 baseline

- `materials/UHPC/audits/NZ_SCCM_G16R_signed_excess坐标_材料参数重审_U候选_D可识别性门禁.md`
- `materials/UHPC/audits/UHPC_STATE_EQUATION_LEDGER.csv`
- `materials/UHPC/audits/D19_LIU_TC_CLOSURE_MATRIX.csv`
- `materials/UHPC/history/10_UHPC_C0_material_contract.json`

### UCFT 历史

- `history/raw/UCFT_V3工程进展.txt`
- `history/UCFT_L0/UCFT_V3工程进展分析.txt`
- `history/UCFT_pathA/路径A与极限承载力.txt`
- `history/NZ_SCCM_moment_first/NZ_SCCM_moment_first_D15_Pu_锁定流程与发展路线_20260809.md`

### 原始对话 / 法证定位

- `history/raw/CHAT_TURN_0001_0148_LOCATOR.md`
- `history/recovery/G15_FORENSIC_PACKAGE_LOCATOR.md`

### R2 完整迁移快照

已复制：
- `snapshots/2026-08-10_R2/00_R2_完整思想历史总纲.md`
- `snapshots/2026-08-10_R2/01_R2_材料研究证据总账.md`
- `snapshots/2026-08-10_R2/02_R2_历史路径裁决矩阵.md`
- `snapshots/2026-08-10_R2/03_R2_历史与材料资料强制恢复清单.md`
- `snapshots/2026-08-10_R2/04_R2_新对话首条指示词.md`
- `snapshots/2026-08-10_R2/05_R2_FINAL_ATTEMPT_OR_NEW_OPERATOR.md`
- `snapshots/2026-08-10_R2/06_R2_明确未知项与未统一项.md`
- `snapshots/2026-08-10_R2/README_R2_使用方法.md`

## 3. 已确认但仍 locator-only 的核心原件

### 原始共享对话

`chat_export_2026-08-05T20-29-31-447Z_part_01_turn_1-148.txt`

File Library ID：
`file_00000000b7788209a161cd5ec2db852a`

原因：当前 GitHub connector 不提供把 File Library 对象直接作为上传文件参数的动作。不得用摘要重建原件。

### G31 原始完整 MD

`00_G31_Case21_Pu全过程与UHPC_C0同步模型.md`

File Library ID：
`file_0000000095688206bc564face5eb85fc`

当前检索可以读取正文，但返回 payload 对长文件会截断；因此只保存 locator，不把不完整正文冒充原件。

### Conversation JSON 法证包

`01_RAW_ACTIVE_BRANCH_MACHINE_AUDIT.json` 及配套 10 文件法证包仍以 File Library 原件为 authoritative source；GitHub 已保存精确 SHA-256 manifest 和恢复说明。

## 4. 已确认的核心原始 PDF

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

这些原文不得被 evidence note 或 summary 替代。

## 5. PDF/ZIP 二进制迁移状态

本轮已建立不可丢失 locator 层：

`精确文件名 + File Library ID + 本地 SHA（若可得）+ 外部 DOI/URL（若已核验）+ 历史身份`

当前 GitHub connector 的通用写动作支持 UTF-8 text/blob，但没有把本地 `/mnt/data/*.pdf` 或 File Library file reference 直接作为 GitHub file 参数上传的动作。对几十 MB PDF/ZIP 不通过模型消息手工 base64 搬运，以免产生截断、费用和完整性风险。

因此：
- 文本原件：能完整取得时直接复制；
- 长文本：若工具返回会截断，则只存 locator，绝不冒充原件；
- PDF/ZIP：当前保留 SHA / File Library ID / source URL；待出现正常 file-upload / git-push 通道后迁入；
- 已有 PDF 机器提取文本可作为 `sources_text/` 检索镜像，但若与 PDF 冲突，PDF 永远优先。

## 6. P0 当前裁决

P0 中可通过当前连接器可靠完整复制的核心文本已经大体迁入。

仍未直接复制的 P0 原件主要是：
1. TURN 1–148 原始导出全文；
2. G31 原始完整长 MD；
3. 大型 Conversation JSON / raw dump。

这些均已建立精确 locator，不会因当前对话结束而失去恢复路径。

## 7. 下一批 P1

优先迁入：
- R04 / R05 recovery reports；
- D11–D19R gate/test/rollback artifacts；
- G16/G20/G21 等材料审计；
- G31 可完整取得的配套 JSON/CSV；
- Case21 direct analytic / CAS / piecewise / nested 的可读报告与代码；
- v5 shell/material/asymmetric/all-buckling 历史模块。

## 8. P2

- 大型 PDF/ZIP 原件正式迁入；
- `sources_text/` extracted text mirrors；
- DOI / publisher URLs 逐篇复核；
- 重复 PDF / TXT 去重关系与 supersedes 链完善。
