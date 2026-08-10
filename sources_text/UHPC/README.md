# UHPC PDF extracted-text mirrors

本目录保存的是**从用户已上传 UHPC PDF 机械提取的可检索文本镜像**，不是 GPT 摘要，也不是高于 PDF 的原始证据。

证据优先级始终为：

`原始 PDF > 本目录 extracted text > evidence note / project interpretation`。

若公式、图表、上下标、符号或分页与 PDF 冲突，以 PDF 为准。

## 当前三份本地 PDF 文本镜像

| source | authoritative PDF | PDF SHA-256 | extracted TXT SHA-256 | GitHub status/layout |
|---|---|---|---|---|
| 周俊 | `UHPC三轴受压力学性能研究_周俊.pdf` | `37531c8f73765fea9192bef094a88edd7d7eacc5756b51640a7353b65ed72e59` | `dad0fe2521e0d79a037dac540d4d75603a45c2d723b98a86a1da57706b671097` | **FULL_TEXT_MIRROR_MIGRATED**: `周俊_UHPC三轴受压力学性能研究/part_01.txt` … `part_06.txt` |
| 王淑楠 | `超高性能混凝土三轴受压力学性能及破坏准则_王淑楠.pdf` | `e6e24cf47b21b1faa09f13ceb97a599321283c154578da92ef844b5d8e5c27dd` | `5f962ddbbfe307c25e1514b9b521b690a2ad55c04d84e98116e370d97f6b3139` | PENDING_TEXT_MIRROR_MIGRATION |
| 胡文旭 | `钢-预制UHPC开孔板组合桥面板界面抗剪性能研究_胡文旭.pdf` | `a554649f440bdb5d6523dc174aab68e1128aa6e4f9d19ebb9b67a9e19b544909` | `cfd0ed0378554f57e3e58373ca10eb619aa772ab5f1c44da53e44c248b8bbf13` | PENDING_TEXT_MIRROR_MIGRATION |

## 分块规则

分块只是 GitHub connector 文本写入与后续检索的工程处理：按原提取文本顺序在换行边界附近切分，不改写正文，不重新总结。重组顺序严格按 `part_01 -> part_02 -> ...`。

### 周俊已迁移 chunk SHA-256

```text
part_01  a8d0ded9fc9564a2e727592706155510339c3e48e3a840634e2eb7982cf5200e
part_02  11f5712f1f2e142ab984e533ce30cbfbbb0477c1ab50770b4daafa0f731018f6
part_03  2f918d9c48e2446cbf7b38023652ba681344759e4ee20ebe4e259b4a7f70a1c9
part_04  50957ae64839435b7c342ef9a21c6673a04bbe2be0c925cfe79a1f33779fc020
part_05  18fc864f594f3e16eedfe2f29100cc06e0f40357083376e2a42b8055ec5f5be2
part_06  45d06c523b6f74f81bffc43c78a679ed7f5c81a06efcd9d9b1783c01a0485911
```

这些 chunk SHA 校验本地分块输入；PDF byte identity 仍由 PDF SHA 控制。GitHub contents API 会保存 UTF-8 文本，但 extracted text 本身不等于 PDF byte-exact original。

## 重要边界

- 周俊文本镜像已经可从 GitHub 全文检索，但若需要核对图、公式排版、上下标或原始页码，仍必须回到 `UHPC三轴受压力学性能研究_周俊.pdf`。
- 王淑楠、胡文旭原始 PDF 和 extracted-text SHA 已登记；其全文文本镜像将在后续批次继续迁移。
- Hiew、Liu、Lee、Leutbecher 等目前以 File Library ID + bibliographic/public-source locator 为主，不能因尚未迁入全文镜像而从 UHPC 来源链中省略。
