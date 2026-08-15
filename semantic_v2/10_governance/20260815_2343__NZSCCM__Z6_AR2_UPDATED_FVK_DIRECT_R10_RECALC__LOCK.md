# NZ-SCCM — Z6 AR2 更新膜力重分布完整理论重算身份锁

**Timestamp:** 2026-08-15 23:43 +08:00  
**Identity:** `Z6_AR2_UPDATED_FVK_R10_DIRECT_CONTINUUM_AUDIT_RECALC`

## 1. 用户指令对应的计算对象

本轮不再围绕原 Z6 的 `D=.50` 局部 checkpoint 继续推进，而直接重算此前已建立的 **Z6 长宽比大于 1 比较板**：

```text
a/b = 2.0
a = 24000 mm
b = 12000 mm
m = 2
ell = a/m = 12000 mm
```

因此正式面外生产域仍然只取一个连续完整代表半波 `ell=12000 mm`，不是两个空间子域，也不是两个独立面外模态。

## 2. 更新后的完整力学系统

保持：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
single (1,1) representative out-of-plane halfwave
current concrete physical operator = frozen R10
local steel radial-cap current operator
A0=a/500
```

并正式释放最小 FvK 面内膜力重分布坐标：

```text
m = [c,p20,p02]^T
```

每个给定 D 的平衡系统：

```text
Rq=0
Rc=0
R20=0
R02=0
unknowns [q,c,p20,p02]
```

`p20,p02` 只是面内重分布坐标，不是新增面外模态。

## 3. 本轮积分/结果身份

为了直接回答“更新完整力学对 AR2 Z6 给出什么路径和峰值”，本轮绕过当前 N48 dense-Cayley-Hamilton representation/runtime gate，直接评价同一冻结 R10 物理 current map，并用高阶 Gauss-Legendre 作为 **continuum audit executor** 求解四广义平衡。

因此必须锁定：

```text
UPDATED_FVK_MECHANICS = ACTIVE
R10_PHYSICAL_CURRENT_OPERATOR = UNCHANGED
FORMAL_N48_D15_PRODUCTION_RELEASE = NO
GAUSS_EXECUTOR = AUDIT_ONLY
N_formal_spatial_sampling = 0   # 正式理论治理不因此改变
N_formal_spatial_quadrature = 0 # 正式理论治理不因此改变
N_formal_spatial_subdomains = 1
```

本轮数值结果不得冒充正式 N48/D15 零空间积分 production certificate；它是完整更新力学的 R10 direct-continuum audit 结果。

## 4. 当前钢构件对象边界

当前 NZ equilibrium operator 中钢材对象仍是两块 faceplates / reduced two-face steel shell。此前 H0 已证明 longitudinal PBL/web steel phase 对截面强度基线重要，但该 phase 尚未进入当前 `q,c,p20,p02` 广义平衡。

因此：

```text
PBL_WEB_PHASE_IN_AUGMENTED_EQUILIBRIUM = NOT_YET_INCLUDED
FULL_ZHOU_SECTION_CAPACITY_IDENTITY = NO
```

不得把本轮 Pu 称为“含完整 PBL/web 钢相的 Z6 最终物理截面承载力”。

## 5. 本轮峰值锁定

高阶 continuum audit 给出更新膜力平衡峰值约：

```text
D_peak ≈ 0.8308
q_peak ≈ 0.01712
c ≈ -0.538
p20 ≈ -0.700
p02 ≈ +0.697
Pu ≈ 40.97 MN
```

160x160x60 audit at D=.8308:

```text
P = 40.9733400613 MN
lambda range ≈ [-1.13695,+0.47949]
steel trial rmax ≈ 1.30146
```

局部钢屈服在峰值附近已激活。

## 6. 解释边界

历史 AR2、未释放 `c,p20,p02` 完整膜力平衡的 R10 direct-continuum audit 峰值为 `44.5529191054 MN`。本轮约 `40.97334 MN`，下降约 8.03%。

因此必须保留以下结论：

```text
MEMBRANE_REDISTRIBUTION_IS_MECHANICALLY_ACTIVE = YES
MEMBRANE_REDISTRIBUTION_AUTOMATICALLY_RAISES_Pu = NO
```

当前更新理论在 reduced two-face steel object 上反而降低峰值；不得为了贴近 Zhou/Winter 而选根、调参或删除 p20/p02。
