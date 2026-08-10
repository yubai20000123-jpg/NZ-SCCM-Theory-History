# UHPC PDF extracted-text mirrors

本目录保存的是**从用户已上传 UHPC PDF 机械提取的可检索文本镜像**，不是 GPT 摘要，也不是高于 PDF 的原始证据。

证据优先级始终为：

`原始 PDF > 本目录 extracted text > evidence note / project interpretation`。

若公式、图表、上下标、符号或分页与 PDF 冲突，以 PDF 为准。

## 当前三份本地 PDF 文本镜像

| source | authoritative PDF | PDF SHA-256 | extracted TXT SHA-256 | GitHub layout |
|---|---|---|---|---|
| 周俊 | `UHPC三轴受压力学性能研究_周俊.pdf` | `37531c8f73765fea9192bef094a88edd7d7eacc5756b51640a7353b65ed72e59` | `dad0fe2521e0d79a037dac540d4d75603a45c2d723b98a86a1da57706b671097` | `周俊_UHPC三轴受压力学性能研究/part_01.txt`, `part_02.txt` |
| 王淑楠 | `超高性能混凝土三轴受压力学性能及破坏准则_王淑楠.pdf` | `e6e24cf47b21b1faa09f13ceb97a599321283c154578da92ef844b5d8e5c27dd` | `5f962ddbbfe307c25e1514b9b521b690a2ad55c04d84e98116e370d97f6b3139` | `王淑楠_超高性能混凝土三轴受压力学性能及破坏准则/part_01.txt`, `part_02.txt` |
| 胡文旭 | `钢-预制UHPC开孔板组合桥面板界面抗剪性能研究_胡文旭.pdf` | `a554649f440bdb5d6523dc174aab68e1128aa6e4f9d19ebb9b67a9e19b544909` | `cfd0ed0378554f57e3e58373ca10eb619aa772ab5f1c44da53e44c248b8bbf13` | `胡文旭_钢-预制UHPC开孔板组合桥面板界面抗剪性能研究/part_01..03.txt` |

## 分块规则

分块只是 GitHub connector 文本写入与后续检索的工程处理：按原提取文本顺序在换行边界附近切分，不改写正文，不重新总结。重组顺序严格按 `part_01 -> part_02 -> ...`。

### chunk SHA-256

```text
ZHOU part_01  2aa62f24253baab209135c16bff8a722a20b1b080436df630f91a83aca6b9a69
ZHOU part_02  8d07e5373937710058a898b17c37284cb6a4507bffe1d763969f034ffd269083
WANG part_01  5a539f0316c3843b5dd666ec5b162d5c00dc429f6637b151cc5b7301668b2ee8
WANG part_02  b09eeafcbf9c352026ca308b991b022cdaa5890a2aa335467006c8284af05029
HU   part_01  d51205d10d92b55b4a0082ff8f6d0511d50ec8dd614bc0ced6e95f2e9c864bbd
HU   part_02  1cdbda4d9b0b47ce62c84ca3fc1002fd7c2181db4346e7fbe4ed50e4b16413a0
HU   part_03  b6cba3840bedec5674d6126d7b6720ab4b0cc9c1aa7db60f8ea907b8dde6ed64
```

这些 chunk SHA 只校验 GitHub 分块文本；PDF byte identity 仍由上表 PDF SHA 控制。
