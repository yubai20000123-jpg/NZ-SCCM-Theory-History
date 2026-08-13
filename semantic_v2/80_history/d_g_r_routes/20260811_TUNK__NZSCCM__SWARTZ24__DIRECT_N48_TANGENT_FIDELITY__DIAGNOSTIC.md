# NZ-SCCM P1 — Swartz 24块板 current tangent / Attard / 周思铭稳定审计

**身份：DIAGNOSTIC ONLY — NO MATERIAL CHANGE, NO CALIBRATION.**

本审计固定已经冻结的24块理论极限状态 `(D_u,q_u,Pu)`，不重算、不调参。目的只是在这些状态上追踪：

`R10 material target tangent -> N48 tangent -> Attard orthotropic proxy -> Zhou-form directional stiffness decomposition -> full-field generalized tangent`。

## 1. 两种 tangent 身份必须区分

- **R10 target tangent**：由闭式 R10 current material operator 本身直接求导；只作为 N48 表示忠实性的材料级基准。
- **N48 current tangent**：当前生产 N48 有限解析表达的同式导数；这是现有极限条件 L 实际依赖的切线。
- **Attard proxy**：把当前点的加载方向 tangent 放进 Attard 正交异性小扰动公式；只作诊断，不把 `E_trans=0.4E0` 移植到 R10。
- **Zhou-form proxy**：按 `Dx, Dy, H` 的思路分解当前切线对 Navier 稳定项的贡献；不是把周思铭的组合墙材料公式替换到 RC 板。

## 2. P1 的首要发现：第一处明确偏离出现在 N48 的切线忠实性，而不是 R10 材料目标

闭式 R10 在 `lambda=0` 有严格材料锚点：

`C(0)=T(0)=T^7(0)=0`, 且 `C'(0)=T'(0)=(T^7)'(0)=0`。

24块板按当前冻结的 N48 通式重新生成后，得到：

- `T_48(0)` 范围：-0.001473 ～ +0.059057；
- `T_48'(0)` 范围：+8.689 ～ +11.364，而 R10 目标为 0；
- N48 normal-tangent 非对称性相对 R10 target 被放大约 23.1～31.1 倍，平均 27.7 倍。

这不是试验相关性推断，而是**同一个材料目标与其有限解析表示之间的直接恒等式审计**。

在完整半波中心 `X=Y=pi/2, zeta=0`，有 `lambda_+=0, lambda_-=-D_u`。此处最适合与 Attard 的均匀压缩切线思想做对照。

### 三组加载方向切线比的组平均

|组|mean D_u|R10 target `E_parallel,t/E0`|N48 `E_parallel,t/E0`|
|---|---:|---:|---:|
|1-8|1.042|-0.0195|0.9928|
|9-16|1.083|-0.0360|0.9362|
|17-24|0.902|+0.0599|0.9659|

闭式 R10 清楚保留了三个区间：Case1–16 的中心加载方向 tangent 已接近零或进入负切线，而 Case17–24 仍保持小的正切线。当前 N48 却把24块几乎全部拉回到约 `0.8~1.08 E0`。

R10 target 加载切线为正的板仅为：[1, 2, 17, 18, 19, 20, 21, 22, 23, 24]。其余板在中心状态已经越过正切线范围。

因此，在 P1 层面，**N48 值函数可以仍较接近 R10，但其一阶导数并没有忠实保留 R10 在压缩峰值附近的 tangent degradation。**

## 3. Attard 对照的意义

Attard 的核心不是一个经验折减，而是正交异性切线板：加载方向采用当前 `Et`，非加载方向以 `0.4Ec` 作为其开裂弯曲近似；并由两方向 tangent 的比例决定最有利半波数和屈曲系数。

在 R10 target tangent 下，Case3–16 的中心加载 tangent 为非正，因此 Attard 的正切线小扰动公式在理论极限状态已经超出直接适用域；这恰好说明这些状态已处于材料峰值/峰后与有限幅值耦合区。Case17–24 仍为正切线，但 Attard margin 在 Pu 时小于1，说明完美基态应早已发生分岔，有限幅值路径继续承载是合理的。

而 N48 tangent 使24块的加载方向 tangent 几乎恢复成弹性量级，从而让 Attard proxy 在许多 Case9–16 上仍给出 `margin>1`。这与它们已经具有非零有限幅值、且试验 Pcr 明显早于 Pf 的物理身份不协调。

## 4. 周思铭视角：不能只看加载方向 Et，必须看 Dx、Dy、H 的共同贡献

周思铭四边简支正交各向异性稳定理论强调：轴压稳定并不是一个单独 `Et` 控制，而由主方向抗弯刚度 `Dy`、次方向抗弯刚度 `Dx`、以及包含泊松/扭转作用的 `H` 共同贡献；并且弹性与弹塑性状态下强度控制—稳定控制的临界宽厚比会显著移动。

本审计因此采用等价切线分解：

`Dx=C_xx,t t^3/12`, `Dy=C_yy,t t^3/12`, `Dmu=(C_xy,t+C_yx,t)t^3/24`, `D66=G_t t^3/12`, `H=Dmu+2D66`。

这只是把当前 RC material tangent 映射到周思铭式的刚度语言，**不导入周论文的组合墙截面材料参数**。

### 三组 Zhou-form 刚度审计

|组|R10 target margin|N48 margin|N48/R10 H 平均放大|full-field Rqq/(Pu b)|当前平均误差|
|---|---:|---:|---:|---:|---:|
|1-8|0.883|3.673|6.60×|9.732|+4.43%|
|9-16|1.275|5.169|6.56×|16.190|-13.23%|
|17-24|0.640|2.378|5.47×|3.078|-2.07%|

24块整体上，N48 对 Zhou-form `H` 的放大为 4.72～6.79 倍，平均 6.21 倍；相应中心模态稳定 margin 被放大 3.28～4.42 倍，平均 3.97 倍。

更关键的是贡献构成发生改变：

- R10 target：`Dx` 约贡献 47–50%，`2H` 约46–51%，`Dy` 在峰值附近仅约 -2%～+3%，钢筋为小量；
- N48 tangent：`2H` 被推到约75%，`Dx` 仅约12–13%，`Dy` 又被恢复到约11%。

也就是说，**周思铭所强调的刚度分项本身正好帮助定位了误差：当前 N48 导数主要不是简单把 `Dy` 稍微算偏，而是重构了整个 `Dx–Dy–H` 稳定刚度构成，尤其把 H 项显著放大。**

## 5. 与 Swartz 原始 fcr/fc' 和当前误差的一一对应

|指标|Spearman rho vs error|p|Spearman rho vs fcr/fc'|p|
|---|---:|---:|---:|---:|
|R10 target loaded tangent ratio|+0.219|0.3036|-0.599|0.001984|
|N48 loaded tangent ratio|+0.210|0.3236|-0.114|0.596|
|Zhou-form margin, R10 tangent|-0.434|0.03413|+0.797|3.161e-06|
|Zhou-form margin, N48 tangent|-0.321|0.1263|+0.719|7.648e-05|
|Full-field Rqq/(Pu b)|-0.397|0.05449|+0.771|1.028e-05|

最值得保留的统计解释有两点：

1. R10 target 的加载 tangent 比与实验 `fcr/fc'` 显著负相关：实验越接近材料峰值，R10 target 在理论 Pu 状态也越接近零/负 tangent。这是材料非线性机制的一致方向。
2. full-field `Rqq/(Pu b)` 与 `fcr/fc'` 仍有很强关联，但它是已包含材料、几何、钢筋及有限幅值耦合的广义切线，不等于单一材料 `Et`。

## 6. 当前裁决

```text
R10_MATERIAL_TARGET = NOT_CHANGED
SWARTZ24_PU_VALUES = NOT_RECALIBRATED
P1_CURRENT_TANGENT_AUDIT = COMPLETE
N48_VALUE_REPRESENTATION = NOT_REOPENED_IN_THIS_STEP
N48_TANGENT_FIDELITY_AT_LAMBDA_ZERO = FAIL_DIAGNOSTIC
FIRST_CLEAR_MECHANICAL_DEVIATION = R10_TARGET -> N48_FIRST_DERIVATIVE
ATTARD_COMPARISON = DIAGNOSTIC_ONLY
ZHOU_Dx_Dy_H_DECOMPOSITION = DIAGNOSTIC_MAPPING_ONLY
STRUCTURAL_CALIBRATION = NO
```

这项 FAIL 的含义不是立即更改 N48，更不是回头调 R10；它只说明：**在继续把24板误差解释成‘材料模型不够好’或‘后屈曲自由度不足’之前，必须先承认当前 N48 对 R10 的一阶 tangent 并不忠实。**

因此当前24块 Pu 可继续作为已经完成的 blind value-closure 记录保存，但其 `L=0` 所依赖的同式 tangent 物理解释必须标记为 `PENDING_TANGENT_REPRESENTATION_REVIEW`。

## 7. 逐板表

|Case|fcr/fc'|误差/%|R10 eta_parallel|N48 eta_parallel|R10 Zhou margin|N48 Zhou margin|H放大|Attard R10状态|Rqq/(Pu b)|
|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
|1|0.661|+22.30|+0.0031|1.0553|0.831|3.586|6.59×|VALID_POSITIVE_TANGENT|9.269|
|2|0.543|+15.95|+0.0029|1.0547|0.905|3.905|6.59×|VALID_POSITIVE_TANGENT|10.443|
|3|0.572|+15.09|-0.0169|1.0367|0.895|3.827|6.79×|BEYOND_POSITIVE_TANGENT_RANGE|9.976|
|4|0.739|+2.35|-0.0122|1.0402|1.008|4.312|6.74×|BEYOND_POSITIVE_TANGENT_RANGE|11.749|
|5|0.773|-14.19|-0.0264|0.9454|0.930|3.736|6.44×|BEYOND_POSITIVE_TANGENT_RANGE|10.403|
|6|0.696|-12.49|-0.0335|0.9415|0.778|3.122|6.52×|BEYOND_POSITIVE_TANGENT_RANGE|8.086|
|7|0.702|-6.24|-0.0353|0.9376|0.858|3.443|6.54×|BEYOND_POSITIVE_TANGENT_RANGE|9.049|
|8|0.641|+12.64|-0.0380|0.9312|0.861|3.453|6.57×|BEYOND_POSITIVE_TANGENT_RANGE|8.883|
|9|0.745|-15.52|-0.0070|1.0610|1.293|5.718|6.78×|BEYOND_POSITIVE_TANGENT_RANGE|16.831|
|10|0.866|-21.51|-0.0058|1.0623|1.430|6.314|6.76×|BEYOND_POSITIVE_TANGENT_RANGE|18.844|
|11|0.798|-19.01|-0.0275|0.9894|1.454|6.042|6.70×|BEYOND_POSITIVE_TANGENT_RANGE|18.708|
|12|0.740|-14.08|-0.0343|0.9575|1.026|4.176|6.66×|BEYOND_POSITIVE_TANGENT_RANGE|12.373|
|13|0.614|+8.90|-0.0502|0.9016|1.211|4.772|6.59×|BEYOND_POSITIVE_TANGENT_RANGE|15.127|
|14|0.706|-12.02|-0.0395|0.9103|1.359|5.355|6.46×|BEYOND_POSITIVE_TANGENT_RANGE|17.368|
|15|0.785|-13.48|-0.0566|0.8074|1.293|4.770|6.17×|BEYOND_POSITIVE_TANGENT_RANGE|16.380|
|16|0.784|-19.11|-0.0669|0.8005|1.137|4.204|6.33×|BEYOND_POSITIVE_TANGENT_RANGE|13.893|
|17|0.668|-21.56|+0.0541|0.9395|0.639|2.339|5.39×|VALID_POSITIVE_TANGENT|3.448|
|18|0.638|-8.86|+0.0371|0.9238|0.679|2.528|5.50×|VALID_POSITIVE_TANGENT|4.466|
|19|0.543|-4.62|+0.0573|0.9416|0.635|2.317|5.36×|VALID_POSITIVE_TANGENT|3.026|
|20|0.575|-5.43|+0.0932|0.9717|0.632|2.233|5.14×|VALID_POSITIVE_TANGENT|2.454|
|21|0.572|-0.03|+0.1078|0.9117|0.627|2.054|4.72×|VALID_POSITIVE_TANGENT|2.140|
|22|0.516|+4.04|+0.0801|0.8907|0.628|2.110|4.87×|VALID_POSITIVE_TANGENT|2.420|
|23|0.531|+8.93|+0.0218|1.0707|0.658|2.799|6.43×|VALID_POSITIVE_TANGENT|3.511|
|24|0.513|+10.98|+0.0280|1.0773|0.625|2.643|6.37×|VALID_POSITIVE_TANGENT|3.156|
