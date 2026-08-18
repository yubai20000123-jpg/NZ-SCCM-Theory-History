# NZ-SCCM 项目级零离散与 GitHub 连续同步治理锁定

**时间：2026-08-19 01:42 +08:00**  
**状态：LOCKED PROJECT-WIDE GOVERNANCE**  
**适用范围：本项目后续所有聊天、算例、理论推导、审计、验证、交接与 GitHub 维护。**

---

## G1. 零离散默认规则

除非用户在某一次具体任务中**明确、单独授权**使用离散化，否则：

\[
\boxed{\text{ANY DISCRETIZATION = PROHIBITED BY DEFAULT}}
\]

禁止范围不仅包括正式理论，也包括辅助验证、oracle、定位、回归、预估、侧面检查和“先算一个参考答案”。

### G1.1 明确禁止

包括但不限于：

- Gauss / Gauss–Legendre / Gauss–Lobatto 空间或厚度数值积分；
- Simpson、梯形、adaptive quadrature；
- spatial grid / material-point grid / integration points；
- Chebyshev collocation；
- spatial cells / numerical subdomains；
- material-point Newton / pointwise state grid；
- finite-element / finite-difference / mesh-based surrogate；
- 通过离散采样连续场来定位材料状态；
- 通过高密度数值积分得到“oracle truth”；
- 用有限 prefix `N32/N48/N96/...` 的稳定性作为无穷级数正式收敛证明；
- 用有限 prefix 或离散网格对解析路线作侧面验证；
- 用离散 continuation 扫描替代正式有限维极限方程。

### G1.2 默认允许

只要不把连续空间/材料域离散化，以下属于允许的解析/有限维数学操作：

- exact symbolic algebra；
- 有限矩阵运算与 Cayley–Hamilton；
- Beta/Gamma、超几何、Appell、Lauricella、Carlson、elliptic/hyperelliptic、Abelian integrals 等标准函数；
- holonomic / D-finite / Picard–Fuchs / Gauss–Manin / creative telescoping；
- 成熟标准特殊函数作为原子数学对象的高精度评价；
- 对已经严格约化为有限维变量的非线性代数方程求根；
- exact/analytic differentiation；
- interval / arbitrary-precision arithmetic 用于有限表达式或有限维根认证。

如果一个成熟标准函数库内部使用何种实现算法，不改变 NZ-SCCM 的理论身份；但助手不得自行建立结构空间、厚度或材料状态的离散网格或有限 prefix 作为理论/验证层。

### G1.3 唯一例外

用户必须明确说出该次任务允许离散化，例如“本轮允许 Gauss 验证”或等价表述。

该授权：

```text
TASK_LOCAL_ONLY = TRUE
PERSIST_TO_OTHER_TASKS = FALSE
```

如果没有这种明确授权，默认继续执行零离散规则。

### G1.4 解析闭合失败时的行为

若当前解析路线无法继续：

```text
STOP_AT_FIRST_ANALYTIC_BLOCK = REQUIRED
ANALYTIC_CLOSURE_BLOCK = REPORT
DISCRETE_FALLBACK = PROHIBITED
```

不得为了“得到一个答案”暗中退回离散化。

---

## G2. GitHub 连续同步默认规则

NZ-SCCM 的 GitHub 仓库是跨聊天恢复与治理的正式外部连续性层。今后不再等待用户重复提醒。

\[
\boxed{\text{MATERIAL PROJECT CHANGE} \Rightarrow \text{GITHUB CHECKPOINT IN SAME WORKFLOW}}
\]

### G2.1 必须主动同步的事件

出现以下任一事件时，应主动更新 GitHub：

- 用户锁定、撤销或修正理论原则；
- 计算路线、formal operator、材料模型身份发生改变；
- 发现已给数值/结论错误并撤回；
- 新建关键账本、执行合同、审计文件或 handoff；
- active next task / gate 改变；
- 一个重要 pilot PASS / FAIL / BLOCK；
- 对话内容已足以形成新的恢复断点；
- 存在聊天长度不足风险；
- 用户要求“继续下一步”且本轮产生实质项目进展。

### G2.2 最小同步集合

若本轮发生实质状态变化，至少维护：

1. 一个 timestamped theory/audit/governance/checkpoint artifact；
2. `current/CURRENT_STATE.md`；
3. `semantic_v2/00_index/README.md` 的 current operational entry；
4. 一个最新的 file-tree / checkpoint index，列出新文件、supersession 与 active next task。

必要时同时更新 supersession map / semantic manifest；历史文件原则上不原地改写理论内容，而通过新 timestamped artifact 与 supersession 关系保留证据链。

### G2.3 聊天长度保护

不需要等待用户说“聊天快满了”。只要出现连续复杂推导或多个重要状态变化，应主动建立 resumable checkpoint。

```text
CHAT_LENGTH_RISK -> PROACTIVE_GITHUB_CHECKPOINT
```

### G2.4 GitHub 暂时不可用

如果 GitHub 工具暂时不可用：

1. 先在当前运行环境生成本地 checkpoint；
2. 明确标记 `GITHUB_SYNC_PENDING`；
3. 在下一次可访问 GitHub 的工作流中优先补同步；
4. 不得声称已经同步。

---

## G3. 本治理与旧规则的关系

本文件把此前“正式空间积分为零”的边界扩展为更严格的项目默认：**连辅助 oracle/侧面验证也不得离散化**，除非用户当次明确授权。

同时把“GitHub 仅在用户提醒时更新”纠正为“实质项目变化后主动同步”。

若旧文件包含：

- `direct-continuum grid oracle`；
- `Gauss audit only`；
- `finite-prefix convergence regression`；

这些内容可作为历史证据保留，但从 2026-08-19 01:42 起不得自动继承为当前允许操作。

---

## G4. 恢复口令

任何新聊天恢复 NZ-SCCM 时，若读到本文件，应立即采用：

```text
ZERO_DISCRETIZATION_DEFAULT = LOCKED
DISCRETE_AUDIT_ORACLE = PROHIBITED
TASK_LOCAL_DISCRETIZATION_EXCEPTION_ONLY = TRUE
AUTO_GITHUB_CHECKPOINT_AFTER_MATERIAL_CHANGE = REQUIRED
PROACTIVE_CHAT_LENGTH_CHECKPOINT = REQUIRED
```
