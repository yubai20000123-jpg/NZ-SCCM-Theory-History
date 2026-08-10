# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 22:20 +08:00  
**Purpose:** 唯一当前工作入口。详细推导、历史偏离/恢复、失败 compiler 与执行证据留在 canonical governance/theory/history/evidence 文件中。

## 0. 最高优先级：EXPLICIT END-TO-END CAPACITY

Canonical current files:

- `governance/EXPLICIT_END_TO_END_CAPACITY_DOCTRINE_20260810.md`
- `governance/USER_SKETCH_SHAPE_PRESERVING_SMOOTHING_RULE_20260810.md`
- `current/theory/NZ_SCCM_USER_SKETCH_SMOOTH_AND_RC_CASE21_R08_20260810.md`
- `current/theory/NZ_SCCM_USER_SKETCH_SMOOTH_AND_RC_CASE21_R08_results.json`
- `history/NZ_SCCM/R08_USER_SKETCH_SMOOTH_AND_RC_CASE21_20260810.md`

User highest requirement:

```text
最终极限承载力必须由显式公式及同一公式的显式导数得到。
```

允许使用 4D stress-strain manifold、invariant/spectral current map、whole-structure global target、低秩面、polynomial/rational/algebraic formula、named special functions、局部 analytic patch、显式 piecewise smooth function 等。

材料 pointwise regression error 不是首要目标。允许 deliberate under-use / smoothing / trimming 局部尖峰；必须透明说明削弱/增强的力学后果。

---

## 1. 最终容量方程

\[
P(D,q),\qquad R_q(D,q)=0,
\]

\[
L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0,
\]

\[
P_u=P(D^*,q^*).
\]

`P,Rq,P_,D,P_,q,Rq_,D,Rq_,q` 必须来自同一显式数学表示。

结构层继续保留：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
```

数值求根可用于求已经显式得到的有限方程。

---

## 2. 材料处理原则 — R08 用户草图修正

R07R 的 rational material curve 虽然全局连续，但 tensile side 出现了人为的 `overshoot -> dip -> rebound`。该形状不再接受为目标。

当前 preferred material-data processing：

```text
source/measured sharp local feature
-> deliberately do not use the full sharp feature
-> replace it by one low-parameter shape-preserving smooth cap
-> keep important material landmarks explicit
-> then inspect structural consequence
```

Tension prototype must have:

- one monotone rise from origin;
- one rounded retained peak;
- one monotone decay to residual;
- zero tangent at retained peak and residual onset;
- no secondary undershoot;
- no rebound;
- no oscillation introduced only by the regression family.

This is a data-processing choice, not an attempt to reproduce every sharp source feature.

---

## 3. MATERIAL-NATIVE DOMAIN GOVERNANCE

```text
PRIMARY_DOMAIN   = MATERIAL_ADMISSIBLE_SPECTRAL_DOMAIN Lambda_M
SECONDARY_DOMAIN = STRUCTURAL_REACHABLE_SUBDOMAIN Lambda_R
MANDATORY        = Lambda_R subset of Lambda_M
```

Case21/Swartz24 cannot define the production material domain.

NC source-active landmark interval remains recorded as

\[
\Lambda_{M,NC}^{active}=[-10,0.49987179453974245].
\]

UHPC must derive its own `Lambda_M`; NC numerical bounds must not be copied into UHPC.

---

## 4. R08 explicit user-sketch NC scalar target

Compression:

```text
lambda < -10         : residual -0.10 fc
-10 <= lambda < -1   : R06 C2 source-faithful postpeak target
-1 <= lambda < 0     : Saenz compression
```

Tension:

```text
0 <= lambda <= lambda_p : quintic Hermite monotone rise
lambda_p < lambda <= lambda_r : quintic Hermite monotone decay
lambda > lambda_r : residual 0.03 fc
```

Landmarks:

\[
\lambda_p=x_{cr}=0.049987179454,
\quad
u(\lambda_p)=0.09,
\]

\[
\lambda_r=10x_{cr}=0.49987179454,
\quad
u(\lambda_r)=0.03.
\]

Rise polynomial in local `tau`:

\[
0+0.1\tau+0\tau^2+0.3\tau^3-0.55\tau^4+0.24\tau^5.
\]

Fall polynomial:

\[
0.09-0.6\tau^3+0.9\tau^4-0.36\tau^5.
\]

Executed shape audit:

```text
rise monotone = PASS
fall monotone = PASS
peak = 0.09 fc
residual = 0.03 fc
slope at origin = kappa
slope at peak = 0
slope at residual = 0
```

`R07R_RATIONAL_TENSILE_OSCILLATION = REJECTED_AS_UNNECESSARY`.

---

## 5. Case21 reinforcement — analytic same-equation coupling

Source mapping:

```text
rho_x = rho_y = 0.00375
Es = 200000 MPa
fy = 530 MPa
eps_y = 0.00265
```

Let

\[
S=q_0q+\frac12q^2,
\qquad
C_m=\frac{\pi^2S}{\varepsilon_0}.
\]

Exact loading-direction steel load:

\[
P_s=
\frac{\rho_y t b E_s\varepsilon_0}{1000}
\left(D-\frac{C_m}{4}\right).
\]

Exact steel amplitude residual:

\[
R_s=
\frac{\rho_y tE_s\pi^2(q_0+q)b\ell}{1000}
\left[
\frac{\varepsilon_0D(\nu-1)}4
+\frac{9\pi^2S}{32}
\right].
\]

The total equations are solved as

\[
P=P_c+P_s,
\qquad
R=R_c+R_s=0,
\]

then

\[
L=P_D R_q-P_qR_D=0.
\]

No `Pu = Pu,c + As fy` post-addition is permitted.

---

## 6. R08 explicit whole-structure target and mandatory refinement

A first coarse degree-(11,11) target on

```text
D in [0.35,1.30]
q in [0.001,0.030]
```

was **rejected** because the `Rc` off-grid/root residual error was too large. Its apparent `Pu=335.047660 kN` is deprecated and must not be used.

The low-q equilibrium branch was then mechanically located from the same material + reinforcement equations, without using the experimental load. A local explicit target was frozen on

```text
D in [0.60,0.84]
q in [0.012,0.0215]
```

Degree sequence `12,14,16,18` was executed. Degree 18 was retained.

Retained validation:

```text
Pc max abs = 0.087275 kN
Pc P95     = 0.059938 kN
Rc max abs = 15.9990 kN mm
Rc P95     = 10.8955 kN mm
```

At the final explicit stationary root, the independent underlying-material audit gives

```text
P_total_audit = 335.585377 kN
R_total_audit = -1.021793 kN mm
P_explicit - P_audit = +0.004406 kN
```

---

## 7. R08 final explicit RC Case21 result

\[
D_u=0.708108615160,
\]

\[
q_u=0.0166001000745,
\qquad
A_u=20.252122\ \mathrm{mm}.
\]

\[
P_c=317.266522\ \mathrm{kN},
\qquad
P_s=18.323261\ \mathrm{kN},
\]

\[
\boxed{P_u=335.589783\ \mathrm{kN}}.
\]

Experiment:

\[
P_f=368.312750\ \mathrm{kN}.
\]

Error:

\[
\boxed{-8.884560\%}.
\]

Reinforcement at this state remains fully elastic:

```text
y-rebar strain range = [-0.00147995, +0.00028949]
x-rebar strain range = [+0.00026639, +0.00203583]
yield strain          = 0.00265
```

This is the current **minimal scalar current-surface + analytic reinforcement** Case21 diagnostic result.

---

## 8. Interpretation of the remaining deficiency

The ~8.9% underprediction is NOT a reason to restore the deleted sharp tensile peak or the R07R rational oscillation.

The next physical question is whether the minimal scalar surface is missing a **small source-grounded multiaxial compression / tension-compression enhancement**.

Any next correction must be smaller and simpler than the historical full CC/TC/TT operator, and must be added only because it repairs an identified mechanical deficiency.

---

## 9. Formal-status boundary

R08 runtime `P,R,L` evaluation is finite and explicit.

However, the retained local `Pc(D,q),Rc(D,q)` coefficients were identified offline using high-accuracy full-halfwave numerical integration.

Therefore:

```text
USER_SKETCH_TENSION_SHAPE = PASS
ANALYTIC_REINFORCEMENT_COUPLING = PASS
RC_CASE21_EXPLICIT_LIMIT = PASS_DIAGNOSTIC
FORMAL_ZERO_SPATIAL_QUADRATURE_PRODUCTION = HOLD
```

This proof-of-concept identity is not silently relabeled as the older pure-D15 zero-quadrature production identity.

---

## 10. Old tool identity

```text
G18/G27 invariant current map = RETAINED TOOL
G20/G21 smooth conservative philosophy = RETAINED
G26 D15 = RETAINED ANALYTIC TOOL
G28/G30 P,Rq,L kernel = RETAINED
R03 exact rank<=4 = RETAINED TOOL
R04 Appell/Carlson = RETAINED KERNEL LIBRARY
R05/R06 compactification evidence = RETAINED EVIDENCE
R07R rational tensile shape = DEMOTED / oscillatory local shape rejected
R08 user-sketch smooth cap + analytic reinforcement = CURRENT
```

---

## 11. UHPC / Swartz24

UHPC: `fc=141.1 MPa` remains the user-forced value. Its arbitrary multiaxial current surface is still open. UHPC may use the same shape-preserving under-use philosophy, but must derive its own source landmarks and material-native domain.

Swartz24 production remains paused until the NC explicit RC chain and the minimum multiaxial correction are frozen.

---

## 12. Current recommended next task

```text
CURRENT_RECOMMENDED_NEXT_TASK
= R09_MINIMUM_SOURCE_GROUNDED_MULTIAXIAL_CORRECTION
```

R09 must:

1. keep the R08 monotone user-sketch tensile cap;
2. keep the exact analytic Case21 reinforcement coupling;
3. add only one minimal source-grounded multiaxial correction candidate;
4. recompute the same explicit `P,R,L` chain;
5. determine whether the remaining ~8.9% Case21 deficiency is plausibly a missing multiaxial effect;
6. not tune the correction directly to the experiment and not restore the full historical CC/TC/TT complexity.

---

## 13. Recovery read order

1. `current/CURRENT_STATE.md`
2. `governance/EXPLICIT_END_TO_END_CAPACITY_DOCTRINE_20260810.md`
3. `governance/USER_SKETCH_SHAPE_PRESERVING_SMOOTHING_RULE_20260810.md`
4. `current/theory/NZ_SCCM_USER_SKETCH_SMOOTH_AND_RC_CASE21_R08_20260810.md`
5. `current/theory/NZ_SCCM_USER_SKETCH_SMOOTH_AND_RC_CASE21_R08_results.json`
6. `history/NZ_SCCM/R08_USER_SKETCH_SMOOTH_AND_RC_CASE21_20260810.md`
7. Case21 reinforcement source/baseline files
8. R07R, then R06/R05/R04/R03/R02/R01 history/evidence
9. Case21 invariant exact-moment foundation
