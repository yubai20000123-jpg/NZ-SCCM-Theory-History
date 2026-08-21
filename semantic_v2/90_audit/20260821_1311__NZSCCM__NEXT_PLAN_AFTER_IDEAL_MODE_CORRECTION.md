# NZ-SCCM — 理想模态修正后的下一步规划

时间：2026-08-21 13:11 +08:00
状态：`CURRENT_NEXT_PLAN`

## 总体目标

在不改变 NC-M6、不引入 M7、不使用试验/FE荷载选阶的前提下，先保证所有连续阶比较都发生在同一个理想全板模态扇区，再继续 H2N 截断误差收敛；最后才进入确定性 FE 误差和物理试验误差分析。

## STEP 0 — 暂停继续机械升阶

当前 H10→H12 的预冻结门槛保留，但 H12 的已执行初步数值只作为工作痕迹，不立即做 production 裁决。

原因：H8→H10 在 Z0 上出现约 31+ MN → 18.42 MN 的巨大跳变。继续 H12/H14 以前必须先排除“代表半波与全板两半波并非完全等价”或“不同阶落入不同模态/支路扇区”的可能性。

## STEP 1 — FULL AR2 TWO-HALFWAVE ↔ ONE REPRESENTATIVE HALFWAVE 等价性证明

对 `a=2b`、四边简支、理想两完整半波，显式写出全板横向场，例如

w(x,y)=b(q0+q) sin(pi x/b) sin(2 pi y/a),  a=2b.

证明其在 y∈[0,b] 与 y∈[b,2b] 为符号相反但同幅的两个完整半波。

必须逐项证明：

1. w、转角、曲率在内部半波节点 y=b 的连续/兼容；
2. u,v 的 H2N 延拓在 y=b 保持位移连续与全板 essential BC；
3. von Karman 膜应变在两个半波之间的重复关系；
4. 弯曲应变符号翻转只造成对称截面上下表面对换，不改变全厚度积分后的总残量/荷载；
5. Swartz 配筋关于中面以及 Z 钢面/core/web 组装满足所需对称性；
6. 全板虚功、P、R、J 恰等于代表半波贡献的正确倍数，且未知量/约束无丢失。

PASS：可继续使用 ONE_CONTINUOUS_COMPLETE_HALFWAVE 作为理想 AR2 两半波的代表单元。

FAIL：此前所有基于单代表半波的 H2→H10 收敛结果降为非正式诊断；重建 full-a=2b 两半波母式后从最低必要阶重新算。

## STEP 2 — 模态/支路嵌套门禁

在等价性 PASS 后，对 H6/H8/H10 做不看 FE/试验的内部审计：

- H6 ⊂ H8 ⊂ H10 必须严格代数嵌套；
- 同一 q0、同一 out-of-plane two-halfwave sector；
- H8 嵌入 H10 后，旧坐标残量与 H8 解一致，新坐标残量只作为 tail forcing；
- 从 origin-connected branch 追踪，不以高荷载最近根替代；
- 对 fold 使用同一伪弧长/KKT极限定义；
- 不允许阶数变化同时改变 halfwave count、q0 或边界。

## STEP 3 — 专门复核 Z0 H8→H10 巨跳

只有 STEP 1–2 PASS 后，重新定位：

- H8 第一可达极限；
- H10 第一可达极限；
- H8→H10 bordered tail forcing；
- 新增 H10 ring 的应变加权幅值；
- 局部化宽度/高频能量占比。

判断：

A. 若 31+→18.4 MN 巨跳复现且分辨率独立，则 H8 确实不收敛；
B. 若巨跳消失，则旧 H8→H10 rejection superseded，原因记录为模态/支路/代表半波实现错误；
C. 若连续阶出现持续向更窄区域集中，则进入 softening-well-posedness 诊断，而不是无限机械加 H12/H14。

## STEP 4 — 恢复连续阶收敛

若 H10 仍是下一候选：完成 H10→H12，门槛不变：

- delta_P ≤ 0.5%
- delta_D ≤ 0.5%
- delta_w ≤ 1.0%
- delta_epsilon ≤ 2.0%
- same ideal mode / same origin branch
- audit localizer marginal peak-load change <0.05%

若决定性失败：在任何 H14 结果之前先冻结 H12→H14 gate。

## STEP 5 — 理想确定性 FE 基准误差（Z0–Z5）

仅在结构阶数冻结后打开 Z0–Z5 FE 极限承载力：

- 逐一 signed error；
- mean systematic bias；
- detrended residual scatter；
- 与 b/t、材料强度、钢面/核心比例等物理参数的趋势。

Z 系列不允许 specimen scatter 解释。若误差大但稳定同号/同趋势，可归入明确系统简化；若无规律正负跳动，production theory 不通过。

FE 结果不得回用于选 N、选根、调材料或改门槛。

## STEP 6 — Swartz24 真实试验误差

所有 Case1–24 以理想 a/b=2 两完整半波理论预测，不按实测半波删样或改模态。

最终同时报告：

- 全24 signed error；
- systematic bias；
- residual scatter/MAD；
- `observed mode = ideal two-halfwave` 与 `observed mode deviates from ideal` 仅作为后验扰动标签，用于解释 specimen realization scatter，不用于剔除。

## 当前唯一下一任务

`STEP 1: FULL_AR2_TWO_HALFWAVE_TO_ONE_REPRESENTATIVE_HALFWAVE_EQUIVALENCE_AUDIT`

在该门禁完成前，不继续把 H12/H14 数值升级为 production convergence conclusion。