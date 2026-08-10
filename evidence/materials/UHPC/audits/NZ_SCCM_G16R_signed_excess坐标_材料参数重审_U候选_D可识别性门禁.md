# NZ-SCCM G16R：signed/excess 二维交互坐标、材料参数重审与生产面可识别性门禁

日期：2026-08-07

## 0. 总裁决

用户最新边界已执行：唯一不可修改材料标量为 `fc=141.1 MPa`。
`Ec、eps_c0、ft、nu` 均重新接受材料来源审计；禁止使用板 `Pcr/Pu` 或结构试验反标材料。

```text
SIGNED_EXCESS_COORDINATE = PASS
MATERIAL_PARAMETER_REAUDIT = PASS
OLD_ft_7.3 = RETIRED
GLOBAL_U_DEGREE70 = NUMERIC SOURCE-ANCHOR CANDIDATE PASS

PRODUCTION_D = FAIL / NOT IDENTIFIABLE FROM CURRENT FROZEN SOURCE ROLES
ACTUAL_P_R_A_L = NOT AUTHORIZED
NEW_Pcr_Pu = NOT AUTHORIZED

G16R_DECISION =
PARTIAL_PASS_COORDINATE_AND_U
FAIL_D_IDENTIFIABILITY
PASS_TO_G16R2
```

## 1. 材料参数重审

| parameter                         |   old_value |   G16R_value | decision               |
|:----------------------------------|------------:|-------------:|:-----------------------|
| fc_MPa                            |    141.1    |    141.1     | IMMUTABLE_BY_USER      |
| Ec_MPa                            |  43400      |  43400       | RETAINED_AFTER_REAUDIT |
| eps_c0                            |      0.0035 |      0.0035  | RETAINED_AFTER_REAUDIT |
| nu                                |      0.2    |      0.2     | RETAINED_AFTER_REAUDIT |
| ft_old_reference_MPa              |      7.3    |    nan       | RETIRED                |
| ft_peak_project_MPa               |    nan      |     10.7348  | UPDATED_FROM_HIEW_2PCT |
| ft_effective_cracking_project_MPa |    nan      |      9.76772 | UPDATED_FROM_HIEW_2PCT |
| ft_localization_project_MPa       |    nan      |     10.348   | UPDATED_FROM_HIEW_2PCT |
| eps_t_cr                          |    nan      |      0.00042 | UPDATED_FROM_HIEW_2PCT |
| eps_t_peak                        |    nan      |      0.0038  | UPDATED_FROM_HIEW_2PCT |
| eps_t_loc                         |    nan      |      0.0069  | UPDATED_FROM_HIEW_2PCT |
| eps_t_lim                         |    nan      |      0.00759 | UPDATED_FROM_HIEW_2PCT |

本轮没有为了“必须改参数”而机械修改 `Ec、eps_c0、nu`。
`Ec=43.4 GPa` 位于 Hiew 2%钢纤维系列 41.6–44.7 GPa 的受压弹模范围内；
`nu=0.20` 也与该系列一致；`eps_c0=0.0035` 没有发现必须推翻的来源冲突。

真正发生更新的是拉伸幅值。旧 `ft=7.3 MPa` 退出生产材料参数。
以固定 `fc=141.1 MPa` 与 Hiew 2%系列56 d抗压强度中位值之间的材料级尺度比
`s_f=0.967100754` 转移直接拉伸锚点，得到：

- `f_t,cr = 9.7677 MPa`
- `f_t,peak = 10.7348 MPa`
- `f_t,loc = 10.3480 MPa`
- `eps_t,cr = 0.000420`
- `eps_t,peak = 0.003800`
- `eps_t,loc = 0.006900`
- `eps_t,lim = 0.007590`

其中 `eps_t,cr` 按 Hiew/AASHTO 的 0.02% offset effective cracking 语义处理，
不再错误强制满足 `f_cr=E*eps_cr`。

## 2. G16 的 Poisson 假软化冲突已解除

现有等效单轴坐标的逆变换为：

`eps1 = eps_c0 (x - nu y)`

`eps2 = eps_c0 (y - nu x)`

定义方向1的 signed/excess 横向交互应变：

`eps2_ex = eps2 + nu eps1 = (1-nu^2) eps_c0 y`

故严格有：

`y=0 -> eps2_ex=0`

这意味着真正单轴压缩的普通 Poisson 横向膨胀不会再触发 TC cracked-softening。
离散恒等式检查最大绝对误差为 `8.674e-19`。

## 3. 新的单轴全域 U(x)

G12 degree-54 不再复用。

本轮以 Wu-type smooth 压缩参考 + Hiew 2%直接拉伸锚点建立材料级参考，
随后用一个 **degree-70 全域有限多项式** 表达 `U(x)`，没有运行时拉/压分支。

强制精确满足：
- `U(0)=0`
- `U'(0)=Ec eps_c0 / fc`
- `U(-1)=-1`
- `U'(-1)=0`
- Hiew有效开裂点
- Hiew拉伸峰值及峰值零切线
- Hiew局部化点
- Hiew拉伸极限点

锚点审计：

| anchor               |        x |   target_stress_MPa |   U_stress_MPa |   stress_error_MPa |
|:---------------------|---------:|--------------------:|---------------:|-------------------:|
| ORIGIN               |  0       |             0       |    3.91631e-15 |        3.91631e-15 |
| COMP_PEAK            | -1       |          -141.1     | -141.1         |        0           |
| HIEW_EFFECTIVE_CRACK |  0.12    |             9.76772 |    9.76772     |        2.4869e-14  |
| HIEW_TENSION_PEAK    |  1.08571 |            10.7348  |   10.7348      |        1.06581e-13 |
| HIEW_LOCALIZATION    |  1.97143 |            10.348   |   10.348       |        1.61648e-13 |
| HIEW_TENSION_LIMIT   |  2.16857 |             0       |    1.76234e-13 |        1.76234e-13 |

全域材料参考误差：
- 最大应力误差 = `1.2887 MPa`
- RMS应力误差 = `0.6846 MPa`
- 导数极值审计最大符号越界 = `1.209e-05`

因此本轮将 degree-70 U 标记为：
`NUMERIC SOURCE-ANCHOR CANDIDATE PASS`，
但由于整个二维面尚未冻结，不单独宣称其为最终不可修改系数集。

## 4. D(x,y) 的真正阻断

材料语法仍为：

`F(x,y)=U(x)+x*y*D(x,y)`

新 excess 坐标使 Diab/Ferche TC 压缩软化只由“超出自由 Poisson 的横向拉伸”驱动。
D 次数扫描：

|   D_total_degree |   coefficient_count |   Diab_holdout_max_abs_error_MPa |   Diab_holdout_RMS_error_MPa |   Liu_CC_TT_fit_max_abs_error_MPa |   Liu_TC_path_holdout_max_abs_error_MPa |
|-----------------:|--------------------:|---------------------------------:|-----------------------------:|----------------------------------:|----------------------------------------:|
|                4 |                  15 |                         39.6356  |                    14.5921   |                        29.7601    |                                 550.583 |
|                6 |                  28 |                          9.85541 |                     3.40871  |                         1.48341   |                                1154.51  |
|                8 |                  45 |                          6.34684 |                     2.02001  |                         0.717972  |                                 382.217 |
|               10 |                  66 |                          3.75113 |                     1.23426  |                         0.169994  |                                 246.817 |
|               12 |                  91 |                          2.54397 |                     0.746657 |                         0.0350134 |                                 158.668 |

以 degree-10 为例：
- Diab current-TC holdout 最大误差 = `3.751 MPa`
- Liu CC/TT 拟合最大误差 = `0.170 MPa`
- 未参与拟合的 Liu TC 路径 holdout 最大误差 = `246.817 MPa`

这里的失败不是“次数不足”。

TC状态 `x<0,y>0` 中，压缩方向使用 `D(x,y)`，
而同一物理点的拉伸方向通过交换主方向使用 `D(y,x)`，即落在 `x>0,y<0` 区域。

当前冻结来源角色只给出了：
- Diab/Ferche：TC压缩方向 current softening；
- Liu CC/TT：稀疏双轴峰值资格；
- Liu proportional/sequential TC：已冻结为 path-dependent holdout；
- Leutbecher：预裂/路径相关独立验证。

因此 `D(x>0,y<0)` 没有路径无关的 current-value 生产来源。
不同正则化能保持已知来源误差较小，却会使这个未见区域的预测显著漂移。
所以不能挑一个“看起来合适”的 D10/D12 系数冒充材料定律。

## 5. 正式门禁

```text
G16R-01  fc=141.1 USER LOCK                    PASS
G16R-02  companion parameter re-audit          PASS
G16R-03  old ft=7.3                            RETIRED
G16R-04  signed/excess coordinate              PASS
G16R-05  exact uniaxial-axis protection        PASS
G16R-06  degree-70 global U candidate           PASS_NUMERIC
G16R-07  Diab current TC compression side      PASS
G16R-08  Liu CC/TT sparse qualification        PASS
G16R-09  opposite TC tensile current sector    FAIL_UNIDENTIFIED
G16R-10  production D freeze                   NOT_AUTHORIZED
G16R-11  actual P/R_A/L                        NOT_AUTHORIZED
G16R-12  new Pcr/Pu                            NOT_AUTHORIZED
```

## 6. 唯一下一步：G16R2

G16R2只剩一个材料理论决策：

如何在不使用板承载力、不引入材料历史积分点的前提下，
为 `x>0,y<0` 的 TC 拉伸方向提供合法 current-value closure？

合法路径只有两类：

1. 采用一套路径无关、同时给出TC两主方向应力的材料级 current source；
2. 明确修改 G14 的来源角色合同，将某一条实测TC路径
   （最自然的是 proportional TC）指定为项目 current-map 的 canonical closure，
   其余路径继续作为外部误差带/验证。

在这一步正式解决以前，本轮不把任何诊断 D 系数送入 G15，
也不计算新的 Pcr/Pu。
