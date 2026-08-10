# NZ-SCCM PF1 执行合同与基础边界锁定

**日期：2026-08-10**  
**身份：CURRENT EXECUTION CONTRACT / USER-RECONFIRMED HARD BOUNDARY**

## 0. 用户本轮重新确认

本轮继续执行 `PF1 = finite Gauss-Manin / Picard-Fuchs closure for canonical M1R outer resolvent periods`，但无论数学表示如何变化、是否引入新的 special-function / differential-system representation，基础限制与项目主路径不得偏离。

本文件在 PF1 长计算前建立 GitHub checkpoint；它不修改材料物理、运动学或结构目标，只把不可退让边界重新写成执行门禁。

## 1. 永久硬边界

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT
ELEMENT_INTEGRATION = PROHIBITED
MATERIAL_POINT_GRID = PROHIBITED
SPATIAL_CELLS = PROHIBITED
GAUSS_SIMPSON_ADAPTIVE = PROHIBITED_IN_FORMAL_OPERATOR
COLLOCATION_AS_FORMAL_THEORY = PROHIBITED
```

辅助变量、period coordinates、Picard-Fuchs/Gauss-Manin state variables 只有在最终形成有限解析对象、有限 ODE/PDE system 或可解析求导的 named special functions 时才允许获得正式理论身份。

禁止：

```text
hard integral -> auxiliary variable -> numerical quadrature
```

任何 numerical quadrature 只能作为外部 audit/oracle，不得作为 formal operator、formal P/Rq/L 或 production material/structure contraction。

## 2. 结构主路径不得修改

继续固定：

```text
finite analytic kinematics
-> finite strain invariants
-> strong nonlinear material law
-> exact analytic material/structural contraction
-> P(D,q), Rq(D,q), analytic tangent, L(D,q)
```

其中

```text
Rq(D,q)=0
L(D,q)=P_,D Rq_,q-P_,q Rq_,D=0
```

PF1 只允许解决 outer analytic closure；不得因为 period 数学困难而修改 P、Rq、L 的结构力学定义、改变 Nguyen 二阶单半波运动学、恢复 FE/material-point path，或用经验 effective-width/strength cutoff 替代材料—结构闭合。

## 3. M1R 当前身份保持

```text
M1R_R01_FROZEN_NC_ORACLE_REGRESSION = PASS_SCREEN
FINAL_NC_SOURCE_CALIBRATION = NOT_YET_DONE
FINAL_GATE_B = NOT_YET_FROZEN
M1R_R01_S_INNER_INTEGRATION = PASS_CLASS_A
M1R_R02_OUTER_PERIOD_CLASS = HYPERELLIPTIC_RELATIVE / PICARD_FUCHS
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

PF1 不得把 frozen NC benchmark 自动升级为最终普通混凝土材料真理；也不得进入 Case21 Pu、Swartz24、UHPC production 或 shell/Y production。

## 4. PF1 唯一任务

```text
single-resolvent algebraic kernel
-> genus-2 de-Rham basis
-> Griffiths/Hermite derivative reduction
-> finite Gauss-Manin connection
-> relative/log endpoint extension
-> pair-resolvent closure
-> outer y-direction closure
-> whole-halfwave finite analytic differential system
```

当前优先执行 single-resolvent algebraic kernel；若该最小 canonical family 无法形成有限 closure，必须先报告具体失败点，不得私自转向数值积分或其他结构路线。

## 5. PASS / FAIL

PF1-PASS 至少要求：

1. canonical period family 有有限维解析 basis；
2. 对当前结构参数的导数能严格 reduce 回同一有限 basis（Gauss-Manin closure）；
3. branch/singularity loci 可显式定义；
4. relative/log periods 有有限扩展或可严格约化；
5. 最终 evaluator 不依赖 spatial/auxiliary numerical quadrature；
6. 可形成 analytic D/q derivatives，供 tangent 与 L 使用。

PF1 若只证明“period 理论上 holonomic”，但不能给出当前 M1R canonical blocks 的实际有限 reduction system，则仍保持 `Gate A = HOLD`。

## 6. 本轮明确禁止

```text
NO Case21 Pu solve
NO Swartz24 solve
NO UHPC production fit
NO shell/Y production solve
NO structural-load calibration
NO formal numerical quadrature
NO route substitution
```
