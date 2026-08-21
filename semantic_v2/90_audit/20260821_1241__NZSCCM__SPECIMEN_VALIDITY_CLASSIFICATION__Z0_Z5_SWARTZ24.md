# SUPERSEDED — NZ-SCCM Z0–Z5 / Swartz24 试件有效性分类

状态：`SUPERSEDED_BY_USER_CORRECTION_20260821_1311`

本文件原先采用 `A_STANDARD_TEST / B_PERTURBED_TEST / C_NONSTANDARD_TEST / V_VIRTUAL_BENCHMARK` 分类，并把实测/FE屈曲形态用于判断“标准破坏”。该口径已被用户明确否决，后续不得继续作为理论收敛或样本筛选入口。

## 被替代的原因

1. 对长宽比 `a/b=2` 的板，当前项目的理想理论基准固定为 **两个完整半波**。试验或某一 FE 后处理若表现为其他半波形式，只能作为实际试件/实现偏离理想状态的扰动证据，不能反向修改理论基准模态。
2. 钢壳混凝土 Z0–Z5 来源于理想化有限元建模，应作为确定性的理想状态基准；不应按物理试件随机性做 A/B/C 有效性降级。
3. 后续误差分析需分开：
   - 理想确定性基准误差（Z0–Z5）；
   - 物理试验误差（Swartz24），其中试件随机性作为试验实现层扰动，不参与理论模态选择。

新的正式入口见同目录：

`20260821_1311__NZSCCM__IDEAL_MODE_AND_VALIDATION_CLASSIFICATION__CORRECTED.md`

以及下一步规划：

`20260821_1311__NZSCCM__NEXT_PLAN_AFTER_IDEAL_MODE_CORRECTION.md`

本文件仅保留历史审计作用，不得再据此删除、降级或分组任何样本。