# NZ-SCCM — Case21 N48-C1/MM 五膜坐标 production continuation 启动执行报告

**时间：2026-08-16 22:34 +08:00**  
**门禁：`UNIFIED_V1_CASE21_MEMBRANE_REDISTRIBUTED_N48_PRODUCTION_GATE`**  
**本轮子门：`CASE21_N48_MEMBRANE_BASELINE_FINGERPRINT_AND_CONNECTED_START_GATE`**

## 0. 本轮结论

本轮没有从旧极限点直接硬解五个膜内未知量，而是完成了生产链必须先通过的两个动作：

1. 用当前 Case21 `N48-C1/MM + Cayley-Hamilton + equivalent Chebyshev-in-sine + General-D15` 系数空间实现重新回归 2026-08-12 18:02 的 `r=0` fresh Case21 指纹；
2. 从原点侧启动 five-term membrane continuation，并得到第一个非零的 connected equilibrium state，使五个 `Rm` 与总 `Rq` 同时接近零。

因此本轮状态为：

```text
N48_1802_LOAD_FINGERPRINT = PASS
N48_1802_GENERALIZED_WORK_FINGERPRINT = PASS_WITH_CANCELLATION_SENSITIVE_1E-6_REL_COMPONENT_ERROR
DIRECT_NEAR_LIMIT_FIVE_R_NEWTON = REJECTED_AS_START_STRATEGY
ORIGIN_CONNECTED_MEMBRANE_CONTINUATION = STARTED
FIRST_NONZERO_CONNECTED_POINT = PASS
NEW_MEMBRANE_REDISTRIBUTED_Pu = NOT_YET_RELEASED
```

没有读取试验值参与求解、没有空间数值积分、没有材料点网格。

---

## 1. 固定输入与正式身份

Case21：

```text
b = ell = 1220 mm
tp = 19.30 mm
fc = 21.23 MPa
E0 = 20321 MPa
eps0 = 0.00209
nu = 0.18
q0 = 1/400 = 0.0025
rho_sx = rho_sy = 0.00375
Es = 200000 MPa
fy = 530 MPa
```

材料 compiler：

```text
order = N48
interval = [-1.15, 0.12]
lambda_c = -0.515
lambda_h = 0.635
U = N48-C1
C = N48-C1
T = N48-C1-CONSTRAINED-MINIMAX
T7 = N48-C1
```

生产 source coefficient 文件：

`current/case21/NZ_SCCM_CASE21_FRESH_MATERIAL_COEFFICIENTS_20260812_1802.csv`

结构积分身份：

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

---

## 2. 系数空间实现

采用 `u=sin X, v=sin Y, zeta`。Case21 的 paired-cosine 结构允许把最终 scalar target 写成 equivalent Chebyshev-in-sine tensor；该表示只在完成与 General-D15 的代数等价后使用，不是空间 collocation。

二维对称矩阵写成 triplet

```text
A = [[a, cosX cosY h],
     [cosX cosY h, b]]
```

其中 `a,b,h` 都是 `T_i(u)T_j(v)T_k(zeta)` 的有限系数张量。乘积中的两个余弦因子解析化为

`cos^2 X cos^2 Y = (1-u^2)(1-v^2)`。

Chebyshev tensor 乘法通过对称 Laurent 系数卷积实现，最终结构积分由解析矩

`int_0^pi T_i(sin X)dX`, `int_0^pi T_j(sin Y)dY`, `int_-1^1 T_k(zeta)dzeta`

逐项收缩。FFT 只加速 coefficient-index convolution，不在物理空间采样。

为了辨认 18:02 指纹，本轮把 coefficient convolution 的纯浮点清理门收紧到 `1e-10`。这是数值实现噪声门，不获得材料/结构理论参数身份。`1e-5` 的历史记录仍保留为早期实现记录，不据此修改 R10 或 N48 coefficient。

---

## 3. 18:02 `r=0` 指纹回归

固定旧 fresh limit state：

```text
D = 0.7822850963110681
q = 0.0017707520964949533
r = [0,0,0,0,0]
```

18:02 冻结值与本轮重构值：

| quantity | 18:02 freeze | this run | difference |
|---|---:|---:|---:|
| `D15[Syy]` | -13.306145538701315 | -13.306145513409462 | +2.5291853e-8 |
| `D15[Qq]` | 4.479715227945151 | 4.479711739911862 | -3.4880333e-6 |
| `Pc` kN | 336.96877733325394 | 336.96877669275550 | -6.4049844e-7 |
| `Ps` kN | 28.61165023207581 | 28.61165023207579 | ~0 |
| `P` kN | 365.58042756532977 | 365.58042692483133 | -6.4049844e-7 |
| `Rq,c` kN mm | 289.26368646992213 | 289.26346124101434 | -2.2522891e-4 |
| `Rq,s` kN mm | -289.26278353076810 | -289.26278353076805 | ~0 |
| total `Rq` kN mm | +9.02939154e-4 | +6.77710246e-4 | -2.2522891e-4 |

对承载力 observable，绝对差仅 `6.4e-7 kN`；对两个约 `289 kN mm` 的 generalized-work 分量，component 相对差约 `7.8e-7`。总 `Rq` 本身是两大数相消，因此不以 total-residual 相对误差作为 fingerprint 指标。

该回归确认当前 reconstructed coefficient-space evaluator 与 18:02 fresh closure 属于同一数值实现族，可用于 continuation corrector。

---

## 4. 为什么不从旧极限点直接解 `Rm=0`

在旧 18:02 `(D,q)` 上先放入 classical elastic membrane predictor

`r/M = [-.295,-.205,.25,-.205,.25]`

得到五残量约

```text
Rm = [
 +2.56554825,
 +0.16092433,
 -0.36131871,
 -15.12577474,
 +2.53362129
]
||Rm||2 = 15.55463867
```

对该点作一次 generalized-coordinate finite-difference diagnostic（仅诊断，不作为 production tangent），得到局部 Jacobian condition number 约

`cond2(J) = 714.75`

且完整 Newton predictor 为

```text
Delta r = [-0.00350724,
           +0.00819312,
           +0.37631853,
           +0.10590527,
           -1.21333188]
```

这不是一个可接受的 connected-start 更新。它再次证明：五膜坐标必须从无载原点沿主支 continuation，而不能在旧极限点突然插入新的内部平衡条件。

---

## 5. 原点侧 first nonzero continuation point

选第一个 continuation 参数

`q = 1.0e-4`。

从线弹性 five-term predictor 开始。该点

`M = 0.0012041861829080321`。

线弹性 predictor：

```text
r_el = [-0.0003552349239578695,
        -0.0002468581674961466,
        +0.0003010465457270080,
        -0.0002468581674961466,
        +0.0003010465457270080]
```

零状态一致五膜切线由 R10 初始斜率和两向弹性钢筋解析得到：

```text
Krr0 =
[[448.677388,   0,          0,          0,          0],
 [  0,        224.338694,   0,          0,          0],
 [  0,          0,        156.573042,   0,         63.898000],
 [  0,          0,          0,        224.338694,   0],
 [  0,          0,         63.898000,   0,        156.573042]]
cond2(Krr0) = 4.8414047566
```

从 `D=0` 与 `D=.05` 的 Rq 符号夹逼开始，经 predictor/corrector 得到当前第一个非零 connected point：

```text
q = 0.0001000000000000000
D = 0.016046306000000000
r0  = -0.0004765646208971642
r20 = -0.0002322819318541890
r22 = +0.0002805628349612065
s02 = -0.0002432861950486819
s22 = +0.0003034158793738149
```

用正式 N=28 coefficient tensor evaluator 复核：

```text
Rm = [-4.4872582699e-6,
      -2.5232115220e-7,
      +2.3273888463e-7,
      -3.4212427008e-6,
      +3.9601355452e-6]
||Rm||2 = 6.9022384258e-6
Rq = +1.9082556149e-6 kN mm
Pc = 14.6815009486053 kN
Ps = 0.5811316255054 kN
P  = 15.2626325741107 kN
```

同一状态用 N=20 predictor evaluator 与 N=28 corrector evaluator所得上述量在显示精度内一致；N=20 仅作为 continuation predictor 加速，N=28 保持正式 corrector 身份。

---

## 6. compiler-domain 全域证书

本点

```text
Cm = 0.0012041861829080321
Cb = 0.0037352609016594366
```

不用空间扫描，直接对 `u,v in [0,1]`, `zeta in [-1,1]` 做解析 interval/Gershgorin enclosure。得到

```text
ex in [-0.00183633520937, +0.00786406231049]
ey in [-0.0203282689761, -0.0105601568410]
X11 in [-0.00567943739672, +0.00616291244223]
X22 in [-0.0213505677075, -0.00945083260141]
|X12| <= 0.00319617767449
```

故两个主值整体满足保守界

```text
-0.02454674538198 <= lambda_- <= lambda_+ <= +0.00935909011672
```

相对 compiler interval `[-1.15,0.12]` 的安全裕量：

```text
lower margin = 1.12545325461802
upper margin = 0.110640909883278
```

因此

`CONTINUOUS_COMPILER_DOMAIN_CERTIFICATE = PASS`。

---

## 7. 本轮门禁裁决与唯一下一步

```text
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
FORMAL_THICKNESS_QUADRATURE = 0
N48_1802_FINGERPRINT = PASS
FIVE_TERM_ZERO_STATE_TANGENT = PASS_EXACT
DIRECT_OLD_LIMIT_INSERTION = REJECTED
CONNECTED_CONTINUATION_START = PASS
FIRST_NONZERO_STATE = PASS
COMPILER_DOMAIN_CERTIFICATE_AT_FIRST_POINT = PASS
SCHUR_CONDENSATION_FULL_BRANCH = NOT_YET_RUN
LIMIT_POINT = NOT_YET_RUN
SAME_STATE_KZ_AT_NEW_BRANCH = NOT_YET_RUN
NEW_MEMBRANE_REDISTRIBUTED_Pu = NOT_RELEASED
```

唯一下一执行门：

`CASE21_N48_MEMBRANE_CONNECTED_BRANCH_CONTINUATION_AND_SCHUR_GATE`

从本文件冻结的 `q=1e-4` 状态继续递增 continuation parameter；每个接受状态同时闭合五个 `Rm` 与总 `Rq`，并保存 `r`, `Krr`, `cond(Krr)`, compiler-domain certificate, `P`, `Rq`。接近首个荷载极大值后再形成一致 Schur 导数与 same-state `KZ`，不得返回旧 `r=0` 根，也不得用试验值选根。