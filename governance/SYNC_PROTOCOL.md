# SYNC PROTOCOL — GitHub 持续检查点同步规则

## 1. 基本原则

NZ-SCCM 的长期研究记录采用：

```text
CONTINUOUS_CHECKPOINT_SYNC
```

稳定研究事件形成后，应尽快写回 GitHub；不得默认等待用户再次说“同步 GitHub”，也不得把全部同步拖到对话结束或临时 handoff。

原因：长对话可能随时中断。GitHub 必须能够在没有上一段长聊天上下文的情况下恢复到最近稳定研究状态。

## 2. 何时必须同步

出现下列任一稳定事件时，应优先形成 Git commit：

- 用户明确接受/否决一条理论路线；
- 一个重要理论判断刚刚确定；
- 理论边界被冻结、解除或被新 governance supersede；
- 材料公式、参数来源或 operator 身份被冻结/解冻；
- Case21 / Swartz24 等 benchmark 的正式结果或身份发生变化；
- 新的原始 PDF/TXT/JSON/CSV/代码进入项目；
- 新 gate / rollback / audit / reproducibility artifact 形成；
- 新 source evidence / source locator / equation-to-code mapping 形成；
- 新失败路线及失败原因形成；
- 新可复现实验形成；
- 新 unresolved blocker 形成；
- 对旧结论形成足以影响未来对话的重要修正；
- 用户明确修改项目优先级；
- 一个长计算完成；
- 准备开始一个可能耗时很长的计算之前；
- 一个较长工作阶段完成、下一阶段尚未开始；
- 对话准备迁移或用户明确说“同步 GitHub”。

原则表达为：

```text
稳定研究事件 -> GitHub checkpoint
```

而不是：

```text
对话结束 -> 才统一总结
```

## 3. 什么不需要逐条提交

持续同步不等于每句话一个 commit。以下对象原则上不需要立即进入正式项目目录：

- 普通讨论；
- 临时猜想；
- 尚未完成的试算；
- 思考草稿；
- 明显中间垃圾；
- 尚未形成稳定身份的候选。

但一旦它们形成稳定研究结论、正式否决、可复现实验或 unresolved blocker，就应形成 checkpoint。

## 4. Repository role 与聊天身份必须一致

后续对话产生的成果，不再建立一套只存在于聊天里的平行分类体系。

- 属于 `current` 的结论，聊天中明确标为 current；
- 属于 `evidence` 的来源，不写成正式理论；
- 属于 `history` 的路线，不写成当前主线；
- 属于 `audit_only` 的数值，不升级成 production；
- 属于 `unresolved` 的缺口，不用推断补齐。

文件路径以同步时最新实际 Git tree 为准，不预先假定目录永远固定。

## 5. Canonical path 与历史真实性

同步时：

1. 优先更新已有 canonical 文件，不制造多份无法管理的“最新版”；
2. `CURRENT` 文件可随正式理论更新；
3. `HISTORY` 文件原则上保持历史真实性；
4. 原始 source / raw conversation / original artifact 不静默改写；
5. 旧文件具有历史证据价值时，不用新的 current 内容覆盖它；
6. 被淘汰路线保留其身份、淘汰原因和证据定位；
7. 不为了“仓库干净”删除唯一历史证据；
8. 避免 `FINAL_v2` / `FINAL_v3` / `NEW_FINAL` / `FINAL_REVISED` 一类无法治理的命名链；
9. 优先依赖 canonical path + Git commit history 表达演化。

## 6. 原始文件策略

- 原始 PDF/TXT/用户指示原则上 immutable；
- 不静默覆盖；新版本另存并登记 SHA-256；
- 二进制暂时不能迁移时，必须登记精确文件名、File Library ID、SHA（若可得）、公开 DOI/URL（若有）与恢复状态；
- 压缩包只保存关键 frozen snapshot，避免 R1/R2/R3 大量重复二进制。

## 7. Commit message 建议

采用：`[stage/module] action: short decision`

例如：
- `[UHPC/G16R] freeze: fc=141.1 only`
- `[Case21] audit: single-domain engineering convergence`
- `[history] import: raw turns 0001-0148`
- `[sources] add: Hiew 2024 original PDF`
- `[governance] update: continuous checkpoint sync`

## 8. 重要同步后的聊天反馈

完成一次重要 GitHub 同步后，聊天中只需简短说明：

- 更新了什么；
- 写入/修改了哪些逻辑目录；
- commit SHA；
- 当前项目状态是否因此改变。

不需要把完整 Git diff 贴回聊天。

## 9. 不允许

- 用最新 summary 覆盖早期原始文件；
- 删除 rejected route 以“保持仓库干净”；
- 因新结论出现而改写旧 commit 中的历史事实；
- 把 audit-only 数值结果重新标成 production；
- 延迟已经稳定的重要结论数十轮之后才同步；
- 把聊天记忆当作 GitHub current-state 的替代物。
