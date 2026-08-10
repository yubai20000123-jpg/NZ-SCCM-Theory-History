# UHPC PDF extracted-text mirrors

本目录保存的是**从用户已上传 UHPC PDF 机械提取的可检索文本镜像**，不是 GPT 摘要，也不是高于 PDF 的原始证据。

证据优先级始终为：

`原始 PDF > 本目录 extracted text > evidence note / project interpretation`。

若公式、图表、上下标、符号或分页与 PDF 冲突，以 PDF 为准。

## 当前本地 PDF 文本镜像迁移状态

| source | authoritative PDF | PDF SHA-256 | extracted TXT SHA-256 | GitHub status/layout |
|---|---|---|---|---|
| 周俊 | `UHPC三轴受压力学性能研究_周俊.pdf` | `37531c8f73765fea9192bef094a88edd7d7eacc5756b51640a7353b65ed72e59` | `dad0fe2521e0d79a037dac540d4d75603a45c2d723b98a86a1da57706b671097` | **FULL_TEXT_MIRROR_MIGRATED**: `周俊_UHPC三轴受压力学性能研究/part_01.txt` … `part_06.txt` |
| 王淑楠 | `超高性能混凝土三轴受压力学性能及破坏准则_王淑楠.pdf` | `e6e24cf47b21b1faa09f13ceb97a599321283c154578da92ef844b5d8e5c27dd` | `5f962ddbbfe307c25e1514b9b521b690a2ad55c04d84e98116e370d97f6b3139` | **FULL_TEXT_MIRROR_MIGRATED**: `王淑楠_超高性能混凝土三轴受压力学性能及破坏准则/part_01.txt` … `part_04.txt` |
| 胡文旭 | `钢-预制UHPC开孔板组合桥面板界面抗剪性能研究_胡文旭.pdf` | `a554649f440bdb5d6523dc174aab68e1128aa6e4f9d19ebb9b67a9e19b544909` | `cfd0ed0378554f57e3e58373ca10eb619aa772ab5f1c44da53e44c248b8bbf13` | **PARTIAL_TEXT_MIRROR_MIGRATION 2/10**: `part_01.txt`, `part_02.txt` 已迁；`part_03..10` 待下一批 |

## 分块规则

分块只是 GitHub connector 文本写入与后续检索的工程处理：按原提取文本顺序在换行边界附近切分，不改写正文，不重新总结。重组顺序严格按 `part_01 -> part_02 -> ...`。

全文镜像的完整性应按以下两层检查：

1. 所有顺序块重组后的文本 SHA-256 必须等于上表 `extracted TXT SHA-256`；
2. extracted TXT 仍然只是一种检索镜像，最终文献事实以 authoritative PDF SHA 对应的 PDF 原件为准。

## 重要边界

- 周俊文本镜像已经可从 GitHub 全文检索，但若需要核对图、公式排版、上下标或原始页码，仍必须回到 `UHPC三轴受压力学性能研究_周俊.pdf`。
- 王淑楠文本镜像已经迁入 4 个顺序块；其 W-W 五参数破坏面、围压/纤维参数试验与三轴全过程内容可以通过 GitHub 文本搜索定位，但公式排版仍以 PDF 为准。
- 胡文旭当前只迁入前 2/10 块，因此在 `PARTIAL` 状态下不得把 GitHub 文本搜索无命中解释为“论文没有该内容”。剩余 8 块完成并通过重组 SHA 后才能标记 `FULL_TEXT_MIRROR_MIGRATED`。
- Hiew、Liu、Lee、Leutbecher 等目前以 File Library ID + bibliographic/public-source locator 为主，不能因尚未迁入全文镜像而从 UHPC 来源链中省略。
