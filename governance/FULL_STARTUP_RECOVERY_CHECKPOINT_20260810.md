# NZ-SCCM FULL STARTUP RECOVERY CHECKPOINT — 2026-08-10

**Status:** RECOVERY COMPLETE / THEORY UNCHANGED / ROUTE IDENTITY CORRECTED

## 0. 恢复基线

- repository: `yubai20000123-jpg/NZ-SCCM-Theory-History`
- default branch: `main`
- recovery-start HEAD: `22b3d39e74972ffcc66abede9691d65ba1732f22`
- recovery mode: `FULL_STARTUP_RECOVERY`
- 本轮不建立新材料函数、不拟合新系数、不求新 Case21/Swartz Pu；只恢复并裁决当前路线身份。

## 1. 15项恢复门禁

### 1.1 当前最终目标

规则轴压板采用一个连续完整代表半波和 Nguyen 二阶运动学，将连续应变场直接送入可信二维 current material map，并以零正式空间求积的解析矩得到

```text
P(D,q)
Rq(D,q)=0
L(D,q)=P_,D Rq_,q-P_,q Rq_,D=0
```

随后冻结同一材料/结构版本验证 Case21 与 Swartz24，不以结构 Pu 反标材料。

### 1.2 当前正式主线

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
-> Nguyen second-order finite kinematics
-> Eu / invariant current-material representation
-> same stress law gives analytic tangent
-> exact D15 / moment-first contraction
-> P, Rq, L
-> all-real-root + physical-branch adjudication
```

### 1.3 当前推进阶段

当前不是 P2R 新 basis 搜索阶段。最新治理已暂停“换函数族—拟合—再救积分”的试错链。恢复后应先在**同一 G18/G27 current-map 架构**内重新审视 production target surface/domain 的必要复杂度，尤其 TC/TT 的保守平滑与实际所需材料域。

### 1.4 ordinary concrete operator 当前身份

`current/theory/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md` 中 Foster/Saenz/source-shaped current operator 是 **benchmark/reference current operator**，不是永久最终普通混凝土理论。

其后 M1/M1R/PF1/P2A 都是“如何把当前强非线性目标压入直接解析结构算子”的实现/编译探索，不是对 G18/G27 current-map 物理架构的替代。

### 1.5 reinforcement 如何进入结构方程

钢筋必须在求根前同时进入

```text
P=Pc+Ps
Rq=Rq,c+Rq,s
```

禁止先求 concrete Pu 后再加 `As fy`。

### 1.6 UHPC 当前闭合程度

UHPC 材料证据对单轴拉伸、平面强度、TC 压缩软化/刚度和三轴强度约束较强，但一般二维/history-capable constitutive operator 并未由来源唯一闭合。历史 UHPC-C0 仅是 `EXECUTED_CALCULABLE_BASELINE`，不是 production operator。用户强制冻结参数当前仅 `fc=141.1 MPa`。

### 1.7 steel-shell / Y / PBL 当前闭合程度

`M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE`。云露、张宁、孙立鹏来源已保存用于后续 Y/PBL/steel-shell 理论；PBL 当前长期角色仍是强局部边界/子板分隔，不自动作为独立轴向承载项或显式 spring energy。

### 1.8 Case21 当前正式计算身份

Case21 结构—不变量—D15 数学基础有效；当前没有发布一个由最终 production 2D material operator 驱动的新正式 RC Pu。历史高精度约 338/342 kN 只能 audit/reference。G31 的 476.935634 kN 是故意忽略裂化的直接解析链验证，不是 validated RC Pu。

### 1.9 Swartz24 当前状态

`PAUSED`。G29 历史 Pcr 批量结果是方法/材料轴线验证；正式 Pu 批算必须等待 production current material target 和直接解析算子关闭，且不得逐板调参。

### 1.10 当前锁定理论边界

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_auxiliary_numerical_quadrature = 0
N_auxiliary_ODE_steps = 0
NO hidden initial-value integration
NO large connection system as production operator
```

同时保留：Nguyen 二阶运动学、D15/moment-first、current map、一致切线、全实根/物理支路、结构 Pu 不参与材料识别。

### 1.11 已淘汰路线

至少包括：正式空间 Gauss/Simpson/adaptive/material-point grid；panel-level surrogate；旧 `U+xyD(x,y)` mandatory grammar；G18 q4/q6 具体锚点系数；G22 高阶全局面作为最终 post-G27 production grammar；M1 simple additive polynomial；M1R rational + PF1 大辅助系统作为 production；P2A degree<=16 单全局 primitive polynomial；PF1-R07。

### 1.12 只能 audit/reference 的历史结果

D/G/R 历史 PASS 必须按阶段身份使用。G22 的 stress+tangent certificate 是真实有效历史实现，但不能覆盖 G27 后恢复的 invariant architecture；PF1 R02-R06 exact mathematics 保留 audit-only；G31 有工件但无用户可见 final/验收。

### 1.13 当前关键 unresolved blocker

不是 Nguyen 二阶运动学，也不是 D15 本身。当前关键问题是：在

```text
strong nonlinear multiaxial concrete
+ one unified continuous current map
+ no material/spatial runtime partition
+ direct zero-quadrature low-complexity formula
```

同时要求下，production target surface 是否被定义得过宽/过尖，尤其 tensile/cracking transition、TC/TT interior interaction 和 `T^8` 类 sharp compiler structure 是否超出了当前单调轴压板真正需要保留的物理复杂度。

### 1.14 下一步最合理工作

不是换路线，也不是新 compiler。下一步应在现有 G18/G27 架构内做 **TARGET-SURFACE REDEFINITION / REGULARIZATION**：

1. 保留 `Eu, J1, J2` 与统一同轴 current map；
2. 保留 G20 已建立的 C1 conservative strength-domain 思想；
3. 明确轴压板 production 所需的材料状态域；
4. 允许材料级拟合误差，在 TC/TT 方向构造受来源约束的平滑保守内缩，而不削弱压缩主控区域；
5. 在拟合前先限定最终表达必须满足 Gate A/B/C；
6. 不使用 Case21/Swartz Pu 选择收缩量或材料系数。

这里的“内缩”是材料目标面的 production approximation，不是空间/material cells，也不是重开 `TT/TC/CC` runtime state partition。

### 1.15 对应核查路径

- current: `current/CURRENT_STATE.md`, `current/theory/`, `current/case21/`
- governance: `RECOVERY_PROTOCOL.md`, `SOURCE_OF_TRUTH_POLICY.md`, `SYNC_PROTOCOL.md`, `EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md`, `NZ_SCCM_ROOT_CAUSE_DIAGNOSTIC_PAUSE_20260810.md`
- history: `history/NZ_SCCM/`, `history/ledgers/HISTORICAL_COMPONENT_LEDGER.md`, `history/RAW_HISTORY_REGISTRY.md`
- primary evidence: `evidence/materials/NC/`, `evidence/materials/UHPC/`, `evidence/steel_shell/`
- raw/File Library recovery: G27, G28, G31 and conversation-evolution records referenced by `history/RAW_HISTORY_REGISTRY.md`.

## 2. 恢复出的关键路线谱系

### 2.1 G18 → G20 → G21 → G22

- G18 已建立低参数强度域 + invariant structured current map + consistent tangent；结构语法是

```text
sigma = U(Eu) + J2[A(J1,J2) I + B(J1,J2) Eu]
```

- G19 失败的是 q4/q6 特定锚点系数的全域外推，不是该语法。
- G20 已经建立 C1 平滑双轴强度域，并发现普通混凝土高阶压力很大部分来自人为开裂轴尖角；C1/C2 正则化是既有路线成果。
- G21 冻结 material admission gate：stress+tangent+shape+strength-domain，同时明确 current/rotating principal surface、保守 tension-stiffening 等项目近似。
- G22 曾得到 524 系数、总代数次数上界 340 的全局 finite polynomial certificate；它证明“统一 global current map + D15”可行，但后续 G27 不再把它当最终 production grammar，且今天 Gate C 也不接受这种规模。

### 2.2 G26 → G27 → G28 → G30

- G26 将 D15 做成 continuous moment-first/parity-orthogonal contraction，解决 naive expand-then-integrate 的数值膨胀；不改变材料物理。
- G27 正式恢复 G18 invariant grammar，撤销 `U+xyD` 历史回退；只留下 `A(J1,J2),B(J1,J2)` production closure 为材料开放项。
- G28 证明 `M(epsilon) -> analytic series -> D15 -> P,R_A` 直接复合链成立，剩余问题明确是二维 material interaction closure，不是积分原理。
- G30 形成用户可见且随后获得操作性接受的方法锁：Pcr/Pu 共享同一直接解析内核，不另造 Pu solver。

### 2.3 G31 的正确身份

- 已执行工件存在；Case21 no-cracking Saenz baseline `Pu=476.935634 kN`, 比实验高约 29.49%；
- 这只证明 `DIRECT_ANALYTIC_PU_CHAIN=PASS`；
- G31 没有用户可见 assistant final，用户验收未解决；
- UHPC-C0 同样只是 calculable baseline。

### 2.4 2026-08-09/10 后续 M1R/PF1/P2A

这些工作是在同一个 current-map/D15 路线里尝试解决“如何把强 nonlinear material target 直接收缩到 zero-quadrature whole-halfwave operator”，不是新物理路线。

- rational compiler 在材料误差上很好，但 whole-halfwave analytic complexity 爆炸到 27 poles / 106 pairs / 15x15 PF connection；production FAIL；
- global primitive polynomial 到 degree 16 时 `T/V` 分别仍约 32.6%/43.3% max normalized error；说明 narrow tensile activation 是关键尺度；
- 因此最新治理已暂停继续 basis hunting。

## 3. 本轮最重要纠偏

之前把“平滑二维强度域 + invariant current map”重新描述成一条新路线是错误的。它从 G18/G20/G27 起就是本项目现有主线的核心组成。

用户当前提出的“换角度思考”应解释为：

> 在**同一路线**中重新定义 production material target surface，使其对轴压板所需状态足够真实、连续、光滑、适度保守，并允许材料级拟合误差；而不是另起一套 current-map 理论。

## 4. 恢复结论

```text
FULL_STARTUP_RECOVERY = COMPLETE_FOR_CURRENT_THEORY_CONTINUATION
ROUTE_SWITCH = NO
NEW_MATERIAL_COMPILER = NOT_AUTHORIZED
NEXT_THEORY_ACTION = SAME_ROUTE_TARGET_SURFACE_REDEFINITION
```

本 checkpoint 只恢复和裁决身份，不批准具体 TC/TT 收缩系数，不修改任何材料参数。