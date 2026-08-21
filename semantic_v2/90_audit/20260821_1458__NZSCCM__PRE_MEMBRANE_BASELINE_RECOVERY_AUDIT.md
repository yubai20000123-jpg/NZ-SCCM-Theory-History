# NZ-SCCM — PRE-MEMBRANE BASELINE RECOVERY AUDIT

时间：2026-08-21 14:58 +08:00  
状态：`CURRENT_ROLLBACK_AUDIT / PRODUCTION_DIRECTION_RESET`

## 0. 本轮目的

本轮不是新理论研究，而是严格执行回退审计：

1. 找到“新增膜应力重分布 / Ritz 扩张”之前最后可复现的历史骨架；
2. 重新整理 Swartz24 与 Z0–Z5 的逐项预测/对比；
3. 将 Z6 单列为大柔度/大宽厚比域外诊断；
4. 判断是否有必要继续 Ritz/膜重分布 production 分支。

本轮不使用试验荷载或 Zhou 值来选根、调参、改材料或修改计算结果。

---

## 1. 回退点不是单一代码文件，而是同一父骨架的两个相位实现

历史证据表明，膜重分布扩张以前的共同父骨架为：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 frozen material target
N48-C1/MM
Cayley-Hamilton current map
General-D15 exact moments
formal spatial sampling/quadrature = 0
D,q generalized coordinates
```

### 1.1 RC / Swartz24

2026-08-16 的历史骨架审计明确把旧 RC 膜应变写成：

`eps_x_old = eps0*nu*D + S*alpha^2/2*cos^2X*sin^2Y`

`eps_y_old = -eps0*D + S*beta^2/2*sin^2X*cos^2Y`

`gamma_xy_old = S*alpha*beta*sinX*cosX*sinY*cosY`

其中 `S=A^2+2A0*A`。该文件同时明确说明，后续 membrane redistribution 是在这个历史接受骨架之外额外增加的 delta，而不是旧骨架本身。

Swartz24 在打开试验 failure loads 之前已有 blind theory freeze：

- commit `d65aa840bb3ce65a9f13d31ad85c59dfea4c227d`
- 后续完整 24/24 comparison freeze：`b646834cea78bafbd952e8d7400a8a69b2c19114`

因此 RC 回退身份是明确的：`HISTORICAL_ACCEPTED_RC_BACKBONE`，不含后来新增的 membrane redistribution delta，也不含 Ritz H2/H4/...。

### 1.2 steel-shell / Z family

钢壳历史分支共享 R10/N48/CH/D15 父骨架，并另外使用钢面局部渐进 radial cap。可复现核：

- commit `a3853c78690c8aa8eb043f13b43803f5af9da7a4`
- file `20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP_D15__REPRO.py`

该核明确：formal structural spatial quadrature = 0；材料坐标节点只用于编译局部 cap，不是结构空间点。

Zhou 原始 full-MCFSTW comparator 后续被正确恢复：

- commit `8315c89ff21722a7a18a33fc3009d077a842b678`

因此不能再使用早期 transferred/reduced Zhou comparator 来评价 Z0–Z6。

### 1.3 重要身份边界

RC 和 steel-shell 不是“完全同一个脚本”；它们是同一 R10/N48/CH/D15 父理论在不同结构相位上的实现。steel-shell 额外包含 face steel local-progressive-cap 处理。

所以本轮恢复的是 `PRE_MEMBRANE_PARENT_BACKBONE + phase-specific steel/rebar treatment`，而不是强行把两个历史脚本说成一个程序。

---

## 2. Z0–Z6：按 Zhou 原始 full-MCFSTW comparator 重新统一比较

采用已持久化的 A500/local-progressive D15 预测值，与后来恢复的 Zhou 原始公式值重新计算 signed error：

| Case | NZ-SCCM pre-membrane / MN | Zhou original / MN | signed error |
|---|---:|---:|---:|
| Z0 | 36.619330 | 36.945541 | -0.883% |
| Z1 | 23.190470 | 23.721432 | -2.238% |
| Z2 | 40.208070 | 41.213379 | -2.439% |
| Z3 | 45.022780 | 44.320271 | +1.585% |
| Z4 | 66.886850 | 70.187272 | -4.702% |
| Z5 | 13.177570 | 14.681648 | -10.245% |
| Z6 | 37.509426 | 49.672436 | -24.486% |

### 2.1 Z0–Z5 statistics

- mean signed error = `-3.154%`
- MAE = `3.682%`
- RMSE = `4.853%`
- sample std(signed error) = `4.041 percentage points`
- max |error| = `10.245%` (Z5)

如果只看 Z0–Z4：

- mean signed error = `-1.736%`
- MAE = `2.370%`
- RMSE = `2.697%`
- max |error| = `4.702%`

因此历史记忆“Z0–Z5 总体可靠、Z6 明显偏低”有实质证据支持，但应精确表述为：

- Z0–Z4 非常稳定；
- Z5 有约 10% 的保守低估；
- Z6 出现约 24.5% 的明显域外低估。

不能把 Z5 的 -10.2% 隐去。

---

## 3. Z6 为什么可以作为 OUT-OF-DOMAIN diagnostic，而不是拿误差倒推边界

不使用误差大小定义边界，而只检查几何/稳定参数包络。

基于 Zhou 表中同一组 Z0–Z6 参数：

| Case | b/h | b/t_s | Zhou lambda_n (仅外部诊断) |
|---|---:|---:|---:|
| Z0 | 46.15 | 1500 | 0.750 |
| Z1 | 60.00 | 1500 | 0.867 |
| Z2 | 46.15 | 1500 | 0.804 |
| Z3 | 46.15 | 1500 | 0.820 |
| Z4 | 40.00 | 2000 | 0.636 |
| Z5 | 15.38 | 500 | 0.241 |
| Z6 | 92.31 | 3000 | 1.434 |

Z0–Z5 已验证包络：

- `b/h <= 60`
- `b/t_s <= 2000`
- Zhou `lambda_n <= 0.867`（仅作为独立柔度佐证，不作为 NZ-SCCM 内部求解参数）

Z6：

- `b/h = 92.31`
- `b/t_s = 3000`
- `lambda_n = 1.434`

它在三个维度上均明显越出 Z0–Z5 包络。因此可以事先、独立于误差值，把 Z6 定义为：

`OUT_OF_CURRENT_VALIDATED_STEEL_SHELL_DOMAIN_DIAGNOSTIC`。

这只是“当前验证域”边界，不宣称 `b/h=60` 或 `b/t_s=2000` 是新的物理临界常数。未来若要扩大适用域，应新增物理依据/样本，而不是拟合 Z6。

---

## 4. Swartz24：旧骨架确实可复现，但误差并不如记忆中那样整齐

使用 2026-08-13 冻结的 R10/N48-C1/MM/general-D15 Pu 与 Swartz failure load Pf：

|Case|Pu theory / kN|Pf / kN|error|
|---:|---:|---:|---:|
|1|608.925|490.194|+24.221%|
|2|596.865|506.652|+17.806%|
|3|519.198|444.377|+16.837%|
|4|555.423|534.231|+3.967%|
|5|546.874|623.641|-12.309%|
|6|617.784|691.698|-10.686%|
|7|612.628|640.099|-4.292%|
|8|523.127|455.053|+14.960%|
|9|532.126|625.865|-14.977%|
|10|549.896|696.147|-21.009%|
|11|525.373|636.541|-17.464%|
|12|560.678|639.654|-12.347%|
|13|569.612|511.990|+11.254%|
|14|644.025|716.164|-10.073%|
|15|671.979|766.429|-12.323%|
|16|593.075|721.946|-17.851%|
|17|333.398|429.253|-22.331%|
|18|357.715|396.337|-9.745%|
|19|356.402|377.654|-5.627%|
|20|347.899|372.761|-6.670%|
|21|365.580|368.313|-0.742%|
|22|367.553|355.858|+3.287%|
|23|375.918|346.961|+8.346%|
|24|441.642|400.340|+10.317%|

重新计算统计：

- mean signed error = `-2.810%`
- MAE = `12.060%`
- RMSE = `13.524%`
- centered sample std ≈ `13.514 percentage points`
- median |error| ≈ `11.782%`
- max |error| = `24.221%`

历史 thickness/slenderness 分组仍显示结构性趋势：

- Cases1–8: mean `+6.313%`, MAE `13.135%`
- Cases9–16: mean `-11.849%`, MAE `14.662%`
- Cases17–24: mean `-2.896%`, MAE `8.383%`

因此：

`SWARTZ24_OLD_BACKBONE = REPRODUCIBLE_AND_NONCALIBRATED`

但不能写成：

`SWARTZ24_ERROR = SMALL_UNIFORM_SYSTEMATIC_BIAS`。

其单板散差相当明显。考虑用户已锁定“试件随机误差可能大于理论随机误差”的原则，这组数据应继续保留为现实试验鲁棒性验证集；不能仅凭单板散差反过来重开膜重分布理论，也不能把所有散差都未经证据地归因于试件。

---

## 5. 本轮真正裁决

### 5.1 Ritz / 新膜重分布主线

```text
RITZ_H2_H4_H6_..._AS_PRODUCTION = RETIRED
NEW_MEMBRANE_REDISTRIBUTION_AS_PRODUCTION_BLOCKER = NO
H14 = CANCELLED / NOT NEEDED
```

理由不是“Ritz 数值算不出来”，而是：

1. 它把原本低维解析理论变成了一个需要空间阶次选择的谱求解器；
2. 为覆盖 Z6 这一明显越出当前验证包络的对象，引入的复杂性不符合当前工程收益；
3. 现有 Z0–Z5 并不要求这层复杂性才能得到可接受结果；
4. Swartz24 的实验散差也没有证据表明必须靠新增膜重分布才能统一消除。

### 5.2 恢复的 production candidate

```text
PRE_MEMBRANE_PARENT_BACKBONE = RESTORED
R10 = ACTIVE CANDIDATE MATERIAL TARGET
N48-C1/MM = ACTIVE CANDIDATE COMPILER
CAYLEY_HAMILTON = ACTIVE
NGUYEN_SECOND_ORDER = ACTIVE
GENERAL_D15 = ACTIVE
FORMAL_SPATIAL_QUADRATURE = 0
RITZ_MEMBRANE_EXTENSION = RESEARCH_ONLY / DORMANT
```

不同结构族保留各自已有的 steel/rebar phase treatment，不强行合并成一个未经验证的代码路径。

### 5.3 steel-shell 当前适用域

```text
PRIMARY_VALIDATED_FAMILY = Z0-Z5-like conventional/intermediate flexibility
Z6 = OUT_OF_CURRENT_VALIDATED_DOMAIN_DIAGNOSTIC
NO_Z6_FITTING = YES
NO_MEMBRANE_EXTENSION_REQUIRED_FOR_Z6 = YES
```

### 5.4 production freeze 状态

不能写成“最终 production 已完全验证”。更准确的是：

`PRE_MEMBRANE_BASELINE = RESTORED_PRODUCTION_CANDIDATE`。

原因：Z0–Z5（尤其 Z0–Z4）支持该方向，但 Swartz24 仍有明显现实样本散差，需要按已经锁定的“理论系统偏差 vs 试件实现随机性”框架重新解读，而不是用膜重分布继续追逐每块板。

---

## 6. 后续唯一建议（不扩张理论）

如果继续，本项目下一阶段不再研究 Ritz 或膜重分布，而只做两项整理性工作：

1. 对 Swartz24 按试验记录/破坏形态/重复参数组，在不看理论误差的前提下建立 specimen-realization audit，区分理想理论与试件实现离散；
2. 将 pre-membrane backbone 写成一份统一、可手算审计的 production-candidate 公式/求解流程，明确 steel-shell 适用参数包络，Z6 放在附录作为域外警示案例。

不再为了 Z6 或单个 Swartz 离群样本新增材料参数、膜场自由度、Ritz 阶次或经验修正。