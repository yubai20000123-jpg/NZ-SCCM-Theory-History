# NZ-SCCM governance — Case21 Airy-scalar mechanics qualification and load identity

**Timestamp:** 2026-08-17 11:05 +08:00  
**Status:** CONTROLLING QUALIFICATION LOCK / FORMAL ZERO-SPATIAL NUMERIC RELEASE STILL OPEN

## 0. Why this lock exists

This lock follows the 2026-08-17 user-directed review of the last 5–10 days of project history. It corrects a repeatedly recurring data-identity error and qualifies the current one-coordinate Airy membrane closure before the formal zero-spatial evaluator is implemented.

It does **not** change R10, Case21 geometry/material input, reinforcement, the one-complete-halfwave domain, or the current direct-source mechanics target.

---

## 1. Case21 load identity is now hard-locked

For Case21, the experimental buckling load and experimental failure/ultimate load are different physical quantities and must never be interchanged:

```text
Pcr_exp = 75.6 kip = 336.285554 kN   # experimental buckling load
Pf_exp  = 82.8 kip = 368.312750 kN   # experimental failure/ultimate load
Nguyen_FE_buckling = 298 kN          # FE buckling comparator only
```

Therefore:

```text
CASE21_336kN_IDENTITY = EXPERIMENTAL_BUCKLING_LOAD_ONLY
CASE21_368.312750kN_IDENTITY = EXPERIMENTAL_FAILURE_ULTIMATE_LOAD
Pu_COMPARISON_TARGET = 368.312750 kN
Pcr_COMPARISON_TARGET = 336.285554 kN
Pcr_AND_Pu_CROSS_COMPARISON = PROHIBITED
```

The current Airy-scalar ultimate-load oracle `366.767829 kN` is correctly compared with `368.312750 kN`, not with `336 kN`.

---

## 2. Frozen backbone retained

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
R10 physical current operator = FROZEN
reinforcement before coupled solve = REQUIRED
General-D15 / target-first exact-moment philosophy = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Gauss/Simpson/adaptive/cells/material-point-grid as formal operator = PROHIBITED
high-order coefficient enumeration as production architecture = PROHIBITED
experimental calibration/root selection = PROHIBITED
Z6 analytical boundary = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```

Gauss-Legendre may be used only as an independent direct-source mechanics/audit oracle and never acquires formal production identity.

---

## 3. Active Case21 membrane closure retained

The five compatible functions remain the exact classical square-halfwave Airy/FvK span, but their nonlinear amplitudes are not released independently.

The active retained subspace is

\[
\boxed{r=\lambda M a(\nu)}
\]

with

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\]

\[
a(\nu)=\left[-\frac{1+\nu}{4},-\frac{1-\nu}{4},\frac14,-\frac{1-\nu}{4},\frac14\right]^T.
\]

For `nu=.18`,

```text
a = [-.295,-.205,+.25,-.205,+.25]
```

The five-free nonlinear `Rm=0` relaxation remains superseded because it can rotate far from the Airy direction and produce nonphysical over-relaxation.

---

## 4. Important benchmark wording correction

The statement `lambda=1 exactly in linear elasticity` must be scoped correctly.

### 4.1 Isotropic continuum benchmark

For a single isotropic plane-stress continuum on the retained complete halfwave, the scalar Airy equilibrium gives exactly

\[
\boxed{\lambda=1}
\]

and reproduces the classical Airy/FvK membrane redistribution.

### 4.2 Actual reinforced Case21 scalar subspace

When the two orthogonal reinforcement phases are included **before** the coupled solve, the composite in-plane operator is no longer the same single isotropic continuum. In the retained one-dimensional Airy subspace, even a fully linear elastic RC material does not generally require `lambda=1`.

For equal directional reinforcement ratio `rho_s`, the exact linear scalar equilibrium has the form

\[
\boxed{\lambda_{lin,RC}=A_{RC}+B_{RC}\frac{D}{M}}
\]

with the current Case21 parameters

```text
A_RC = 0.999266844854884
B_RC = 0.0096124785693025
```

Thus `lambda != 1` for the reinforced composite is not by itself a failure. The exact benchmark is:

```text
PURE_ISOTROPIC_CONTINUUM_LIMIT -> lambda = 1 exactly
ACTUAL_RC_SCALAR_SUBSPACE -> lambda determined variationally with reinforcement included
rho_s*Es -> 0 -> lambda -> 1
```

This correction prevents the continuum Airy benchmark from being misapplied to the reinforced composite.

---

## 5. Variational / virtual-work qualification of the scalar coordinate

Let `Rm` be the five generalized membrane residuals of the existing compatible basis and let `Rq_base` denote the existing Nguyen `q` residual evaluated at fixed `r`.

Under

\[
r=\lambda M(q)a,
\]

the generalized virtual-work residuals in the restricted coordinates are exactly

\[
\boxed{R_\lambda=M\,a^TR_m=M R_A}
\]

and

\[
\boxed{R_q^{restricted}=R_q^{base}+\lambda M_q R_A.}
\]

Therefore, for every active state with `M>0`,

\[
R_A=0,\qquad R_q^{base}=0
\]

is exactly equivalent to the restricted-coordinate equilibrium

\[
R_\lambda=0,\qquad R_q^{restricted}=0.
\]

At equilibrium the two residual pairs differ only by the nonsingular row transformation

\[
\begin{bmatrix}R_q^{restricted}\\R_\lambda\end{bmatrix}
=
\begin{bmatrix}1&\lambda M_q\\0&M\end{bmatrix}
\begin{bmatrix}R_q^{base}\\R_A\end{bmatrix}.
\]

Hence the connected equilibrium manifold and the bordered ultimate-point determinant are unchanged by using `(Rq_base,RA)` as the solver residual pair.

At `M=0`, `lambda` is an inactive coordinate because `r=0` for every finite `lambda`; this origin degeneracy is not an internal-instability event.

---

## 6. Internal scalar stability gate inherited from the 00:10 governance

The old five-coordinate stability requirement is projected consistently onto the retained scalar coordinate.

For `M>0`,

\[
\boxed{R_{A,\lambda}=M\,a^T K_{rr}a}
\]

and the actual conjugate scalar tangent is

\[
\boxed{K_{\lambda\lambda}=M R_{A,\lambda}=M^2a^TK_{rr}a.}
\]

The current branch is internally admissible only while

\[
\boxed{R_{A,\lambda}>0}
\]

(equivalently `K_lambda_lambda>0`).

If it reaches zero before the outer load maximum, that state is an `INTERNAL_MEMBRANE_STABILITY_EVENT`; changing to another `RA=0` root is prohibited.

The direct-source audit performed in the companion execution report finds this scalar stiffness positive from the active low-load branch through the present Case21 peak. This is a mechanics/audit qualification only; the final formal evaluator must reproduce the same sign and derivative from the same source-level tangent without formal spatial quadrature.

---

## 7. Small-driver qualification

The retained membrane displacement correction is proportional to the common driver `M`:

\[
r=\lambda M a.
\]

At the current Case21 mechanics peak,

```text
D = 0.7887924801
q = 0.0018083573
M = 0.02907033478
(M/4)/D = 0.00921356 = 0.921356 %
lambda = 0.0862359635
```

and the resulting load change relative to the same direct-R10 constrained `r=0` backbone is only

```text
Delta Pu = -1.96363 kN = -0.53254 %
```

which is consistent with Case21 being a small membrane-redistribution correction case.

No requirement is imposed that the correction must be positive relative to the over-constrained `r=0` model. The classical positive membrane postbuckling statement is relative to the elastic buckling branch, not to an artificially suppressed in-plane redistribution model.

---

## 8. Mechanics qualification decision

```text
CASE21_LOAD_IDENTITY = PASS / HARD-LOCKED
AIRY_SHAPE_ISOTROPIC_ELASTIC_DEGENERATION = PASS_EXACT
RC_LINEAR_SCALAR_BENCHMARK = PASS_EXACT_WITH_REINFORCEMENT_CORRECTION
SCALAR_VIRTUAL_WORK_TRANSFORMATION = PASS_EXACT
SCALAR_INTERNAL_STABILITY_TO_CURRENT_PEAK = PASS_DIRECT_SOURCE_AUDIT
CASE21_SMALL_M_SCALING = PASS
FIVE_FREE_NONLINEAR_MEMBRANE_RELAXATION = REMAINS_REJECTED
CURRENT_DIRECT_SOURCE_MECHANICS_TARGET_Pu = 366.767829 kN
CASE21_Pf_EXP = 368.312750 kN
CURRENT_MECHANICS_ERROR_VS_Pf = -0.419459 %
FORMAL_ZERO_SPATIAL_NUMERIC_RELEASE = OPEN
```

---

## 9. Unique next formal gate

No parallel route is authorized.

The next unique production task is

```text
CASE21_AIRY_SCALAR_FORMAL_T12_FIXED_ENDPOINT_DESCRIPTOR_GATE
```

using the already selected source-regular fixed-endpoint R10 factorised-period representation.

The formal evaluator must return the concrete value package required for `P,RA,Rq` and same-source derivatives with respect to `(D,q,lambda)`, while retaining the finite tangent thickness family through `k<=2` and without spatial numerical quadrature, spatial cells, material-point grids, or high-order coefficient enumeration.

No new `Pu` is released in this qualification lock.