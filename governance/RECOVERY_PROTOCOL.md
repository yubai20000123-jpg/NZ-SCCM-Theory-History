# RECOVERY PROTOCOL — 跨对话恢复

本文件规定新 ChatGPT / Work / Codex 对话如何从重构后的仓库恢复 NZ-SCCM。

仓库支持两种恢复模式：

1. `FULL_STARTUP_RECOVERY`：用于新的长期项目对话接管、长对话中断后的正式恢复，或用户明确要求“完整恢复项目”时。此模式优先于最小按需读取。
2. `TASK_SCOPED_RECOVERY`：用于已经建立完整上下文后的普通窄任务，只恢复与当前问题直接相关的最小证据集。

不得把 `TASK_SCOPED_RECOVERY` 的最小读取原则用于削弱用户明确要求的 `FULL_STARTUP_RECOVERY`。

## 0. FULL_STARTUP_RECOVERY

当进入完整启动恢复模式时，必须先确认实际 GitHub 状态，而不是根据旧聊天记忆、旧文件名单或历史 handoff 猜测当前结构。

### 0.1 仓库身份与动态扫描

依次完成：

1. 实际连接仓库；
2. 确认默认分支；
3. 记录恢复开始时的 HEAD commit；
4. 递归扫描当前默认分支目录树；
5. 以实际 tree 决定读取对象，不使用僵硬固定文件名单；
6. 若恢复过程中对 governance 形成稳定修订并提交，区分“恢复基线 HEAD”和“同步后新 HEAD”。

### 0.2 固定前置读取

无论仓库结构如何演化，优先寻找并读取当前承担以下角色的文件：

1. 项目入口 / `START_HERE`；
2. 当前状态 / `CURRENT_STATE`；
3. source-of-truth / evidence hierarchy；
4. recovery / sync governance。

当前仓库对应入口为：

- `START_HERE.md`
- `current/CURRENT_STATE.md`
- `governance/SOURCE_OF_TRUTH_POLICY.md`
- 本文件
- `governance/SYNC_PROTOCOL.md`

这些路径以后若调整，以最新实际 tree 与 repository role 为准。

### 0.3 分层完整恢复顺序

在工具和上下文容量允许的前提下，按以下层级分批继续读取；“顺序靠后”不等于“可以忽略”。

**第一层：当前状态 / 当前正式理论 / 当前执行入口**

- `current/` 中 current-state、theory、case、result、code 和当前执行报告；
- 当前正式主线、benchmark、未闭合问题与下一任务。

**第二层：governance / source-of-truth / recovery / sync / project rules**

- source hierarchy；
- supersession / revocation / rollback；
- recovery 与 checkpoint 规则；
- 当前优先级重置。

**第三层：evidence / source maps / registries / inventories / audits**

- material evidence；
- formula evidence；
- source registry；
- source locator；
- equation-to-code mapping；
- audit/report/JSON/CSV/TXT/code；
- 原始 PDF 或正式来源的有效摘录与身份信息。

**第四层：history / rejected routes / rollback / old operators / raw history / forensic records**

- D/G/R 历史；
- old Case21 routes；
- UCFT historical routes；
- raw conversation / original user instruction locators；
- decision/component ledgers；
- forensic recovery artifacts。

**第五层：大型全文镜像、旧迁移资产或只存在于历史 commit 的资料**

只有当前四层仍无法解决证据问题时，再读取：

- pre-clean repository tree；
- 迁移期全文镜像；
- 旧 snapshots / checkpoints；
- 其他已从当前 `main` 清出的超大迁移资产。

第五层不得整体重新合并回当前 `main`；只定点恢复当前证据问题需要的内容。

### 0.4 大型文件与二进制来源

- 大型文本文件允许分段读取，但不能因为首段已有 summary 就宣布完整恢复；
- PDF/DOCX/ZIP 等二进制若正文不在 Git 中，至少恢复 repository metadata、locator、SHA、file identity、source role 和已有 provenance 摘录；
- 当前理论/证据判断确实需要正文时，再回原 PDF / File Library /正式出版来源；
- `SOURCE_BYTES_NOT_RECOVERED` 必须显式标记，不能从 summary 补写原文。

### 0.5 重要对象必须判定身份

文件“存在”不等于“当前有效”。对重要理论、公式、材料模型、计算路线和数值结果，必须依据最新 current/governance 判断其身份，例如：

- `CURRENT`
- `CURRENT_BENCHMARK`
- `SOURCE_ONLY`
- `RETAINED`
- `HISTORICAL`
- `SUPERSEDED`
- `REJECTED`
- `DIAGNOSTIC_ONLY`
- `AUDIT_ONLY`
- `EXECUTED_BUT_UNACCEPTED`
- `UNRESOLVED`

历史文件中的 `PASS`、`READY`、`LOCKED`、`PRODUCTION` 不得自动覆盖后续 current/governance。

### 0.6 冲突裁决

涉及文献事实：

```text
原始 PDF / 正式出版来源
> 有 provenance 的原文有效摘录
> 机械文本镜像
> evidence note / formula extraction
> 项目解释
> summary / handoff / model memory
```

涉及项目历史：

```text
原始 user-assistant conversation / 原始用户指示 / 原始 Conversation JSON
> 原始执行工件、源码、CSV、报告、可复现实验
> audit / decision ledger / recovery report
> handoff / summary
> 模型记忆或推断
```

冲突时必须记录证据等级、时间顺序和 current/history 身份，不得自行合成一个“看起来合理”的版本。

### 0.7 FULL_STARTUP_RECOVERY 完成门禁

至少能够从仓库证据回答下列问题后，才可宣布恢复完成：

1. 当前项目最终目标；
2. 当前正式主线；
3. 当前推进阶段；
4. ordinary concrete operator 当前身份；
5. reinforcement 如何进入结构方程；
6. UHPC 当前闭合程度；
7. steel-shell / Y / PBL 当前闭合程度；
8. Case21 当前正式计算身份；
9. Swartz24 当前状态；
10. 当前锁定理论边界；
11. 已淘汰路线；
12. 只能作 audit/reference 的历史结果；
13. 当前关键 unresolved blocker；
14. 下一步最合理工作；
15. 上述每一点对应的 GitHub 核查路径。

若仓库过大，应分批继续读取，而不是自行认定剩余内容不重要。若发现访问失败、损坏、current 冲突、registry 冲突、关键原件缺失或历史身份无法判断，必须在宣布恢复完成前显式报告。

## 1. TASK_SCOPED_RECOVERY 固定前置

当完整上下文已经建立、当前只是普通窄任务时，先读：

1. `START_HERE.md`
2. `current/CURRENT_STATE.md`
3. `governance/SOURCE_OF_TRUTH_POLICY.md`

然后按任务进入对应证据或历史目录。

## 2. Case21 / Pu / current operator

读取：

- `current/CURRENT_STATE.md`
- `current/theory/`
- `current/case21/`
- 必要时 `governance/PRIORITY_RESET_20260810.md`

只有当问题涉及“为什么旧路线被否决”时，才进入 `history/Case21/` 或 `history/NZ_SCCM/`。

338/342 kN 等历史高精度数值只能作 audit/reference，不得用于材料拟合、选阶、选根或结构校准。

## 3. 普通混凝土 / Nguyen / reinforcement

优先读取：

- `evidence/materials/NC/Nguyen_source_map.md`
- `evidence/materials/NC/Nguyen_AppendixB/`
- `current/theory/` 中当前 NC+rebar benchmark

需要历史 Branch-C 数值来源时，再读：

- `history/NZ_SCCM/R_series/`
- `history/NZ_SCCM/material_recovery/`

不要把 Nguyen 的 FE/Gauss/material-point 路线恢复成当前正式零空间积分 operator。

## 4. UHPC

优先读取：

- `evidence/materials/UHPC/core_sources/`
- `evidence/materials/UHPC/audits/`
- `evidence/materials/UHPC/source_data/`
- `evidence/materials/UHPC/LOCAL_THESES_SOURCE_MAP.md`

历史 UHPC-C0 在 `history/materials/UHPC/old_operator_baselines/`，只用于历史追溯，不是 production operator。

若证据包不够，再通过 `evidence/catalog/SOURCE_REGISTRY.md` / `MASTER_SOURCE_INVENTORY.csv` 找到原 PDF/File Library/DOI，按需回原文。

## 5. steel shell / Y / PBL

优先读取：

- `evidence/steel_shell/Yun_Lu_source_map.md`
- `evidence/steel_shell/Zhang_Ning_source_map.md`
- `evidence/steel_shell/Sun_Lipeng/`

必要时再查 `history/UCFT/v5/`。

云露经验有效宽度修正、张宁历史弹性支撑表示、孙立鹏历史有效面积/弹塑性闭合均不能因“来源存在”自动升格为当前 production shell operator。

## 6. 历史路线裁决

先读 `history/README.md`，再进入：

- `history/NZ_SCCM/` — D/G/R、moment-first、direct-analytic、nested-D15 等；
- `history/Case21/` — Case21 旧路线；
- `history/UCFT/` — Layer0 / PathA / v5；
- `history/raw/` 与 `history/recovery/` — 原始历史/法证 locator；
- `history/ledgers/` — 历史组件/决策台账。

不得只从最新 handoff 反推历史。

## 7. 查上传文件/原始来源

读取：

- `evidence/catalog/SOURCE_REGISTRY.md`
- `evidence/catalog/MASTER_SOURCE_INVENTORY.csv`
- `evidence/catalog/INVENTORY_CHAIN.md`

这些目录保存 File Library ID、SHA、URL、历史身份。若其中旧的 migration path/status 与当前树不同，以 `START_HERE.md`、`current/CURRENT_STATE.md` 和当前 Git tree 为准；catalog 的主要职责是“原件是否存在/如何找回”。

## 8. 已移出的迁移期大文件

此前的全文 TXT 镜像、R2 恢复快照、GitHub 迁移 checkpoint 和 migration metadata **不再存在于当前 `main`**，以避免搜索污染。

若极少数情况下确需这些资料：

1. 读 `history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md`；
2. 从其中记录的 pre-clean Git commit 定点读取所需文件；
3. 只恢复当前问题需要的片段，不要把整套旧目录重新合并到 `main`。

优先仍应回原 PDF / File Library，而不是依赖旧全文镜像。

## 9. 证据冲突

文献事实：原始 PDF/正式来源 > 有 provenance 的有效摘录 > Git 历史中的机械全文镜像 > evidence note > summary。

项目历史：原始 user-assistant dialogue / 原始用户指示 > 原始执行工件 > audit/ledger > handoff/summary > memory。

找不到原件时必须明确标记 `SOURCE_BYTES_NOT_RECOVERED`，不能从摘要补写原文。
