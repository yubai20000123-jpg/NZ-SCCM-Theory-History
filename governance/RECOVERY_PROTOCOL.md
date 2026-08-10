# RECOVERY PROTOCOL — 跨对话按需恢复

本文件规定新 ChatGPT / Work / Codex 对话如何从重构后的仓库恢复 NZ-SCCM。原则是**最小读取集**，禁止一次性加载全部历史或 `archive/`。

## 0. 固定前置

先读：

1. `START_HERE.md`
2. `current/CURRENT_STATE.md`
3. `governance/SOURCE_OF_TRUTH_POLICY.md`

然后按任务进入对应证据或历史目录。

## 1. Case21 / Pu / current operator

读取：

- `current/CURRENT_STATE.md`
- `current/theory/`
- `current/case21/`
- 必要时 `governance/PRIORITY_RESET_20260810.md`

只有当问题涉及“为什么旧路线被否决”时，才进入 `history/Case21/` 或 `history/NZ_SCCM/`。

338/342 kN 等历史高精度数值只能作 audit/reference，不得用于材料拟合、选阶、选根或结构校准。

## 2. 普通混凝土 / Nguyen / reinforcement

优先读取：

- `evidence/materials/NC/Nguyen_source_map.md`
- `evidence/materials/NC/Nguyen_AppendixB/`
- `current/theory/` 中当前 NC+rebar benchmark

需要历史 Branch-C 数值来源时，再读：

- `history/NZ_SCCM/R_series/`
- `history/NZ_SCCM/material_recovery/`

不要把 Nguyen 的 FE/Gauss/material-point 路线恢复成当前正式零空间积分 operator。

## 3. UHPC

优先读取：

- `evidence/materials/UHPC/core_sources/`
- `evidence/materials/UHPC/audits/`
- `evidence/materials/UHPC/source_data/`
- `evidence/materials/UHPC/LOCAL_THESES_SOURCE_MAP.md`

历史 UHPC-C0 在 `history/materials/UHPC/old_operator_baselines/`，只用于历史追溯，不是 production operator。

若证据包不够，再通过 `evidence/catalog/SOURCE_REGISTRY.md` / `MASTER_SOURCE_INVENTORY.csv` 找到原 PDF/File Library/DOI，按需回原文。

## 4. steel shell / Y / PBL

优先读取：

- `evidence/steel_shell/Yun_Lu_source_map.md`
- `evidence/steel_shell/Zhang_Ning_source_map.md`
- `evidence/steel_shell/Sun_Lipeng/`

必要时再查 `history/UCFT/v5/`。

云露经验有效宽度修正、张宁历史弹性支撑表示、孙立鹏历史有效面积/弹塑性闭合均不能因“来源存在”自动升格为当前 production shell operator。

## 5. 历史路线裁决

先读 `history/README.md`，再进入：

- `history/NZ_SCCM/` — D/G/R、moment-first、direct-analytic、nested-D15 等；
- `history/Case21/` — Case21 旧路线；
- `history/UCFT/` — Layer0 / PathA / v5；
- `history/raw/` 与 `history/recovery/` — 原始历史/法证 locator；
- `history/ledgers/` — 历史组件/决策台账。

不得只从最新 handoff 反推历史。

## 6. 查上传文件/原始来源

读取：

- `evidence/catalog/SOURCE_REGISTRY.md`
- `evidence/catalog/MASTER_SOURCE_INVENTORY.csv`
- `evidence/catalog/INVENTORY_CHAIN.md`

这些目录保存 File Library ID、SHA、URL、历史身份。若目录中旧的迁移状态/path 与当前树不同，以当前 `README/START_HERE` 和 Git tree 为准；catalog 主要承担“原件是否存在/如何找回”的职责。

## 7. archive 规则

`archive/` 默认不读取。它包含此前的全文 TXT 镜像、R2 恢复快照、迁移 checkpoint 和迁移元数据。

只有以下情况进入：

- 当前 evidence excerpt 丢失关键上下文；
- 需要历史法证；
- 需要恢复被重构删除的迁移期文件；
- 原 PDF 暂时无法访问而 archive 中恰有全文检索镜像。

## 8. 证据冲突

文献事实：原始 PDF/正式来源 > 有 provenance 的有效摘录 > 机械全文镜像 > evidence note > summary。

项目历史：原始 user-assistant dialogue / 原始用户指示 > 原始执行工件 > audit/ledger > handoff/summary > memory。

找不到原件时必须明确标记 `SOURCE_BYTES_NOT_RECOVERED`，不能从摘要补写原文。