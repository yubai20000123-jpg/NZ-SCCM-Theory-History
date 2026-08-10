# EFFECTIVE SOURCE EXCERPT POLICY

**Effective date:** 2026-08-10

本仓库停止“为了全文可搜索而迁移整篇/整本 PDF 文本”的做法。后续文献归档只保留**对当前或历史理论具有明确证据价值的有效部分**，并用原 PDF 文件名、SHA-256、File Library ID、DOI/出版社/公开来源 URL 作为完整原文回溯入口。

## 1. 不再执行

- 不为档案完整性逐块上传整篇 PDF 提取文本；
- 不追求全文镜像百分比；
- 不把大段背景综述纳入默认工作区；
- 不因“来源存在”自动把历史经验公式/数值实现升格为当前理论。

此前建立的全文镜像已经从当前 `main` 移除，以免污染正常 GitHub 检索。它们仍可通过 `history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md` 指向的 pre-clean commit 在 Git 历史中恢复。

## 2. 有效部分的判定

满足至少一项才进入 `evidence/`：

1. 当前正式理论直接采用、改写或需要审计的公式/定义；
2. 决定材料参数、状态边界、破坏准则、一致切线、峰值/峰后关系的原始数据或方程；
3. 决定稳定骨架、运动学、边界条件、耦合、虚功/残量/Jacobian 的原始推导；
4. Case21 / Swartz24 / UCFT 的输入、试验值、比较基准或来源解释；
5. 能证明某路线为何采用、废止、降级或未闭合的原始文字/代码/响应；
6. 对 NC、UHPC、rebar、steel-shell/Y operator 设计可复用的公式、表格或试验路径；
7. 缺失后会导致错误恢复、错误归因或旧路线复活的证据。

## 3. 当前目录

```text
evidence/
  catalog/               # 文件名 / File ID / SHA / URL / inventory
  materials/
    NC/
    UHPC/
  steel_shell/
  stability/
```

每个来源包不要求统一模板，但至少应能回答：

- 来源是什么；
- 用于什么；
- 不用于什么；
- 当前理论是否采用；
- 需要回原文时去哪里找。

## 4. provenance 最低要求

有效摘录/公式包尽量记录：

- authoritative source filename；
- PDF/source SHA-256；
- File Library ID 或 DOI/URL；
- 页码或冻结提取文本行号；
- extraction method；
- `SOURCE_ROLE`；
- `USED_FOR`；
- `NOT_USED_FOR`；
- CURRENT / RETAINED / SUPERSEDED / DIAGNOSTIC_ONLY / REJECTED / SOURCE_ONLY 等身份。

项目解释不能伪装成原文。

## 5. 证据等级

`原始 PDF / 正式出版原文 > 有 provenance 的有效摘录 > Git 历史中的机械全文镜像 > evidence note > 项目总结`。

涉及符号、图表、精确数值或上下文歧义时必须回原 PDF。

## 6. 历史全文镜像的处理

周俊、王淑楠、胡文旭、Attard、张宁、云露以及 Nguyen 曾建立的全文/章节镜像没有丢失，但**不再存在于当前工作树**。如某个 effective excerpt 缺少必要上下文，应优先回原 PDF/File Library；只有原件暂时不可用时，才通过 `history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md` 从 Git 历史定点恢复旧镜像中的相关片段。

## 7. 完成条件

来源归档是否“完成”不看全文率，而看：

- 核心来源都有可靠 locator；
- 当前理论需要的公式/参数/状态/试验路径已保留有效证据；
- 历史关键转折能回到原始对话/工件；
- 新对话可以按任务恢复而不依赖上一段超长聊天上下文。