# SOURCE OF TRUTH POLICY

## 1. 文献事实

证据优先级：

1. 原始 PDF / 正式出版物 / 规范原文；
2. 由原始 PDF 机械提取的 TXT（仅检索镜像）；
3. evidence note / 公式摘录；
4. 项目理论解释；
5. 阶段总结 / handoff / model memory。

若 TXT 与 PDF 版式、公式或图表冲突，以 PDF 为准。

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

## 4. GitHub 中的文本镜像

`sources_text/` 下的 TXT 是从 PDF 机械提取的检索镜像，不是 GPT 摘要，也不具有高于 PDF 的证据等级。

## 5. 结构试验不得反标材料

Case21、Swartz24、UCFT 构件承载力不得用于反标普通混凝土、UHPC、钢筋或钢壳材料参数。新材料 operator 只能由材料级文献/试验确定或验证。
