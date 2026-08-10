# SOURCE OF TRUTH POLICY

## 1. 文献事实

证据优先级：

1. 原始 PDF / 正式出版物 / 规范原文；
2. 带明确 provenance 的有效原文摘录（来源文件、SHA、File ID/URL，尽量带页码/行号）；
3. 必要时从 Git 历史定点恢复的机械全文镜像；
4. evidence note / 公式整理；
5. 项目理论解释；
6. stage summary / handoff / model memory。

若摘录/历史 TXT 与 PDF 的符号、图表、版式或上下文冲突，以 PDF 为准。

## 2. 项目历史

证据优先级：

1. 原始 user-assistant conversation / 原始用户上传指示词 / 原始 Conversation JSON；
2. 原始执行输出、源码、CSV、报告和可复现实验；
3. decision ledger / audit / recovery report；
4. stage summary / handoff；
5. model memory / inference。

不得用后期工件虚构共享对话中没有发生的正式回复或用户验收。

## 3. 当前身份与历史身份分离

- `current/` 决定“现在下一步该用什么”。
- `evidence/` 决定“这个事实/公式/来源由什么支持”。
- `history/` 说明“以前做过什么、为什么被保留/替代/否决”，并保存 pre-clean repository recovery pointer。

历史文件中的 `PASS/HOLD/READY` 不自动覆盖 `current/CURRENT_STATE.md`。

## 4. 原件保全

- 原始 PDF/TXT/JSON 一经登记，不静默覆盖；
- 可取得的本地原件记录 SHA-256、字节数和来源身份；
- GitHub 暂无二进制原件时，至少保留 File Library ID / 文件名 / SHA（若可得）/ DOI或URL；
- 新扫描版/新版本另存，不覆盖旧 SHA。

## 5. GitHub 文本身份

### BYTE_EXACT_ORIGINAL

只有按字节校验与登记 SHA 一致，才能这样标记。

### EFFECTIVE_SOURCE_EXCERPT

用于当前或历史理论的原始公式、参数、表格、试验路径、程序片段或关键论述。应记录来源及使用边界。

### FULL_TEXT_MIRROR / NORMALIZED_TEXT_COPY

聊天/connector UTF-8 复制可能改变 CRLF、Unicode、末尾换行或转义，因此只能作为检索镜像。迁移期建立的全文镜像已从当前 `main` 删除；若确需恢复，从 `history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md` 指向的 pre-clean commit 定点读取。

正常工作不应优先依赖这些旧镜像。

## 6. 原始信息优先

此前上传过的 PDF、TXT/prompt/instruction、JSON、CSV ledger、execution/gate/rollback/response、source registry、equation-to-code registry、raw conversation export，应优先保存原件或至少保存可靠 locator。

文献 PDF 不要求整篇文本继续复制进 GitHub；只要原件 locator 完整，且项目实际使用的有效部分有可审计证据，即满足恢复要求。

## 7. 结构试验不得反标材料

Case21、Swartz24、UCFT 构件承载力不得用于反标普通混凝土、UHPC、钢筋或钢壳材料参数。材料 operator 的参数与形式只能由材料级来源确定/验证；结构试验只用于结构层验证。