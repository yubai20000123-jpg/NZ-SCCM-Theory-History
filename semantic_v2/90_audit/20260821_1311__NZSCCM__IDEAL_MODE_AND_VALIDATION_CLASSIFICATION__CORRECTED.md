# NZ-SCCM — 理想模态与验证样本分类（用户修正版）

时间：2026-08-21 13:11 +08:00
状态：`CURRENT_CORRECTED_GOVERNANCE`

## 1. 最高原则

理论模态由几何、边界条件和理想稳定问题决定，不由试验中偶然出现的非理想破坏/屈曲形态决定。

对于 `a/b=2` 的四边简支轴压板，当前项目固定理想基准为：

`TWO_COMPLETE_HALFWAVES_ON_FULL_PANEL`。

等价的代表半波表达只有在完整证明重复/反对称延拓与全板运动学、材料和边界完全等价后才可使用：

`ONE_CONTINUOUS_COMPLETE_HALFWAVE = representative cell of the ideal two-halfwave full panel`。

不得把“一完整代表半波”误写成全长板只有一个半波。

## 2. Swartz24

当前输入几何统一为宽度 1220 mm、加载方向长度 2440 mm，因此 `a/b=2`。

故 Case1–Case24 的理想理论目标全部固定为：

`IDEAL_FULL_PANEL_MODE = TWO_COMPLETE_HALFWAVES`。

Nguyen/试验中对部分板记录的一完整/近似一半波形态，不获得理论模态身份；在本项目误差治理中仅属于 `SPECIMEN_REALIZATION_DEVIATION`，可用于解释试件随机散差，但不能：

- 修改理论半波数；
- 决定 Ritz 阶数；
- 决定是否剔除样本；
- 调整材料参数；
- 调整收敛阈值。

Swartz24 全部保留在最终试验验证集合中。

## 3. Z0–Z5 steel-shell concrete

Z0–Z5 是理想化有限元建模对象，因此归类为：

`IDEAL_DETERMINISTIC_FE_BENCHMARK`。

它们不存在“物理试件制造随机性”这一解释层。只要 FE 基准自身已经做过网格/求解收敛，其与解析理论之间的差异原则上只能归入：

- 理论模型系统简化；
- 理论结构空间截断；
- 材料模型差异；
- 边界/荷载定义差异；
- 数值实现错误或残余 FE 离散误差。

不得把 Z0–Z5 的误差解释为 specimen scatter。

对 modified AR2/SSSS Z 系列，同样固定全板两完整半波；当前 `ell=b, k=1, m=1` 只有在其被严格证明为 `a=2b, m*=2` 全板的一个代表半波后才可沿用。

## 4. 误差统计身份

### Z0–Z5

优先用于确定性理论误差诊断：

- 连续阶 Ritz 截断误差；
- 系统偏差；
- 参数趋势；
- 是否存在无规律的理论散差。

由于不存在 specimen randomness，Z 系列是判断“理论随机误差”最干净的基准族。

### Swartz24

用于真实试验验证：

`observed error = theory systematic error + theory residual error + specimen realization error + measurement error`。

但理论模态始终由理想几何问题确定。实际半波偏离只作为后验试件扰动解释变量，不作为删样条件。

## 5. 对现有收敛账本的影响

此前 H2→H4→H6→H8 数值结果不自动作废，但必须先通过 `FULL_AR2_TWO_HALFWAVE ↔ ONE_REPRESENTATIVE_HALFWAVE` 等价性审计，才能继续作为正式连续阶证据。

尤其 H8→H10 的 Z0 约 31+ MN → 18.42 MN 跳变，在该等价性和支路/模态身份审计完成以前，只保留为 `EXECUTED_WARNING_RESULT`，不得直接解释为已证明的材料软化谱局部化或 production rejection 的最终物理原因。

NC-M6 继续冻结；M7 继续禁止；不得使用 FE/试验荷载选择阶数或根。