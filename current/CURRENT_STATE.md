# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 23:38 +08:00  
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

Final capacity must come from explicit formulas and explicit derivatives of the same formulas. Numerical root finding of already-explicit finite equations is allowed.

Formal production still prohibits spatial Gauss/Simpson/adaptive quadrature, material-point grids, moving TT/TC/CC spatial cells, whole-structure surfaces fitted from spatial numerical integration, panel-load calibration, and finite-difference production derivatives.

---

## 1. Critical correction: global energy-potential gate revoked

Canonical correction:

- `governance/REVOCATION_WRONG_GLOBAL_ENERGY_POTENTIAL_GATE_20260810.md`

The recent test

```text
NC_ENERGY_POTENTIAL_AND_D15_FEASIBILITY_GATE = FAIL__STOP_AT_GATE
```

is **not a governing blocker**. It tested whether the complete scalar material response could be replaced by one low-order global energy polynomial. That was not the user's intended route.

Its numerical results remain historical evidence only.

```text
NC_GLOBAL_ENERGY_POTENTIAL_GATE = REVOKED_AS_WRONG_ROUTE_TEST
```

---

## 2. Correct material architecture restored

The current route is:

\[
\text{multidimensional/current material relation}
\rightarrow
(\lambda_+,\lambda_-)
\rightarrow
\text{1D scalar master material functions}
\rightarrow
\text{low-parameter multidimensional interaction/spectral return}.
\]

For the explicit NC operator this architecture is already visible through

\[
(\varepsilon_x,\varepsilon_y,\gamma_{xy})
\to \mathbf X
\to(\lambda_+,\lambda_-)
\to(c_\pm,t_\pm)
\to(C_\pm,T_\pm,U_\pm)
\to(s_+,s_-)
\to(\sigma_x,\sigma_y,\tau_{xy}).
\]

The hard material-approximation problem is therefore localized to one-dimensional scalar functions, especially the narrow cracking/peak boundary layer. It is **not** a reason to rebuild the whole 2D/4D material relation as one global potential.

---

## 3. Energy method has a narrow role

Energy is used only to smooth/regularize the sharp one-dimensional scalar feature.

For a selected scalar interval \([\lambda_a,\lambda_b]\), an admissible rule is

\[
\int_{\lambda_a}^{\lambda_b}u_{smooth}(\lambda)d\lambda
=\eta_E
\int_{\lambda_a}^{\lambda_b}u_{source}(\lambda)d\lambda,
\]

with additional physical anchors such as initial tangent, retained compression peak, monotonicity and derivative continuity.

This does **not** create a new global material potential and does **not** replace the existing multidimensional interaction architecture.

R09B's tensile-work observation remains useful material evidence, but it is only one possible scalar smoothing constraint.

---

## 4. Historical evidence supporting this route

### G19 localization

G19 already concluded that the remaining ordinary-concrete difficulty was the **one-dimensional cracking-axis boundary layer**, not the 2D interaction surface. It explicitly prohibited repairing that issue by increasing 2D interaction degree.

### Case21 zero-spatial analytic success

The zero-spatial analytic-series Case21 execution already demonstrated the end-to-end feasibility of

```text
explicit current material operator
 -> finite analytic scalar/structural series
 -> exact monomial/moment integration
 -> parameter-space root solve
```

with

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
```

and the reinforced Case21 central result approximately

\[
D_u\approx0.70538385,
\quad q_u\approx0.0021930282,
\]

\[
P_c\approx316.6423\ \mathrm{kN},
\quad P_s\approx25.6909\ \mathrm{kN},
\quad P_u\approx342.3332\ \mathrm{kN}.
\]

The unresolved tight remainder certificate did not invalidate the central analytic solution.

---

## 5. Correct forward chain

```text
STEP 1  keep the accepted/current multidimensional NC current architecture
STEP 2  recover its 1D scalar master branch(es)
STEP 3  locate only the sharp scalar peak/kink interval
STEP 4  smooth that interval by material-energy equivalence + physical derivative/shape anchors
STEP 5  reinsert the smoothed scalar function into the same multidimensional interaction/spectral map
STEP 6  audit the reconstructed 2D/4D material surface and tangent
STEP 7  substitute Nguyen continuous second-order strain field
STEP 8  use the proven zero-spatial analytic/D15 contraction to obtain P(D,q), Rq(D,q)
STEP 9  differentiate the same explicit representation to obtain P_D, P_q, Rq_D, Rq_q
STEP 10 solve Rq=0 and L=P_D Rq_q-P_q Rq_D=0
STEP 11 include analytic reinforcement before root solving and report Pu
```

No whole-structure target surface is fitted.

---

## 6. Current prohibitions specific to this correction

- do not replace the full multidimensional material law by one global energy polynomial;
- do not increase 2D interaction degree to repair a 1D scalar kink;
- do not introduce large banks of free material coefficients;
- do not fit the scalar smoothing to Case21/Swartz Pu;
- do not use spatial numerical integration to generate production P/R/U coefficients;
- do not restore runtime spatial material-state partitioning.

---

## 7. Current recommended next task

```text
CURRENT_RECOMMENDED_NEXT_TASK
= R10_1D_ENERGY_SMOOTHING_REINSERTION_CASE21
```

R10 must stop before Swartz24. It must first show:

1. exact identity of the one-dimensional scalar branch being modified;
2. exact interval/feature being smoothed;
3. original vs adopted scalar work;
4. smoothing formula and all physically meaningful inputs;
5. stress/derivative/monotonicity audit;
6. unchanged multidimensional interaction reconstruction;
7. reconstructed 3D surface + coordinate-plane projections;
8. zero-spatial analytic/D15 Case21 integration trace;
9. all explicit equilibrium/limit derivatives;
10. reinforced Case21 root and comparison only after the material target is frozen.

---

## 8. Recovery read order

1. `current/CURRENT_STATE.md`
2. `governance/REVOCATION_WRONG_GLOBAL_ENERGY_POTENTIAL_GATE_20260810.md`
3. G19 one-dimensional boundary-layer diagnosis
4. `NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`
5. `NZ_SCCM_CASE21_EXPLICIT_ALGEBRAIC_ZERO_SPATIAL_SERIES_RESULT.md`
6. R09A/R09B scalar-smoothing evidence
7. revoked global-potential gate as historical negative evidence only
