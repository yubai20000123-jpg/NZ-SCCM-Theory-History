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
- [x] BH050
- [ ] BH032
- [ ] BH020
- [ ] BH010
- [ ] BH005

## 已冻结结果
- BH100 gate: (P(82)=13.3961) MN。
- BH085: (w_u=66.3600852) mm, (P_u=11.41091) MN。
- BH070: (w_u=49.3888169) mm, (P_u=9.51798) MN。
- BH060: (w_u=35.2080233) mm, (P_u=8.43835) MN。
- BH050: (w_u=20.5328714) mm, (P_u=7.59054) MN。

BH085→BH050 目前均由 BOTTOM elastic predictor 首次触及 (f_y) 的真实根形成曲线峰值。

## 日志
1. BH100 gate 复核并冻结 ABS/raw current path。
2. BH085 完成并提交。
3. BH070 完成并提交。
4. BH060 完成并提交。
5. BH050 完成：全曲线 coarse scan、20–21 mm BOTTOM-yield 根、nq=80/100/120/160 convergence 完成。
6. 下一步：BH032。
