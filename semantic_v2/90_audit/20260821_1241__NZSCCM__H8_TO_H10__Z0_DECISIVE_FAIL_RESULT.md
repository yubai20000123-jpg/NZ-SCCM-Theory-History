# NZ-SCCM — H8→H10 Z0 决定性失败结果

时间：2026-08-21

## 1. 前置身份

本结果使用已经在 H10 结果出现以前冻结的 `H8_TO_H10__PREFROZEN_NO_EXPERIMENT_GATE`：

- δP ≤ 0.5%
- δD ≤ 0.5%
- δw ≤ 1.0%
- δε ≤ 2.0%
- same origin-connected branch
- audit-localizer marginal peak-load refinement < 0.05%

NC-M6、钢面、web、多相组装和 H2N 母空间均未修改。direct-current quadrature 仅为 AUDIT/DECIMAL LOCALIZER。

## 2. 支路身份检查

H10 不能从高荷载 H8 嵌入态直接认根。为防止选到 disconnected root，本轮从

`D=0, q=0, eta=0, all H10 membrane coefficients=0`

开始，逐级连续追踪 origin-connected H10 equilibrium branch。

24×24×12 localizer 下，origin branch 在 D=0.34 仍严格闭合：

- D = 0.340000
- P ≈ 17.963236 MN
- q ≈ 0.0007109
- eta ≈ 0.0690153

随后用伪弧长继续穿过 D-fold，不用固定 D 强行扫根。

## 3. H10 第一可达极限点

24×24×12 localizer：

- sampled first load maximum around P ≈ 18.4397 MN
- local quadratic estimate ≈ 18.4409 MN

28×28×14 localizer：

- first local maximum bracket around D ≈ 0.3530
- local quadratic peak estimate ≈ 18.42567 MN

32×32×16 localizer：

- D values around first fold: 0.3526651, 0.3530169, 0.3530958
- P values: 18.4153915, 18.4229697, 18.4199195 MN
- local quadratic estimate:
  P_u,H10 ≈ 18.42321 MN

28→32 marginal change:

|18.42567-18.42321|/18.42321 ≈ 0.0133% < 0.05%.

因此 audit-localizer independence gate 通过。

## 4. H8 无需完整峰值即可决定性拒绝

32×32×16 H8 origin-connected continuation 在

- D ≈ 0.880338
- P_H8 ≈ 31.318110 MN

时仍然沿同一 equilibrium branch 上升。因此

P_u,H8 > 31.318110 MN.

按预冻结定义

δP = |P10-P8|/|P10|,

故仅用 H8 的严格下界就有

δP > (31.318110-18.423211)/18.423211 ≈ 69.99%.

这远高于 0.5%，不需要继续耗费成本寻找 H8 的精确后续峰值，也不需要计算 δD/δw/δε 才能改变裁决。

## 5. 裁决

`H8_GLOBAL_PRODUCTION_FREEZE = NO`

`H8_REJECTION = DECISIVE_BY_Z0_DELTA_P`

`H10 = NEXT_MINIMUM_CANDIDATE`

按预冻结 fail-fast 规则，Z1–Z5 和 Swartz24 的 H8→H10 全批在本节点不再执行，因为任何结果都不能撤销 H8 全局拒绝。

## 6. 物理/数学警告

H10 新增高阶膜内 Ritz 自由度后，Z0 origin-connected branch 出现远早于 H8 的 limit/fold。该现象不能事先解释成“更准确”或“数值坏根”；下一步必须用同样预冻结 gate 做 H10→H12，判断是正常 Ritz 收敛、还是 NC-M6 softening + 高阶膜内自由度导致的谱局部化/缺乏长度尺度问题。
