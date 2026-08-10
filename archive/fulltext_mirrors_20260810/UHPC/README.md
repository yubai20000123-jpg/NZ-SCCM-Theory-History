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
| 胡文旭 | `钢-预制UHPC开孔板组合桥面板界面抗剪性能研究_胡文旭.pdf` | `a554649f440bdb5d6523dc174aab68e1128aa6e4f9d19ebb9b67a9e19b544909` | `cfd0ed0378554f57e3e58373ca10eb619aa772ab5f1c44da53e44c248b8bbf13` | **FULL_TEXT_MIRROR_MIGRATED 10/10**: `胡文旭_钢-预制UHPC开孔板组合桥面板界面抗剪性能研究/part_01.txt` … `part_10.txt` |

## 分块规则与完整性

分块只是 GitHub connector 文本写入与后续检索的工程处理：按原提取文本顺序在换行边界附近切分，不改写正文，不重新总结。重组顺序严格按 `part_01 -> part_02 -> ...`。

本地分块前已经验证胡文旭 10 个顺序块重组成原 extracted TXT 后：

```text
combined bytes = 215375
combined SHA-256 = cfd0ed0378554f57e3e58373ca10eb619aa772ab5f1c44da53e44c248b8bbf13
```

与上表原 extracted TXT SHA-256 严格一致。GitHub Contents API 保存 UTF-8 文本时可能产生表示层差异，因此这里的 SHA 是**本地机械提取全文及其分块重组**的完整性证明，不把 GitHub blob SHA 冒充 PDF 或 extracted TXT 的 SHA。

胡文旭本地 10 个分块的源 SHA-256：

```text
part_01  b6e5326b9b8d825cd5a760208708024e2e0aaf9f02fb3c6a45ab3ed248a6d913
part_02  d5cc96f66f391d87b9dfbaa00eeba879d31d5abfd21f7fb36bb4b17473aeae76
part_03  3bf0b49cd5855c705ed9a6dfea52fcd5d127a85b014d59e60aa6fe6f36e47827
part_04  9a5613f5b89c002131ecbf8db03b0c1ac787cbb3307857fef1578a4b5527c97e
part_05  6825cf41a27e098ab29d29fd73ff20daa75643dc9f13f02a1e59b5dccd6bd399
part_06  ec8e1f71784afacb34dcb25022f84b172a511f75b96f863200d30a9aea3cacb3
part_07  1c52390673758d5363ebff37df27f61d737c67221871a056d52b3e5528007cf9
part_08  48688af900f04087d4023aaa053153e4c2f01a78b81cbc54f417bd714189e97b
part_09  06e2ed806e8192742648274b87ab21d848c788ea3d472b5780a4a0e1373c8760
part_10  880289e91333bd511325699b03aa0e0bd1dbaf050ae9ecb0713f60cf7001d9d9
```

## 重要边界

- 周俊、王淑楠、胡文旭三份本地 UHPC PDF 都已经具有 GitHub 全文检索镜像。
- 全文镜像不能替代 PDF。需要核对图、公式排版、上下标、原始页码、表格结构时，必须回到对应 authoritative PDF SHA 所指向的原件。
- 胡文旭论文第 2 章包含本项目早期使用的 UHPC 单轴受压/受拉本构来源链，但该论文的主研究对象是钢-预制 UHPC 组合桥面板界面抗剪；其材料曲线的来源角色不得被夸大为完整 UHPC 多轴本构。
- Hiew、Liu、Lee、Leutbecher 等目前以 File Library ID + bibliographic/public-source locator 为主，不能因尚未迁入全文镜像而从 UHPC 来源链中省略。
