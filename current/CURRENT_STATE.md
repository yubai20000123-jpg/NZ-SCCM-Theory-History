# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 19:20 +08:00  
**Purpose:** 唯一当前工作入口。历史 PASS、旧路线、迁移期文件不得覆盖本文件。  
**Canonical recovery:** `governance/FULL_STARTUP_RECOVERY_CHECKPOINT_20260810.md`

## 0. 主线身份

```text
G18/G27 invariant current-map architecture = ACTIVE
G20/G21 smooth conservative material philosophy = RETAINED
G26 moment-first D15 architecture = RETAINED
G28/G30 direct analytic P,Rq,L kernel = RETAINED
M1R/PF1/P2A = COMPILER/REPRESENTATION EXPERIMENTS, NOT ARCHITECTURE REPLACEMENTS
P2R = CANCELLED
ROUTE_SWITCH = NO
```

此前局部恢复导致的主线误判已记录：

- `history/NZ_SCCM/MAINLINE_DEVIATION_AND_RECOVERY_20260810.md`
- `history/NZ_SCCM/R03_DIMENSION_REDUCTION_SADDLE_AND_SPECIAL_FUNCTION_REFRAME_20260810.md`

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
GAUSS/SIMPSON/ADAPTIVE = PROHIBITED_IN_FORMAL_OPERATOR
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

一致切线必须从同一 stress map 解析微分获得。

G20/G21 继续允许：C1/C2 regularization、平滑保守 CC/TC/TT target、current/rotating principal surface、保守 tension stiffening、smooth postpeak compression；不恢复 runtime TT/TC/CC state machine。

---

## 3. D15 / exact moment mainline

G26：

\[
\boxed{continuous\ material\to moment\!-\!first\ contraction\to D15\ exact\ moments}
\]

with

\[
s=\sin^2X,\quad t=\sin^2Y,\quad \eta=\zeta^2,\quad \chi=\sin X\sin Y\zeta.
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

## 4. Case21 invariant foundation

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

## 5. 已失败/限制的 compiler

```text
M1 simple polynomial = FAIL
M1R rational = material regression good / production HOLD
PF1 R02-R06 = exact mathematics AUDIT ONLY
PF1 R06 15x15 connection = FAIL production complexity
PF1 R07 = CANCELLED
P2A one-global primitive polynomial <=16 = FAIL
```

P2A：`U≈2.43%`, `C≈2.44%`, `C2≈0.51%`, `T≈32.58%`, `T8≈43.28%` max normalized errors。

---

## 6. R01/R02 已关闭的问题

R01：current reference 中存在三条 narrow tensile ridge：

```text
lambda≈0
lambda≈xcr≈0.05
lambda≈10*xcr≈0.50
```

characteristic width `≈0.00249936`，相对历史大域尺度比约 `1268.6:1`。

R02：适度展宽有物理帮助，但不能单独解决解析复杂度：

```text
k=1.25: curvature reduction ~19.8%; TC tangent P95 change ~4.38%
k=1.50: curvature reduction ~33.0%; TC tangent P95 change ~9.73%
k>=1.75: HOLD
```

但 full-domain degree-32 `T` error 从 `31.81%` 仅降到 `31.32%` (`k=2`)。

```text
PURE_WIDTH_WIDENING = INSUFFICIENT_AS_SOLE_SOLUTION
K_1P25 = OPTIONAL, NOT FROZEN
```

R02 同时证明 spectral/reachable-domain reduction 比物理展宽更有效。

---

## 7. R03 — spectral reachable-domain reduction

Canonical：

- `current/theory/NZ_SCCM_SPECTRAL_REACHABLE_DOMAIN_REDUCTION_R03_20260810.md`
- `current/theory/NZ_SCCM_SPECTRAL_REACHABLE_DOMAIN_REDUCTION_R03_results.json`
- `evidence/mathematics/NZ_SCCM_SPECIAL_FUNCTION_AND_SADDLE_SURFACE_RESEARCH_R03_20260810.md`

### 7.1 r convention

```text
r = ell/b
cases 1-16: r=2
cases 17-24: r=1
```

### 7.2 Analytic spectral-order condition

\[
\boxed{
D>D_{sep}(q)=\frac{C_m}{r^2(1+\nu)}+
\frac{|C_b|(1-r^{-2})}{1+\nu}
}
\]

R03 common **diagnostic** contract：

```text
D in [0.60,0.78]
q in [0.0001,0.006]
```

24 Swartz geometries 全部 certified。Worst = Case 11：

```text
D_sep(q=0.006)=0.3214976720
certified gap lower at D=0.60=0.2785023280
audit min gap=0.3179329509
```

Audit union：

\[
\lambda_+\in[-0.479285,0.479285],
\qquad
\lambda_-\in[-1.123467,-0.252159].
\]

**Final Swartz24 production D-q box remains OPEN.** 当前结果不能冒充最终 production reachability theorem。

### 7.3 Saddle geometry

Reference `s1(lambda1,lambda2)` Hessian diagnostic：

```text
saddle-like det(H)<0 ~30.62%
convex-like          ~68.54%
concave-like         ~0.84%
```

因此曲面局部确有马鞍性，但不是 global hyperbolic paraboloid；视觉形状本身不能决定积分公式。

### 7.4 R03 最重要结果：exact separated rank <= 4

\[
s_+=U(\lambda_+)-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8,
\]

\[
s_-=U(\lambda_-)-a_{cc}C_-^2C_+ +C_-T_+-\rho a_tT_-T_+^8.
\]

因此每个 principal stress surface **严格由最多四个一维函数乘积组成**。

```text
EXACT_RANK4_PRINCIPAL_FACTORIZATION = PROMOTED
GENERIC_2D_SURFACE_FIT = NOT_NEEDED_FOR_SOURCE_SHAPED_REFERENCE
```

R03 reachable rectangle 的 numerical SVD：rank 2 已 `<1e-4` relative Frobenius residual，rank 3 到 machine level。原因之一：

```text
max |T(lambda-)| ~= 1.238e-4
```

若干 tensile-on-negative-branch interaction 在当前 diagnostic contract 内天然极小。

### 7.5 1D branch compiler difficulty

```text
lambda-:
  U,C,T,T8 -> degree 8 already <=0.1% normalized max error

lambda+:
  U -> <=1% by degree 32
  C -> <=1% by degree 48
  T,T8 -> degree 96 still not <=1% on broad R03 diagnostic union
```

困难已从“整个二维材料面”收缩为 **positive ordered branch 的 tensile scalar transition**。

### 7.6 Named special-function kernel

对

\[
D=a+b\sin^2X+c\sin^2Y+d\sin^2X\sin^2Y,
\]

whole-domain exact master：

\[
\boxed{
\mathcal M=\frac{\pi^2}{\sqrt{a(a+b)}}
F_1\left(\frac12;\frac12,\frac12;1;-\frac ca,-\frac{c+d}{a+b}\right)
}
\]

R03 demo：

```text
formal Appell F1 = 6.611588675823622
audit-only Gauss = 6.611588675823635
relative diff = 1.881e-15
formal quadrature count = 0
```

Appell F1 / Carlson RF,RD,RJ 只有在 **actual reduced kernel matches their algebraic class** 时才是 production candidate；不得借此重开 large PF/Gauss-Manin system。

### 7.7 Coalescence-safe 2x2 matrix function

\[
X=\mu I+Y,\quad Y^2=r_s^2I,
\]

\[
f(X)=f_eI+f_oY,
\]

\[
f_e=\frac{f(\mu+r_s)+f(\mu-r_s)}2,
\qquad
f_o=\frac{f(\mu+r_s)-f(\mu-r_s)}{2r_s}\to f'(\mu).
\]

该形式在 principal values 接近时仍连续，不需要 runtime material-state partition。

---

## 8. 正式 Gate A/B/C

```text
Gate A = exact/engineering-analytic direct structural closure
Gate B = concrete nonlinear/material adequacy
Gate C = production analytic complexity
```

Gate C：

```text
no formal x/y/z numerical quadrature
no auxiliary quadrature
no auxiliary ODE stepping
no hidden initialization
no runtime TT/TC/CC state partition
P,Rq and derivatives -> direct finite formulas
large auxiliary connection system != production
actual formulas must be exposed
```

---

## 9. Other material/structure status

Ordinary concrete：Nguyen/Foster = primary benchmark/reference；final compact production closure OPEN。

Reinforcement 必须在 root solve 前：

\[
P=P_c+P_s,\qquad R_q=R_{q,c}+R_{q,s}.
\]

UHPC：仅 `fc=141.1 MPa` 用户强制冻结；final strong multiaxial production operator OPEN；UHPC-C0 不是 production。

Steel shell/Y：`M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE`。PBL 保持强局部边界/子板分隔身份。

---

## 10. Case21 / Swartz24 production status

```text
Case21 = analytic benchmark; no new final RC Pu frozen
old 338/342 kN = audit/reference only
G31 476.936 kN = uncracked chain validation only
Swartz24 production Pu = PAUSED
```

结构 Pu 不得反标材料、reachable domain、平滑量或 compiler order。

---

## 11. 当前唯一下一理论任务

```text
CURRENT_RECOMMENDED_NEXT_TASK = EXACT_RANK4_BRANCH_KERNEL_CLASSIFICATION_R04
```

R04 禁止 generic 2D surface fitting。只允许：

1. 以 exact rank-4 principal factorization 为材料结构；
2. 负谱分支作为低复杂度 1D primitive candidate，逐项检查 stress+tangent；
3. 正谱分支保留 source landmarks，不盲目提高 global polynomial degree；
4. 将真正活跃 separated products 经 `lambda± -> (J1,J2) -> Case21/Swartz kinematics` 复合；
5. **拟合新函数之前**逐项分类 structural moments 是否落入：
   - finite Beta/D15 polynomial moments；
   - Appell F1；
   - Carlson RF/RD/RJ；
   - 其它直接小型 named special function；
6. 如重新需要 large PF/Gauss-Manin/ODE state system，立即 FAIL Gate C；
7. 只有 exact source positive branch 没有小型 named kernel 时，才允许进入严格受限的 sigmoid-aware **1D** scalar representation screen。

R04 不使用 Case21/Swartz Pu 选择材料或表示。

---

## 12. 恢复读取顺序

1. `current/CURRENT_STATE.md`
2. `governance/FULL_STARTUP_RECOVERY_CHECKPOINT_20260810.md`
3. `history/NZ_SCCM/MAINLINE_DEVIATION_AND_RECOVERY_20260810.md`
4. `history/NZ_SCCM/R03_DIMENSION_REDUCTION_SADDLE_AND_SPECIAL_FUNCTION_REFRAME_20260810.md`
5. `current/theory/NZ_SCCM_SPECTRAL_REACHABLE_DOMAIN_REDUCTION_R03_20260810.md`
6. `current/theory/NZ_SCCM_SPECTRAL_REACHABLE_DOMAIN_REDUCTION_R03_results.json`
7. `evidence/mathematics/NZ_SCCM_SPECIAL_FUNCTION_AND_SADDLE_SURFACE_RESEARCH_R03_20260810.md`
8. R01/R02 canonical reports
9. Case21 invariant derivation
10. explicit NC/rebar source operator
