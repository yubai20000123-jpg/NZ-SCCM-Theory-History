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

## 3. 结构目标函数的当前身份

不因旧 integrand 难积分而改变结构力学问题本身。Case21 继续保留：

- 轴向承载力 `P(D,q)`；
- 幅值方向平衡 `Rq(D,q)=0`；
- 极限点条件

`L(D,q)=P_,D Rq_,q - P_,q Rq_,D = 0`。

重建的是中间链：

```text
finite analytic kinematics
-> finite invariants
-> compact invariant/tensor-basis material law
-> finite analytic material moments
-> P, Rq, derivatives/tangent, L
```

当前 V1 首选二维各向同性表示：

`sigma_hat = A(I1,I2) I + B(I1,I2) X`

其中 `A,B` 采用材料级来源约束的有限解析基，使其与有限三角—厚度运动学复合后仍可化为有限精确矩。NC 与 UHPC 可共享此表示/积分骨架，但不能共享未经材料证据证明的具体 scalar law 和参数。

## 4. 当前 NC + reinforcement benchmark

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

## 5. Case21 benchmark 当前生产入口

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

## 6. 旧 Case21 final-attempt 的新身份

旧单域 Nguyen/Foster 路线仍可按 engineering analytic convergence 做一次短收口，但不再继续扩展 strict certificate 数学工具链。其任务是形成稳定 benchmark 身份，而不是阻断新的 target-function/material-moment 理论。

## 7. UHPC 当前身份

UHPC 不允许通过只替换普通混凝土 `fc` 得到。

当前有效材料证据集中在 `evidence/materials/UHPC/`，包括 Hiew direct tension、Liu planar biaxial/path effect、Lee 与 Leutbecher TC、Shen TT、周俊/王淑楠三轴证据，以及历史状态/闭合台账。

当前仍未由文献直接闭合：完整二维应力向量更新、任意加载历史、TCX/history loop、一致 tangent 等。历史 UHPC-C0 仅为 calculable baseline，不是 production multiaxial operator。

用户强制冻结的 UHPC 参数目前只有 `fc = 141.1 MPa`；Ec、epsc0、ft、nu 等可根据正式材料模型和来源重新确定。

新主线要求：UHPC 与 NC 可共享 invariant/tensor-basis + analytic moment architecture，但 UHPC 的 `A/B` scalar laws、内部变量与参数必须由 UHPC 材料级证据独立确定。

## 8. steel shell / Y / PBL 当前身份

最终 production shell operator 尚未冻结：

```text
M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE
```

有效来源见 `evidence/steel_shell/`。PBL 长期建模边界仍是强局部边界/子板分隔，不自动作为独立轴向承载项，也不自动加入显式弹簧能量；历史来源中的弹簧/有效宽度等表达必须按其 source/historical 身份处理。

## 9. 历史真实性

TURN 0001–0148 是共享对话连续基线；TURN 0148 为中断，不能虚构不存在的 D20 用户可见 final。历史恢复时读 `history/RAW_HISTORY_REGISTRY.md`、`history/recovery/` 和对应 D/G/R/UCFT 路线。

## 10. 后续工作读取原则

默认先读本文件和 `current/theory/NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`。`history/` 只在追溯理由、核查旧路线或来源 provenance 时进入。迁移期全文镜像/旧 checkpoint/R2 snapshot 已从当前 `main` 移除；如极少数情况下确需恢复，使用 `history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md` 定点访问 pre-clean Git commit。
