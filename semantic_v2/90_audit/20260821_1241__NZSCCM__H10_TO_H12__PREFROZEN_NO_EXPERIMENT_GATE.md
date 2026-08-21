# NZ-SCCM — H10→H12 无试验值连续阶收敛门禁（结果前冻结）

时间：2026-08-21

H10 已因 Z0 的 H8→H10 决定性差异成为下一最低候选。本文件在任何 H12 结果出现以前冻结 H10→H12 门禁。

## 冻结边界

- NC-M6 FROZEN；禁止 M7、经验系数和试验反标。
- H10=N=5；H12=N=6；同一 nested H2N displacement family。
- ONE_CONTINUOUS_COMPLETE_HALFWAVE。
- 正式空间 sampling/quadrature/material points = 0；direct-current quadrature only AUDIT/DECIMAL LOCALIZER。
- 试验 failure load、Zhou/Winter comparator 不得参与求根、选支、阶次、门槛或容差。

## Acceptance gate

与此前各连续阶完全相同：

- δP(H10,H12) ≤ 0.5%
- δD ≤ 0.5%
- δw ≤ 1.0%
- δε ≤ 2.0%
- same origin-connected physical branch
- audit-localizer marginal peak-load refinement < 0.05%

任何决定性失败即可 `H10_GLOBAL_PRODUCTION_FREEZE=NO` 并 fail-fast。

要判 `H10_GLOBAL_PRODUCTION_FREEZE=YES`，必须完成当前要求的全部结构族；单个代表算例通过不够。

## 执行顺序

1. Z0 H10→H12 first；
2. 若 Z0 决定性失败，立即拒绝 H10，并在任何 H14 结果以前预冻结 H12→H14；
3. 若 Z0 通过，再继续 Z1–Z5；
4. Z0–Z5 全部通过后才进行 Swartz24 H10→H12 全批。

鉴于 H8→H10 暴露出可能的高阶膜内谱局部化，本次必须额外记录：

- 新增 H12 ring 的 coefficient norm / strain-weighted norm；
- H10 状态嵌入 H12 后的 tail residual；
- first reachable limit point 的 origin-connectivity；
- limit point 是否随 N 单调向低载移动。

这些诊断不能改变 acceptance thresholds，也不能替代真实 H12 解。
