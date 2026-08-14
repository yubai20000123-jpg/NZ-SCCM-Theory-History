# NZ-SCCM Z6 — local ideal-EP progressive-yield preflight audit

**Timestamp:** 2026-08-15 01:26 +08:00  
**Identity:** CURRENT Z6-C PREFLIGHT / SOURCE-CONSTRAINED / NO NEW Pu CLAIM  
**Parent root-cause audit:** `20260815_0126__NZSCCM__Z6__IMPERFECTION_COMPILER_AND_REDUCED_STEEL_ROOT_CAUSE__AUDIT.md`

---

## 0. Purpose

The first Z6 isolation pass narrowed the unexplained discrepancy from `10.479 MN` to `7.363 MN` under the source-equivalent `a/500` imperfection sensitivity and showed that compiler-width sensitivity is too small to be the dominant cause. This preflight now audits the remaining steel mechanism before any new production operator is introduced.

The question is specific:

> Does the current homogeneous whole-shell radial cap turn **first local yield** into an artificially global shell stiffness/resultant loss, whereas the source FE uses local ideal elastic-perfectly-plastic material and therefore permits progressive growth of the yielded zone?

---

## 1. Direct source correction: Zhou steel is ideal elastic-perfectly-plastic

Zhou's Chapter 2 §2.5.1 elastoplastic finite-element model explicitly adopts an **ideal elastic-perfectly-plastic steel constitutive model**. Figure 2.15(a) is labelled `理想弹塑性模型`, with the steel curve reaching `fy` at `ey` and then remaining on the plastic plateau.

Therefore:

```text
ZHOU_STEEL_STRAIN_HARDENING_AS_EXPLANATION = REJECTED
NZ_IDEAL_EP_VS_ZHOU_STEEL_LAW_FAMILY = CONSISTENT AT THIS LEVEL
```

The Z6 discrepancy must not be “fixed” by inserting Ramberg-Osgood or strain hardening merely because it raises Pu.

The source also establishes that the four-edge stability family is deeply sensitive to `a/h` and `b/h`; Zhou reports elastic critical ratios around `a/h=36`, `b/h=60` and elastoplastic critical ratios `a/h<20`, `b/h=40`. Z6 (`a/h=69.23`, `b/h=92.31`) lies well inside the stability-sensitive region.

---

## 2. Why the current whole-shell cap is not the same mechanism as local ideal EP

Current reduced Z0-Z6 continuation:

\[
\alpha_g(D,q)=\min\left(1,\frac{f_y}{\max_{\Omega_s}\sigma_{VM}^{E}(D,q)}\right),
\]

\[
\boldsymbol\sigma_s^{red}(X,Y,z)=\alpha_g\,\boldsymbol\sigma_s^E(X,Y,z).
\]

After the first material point reaches yield, the single scalar `alpha_g<1` acts on the **entire shell stress field**. The reduced stability-material branch simultaneously applies the authorized ideal-plastic effective tangent rule.

A continuum shell with local ideal EP instead has the material status

\[
\Omega_y(D,q)=\{(X,Y,z):\sigma_{VM}=f_y\},
\]

with the remainder

\[
\Omega_e=\Omega_s\setminus\Omega_y
\]

still elastic. Immediately after first yield, the yielded region begins locally and then grows; the entire shell does not instantaneously acquire one common radial scaling factor.

Consequently:

```text
SAME_UNIAXIAL_STEEL_LAW != SAME_STRUCTURAL_POSTYIELD_OPERATOR
```

The present reduced cap is a valid deliberately simplified mechanism diagnostic, but its first-yield cusp is not automatically a physical ultimate-state identity for a very slender global panel.

---

## 3. First-yield continuity argument

At the first yield event `Y_s`, current reduced continuation has

```text
alpha_g = 1 exactly at Y_s
alpha_g < 1 immediately after Y_s
```

but the derivative `d alpha_g/d(D,q)` is generated from the **maximum local elastic stress** and then multiplies the entire shell resultant. Thus a local constitutive event produces a global derivative change in `Ps` and `Rq,s`.

For a local continuum ideal-EP material, if first yield initiates at an isolated extremum or a zero-measure set, then as the load passes through first yield:

```text
measure(Omega_y) -> 0+
measure(Omega_e) -> measure(Omega_s)
```

so there is no physical reason for the whole shell's elastic contribution to disappear at finite measure at that instant. The global tangent/resultants evolve as the yielded region expands.

This is the central mechanism distinction exposed by Z6.

It also explains why the discrepancy is largest for Z6: its global deformation amplitude is the largest in the representative batch, and its very large `a/h` and `b/h` make post-yield redistribution and remaining elastic-region stiffness more consequential.

---

## 4. Magnitude check retained from the first Z6 audit

Under the source-equivalent imperfection sensitivity, the reduced yield-cusp state is approximately

```text
Pu = 37.37773 MN
Ps = 23.09148 MN
remaining gap to Zhou = 7.36268 MN
```

The two faceplates have total steel area

\[
A_s=96000\ \mathrm{mm^2},
\]

so the uniform axial ideal-yield force reference is

\[
A_sf_y=34.08\ \mathrm{MN}.
\]

The steel resultant reserve from first yield to that arithmetic upper reference is about `10.989 MN`; the remaining comparator gap is about `67%` of this reserve.

This is not an upper-bound proof and does not imply the panel can mobilize uniform yield before global instability. It only demonstrates that the unexplained load scale is compatible with progressive steel redistribution and is not orders of magnitude larger than the available steel-force reserve.

---

## 5. Source-consistent zero-spatial-quadrature diagnostic architecture

A next diagnostic must preserve the formal structural identity:

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

The elastic shell field is already a finite analytic function of `(D,q,X,Y,z)`. Therefore its local von-Mises invariant

\[
\sigma_{VM,E}^2(X,Y,z;D,q)
\]

is also a finite analytic field.

A **diagnostic** local ideal-EP projection may be defined pointwise as

\[
\alpha_{loc}=\min\left(1,\frac{f_y}{\sigma_{VM,E}}\right),
\qquad
\boldsymbol\sigma_s^{loc}=\alpha_{loc}\boldsymbol\sigma_s^E.
\]

This differs fundamentally from the current whole-shell `alpha_g`: `alpha_loc` varies continuously over the shell and allows the yielded zone to grow while the rest remains elastic.

To keep zero structural quadrature, `alpha_loc` must not be evaluated on a structural point grid. The compatible route is:

```text
finite analytic elastic invariant field
-> scalar material-coordinate ideal-EP projection compiler
-> finite analytic coefficient composition
-> general-D15 exact moments
-> Ps(D,q), Rq,s(D,q)
```

Material-coordinate nodes used only to construct/check the scalar compiler are allowed under existing governance; they are not structural-space collocation or quadrature.

This local radial projection remains a **mechanism diagnostic**, not yet a final flow-plasticity material operator.

---

## 6. Why the existing J2 deformation-theory candidate cannot simply solve ideal perfect plasticity

The existing candidate derivation

`20260813_1834__NZSCCM__STEEL_SHELL__J2_DEFORMATION_THEORY_SOURCE_CURVE_PLANE_STRESS__MATERIAL_OPERATOR_DERIVATION.md`

uses a path-independent source function

\[
\varepsilon^{uni}(\bar\sigma)=\frac{\bar\sigma}{E_s}+\psi(\bar\sigma),
\]

where plastic strain is represented as a single-valued function of equivalent stress.

That architecture works naturally for a monotonic Ramberg-Osgood/multilinear source with a one-to-one stress-strain relation over the represented range. A strictly ideal plastic plateau is different: after yield,

\[
\bar\sigma=f_y
\]

while plastic strain can continue to increase. Thus plastic strain is not a single-valued function of `bar sigma` on the plateau.

Therefore:

```text
PROMOTE_EXISTING_J2_DEFORMATION_THEORY_BY_INSERTING_IDEAL_EP_PLATEAU = NOT FORMALLY CLOSED
REPLACE_IDEAL_EP_WITH_HARDENING_FOR_CONVENIENCE = PROHIBITED
```

A source-consistent production ideal-EP operator needs an active/yield-front or equivalent monotonic internal-parameter treatment with a consistent current tangent, while still compiling to the finite analytic structural operator.

---

## 7. Z6-C gates before any new Pu can be accepted

```text
C1 ELASTIC_DEGENERATION
   local operator reproduces current exact elastic shell P,Rq before yield

C2 LOCAL_STRENGTH
   sigma_VM <= fy everywhere under projected ideal-EP diagnostic

C3 FIRST_YIELD_LOCALITY
   yielded-region measure tends to zero at first yield; no whole-shell finite-measure stiffness deletion

C4 MATERIAL_COMPILER_FIDELITY
   convergence/error of scalar local projection is reported independently of structural Pu

C5 EXACT_MOMENT_CLOSURE
   shell P,Rq are obtained from coefficient-space general-D15, no structural quadrature/cells

C6 CONNECTED_BRANCH
   solve Rq=0 from the origin and trace the same connected branch through first yield

C7 LIMIT_IDENTITY
   distinguish smooth Rq-L maximum, constitutive cusp, and KZ control; do not force an L=0 root across a non-smooth event

C8 SAME_BRANCH_KZ
   evaluate KZ using the corresponding local elastic/plastic tangent structure

C9 NO_COMPARATOR_TUNING
   Zhou load is opened only after theory state is frozen
```

---

## 8. Current Z6-C verdict

```text
ZHOU_STEEL_MODEL = IDEAL ELASTIC-PERFECTLY-PLASTIC / SOURCE CONFIRMED
STEEL_HARDENING_MISMATCH = REJECTED
CURRENT_GLOBAL_ALPHA_CAP = REDUCED DIAGNOSTIC ONLY
FIRST_LOCAL_YIELD_AS_AUTOMATIC_GLOBAL_Pu = NOT PHYSICALLY CERTIFIED
PROGRESSIVE_LOCAL_YIELD_REDISTRIBUTION = REQUIRED NEXT MECHANISM TEST
ZERO_STRUCTURAL_QUADRATURE = MUST REMAIN
NEW_LOCAL_PROGRESSIVE_YIELD_Pu = NOT YET COMPUTED / NO FABRICATION
```

The next executable calculation is therefore narrowly defined: implement and audit a **local, progressive, ideal-EP coefficient-space diagnostic** for the shell, then recompute Z6 only. Z1/Z3/Z4/Z5 remain frozen and are not rerun.
