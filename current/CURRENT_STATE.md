# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 19:01 +08:00  
**Purpose:** 唯一当前工作入口。历史 PASS、旧路线、迁移期文件不得覆盖本文件。  
**Canonical full-recovery checkpoint:** `governance/FULL_STARTUP_RECOVERY_CHECKPOINT_20260810.md`

## 0. FULL STARTUP RECOVERY 与主线身份

近期曾因局部只恢复 `M1R -> PF1 -> P2A` 而把既有“平滑二维强度域 + invariant current map”误判成新路线。该错误已经通过 FULL_STARTUP_RECOVERY 纠正，并独立登记：

- `history/NZ_SCCM/MAINLINE_DEVIATION_AND_RECOVERY_20260810.md`

当前正式身份：

```text
G18/G27 invariant current-map architecture = ACTIVE
G20/G21 smooth conservative material philosophy = RETAINED
G26 moment-first D15 architecture = RETAINED
G28/G30 direct analytic P,Rq,L kernel = RETAINED
M1R/PF1/P2A = COMPILER/REPRESENTATION EXPERIMENTS, NOT ARCHITECTURE REPLACEMENTS
P2R = CANCELLED
ROUTE_SWITCH = NO
```

任何 compiler failure 只能先定级为表示/编译失败，不得无证据升级为 current-map architecture 失败。

---

## 1. 固定结构目标与正式空间边界

```text
finite analytic kinematics
-> finite strain invariants
-> unified strong nonlinear current material law
-> consistent tangent from same map
-> moment-first exact/engineering-analytic contraction
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

`governance/PRIORITY_RESET_20260810.md` 已把 theorem-level tight remainder certificate 降为可选数学附录；工程解析可采用内部解析收敛 + 事后独立 audit，audit 不得选阶、调参或选根。

---

## 2. 当前正式材料表示骨架：G18 -> G27

Equivalent-uniaxial tensor：

\[
\mathbf E_u=\frac{(1-\nu)\mathbf E+\nu\,\mathrm{tr}(\mathbf E)\mathbf I}{1-\nu^2},
\]

\[
J_1=\mathrm{tr}\mathbf E_u,
\qquad
J_2=\det\mathbf E_u.
\]

统一同轴 current-map architecture：

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

当 `J2=0` 时 interaction 自动消失；一致切线必须由同一 stress map 解析微分获得，禁止独立拟合 tangent。

历史语法身份：

```text
G12 U+xyD = diagnostic only
G16 total-Poisson TC semantics = fail
G16R signed/excess = partial pass
G17 U+xyD mandatory grammar = retired
G18 invariant architecture = pass
G19 q4/q6 fitted coefficients = fail, architecture retained
G27 invariant architecture = explicitly restored
```

---

## 3. G20/G21：平滑保守二维目标是既有主线

G20/G21 已建立/允许：

```text
CC = smooth conservative biaxial-compression envelope
TT = p=8 smooth superellipse reference
TC = C1 Bernstein connection with axis tangent matching
source jumps/cracking-axis corners = C1/C2 regularized where permitted
current/rotating principal surface
conservative tension-stiffening
smooth conservative post-peak compression
no independent TCX history state
```

强度包络只规定允许强度域/峰值几何，不等于完整 current stress surface，也不能用包络斜率产生 tangent。

材料验收必须同时看：

```text
stress
tangent
shape
full-domain boundedness
```

允许 TC/TT 合理向内保守收缩属于同一路线的 target regularization，不是 route switch。

---

## 4. D15 / P-Rq-L 内核

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

G28/G30 已确认同一内核：

\[
\mathbf E(X,Y,\zeta;D,A)
\to\boldsymbol\sigma=\mathcal M(\mathbf E)
\to\text{analytic representation}
\to\text{D15 exact moments}
\to P(D,A),R_A(D,A),L(D,A).
\]

Pu 不需要 load stepping/arclength/second solver。

历史身份：

```text
LATEST_FULLY_DELIVERED_STAGE        = G30
LATEST_OPERATIONALLY_ACCEPTED_STAGE = G30
LATEST_EXECUTED_ARTIFACT_STAGE      = G31
G31_FINAL_VISIBLE_DELIVERY          = ABSENT
G31_USER_ACCEPTANCE                 = UNRESOLVED
```

G31 `Pu ~= 476.936 kN` 是故意忽略裂化的 chain validation，不是 validated RC Pu；UHPC-C0 只属于 executed calculable baseline。

---

## 5. Case21 invariant foundation

Canonical：

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

`I2` 中全部 `M^2` 项严格抵消；`I1,I2` 为有限 polynomial field。

---

## 6. Compiler 实验当前定级

Frozen source-shaped NC regression/reference 使用 `U,C,C2,T,T^8`；它是 benchmark/oracle，不是 final source truth。

```text
M1 simple polynomial = FAIL
M1R rational = good material regression, production HOLD
PF1 R02-R06 exact mathematics = audit only
PF1 R06 15x15 connection = FAIL production complexity
PF1 R07 = CANCELLED
P2A degree<=16 single-global primitive polynomial = FAIL
```

P2A 的主要失败量：

```text
U  ~= 2.43% max normalized error
C  ~= 2.44%
C2 ~= 0.51%
T  ~= 32.58%
V=T^8 ~= 43.28%
```

这些只否定具体 compiler family，不否定 current-map architecture。

---

## 7. R01：current-target 几何诊断

Canonical：

- `current/theory/NZ_SCCM_CURRENT_TARGET_GEOMETRIC_REGULARIZATION_R01_20260810.md`
- `current/theory/NZ_SCCM_CURRENT_TARGET_GEOMETRIC_REGULARIZATION_R01_results.json`

R01 定位出三条高曲率 tensile transition ridge：

```text
lambda ~= 0          sign split
lambda ~= xcr        Foster r=1
lambda ~= 10*xcr     Foster r=10
```

局部 characteristic width：

\[
\eta_\Pi=\eta_r x_{cr}=0.0024993589727.
\]

历史 qualification interval 宽约 `3.17073`，尺度比约 `1268.62:1`。

R01 sector 决策：

```text
CC = RETAIN
TC = RETAIN EXISTING CONSERVATIVE TARGET
TT p=8 = OUTER REFERENCE
TT p=4 = MATERIAL-ONLY SCREEN AUTHORIZED
TT p=2 = LOWER-BOUND DIAGNOSTIC ONLY
PRIMARY_REFORMULATION_TARGET = TENSILE CURRENT-MAP TRANSITION CORRIDOR
```

---

## 8. R02：transition-corridor 实际执行结果

Canonical：

- `current/theory/NZ_SCCM_TENSILE_CURRENT_MAP_TRANSITION_CORRIDOR_R02_20260810.md`
- `current/theory/NZ_SCCM_TENSILE_CURRENT_MAP_TRANSITION_CORRIDOR_R02_results.json`
- `current/theory/nz_sccm_tensile_current_map_transition_corridor_r02.py`

R02 首先实际执行 common-width `k=1,2,4,8`。`k>=4` 虽大幅降低曲率，但 TC/CC stress drift 明显，因此 fail-fast 收缩到 `1<k<=2`。

refined screen：

```text
k=1.25:
  mean three-peak curvature ratio = 0.8023
  TC stress P95 change           = 0.002103 fc
  TC tangent P95 change          = 0.04384 kappa

k=1.50:
  mean curvature ratio           = 0.6704
  TC stress P95 change           = 0.004029 fc
  TC tangent P95 change          = 0.09734 kappa

k=1.75:
  TC tangent P95 change          = 0.16006 kappa

k=2.00:
  mean curvature ratio           = 0.5054
  TC tangent P95 change          = 0.23131 kappa
```

因此：

```text
K_1P25 = RETAIN MODERATE MATERIAL CANDIDATE, NOT FROZEN
K_1P5  = RETAIN STRONGER DIAGNOSTIC
K_GE_1P75 = HOLD DUE TANGENT DISTURBANCE
```

### 8.1 R02 关键负结果：合理展宽本身不足以解决解析复杂度

在完整历史 qualification interval 上，同一 degree-32 `T(lambda)` global polynomial screen：

```text
k=1 baseline max normalized error ~= 31.806%
k=2 widened  max normalized error ~= 31.324%
```

即使曲率峰约减半，global compiler difficulty 几乎没有改变。

正式：

```text
PURE_WIDTH_WIDENING = INSUFFICIENT_AS_SOLE_SOLUTION
```

### 8.2 R02 关键正结果：spectral/reachable-domain reduction 的收益远大于展宽

沿用既有 Case21 zero-spatial diagnostic state `D=0.75,q=0.002` 的分离主谱：

\[
\lambda_+\in[-0.1051,0.13584],
\qquad
\lambda_-\in[-0.86569,-0.62473].
\]

这些区间当前只作 diagnostic，不是 Swartz-family production bounds。

对同一个 baseline `T(lambda)`：

```text
full historical interval, degree 32:
  max normalized error ~= 31.806%

lambda+ diagnostic interval, degree 32:
  max normalized error ~= 2.283%

lambda- diagnostic interval, degree 6:
  max absolute error ~= 5.19e-12
```

因此 R02 将下一主动作从“继续物理展宽”转向：

```text
SPECTRAL_REACHABLE_DOMAIN_REDUCTION
```

这仍属于同一个 invariant current-map / D15 路线。

---

## 9. “降维”的允许身份

`(epsilon1,epsilon2,sigma1,sigma2)` 是一个 2->2 current map 的图，不是四个独立输入。允许的降维/降复杂度方式：

1. **Invariant reduction — 已 active**：以 `(J1,J2)` 和固定 tensor basis 表示同轴 current map。
2. **Spectral-branch reduction**：若在目标结构参数盒内可证明 `lambda+`、`lambda-` 存在正 spectral gap，则可在两个互不重叠的谱区间上分别构造同一材料函数的 scalar analytic representation；这不是空间/material-state partition。
3. **Reachable-domain reduction**：只对由结构运动学和参数边界解析可达的 material-state union 做 production qualification，不再默认覆盖过大的 oracle square；不得用试验 Pu 缩域。
4. **Low-rank invariant representation**：在 reachable `(J1,J2)` domain 上检查 `A(J1,J2),B(J1,J2)` 是否可用少量 separated polynomial terms 表示，并保持 D15-compatible。

禁止把“降维”理解为删除一个主应力、忽略双轴耦合，或重新启用 TT/TC/CC runtime state partition。

---

## 10. 三个正式门禁

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

`governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md` 继续有效。

---

## 11. Other components

### Reinforcement

必须在 root solve 前：

\[
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s}.
\]

禁止 concrete Pu 后事后加 `As fy`。

### UHPC

仅 `fc=141.1 MPa` 为用户强制冻结；final strong multiaxial current operator = OPEN；UHPC-C0 不是 production。

### Steel shell / Y / PBL

```text
M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE
```

Yun Lu/Zhang Ning/Sun Lipeng evidence retained；PBL 继续作为强局部边界/子板分隔，不自动作为独立轴向承载项或显式 spring energy。

### Case21 / Swartz24

```text
Case21 = analytic/structural benchmark; no new final RC Pu frozen
old 338/342 kN = audit/reference only
G31 476.936 kN = uncracked chain validation only
Swartz24 production = PAUSED
```

结构 Pu 不得反标材料参数、平滑宽度、reachable domain 或 compiler order。

---

## 12. 当前唯一下一理论任务

```text
CURRENT_RECOMMENDED_NEXT_TASK = SPECTRAL_REACHABLE_DOMAIN_REDUCTION_R03
```

R03 不是 route switch，也不是重新做 polynomial/rational/PF family search。只允许：

1. 从 Case21/Swartz 运动学与明确的 `(D,q,geometry,material parameter)` production box 推导 `lambda+`、`lambda-` 的解析/严格保守范围；
2. 证明或否证整个 production box 上的正 spectral gap；
3. 将可达状态映射到 `(J1,J2)` reachable domain；
4. 在分离谱区间和 reachable invariant domain 上重新测量需要的 polynomial/separated-rank 复杂度；
5. 决定是否仍需要 `k=1.25` mild physical regularization；
6. 禁止用 Case21/Swartz Pu 选择范围、阶数或材料参数；
7. 正式结构空间 sampling/quadrature/subdomain 继续为 `0/0/1`。

R03 fail-fast：如果没有可证明的 branch gap，或 Swartz family reachable domain 仍覆盖历史宽域的大部分，则必须直接报告，而不是靠人工缩域。

---

## 13. 恢复与继续读取顺序

```text
FULL_STARTUP_RECOVERY = PASS_FOR_PROJECT_CONTINUATION
ROUTE_SWITCH = NO
TARGET_SURFACE_REFORMULATION_R01 = PASS_DIAGNOSTIC
TENSILE_CURRENT_MAP_TRANSITION_CORRIDOR_R02 = PASS_DIAGNOSTIC_WITH_REFRAME
PURE_WIDTH_WIDENING = INSUFFICIENT_AS_SOLE_SOLUTION
RECOVERY_BASELINE_HEAD = 22b3d39e74972ffcc66abede9691d65ba1732f22
```

后续优先读取：

1. `current/CURRENT_STATE.md`
2. `governance/FULL_STARTUP_RECOVERY_CHECKPOINT_20260810.md`
3. `history/NZ_SCCM/MAINLINE_DEVIATION_AND_RECOVERY_20260810.md`
4. `current/theory/NZ_SCCM_TENSILE_CURRENT_MAP_TRANSITION_CORRIDOR_R02_20260810.md`
5. `current/theory/NZ_SCCM_TENSILE_CURRENT_MAP_TRANSITION_CORRIDOR_R02_results.json`
6. `current/theory/nz_sccm_tensile_current_map_transition_corridor_r02.py`
7. `current/theory/NZ_SCCM_CURRENT_TARGET_GEOMETRIC_REGULARIZATION_R01_20260810.md`
8. `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`
9. `governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md`
10. `governance/PRIORITY_RESET_20260810.md`
11. G20/G21/G22 historical evidence and File Library G27/G28/G30/G31 when historical identity is questioned.
