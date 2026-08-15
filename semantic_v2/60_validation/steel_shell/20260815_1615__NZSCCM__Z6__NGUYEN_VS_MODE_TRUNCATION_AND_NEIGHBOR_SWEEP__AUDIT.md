# NZ-SCCM Z6 — Nguyen 二阶运动学 vs 单模态截断与邻域扫掠审计

**Timestamp:** 2026-08-15 16:15 +08:00  
**Status:** NGUYEN SECOND-ORDER PRIMARY-CAUSE HYPOTHESIS NOT SUPPORTED / LINEAR WRONG-MODE HYPOTHESIS NOT SUPPORTED / HIGH-SLENDERNESS LOW-DIMENSIONAL POSTBUCKLING BIAS SUPPORTED BY NEIGHBORHOOD TREND

## 0. 本轮问题

本轮只回答：Z6 的约 24.5% 低估，到底更像 Nguyen 二阶运动学本身失效，还是当前将 Nguyen 连续运动学投影到一个完整半波、一个主面外幅值 q 的低维位移空间后，在高长细比区缺少有限幅值后屈曲重分布能力。

冻结：R10、N48-C1/MM、Cayley-Hamilton、General-D15、Nguyen second-order、A0=a/500、local progressive radial-cap shell current map。正式结构空间采样/积分均为 0；不使用 Zhou/Winter 荷载选根或调参。

## 1. 来源边界

Nguyen Chapter 6 Eq. (6.3) 明确保留初始缺陷和面外位移斜率的二阶膜应变项；Chapter 2 的稳定扰动推导说明三阶及更高阶位移函数项被忽略。因此要判断“二阶截断是否失效”，控制量首先应是转角/斜率，而不是单独的 b/h。

Zhou Chapter 5 Table 5.1 的四边简支轴压 Group 4 范围为 ns=10–60, ls=200 mm, h=100–130 mm, ts=4 mm, fy=355 MPa, fcu=40 MPa, a=3000–9000 mm, b=2000–12000 mm。Z6 位于该参数空间极端角点。Zhou 同章指出弹性临界宽厚比约 b/h=60、弹塑性临界宽厚比约 b/h=40；Z6 的 b/h=92.31 明显处于深稳定控制区。

## 2. Nguyen 小斜率量级审计

当前 Z6 reduced local-cap 峰附近：

- q0 = 0.0015
- q = 0.0058975999
- q_total = 0.0073975999
- max |w,x| = pi q_total b/a = 0.030987 rad = 1.775 deg
- max |w,y| = pi q_total = 0.023240 rad

H0 后续同 D=0.705 支路定位即便达到 q≈0.0073561，最大斜率也仅 0.03710 rad = 2.125 deg。

用 Nguyen Chapter 2 所采用的小角度 Taylor 截断作量级指标：sin(theta)=theta-theta^3/6+...，因此当前 Z6 最大斜率下首个被舍弃项相对 theta 的量级约 theta^2/6 = 1.60e-4，即 0.016%；H0 较深状态约 0.023%。即使人为把 q 推到 0.02，最大斜率约 0.0901 rad=5.16 deg，该指标仍约 0.135%。

这不是对所有高阶 Green-Lagrange 项的严格误差上界，但足以排除“因为 b/h 很大，所以 Nguyen 二阶小斜率运动学本身直接产生 20% 级误差”的简单解释。

判定：`NGUYEN_SECOND_ORDER_AS_PRIMARY_Z6_ERROR_CAUSE = NOT SUPPORTED`。

## 3. 线性模态间隔审计

采用 Zhou 四边简支原全拓扑 Dx-Dy-H 弹性公式，对 S0–S4 计算 (m,n) 候选模态。S0=Z6：

- Pcr(1,1)=42.8315 MN
- Pcr(2,1)=91.4317 MN = 2.135 Pcr(1,1)
- Pcr(3,1)=178.3236 MN = 4.163 Pcr(1,1)
- Pcr(1,2)=182.38 MN ≈4.258 Pcr(1,1)

S1–S4 中最近的第二模态也均至少为第一模态的 1.774–2.367 倍。因此 Z6 不是线性屈曲阶段的近简并模态点，m=1 并没有因为 Z6 进入极端宽厚比就失去线性控制地位。

判定：`WRONG_LINEAR_HALFWAVE_COUNT_AS_PRIMARY_CAUSE = NOT SUPPORTED`。

注意：这不等于证明有限幅值后屈曲仍能由单一 q 完整描述。非线性项会生成更高谐波和面内膜力重分布，有限幅值阶段仍需另行检验。

## 4. 不改原方法的 Z6 邻域扫掠

邻域冻结：

- S0: a=9000, b=12000, h=130, ns=60
- S1: a=8000, b=12000, h=130, ns=60
- S2: a=9000, b=10000, h=130, ns=50
- S3: a=8000, b=10000, h=130, ns=50
- S4: a=8550, b=11400, h=130, ns=57（a,b 同时仅减 5%）
- ls=200, ts=4, fy=355, fcu=40
- A0=a/500

S1–S4 均使用原 reduced NZ-SCCM 路径：R10→N48→CH→Nguyen D,q→D15；外钢板采用当前 local progressive radial-cap。先用 degree-20 shell scalar compiler 在若干 D 上建立 Rq 符号变化括号并线性定位 connected root，再在峰值邻域用 degree-32 复核。degree-20→32 在选定峰值邻域的 P 差均约 0.001 MN 或更小，说明本轮邻域趋势不由 shell scalar compiler degree 决定。

工程峰值邻域结果：

|Case|a/h|b/h|Zhou lambda|NZ local-cap P(MN)|Zhou lower(MN)|NZ-Zhou|
|---|---:|---:|---:|---:|---:|---:|
|S0 Z6|69.23|92.31|1.4341|37.5094|49.6724|-24.49%|
|S1 a=8000|61.54|92.31|1.3782|40.7732|50.2501|-18.86%|
|S2 b=10000|69.23|76.92|1.2400|37.0002|44.1305|-16.16%|
|S3 a=8000,b=10000|61.54|76.92|1.2154|39.6080|44.6847|-11.36%|
|S4 a,b -5%|65.77|87.69|1.3625|38.1674|47.9466|-20.40%|

S4 是最关键的“微扰”判别：几何仅缩小 5%，NZ 误差从 -24.49% 改善到约 -20.40%，没有突然跳回 ±5% 区间。因此 Z6 不是一个孤立的数值奇点；误差随整体长细比降低呈连续改善趋势。

S1/S2/S3 进一步显示：减小 a 或 b 都会改善差异，减小 b 的作用更明显；这与 Zhou Chapter 5 对 b/h 更敏感的来源结论方向一致。

判定：

- `Z6_ISOLATED_NUMERICAL_BUG = NOT SUPPORTED`
- `HIGH_SLENDERNESS_SYSTEMATIC_BIAS = SUPPORTED`
- `WIDTH_SLENDERNESS_SENSITIVITY = CONSISTENT_WITH_ZHOU_SOURCE_TREND`

## 5. 本轮真正指向哪里

当前证据把问题从“Nguyen 二阶运动学可能失效”进一步收缩为：

1. Nguyen 二阶连续运动学本身：目前小斜率量级不支持其为 20% 级主因；
2. 线性 m=1 模态选择：模态间隔很大，不支持为主因；
3. **当前把连续运动学截断成 ONE_CONTINUOUS_COMPLETE_HALFWAVE + 单一主 q 的有限幅值位移空间**：成为第一开放嫌疑；
4. 离散内腹板拓扑的大挠度约束、完整增量 J2 塑性重分布：仍是第二层开放机制。

换言之，目前更合理的表述是：

> Z6 的异常并非“Nguyen 二阶关系在大 b/h 下错误”，而是 NZ-SCCM 当前低维投影在 lambda≈1.2–1.4 的高长细比后屈曲区表现出越来越保守的系统趋势。

## 6. 下一步建议

不修改 Nguyen、R10 或材料本构，建立仅用于诊断的高阶谐波释放试验：在现有 w11 主模态上增加一个对称高阶幅值（优先 w31，随后按需要检验 w13），保持同一连续完整域和 D15 精确矩，不引入空间积分点。比较：

- q3=0 退化回当前模型；
- q3 自由时 Z6/S4/S3 的极限承载力增量；
- 若增量随 lambda 增大显著增加，即确认单 q 有限幅值空间不足；
- 若增量很小，则转向离散腹板拓扑/增量塑性重分布。

本轮不创建新的 production multimode theory，只定义下一诊断门禁。
