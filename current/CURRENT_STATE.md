# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 20:00 +08:00  
**Purpose:** 唯一当前工作入口；详细推导留在 canonical theory/history/evidence 文件中。

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

此前局部恢复导致的主线偏离及恢复已记录；R03-R05 继续沿恢复后的同一主线推进。

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

Production grammar 不要求永久保留旧 source-shaped `C,T,T^8` primitives；它们可继续作为 benchmark/reference。当前优先闭合一维 scalar master `U`，随后再闭合低参数 `A,B` interaction layer。

---

## 3. MATERIAL-NATIVE DOMAIN GOVERNANCE

Canonical：

- `governance/MATERIAL_NATIVE_SPECTRAL_DOMAIN_RULE_20260810.md`
- `governance/MATERIAL_NATIVE_SCALAR_DOMAIN_CONTRACT_R05_20260810.md`

```text
PRIMARY_DOMAIN   = MATERIAL_ADMISSIBLE_SPECTRAL_DOMAIN Lambda_M
SECONDARY_DOMAIN = STRUCTURAL_REACHABLE_SUBDOMAIN Lambda_R
MANDATORY         = Lambda_R subset of Lambda_M
```

材料 compiler 必须先在所选本构自身定义的谱域上通过 Gate B/C。Case21/Swartz reachable spectra 只作后验结构验证和可选效率诊断，不允许由 Pu 或样本反向缩小材料谱域。

NC 与 UHPC 可以有不同 `Lambda_M`，但共享 Eu/J1/J2、2x2 matrix-function、separable/invariant compilation、D15 与 P/Rq/L 架构。UHPC 禁止继承 NC 数字谱域。

---

## 4. R05 — MATERIAL-NATIVE 1D PRIMITIVE REFORMULATION

Canonical：

- `current/theory/NZ_SCCM_MATERIAL_NATIVE_1D_PRIMITIVE_REFORMULATION_R05_20260810.md`
- `current/theory/NZ_SCCM_MATERIAL_NATIVE_1D_PRIMITIVE_REFORMULATION_R05_results.json`
- `history/NZ_SCCM/R05_MATERIAL_NATIVE_DOMAIN_AND_COMPACTIFICATION_20260810.md`

### 4.1 NC material-native scalar landmarks

采用等效单轴归一化坐标

\[
\lambda=\varepsilon_u/\varepsilon_{p,c}
\]

（压缩为负）。来源/项目保留的材料尺度：

```text
compression residual scale : lambda = -gamma2
compression peak           : lambda = -1
origin                     : lambda = 0
tension cracking           : lambda_cr = rho/kappa
tension residual onset     : lambda = alpha1*rho/kappa
```

当前 ordinary-concrete source choices：

```text
gamma2 = 10
alpha1 = 10
alpha2 = 0.30  # project-conservative residual tension
```

因此 R05 正式冻结 source-native **active transition interval**：

\[
\boxed{
\Lambda_{M,NC}^{active}=[-\gamma_2,\ \alpha_1\rho/\kappa]
}
\]

当前 NC material instance：

```text
rho = 0.10
kappa = 2.0005129533678754
lambda_cr = 0.04998717945397425
Lambda_M,NC^active = [-10, 0.49987179453974245]
```

这不是 Swartz24 谱域。

### 4.2 Material blocker newly exposed

纯 Saenz continuation 在 `lambda=-10` 给出

\[
\sigma/f_c=-0.1980605304506671,
\]

而 Nguyen source postcrush residual landmark 约为

\[
\sigma/f_c=-0.10.
\]

因此纯 Saenz 延拓不能作为完整 material-native deep-postpeak scalar target。G21 已允许 smooth conservative postpeak replacement，但该一维 postpeak closure 现在必须在材料层显式冻结。

```text
FINAL_NC_SCALAR_U = OPEN
```

### 4.3 Compactification screen

Candidate A：one-global Chebyshev in `lambda` — NOT PREFERRED。

Candidate B：

\[
\boxed{
\chi(\lambda)=\frac{\lambda}{\sqrt{\lambda^2+1}}
}
\]

以及

\[
U_n(\lambda)=\sum_{j=0}^{n}a_jT_j(z(\chi)).
\]

`delta=1` 取自归一化 compression-peak material scale，不由 Case21/Swartz Pu 调参。

对 frozen smooth benchmark `U` 的 executed metrics：

```text
n=16: stress P95 0.4118% fc, max 2.4134% fc; tangent P95 3.5923%
n=24: stress P95 0.1276% fc, max 1.5627% fc; tangent P95 2.3531%
n=32: stress P95 0.0692% fc, max 1.1274% fc; tangent P95 1.9274%
```

`n=24` 仅保留为 preferred material representation screen candidate，不是 production coefficient set。`n=32` 仅作 upper-order diagnostic。

Candidate C：degree-9 landmark Hermite in `chi` — FAIL SHAPE；stress max 约 `6.376 fc`，出现严重振荡。

### 4.4 Algebraic complexity advantage

`chi=lambda/sqrt(lambda^2+1)` 仅引入一个 quadratic extension；任意有限 `P_n(chi)` 仍属于 scalar algebraic degree `<=2`。

`lambda±=mu±sqrt(Q)` 后 generic structural field degree `<=4`。

R04 旧 source-shaped `U=Pi+H1+H10...` 的 corresponding upper bounds 是 scalar `<=8`、structural `<=16`。

因此 compactification 是真实 algebraic complexity reduction；但其 D15/small-named-kernel closure 尚未通过 Gate C。

### 4.5 R05 status

```text
MATERIAL_NATIVE_1D_PRIMITIVE_REFORMULATION_R05
= PASS_DOMAIN_AND_COMPACTIFICATION_SCREEN__HOLD_FINAL_NC_SCALAR

MATERIAL_NATIVE_DOMAIN_CONTRACT = PASS
GLOBAL_LAMBDA_POLYNOMIAL = NOT_PREFERRED
LANDMARK_HERMITE_CHI_DEG9 = FAIL_SHAPE_OSCILLATION
SOFTSIGN_DELTA1_N24 = PREFERRED_MATERIAL_SCREEN_CANDIDATE_NOT_PRODUCTION
SOFTSIGN_DELTA1_N32 = DIAGNOSTIC_UPPER_ORDER_ONLY
FINAL_NC_SCALAR_U = OPEN
CASE21_PU = NOT_RUN
SWARTZ24_PU = NOT_RUN
ROUTE_SWITCH = NO
```

---

## 5. R01-R04 retained conclusions

R01：three narrow tensile transition ridges at `lambda≈0`, `xcr≈0.05`, `10xcr≈0.50`；characteristic width `≈0.00249936`。

R02：mild widening helps but cannot solve representation alone；`k=1.25` optional, not frozen。

R03：source-shaped principal surface exact separated rank `<=4`; saddle-like patches exist locally but no single global saddle function identity. Swartz spectral separation result is structural diagnostic only.

R04：full `Pi+H1+H10` source tower is not generic direct Appell/Carlson; Appell/Carlson retained as small named-kernel library only when actual reduced integrand matches. Large PF/Gauss-Manin/ODE remains non-production.

---

## 6. D15 / structural mainline retained

G26：

\[
continuous\ material\to moment\!-\!first\ contraction\to D15\ exact\ moments.
\]

G28/G30：same analytic kernel -> `P,Rq,L`; no second Pu solver or load-stepping identity.

Case21 invariant foundation remains finite polynomial in `I1,I2`; `I2` all `M^2` terms cancel exactly.

---

## 7. Gate A/B/C

```text
Gate A = exact/engineering-analytic direct structural closure
Gate B = concrete nonlinear/material adequacy
Gate C = production analytic complexity
```

Gate C：zero formal x/y/z quadrature；zero auxiliary quadrature/ODE；no runtime TT/TC/CC state propagation；`P,Rq` and derivatives -> direct finite formulas；large auxiliary systems != production。

Any future production formula must be exposed directly; scripts are reproducibility tools, not theory identities.

---

## 8. Material/structure production status

Ordinary concrete：Nguyen/Foster primary source/benchmark；material-native active scalar domain frozen in R05；final compact postpeak scalar/current closure OPEN。

Reinforcement must enter before root solve：

\[
P=P_c+P_s,\qquad R_q=R_{q,c}+R_{q,s}.
\]

UHPC：only `fc=141.1 MPa` user-forced; final strong multiaxial production operator OPEN；its `Lambda_M,UHPC` must come from chosen UHPC source/model, not NC.

Steel shell/Y：`M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE`。PBL retains strong local-boundary/subpanel-segmentation identity.

---

## 9. Case21 / Swartz24 status

```text
Case21 = analytic benchmark; no new final RC Pu frozen
old 338/342 kN = audit/reference only
G31 476.936 kN = uncracked chain validation only
Swartz24 production Pu = PAUSED
```

No structural Pu may tune material domain, postpeak law, compactification order or root selection.

---

## 10. 当前唯一下一理论任务

```text
CURRENT_RECOMMENDED_NEXT_TASK
= NC_POSTPEAK_SCALAR_CLOSURE_AND_SOFTSIGN_D15_KERNEL_PRECHECK_R06
```

R06 必须先于任何 Pu 计算完成：

1. 在 R05 material-native NC domain 内冻结一个 low-parameter、C1/C2、smooth-conservative compression postpeak scalar closure，保留 peak/residual material landmarks；
2. 不用 Swartz/Case21 Pu 调参；
3. 将 `P_n(lambda/sqrt(lambda^2+1))` 直接代入 Case21 invariant/spectral algebra，判定 structural field degree<=4 是否真正能化为 finite D15/Beta 或 small Carlson/Appell/other named kernels；
4. 如果仍需要 large PF/ODE/master-state system，softsign candidate 立即 FAIL Gate C；
5. 只有 R06 material + kernel 双门通过后，才允许继续 `A,B` multiaxial compact closure 或恢复 Case21 Pu。

---

## 11. 恢复读取顺序

1. `current/CURRENT_STATE.md`
2. `governance/MATERIAL_NATIVE_SCALAR_DOMAIN_CONTRACT_R05_20260810.md`
3. `current/theory/NZ_SCCM_MATERIAL_NATIVE_1D_PRIMITIVE_REFORMULATION_R05_20260810.md`
4. `current/theory/NZ_SCCM_MATERIAL_NATIVE_1D_PRIMITIVE_REFORMULATION_R05_results.json`
5. `history/NZ_SCCM/R05_MATERIAL_NATIVE_DOMAIN_AND_COMPACTIFICATION_20260810.md`
6. R04 canonical theory/results + material-native spectral-domain governance
7. R03 exact-rank4/saddle/special-function evidence
8. R01/R02 ridge/regularization reports
9. `governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md`
10. Nguyen Chapter 3 / Appendix-B source evidence and Case21 invariant derivation
