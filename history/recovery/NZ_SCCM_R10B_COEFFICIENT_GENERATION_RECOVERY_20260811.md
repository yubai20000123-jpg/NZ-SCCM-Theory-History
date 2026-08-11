# NZ-SCCM R10B 系数生成恢复记录 — 非治理性历史说明

**日期：2026-08-11**  
**当前身份：SUPERSEDED_RECOVERY_NOTE / NON-GOVERNING**

> 本文件记录 2026-08-11 对 R10B coefficient-generation 的一次恢复尝试。该尝试中出现了超出原始证据的推断。当前治理解释已转移到：
>
> `governance/R10_R10B_IDENTITY_AND_INTERPRETATION_CLARIFICATION_20260811.md`
>
> 任何与该治理文件、`current/CURRENT_STATE.md`、R10/R10B canonical theory/governance 不一致的内容，均以治理文件和 current 为准。

---

## 1. 本恢复尝试中明确撤回的说法

以下内容不得再作为 R10B 正式理论事实：

1. `N=48` 可以被重新解释成某个总 coefficient count；
2. 由假定的 `U/C/T` 三组数组推导出 `147` 个“一级材料系数”；
3. 在没有原 `07_R10B_zero_spatial_compiler_core.py` 的情况下，把 DCT-I、DCT-II、continuous projection、least-squares 或某一种权重方案认定为历史 R10B 唯一 coefficient generator；
4. 用 forensic least-squares 数值接近性反向定义历史 R10B 的正式 compiler convention；
5. 把 R10 描述为只在一个极窄 `lambda` 小窗上的局部 patch；
6. 把 R10B 的有限阶表示误差与 R10 的材料目标改变混为一类。

---

## 2. 当前仍可保留的恢复事实

### 2.1 R10 与 R10B 是两次不同性质的变换

```text
SOURCE FOSTER -> R10
= material-target modification

R10 -> R10B
= finite analytic compilation / reintegration
```

R10 是唯一允许改变材料目标的一步；R10B 不允许重新调整材料参数或多轴 interaction。

### 2.2 R10 的实际执行范围

R10 使用内部 scalar coordinate

\[
t=\Pi_\eta(\lambda)
\]

并对 retained tensile interval

\[
0\le t\le10x_{cr}
\]

采用两段 C2 quintic reconstruction。它保留 source work、origin tangent、rounded peak、residual level 和 endpoint regularity，但不是仅对一个无穷小尖点做局部修补。

### 2.3 R10B 的阶次身份

```text
material degree = 48
spatial Chebyshev degree = 28
```

当前只允许解释为：

\[
N_M=48=\text{material-coordinate finite analytic representation order},
\]

\[
N_S=28=\text{structural spatial coefficient-representation order}.
\]

不得由这两个阶次自行推导物理参数数量、材料点数量、空间积分点数量或内部 coefficient-array 总数。

### 2.4 R10B 历史 coefficient generator 仍未恢复

当前仓库没有保存 byte-exact 原：

- `07_R10B_zero_spatial_compiler_core.py`；
- N48 actual coefficient arrays；
- coefficient-generation nodes/weights/projection convention 的完整原始执行内容。

因此历史 coefficient generator 的精确 convention 仍是：

```text
UNRESOLVED_FROM_CURRENT_ORIGINAL_EVIDENCE
```

---

## 3. 后续恢复必须采用的顺序

若继续 R10/R10B 可重复性恢复，必须按以下顺序：

```text
STEP 1  审计 frozen R10 material target
        - Foster source scalar vs R10 scalar
        - 0..10*xcr 材料功重新分布
        - stress/tangent differences
        - multidimensional surface differences
        - 禁止用 Case21/Swartz Pu 反调

STEP 2  审计 R10B 对 frozen R10 的 representation fidelity
        - material-coordinate approximation error
        - spatial coefficient truncation
        - exact moment contraction identity

STEP 3  恢复原 coefficient generator
        - 只有原 core / 原 coefficient artifacts 可以定义历史 convention
        - 若原件无法恢复，则另行冻结一个 NEW reproducibility contract

STEP 4  生成正式 coefficient table / supplementary package
        - 必须明确是 historical recovery 还是 newly frozen convention
```

---

## 4. 当前状态不受本恢复纠错影响

以下已执行结果不因本恢复 note 的降级而改变：

```text
R10_1D_ENERGY_SMOOTHING      = PASS
R10B_1D_MATERIAL_RECOMPILE   = PASS
R10B_ZERO_SPATIAL_CASE21     = PASS_ENGINEERING
CASE21_N48_LIMIT_ROOT        = PASS
SWARTZ24                     = NOT_STARTED
```

Case21 当前正式 R10B 工程结果仍为：

```text
D_u  = 0.8449505
q_u  = 0.001779254542005754
Pc   = 337.39660909142 kN
Ps   = 30.922943404456966 kN
Pu   = 368.31955249587696 kN
```

---

## 5. 阅读规则

恢复顺序必须是：

1. `current/CURRENT_STATE.md`
2. `governance/R10_R10B_IDENTITY_AND_INTERPRETATION_CLARIFICATION_20260811.md`
3. R10 / R10B canonical governance + theory
4. original execution artifacts / original conversation
5. 本文件

本文件不得再被用于反向覆盖 current 或 canonical R10/R10B 数学身份。
