# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 23:09 +08:00  
**Purpose:** 唯一当前工作入口。详细推导、失败路线、历史证据与审计结果保留在 governance / current/theory / evidence / history。

## 0. 最高优先级

```text
FINAL_THEORY_MUST_PRODUCE_ULTIMATE_CAPACITY_FROM_EXPLICIT_FORMULAS
AND_EXPLICIT_DERIVATIVES_OF_THE_SAME FORMULAS.
```

结构层固定：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
N_formal_spatial_quadrature = 0
N_formal_spatial_sampling = 0
N_formal_spatial_subdomains = 1
```

正式理论禁止：空间 Gauss / Simpson / adaptive quadrature、material-point grid、moving TT/TC/CC spatial cells、offline spatial integration 后拟合 production `P/R/U`、有限差分导数、结构试验反标材料参数。

数值求根仍可用于最终已经显式得到的有限方程。

---

## 1. 当前能量路线

用户已将当前主线修正为：

```text
材料层：energy-first / current-work pseudo-potential
结构层：不拟合 whole-structure target
结构内功必须由材料势 + Nguyen 应变 + D15/解析积分直接生成
```

理想链：

\[
\psi_m(\varepsilon)
\rightarrow
\sigma=\partial\psi_m/\partial\varepsilon
\rightarrow
C_t=\partial^2\psi_m/\partial\varepsilon^2
\]

\[
\varepsilon=\varepsilon(D,q,x,y,z)
\rightarrow
\mathcal U(D,q)=\int_\Omega\psi_m\,dV+\mathcal U_s
\]

\[
R_q=\mathcal U_{,q}=0,
\]

\[
\mathcal U_{,DD}\mathcal U_{,qq}-\mathcal U_{,Dq}^2=0,
\]

\[
P_u=\mathcal U_{,D}(D^*,q^*)/c_D.
\]

`integrate-then-differentiate` 与 `differentiate-then-integrate` 必须最终逐项一致。

材料势可有少量具有明确物理意义的材料参数以及由材料锚点/能量条件唯一确定的派生代数常数；禁止大量 generic free fitting coefficients。

---

## 2. R09B material-energy observation retained

当前 NC 参数：

```text
fc = 21.23 MPa
E0 = 20321 MPa
eps0 = 0.00209
nu = 0.18
kappa = E0 eps0 / fc = 2.0005129533678754
```

R08 tensile reference work over

\[
0\le\lambda\le10x_{cr}=0.49987179453974245
\]

is

\[
E_{t,R08}=0.029742371775134682.
\]

For the simple monotone saturation potential

\[
\phi_t(\lambda)=u_\infty\lambda-
\frac{u_\infty^2}{\kappa}
\ln\left(1+\frac{\kappa\lambda}{u_\infty}\right),
\]

preserving the R08 material tensile work gives

\[
u_\infty=0.07422110763929314.
\]

This is a material-energy result only; it is not selected from Case21/Swartz Pu and is not yet a final full NC multiaxial production operator.

---

## 3. R09C structural global-potential fit remains STOPPED

The proposal to generate numerical whole-structure energy data and then fit a global `U(D,q)` was stopped because coefficient identification would contain hidden offline spatial numerical quadrature.

```text
R09C_ENERGY_POTENTIAL_STRUCTURAL_TARGET = STOP_NOT_EXECUTED
```

No structural global potential may be fitted from numerical spatial integration and then relabelled as zero-quadrature production theory.

---

## 4. Latest executed gate: NC ENERGY POTENTIAL + D15 FEASIBILITY

Canonical files:

- `governance/NC_ENERGY_POTENTIAL_D15_GATE_DECISION_20260810.md`
- `current/theory/NZ_SCCM_NC_ENERGY_POTENTIAL_D15_FEASIBILITY_GATE_20260810.md`
- `current/theory/NZ_SCCM_NC_ENERGY_POTENTIAL_D15_FEASIBILITY_GATE_results.json`
- `evidence/NZ_SCCM_NC_ENERGY_POTENTIAL_D15_GATE_metrics_20260810.csv`

### 4.1 D15 exact mathematical closure

For finite polynomial material potential `p_N(Eu)`:

\[
\Psi_N=f_c\varepsilon_0\operatorname{tr}[p_N(E_u)].
\]

For 2x2 `Eu`, Cayley-Hamilton gives

\[
E_u^2-J_1E_u+J_2I=0.
\]

Let

\[
s_n=\operatorname{tr}(E_u^n).
\]

Then

\[
s_0=2,\qquad s_1=J_1,\qquad
s_n=J_1s_{n-1}-J_2s_{n-2}.
\]

Hence every finite polynomial potential reduces to a finite polynomial in `J1,J2`; after inserting the frozen Nguyen second-order kinematics, every term becomes a finite trigonometric-thickness polynomial and is exactly D15-integrable.

```text
D15_POLYNOMIAL_EXACT_CLOSURE = PASS
FORMAL_SPATIAL_QUADRATURE = 0
```

### 4.2 Minimum anchor-exact global polynomial

A degree-7 stress polynomial was fixed only by material anchors / material tensile work. No free material coefficients were introduced.

It nevertheless developed catastrophic interior oscillation:

```text
minimum stress ≈ -12965.289 fc
at lambda ≈ -7.2363
```

Therefore:

```text
ANCHOR_EXACT_LOW_PARAMETER_GLOBAL_POLYNOMIAL = FAIL
```

### 4.3 Energy-first low-order global potential

A single global energy potential was tested at `N=8,10,12` only. Energy values were fitted at material level; origin/peak/residual/tensile-work conditions were imposed exactly.

At `N=12`:

```text
potential max abs error ≈ 0.231823
stress max abs error    ≈ 0.879333 fc
stress P95 abs error    ≈ 0.405728 fc
tangent max abs error   ≈ 9.918593
spurious compression in tension ≈ 0.810240 fc
```

Thus fitting the energy much better did NOT make its first/second derivatives mechanically acceptable.

No degree escalation beyond `N=12` was attempted.

```text
ENERGY_FIRST_LOW_ORDER_GLOBAL_POTENTIAL_N8_N10_N12 = FAIL
```

### 4.4 Overall gate

```text
NC_ENERGY_POTENTIAL_AND_D15_FEASIBILITY_GATE
= FAIL__STOP_AT_GATE
```

Interpretation:

```text
ENERGY_POTENTIAL_PHILOSOPHY = RETAINED
D15_FINITE_POLYNOMIAL_CLOSURE = PASS
CURRENT_LOW_ORDER_GLOBAL_POLYNOMIAL_GRAMMAR = REJECTED
```

No Case21 calculation and no Swartz24 calculation followed this failure.

---

## 5. Current formal prohibitions after the gate

The following may NOT be used to rescue this failed grammar without explicit user approval:

- simply raising global polynomial/Chebyshev degree;
- adding large banks of unconstrained coefficients;
- using Case21/Swartz Pu to tune the material potential;
- returning to TT/TC/CC runtime spatial classification;
- using numerical spatial integration to identify `U(D,q)`, `P(D,q)` or `Rq(D,q)`;
- hiding a numerical compiler behind an explicit runtime polynomial;
- finite-difference tangent/Jacobian.

---

## 6. What remains open

The project still needs a **different low-parameter material-potential grammar** that simultaneously satisfies:

1. few physically meaningful material parameters;
2. energy-based material simplification;
3. explicit stress and tangent from the same potential;
4. no runtime spatial material partition;
5. zero-spatial-quadrature closure proven BEFORE any structural calculation;
6. no high-degree/global coefficient inflation;
7. sufficient NC compression/tension/multiaxial behavior.

A non-polynomial compact potential may be considered only if its complete halfwave integral and required derivatives admit a genuine analytic closed form; otherwise it fails the zero-numerical gate.

UHPC remains later-stage: NC numerical parameters/domains must not be copied into UHPC, and the UHPC full multiaxial current-work potential remains OPEN.

---

## 7. Current recommended action

```text
CURRENT_RECOMMENDED_NEXT_TASK = NONE_AUTOMATIC
STATUS = WAIT_FOR_USER_REVIEW_AFTER_GATE_FAILURE
```

The failed global-polynomial energy grammar must not be automatically replaced by another route. The next material-potential grammar requires explicit user approval first.

---

## 8. Recovery read order

1. `current/CURRENT_STATE.md`
2. `governance/NC_ENERGY_POTENTIAL_D15_GATE_DECISION_20260810.md`
3. `current/theory/NZ_SCCM_NC_ENERGY_POTENTIAL_D15_FEASIBILITY_GATE_20260810.md`
4. `current/theory/NZ_SCCM_NC_ENERGY_POTENTIAL_D15_FEASIBILITY_GATE_results.json`
5. `governance/EXPLICIT_END_TO_END_CAPACITY_DOCTRINE_20260810.md`
6. energy-potential governance / R09B / R09C-stop records
7. R09A / R08 / R07R evidence
8. Case21 invariant exact-moment foundation
