# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 20:18 +08:00  
**Purpose:** 唯一当前工作入口。详细推导、失败路线和执行历史留在 canonical theory/history/evidence 文件中。

## 0. 主线身份

```text
G18/G27 invariant current-map architecture = ACTIVE
G20/G21 smooth conservative material philosophy = RETAINED
G26 moment-first D15 architecture = RETAINED
G28/G30 direct analytic P,Rq,L kernel = RETAINED
M1R/PF1/P2A = compiler/representation experiments, not architecture replacements
P2R = CANCELLED
ROUTE_SWITCH = NO
```

此前“局部恢复 -> 误把既有 current-map 当新路线 -> 完整恢复”的过程已写入 history。R01-R06 均属于恢复后的同一 current-map 主线。

---

## 1. 固定结构目标与零空间离散边界

\[
P(D,q),\qquad R_q(D,q)=0,
\]

\[
L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0.
\]

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_auxiliary_numerical_quadrature = 0
N_auxiliary_ODE_steps = 0
MATERIAL_POINT_GRID = PROHIBITED
SPATIAL_CELLS = PROHIBITED
NO hidden initial-value integration
NO large connection system as production operator
```

工程解析允许内部解析收敛 + 独立 audit；audit 不得选阶、调参或选根。

---

## 2. 当前 unified material grammar

\[
\mathbf E_u=\frac{(1-\nu)\mathbf E+\nu\,\mathrm{tr}(\mathbf E)\mathbf I}{1-\nu^2},
\qquad J_1=\mathrm{tr}\mathbf E_u,
\qquad J_2=\det\mathbf E_u.
\]

G18/G27：

\[
\boxed{\boldsymbol\sigma=U(\mathbf E_u)+J_2[A(J_1,J_2)\mathbf I+B(J_1,J_2)\mathbf E_u]}
\]

一致切线必须由同一 stress map 解析求导。G20/G21 允许 C1/C2 regularization、smooth conservative postpeak/TC/TT/CC target；禁止恢复 runtime TT/TC/CC state machine。

旧 source-shaped `C,T,T^8` 继续保留 benchmark/reference 身份，但不是必须永久保留的 production grammar。

---

## 3. MATERIAL-NATIVE DOMAIN GOVERNANCE

Canonical：

- `governance/MATERIAL_NATIVE_SPECTRAL_DOMAIN_RULE_20260810.md`
- `governance/MATERIAL_NATIVE_SCALAR_DOMAIN_CONTRACT_R05_20260810.md`

```text
PRIMARY_DOMAIN   = MATERIAL_ADMISSIBLE_SPECTRAL_DOMAIN Lambda_M
SECONDARY_DOMAIN = STRUCTURAL_REACHABLE_SUBDOMAIN Lambda_R
MANDATORY        = Lambda_R subset of Lambda_M
```

材料 compiler 先在材料本构自己的适用/活动谱域通过 Gate B/C。Case21/Swartz24 只作后验结构验证与可选效率诊断，禁止反向定义或缩小 production material domain。

NC 与 UHPC 可有不同 `Lambda_M`，但共享 Eu/J1/J2、matrix-function、invariant/separable compilation、D15 和 P/Rq/L 架构。UHPC 禁止继承 NC 数字谱域。

R05 NC active transition interval：

\[
\boxed{\Lambda_{M,NC}^{active}=[-\gamma_2,\alpha_1\rho/\kappa]}
\]

当前普通混凝土 source instance：

```text
gamma2 = 10
alpha1 = 10
alpha2 = 0.30
rho = 0.10
kappa = 2.0005129533678754
lambda_cr = 0.04998717945397425
Lambda_M,NC^active = [-10, 0.49987179453974245]
```

---

## 4. R01-R05 retained conclusions

```text
R01: three narrow tensile current-map ridges located
R02: mild widening helps but is insufficient alone; k=1.25 optional, not frozen
R03: source-shaped principal surface exact separated rank <=4; Swartz spectral range only structural diagnostic
R04: full Pi+H1+H10 tower not generic direct Appell/Carlson; material-native spectral governance frozen
R05: material-native NC domain frozen; pure Saenz continuation conflicts with 10% source postcrush residual
```

R05 compactification screen showed material-coordinate compression is useful, but final NC scalar remained open because the deep-postpeak target was not yet explicitly closed.

---

## 5. R06 — NC POSTPEAK C2 SCALAR CLOSURE

Canonical：

- `governance/NC_POSTPEAK_C2_SCALAR_TARGET_RULE_20260810.md`
- `current/theory/NZ_SCCM_NC_POSTPEAK_SCALAR_CLOSURE_AND_D15_PRECHECK_R06_20260810.md`
- `current/theory/NZ_SCCM_NC_POSTPEAK_SCALAR_CLOSURE_AND_D15_PRECHECK_R06_results.json`
- `history/NZ_SCCM/R06_POSTPEAK_C2_AND_COMPILER_HEADTOHEAD_20260810.md`

Nguyen source postcrush branch: linear from peak to `0.1 sigma_p` at `gamma2 eps_p`, then zero-tangent residual plateau. To remove the source tangent jumps without restoring a state machine, R06 freezes a C2 endpoint regularization of that material target.

Define

```text
s=(-lambda-1)/9
sigma/fc=-1+0.9 q(s)
```

with source `q=s`. R06 bridge:

```text
g(tau)=3 tau^5-8 tau^4+6 tau^3
delta_s=0.05
Delta_lambda=0.45 per endpoint
```

Material-only width gate: local extra compression relative to source <=1% fc.

Executed:

```text
max extra compression = 0.888889% fc
max conservative reduction = 0.888889% fc
U(-1)=-1, U'(-1)=0
U(-10)=-0.1, U'(-10)=0
```

Formal status：

```text
NC_POSTPEAK_C2_SCALAR_TARGET = PASS
```

The target is used by a unified compiler; it does not create runtime crushing subdomains.

---

## 6. R06 compiler head-to-head

### 6.1 Direct polynomial in lambda

Degree 64 executed material screen：

```text
stress max = 1.981970% fc
stress P95 = 0.185018% fc
tangent P95 = 3.365831% initial tangent
local tangent max = 185.101% in narrow transition neighborhoods
```

Formal integration identity is solved: finite scalar polynomial -> Cayley-Hamilton invariant polynomial -> Beta/D15 exact moments.

But generic degree-64 invariant footprint is large：

```text
A(J1,J2) unique pairs = 1025
B(J1,J2) unique pairs = 1056
union unique pairs     = 1088
A+B pair count         = 2081
```

```text
GLOBAL_LAMBDA_N64 = PASS_MATERIAL_SCREEN / HOLD_GATE_C
```

### 6.2 Softsign

`chi_s=lambda/sqrt(1+lambda^2)`，degree 48：

```text
stress max = 0.988210% fc
tangent P95 = 1.991297%
```

Algebraic kernel smaller than old source tower but exact direct D15 closure remains unproved：

```text
SOFTSIGN_N48 = PASS_MATERIAL_SCREEN / HOLD_KERNEL
```

### 6.3 Möbius compactification

\[
\chi_M(\lambda)=\frac{\lambda}{1-\lambda}.
\]

For the 2x2 tensor：

\[
\boxed{\chi_M(E)=E(I-E)^{-1}=\frac{E-J_2I}{1-J_1+J_2}}
\]

so the only scalar denominator is

\[
\boxed{\Delta_M=1-J_1+J_2=(1-\lambda_+)(1-\lambda_-)}.
\]

NC material-domain pole safety：

```text
lambda_p=1 > lambda_M,max=0.49987179454
Delta_M >= 0.250128221897 on the full NC material square
```

Material screens：

```text
n=24: stress max 2.081055% fc; tangent P95 4.417013%
n=48: stress max 0.984912% fc; tangent P95 2.369704%
```

After Case21 substitution：

\[
\Delta_M=1-I_1+I_2=A_0(s,t)+A_1(s,t)\zeta+A_2(s,t)\zeta^2.
\]

Fixed-`s,t` thickness integration of integer powers `Delta_M^{-m}` is elementary-recursive; however the remaining 2D master is not yet proven to reduce to a small Beta/Appell/Carlson kernel.

```text
MOBIUS_COMPACTIFICATION = PROMOTED_FOR_KERNEL_SCREEN
MOBIUS_D15_KERNEL = HOLD_NOT_YET_CLOSED
```

---

## 7. R06 formal decision

```text
R06 = PASS_POSTPEAK_C2__HOLD_FINAL_COMPILER
NC_POSTPEAK_C2_SCALAR_TARGET = PASS
GLOBAL_LAMBDA_N64 = PASS_MATERIAL_SCREEN / HOLD_GATE_C
SOFTSIGN_N48 = PASS_MATERIAL_SCREEN / HOLD_KERNEL
MOBIUS_N24_N48 = PROMISING / HOLD_KERNEL
FINAL_NC_COMPILER = OPEN
CASE21_PU = NOT_RUN
SWARTZ24_PU = NOT_RUN
ROUTE_SWITCH = NO
```

Important interpretation：

```text
Direct polynomial = integration solved / representation footprint high
Compactified maps = representation smaller / structural kernel unresolved
```

No compiler may be selected from material error alone.

---

## 8. D15 / structural mainline retained

G26：

\[
continuous\ material\to moment\!-\!first\ contraction\to D15\ exact\ moments.
\]

G28/G30：same analytic kernel -> `P,Rq,L`; no second Pu solver/load stepping identity.

Case21 invariant foundation remains finite polynomial in `I1,I2`; all `M^2` terms in `I2` cancel exactly.

---

## 9. Gate A/B/C

```text
Gate A = exact/engineering-analytic direct structural closure
Gate B = concrete nonlinear/material adequacy
Gate C = production analytic complexity
```

Gate C：zero formal x/y/z quadrature；zero auxiliary quadrature/ODE；no runtime TT/TC/CC state propagation；`P,Rq` and derivatives -> direct finite formulas；large auxiliary systems != production。

---

## 10. Material/structure status

Ordinary concrete：material-native active domain = PASS；NC postpeak C2 target = PASS；full compact scalar compiler = OPEN；multiaxial `A,B` final closure follows only after scalar compiler decision。

Reinforcement must enter root solve before ultimate state：

\[
P=P_c+P_s,\qquad R_q=R_{q,c}+R_{q,s}.
\]

UHPC：only `fc=141.1 MPa` user-forced；UHPC material-native domain and scalar/multiaxial law must come from UHPC sources, but reuse the same compiler/kernel architecture after NC proves it.

Steel shell/Y：`M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE`；PBL remains strong local boundary/subpanel segmentation.

---

## 11. Case21 / Swartz24 status

```text
Case21 = analytic benchmark; no new final RC Pu frozen
old 338/342 kN = audit/reference only
G31 476.936 kN = uncracked chain validation only
Swartz24 production Pu = PAUSED
```

No Pu may tune material domain, postpeak target, compactification, compiler order or root selection.

---

## 12. 当前唯一下一理论任务

```text
CURRENT_RECOMMENDED_NEXT_TASK
= R07_HEAD_TO_HEAD_KERNEL_COMPLEXITY_DECISION_GLOBAL_POLY64_VS_MOBIUS24
```

R07 **禁止再引入新的材料函数族**。只比较已执行的两个候选：

1. `GLOBAL_LAMBDA_N64`：给出不经 naive full expansion 的 exact recurrence、实际 D15 moment/operation count，并判断 1088 invariant-pair footprint 是否可接受；
2. `MOBIUS_N24`：对 `Delta_M^{-m}` 做 exact thickness elimination + parity/symmetry reduction，并硬判剩余 2D master 是否属于 small named kernel。

Fail-fast：

```text
Möbius -> PF/large ODE/master system       => FAIL
Direct polynomial -> auditable finite recurrence with acceptable Gate-C cost => PREFER DIRECT
Both fail Gate C                          => HOLD and return to material target
```

不得 blind degree escalation，不得 Case21/Swartz Pu 选 compiler。

---

## 13. 恢复读取顺序

1. `current/CURRENT_STATE.md`
2. `governance/NC_POSTPEAK_C2_SCALAR_TARGET_RULE_20260810.md`
3. `current/theory/NZ_SCCM_NC_POSTPEAK_SCALAR_CLOSURE_AND_D15_PRECHECK_R06_20260810.md`
4. `current/theory/NZ_SCCM_NC_POSTPEAK_SCALAR_CLOSURE_AND_D15_PRECHECK_R06_results.json`
5. `history/NZ_SCCM/R06_POSTPEAK_C2_AND_COMPILER_HEADTOHEAD_20260810.md`
6. R05 material-native domain/compactification canonical files
7. R04 material-native spectral-domain governance + kernel classification
8. R03 exact-rank4/saddle/special-function evidence
9. R01/R02 ridge/regularization evidence
10. `governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md`
11. Nguyen Ch.3/Appendix-B source evidence + Case21 invariant derivation
