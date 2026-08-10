# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 23:58 +08:00  
**Purpose:** 唯一当前工作入口。

## 0. Highest-priority contract

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

Final production capacity must come from explicit formulas and explicit derivatives of the same formulas. Numerical root solving of already explicit finite equations is allowed.

Formal production prohibits spatial Gauss/Simpson/adaptive quadrature, material-point grids, moving spatial TT/TC/CC cells, whole-structure P/R/U surfaces fitted from spatial numerical integration, structural-load calibration of material parameters, and finite-difference production derivatives.

---

## 1. Current material architecture

The active route is NOT a global material-energy-potential fit.

The active route is

\[
\text{multidimensional/current NC operator}
\rightarrow
(\lambda_+,\lambda_-)
\rightarrow
\text{1D scalar master law}
\rightarrow
\text{same multiaxial interaction/spectral return}.
\]

Energy is used only to regularize the sharp one-dimensional tensile scalar feature.

The previous global-energy-potential gate remains revoked as the wrong route test.

Canonical correction:

- `governance/REVOCATION_WRONG_GLOBAL_ENERGY_POTENTIAL_GATE_20260810.md`

---

## 2. Latest executed stage: R10

Canonical files:

- `current/theory/NZ_SCCM_R10_1D_ENERGY_SMOOTHING_REINSERTION_CASE21_20260810.md`
- `current/theory/NZ_SCCM_R10_1D_ENERGY_SMOOTHING_REINSERTION_CASE21_results.json`
- `governance/R10_1D_ENERGY_SMOOTHING_DECISION_20260810.md`
- `evidence/NZ_SCCM_R10_ARTIFACT_HASHES_20260810.md`

R10 performs:

```text
source Foster 1D tensile scalar
→ C2 material-energy smoothing
→ SAME U/C/T + CC/TC/TT + spectral current map
→ same-execution Case21 audit
```

No multidimensional interaction refit is performed.

---

## 3. Frozen R10 one-dimensional energy smoothing

The current Foster scalar entering the NC operator is

\[
u_{t,src}(t)=\rho T_{Foster}(t),\qquad t=\Pi_\eta(\lambda).
\]

The retained interval is

\[
0\le t\le10x_{cr},
\qquad
x_{cr}=0.04998717945397425.
\]

Source material work:

\[
\boxed{W_{src}=0.031741235181249904}.
\]

Source peak:

\[
\max u_{t,src}=0.09867291206823792.
\]

R10 replaces only this 1D scalar by two C2 quintic pieces preserving:

- origin stress and tangent;
- zero origin curvature;
- a rounded stationary peak at \(t=x_{cr}\);
- residual \(0.03\) at \(10x_{cr}\);
- zero first/second derivatives at peak and residual onset;
- the full retained 1D scalar work exactly.

Energy equality

\[
\int_0^{10x_{cr}}u_{sm}(t)dt
=
\int_0^{10x_{cr}}u_{t,src}(t)dt
\]

fixes the peak uniquely:

\[
\boxed{h=0.09799750427197301}.
\]

Peak reduction is only

\[
0.6844916017\%.
\]

No Case21/Swartz capacity is used to determine \(h\).

---

## 4. Multiaxial reinsertion

Only

\[
T_i\to T_i^{R10}=u_{sm}(t_i)/\rho
\]

changes.

The same current master remains

\[
U_i=\kappa\lambda_i-C_i+\kappa c_i+\rho T_i-\kappa t_i,
\]

and the same multiaxial interaction remains

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_--\rho a_tT_+T_-^8,
\]

\[
s_-=U_--a_{cc}C_-^2C_++C_-T_+-\rho a_tT_-T_+^8.
\]

Then the same spectral return generates \(\sigma_x,\sigma_y,\tau_{xy}\).

```text
MULTIAXIAL_ARCHITECTURE_CHANGED = NO
FREE_MULTIDIMENSIONAL_FITTING = NO
```

---

## 5. R10 same-execution Case21 audit

Both the source Foster and energy-smoothed versions are recomputed in the same execution using the same structure and reinforcement evaluator.

Final audit uses one 48×48×28 full-halfwave Gauss evaluator for both D and q reclosure.

### Source Foster baseline

```text
D_u  = 0.7057271404732661
q_u  = 0.0021940477872221006
A_u  = 2.6767383004109626 mm
Pc   = 316.6306821397406 kN
Ps   = 25.7033473236443 kN
Pu   = 342.3340294633849 kN
R    = 1.4210854715202004e-12 kN mm
```

### Energy-smoothed R10 audit

```text
D_u  = 0.843270404668947
q_u  = 0.0017832151821667267
A_u  = 2.1755225222434067 mm
Pc   = 337.8632691214933 kN
Ps   = 30.860195005805895 kN
Pu   = 368.7234641272992 kN
R    = -1.924968273669947e-08 kN mm
```

Experiment, used only after material freeze:

\[
P_f=368.312750\ \mathrm{kN}.
\]

R10 audit error:

\[
\boxed{+0.1115123295\%}.
\]

Same-execution material-change consequence:

\[
\boxed{\Delta P_u=+26.389434664\ \mathrm{kN}}.
\]

This agreement is not a calibration basis and must not be used to modify the frozen R10 scalar.

---

## 6. Formal-production boundary

The R10 Case21 structural evaluator uses spatial Gauss integration **for audit only**.

Therefore:

```text
R10_1D_ENERGY_SMOOTHING     = PASS
MULTIAXIAL_REINSERTION      = PASS
CASE21_SAME_EXECUTION_AUDIT = PASS
STRUCTURAL_CALIBRATION      = NO
SWARTZ24                     = NOT_STARTED

FORMAL_ZERO_SPATIAL_QUADRATURE_PRODUCTION = HOLD
```

R10 does NOT promote the 368.723464 kN audit value to formal zero-spatial production yet.

---

## 7. Frozen next task

```text
CURRENT_RECOMMENDED_NEXT_TASK
= R10B_RECOMPILE_FROZEN_ENERGY_SMOOTH_SCALAR_IN_EXISTING_ZERO_SPATIAL_D15_BACKEND
```

R10B is a compiler/integration task only. It must make no material retuning.

Required chain:

```text
frozen R10 u_sm(t)
→ existing 1D material compiler
→ SAME multidimensional current map
→ Nguyen second-order continuous halfwave
→ nested-D15 / exact analytic moments
→ explicit P(D,q), Rq(D,q)
→ same-expression P_D, P_q, Rq_D, Rq_q
→ Rq=0 and L=0
→ reinforced Case21 Pu
```

R10B must stop before Swartz24.

---

## 8. Prohibitions after R10

- do not adjust \(h\) because R10 is close to the Case21 experiment;
- do not alter the R10 smoothing endpoints/energy rule to improve capacity;
- do not introduce free scalar coefficients;
- do not refit the multidimensional interaction;
- do not replace R10B by production Gauss integration;
- do not fit whole-structure P/R/U from spatial numerical data;
- do not start Swartz24 until R10B formal zero-spatial closure passes.

---

## 9. Recovery read order

1. `current/CURRENT_STATE.md`
2. `governance/R10_1D_ENERGY_SMOOTHING_DECISION_20260810.md`
3. `current/theory/NZ_SCCM_R10_1D_ENERGY_SMOOTHING_REINSERTION_CASE21_20260810.md`
4. `current/theory/NZ_SCCM_R10_1D_ENERGY_SMOOTHING_REINSERTION_CASE21_results.json`
5. `evidence/NZ_SCCM_R10_ARTIFACT_HASHES_20260810.md`
6. `governance/REVOCATION_WRONG_GLOBAL_ENERGY_POTENTIAL_GATE_20260810.md`
7. frozen explicit NC current operator + Case21 nested-D15 baseline
8. G19/G20 scalar-boundary-layer historical evidence
