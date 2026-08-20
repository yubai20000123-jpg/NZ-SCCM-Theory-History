# NZ-SCCM — NC-M2 拉伸曲线执行审计

时间：2026-08-20 14:41 +08:00

对应理论审计：

`semantic_v2/20_theory/20260820_1441__NZSCCM__NC_M2_TENSION_BACKBONE_AUDIT__FINITE_ENERGY_GATE.md`

## 1. 审查对象

当前 NC-M2 拉伸骨架：

\[
T(t)=\frac{t}{1-t+t^2}.
\]

本轮只做材料曲线审查，不进入板积分、不计算 Case21 Pu。

## 2. 曲线样点

| t | M2 | Foster-light-RC reference | finite-energy diagnostic p=3 |
|---:|---:|---:|---:|
| 1.0 | 1.000000 | 1.000000 | 1.000000 |
| 1.5 | 0.857143 | 0.961111 | 0.901023 |
| 2.0 | 0.666667 | 0.922222 | 0.736842 |
| 3.0 | 0.428571 | 0.844444 | 0.468750 |
| 5.0 | 0.238095 | 0.688889 | 0.212766 |
| 10.0 | 0.109890 | 0.300000 | 0.059041 |

Foster 曲线仅作为 Nguyen 来源中的 RC bond tension-stiffening 参照，不作为素混凝土裂缝软化拟合目标。

## 3. 面积

- M2 `0..3`: `1.98962`
- diagnostic p=3 `0..3`: `2.13507`
- Foster reference `0..3`: `2.34444`

- M2 `0..5`: `2.62169`
- diagnostic p=3 `0..5`: `2.77229`
- Foster reference `0..5`: `3.87778`

- M2 `0..10`: `3.41214`
- diagnostic p=3 `0..10`: `3.33652`
- Foster reference `0..10`: `6.35`

- diagnostic p=3 `0..infinity`: approximately `3.93654`, finite.
- M2 `0..infinity`: divergent because `T(t)~1/t`.

## 4. 执行判定

`T(t)=t/(1-t+t^2)` 在有限区间内具有合理的光滑单峰形状，但不能通过材料级有限耗能门禁。

因此：

- M2 不冻结；
- 当前 T 不作为 production tensile law；
- p=3 只作为证明“单式有限耗能修正可行”的诊断曲线，不是新材料候选；
- 尚未触发完整五图的新候选发布；
- 下一步不做 Case21；先由材料物理尺度决定是否需要 fracture-energy / crack-band length，再正式选 T。
