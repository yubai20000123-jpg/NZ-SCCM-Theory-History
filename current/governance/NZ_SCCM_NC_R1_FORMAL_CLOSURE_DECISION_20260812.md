# GOVERNANCE DECISION — NZ-SCCM NC-R1 FORMAL CLOSURE

**Date:** 2026-08-12  
**Identity:** FORMAL-CLOSURE DECISION; NO NEW THEORY NUMBER

## 1. Audit purpose and central conclusion

The independent theory audit achieved its intended purpose. It did **not** overturn the central analytic architecture:

\[
\boxed{
\text{continuous complete halfwave}
\rightarrow
\text{finite material compiler}
\rightarrow
\text{finite tensor/trigonometric algebra}
\rightarrow
\text{D15 exact moments}
\rightarrow
P(D,q),R_q(D,q),L(D,q)
\rightarrow
\text{low-dimensional limit root}
}
\]

The audit did identify formal gaps in the written derivation. The governing corrected derivation is now:

- `current/theory/NZ_SCCM_NC_R1_FORMAL_CLOSURE_ZHOU_STYLE_CANONICAL_20260812.md`
- `current/theory/NZ_SCCM_NC_R1_FORMAL_CLOSURE_CANONICAL_ERRATA_20260812.md` — editorial-symbol correction only

No Case21 or Swartz24 result is used to define the repairs.

## 2. Frozen invariants

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
STRUCTURAL_CALIBRATION = NO
PANEL_LEVEL_SURROGATE = NO
```

No R10 reopening, no N96/N112 escalation, no spatial Gauss/Simpson/adaptive quadrature, no spatial material-point grid/cells, no new material mechanism and no new Pu solver are authorized.

## 3. Formal repairs accepted

### 3.1 D15 basis repair

The previous restricted statement that every intermediate tensor component belongs to a basis containing only functions of `sin X`, `sin Y` and `zeta` is superseded.

The governing exact-moment basis is restored to the historical general trigonometric form

\[
Q=\sum c_{prush}\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h,
\]

with exact moments

\[
J_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX,
\qquad
Z_h=\int_{-1}^{1}\zeta^h\,d\zeta.
\]

This repair changes no structural physics and keeps formal spatial quadrature equal to zero.

### 3.2 Rebar closure

The governing formal theory now contains executable continuous/smeared rebar formulas for both

\[
P_s(D,q),\qquad R_{q,s}(D,q),
\]

with the frozen source steel law and a supported-single-branch gate. Spatially mixed unsupported steel branches are not silently partitioned; they block instead.

### 3.3 Axial load identity

\(P_c\) is explicitly classified as the representative-halfwave **average axial load observable**

\[
P_c=-\ell^{-1}\int_{\Omega_h}\sigma_{yy}\,dV,
\]

not as an unconditional local-end-reaction identity. This clarification preserves the current reduced path definition.

### 3.4 T constrained-minimax unique coefficient identity

The primary constrained minimax problem remains unchanged. If its primary optimum is non-unique, the unique production coefficient vector is selected by a strict-convex secondary minimum-distance problem relative to the T-C1 reference in the existing positive-definite H metric.

This does not alter the minimax optimal error, material physics or N48 order.

### 3.5 Compiler fidelity reporting

For every new compiler interval the formal theory records full-hull value and scaled first-derivative errors. Existing frozen C1 anchor, near-zero T, O(1)-coefficient, CH/D15 compatibility and tangent-diagnostic gates remain the current engineering acceptance evidence. No new theorem-level remainder threshold is imposed.

### 3.6 Pi_eta wording

`Pi_eta` is classified as the project-defined smooth nonnegative one-sided material coordinate. It is not claimed to be a globally monotone softplus or an exact positive/negative decomposition.

### 3.7 a_cc provenance

\[
a_{cc}=0.1072329249362415
\]

is classified as a **project-frozen low-parameter biaxial-compression physical target**, selected so the equal-biaxial target meets the current conservative CC envelope while uniaxial axes remain unchanged. It is not claimed as a verbatim Nguyen/Foster constant and is not a panel-Pu calibration parameter.

### 3.8 NC-R1 rescaling convention

The prior coordinate-rescaling ambiguity is closed by explicitly distinguishing:

1. scalar level-set residual re-expression under `(D,q) -> (D',q')`; and
2. redefinition of an energy-conjugate residual under a new generalized coordinate.

Both conventions preserve the normalized limit residual when used consistently.

### 3.9 Root-repeatability metric

The normalized root-distance formula explicitly requires `q0 > 0`, which is already the current positive-imperfection production contract.

### 3.10 Zhou current-tangent identity

The local expression `t^3 C_t/12` is no longer used without qualification for a nonuniform current tangent field.

The governing Zhou role is:

```text
ZHOU = DIRECTIONAL-STIFFNESS / NAVIER CURRENT-TANGENT AUDIT LANGUAGE
NOT = SECOND Pu SOLVER
```

For a nonuniform current tangent, the formal theory defines exact full-field modal second-variation quantities and mode-weighted `Dx*`, `Dy*`, `H*` projections, all evaluable by the same D15 exact moments. The old `t^3 C_t/12` form remains only as the uniform-tangent degeneration.

## 4. Non-iterative structural identity

After material coefficients are frozen, and within a globally supported rebar branch, the structural functions are finite in the two generalized coordinates:

\[
P(D,q)=\sum p_{ij}D^iq^j,
\qquad
R_q(D,q)=\sum r_{ij}D^iq^j,
\]

and

\[
L=P_D R_{q,q}-P_qR_{q,D}.
\]

Therefore the formal ultimate-load theory does not require load-step/material-point iteration. The joint roots can in principle be obtained by algebraic elimination/all-real-root isolation or any equivalent low-dimensional backend. A numerical backend may internally iterate, but this is not a formal structural loading/history requirement and introduces no spatial discretization.

## 5. Current status

```text
CORE_ZERO_SPATIAL_ANALYTIC_IDEA = PASS / RETAINED
R10_INTERNAL_TARGET = FROZEN
N48_C1 = GOVERNING
T_MM_UNIQUE_PRODUCTION_IDENTITY = CLOSED
CAYLEY_HAMILTON = GOVERNING
NGUYEN_KINEMATICS = GOVERNING
D15_GENERAL_EXACT_TRIG_MOMENTS = GOVERNING
PC_LOAD_OBSERVABLE_IDENTITY = CLOSED
REBAR_FORMAL_CLOSURE = CLOSED UNDER SUPPORTED SINGLE-BRANCH CONTRACT
NC_R1_ROOT_TOPOLOGY = GOVERNING
NC_R1_RESCALING_CONVENTION = CLOSED
ZHOU_FULL_FIELD_MODAL_AUDIT = CLOSED / DIAGNOSTIC
ZERO_FORMAL_SPATIAL_DISCRETIZATION = PASS
CASE21_NEW_CALCULATION = NOT PERFORMED
SWARTZ24_RECALCULATION = NOT PERFORMED
```

The formal closure is not named `NC-R1.1`, `NC-R2`, or another new theory number. It is a correction/closure of the NC-R1 written derivation.
