# SYNC PROTOCOL — GitHub 同步规则

## 1. 何时必须同步

出现下列任一事件时，应形成 Git commit：
- 用户明确接受/否决一条理论路线；
- 材料公式、参数来源或 operator 身份被冻结/解冻；
- Case21 / Swartz24 等 benchmark 的正式结果或身份发生变化；
- 新的原始 PDF/TXT/JSON/CSV/代码进入项目；
- 新 gate / rollback / audit / reproducibility artifact 形成；
- 对话准备迁移或用户明确说“同步 GitHub”。

## 2. 什么不需要逐条提交

普通讨论、尚未裁决的猜想、临时试算不要求每条消息形成 commit。达到稳定研究事件后再同步，并在 decision/history 中保留其前因后果。

## 3. 原始文件策略

- 原始 PDF/TXT/用户指示原则上 immutable；
- 不静默覆盖；新版本另存并登记 SHA-256；
- 二进制暂时不能迁移时，必须登记精确文件名、File Library ID、SHA（若可得）、公开 DOI/URL（若有）与恢复状态；
- 压缩包只保存关键 frozen snapshot，避免 R1/R2/R3 大量重复二进制。

## 4. Commit message 建议

采用：`[stage/module] action: short decision`

例如：
- `[UHPC/G16R] freeze: fc=141.1 only`
- `[Case21] audit: single-domain engineering convergence`
- `[history] import: raw turns 0001-0148`
- `[sources] add: Hiew 2024 original PDF`

## 5. 不允许

- 用最新 summary 覆盖早期原始文件；
- 删除 rejected route 以“保持仓库干净”；
- 因新结论出现而改写旧 commit 中的历史事实；
- 把 audit-only 数值结果重新标成 production。
