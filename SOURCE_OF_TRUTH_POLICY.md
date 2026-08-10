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

## 4. GitHub 文本副本的完整性身份

必须区分两类：

### A. BYTE_EXACT_ORIGINAL

只有当 GitHub 文件按字节校验与登记原件 SHA-256 一致时，才允许标记为 `BYTE_EXACT_ORIGINAL`。

### B. FULL_TEXT_MIRROR / NORMALIZED_TEXT_COPY

通过聊天/connector UTF-8 文本接口复制的 TXT/MD/CSV，即使内容完整，也可能因：
- CRLF/LF；
- 末尾换行；
- Unicode normalisation；
- 工具转义；

导致字节 SHA 与原件不同。因此默认身份只能是 `FULL_TEXT_MIRROR` 或 `NORMALIZED_TEXT_COPY`，不能覆盖原始 SHA。

原始 SHA-256 和 File Library locator 永远保留在 inventory/registry 中。若未来获得正常 file-upload/git-push 通道，应将真正原件另存到 `raw_original/` 或 `sources/`，并完成 SHA 校验。

## 5. PDF 文本镜像

`sources_text/` 下的 TXT 是从 PDF 机械提取的检索镜像，不是 GPT 摘要，也不具有高于 PDF 的证据等级。

## 6. 原始信息优先原则

对任何此前上传过的：
- PDF；
- TXT / prompt / instruction；
- JSON；
- CSV ledger；
- execution / gate / rollback / response file；
- source registry / equation-to-code registry；
- raw conversation export；

优先目标是保存原件或 byte-exact copy。当前工具不能直接复制原件时，至少保存**精确文件名 + File Library ID + 原始 SHA（若可得）+ 外部来源 URL（若有）+ 历史角色 + 当前复制状态**。禁止只留下 GPT 摘要。

## 7. 结构试验不得反标材料

Case21、Swartz24、UCFT 构件承载力不得用于反标普通混凝土、UHPC、钢筋或钢壳材料参数。新材料 operator 只能由材料级文献/试验确定或验证。
