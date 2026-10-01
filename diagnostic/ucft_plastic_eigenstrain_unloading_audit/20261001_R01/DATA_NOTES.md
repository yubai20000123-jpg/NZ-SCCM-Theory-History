# 轻量版数据范围

本册用于读取和讨论已有 BH050 / BH032 卸载审计结果，不是全积分点原始数据的完整替代品。完整 Excel、CSV、ODB 保留不动。

保留内容：两件汇总结论和材料参数；所有候选点的 500 个相邻增量按帧汇总；每个真正卸载点的刚度统计；原来选定的每件 7 个代表点的全部 501 帧、500 个相邻增量和附近 UHPC 同步状态；全部配对事件时序；全荷载历史；PRE95/PEAK/POST95 空间分类计数。

减小体量的方法：不嵌入图片；不重复存储百万行候选点原始历史；不在本册重复存储几十万行逐点空间坐标/基向量；代表点只保留本轮卸载判别所需的核心列。没有对保留的代表点历史跳帧，也没有重新计算或改动 FEM 结果。

`AllCandidateFrameStats` 来自全部原始候选增量，不是用代表点推估全体。它保留全部帧；汇总 metrics 的时间窗则从上升支首次达到 85%Pu 开始（BH050 frame_end≥179；BH032 frame_end≥201）。仅在该时间窗内累加每帧计数后与原诊断 metrics 对齐，已独立核对。`AllUnloadingPoints` 覆盖该审计时间窗的所有确认卸载点。代表点表不能用来计算全体卸载比例；空间计数不能当作面积比例。全帧统计中的 d_s 分位数只针对原来 qualified 的卸载增量，空集合保持空白。

应力 MPa，位移 mm，时间 s，荷载 N，汇总 Pu 为 MN。应变和比例无量纲。钢壳轴向为映射后的物理 y；全局加载轴为 Z。ODB LE12/PE12 已是 engineering shear，不再乘 2。空值代表缺失或不适用，尤其 PEQC 不存在、A/V 仅 21/501 帧实际提供；未补造缺失值。真正卸载段的 d_s 原始负值保留。

钢壳原始坐标/应变基、UHPC 泊松修正版本、当前硬化屈服面和空间连续性标志仍可核查。所有分类沿用已完成审计；不拟合 damage law，不修改 production，不重新提交计算。

推荐先读取 Summary / ConclusionAnswers，再用 AllCandidateFrameStats 和 AllUnloadingPoints 判断整体规律，最后用 SteelPointHistory / SteelIncrementHistory / UHPCSteelHistory 核查代表点连续路径。需要任意其他材料点的完整历史时，再从保留的完整源数据按 element/IP/SP 定向提取。
