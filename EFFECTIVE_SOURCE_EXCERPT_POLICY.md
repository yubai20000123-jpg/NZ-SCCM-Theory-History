# EFFECTIVE SOURCE EXCERPT POLICY

**Effective date:** 2026-08-10

本仓库从本日开始停止“为了全文可搜索而迁移整篇/整本 PDF 文本”的做法。后续文献归档只保留**对当前或历史理论具有明确证据价值的有效部分**，并继续用原 PDF 的文件名、SHA-256、File Library ID、DOI/出版社/公开来源 URL 作为完整原文回溯入口。

## 1. 不再执行的工作

- 不再为了档案完整性把整篇 PDF 机械提取后逐块上传；
- 不再追求每篇文献的全文 GitHub searchable mirror；
- 不再把“全文迁移百分比”作为项目进度指标；
- 不再继续 Nguyen Appendix B 全量 8 块、孙立鹏全文约 59 块、Nguyen 非核心章节约 26 块等纯全文迁移任务，除非后续某一具体理论问题确实需要其中内容。

已经上传的全文镜像不删除，保留为历史检索资产。

## 2. 什么叫“有效部分”

只有满足至少一项时才进入 GitHub 文本层：

1. 当前正式理论直接采用、改写或需要审计的原始公式/定义；
2. 决定材料参数、状态边界、破坏准则、一致切线、峰值/峰后关系的原始数据或方程；
3. 决定稳定骨架、运动学、边界条件、局部/整体耦合、虚功/残量/Jacobian 的原始推导；
4. Case21 / Swartz24 / UCFT 算例输入、试验值、比较基准或来源解释；
5. 能证明某历史路线为何采用、废止、降级或未闭合的原始文字/代码/响应；
6. 对后续 UHPC、NC、rebar、steel-shell/Y operator 设计具有可复用价值的公式、表格或试验路径；
7. 未来新对话若缺少该片段，可能导致错误恢复、错误归因或旧路线复活。

仅有背景综述、一般性文献回顾、与本项目无直接关系的章节，不默认迁移。

## 3. 每个有效摘录必须保留的 provenance

每个摘录/公式包至少记录：

- authoritative PDF / source filename；
- PDF/source SHA-256（若可得）；
- File Library ID 或其他恢复 locator；
- PDF 页码或冻结机械提取文本的行号范围；
- extraction method；
- `SOURCE_ROLE`；
- `USED_FOR`；
- `NOT_USED_FOR`；
- 当前身份：CURRENT / RETAINED / SUPERSEDED / DIAGNOSTIC_ONLY / REJECTED / SOURCE_ONLY；
- 若为项目解释而非原文，必须单独标记 `PROJECT_INTERPRETATION`。

## 4. 原文与摘录的证据等级

`原始 PDF / 正式出版原文 > 有 provenance 的有效摘录 > 机械全文镜像 > evidence note > 项目总结`。

摘录用于快速恢复，不取代 PDF。遇到公式符号、图表、上下文歧义时必须回到原 PDF。

## 5. 推荐目录

后续优先使用：

```text
sources_excerpt/
  NC/
  UHPC/
  shell_Y/
  stability/
  experiments/
```

每个文献可以包含：

```text
README.md            # 来源身份与角色
formula_core.md       # 关键公式/定义
parameter_table.csv  # 关键材料/试验数据
validation_excerpt.md# 与本项目直接有关的验证段落
source_locator.md     # PDF/File ID/URL/SHA/页码
```

不要求每篇文献都有全部文件。

## 6. 已上传全文的处理

周俊、王淑楠、胡文旭、Attard、张宁、云露以及 Nguyen 已上传的章节镜像全部保留，不回删，不再继续为了“全文完整率”扩张。未来优先从这些全文镜像中提炼有效摘录；只有需要新证据时才再打开原 PDF/File Library。

## 7. 进度定义更新

今后的迁移完成条件是：

- 核心来源都已登记 locator；
- 当前理论需要的有效公式/参数/状态/试验数据已有 provenance 摘录；
- 历史关键转折已有原始对话/响应/报告证据；
- 新对话可以按任务恢复而不依赖本次长上下文。

不要求所有 PDF 全文上传。
