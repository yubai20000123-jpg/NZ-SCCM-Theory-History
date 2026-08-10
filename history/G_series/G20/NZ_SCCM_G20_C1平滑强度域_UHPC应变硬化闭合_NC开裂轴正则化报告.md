# NZ-SCCM G20：C1平滑双轴强度域、UHPC拉伸应变硬化来源闭合与普通混凝土开裂轴正则化

日期：2026-08-08

## 0. 总裁决

本轮不是新增材料机制，而是对 G19 暴露出的“开裂轴尖锐化”进行来源回查与平滑重构。

```text
UHPC_STRAIN_HARDENING_SOURCE_CLOSURE = PASS
UHPC_STRAIN_HARDENING_ALREADY_PRESENT_IN_G16R = PASS
UHPC_TT_P8_SUPERELLIPSE = PASS
UHPC_TC_C1_SOURCE_CONSTRAINED = PASS
NC_G19_ZERO_TENSION_AT_ORIGIN = RETIRED
NC_TC_C1_ROUNDED_ENVELOPE = PASS
NC_SCALAR_SMOOTH_DEGREE70 = PASS_AS_UNIAXIAL_CANDIDATE_NOT_PRODUCTION
NC_LEGACY_2D_INTERACTION_AFTER_RESTORED_TENSION = FAIL / REIDENTIFY
NEW_Pcr_Pu = NOT COMPUTED
SWARTZ24 = HOLD
```

最重要的材料结论：**用户关于 UHPC 钢纤维桥联后出现数千微应变的应变硬化判断完全正确，但这并不是当前来源链遗漏。Hiew 2024 的统一拉伸本构本身就明确包含 elastic → strain-hardening → strain-softening，而且 G16R 已经把有效开裂、拉伸峰值、局部化和拉伸极限四类锚点写进一维 UHPC 候选。**

## 1. UHPC 应变硬化量级

Hiew 2%钢纤维三组直接拉伸数据的开裂→峰值硬化区：

| series    |   eps_cr_microstrain |   eps_peak_microstrain |   crack_to_peak_delta_microstrain |   f_cr_MPa |   f_peak_MPa |   crack_to_peak_delta_stress_MPa |   hardening_secant_modulus_MPa |   hardening_secant_over_Et_percent |
|:----------|---------------------:|-----------------------:|----------------------------------:|-----------:|-------------:|---------------------------------:|-------------------------------:|-----------------------------------:|
| SL-2.0    |                  400 |                   3800 |                              3400 |       10   |         11.7 |                              1.7 |                        500     |                           1.04603  |
| HL-2.0    |                  420 |                   6740 |                              6320 |       10.3 |         11.1 |                              0.8 |                        126.582 |                           0.258331 |
| SL-HL-2.0 |                  420 |                   3800 |                              3380 |       10.1 |         11   |                              0.9 |                        266.272 |                           0.551288 |

项目尺度（fc固定141.1 MPa，采用G16R来源转移）为：

- 有效开裂：eps = 420 με，sigma = 9.7677 MPa；
- 拉伸峰值：eps = 3800 με，sigma = 10.7348 MPa；
- 局部化：eps = 6900 με，sigma = 10.3480 MPa；
- 拉伸极限：eps = 7590 με。

因此 crack→peak 的应变增长为 **3380 με**，应力只增加 **0.9671 MPa**；对应割线硬化模量仅 **286.1 MPa = 0.659% Ec**。峰值后到局部化还可继续增长 **3100 με**，应力只下降 **0.3868 MPa**。

也就是说，用户所说的“应力不变或微小变化，但应变持续几千微应变”就是当前 Hiew 2%来源数据的直接特征，不需要另外虚构一个纤维桥联分支。

## 2. 为什么 UHPC 这部分反而比 G19 普通混凝土尖角容易编译

UHPC 的开裂后响应不是 `sigma -> 0` 的突降，而是一个宽广的低斜率硬化/近平台区。对全域有限多项式而言，这是一条连续缓变目标；G19真正困难的是普通混凝土被人为写成 `x>=0 => sigma=0` 后在原点制造出的导数断裂。

因此本轮保持 G16R 的 UHPC degree-70 一维候选身份，不删除其硬化锚点。

## 3. C1 平滑双轴强度包络

强度包络只负责“可允许的强度域”；材料切线仍由当前应力—应变映射直接微分获得，**不从强度包络斜率生成材料切线**。

两类材料均保留 G18 的双压椭圆与 TT p=8 超椭圆。TC 不再使用在拉伸轴形成几何不相容的简单三次拼接，而改为 Bernstein 多项式曲线 `tau(c)`，同时强制：

- `tau(0)=1`；
- `tau'(0)=0`，与 TT p=8 在拉伸轴 C1 相接；
- `tau(1)=0`；
- `tau'(1)=-2/[alpha*(ft/fc)]`，使物理应力空间中的切线与 CC 椭圆在压缩轴相同；
- 全区 `0<=tau<=1` 且单调；
- UHPC 曲线位于现有 Liu TC 来源点内侧；
- NC 曲线在高压缩区不超过 G18 已通过的保守三次边界。

本轮 UHPC 与 NC 的第一可行阶数均为 degree 12。四个轴线切线匹配误差均小于 1e-9，见 `09_strength_envelope_C1_axis_tangent_audit.csv`。

UHPC TT 继续采用 p=8。等双拉强度为 `2^(-1/8)=0.9170 ft`，且现有 Liu 两个 TT 峰值点均位于该保守曲线外侧。

## 4. 普通混凝土 G19 开裂轴修正与次数门禁

G19 的 `x>=0 => sigma=0` 被正式废止。本轮采用来源约束更合理的参考：

- 原点至开裂前保持真实弹性斜率；
- `ft/fc=0.1`，`x_cr=0.05`；
- 采用 Nguyen/Foster tension-stiffening 的 `alpha1=10`；
- `alpha2` 取来源允许范围下限 0.3 作为保守参考；
- 仅在两个原始斜率突变点附近用窄 C2 quintic bridge 正则化，避免把源公式尖角直接塞给全域多项式。

重新进行单一全域 Chebyshev 次数门禁，degree 70（Sobolev stress+tangent fit, lambda=0.01）得到：

- RMS stress error = 0.002357 fc；
- P95 stress error = 0.004974 fc；
- max stress error = 0.020082 fc；
- tangent RMS error = 0.099575（归一化）；
- 最大拉应力 = 0.099899 fc <= 0.1 fc；
- `U(0)=0`, `U'(0)=2`, `U(-1)=-1`, `U'(-1)=0` 精确约束。

相对 G19 degree-70：

- RMS 误差下降 75.2%；
- P95 误差下降 75.0%；
- max 误差下降 58.3% 。

这验证了 G19 的高阶压力主要来自**人为开裂尖角**，而不是“一维本构天然需要极高阶”。

## 5. 为什么仍不开始 Swartz24

恢复真实普通混凝土拉伸以后，G19 旧的二维 current interaction `1+0.05xy` 不再够用。它在结构可达云中的 TC 区会让“较大压应力 + 尚存拉应力”组合超出新 C1 保守强度域。因此：

```text
NC scalar problem = substantially repaired
NC strength envelope = C1 closed
NC 2D current interaction = active blocker
```

这不是回到 300 系数二维面。下一步只需要在当前**已冻结的一维骨架 + C1强度域**之间重新识别一个低参数、全结构域受约束的二维 interaction kernel，并继续要求其应力与切线由同一个解析映射产生。

本轮未计算任何新的 Pcr/Pu。
