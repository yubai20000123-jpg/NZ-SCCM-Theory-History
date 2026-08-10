# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 19:47 +08:00  
**Purpose:** 唯一当前工作入口；详细推导留在 canonical theory/history/evidence 文件中。  
**Canonical recovery:** `governance/FULL_STARTUP_RECOVERY_CHECKPOINT_20260810.md`

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

此前局部恢复导致的主线偏离及恢复已记录于：

- `history/NZ_SCCM/MAINLINE_DEVIATION_AND_RECOVERY_20260810.md`
- `history/NZ_SCCM/R03_DIMENSION_REDUCTION_SADDLE_AND_SPECIAL_FUNCTION_REFRAME_20260810.md`
- `history/NZ_SCCM/R04_MATERIAL_DOMAIN_AND_NAMED_KERNEL_REFRAME_20260810.md`

任何 compiler failure 不得无证据升级为 current-map architecture failure。

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

工程解析允许内部解析收敛 + 事后 independent audit；audit 不得选阶、调参、选根。

---

## 2. 当前材料/张量骨架

\[
\mathbf E_u=\frac{(1-\nu)\mathbf E+\nu\,\mathrm{tr}(\mathbf E)\mathbf I}{1-\nu^2},
\qquad J_1=\mathrm{tr}\mathbf E_u,
\qquad J_2=\det\mathbf E_u.
\]

G18/G27 unified coaxial architecture：

\[
\boxed{
\boldsymbol\sigma=U(\mathbf E_u)
+J_2[A(J_1,J_2)\mathbf I+B(J_1,J_2)\mathbf E_u]
}
\]

一致切线必须从同一个 stress map 解析求导。G20/G21 允许 C1/C2 regularization、平滑保守 CC/TC/TT target、current/rotating principal surface、保守 tension stiffening 与 smooth postpeak compression；不恢复 runtime TT/TC/CC material-state machine。

---

## 3. MATERIAL-NATIVE SPECTRAL DOMAIN — R04 新治理锁

Canonical governance：

- `governance/MATERIAL_NATIVE_SPECTRAL_DOMAIN_RULE_20260810.md`

生产材料谱域不得再由 Case21/Swartz24 几何定义：

```text
PRIMARY_DOMAIN   = MATERIAL_ADMISSIBLE_SPECTRAL_DOMAIN Lambda_M
SECONDARY_DOMAIN = STRUCTURAL_REACHABLE_SUBDOMAIN Lambda_R
MANDATORY         = Lambda_R subset of Lambda_M
```

含义：

1. 材料 compiler 首先必须在所选本构自身允许/需要覆盖的谱域内通过 stress+tangent+shape+complexity gate；
2. Case21/Swartz reachable spectra 只作后验结构验证和可选加速；
3. 不允许由结构 Pu 或 Swartz 样本反向缩小材料谱域；
4. NC 与 UHPC 可以有不同 `Lambda_M`，但共享完全相同的 Eu/J1/J2、2x2 matrix-function、rank/separable compilation、D15 与 P/Rq/L 架构。

普通混凝土来源锚点：Nguyen Chapter 3 equivalent-uniaxial framework；Saenz Eq.3.39 在 Nguyen 中注明适用于强度不超过 70 MPa 的混凝土；Foster/Nguyen tension transition 从 `eps_cr` 到 `alpha1 eps_cr`, `alpha1=10` 后进入 residual plateau；source post-crushing 从 `eps_p` 到 `gamma2 eps_p` 再进入 residual plateau，项目 G21 source audit 记录 `gamma2=10`。这些只定义 domain interface；最终 NC `lambda_min/lambda_max` 尚未冻结，因为 compact production NC operator 尚未冻结。

UHPC 后续必须由最终选择的 UHPC 本构来源自己给出 `Lambda_M_UHPC`；严禁继承 NC 数字谱域。

---

## 4. D15 / exact moment mainline

G26：

\[
\boxed{continuous\ material\to moment\!-\!first\ contraction\to D15\ exact\ moments}
\]

```text
NAIVE_EXPAND_THEN_INTEGRATE = REJECTED
MOMENT_FIRST_D15 = ACTIVE
```

G28/G30 已确认 `M(epsilon) -> analytic representation -> D15 -> P,Rq,L`；Pu 不另造 load stepping/arclength solver。

```text
LATEST_FULLY_DELIVERED_STAGE = G30
LATEST_OPERATIONALLY_ACCEPTED_STAGE = G30
LATEST_EXECUTED_ARTIFACT_STAGE = G31
G31_FINAL_VISIBLE_DELIVERY = ABSENT
G31_USER_ACCEPTANCE = UNRESOLVED
```

G31 `Pu≈476.936 kN` 只是不考虑裂化的 chain validation，不是 validated RC Pu。

---

## 5. Case21 invariant foundation

```text
q=A/b
M=pi^2/eps0*(q0*q+q^2/2)
B=pi^2/(2eps0)*(t/b)*q
H=u^2+v^2-2u^2v^2
K=nu*u^2-v^2+(1-nu)u^2v^2
W=uvz
```

\[
I_1=(\nu-1)D+MH+2BW,
\]

\[
I_2=-\nu D^2+DMK+BD(\nu-1)W+BMW(2-u^2-v^2)+B^2z^2(u^2+v^2-1).
\]

`I2` 中全部 `M^2` 项严格抵消；`I1,I2` 为有限 polynomial field。

---

## 6. 已失败/限制的 compiler

```text
M1 simple polynomial = FAIL
M1R rational = material regression good / production HOLD
PF1 R02-R06 = exact mathematics AUDIT ONLY
PF1 R06 15x15 connection = FAIL production complexity
PF1 R07 = CANCELLED
P2A one-global primitive polynomial <=16 = FAIL
```

P2A max normalized error：`U≈2.43%`, `C≈2.44%`, `C2≈0.51%`, `T≈32.58%`, `T8≈43.28%`。

---

## 7. R01/R02 — current-target ridge diagnosis

R01 定位三条 narrow tensile transition ridge：

```text
lambda≈0
lambda≈xcr≈0.05
lambda≈10*xcr≈0.50
```

characteristic width `≈0.00249936`。

R02：适度展宽有物理帮助但不能单独解决解析复杂度：

```text
k=1.25: curvature reduction ~19.8%; TC tangent P95 change ~4.38%
k=1.50: curvature reduction ~33.0%; TC tangent P95 change ~9.73%
k>=1.75: HOLD
PURE_WIDTH_WIDENING = INSUFFICIENT_AS_SOLE_SOLUTION
K_1P25 = OPTIONAL, NOT FROZEN
```

---

## 8. R03 — spectral reduction / saddle / exact rank-4

Canonical：

- `current/theory/NZ_SCCM_SPECTRAL_REACHABLE_DOMAIN_REDUCTION_R03_20260810.md`
- `current/theory/NZ_SCCM_SPECTRAL_REACHABLE_DOMAIN_REDUCTION_R03_results.json`
- `evidence/mathematics/NZ_SCCM_SPECIAL_FUNCTION_AND_SADDLE_SURFACE_RESEARCH_R03_20260810.md`

R03 证明在其明确 diagnostic box 内 Swartz24 geometries 有正谱间隙；该结论现在正式定级为**结构诊断**，不再作为 production material spectral domain。

Reference principal stress surface 局部确有 saddle-like patches，但并非单一 global hyperbolic paraboloid。

最重要：source-shaped principal surface 精确 separated rank <=4：

\[
s_+=U(\lambda_+)-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8,
\]

\[
s_-=U(\lambda_-)-a_{cc}C_-^2C_+ +C_-T_+-\rho a_tT_-T_+^8.
\]

```text
EXACT_RANK4_PRINCIPAL_FACTORIZATION = RETAINED
GENERIC_2D_SURFACE_FIT = NOT_NEEDED_FOR SOURCE-SHAPED REFERENCE
```

R03 的 Appell F1 master 与 Carlson research 保留为 named-kernel library；只有 actual reduced kernel 匹配时才能获得 production 身份。

---

## 9. R04 — exact rank-4 branch kernel classification

Canonical：

- `current/theory/NZ_SCCM_EXACT_RANK4_BRANCH_KERNEL_CLASSIFICATION_R04_20260810.md`
- `current/theory/NZ_SCCM_EXACT_RANK4_BRANCH_KERNEL_CLASSIFICATION_R04_results.json`
- `evidence/mathematics/NZ_SCCM_R04_NAMED_KERNEL_AND_MATRIX_FUNCTION_EVIDENCE_20260810.md`

### 9.1 Exact scalar algebra

消去 `R=sqrt(z^2+eta^2)` 后，`p=Pi_eta(z)` 满足二次代数关系：

```text
4 eta^4 p^2 + 8 eta^2 p^2 z^2 - 4 eta^2 p z^3
- eta^2 z^4 + 4 p^2 z^4 - 4 p z^5 = 0
```

而 Foster H 在去掉固定归一化常数后满足：

```text
hbar^2-(r-r0)hbar-eta_r^2/4=0
```

故 generic scalar field degree upper bounds：

```text
C(lambda)   <=2
T(lambda)   <=8
T(lambda)^8 <=8
U(lambda)   <=8
```

这些是上界，不声称 irreducible degree。

### 9.2 Structural spectral substitution complexity

`lambda±=mu±sqrt(Q)` 后的 generic algebraic extension upper bounds：

```text
U(lambda+)   <=16
C+^2 C-      <=8
C+ T-        <=32
T+ T-^8      <=128
```

因此当前 source-shaped exact tension tower 的真正难点已经被定位为**一维材料 primitive 本身的 nested radical complexity**，而不是二维 surface rank，也不是 D15 本身。

### 9.3 Named special-function result

```text
finite polynomial / D15 Beta moments         = PASS DIRECT
bilinear sin^2 denominator / Appell F1       = PASS DIRECT
small derivative Appell family               = PASS CONDITIONAL
single cubic/quartic sqrt / Carlson RF/RD/RJ = PASS CONDITIONAL
full Pi+H1+H10 source tower / Appell          = FAIL GENERIC
full Pi+H1+H10 source tower / Carlson         = FAIL GENERIC
large PF/Gauss-Manin/ODE connection           = FAIL PRODUCTION
```

因此“曲面像马鞍”并不能直接把完整 frozen source oracle 变成一个简单 Appell/Carlson 积分。Appell/Carlson 仍然是有价值的小型 kernel library，但不是 full-source magic wrapper。

R04 正式：

```text
EXACT_RANK4_BRANCH_KERNEL_CLASSIFICATION_R04 = PASS_WITH_NEGATIVE_SPECIAL_FUNCTION_RESULT
MATERIAL_NATIVE_SPECTRAL_DOMAIN_GOVERNANCE = PASS
FULL_SOURCE_EXACT_APPELL_CLOSURE = FAIL_GENERIC
FULL_SOURCE_EXACT_CARLSON_CLOSURE = FAIL_GENERIC
SWARTZ24_AS_PRODUCTION_SPECTRAL_DOMAIN = REJECT
ROUTE_SWITCH = NO
CASE21_PU = NOT_RUN
SWARTZ24_PU = NOT_RUN
```

---

## 10. Gate A/B/C

```text
Gate A = exact/engineering-analytic direct structural closure
Gate B = concrete nonlinear/material adequacy
Gate C = production analytic complexity
```

Gate C：zero formal x/y/z quadrature；zero auxiliary quadrature/ODE；no runtime TT/TC/CC state propagation；`P,Rq` and derivatives -> direct finite formulas；large auxiliary systems != production。

---

## 11. Material/structure status

Ordinary concrete：Nguyen/Foster = primary source/benchmark；final compact production scalar/current closure OPEN。

Reinforcement：

\[
P=P_c+P_s,\qquad R_q=R_{q,c}+R_{q,s}
\]

必须在 root solve 前进入。

UHPC：仅 `fc=141.1 MPa` 用户强制冻结；final strong multiaxial production operator OPEN；其 material-native spectral domain 必须由最终 UHPC source/model 独立定义。

Steel shell/Y：`M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE`。PBL 保持强局部边界/子板分隔身份。

---

## 12. Case21 / Swartz24 production status

```text
Case21 = analytic benchmark; no new final RC Pu frozen
old 338/342 kN = audit/reference only
G31 476.936 kN = uncracked chain validation only
Swartz24 production Pu = PAUSED
```

结构 Pu 不得反标材料、material-native domain、平滑量、compiler order 或 root selection。

---

## 13. 当前唯一下一理论任务

```text
CURRENT_RECOMMENDED_NEXT_TASK = MATERIAL_NATIVE_1D_PRIMITIVE_REFORMULATION_R05
```

R05 不是新的二维 surface fit，也不是新的空间积分理论。它必须：

1. 先选定/冻结普通混凝土 production target 的 **material-native scalar domain contract**；
2. 将 NC scalar branches 分成物理必须保留的 landmarks（origin tangent、peak、cracking transition、residual/postpeak behavior）与可允许的 C1/C2 conservative regularization；
3. 在该 material domain 上建立极少数一维 compact primitive candidates；
4. 优先要求 finite polynomial/Beta-D15；若使用 rational/algebraic basis，则必须在拟合前证明只产生 small Appell/Carlson/other named kernels；
5. stress + same-map tangent + shape + source-validity 同时过 Gate B；
6. 保留 exact rank<=4 / invariant reconstruction；
7. 结构 reachable spectra 只在材料版本冻结后作 verification；
8. UHPC 后续沿同一 R05 interface，用自己的 material-native domain 和 scalar source 替换 NC，不改 structural theory。

禁止：再用 Swartz24 spectrum 定义 production material range；blind degree escalation；generic 2D fitting；large PF/ODE rescue；Case21/Swartz Pu calibration。

---

## 14. 恢复读取顺序

1. `current/CURRENT_STATE.md`
2. `governance/MATERIAL_NATIVE_SPECTRAL_DOMAIN_RULE_20260810.md`
3. `current/theory/NZ_SCCM_EXACT_RANK4_BRANCH_KERNEL_CLASSIFICATION_R04_20260810.md`
4. `current/theory/NZ_SCCM_EXACT_RANK4_BRANCH_KERNEL_CLASSIFICATION_R04_results.json`
5. `history/NZ_SCCM/R04_MATERIAL_DOMAIN_AND_NAMED_KERNEL_REFRAME_20260810.md`
6. R03 canonical theory/results/evidence
7. R01/R02 canonical reports
8. `governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md`
9. Case21 invariant derivation
10. explicit NC/rebar source operator + Nguyen Chapter 3 source
