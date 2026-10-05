# UCFT 单参数当前路径：按宽厚比由大到小逐件计算监控

- 开始时间：2026-10-05 12:08 +08:00
- 分支：`diagnostic/20261004-analytic-ninecurve-attempt`
- 顺序：BH100 gate → BH085 → BH070 → BH060 → BH050 → BH032 → BH020 → BH010 → BH005
- 每个 (w) 独立 current-state 求值；FEM/试验不参与求根。
- 停止规则：只在一个试件完整冻结并提交后停止，不留下半个试件的未记录状态。

## 执行口径修正
复核旧 BH100 数值链后确认，当前约 13.40 MN 的 BH100 曲线来自 **ABS/raw UC141 damage + ABS/raw plastic**，不是 formal peak-rebased 版本。为保证系列外推不偷换模型，本轮所有剩余 BH 试件统一沿用 ABS/raw 路径；该 formal-vs-execution 差异已同步写入 CURRENT_PATH_SPEC.md。

## 状态
- [x] BH100：当前路径回归门复核
- [ ] BH085
- [ ] BH070
- [ ] BH060
- [ ] BH050
- [ ] BH032
- [ ] BH020
- [ ] BH010
- [ ] BH005

## BH100 回归门
在 (b=5000) mm、(w=82) mm：
- (ho_A=0.75441), (ho_D=0.68278), (w_P=45.2254) mm；
- (P_U=5.00148) MN；
- TOP predictor (A^+=4.423037) mm，trial VM = 444.887 MPa；
- TOP corrector (e^+=1.910240) mm，VM = 355.000 MPa，(P_s^+=2.974365) MN；
- BOTTOM (A^-=e^-=4.653450) mm，VM = 354.110 MPa，(P_s^-=5.420269) MN；
- (P(82)=13.39611) MN（与旧保存 13.39592 MN 的差异来自积分阶次，约 0.0014%）。

因此当前代码链已复现 BH100，允许进入 BH085。

## 日志
1. 初始化监控。
2. 复核并冻结 current numerical path；修正“formal rebase”与“实际 BH100 ABS/raw”之间的执行口径差异。
3. 下一步：计算 BH085 完整 (P(w)) 曲线并冻结后再进入 BH070。
