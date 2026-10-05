# UCFT 单参数当前路径：按宽厚比由大到小逐件计算监控

- 开始时间：2026-10-05 12:08 +08:00
- 分支：`diagnostic/20261004-analytic-ninecurve-attempt`
- 顺序：BH100 gate → BH085 → BH070 → BH060 → BH050 → BH032 → BH020 → BH010 → BH005
- 当前 numerical path：ABS/raw UC141 damage + ABS/raw plastic；每个 (w) 独立；FEM/试验不参与求根。
- 停止规则：仅在一个试件完整冻结并提交后停止。

## 状态
- [x] BH100 gate
- [x] BH085
- [x] BH070
- [x] BH060
- [ ] BH050
- [ ] BH032
- [ ] BH020
- [ ] BH010
- [ ] BH005

## 已冻结结果
- BH100 gate: (P(82)=13.3961) MN。
- BH085: (w_u=66.3600852) mm, (P_u=11.41091) MN。
- BH070: (w_u=49.3888169) mm, (P_u=9.51798) MN。
- BH060: (w_u=35.2080233) mm, (P_u=8.43835) MN。

当前 BH085/BH070/BH060 的峰值机制一致：TOP 先进入 corrector；总荷载继续上升到 BOTTOM elastic predictor 首次触及 355 MPa 的真实根；BOTTOM corrector 激活后立即转入下降支。

## 日志
1. BH100 gate 复核并记录 formal-vs-execution 口径差异。
2. BH085 完成并提交。
3. BH070 完成并提交。
4. BH060 完成：(w=0sim80) mm coarse scan、35–36 mm BOTTOM-yield 根、nq=80/100/120/160 收敛检查完成。
5. 下一步：BH050。
