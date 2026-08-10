# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10  
**Purpose:** 唯一的当前工作入口。历史文件、旧 PASS、旧路线名称不得覆盖本文件的当前身份。

## 1. 当前优先级

当前主线已经进一步明确为两级：

1. Case21 旧 benchmark 只做短收口，不再继续投入大量研究资源追求 theorem-level tight remainder certificate；
2. 新的正式理论主线转入“保留结构目标 P/Rq/L，重建材料 operator → 有限解析材料矩 → 结构目标函数”的体系。

新的不可退让积分边界是：正式结果必须来自**一个连续完整代表半波上的解析积分 / 精确矩闭合**，不是 element integration，也不是把 Gauss/cells/collocation/material points 换名字重新引入。

新主线设计文件：

`current/theory/NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`

治理依据仍包括：`governance/PRIORITY_RESET_20260810.md`。

## 2. 正式空间身份

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT_MOMENTS
ELEMENT_INTEGRATION = PROHIBITED
```

空间 cells、Gauss/Simpson、自适应积分、Chebyshev collocation、材料点网格只能做独立数值审计，不能作为正式理论 operator。

## 3. 结构目标函数与解析矩当前身份

不因旧 integrand 难积分而改变结构力学问题本身。Case21 继续保留：

- 轴向承载力 `P(D,q)`；
- 幅值方向平衡 `Rq(D,q)=0`；
- 极限点条件

`L(D,q)=P_,D Rq_,q - P_,q Rq_,D = 0`。

重建的是中间链：

```text
finite analytic kinematics
-> finite invariants
-> compact nonlinear material law
-> finite analytic material moments
-> P, Rq, derivatives/tangent, L
```

当前 V1 首选二维各向同性同轴表示骨架：

`sigma_hat = A(I1,I2) I + B(I1,I2) X`

但这里的 `A/B` 只是 tensor representation，不代表“低阶自由二维多项式”已经足够描述混凝土。

### 3.1 Case21 不变量精确展开已完成

当前推导文件：

`current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`

透明符号核验代码：

`current/theory/nz_sccm_case21_invariant_exact_moments_v1.py`

对冻结 Nguyen 二阶运动学，令 `u=sin X, v=sin Y, z=zeta, M=Cm(q), B=Cb(q)`，则两个归一化应变不变量可严格写成有限 `u,v,z` 多项式。尤其：

- `I2=det(X)` 中全部 `M^2` 项严格抵消；
- 利用 `cos^2=1-sin^2` 后，`I1,I2` 均不再显式含 `cos X,cos Y`；
- `P/Rq` 所需积分可以进一步缩成 `sin^a X sin^b Y zeta^h` 的有限解析矩。

当前四族核心 exact moments 为：

```text
J_P^A(m,n) = Mcal[I1^m I2^n]
J_P^B(m,n) = Mcal[I1^m I2^n Xyy]
J_q^A(m,n) = Mcal[I1^m I2^n I1,q]
J_q^B(m,n) = Mcal[I1^m I2^n (I1 I1,q - I2,q)]
```

其中 `Mcal` 是完整半波上的解析积分泛函，不是数值 quadrature。

## 4. 混凝土强非线性是当前硬门禁，不允许后置

用户已明确修正：由于目标是极限承载力，混凝土强非线性不能在“数学流程做通”以后再补。

因此新增：

`current/theory/NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`

以及 diagnostic-only 可复现实验：

`current/theory/nz_sccm_frozen_nc_invariant_surface_screen_r01.py`

正式身份：

```text
LOW_ORDER_GENERIC_MATERIAL = ALGEBRA_UNIT_TEST_ONLY
LOW_ORDER_GENERIC_MATERIAL != ARCHITECTURE_FEASIBILITY_PROOF
```

新材料 operator 至少必须在材料级证据上覆盖：初始刚度、压缩非线上升、峰值、峰后下降、拉伸开裂后响应、CC 增强、TC coupling，以及与同一 law 一致的 tangent。

已经用 frozen NC current operator 做了一个纯材料空间 stress-test：在归一化主应变 `[-2,0.6]^2` 上，naive total-degree invariant A/B surface 到 degree 10–12 仍有明显误差且条件数快速恶化。因此**低/中阶自由 A/B surface 已被否定为新架构可行性的充分证明**。这不是对所有 finite analytic concrete laws 的否定；下一步应比较 structured matrix polynomial 与 shape-constrained global invariant polynomial/Bernstein 等强非线性解析骨架。

任何最终候选仍必须同时通过：

```text
Gate A = exact analytic integration
Gate B = concrete nonlinear adequacy
```

失败时只能重构材料解析表示或有限全局 internal-variable architecture，不能退回 element/material-point integration。

## 5. 当前 NC + reinforcement benchmark

旧 benchmark 仍保留用于回归/比较：

- `current/theory/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`
- `current/theory/nz_sccm_current_operator_explicit_v1.py`

材料链：

```text
engineering strain
→ equivalent-uniaxial tensor
→ principal coordinates
→ Saenz compression + algebraic Foster tension
→ biaxial interaction
→ spectral return
→ sigma = M_NC(epsilon)
```

这是 benchmark/reference operator，不再作为永久最终普通混凝土理论。正式 benchmark tension branch 为 algebraic Foster，不是历史 tanh/sigmoid 变体。

## 6. Case21 benchmark 当前生产入口

读取：

- `current/case21/NZ_SCCM_CASE21_GLOBAL_AUDIT_HANDOFF_20260809.md`
- `current/case21/NEXTSTEP_EXECUTION_REPORT.md`
- `current/case21/results_nextstep.json`

结构未知量为 `D` 与 `q=A/b`。Nguyen 二阶连续半波运动学；钢筋必须在求根前同时进入 `P` 与 `Rq`：

```text
P = Pc + Ps
Rq = Rq,c + Rq,s
Rq(D,q)=0
L(D,q)=P_,D Rq_,q - P_,q Rq_,D = 0
```

禁止使用 `Pu = Pu,concrete + As fy` 作为正式 RC Pu。

历史高精度数值参考约为 concrete 338.3184 kN、RC 342.3339 kN；实验 failure load 约 368.3128 kN。它们只能做 audit/reference，不得用于选阶、选根、拟合材料或校准模型。

## 7. 旧 Case21 final-attempt 的新身份

旧单域 Nguyen/Foster 路线仍可按 engineering analytic convergence 做一次短收口，但不再继续扩展 strict certificate 数学工具链。其任务是形成稳定 benchmark 身份，而不是阻断新的 target-function/material-moment 理论。

## 8. UHPC 当前身份

UHPC 不允许通过只替换普通混凝土 `fc` 得到。

当前有效材料证据集中在 `evidence/materials/UHPC/`，包括 Hiew direct tension、Liu planar biaxial/path effect、Lee 与 Leutbecher TC、Shen TT、周俊/王淑楠三轴证据，以及历史状态/闭合台账。

当前仍未由文献直接闭合：完整二维应力向量更新、任意加载历史、TCX/history loop、一致 tangent 等。历史 UHPC-C0 仅为 calculable baseline，不是 production multiaxial operator。

用户强制冻结的 UHPC 参数目前只有 `fc = 141.1 MPa`；Ec、epsc0、ft、nu 等可根据正式材料模型和来源重新确定。

新主线要求：UHPC 与 NC 可共享 invariant/tensor-basis + analytic moment architecture，但 UHPC 的 scalar laws、内部变量与参数必须由 UHPC 材料级证据独立确定，而且同样必须同时通过 exact-moment Gate A 和 nonlinear material Gate B。

## 9. steel shell / Y / PBL 当前身份

最终 production shell operator 尚未冻结：

```text
M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE
```

有效来源见 `evidence/steel_shell/`。PBL 长期建模边界仍是强局部边界/子板分隔，不自动作为独立轴向承载项，也不自动加入显式弹簧能量；历史来源中的弹簧/有效宽度等表达必须按其 source/historical 身份处理。

## 10. 历史真实性

TURN 0001–0148 是共享对话连续基线；TURN 0148 为中断，不能虚构不存在的 D20 用户可见 final。历史恢复时读 `history/RAW_HISTORY_REGISTRY.md`、`history/recovery/` 和对应 D/G/R/UCFT 路线。

## 11. 后续工作读取原则

默认先读：

1. 本文件；
2. `current/theory/NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`；
3. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`；
4. `current/theory/NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`。

`history/` 只在追溯理由、核查旧路线或来源 provenance 时进入。迁移期全文镜像/旧 checkpoint/R2 snapshot 已从当前 `main` 移除；如极少数情况下确需恢复，使用 `history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md` 定点访问 pre-clean Git commit。
