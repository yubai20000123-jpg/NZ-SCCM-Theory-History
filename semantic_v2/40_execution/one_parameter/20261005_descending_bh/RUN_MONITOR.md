# UCFT 单参数当前路径：按宽厚比由大到小逐件计算监控

- 开始时间：2026-10-05 12:08 +08:00
- 分支：`diagnostic/20261004-analytic-ninecurve-attempt`
- 顺序：BH100 gate → BH085 → BH070 → BH060 → BH050 → BH032 → BH020 → BH010 → BH005
- 每个 (w) 独立 current-state 求值；FEM/试验不参与求根。
- 停止规则：只在一个试件完整冻结并提交后停止，不留下半个试件的未记录状态。

## 执行口径
本轮固定为产生 BH100 约 13.40 MN 曲线的 **ABS/raw UC141 damage + ABS/raw plastic** current path。

## 状态
- [x] BH100：当前路径回归门复核
- [x] BH085
- [x] BH070
- [ ] BH060
- [ ] BH050
- [ ] BH032
- [ ] BH020
- [ ] BH010
- [ ] BH005

## 已冻结结果
- BH100 gate: (P(82)=13.3961) MN；保存曲线峰值约 13.40 MN。
- BH085: (w_u=66.3600852) mm，(P_u=11.41091) MN。
- BH070: (w_u=49.3888169) mm，(P_u=9.51798) MN。

BH085、BH070 均表现为：TOP 已进入 Mises corrector，曲线继续上升，直到 BOTTOM elastic predictor 首次触及 355 MPa；该真实根处形成 cusp-type maximum，随后 BOTTOM corrector 激活并进入下降段。

## 日志
1. 初始化监控并冻结 current numerical path。
2. BH085 完成并提交。
3. BH070 完成：(w=0sim90) mm coarse scan、45–52 mm 加密、BOTTOM-yield 根和 nq 收敛检查完成并提交。
4. 下一步：BH060。
