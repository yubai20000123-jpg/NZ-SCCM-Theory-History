# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10  
**Purpose:** 唯一的当前工作入口。历史文件、旧 PASS、旧路线名称不得覆盖本文件的当前身份。

## 1. 当前优先级

当前目标不是继续追求 theorem-level tight remainder certificate，而是：

1. 在 `ONE_CONTINUOUS_COMPLETE_HALFWAVE`、正式零空间采样/零空间数值积分/单一连续域条件下，把 Case21 的当前解析 evaluator 做到工程可用；
2. 若当前单域路线仍存在会改变 Pu 身份的实质性阻断，停止补丁式推进，转入“新材料 / 新目标函数 / 新 solution operator”设计；
3. 通过后再进入 Swartz24，禁止逐板调参。

治理依据：`governance/PRIORITY_RESET_20260810.md`。

## 2. 正式空间身份

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

空间 cells、Gauss/Simpson、自适应积分、Chebyshev collocation、材料点网格只能做独立数值审计，不能作为正式理论 operator。

## 3. 当前 NC + reinforcement benchmark

当前显式 benchmark：

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

这是当前 benchmark/reference operator，不是永久最终普通混凝土理论。正式 tension branch 为 algebraic Foster，不是历史 tanh/sigmoid 变体。

## 4. Case21 当前生产入口

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

## 5. 当前 final-attempt 门槛

生产通过至少要求：

- sampling=0 / quadrature=0 / subdomains=1；
- 解析阶次由内部收敛决定；
- 数值 audit 只在正式结果之后使用；
- 解析/求解误差明显小于材料/结构模型误差；
- concrete + reinforcement 共用同一 evaluator 的 P/R/root；
- 不存在 large Rq/root drift、audit-selected degree、必须空间分区、provenance failure 或 structure-Pu calibration 等实质性阻断。

通过：`CURRENT_OPERATOR_SINGLE_DOMAIN_ROUTE = PASS`  
失败：`CURRENT_OPERATOR_SINGLE_DOMAIN_ROUTE = TERMINATED_FOR_PRODUCTION`

## 6. UHPC 当前身份

UHPC 不允许通过只替换普通混凝土 `fc` 得到。

当前有效材料证据集中在 `evidence/materials/UHPC/`，包括 Hiew direct tension、Liu planar biaxial/path effect、Lee 与 Leutbecher TC、Shen TT、周俊/王淑楠三轴证据，以及历史状态/闭合台账。

当前仍未由文献直接闭合：完整二维应力向量更新、任意加载历史、TCX/history loop、一致 tangent 等。历史 UHPC-C0 仅为 calculable baseline，不是 production multiaxial operator。

用户强制冻结的 UHPC 参数目前只有 `fc = 141.1 MPa`；Ec、epsc0、ft、nu 等可根据正式材料模型和来源重新确定。

## 7. steel shell / Y / PBL 当前身份

最终生产 shell operator 尚未冻结：

```text
M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE
```

有效来源见 `evidence/steel_shell/`。PBL 长期建模边界仍是强局部边界/子板分隔，不自动作为独立轴向承载项，也不自动加入显式弹簧能量；历史来源中的弹簧/有效宽度等表达必须按其 source/historical 身份处理。

## 8. 历史真实性

TURN 0001–0148 是共享对话连续基线；TURN 0148 为中断，不能虚构不存在的 D20 用户可见 final。历史恢复时读 `history/RAW_HISTORY_REGISTRY.md`、`history/recovery/` 和对应 D/G/R/UCFT 路线。

## 9. 后续工作读取原则

默认只读本文件和任务对应的最小文件集。`history/` 只在追溯理由、核查旧路线或来源 provenance 时进入。迁移期全文镜像/旧 checkpoint/R2 snapshot 已从当前 `main` 移除；如极少数情况下确需恢复，使用 `history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md` 定点访问 pre-clean Git commit。
