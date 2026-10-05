# BH085–BH050 低承载力审计（2026-10-05）

## 结论
BH085→BH050 的高层调用链与 BH100 13.40 MN 路径保持了同一组尺寸缩放、ABS/raw UC141 damage+plastic、whole-face N=m=4、predictor→Mises-corrector 和 P=PU+Ps+ + Ps- 结构；但**不能证明 steel Mises 的逐项实现与 BH100 完全逐字节一致**，因为 BH100 当时使用的“钢板两厚度表面 + global low-order field 的 mean-shift 到 Yun mean + local seven-harmonic”实现细节没有写入 CURRENT_PATH_SPEC，也没有把执行代码提交到本目录。故系列结果先降级为 PROVISIONAL/QUARANTINED。

更重要的是，低值的第一主因已经定位在 UHPC raw damage 驱动，而不是积分误差。

## 1. 系列当前峰值
| case | b mm | wu mm | q=wu/b | rhoA | rhoD | wP/w | PU/P |
|---|---:|---:|---:|---:|---:|---:|---:|
| BH100 | 5000 | 82.1407 | 0.016428 | 0.7540 | 0.6823 | 0.5520 | 0.3736 |
| BH085 | 4250 | 66.3601 | 0.015614 | 0.748835 | 0.676795 | 0.5422 | 0.3771 |
| BH070 | 3500 | 49.3888 | 0.014111 | 0.726015 | 0.662255 | 0.5327 | 0.3674 |
| BH060 | 3000 | 35.2080 | 0.011736 | 0.702053 | 0.656055 | 0.5243 | 0.3370 |
| BH050 | 2500 | 20.5329 | 0.008213 | 0.660889 | 0.650619 | 0.5372 | 0.2906 |

该序列表明不是随机数值噪声：随着 b 减小，UHPC 保留膜刚度和总荷载占比系统下降，BOTTOM first-yield 更早控制峰值。

## 2. 已定位的 UHPC 错误机制：Poisson 横向伸长被 raw tension-damage 当成拉裂
当前 trial 中面横向应变含
[
+
u_car N_y^E/(E_ct_c).
]
即便处于纯单轴压缩、横向主应力为零，仍会有正的 Poisson 横向应变。

各峰值点的均匀轴向压应变与其 Poisson 正应变为：
| case | NyE/(Ec tc) | nu*NyE/(Ec tc) | 仅按 raw tension table 映射得到的 d_t 约值 |
|---|---:|---:|---:|
| BH100 | 0.00126881 | 0.00038064 | 0.3807 |
| BH085 | 0.00131935 | 0.00039581 | 0.3948 |
| BH070 | 0.00139800 | 0.00041940 | 0.4060 |
| BH060 | 0.00142766 | 0.00042830 | 0.4102 |
| BH050 | 0.00150677 | 0.00045203 | 0.4214 |

UC141 tension 表换成 total strain 后，第一点约为 0.00012834 (d=0)，第二点约为 0.00038739 (d=0.39086)。因此 current ABS/raw 算法会把**没有 tensile principal stress 的 Poisson lateral strain**直接解释成约 0.38–0.42 的 tensile damage。b 越小、峰值处平均压应变越高，这一伪损伤越严重。

这解释了为什么 BH050 在理论峰值时已经只有 rhoA≈0.661、rhoD≈0.651，且 PU 仅 2.206 MN。

## 3. BH100 的 13.40 MN 不能作为“该 raw 路线已验证”的充分门
BH100 当前总峰值虽然与 DIRECT 总荷载接近，但其当前分配是 PU≈5.0 MN、steel≈8.4 MN，即 UHPC 约 37%、steel 约 63%。因此总值接近可以由“UHPC 过低 + steel 过高”的抵消产生。到了较小 b，这种抵消不再保持，于是总承载力系统偏低。

## 4. steel peak mechanism
BH100、BH085、BH070、BH060、BH050 均在 BOTTOM first-yield 附近形成总峰值。整体钢壳弯曲应变含
[
z_seta^2wsim z_s w/b^2,
]
因此 b 减小时 BOTTOM global+local Mises 更早触及 355 MPa；这与当前序列 q_u 单调下降一致。该现象是同一公式的系统行为，不是单个试件求根失败。

但 BH100 原执行中的 steel Mises 细节没有完整备份代码，所以必须重新做一个 BH100/BH050 side-by-side evaluator 才能正式证明 steel implementation 完全一致。

## 5. 积分后端的程序合规问题
BH085→BH050 结果文件使用 nq=80/100/120/160 数值求积做收敛。其数值扩散只有约 1e-5 MN 量级，**不是低承载力的原因**；但它不符合用户要求的 production 级“水平集 + 连续定积分/显式特殊函数”口径。因此这些结果只能作为 numerical audit，不应称为最终显式生产结果。

## 6. 暂停规则
暂停 BH032 及以下试件。下一步应先完成：
1. BH100 与 BH050 使用完全相同、逐项冻结的 evaluator 做 side-by-side 审计；
2. tensile damage 不能再由正 principal total strain 单独触发；至少必须排除 pure Poisson expansion（例如以 tensile principal stress / cracking-state gate 作为激活条件），但不允许用 FEM 反标；
3. 保留 ABS/raw damage 数值本身与连续 Macaulay 表达，只修正其多轴激活变量；
4. 再复算 BH100，确认总荷载与受力分配同时合理后，才继续 BH085→BH005。
