# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 18:31 +08:00  
**Purpose:** 唯一当前工作入口。历史 PASS、旧路线、迁移期文件不得覆盖本文件。  
**Canonical full-recovery checkpoint:** `governance/FULL_STARTUP_RECOVERY_CHECKPOINT_20260810.md`

## 0. FULL STARTUP RECOVERY 与主线纠偏

近期一度只沿 `M1R -> PF1 -> P2A` 局部恢复，导致把“平滑二维强度域 + invariant current map”误解成新路线。FULL_STARTUP_RECOVERY 已重新接回 G18/G20/G21/G26/G27/G28/G30/G31 及 D/G/R 历史身份。

当前正式身份：

```text
G18/G27 invariant current-map architecture = ACTIVE
G20/G21 smooth conservative material philosophy = RETAINED
G26 moment-first D15 architecture = RETAINED
G28/G30 direct analytic P,Rq,L kernel = RETAINED
M1R/PF1/P2A = LATER COMPILER EXPERIMENTS, NOT ARCHITECTURE REPLACEMENTS
P2R = CANCELLED
ROUTE_SWITCH = NO
```

最近的偏离与恢复过程已单独登记：

- `history/NZ_SCCM/MAINLINE_DEVIATION_AND_RECOVERY_20260810.md`

后续任何 compiler failure 都必须先判定为“表示/编译失败”，不得无证据升级为“current-map architecture 失败”。

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

`governance/PRIORITY_RESET_20260810.md` 已把 theorem-level tight remainder certificate 降为可选方法学附录；这不改变零正式空间积分身份。工程解析收口可采用内部解析收敛 + 事后独立 audit，但 audit 不得选阶、调参或选根。

---

## 2. 当前正式材料表示骨架：G18 -> G27 连续继承

Equivalent-uniaxial tensor：

\[
\mathbf E_u=\frac{(1-\nu)\mathbf E+\nu\,\mathrm{tr}(\mathbf E)\mathbf I}{1-\nu^2},
\]

\[
J_1=\mathrm{tr}\mathbf E_u,
\qquad
J_2=\det\mathbf E_u.
\]

当前统一同轴 current-map architecture：

\[
\boxed{
\boldsymbol\sigma=
U(\mathbf E_u)
+J_2\left[A(J_1,J_2)\mathbf I+B(J_1,J_2)\mathbf E_u\right]
}
\]

主值形式：

\[
s_1=U(x)+xy[A(J_1,J_2)+B(J_1,J_2)x],
\]

\[
s_2=U(y)+xy[A(J_1,J_2)+B(J_1,J_2)y].
\]

当 `J2=0` 时 interaction 自动消失，单轴轴线严格退化为 `U`。一致切线必须由同一 stress map 解析微分获得，禁止独立拟合 tangent。

历史语法身份：

```text
G12 U+xyD = diagnostic only
G16 total-Poisson TC semantics = fail
G16R signed/excess = partial pass, D source non-unique
G17 U+xyD mandatory grammar = retired
G18 invariant architecture = pass
G19 q4/q6 coefficients = fail, architecture retained
G27 invariant architecture = explicitly restored
```

---

## 3. G20/G21：平滑、保守二维材料目标是既有主线

G20 已建立：

```text
CC = smooth conservative biaxial-compression envelope
TT = p=8 smooth superellipse
TC = C1 Bernstein connection with axis tangent matching
source jumps/cracking-axis corners = C1/C2 regularized where project permits
```

强度包络只规定允许强度域/峰值几何，不等于完整 current stress surface，也不能用包络斜率产生材料 tangent。

G21 已锁定 ordinary-concrete project approximations：

```text
current/rotating principal surface instead of fixed-crack history
no independent Nguyen beta shear-retention state
C1/C2 regularization instead of source finite jumps
alpha2=0.3 conservative tension-stiffening
smooth conservative post-peak compression
no independent TCX history state
```

材料验收同时看：

```text
stress
tangent
shape
full-domain boundedness
```

因此允许存在材料面拟合误差、允许 TC/TT 合理向内保守收缩，是**当前既有路线内部的 target regularization**，不是 route switch。

---

## 4. G22/G26/G28/G30 的正确身份

G22 曾得到统一 global current target：

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

它证明“统一 continuous current target + same-map tangent + finite polynomial D15”存在；但 524 个编译系数、最高总代数次数约 340，不符合今天 Gate C，而且 G27 已恢复 invariant production grammar。因此 G22 是存在性/历史证据，不是 final production grammar。

G23-G25 point/material surrogate 只能作性能对照，正式拒绝。

G26 保留：

\[
\boxed{
\text{continuous material}
\to\text{moment-first dual contraction}
\to\text{D15 exact moments}
}
\]

with parity-orthogonal variables

\[
s=\sin^2X,\quad t=\sin^2Y,\quad\eta=\zeta^2,\quad\chi=\sin X\sin Y\zeta.
\]

```text
NAIVE_EXPAND_THEN_INTEGRATE = REJECTED
MOMENT_FIRST_D15 = ACTIVE COMPILER ARCHITECTURE
```

G28/G30 已确认：

\[
\mathbf E(X,Y,\zeta;D,A)
\to\boldsymbol\sigma=\mathcal M(\mathbf E)
\to\text{analytic representation}
\to\text{D15 exact moments}
\to P(D,A),R_A(D,A),L(D,A)
\]

使用同一 analytic kernel + all-real-root isolation；Pu 不需要另造 load stepping/arclength/second solver。

历史身份：

```text
LATEST_FULLY_DELIVERED_STAGE        = G30
LATEST_OPERATIONALLY_ACCEPTED_STAGE = G30
LATEST_EXECUTED_ARTIFACT_STAGE      = G31
G31_FINAL_VISIBLE_DELIVERY          = ABSENT
G31_USER_ACCEPTANCE                 = UNRESOLVED
```

G31 `Pu ~= 476.936 kN` 是故意忽略裂化的 Case21 mathematical-chain validation，不是 validated RC Pu；UHPC-C0 仅为 executed calculable baseline。

---

## 5. Case21 exact invariant foundation

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

## 6. 2026-08-09~10 compiler 实验当前定级

Frozen source-shaped NC regression/reference 使用 `U,C,C2,T,T^8`；它是 benchmark/oracle，不是 final source truth。

M1R rational screen 材料误差较小，但 production 会产生：

```text
27 scalar poles
106 pair blocks
algebraic periods / PF systems
```

PF1 R02-R06 exact mathematics 保留 audit only：

```text
R02 rational resolvents
R03 genus-2 de-Rham/Gauss-Manin
R04 Phi endpoint reduction
R05 common rational driver
R06 15x15 witness connection, 211/225 nonzero, ~2.68e5 chars
PF1_R06_PRODUCTION_ACCEPTANCE = FAIL_COMPLEXITY_GATE
PF1_R07 = CANCELLED
```

P2A `degree<=16` one-global-polynomial primitive compiler：

```text
U max normalized error  ~= 2.43%
C                       ~= 2.44%
C2                      ~= 0.51%
T                       ~= 32.58%
V=T^8                   ~= 43.28%
```

因此：

```text
M1R_P2A_GLOBAL_POLYNOMIAL_PRIMITIVE_COMPILER = FAIL
```

只否定该 compiler family，不等于统一 current-map architecture 失败，也不等于 `T^8` 必须永久保留为 production representation。

---

## 7. R01 已执行：current-target 几何正则化诊断

Canonical：

- `current/theory/NZ_SCCM_CURRENT_TARGET_GEOMETRIC_REGULARIZATION_R01_20260810.md`
- `current/theory/NZ_SCCM_CURRENT_TARGET_GEOMETRIC_REGULARIZATION_R01_results.json`
- `current/theory/nz_sccm_current_target_geometric_regularization_r01.py`

### 7.1 核心新发现

旧判断“全局 lambda 宽约 3.17，而主要 tension transition 宽约 0.05”不完整。当前 reference map 中真正高曲率的局部层宽约为

\[
\eta_\Pi=\eta_r x_{cr}=0.0024993589727.
\]

主要存在三条 strain-space transition ridge：

```text
lambda ~= 0          sign split
lambda ~= xcr        Foster r=1
lambda ~= 10*xcr     Foster r=10
```

历史 qualification interval：

\[
[-2.4390243902,0.7317073171],\qquad\Delta\lambda=3.1707317073.
\]

因此尺度比：

\[
\boxed{3.1707317073/0.00249935897\approx1268.62}.
\]

R01 结论：

```text
PRIMARY_COMPLEXITY_SOURCE = THREE_THIN_TENSILE_CURRENT_MAP_TRANSITION_LAYERS
```

这比“普通混凝土一般非线性太强”更精确。G20 已经消除了 strength-envelope 的主要几何尖角；现在的困难主要是完整 `(epsilon1,epsilon2)->(sigma1,sigma2)` current surface 中的窄高曲率 ridge。

### 7.2 R01 实际曲率定位

```text
zero-split peak: lambda ~= 0.000684, d2T/dlambda2 ~= +1.1583e4
r=1 peak:        lambda ~= 0.050080, d2T/dlambda2 ~= -4.3300e3
r=10 peak:       lambda ~= 0.499882, d2T/dlambda2 ~= +3.1128e2
```

这些只是材料坐标诊断，不是 formal structural spatial quadrature。

### 7.3 sector 决策

CC 保留：

\[
\boxed{c_i^*=c_i(1+a_{cc}c_1c_2)},\qquad a_{cc}=0.1072329249362415.
\]

TC/CT 保留既有保守目标：

\[
\boxed{c^*=c(1-\tau)},
\]

拉向分量不放大。

TT：G20 `p=8` 仍是当前 outer reference；R01 只授权更简单的 inner candidates 做 material-only screen：

```text
p=8: equal biaxial = 0.917004 ft
p=4: equal biaxial = 0.840896 ft, reduction vs p8 = 8.2996%
p=2: equal biaxial = 0.707107 ft, reduction vs p8 = 22.8895%
```

当前：

```text
TT_P4 = AUTHORIZED_FOR_MATERIAL_ONLY_SCREEN
TT_P2 = LOWER_BOUND_DIAGNOSTIC_ONLY
NEW_TT_P_FROZEN = NO
```

### 7.4 R01 gate

```text
TARGET_SURFACE_REFORMULATION_R01 = PASS_DIAGNOSTIC
ROUTE_SWITCH = NO
CC = RETAIN
TC = RETAIN_EXISTING_CONSERVATIVE_TARGET
PRIMARY_REFORMULATION_TARGET = TENSILE_CURRENT_MAP_TRANSITION_CORRIDOR
CASE21_PU = NOT_RUN
SWARTZ24 = NOT_RUN
```

只缩 TT/TC strength envelope **不能**消除 lambda-space thin layers；下一步必须直接处理 current-map transition corridor。

---

## 8. 三个正式门禁

```text
Gate A = exact/engineering-analytic direct structural closure
Gate B = concrete nonlinear/material adequacy
Gate C = production analytic complexity
```

Gate C：

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

`governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md` 继续有效：任何执行/PASS必须在聊天中真实展示公式、中间量、误差和复杂度。

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

必须在 root solve 前：

\[
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s}.
\]

禁止 `Pu=Pu,c+As fy` 事后相加。

### UHPC

仅 `fc=141.1 MPa` 为用户强制冻结。Hiew/Liu/Leutbecher/周俊/王淑楠等材料证据已保留；UHPC-C0 不是 production；final strong multiaxial current operator = OPEN。

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

结构 Pu 不得反标材料参数、TC/TT 收缩程度、平滑宽度或 compiler order。

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

## 12. 当前唯一下一理论任务

```text
CURRENT_RECOMMENDED_NEXT_TASK = TENSILE_CURRENT_MAP_TRANSITION_CORRIDOR_R02
```

R02 不是新 compiler search，也不是 route switch。它只允许在同一 G18/G20/G27 current-map target 内，构造**极少数明确 C2 conservative transition-corridor candidates**，并在进入 D15 以前做材料级门禁。

固定要求：

```text
preserve sigma(0,0)=0
preserve initial elastic tangent
preserve uniaxial ft axis anchor
never increase stress above accepted material target
stress and tangent from same map
no runtime TT/TC/CC state partition
no structural Pu calibration
compare material stress + tangent + surface shape + algebraic complexity
```

优先比较：

1. G20/current narrow ridge reference；
2. 一个 moderate widened C2 transition corridor；
3. 必要时一个 stronger conservative bound；
4. TT p=8 vs p=4 同步作为 material-only geometry comparison；p=2 只作 lower-bound diagnostic。

若 moderate regularization 不能显著降低 target curvature/representation complexity 而不破坏 material stress+tangent gate，则停在 R02，不再重新进入大函数族/PF 扩张。

---

## 13. 恢复与继续读取顺序

```text
FULL_STARTUP_RECOVERY = PASS_FOR_PROJECT_CONTINUATION
ROUTE_SWITCH = NO
TARGET_SURFACE_REFORMULATION_R01 = PASS_DIAGNOSTIC
RECOVERY_BASELINE_HEAD = 22b3d39e74972ffcc66abede9691d65ba1732f22
```

后续恢复优先读取：

1. `current/CURRENT_STATE.md`
2. `governance/FULL_STARTUP_RECOVERY_CHECKPOINT_20260810.md`
3. `history/NZ_SCCM/MAINLINE_DEVIATION_AND_RECOVERY_20260810.md`
4. `current/theory/NZ_SCCM_CURRENT_TARGET_GEOMETRIC_REGULARIZATION_R01_20260810.md`
5. `current/theory/NZ_SCCM_CURRENT_TARGET_GEOMETRIC_REGULARIZATION_R01_results.json`
6. `current/theory/nz_sccm_current_target_geometric_regularization_r01.py`
7. `governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md`
8. `governance/PRIORITY_RESET_20260810.md`
9. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`
10. `current/theory/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`
11. G20/G21/G22 historical evidence and File Library G27/G28/G30/G31 when historical identity is questioned.
