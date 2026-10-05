# UCFT 单参数当前路径：按宽厚比由大到小逐件计算监控

- 开始时间：2026-10-05 12:08 +08:00
- 分支：`diagnostic/20261004-analytic-ninecurve-attempt`
- 顺序：BH100 gate → BH085 → BH070 → BH060 → BH050 → BH032 → BH020 → BH010 → BH005
- 当前 numerical path：ABS/raw UC141 damage + ABS/raw plastic；每个 w 独立；FEM/试验不参与求根。
- **2026-10-05 审计状态：BH085–BH050 全部降级为 PROVISIONAL/QUARANTINED，暂停继续 BH032。**

## 状态
- [x] BH100 gate（仅 total-load numerical gate；不能作为分项正确性的充分验证）
- [x] BH085（PROVISIONAL）
- [x] BH070（PROVISIONAL）
- [x] BH060（PROVISIONAL）
- [x] BH050（PROVISIONAL）
- [ ] BH032 — PAUSED BY AUDIT
- [ ] BH020
- [ ] BH010
- [ ] BH005

## 已冻结但待复核结果
- BH100 gate: P(82)=13.3961 MN。
- BH085: wu=66.3600852 mm, Pu=11.41091 MN。
- BH070: wu=49.3888169 mm, Pu=9.51798 MN。
- BH060: wu=35.2080233 mm, Pu=8.43835 MN。
- BH050: wu=20.5328714 mm, Pu=7.59054 MN。

## 审计结论
1. 高层公式口径确实沿用了 BH100 的 ABS/raw current route；
2. 但 raw tension damage 被 positive principal total strain 触发，会把单轴压缩的 Poisson 横向伸长误判为 tensile cracking，且 b 越小越严重；
3. BH100 总峰值接近 DIRECT 可能是 UHPC 偏低与 steel 偏高的抵消，不能继续把总荷载单点当作系列 gate；
4. BH085→BH050 的 nq 数值求积收敛误差极小，不是低值原因，但不符合最终“连续显式 production”要求；
5. BH100 steel Mises 逐项 evaluator 未随结果代码备份，因此 exact implementation identity 尚未证明。

详见 `AUDIT_BH085_BH050_LOW_BIAS.md`。
