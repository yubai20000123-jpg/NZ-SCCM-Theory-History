# UCFT BH050 / BH032 钢壳卸载与 UHPC 同步审计：GPT 阅读包

版本：20261001_R01，diagnostic。不是 production 理论、不是重新计算或拟合。

## 读取顺序

1. 先读 [DATA_NOTES.md](DATA_NOTES.md)，了解坐标、剪应变、时间窗、筛选与证据边界。
2. 读 [Summary](tables/Summary/Summary_001.csv) 和 [ConclusionAnswers](tables/ConclusionAnswers/ConclusionAnswers_001.csv)。
3. 用 [TABLE_INDEX.csv](TABLE_INDEX.csv) 查找需要的表格分块；每块不超过 500 行，重复表头。所有分块合并才能得到该表全部保留记录。
4. 整体统计读 `AllCandidateFrameStats`、`AxialDropClasses`、`AllUnloadingPoints`、`AllPairEventTiming`。
5. 连续路径读 `RepresentativePoints`、`SteelPointHistory`、`SteelIncrementHistory`、`UHPCSteelHistory`；通过 case / element / integration_point / section_point 与 frame 关联。UHPC 同步表使用 steel_element / steel_ip / steel_section_point。
6. 人工查看或下载 [轻量 Excel](UCFT_BH050_BH032_GPT_LIGHT_R01.xlsx)。它与 CSV 来自同一份已核验的数据计划，不需要从图像读取数值。

## 数据范围：请勿把精简包误当完整原始数据

- BH050、BH032 各 7 个既有代表材料点，保留全部 501 帧及 500 个相邻增量，不跳帧。
- 候选点共有 BH050 1,832 个、BH032 1,824 个。共 1,828,000 个原始相邻增量全部进入逐帧分类统计；没有用代表点推估全体。
- 完整百万行逐点历史及空间坐标未放入此包，原始 CSV、完整 Excel 和 ODB 在本地保留。当前上传不包含 CAE / INP / ODB，不包含几 GB 的全明细 Excel。
- 每件 501 帧，但 A/V 实际只在 21 帧可用；缺失值留空。PEQC 没有可用值，留空。不补造数据。
- 每帧分类统计涵盖整个时间轴。Summary 和事件/点级卸载统计的审计窗口从上升支首次达到 85%Pu 起：BH050 frame_end≥179，BH032 frame_end≥201。比较全帧计数总和与 Summary 前，必须先筛选该窗口。
- 比例的分母是候选点-帧增量；不是钢壳面积比例，不是独立统计样本概率。

## 本轮主要诊断结论

| 项目 | BH050 | BH032 |
|---|---:|---:|
| 当前加载端峰值 Pu / MN | 11.6301988844 | 10.4798601280 |
| 确认真弹性卸载增量数（审计窗） | 139848 | 122428 |
| 同帧邻单元支持的卸载增量 | 119815 | 108336 |
| 合格标量刚度增量 | 71484 | 50916 |
| 轴向明显降幅中真卸载占比 | 32.9225% | 34.1572% |
| 轴向明显降幅中仍塑化占比 | 51.4207% | 60.3339% |
| 合格卸载 d_s_raw 中位 | 4.4600207405e-7 | 1.0142317630e-7 |
| 原始 Cs 卸载增量残差中位 | 0.0004155177674 | 0.0003819865311 |
| steel damage 判定 | NOT_NEEDED | NOT_NEEDED |

限定结论：当前 FEM 的可靠真正卸载段支持原始弹性刚度 + J2 塑性历史；不能把轴向应力分量下降全部解释为弹性卸载，更不能据单点拟合值宣布钢材损伤。UHPC 非弹性增长部分先于钢壳卸载，但不具有普遍稳定的先后顺序；时间关联不是唯一因果证明。结构级广义本征应变投影未在本轮验证。

## 单位与约定

应力 MPa；位移/坐标 mm；时间 s；荷载 N（Summary Pu 用 MN）；应变、比例无量纲。全局 Z 是加载轴；壳物理 y 是映射后的局部轴向。ODB LE12 / PE12 是 engineering shear，不再乘 2。d_s_raw 的负值和高残差项保留；非真卸载的 d_s 留空，不伪填零。

## 完整性

轻量 Excel 的所有保存值、数值/布尔类型、行数、公式缓存及 ZIP CRC 已独立核验；全部候选增量聚合与原诊断 metrics 在同一审计窗口匹配。

- [EXCEL_VALIDATION.json](EXCEL_VALIDATION.json)：逐表完整保存值验证。
- [AGGREGATION_VALIDATION.json](AGGREGATION_VALIDATION.json)：全部原始增量的聚合校验。
- [FILE_MANIFEST.json](FILE_MANIFEST.json)：文件大小与 SHA256；清单自身不包含在哈希列表中。

建议给 GPT 的指令：先读取本目录 README、DATA_NOTES、Summary、ConclusionAnswers 与 TABLE_INDEX，再根据问题逐块读取需要的 CSV。不得把未读取的完整数据宣称已读取；不得用代表点比例代替全候选统计；不得跳过空值和筛选限定。
