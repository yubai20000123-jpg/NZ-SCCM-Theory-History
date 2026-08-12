# NZ-SCCM 时间戳命名与当前基线治理决定

**时间：2026-08-12 17:34 +08:00**  
**身份：CURRENT GOVERNANCE DECISION**

## 1. 命名规则

自本决定起，正式新文件不再使用 `V1`、`V2`、`R1`、`R2`、`NC-R1.1`、`NC-R2` 等容易与理论阶段、程序版本、审计轮次混淆的序号作为主文件名标识。

统一格式：

```text
<清晰内容描述>_YYYYMMDD_HHMM.<ext>
```

时间戳采用项目用户本地时区 `+08:00`。

若同一内容后续发生实质修订，建立新的时间戳文件并在 `current/CURRENT_STATE.md` 指向最新文件；旧文件保留为历史证据，不删除，不继续获得 current governing 身份。

## 2. 新理论名称

当前理论正式名称统一为：

**NZ-SCCM 普通混凝土钢筋板零空间解析极限承载力—切线稳定统一理论**

对应当前文件：

`current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_ANALYTIC_LIMIT_TANGENT_UNIFIED_THEORY_20260812_1734.md`

该名称取代将当前理论主线称为 `NC-R1`、`NC-R2` 等编号式称呼的做法。旧编号只允许出现在历史追溯时。

## 3. 新 Case21 合同名称

当前 Case21 执行合同正式名称统一为：

**NZ-SCCM Case21 零空间解析极限—切线稳定统一计算合同**

对应当前文件：

`current/workflows/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_EXECUTION_CONTRACT_20260812_1734.md`

该合同把 general-D15 平衡支与 Zhou/Navier current-tangent gate 置于同一条强制执行链，不再允许旧 restricted-D15 Case21 workflow 作为正式生产合同。

## 4. 理论身份不变的内容

本次重命名和整理不是新理论机制，不重新打开：

```text
R10 material target
N48 order
Cayley-Hamilton lift
Nguyen second-order kinematics
ONE_CONTINUOUS_COMPLETE_HALFWAVE
D15 general exact trigonometric moments
zero formal spatial discretization
rebar continuous analytic mapping
Zhou/Navier full-field tangent projection
```

## 5. 当前 Case21 状态

本次整理不把旧 Case21 候选荷载恢复为 production 结果。

当前状态仍为：

```text
GENERAL_D15_Syy_RECHECK = PASS
GENERAL_D15_Qq_RECHECK = FAIL AGAINST PREVIOUS EXECUTION
PREVIOUS_CASE21_BRANCH = AUDIT RECORD ONLY
ZERO_STATE_TANGENT_REGRESSION = PASS
PRODUCTION_TANGENT_GATE = PENDING CORRECTED GENERAL-D15 BRANCH
CASE21_COMPLETE_CLOSURE = BLOCKED
```

下一步必须从原始 Case21 输入和当前时间戳理论/合同重新建立 general-D15 `Rq(D,q)` 与正确主平衡支，再完成 tangent gate。
