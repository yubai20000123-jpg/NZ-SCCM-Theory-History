# NZ-SCCM — local radial-cap full directional tangent + phase-assembly correction lock

**Timestamp:** 2026-08-17 22:04 +08:00  
**Status:** CURRENT IMPLEMENTATION CORRECTION / AUDIT GATE / NO NEW MATERIAL LAW  
**Parent governance:**
- `20260817_1442__NZSCCM__UNIFIED_END_TO_END_THEORY_CHAIN__CANONICAL_LOCK.md`
- `20260817_1824__NZSCCM__ZERO_SPATIAL_DISCRETIZATION_FINITE_CURRENT_TRUE_INFINITE_D15__CANONICAL_LOCK.md`
- `20260817_2020__NZSCCM__INCREMENTAL_AIRY_MEMBRANE_RESIDUAL_ZERO_DRIVER__CORRECTION_LOCK.md`

## 0. Purpose

This lock closes an implementation ambiguity exposed by the Z1/Z4 audit. It does **not** change the accepted steel source law, the Nguyen kinematics, Airy membrane coordinate, D15 integration, root topology, or the zero-spatial-discretization contract.

Two requirements are made explicit:

1. every phase contributes to the same residual/Jacobian before the coupled root is solved;
2. a **local** ideal-EP/radial-cap event may remove the tangent in its active loading direction, but may not be interpreted as setting the **entire steel phase** or the full plane-stress `3x3` tangent matrix to zero.

The earlier scalar wording `E_t,eff=0` at plastic loading is retained only as a loading-direction/effective-modulus statement. It is not authorization for `C_t^s = 0_{3x3}` over the whole shell.

---

## 1. Exact phase assembly invariant

At one common generalized state

\[
g=(D,q,\alpha),
\]

the total residual vector is assembled from the current concrete, two-face shell and web/PBL steel phases:

\[
\boxed{
\mathbf R^{tot}(g)
=\mathbf R^c(g)+\mathbf R^{face}(g)+\mathbf R^w(g)
}
\]

with, at minimum,

\[
\boxed{R_q^{tot}=R_q^c+R_q^{face}+R_q^w}
\]

and for the incremental Airy coordinate

\[
\boxed{R_A^{\Delta,tot}=R_A^{\Delta,c}+R_A^{\Delta,face}+R_A^{\Delta,w}}.
\]

Because every phase is evaluated at the same `g`, differentiation is linear:

\[
\boxed{
\mathbf J^{tot}
=\frac{\partial\mathbf R^{tot}}{\partial g}
=\mathbf J^c+\mathbf J^{face}+\mathbf J^w
}.
\]

This is a formal identity of the current theory, not an optional diagnostic.

A production execution report is not sufficient merely because it prints `Pc`, `Pface`, `Pw` and a total residual. It must be possible to persist the phase contributions to `Rq`, `RA^Delta` and the corresponding Jacobian blocks and demonstrate the above sums at the same state.

---

## 2. Local plane-stress radial cap

For the current local radial-projection diagnostic/current-map interpretation, use the plane-stress engineering stress vector

\[
\mathbf s^{tr}
=\begin{bmatrix}\sigma_x^{tr}&\sigma_y^{tr}&\tau_{xy}^{tr}\end{bmatrix}^T
=\mathbf C_e\mathbf e.
\]

Define

\[
\sigma_{vm}^{tr}=\sqrt{(\mathbf s^{tr})^T\mathbf H\mathbf s^{tr}},
\qquad
\mathbf H=
\begin{bmatrix}
1&-1/2&0\\
-1/2&1&0\\
0&0&3
\end{bmatrix}.
\]

The local radial projection is

\[
\lambda_{loc}=
\min\left(1,\frac{f_y}{\sigma_{vm}^{tr}}\right),
\qquad
\boxed{\mathbf s=\lambda_{loc}\mathbf s^{tr}}.
\]

`lambda_loc` is a **local continuous-field material function**. It is not a specimen-wide `alpha_g` based on `max_Omega sigma_vm`, and it is not a spatial cell label.

The 2026-08-15 progressive-yield preflight already established that a whole-shell multiplier triggered by the first local yield is only a reduced diagnostic and is not a physical progressive-yield operator. This correction remains in force.

---

## 3. Exact consistent tangent of the active local radial cap

For an active cap (`sigma_vm^tr > fy`),

\[
\lambda=\frac{f_y}{r},\qquad
r=\sqrt{(\mathbf s^{tr})^T\mathbf H\mathbf s^{tr}}.
\]

Since

\[
dr=\frac{(\mathbf H\mathbf s^{tr})^T d\mathbf s^{tr}}{r},
\]

and `d s^tr = C_e d e`, exact differentiation gives

\[
\boxed{
\mathbf C_t^{cap}
=\frac{\partial\mathbf s}{\partial\mathbf e}
=\lambda
\left[
\mathbf I
-\frac{\mathbf s^{tr}(\mathbf H\mathbf s^{tr})^T}{r^2}
\right]\mathbf C_e
}.
\]

For the elastic region,

\[
\boxed{\mathbf C_t^{cap}=\mathbf C_e}.
\]

This formula is the exact derivative of the stated radial-cap current map. It is not a secant approximation and it is not a scalar tangent substitution.

### 3.1 Consequence

On the active radial branch the loading/radial direction has zero incremental stress magnitude, but the full `3x3` tangent is generally rank two rather than rank zero:

\[
\boxed{
\mathbf C_t^{cap}\neq\mathbf 0_{3\times3}
\quad\text{in general.}
}
\]

Therefore

```text
FIRST_LOCAL_YIELD -> WHOLE_STEEL_PHASE_TANGENT_ZERO = PROHIBITED
ACTIVE_LOCAL_CAP -> FULL_3X3_TANGENT_ZERO = PROHIBITED
LOCAL_LOADING_DIRECTION_TANGENT_ZERO = CONSISTENT WITH IDEAL EP/RADIAL CAP
OTHER_DIRECTIONAL_TANGENT_COMPONENTS = RETAINED BY SAME CURRENT MAP
```

If a later source-frozen ideal-EP flow operator replaces the radial-projection diagnostic, its own exact consistent plane-stress tangent shall replace the boxed formula. The prohibition against a whole-phase zero tangent remains.

---

## 4. Continuous nonuniform yielding without spatial cells

Define the local trial yield function

\[
g_s(X,Y,z)=\sigma_{vm}^{tr}(X,Y,z)-f_y.
\]

The formal theory does **not** create elastic/plastic spatial cells. Instead:

```text
finite continuous Nguyen strain field
-> local finite steel current map / yield-cap function
-> true-infinite analytic representation of composed stress AND tangent
-> exact algebra / CH where applicable
-> General-D15 exact continuous-domain moments
-> converged target sum
```

The canonical 2026-08-17 zero-spatial lock already permits finite steel maps with yield/current caps to be represented analytically and contracted by D15. This lock only makes the same-source tangent requirement explicit.

Formal counters remain:

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
GAUSS = 0
SIMPSON = 0
ADAPTIVE_SPATIAL_QUADRATURE = 0
SPATIAL_MATERIAL_POINT_GRID = 0
SPATIAL_ELASTIC_PLASTIC_CELLS = 0
```

Material-coordinate coefficient generation/convergence is not structural spatial quadrature.

---

## 5. Required exact-D15 phase certificate

For Z1 and Z4, OFF and ON states, the next accepted execution must persist, before any new Pu interpretation:

\[
R_q^c,\ R_q^{face},\ R_q^w,
\]

\[
R_A^{\Delta,c},\ R_A^{\Delta,face},\ R_A^{\Delta,w},
\]

and every corresponding Jacobian entry with respect to the active generalized coordinates.

The machine-check identities are

\[
\Delta R_q=R_q^{tot}-(R_q^c+R_q^{face}+R_q^w),
\]

\[
\Delta R_A=R_A^{\Delta,tot}-(R_A^{\Delta,c}+R_A^{\Delta,face}+R_A^{\Delta,w}),
\]

\[
\Delta\mathbf J=\mathbf J^{tot}-(\mathbf J^c+\mathbf J^{face}+\mathbf J^w).
\]

The same execution must persist the steel-shell exact-moment targets

\[
K_{Z,s}^{mat},\quad R_{q,s},\quad R_{A,s}^{\Delta},\quad \mathbf J_s
\]

using the same local current stress and same-source consistent tangent.

No value may be reconstructed from a comparator or from a separate spatial quadrature solve.

---

## 6. Current result status until certificate passes

```text
MULTIPHASE_ASSEMBLY_THEORY_IDENTITY = PASS
LOCAL_PROGRESSIVE_YIELD_REQUIREMENT = PASS / PREVIOUSLY ESTABLISHED
LOCAL_RADIAL_CAP_ANALYTIC_TANGENT = CLOSED
WHOLE_PHASE_ZERO_TANGENT_INTERPRETATION = REJECTED
EXACT_D15_PHASEWISE_NUMERIC_CERTIFICATE_Z1_Z4 = PENDING
CURRENT_Z1_Z4_AIRY_Pu = DIAGNOSTIC / NOT YET PRODUCTION-CERTIFIED
COMPARATOR_TUNING = NO
```

This is an implementation-audit correction inside the existing unified theory, not a new branch.