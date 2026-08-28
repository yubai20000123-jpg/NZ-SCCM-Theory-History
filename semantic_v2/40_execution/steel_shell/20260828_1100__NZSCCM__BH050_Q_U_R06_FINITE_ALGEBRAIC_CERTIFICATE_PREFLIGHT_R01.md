# NZ-SCCM — BH050 qU-on R06 有限代数认证前置审计 R01

**Time:** 2026-08-28 11:00 +08:00  
**Status:** `FORMAL LOW-DEGREE R06 CERTIFICATE DOES NOT CARRY OVER UNCHANGED / NO QUADRATURE / NO THEORY UPGRADE EXECUTED`

## 0. 执行目标

按 2026-08-27 恢复后的原始显式 demand-capacity contact 主线，仅检查唯一剩余问题：

> 已加入 qU 的 GL+LL 局部钢板应力场，能否直接复用 2026-08-25 common R06 的低阶 `(u,v)=(cos kx x, cos ky y)` 多项式有限代数极值后端，从而把 BH050 `Pu=13.29348446718 MN` 从 pre-certified 提升为 formal？

本节点不改 Airy、不改 UHPC N-M、不改 web、不改 terminal 5×5 contact、不强制 terminal curvature、不引入 current-moment feedback。

## 1. qU-off formal R06 的已冻结代数结构

common R06 在 qU-off R02 场中只有局部谐波

```text
(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)
```

因此令

`u=cos(kx*x), v=cos(ky*y)`

以后，normal stresses 是 `(u,v)` 的有限低阶多项式，shear 的平方也能消去根号；Mises 平方

`Phi = sx^2 - sx*sy + sy^2 + 3*tau^2`

成为总次数不超过 6 的多项式。正式候选集是 interior resultant roots + four edges + four corners，零空间网格、零数值积分。

这就是 `20260825_1535__...R06_LOCAL_YIELD_RESULTANT_GATE.py` 的正式有限代数后端。

## 2. qU-on 后的精确 Fourier support

20260827 的 exact qU geometry backend 使用 global halfwave `psi=sin(pi x/B)sin(pi y/B)` 与 local PBL mode 的 GL cross term。所有频率仍是精确有理数，并未使用空间积分。

对 BH self-similar cell，局部 LL support（将 x-frequency 乘 9 以去掉分母）为：

```text
9*a_x in {0, ±80, ±160}
y-frequency in {0, ±9, ±18}
```

而 qU GL support 新增：

```text
9*a_x in {±9, ±71, ±89}
y-frequency in {±1, ±8, ±10}
```

具体非零 GL frequency pairs 共 32 个，例如

```text
(9*a_x, a_y)=
(±89,±10),(±89,±8),(±89,±1),
(±71,±10),(±71,±8),(±71,±1),
(±9,±10),(±9,±8)
```

连同 LL 后，当前 exact stress kernel 共 54 个 signed Fourier frequencies。

## 3. 关键裁决：原低阶 `(u,v)` 多项式证书不能直接复用

原 R06 的 `u=cos(kx*x)` 对应 local frequency `kx=80*pi/(9B)`。qU GL 中同时含 global `pi/B`，即 local frequency ratio `9/80`。

因此诸如

`cos[(80/9 ± 1) pi x/B]`

无法写成 `u=cos(kx*x)` 的有限低阶 Chebyshev polynomial。于是 qU-on 的 `Phi` 不再是原 R06 所声称的 degree<=6 polynomial in `(u,v)`。

若强行继续调用旧 `phi_polynomial()`，会**漏掉全部 GL mixed harmonics**，得到的是 qU-off certificate，不是 qU-on certificate。

因此：

```text
REUSE_20260825_LOW_DEGREE_PHI_POLYNOMIAL_UNCHANGED = INVALID
```

这不是数值问题，而是精确频率代数结构已经改变。

## 4. 是否必须升级成巨大 resultant？——本节点明确不执行

因为所有 x frequencies 的 denominator 只有 9，可以定义基础角

`theta_x = pi*x/(9B)`

使全部 x Fourier orders 变为整数，最大 order 为 160；y 最大 order 为 18。于是 qU-on field 当然仍可以通过 unit-circle / tangent-half-angle 变成有限代数系统。

但那会把原先 degree<=6 的 R06 certificate 升级为高阶 two-variable algebraic elimination，属于新的复杂求解后端。当前用户边界明确要求不得为了一个认证问题把理论/后端重新升级成难以维护的高阶 resultant 系统。

所以本节点**不**把这一事实当作继续升级的许可。

## 5. BH050 当前 pre-certified 状态的直接核对

恢复后的正式结构/容量主线保持：

```text
q = 0.004715120492577262
Pu = 13.29348446718 MN
Ax = 1.98641610447e-5
Bx = 4.42205818884e-5 1/mm
Ay = -0.00213259496557
By = 6.51145254490e-5 1/mm
```

qU-on terminal face states：

```text
TOP:
eta = 1
U = 0.01727562617 mm
mean = (+189.0570,-75.8976,0) MPa

BOTTOM:
eta = 0.38380722563
U = 2.84115552117 mm
mean = (-59.1766,-217.8308,-0.4205) MPa
```

作为**诊断而非 formal certificate**，用完整 54-frequency analytic field 的连续驻点求值仍回归：

```text
TOP max VM ≈ 239.917 MPa < fy
BOTTOM max VM ≈ 355.000 MPa
```

bottom active point 位于 central cell interior，约

```text
x/B ≈ 0.47862062
y/B ≈ 0.55555994
```

所以 pre-certified R06 物理状态本身没有出现明显漂移；问题只在 formal algebraic certificate 的低阶表示不再适用。

## 6. 本节点最终状态

```text
SPATIAL_QUADRATURE_USED = NO
THICKNESS_QUADRATURE_USED = NO
MATERIAL_POINTS_USED = NO
NUMERICAL_SPATIAL_OPTIMIZATION_USED_FOR_FORMAL_CERTIFICATE = NO

Q_U_EXACT_HARMONIC_BACKEND = PASS
OLD_R06_LOW_DEGREE_POLYNOMIAL_CERTIFICATE_WITH_Q_U = FAIL_NOT_APPLICABLE
BH050_13.29348446718_MN = RETAIN_PRE_CERTIFIED
BH050_FORMAL_PROMOTION = NOT YET
HIGH_DEGREE_RESULTANT_ESCALATION = NOT EXECUTED
```

## 7. 下一步边界

不能再说“只要把旧 R06 polynomial routine 换进去就能 formalize”。真正可接受的下一步必须二选一，并且在执行前先保持理论主线不动：

1. **寻找 qU GL stress 在 R06 first-yield gate 中可由来源/现有推导合法凝聚的更低阶表达**，如果存在，则保持原有限低阶风格；
2. 若不存在，则明确 qU-on R06 formal certificate 本身需要高阶 finite-trigonometric all-root backend，并由用户决定是否值得为了约 0.47% 的 Pu 修正承担该复杂度。

在没有这个裁决前，不允许偷偷用旧 qU-off `Phi(u,v)` 给 qU-on 结果盖 formal 章，也不允许用 L-BFGS/grid 冒充 finite-algebraic certificate。