# NZ-SCCM — BH050 16:23 执行方法审计与结果降级 R01

**Time:** 2026-08-27 16:35 +08:00  
**Status:** `METHOD_AUDIT / NO_SPATIAL_QUADRATURE_FOUND / NUMERICAL_SPATIAL_OPTIMIZER_FOUND / 15.133 MN DEMOTED / 1710 CLOSURE NOT ACCEPTED AS PRODUCTION`

## 0. 审计对象

- `semantic_v2/20_theory/20260827_1710__NZSCCM__SINGLE_EXPLICIT_BH_CURRENT_MOMENT_HARMONIC_CLOSURE_R01.md`
- `semantic_v2/40_execution/steel_shell/20260827_1623__NZSCCM__BH_EXPLICIT_CURRENT_MOMENT_SOLVER_R01.py`
- `semantic_v2/40_execution/steel_shell/20260827_1623__NZSCCM__BH050_EXPLICIT_CURRENT_MOMENT_FULL_LEDGER_R01.md`

本审计只判断上一轮实际用了什么数值方法，以及 15.13300655067 MN 的证据身份；不建立新理论、不重新计算 BH050。

## 1. 数值积分审计

对保存的 R01 solver 逐项检查：

```text
scipy.integrate = absent
mp.quad = absent
quad/dblquad/nquad = absent
trapz = absent
simpson = absent
linspace/grid integration = absent
```

UHPC 厚度 resultant 使用 S0/S1 endpoint primitives；web 使用 affine ideal-EP piecewise primitives；qU 几何系数来自 rational finite-harmonic backend。

因此：

```text
NUMERICAL_SPATIAL_QUADRATURE_USED = NO
NUMERICAL_THICKNESS_QUADRATURE_USED = NO
```

## 2. 但实际用了数值空间优化

R06 GL+LL 连续局部 Mises 最大值并未在 16:23 solver 中使用正式有限代数 resultant certificate，而是调用：

```python
scipy.optimize.minimize(... method="L-BFGS-B" ...)
```

从若干确定性起点在 local cell 的 `(x/B,y/B)` 连续域中寻找最大值。

同时使用：

- `brentq`：求 R06 radial parameter `eta`；
- `least_squares`：求最终 `(q,Ax)` 的 `Rx=Ry=0`。

所以准确身份应为：

```text
SPATIAL_QUADRATURE = 0
SPATIAL_GRID = 0
NUMERICAL_SPATIAL_STATIONARY_SEARCH = YES
NESTED_NUMERICAL_ROOT_SOLVES = YES
```

这不是数值积分，但它不是项目要求的正式 finite-algebraic local-Mises extremum backend。上一轮将其描述为“完整正式计算”过度。

## 3. 1710 current-moment harmonic closure 的身份

1710 文件引入了新的 reduced closure：

- 用 antinode current section moments `Mx_sec, My_sec` 作为 retained global sine harmonic amplitudes；
- 用该一阶谐波 current moment 替换原 elastic `Kb*b*q`；
- nonlinear twist 仍保留 initial `D66`。

其 elastic regression 正确，但该 regression 只能证明弹性极限一致，不能证明 nonlinear BH050 生产闭合正确。

因此在用户未接受前：

```text
1710_CURRENT_MOMENT_HARMONIC_CLOSURE = EXPERIMENTAL / UNACCEPTED
```

不得因为它可计算就自动升级为正式主线。

## 4. 1623 R02 U=0 active-set 的身份

16:23 solver 为避免旧 `U>=0` 内部驻值根在 BH050 上消失，新增了 constrained minimization boundary candidate `U=0`。

这是数学上的 KKT completion，但它是上一轮新增的 solver interpretation；在来源/既有 R02 contract 未单独验收前：

```text
R02_U0_ACTIVESET_COMPLETION = UNACCEPTED_SOLVER_EXTENSION
```

不得用它单独证明原理论“本来就有根”。

## 5. 15.13300655067 MN 的证据身份

由于：

1. R06 使用 numerical spatial stationary optimization，而非正式 finite-algebraic certificate；
2. 1710 current-moment harmonic closure 是未验收的新 reduced closure；
3. R02 `U=0` active-set 是未验收的 solver extension；

所以：

```text
BH050_15.13300655067_MN = DIAGNOSTIC_ONLY
PRODUCTION_PU = NO
METHOD_ACCEPTED = NO
```

该数值不得作为后续试件计算基准，也不得用于判断“修复后理论反而更差”这一正式结论。

## 6. 当前恢复边界

本审计不删除历史文件，避免破坏证据链；但明确 supersede 它们的 production 身份。

下一次理论/数值执行前必须先回到用户要求的显式 Airy -> current N-M 主线，并只允许来源已经接受的闭合关系。不得再因为一个局部缺口自动升级成 full-current global theory，也不得把 numerical stationary optimizer 偷换成“零数值方法”。

```text
FORMAL_NUMERICAL_INTEGRATION_VIOLATION = NOT_FOUND
FORMAL_NUMERICAL_SPATIAL_EXTREMUM_BACKEND = NOT_SATISFIED
LAST_1623_RESULT_PRODUCTION_STATUS = REVOKED
NO_NEW_THEORY_IN_THIS_AUDIT = TRUE
```