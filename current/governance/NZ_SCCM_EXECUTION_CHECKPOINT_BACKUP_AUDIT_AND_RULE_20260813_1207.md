# NZ-SCCM 执行断点备份审计与可恢复计算规则

**时间：2026-08-13 12:07 +08:00**  
**身份：CURRENT GOVERNANCE / BACKUP AUDIT**

## 0. 审计结论

当前 GitHub 并未丢失理论和既有结果，但此前备份标准偏向“结果归档”，没有达到“任意新会话可从中断点无损续算”的 execution-checkpoint 标准。

因此当前应区分：

```text
THEORY_BACKUP = SUBSTANTIAL / CURRENT GOVERNING FILES PRESENT
CASE21_RESUMABLE_CHECKPOINT = COMPLETE
SWARTZ24_FINAL_Pu_TABLE = 24/24 PRESENT
SWARTZ24_CURRENT_RESUMABLE_CHECKPOINT = INCOMPLETE
SWARTZ24_CURRENT_ROOT_COORDINATES = 6/24 RETAINED IN CURRENT FRESH PACKAGE
SWARTZ24_CURRENT_FULL_DERIVATIVE_CHECKPOINT = NOT 24/24 RETAINED
SWARTZ24_CURRENT_KZ_CHECKPOINT = CASE21 COMPLETE / OTHERS NOT BULK-COMPLETE
```

## 1. 已确认存在的当前备份

### 1.1 Governing theory and state

- `current/CURRENT_STATE.md`
- `current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_ANALYTIC_LIMIT_TANGENT_UNIFIED_THEORY_20260812_1734.md`
- `current/workflows/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_EXECUTION_CONTRACT_20260812_1734.md`

当前不变量：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

### 1.2 Case21

Case21 当前具有可恢复的：原始输入、材料系数、理论冻结、最终 `(D_u,q_u,A_u)`、`Pc/Ps/Pu`、`R`、`L`、KZ 分解、同支第一 KZ 零点以及实验后开封比较。因此 Case21 达到 resumable-checkpoint 水平。

### 1.3 Swartz24 已完成的最终量

`current/results/NZ_SCCM_SWARTZ24_CURRENT_FRESH_PU_FAILURE_COMPARISON_20260813_0047.csv` 已保存 24/24 当前 `Pu` 与实验 `Pf` 比较。

Cases19–24 的 current fresh 结果另保留了当前 `(D_u,q_u)` 及 `Pc/Ps/Pu`。Case21 进一步保留完整 tangent/KZ 数据。

## 2. 发现的备份缺口

### 2.1 最大缺口：Cases1–18 current root checkpoint 未被持久化

当前 24/24 `Pu` 已存在，但 inspected current fresh package 中 Cases1–18 没有与这些 current `Pu` 一一对应的 `(D_u,q_u,A_u)` checkpoint。

历史文件 `NZ_SCCM_SWARTZ24_FRESH_BLIND_THEORY_RESULTS_20260811.csv` 确实保存了 24/24 的旧 direct-N48 `(D_u,q_u)`、`P_D,P_q,R_D,R_q,L` 等，但这些属于被 tangent-representation 审计后淘汰的旧表示，不能作为 current C1/MM + general-D15 根继续使用。

### 2.2 current 24-panel derivative checkpoint 不完整

对于 current 生产结果，应在极限状态同步保留：

- `P_D`
- `P_q`
- `R_q,D`
- `R_q,q`
- `L=P_D R_q,q-P_q R_q,D`
- `L_normalized`
- equilibrium residual
- branch direction / `dP/ds` sign before and after root

这些量在旧 direct-N48 24-panel CSV 中曾完整保存，说明原计算流程本身会产生它们；问题是 current 修订后的 24-panel 结果没有按同样粒度重新持久化。

### 2.3 current KZ checkpoint 未形成 24-panel machine-readable table

Case21 已保存：

- `KZ_c_mat`
- `KZ_c_geo`
- `KZ_s_mat`
- `KZ_s_geo`
- `KZ_total`
- first same-branch `KZ=0` coordinate

但尚无对应的 current Swartz24 24行生产表。

### 2.4 current material compiler checkpoint 不完整

Case21 当前材料系数有 timestamped CSV；24板 current run 未找到统一的每板 current C1/MM coefficient checkpoint。若需要从任意中断点继续，不应只依赖“以后可重新生成”。至少应保存 compiler interval、compiler variant、coefficient checksum/hash；大系数表可按文件分离保存。

### 2.5 current 24-panel canonical raw-input freeze 缺一个统一机器表

原始 Swartz 24板输入可从 Nguyen Table 5.1 和已有历史结果恢复，但 current production 应额外存在一张独立 raw-input freeze，明确每板：geometry、`fc,E0,eps0,nu`、reinforcement split/layers/location、steel properties、`q0` 来源、代表半波规则、compiler interval source。

“可从文献恢复”不等于“当前执行断点已备份”。

### 2.6 workflow 文档存在版本陈旧问题

`current/workflows/NZ_SCCM_CASE21_CALCULATION_PROCESS_TEMPLATE_V1_20260811.md` 仍写旧 direct-N48 根点插值公式。当前真正 governing workflow 已是 timestamped 20260812 zero-spatial analytic execution contract，并包含 C1/MM/general-D15/tangent control。

因此旧 V1 必须标记为 HISTORY/OBSOLETE FOR CURRENT PRODUCTION，不能再作为当前续算入口。

## 3. 对 “L/KZ bulk gate” 名称的纠正

此前把 `L` 与 `KZ` 合称一个后置 bulk gate 容易造成错误印象。

### 3.1 L 不是 Pu 算完后的额外门禁

当前 Pu 定义本身就是同一 equilibrium branch 上的第一极限点：

`Rq(D,q)=0` 与 `L(D,q)=0`，并要求沿主支 `dP/ds : + -> -`。

因此：

```text
CURRENT_Pu_EXISTS
=> current solve must have evaluated Rq and L at the root
```

对 Cases1–18 真正的问题是 **current L/root intermediate values 没有保存到 GitHub checkpoint**，而不是“Pu 已经算出来但当时根本没有算 L”。

### 3.2 KZ 才是独立的额外一致性/稳定性审计

KZ 用同一 current tangent 检查在 Pu 之前是否已有 tangent-zero。它不作为第二套 Pu 求解器。

所以以后状态名称改为：

```text
PU_LIMIT_POINT_SOLVE = Rq + L + branch maximum
KZ_PRELIMIT_STABILITY_AUDIT = independent same-branch audit
```

不得再用“L/KZ 后置门禁”掩盖 L 已经属于 Pu 求解本体这一事实。

## 4. 新的最低可恢复 checkpoint 标准

从本规则生效后，每块板只有在下列 RESUME_MINIMUM 已提交 GitHub 后，才能标记 `CALCULATION_COMPLETE`：

| 类别 | 必须保存 |
|---|---|
| identity | case id, theory-baseline commit SHA, timestamp |
| raw input | geometry, material, rebar, steel, q0, halfwave identity and provenance |
| compiler | interval, variant, order, coefficient checksum/hash, domain certificate |
| root | `D_u,q_u,A_u` |
| load | `Pc,Ps,Pu` |
| equilibrium | `Rq_c,Rq_s,Rq_total,R_norm` |
| limit | `P_D,P_q,Rq_D,Rq_q,L,L_norm`, pre/post root load-slope sign |
| material branch | lambda bounds, steel max strain / elastic-yield state |
| tangent audit | `KZ` four contributions at root; if KZ audit requested, first same-branch KZ-zero coordinate |
| execution | solver/script/version or reproducible calculation artifact hash; no-spatial-quadrature flags |
| experiment isolation | explicit flag that Pf/Pcr were not used in solve/root selection |

A 24-panel production run must additionally commit one machine-readable summary table containing the same minimum columns for all panels.

## 5. Current stop point

本文件只完善备份治理并审计缺口；不重算 Cases1–18，不尝试替代根，不另开求解分支。

```text
NEXT_REQUIRED_REPAIR = regenerate/persist missing current Cases1–18 checkpoints only when explicitly authorized
FAIL_FAST = YES
NO_ALTERNATIVE_BRANCH = YES
```
