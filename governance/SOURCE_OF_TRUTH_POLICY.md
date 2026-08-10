# SOURCE OF TRUTH POLICY

## 1. 文献事实

证据优先级：

1. 原始 PDF / 正式出版物 / 规范原文；
2. 带明确 provenance 的有效原文摘录（页码/行号、来源文件、SHA、File ID/URL）；
3. 由原始 PDF 机械提取的 TXT（仅检索镜像）；
4. evidence note / 公式整理；
5. 项目理论解释；
6. 阶段总结 / handoff / model memory。

若摘录/TXT 与 PDF 版式、公式或图表冲突，以 PDF 为准。

## 2. 项目历史

证据优先级：

1. 原始 user-assistant conversation / 原始用户上传指示词 / 原始 Conversation JSON；
2. 原始执行输出、源码、CSV、报告和可复现实验；
3. decision ledger / audit / recovery report；
4. stage summary / handoff；
5. model memory / inference。

不得用后期工件虚构共享对话中没有发生的正式回复或用户验收。

## 3. 原件保全

- 原始 PDF/TXT/JSON 一经登记，不静默覆盖。
- 每份可取得的本地原件记录 SHA-256、字节数和来源身份。
- 若 GitHub 尚未保存二进制原件，必须登记 `BINARY_COPY_STATUS=PENDING` 和 ChatGPT File Library/file id 或其他恢复指针。
- 新扫描版/新版本作为新文件保存，不覆盖旧 SHA。

## 4. GitHub 文本副本的完整性身份

必须区分：

### A. BYTE_EXACT_ORIGINAL

只有当 GitHub 文件按字节校验与登记原件 SHA-256 一致时，才允许标记为 `BYTE_EXACT_ORIGINAL`。

### B. EFFECTIVE_SOURCE_EXCERPT

从原始文献中抽取、且对当前/历史理论具有明确证据价值的公式、表格、参数、试验路径、原始论述或程序片段。必须记录来源页码/冻结文本行号、source filename、SHA/File ID/URL、SOURCE_ROLE、USED_FOR、NOT_USED_FOR。

### C. FULL_TEXT_MIRROR / NORMALIZED_TEXT_COPY

通过聊天/connector UTF-8 文本接口复制的 TXT/MD/CSV，即使内容完整，也可能因 CRLF/LF、Unicode normalisation、工具转义等导致字节 SHA 与原件不同。因此只能作为检索镜像，不能覆盖原始 SHA。

## 5. PDF 文本策略（2026-08-10 更新）

本项目**不再要求全文镜像**。后续默认只保存 `EFFECTIVE_SOURCE_EXCERPT`，详见 `EFFECTIVE_SOURCE_EXCERPT_POLICY.md`。

已经上传的全文镜像保留，不回删；但不再为了“全文完整率”继续迁移 Nguyen Appendix B、孙立鹏整本等大段文本。只有某个当前理论问题确实需要时，才从原 PDF / File Library 按需提取相应部分。

## 6. 原始信息优先原则

对任何此前上传过的 PDF、TXT/prompt/instruction、JSON、CSV ledger、execution/gate/rollback/response file、source registry、equation-to-code registry、raw conversation export：优先保存原件；工具不能直接复制原件时，至少保存**精确文件名 + File Library ID + 原始 SHA（若可得）+ 外部来源 URL（若有）+ 历史角色 + 当前复制状态**。

对于文献 PDF，不再要求把整个 PDF 文本复制进 GitHub；只要原件 locator 完整，并且项目实际使用的有效部分有可审计摘录，即满足恢复要求。

## 7. 结构试验不得反标材料

Case21、Swartz24、UCFT 构件承载力不得用于反标普通混凝土、UHPC、钢筋或钢壳材料参数。新材料 operator 只能由材料级文献/试验确定或验证。
