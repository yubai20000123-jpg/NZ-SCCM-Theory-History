# UCFT 单参数当前路径：按宽厚比由大到小逐件计算监控

- 开始时间：2026-10-05 12:08 +08:00
- 分支：`diagnostic/20261004-analytic-ninecurve-attempt`
- 目标：在已完成 BH100 当前路径后，严格按 BH085 → BH070 → BH060 → BH050 → BH032 → BH020 → BH010 → BH005 顺序逐件计算。
- 求解原则：每个给定整体挠度 (w) 独立求当前状态；FEM/试验峰值不作为求根输入；UHPC damage + plastic-reference、TOP/BOTTOM whole-face Yun–Mises predictor/corrector、最终 (P=P_U+P_s^++P_s^-)。
- 钢壳当前塑性接口：先由总几何兼容求 (A^pm)，再固定 (A^pm) 由 total(global+local) Mises 求最大可恢复 (e^pm)，输出 (A_P^pm=A^pm-e^pm)。
- UHPC 当前 damage：按 UC141 原始表峰值重基准；理论定义保持连续积分，数值求值后端必须做积分阶次收敛检查。
- 计算停止规则：若本轮资源不足，只在一个试件完整冻结并提交后停止，不留下“半个试件”的未记录状态。

## 状态
- [ ] BH100：当前路径回归门复核
- [ ] BH085
- [ ] BH070
- [ ] BH060
- [ ] BH050
- [ ] BH032
- [ ] BH020
- [ ] BH010
- [ ] BH005

## 日志
1. 初始化本轮监控文件。下一步先复核 BH100 数值门，再进入 BH085。
