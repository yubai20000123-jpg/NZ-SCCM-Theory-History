# NZ-SCCM Z4/Z6 长宽比能量一致性与 Zhou 拟合曲线审计

**Timestamp:** 2026-08-15 18:44 +08:00  
**Status:** ZHOU ELASTIC ENERGY RESPONSE = PASS; PRIOR SYNTHETIC Pu COMPARATOR INTERPRETATION = CORRECTED

## 1. 触发原因

用户指出：先前将 Z4/Z6 的轴向长度 a 改为 a=b 与 a=1.25b 后，Z4 的承载力变化而 Z6 的 Zhou “Pu” 几乎不变；这看起来违背经典薄板能量规律。

审计后确认：此前表中 `Zhou lower Pu` 不是能量法直接给出的承载力，而是把 Zhou 第5.3.4节基于 FE 点拟合的 Perry-Robertson 下包络式(5-87)–(5-88)继续外插到“只修改 a 的虚拟算例”。这一用法会把能量法的 Pcr 灵敏度压扁，因而不能作为长宽比能量一致性的主判据。

## 2. 正确分层

### 2.1 能量层

Zhou 四边简支正交各向异性弹性屈曲公式来自第5.2–5.3.1节能量法/齐次方程。保持截面不变、只改变 a 时，Pcr 必须按弯曲能与几何刚度重新变化。

经典各向同性 m=1 参考：
`k=(a/b+b/a)^2`。

a/b = 0.75, 1.00, 1.25 时：
- k = 4.340278
- k = 4.000000
- k = 4.202500

因此方形附近是 m=1 的能量低点，0.75 -> 1.0 应降低 Pcr，1.0 -> 1.25 应回升。

### 2.2 Zhou 正交各向异性能量结果

Z4:
- 0.75: Pcr = 196.411220 MN
- 1.00: Pcr = 179.754773 MN, 相比 0.75 降低 8.4804%
- 1.25: Pcr = 187.589343 MN, 相比 1.00 回升 4.3585%

Z6:
- 0.75: Pcr = 42.831476 MN
- 1.00: Pcr = 39.288015 MN, 相比 0.75 降低 8.2730%
- 1.25: Pcr = 41.041374 MN, 相比 1.00 回升 4.4628%

**Z4 与 Z6 的能量响应几乎同型。不存在“Z6 的 Zhou 弹性屈曲公式违反能量法”的证据。**

## 3. 为什么先前 Z6 的 fitted Pu 几乎不动

第5.3.4节式(5-87)–(5-88)是 FE 稳定点的下包络拟合，不是能量泛函驻值得到的 Pu。

在 Z6 三个虚拟 a/b 下：
- λn = 1.434107 -> φ = 0.563884 -> Pu_fit = 49.672436 MN
- λn = 1.497383 -> φ = 0.561776 -> Pu_fit = 49.486767 MN
- λn = 1.465049 -> φ = 0.562021 -> Pu_fit = 49.508397 MN

该拟合高长细比分支在 λ≈1.48559 附近本身存在一个很平的局部极小值；Z6 的三个 λ 恰好落在该平坦区附近。因此 Pcr 改变约 8%，映射后的 φ/Pu 只改变约 0.4%。

这说明：
`Zhou Eq5-87/5-88 fitted lower envelope` 不应再用于“人为只改变 a”的能量一致性诊断。

这不是否定 Zhou 原公式对其 FE 参数集的设计用途，而是纠正我们此前把“经验下包络”当作“能量响应曲线”的使用错误。

## 4. 后续 comparator 规则

对于虚拟长宽比扰动：
1. 第一判据 = Zhou/经典弹性 Pcr（能量层）；
2. 第二判据 = NZ 同一 current operator 的真实平衡路径 Pu；
3. 可辅以 Zhou 第5.3.5节 theory-based 分项稳定曲线 / Winter 作为工程参考；
4. 禁止再用 Eq(5-87)-(5-88) 的 fitted Pu 单独判断“是否符合能量法”；
5. 真实 Z6 原始几何的 49.672436 MN 仍保留其身份：`ZHOU_EQ_5_87_5_88_FE_FITTED_LOWER_ENVELOPE`，不是 raw FE Pu，不是能量法 Pu。

## 5. 结论

`Z6_ENERGY_FORMULA_ASPECT_RESPONSE = PASS`

`PRIOR_Z6_SYNTHETIC_FITTED_Pu_AS_ENERGY_DISCRIMINATOR = INVALID / RETRACTED`

`CURRENT_ASPECT_DIAGNOSTIC = Pcr_energy + NZ_equilibrium_Pu`
