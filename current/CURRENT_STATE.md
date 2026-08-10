# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10  
**Purpose:** 唯一当前工作入口。历史 PASS、旧路线、迁移期文件不得覆盖本文件。  
**Full recovery checkpoint:** `governance/FULL_STARTUP_RECOVERY_AND_ARCHITECTURE_CONTINUITY_20260810.md`

## 0. 2026-08-10 FULL STARTUP RECOVERY 纠偏

近期局部恢复只沿 `M1R -> PF1 -> P2A` 推进，导致把“平滑二维强度域 + invariant current map”误解成一个可能的新路线。FULL_STARTUP_RECOVERY 已重新读取 current/governance/evidence/history，并回 File Library 原始 Conversation JSON/G12-G31 工件核验。

当前正式纠偏：

```text
G18/G27 invariant current-map architecture = STILL ACTIVE
G20/G21 smooth conservative material philosophy = RETAINED
G26 moment-first D15 architecture = RETAINED
G28/G30 direct analytic P,Rq,L kernel = RETAINED
M1R/PF1/P2A = LATER COMPILER EXPERIMENTS, NOT ARCHITECTURE REPLACEMENTS
```

因此当前**不是换路径**，也不再执行 P2R basis search。下一理论任务只允许在既有路径内部重新定义更平顺、允许合理保守误差的 current target domain。

---

## 1. 不可改变的结构目标与正式空间边界

```text
finite analytic kinematics
-> finite strain invariants
-> unified strong nonlinear current material law
-> consistent tangent from same map
-> moment-first exact analytic contraction
-> P, Rq, L
-> all-real-root physical branch decision
```

结构目标：

```text
P(D,q)
Rq(D,q)=0
L(D,q)=P_,D Rq_,q-P_,q Rq_,D=0
```

formal identity：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1 representative complete halfwave
KINEMATICS = NGUYEN_SECOND_ORDER / CURRENT CASE21 FINITE ANALYTIC KINEMATICS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT / ENGINEERING-ANALYTIC AS GOVERNED
ELEMENT_INTEGRATION = PROHIBITED
MATERIAL_POINT_GRID = PROHIBITED
SPATIAL_CELLS = PROHIBITED
GAUSS_SIMPSON_ADAPTIVE = PROHIBITED_IN_FORMAL_OPERATOR
COLLOCATION_AS_FORMAL_OPERATOR = PROHIBITED
N_auxiliary_numerical_quadrature = 0
N_auxiliary_ODE_steps = 0
NO hidden initial-value integration
NO large connection system as production operator
```

`PRIORITY_RESET_20260810.md` 已把 theorem-level tight remainder certificate 降为可选方法学附录；这不改变零正式空间积分身份。工程解析收口可按内部解析收敛 + 事后独立 audit，但 audit 不得选阶、调参或选根。

---

## 2. 当前正式材料表示骨架：G18 -> G27 连续继承

固定 equivalent-uniaxial tensor：

\[
\mathbf E_u=
\frac{(1-\nu)\mathbf E+\nu\,\mathrm{tr}(\mathbf E)\mathbf I}{1-\nu^2},
\]

\[
J_1=\mathrm{tr}\mathbf E_u,
\qquad
J_2=\det\mathbf E_u.
\]

当前允许的统一同轴 current-map architecture：

\[
\boxed{
\boldsymbol\sigma=
U(\mathbf E_u)
+J_2\left[
A(J_1,J_2)\mathbf I+B(J_1,J_2)\mathbf E_u
\right]
}
\]

在主值 `x,y` 下：

\[
s_1=U(x)+xy[A(J_1,J_2)+B(J_1,J_2)x],
\]

\[
s_2=U(y)+xy[A(J_1,J_2)+B(J_1,J_2)y].
\]

这不是近期新路线。历史已确认：

```text
G12 U+xyD = diagnostic only
G16 total-Poisson TC semantics = fail
G16R signed/excess = partial pass, D source non-unique
G17 U+xyD mandatory grammar = retired
G18 invariant architecture = pass
G19 q4/q6 coefficients = fail, architecture retained
G27 invariant architecture = explicitly restored
```

当 `J2=0` 时 interaction 自动消失，因此单轴轴线严格退化为 `U`，不再需要两个方向独立的 `D(x,y)/D(y,x)`。

一致切线必须由同一 stress map 解析微分获得，禁止独立拟合 tangent。

---

## 3. G20/G21：平滑、保守二维材料目标已经是既有主线

G20 已建立：

```text
CC = smooth conservative biaxial-compression envelope
TT = p=8 smooth superellipse
TC = C1 Bernstein connection with axis tangent matching
source jumps/cracking-axis corners = C1/C2 regularized where project permits
```

强度包络只规定峰值/启动/转换几何，不等于完整 current stress surface，也不能用包络斜率生成材料 tangent。

G21 已锁定 ordinary-concrete project approximations：

```text
current/rotating principal surface instead of fixed-crack history
no independent Nguyen beta shear-retention state
C1/C2 regularization instead of source finite jumps
alpha2=0.3 conservative tension-stiffening
smooth conservative post-peak compression
no independent TCX history state
```

材料验收必须同时看：

```text
stress
tangent
shape
full-domain boundedness
```

因此用户当前允许“存在材料面拟合误差，并适当向内收缩 TC/TT 区以得到平顺、偏保守的板 current response”应理解为**现有 G18/G20/G27 路径的 target-domain 进一步约束**，不是 route switch。

---

## 4. G22-G26 的正确身份

G22 曾得到：

```text
sigma_i/fc = K180(e_i)*U70[(e_i+nu e_j)/(1-nu^2)]*M90(e_j)+H180(e_i)
```

历史 certificate：

```text
stress RMS  = 0.000655 fc
stress P95  = 0.001635 fc
tangent RMS = 0.021726
tangent P95 = 0.053346
D15 compatibility = PASS
```

这证明“一个统一连续 current target + same-map tangent + finite polynomial D15”可以实现。但 524 个编译系数、最高总代数次数约 340，且 G27 后来重新裁决 production grammar，因此：

```text
G22 certificate = RETAINED EVIDENCE
G22 KUMH as final production grammar = DIAGNOSTIC ONLY
```

G23-G25 的 point/material surrogate 只能作性能对照，正式拒绝。G26 保留：

\[
\boxed{
\text{continuous material}
\to\text{moment-first dual contraction}
\to\text{D15 exact moments}
}
\]

并使用 parity-orthogonal variables

\[
s=\sin^2X,\quad t=\sin^2Y,\quad\eta=\zeta^2,\quad\chi=\sin X\sin Y\zeta.
\]

所以：

```text
NAIVE_EXPAND_THEN_INTEGRATE = REJECTED
MOMENT_FIRST_D15 = ACTIVE COMPILER ARCHITECTURE
```

---

## 5. G28/G30：Pu 的直接解析求解内核已经不是 blocker

G28 证明了：

\[
\mathbf E(X,Y,\zeta;D,A)
\to\boldsymbol\sigma=\mathcal M(\mathbf E)
\to\text{analytic series}
\to\text{D15 exact moments}
\to P(D,A),R_A(D,A)
\]

的零正式空间积分机制；其 remaining issue 明确是 G18 `A(J1,J2),B(J1,J2)` 的 production closure，不是新的 integration theory。

G30 进一步锁定 Pu：

\[
R_A=0,
\qquad
L=P_{,D}R_{A,A}-P_{,A}R_{A,D}=0,
\]

使用同一 `P,R_A,L` analytic kernel + all-real-root isolation，不需要另造 load stepping / arclength / second Pu solver。

历史身份：

```text
LATEST_FULLY_DELIVERED_STAGE        = G30
LATEST_OPERATIONALLY_ACCEPTED_STAGE = G30
LATEST_EXECUTED_ARTIFACT_STAGE      = G31
G31_FINAL_VISIBLE_DELIVERY          = ABSENT
G31_USER_ACCEPTANCE                 = UNRESOLVED
```

G31 `Pu ~= 476.936 kN` 是故意忽略裂化的 Case21 mathematical-chain validation；不是 validated RC Pu。UHPC-C0 仅是 executed calculable baseline。

---

## 6. Case21 当前 exact invariant foundation

保留：

- `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`

定义：

```text
q=A/b
M=Cm(q)=pi^2/eps0*(q0*q+q^2/2)
B=Cb(q)=pi^2/(2 eps0)*(t/b)*q
H=u^2+v^2-2u^2v^2
K=nu*u^2-v^2+(1-nu)u^2v^2
W=uvz
```

\[
\boxed{I_1=(\nu-1)D+MH+2BW}
\]

\[
\boxed{
I_2=-\nu D^2+DMK+BD(\nu-1)W
+BMW(2-u^2-v^2)+B^2z^2(u^2+v^2-1)
}
\]

`I2` 中所有 `M^2` 项严格抵消。`I1,I2` 属有限 polynomial field；这一结构没有被任何后续 compiler failure 否定。

---

## 7. 2026-08-09~10 的 material/compiler 实验如何定级

### 7.1 frozen source-shaped regression operator

当前显式 NC regression/reference 使用 `U,C,C2,T,T^8` source-shaped map。它是 benchmark/oracle，不是 final source truth。

M1R rational screen 的材料误差较小，但作为 production compiler 会产生 27 scalar poles、106 pair blocks，随后进入 algebraic periods / PF systems。

### 7.2 PF1 R02-R06

数学身份保留 audit only：

```text
R02 rational resolvents
R03 genus-2 de-Rham/Gauss-Manin
R04 Phi endpoint reduction
R05 common rational driver
R06 15x15 witness connection, 211/225 nonzero, ~2.68e5 chars
```

正式：

```text
PF1_R06_PRODUCTION_ACCEPTANCE = FAIL_COMPLEXITY_GATE
PF1_R07 = CANCELLED
```

### 7.3 P2A

`degree<=16` one-global-polynomial primitive compiler 对 U/C/C2 尚可，但：

```text
T max normalized error ~= 32.58%
V=T^8 max normalized error ~= 43.28%
```

因此：

```text
M1R_P2A_GLOBAL_POLYNOMIAL_PRIMITIVE_COMPILER = FAIL
```

这只否定该 compiler family，**不能**推导出统一 current-map architecture 失败，也不能推导出必须永久保留 `T^8` 这一特定 regression representation。

---

## 8. 三个正式门禁

```text
Gate A = exact/engineering-analytic direct structural closure
Gate B = concrete nonlinear/material adequacy
Gate C = production analytic complexity
```

Gate C 继续要求：

```text
original x/y/z numerical quadrature = 0
auxiliary numerical quadrature = 0
auxiliary ODE stepping = 0
no hidden numerical initialization
no branch-by-branch spatial/material state propagation
P,Rq and derivatives reduce to direct finite formulas
large auxiliary connection system is not production
actual formulas must be exposed, not hidden behind scripts
```

`EXPLICIT_EXECUTION_EVIDENCE_RULE` 继续有效：以后任何执行/PASS必须在聊天里真实展示公式、系数/中间表达、误差与复杂度。

---

## 9. ordinary concrete / reinforcement / UHPC / shell 当前身份

### Ordinary concrete

```text
Nguyen/Foster exact/history material = PRIMARY SOURCE / BENCHMARK
G18/G27 invariant current architecture = ACTIVE
G20/G21 smooth conservative target philosophy = ACTIVE CONSTRAINT
final compact A_NC(J1,J2),B_NC(J1,J2) closure = OPEN
```

### Reinforcement

必须在 root solve 之前：

\[
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s}.
\]

禁止 `Pu=Pu,c+As fy` 事后相加。

### UHPC

仅 `fc=141.1 MPa` 为用户强制冻结值。Hiew/Liu/Leutbecher/周俊/王淑楠等材料证据已保留；UHPC-C0 不是 production。final strong multiaxial current operator = OPEN。

### Steel shell / Y / PBL

```text
M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE
```

Yun Lu/Zhang Ning/Sun Lipeng evidence 已保留；production Y/shell 未开始。PBL 继续作为强局部边界/子板分隔，不自动作为独立轴向承载项或显式 spring energy。

---

## 10. Case21 / Swartz24 当前生产状态

```text
Case21 = analytic/structural benchmark; no new final RC Pu frozen
old 338/342 kN = audit/reference only
G31 476.936 kN = uncracked chain validation only
Swartz24 production = PAUSED
```

G29 等历史 Pcr population 不能覆盖当前 m=1 representative-halfwave hard lock，也不能作为 final Pu material calibration。

---

## 11. 当前明确淘汰/限制

```text
U+xyD(x,y) mandatory production grammar
G18 q4/q6 specific fitted coefficients
panel-level Chebyshev/proxy production
material-point/grid/Gauss production
D15 UHPC Layer-0 material identity
naive expand-then-integrate
G23/G25 point-cloud material surrogate
Pu second load-step/arclength solver
PF1 large connection production
P2A degree<=16 single-global primitive compiler
blind compiler-family hopping
```

---

## 12. 当前暂停与唯一下一理论任务

`governance/NZ_SCCM_ROOT_CAUSE_DIAGNOSTIC_PAUSE_20260810.md` 中“禁止继续盲目换 compiler”继续有效；但其 D1-D3 从零 provenance 审计要求已被 FULL_STARTUP_RECOVERY 部分 supersede，因为 G20/G21/G27 已经完成大量来源/机制/架构裁决。

当前：

```text
P2R = CANCELLED / NOT AUTHORIZED
NEW COMPILER FAMILY SEARCH = PAUSED
CURRENT_RECOMMENDED_NEXT_TASK = EXISTING_PATH_CONSERVATIVE_CURRENT_TARGET_REFORMULATION
```

该任务**不换路径**。输入固定为：

```text
G18/G27 invariant architecture
G20 C1 smooth conservative strength-domain geometry
G21 mechanism/project-approximation locks
current Gate A/B/C
Case21 exact I1/I2 kinematics
user-allowed material fitting error and conservative TC/TT contraction
```

下一步只回答：

1. CC 中哪些峰值/双压增强特征必须保持；
2. TC 中压向 softening 与拉向残余响应哪些是板 Pu 真正必须保留；
3. TT 区可以向内收缩到什么材料级保守边界；
4. 如何使三个象限通过同一 `A(J1,J2),B(J1,J2)` 连续光滑连接；
5. 在**先冻结 target geometry/constraints**后，再决定最低复杂度 closure/编译形式。

禁止在这一任务开始前再次拟合 polynomial/rational/spline/special-function family。

---

## 13. 恢复状态

```text
FULL_STARTUP_RECOVERY = PASS_FOR_PROJECT_CONTINUATION
RECOVERY_BASELINE_HEAD = 22b3d39e74972ffcc66abede9691d65ba1732f22
BYTE_FOR_BYTE_BULK_HISTORY_REIMPORT = NOT_REQUIRED
```

后续恢复优先读取：

1. `current/CURRENT_STATE.md`
2. `governance/FULL_STARTUP_RECOVERY_AND_ARCHITECTURE_CONTINUITY_20260810.md`
3. `governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md`
4. `governance/PRIORITY_RESET_20260810.md`
5. `history/ledgers/HISTORICAL_COMPONENT_LEDGER.md`
6. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`
7. `current/theory/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`
8. G20/G21/G22 historical evidence
9. File Library G27/G28/G30/G31 + raw Conversation JSON when historical identity is questioned
