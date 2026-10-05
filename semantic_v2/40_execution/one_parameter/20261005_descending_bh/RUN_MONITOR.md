# UCFT 单参数当前路径：按宽厚比由大到小逐件计算监控

- 开始时间：2026-10-05 12:08 +08:00
- 分支：`diagnostic/20261004-analytic-ninecurve-attempt`
- 顺序：BH100 gate → BH085 → BH070 → BH060 → BH050 → BH032 → BH020 → BH010 → BH005
- 每个 (w) 独立 current-state 求值；FEM/试验不参与求根。
- 停止规则：只在一个试件完整冻结并提交后停止，不留下半个试件的未记录状态。

## 执行口径
当前约 13.40 MN 的 BH100 曲线来自 **ABS/raw UC141 damage + ABS/raw plastic**。本轮剩余 BH 试件全部保持这一 numerical path；formal peak-rebased 与 execution ABS/raw 的差异另行治理，不在系列中途切换。

## 状态
- [x] BH100：当前路径回归门复核
- [x] BH085：完整曲线 + 峰值冻结
- [ ] BH070
- [ ] BH060
- [ ] BH050
- [ ] BH032
- [ ] BH020
- [ ] BH010
- [ ] BH005

## 已冻结结果
- BH100 gate: (P(82)=13.3961) MN；旧保存曲线峰值约 13.40 MN。
- BH085: (w_u=66.3600852) mm，(P_u=11.41091) MN；峰值由 BOTTOM predictor 首次达到 355 MPa 的真实根形成，峰后直接下降。

## 日志
1. 初始化监控。
2. 复核并冻结 current numerical path；记录 formal-rebase / actual-ABS 差异。
3. BH085 完整执行完成：coarse (w=0sim105) mm，峰区 (56sim70) mm 加密，BOTTOM-yield 根求解及 nq=80/100/120/160 收敛检查完成。
4. 下一步：BH070；完成并提交后才进入 BH060。
