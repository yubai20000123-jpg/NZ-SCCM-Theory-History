# NZ-SCCM steel shell — Yun Lu local-wall replacement / zero-quadrature feasibility audit

**Timestamp:** 2026-08-13 18:54 +08:00  
**Identity:** SOURCE-GROUNDED FEASIBILITY AUDIT / NOT YET PRODUCTION FREEZE  
**Parent NC theory changed:** NO  
**Formal spatial quadrature:** ZERO TARGET  
**Structural calibration:** NO

---

## 0. Question

After proving that a bonded finite-thickness steel shell can enter the locked complete-halfwave/general-D15 architecture without numerical spatial integration, can the simple steel-shell local model be replaced by the analytical local-buckling/postbuckling model in Yun Lu's 2024 thesis?

Answer:

```text
ZERO-QUADRATURE ANALYTIC FEASIBILITY = YES
LOCAL SINGLE-SIDE-CONSTRAINED STEEL-WALL COMPATIBILITY = HIGH
LITERAL DROP-IN REPLACEMENT OF EVERY STEEL-SHELL EQUATION = NO
```

The reason for the last line is important: Yun Lu supplies a **local plate structural postbuckling model**, not a complete multiaxial steel material current law and not the global four-edge simply-supported Zhou/Navier parent model.

---

## 1. What Yun Lu actually derives

Yun Lu's thesis studies steel box concrete wall panels whose steel wall is restrained by concrete on one side and can buckle outward on the other side. The analytical theory is built from:

1. a boundary-compatible finite deflection shape;
2. Kármán large-deflection equations;
3. an analytical Airy/stress-function solution;
4. a Galerkin equation;
5. an analytical postbuckling strength/path relation including initial geometric imperfection and membrane effect.

The thesis explicitly states that the analytical route was developed because the single-side contact and nonlinear FE problem can be difficult to converge, and its aim is an analytical postbuckling solution.

For the final local-wall theory the investigated boundary is a four-edge clamped, single-side-constrained steel wall under uniform axial compression. This must be kept distinct from the global four-edge simply-supported Zhou/Navier benchmark.

---

## 2. Why Yun Lu is naturally compatible with zero numerical integration

The local deflection is a finite cosine form of the type

\[
w=A\left(1-\cos\frac{2m\pi x}{a}\right)
\left(1-\cos\frac{2\pi y}{b}\right),
\]

with the same finite form for initial imperfection using amplitude `A0`.

The analytical stress field obtained from the stress function is likewise a finite combination of cosine harmonics. The governing Galerkin equation is a finite double integral of products of those harmonics.

Therefore every spatial integral belongs to the same general family

\[
\int\!\int
\sin^p(\cdot)\cos^r(\cdot)
\sin^u(\cdot)\cos^s(\cdot)
\,dx\,dy,
\]

which is exactly compatible with the existing `general-D15` trigonometric moment engine after coordinate normalization.

Yun Lu subsequently reduces the Galerkin equation to closed analytical expressions, so the source theory itself already demonstrates that numerical quadrature is not fundamental to this local-wall model.

```text
YUN_LU_SPATIAL_GAUSS_REQUIRED = NO
YUN_LU_ADAPTIVE_QUADRATURE_REQUIRED = NO
YUN_LU_CELLS_REQUIRED = NO
YUN_LU_FINITE_TRIG_MOMENT_CLOSURE = YES
```

---

## 3. Main local postbuckling relation

In the project transcription verified against Yun Lu's source, the local axial load/path relation can be written as

\[
\boxed{
p_x(A,A_0)=
\left[
k_{crx}\frac{A}{A+A_0}
+k_p(1-\nu_s^2)\frac{2A_0A+A^2}{t_s^2}
\right]
\frac{\pi^2D_s}{B_s^2}
}
\]

with

\[
D_s=\frac{E_st_s^3}{12(1-\nu_s^2)}.
\]

The two terms have clear structural identities:

- `k_crx A/(A+A0)`: imperfection-sensitive buckling term;
- `k_p(1-nu_s^2)(2A0A+A^2)/t_s^2`: large-deflection membrane contribution.

The local average axial stress is

\[
\boxed{\sigma_{s,post}^{avg}=p_x/t_s}.
\]

This is already a closed algebraic function of local amplitude, local imperfection and design geometry once `k_crx,k_p` are generated from the source formulas.

---

## 4. Relation to the locked NZ-SCCM mother theory

The locked parent remains:

```text
one theoretical energy-minimum complete halfwave
Nguyen second-order D,q global kinematics
R10 / N48-C1-MM concrete current operator
general-D15 exact moments
direct Rq=0,L=0 first limit solve
Zhou/Navier global current-tangent stability check
```

Yun Lu therefore must **not** replace:

- R10 concrete;
- Nguyen global `D,q` kinematics;
- the theoretical global halfwave rule;
- global Zhou/Navier simply-supported stability;
- the direct whole-panel `Rq=0,L=0` limit logic.

The natural role is narrower:

\[
\boxed{
\text{Yun Lu} = \text{local steel-shell subpanel buckling/postbuckling operator}
}
\]

for a shell region whose design boundary is actually compatible with the single-side-constrained/clamped source model.

For PBL-separated steel-shell subpanels, this is particularly compatible with the already locked project interpretation that PBL acts primarily as a strong local boundary/subpanel divider rather than as an independent axial-load steel term.

---

## 5. The main coupling issue: local amplitude is not automatically the global q

A literal Yun Lu local plate has its own buckle amplitude `A_s` and initial imperfection `A_s0`.

The locked mother theory has a global/representative complete-halfwave coordinate

\[
q=A/b.
\]

These cannot be silently identified merely because both are called amplitudes.

The production extension must choose and prove one of two routes:

### Route Y-A — local internal variable

For each active local steel subpanel,

\[
A_s=A_s(D,q)
\]

is determined from a local analytical compatibility/Galerkin residual

\[
R_{A_s}(D,q,A_s)=0.
\]

Then its local shell work/stress contribution is inserted into the global `P,Rq,L` system. `A_s` is an analytically eliminated or directly coupled finite internal coordinate, not a spatial material point.

### Route Y-B — proven kinematic identification

If the particular shell geometry and global halfwave make the Yun Lu local shape exactly proportional to the global shell deflection over that subpanel, a deterministic geometric relation

\[
A_s=\omega_s A
\]

may be derived from shape compatibility.

This is acceptable only if derived from geometry/boundaries. It may not be selected from an experimental ultimate load.

Current verdict:

```text
YUN_LU_LOCAL_AMPLITUDE_COUPLING = OPEN BUT FINITE-DIMENSIONAL
ZERO-QUADRATURE CONSEQUENCE = NOT THREATENED
```

---

## 6. Steel plasticity boundary

Yun Lu explicitly states that the analytical theory does **not** include a steel plastic constitutive model, and identifies material plasticity as a needed future extension.

Therefore Yun Lu's analytical postbuckling equation alone cannot replace the complete steel current material operator all the way to arbitrary ultimate states.

A production steel-shell theory still needs a source-consistent transition when the shell stress enters inelasticity. Two source-consistent architectures remain possible:

1. Yun Lu elastic large-deflection local branch + independently frozen steel current material law for inelastic states;
2. re-derive the same local Galerkin operator with the approved finite analytic current tangent/material representation.

This is a material closure issue, not a spatial integration issue.

```text
YUN_LU_AS_STEEL_MATERIAL_LAW = NO
YUN_LU_ELASTIC_POSTBUCKLING_STRUCTURE = YES
STEEL_INELASTIC_COMPLETION = REQUIRED FOR GENERAL Pu
```

---

## 7. Source comparison with FE

Yun Lu's thesis performs Abaqus comparisons over aspect ratio, width-to-thickness ratio and initial imperfection. The source reports:

- theoretical and FE buckling-wave number/location are consistent across aspect-ratio changes;
- at relatively small width-to-thickness ratio, theoretical-vs-FE deflection amplitude error is within about 10%;
- larger width-to-thickness ratio can produce larger differences (reported up to about 19.6% in the discussed deflection comparison);
- the source also reports larger differences in some buckling/ultimate stress comparisons, especially in wider/slender ranges;
- material plasticity is not included in the analytical model.

These are validation limits of the source model and must remain visible. They do not justify importing the later experiment-fitted effective-width correction into NZ-SCCM.

---

## 8. Effective-width fitted correction is excluded

Yun Lu later derives an effective-width formula and applies an empirical correction from literature experimental data. That fitted correction is outside the present locked mother theory.

```text
YUN_LU_KARMAN_GALERKIN_ANALYTIC_MECHANICS = ADMISSIBLE
YUN_LU_SOURCE k_crx / k_p ANALYTIC TERMS = ADMISSIBLE SUBJECT TO BOUNDARY MATCH
YUN_LU_EXPERIMENT_FITTED_EFFECTIVE_WIDTH_CORRECTION = EXCLUDED
```

---

## 9. Replacement architecture after Gate 1

The preferred architecture is now:

```text
GLOBAL MOTHER THEORY
energy-minimum complete halfwave
-> Nguyen second-order D,q field
-> R10 concrete current operator
-> general-D15
-> global P,Rq,L
-> Zhou/Navier global KZ

LOCAL STEEL-SHELL MODULE
PBL/design boundaries define local steel subpanel
-> Yun Lu finite cosine local shape + initial imperfection
-> source k_crx and k_p / Galerkin closure
-> local A_s compatibility/internal residual
-> exact trig moments, zero spatial quadrature
-> local shell stress/work/tangent contribution
-> assembled back into global P,Rq,L,KZ
```

The shell remains a finite analytical component. No local Gauss mesh or shell material grid is created.

---

## 10. Gate verdict

```text
GATE_1_FINITE_THICKNESS_SHELL_ZERO_QUADRATURE = PASS
YUN_LU_ANALYTIC_ZERO_QUADRATURE = PASS
YUN_LU_AS_LOCAL_SINGLE_SIDE_SHELL_MODEL = HIGH_COMPATIBILITY
YUN_LU_AS_GLOBAL_ZHOU_SSSS_REPLACEMENT = NO
YUN_LU_AS_CONCRETE_MOTHER_THEORY_REPLACEMENT = NO
YUN_LU_AS_STEEL_MATERIAL_CONSTITUTIVE_LAW = NO
YUN_LU_LOCAL_AMPLITUDE_COUPLING = OPEN
STEEL_PLASTICITY_COMPLETION = OPEN
EXPERIMENTAL_EFFECTIVE_WIDTH_FIT = EXCLUDED
```

Thus the answer to the second question is also positive, with a precise boundary: **Yun Lu can replace/refine the local steel-shell buckling/postbuckling structural module while preserving zero numerical spatial integration; it does not replace the locked global mother theory or by itself close steel plasticity.**
