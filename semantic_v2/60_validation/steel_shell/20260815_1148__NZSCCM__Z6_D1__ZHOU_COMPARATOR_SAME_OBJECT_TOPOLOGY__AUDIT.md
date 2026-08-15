# NZ-SCCM Z6-D1 — Zhou comparator same-object / topology audit

**Timestamp:** 2026-08-15 11:48 +08:00  
**Identity:** CURRENT Z6-D1 AUDIT / COMPARATOR-GOVERNANCE CORRECTION / NO PARENT-THEORY CHANGE

---

## 0. Question

The audit question is exact:

> Is the current numerical quantity labelled `Pu_Zhou_empirical` for Z0–Z6 a source-exact ultimate-capacity prediction for the **same reduced structural object** solved by NZ-SCCM — namely continuous concrete core + two outer faceplates with the internal multi-cell webs deleted as independent steel members?

Decision:

```text
SOURCE_EXACT_SAME_OBJECT_ZHOU_COMPARATOR = NO
CURRENT_ZHOU_Z0_Z6_NUMERIC_COMPARATOR = PROJECT_TRANSFERRED_REDUCED_EMPIRICAL_COMPARATOR
```

This does not invalidate Zhou's source theory. It corrects the identity of the project-created comparison quantity.

---

## 1. What is genuinely same-object

The reduced section-strength replay

\[
P_{yth}^{red}=f_yA_s^{red}+f'_cA_c^{red},\qquad f'_c=0.76f_{cu},
\]

with

\[
A_s^{red}=2bt_s,\qquad A_c^{red}=b(h-2t_s),
\]

is a legitimate algebraic replay of Zhou's section-strength expression on the project reduced object.

Therefore:

```text
PYTH_REDUCED_AS_REDUCED_SECTION_BASELINE = VALID
PYTH_REDUCED_AS_ORIGINAL_FULL_MCFSTW_STRENGTH = INVALID
```

The 2026-08-14 14:05 validation already stated this boundary explicitly.

Likewise the sandwich bending quantity

\[
D_{EI}^{red}=E_c\frac{(h-2t_s)^3}{12}+E_s\frac{h^3-(h-2t_s)^3}{12}
\]

is a defensible `E*I` degeneration for the concrete core + two outer faceplates. It is a project-reduced section quantity.

---

## 2. What is not source-exact same-object

Zhou's four-edge simply-supported elastic stability formula is retained in source form as

\[
N_{cr,m}=\pi^2\left[
\frac{D_xa^2}{m^2b^4}+\frac{2H}{b^2}+\frac{D_ym^2}{a^2}
\right],
\]

where the original MCFSTW `D_y`, `D_xy`, `D_mu` and `H` depend on the original multi-cell/web topology.

The earlier 14:05 source audit explicitly ruled that only two paths are valid:

1. original MCFSTW object + original Zhou stiffness constants;
2. reduced double-faceplate object + a consistently rederived reduced `D_x,D_y,H`.

It explicitly rejected mixing original multi-cell stiffness identity with the reduced object.

However the later Z0–Z6 batch did **not** complete route 2. Instead it introduced the isotropic diagnostic

\[
P_{cr}^{diag}(m)=bD_{EI}^{red}\frac{(\alpha^2+\beta^2)^2}{\beta^2},
\qquad \alpha=\pi/b,\quad\beta=m\pi/a,
\]

selected the minimizing integer `m`, then set

\[
\lambda_n^{diag}=\sqrt{P_{yth}^{red}/P_{cr}^{diag}}
\]

and inserted this diagnostic slenderness into Zhou Eqs. (5-87)–(5-88).

Therefore:

```text
Pcr_used_in_current_Z0_Z6_comparator = PROJECT_REDUCED_ISOTROPIC_DIAGNOSTIC
Pcr_used = NOT SOURCE_EXACT_REDUCED_EQ5_79_REDERIVATION
REDUCED_Dx_Dy_H = NOT YET CLOSED
```

The 21:41 reduced-reference report itself recorded that the source-exact reduced-object orthotropic `H` had not been rederived and substituted.

---

## 3. Empirical curve transfer is a second, independent identity gap

Even if a source-exact reduced `Pcr` were derived, one additional question would remain.

Zhou's empirical stable/ultimate resistance curve

\[
P_u=\phi_N(\lambda_n)P_{yth}
\]

was proposed/validated for the **original multi-cell concrete-filled steel tubular wall family**. The present NZ object deletes the internal web plates as independent steel-bearing/stiffness members and replaces the interior by one continuous concrete core.

No current source evidence establishes that the fitted/recommended mapping

\[
\lambda_n\mapsto\phi_N
\]

is invariant to that topology change.

Thus the current numerical operation

\[
\boxed{
P_{u,transferred}
=\phi_N\!\left(\sqrt{P_{yth}^{red}/P_{cr}^{diag}}ight)P_{yth}^{red}
}
\]

is a **transferred reduced empirical comparator**, not a Zhou source-exact prediction for the reduced object.

This is the main D1 correction.

---

## 4. Chronology check: the repository already contained the warning

The chronology is important:

### 2026-08-14 14:48 comparator correction

The correction file refused to release a numeric Zhou empirical `Pu` until:

```text
1. exact Zhou lambda_n identity is recovered;
2. Pcr/reference quantities are evaluated on exactly the same object;
3. phi_N is then evaluated;
4. final NZ Pu is compared with phi_N*Pyth.
```

### 2026-08-14 21:41 / 21:52 numerical batch

The later batch supplied a numeric comparator by using the project reduced isotropic `D_EI/Pcr` degeneration. This made a useful engineering comparison possible, but it did not close the previously stated source-exact reduced-object `D_x,D_y,H` requirement.

Therefore the later label `same reduced object on both sides` was too strong. Correct label:

```text
SAME_REDUCED_SECTION_STRENGTH_BASE = YES
SAME_SOURCE_EXACT_STABILITY_OBJECT = NO
EMPIRICAL_CURVE_TOPOLOGY_TRANSFER = UNVALIDATED
```

---

## 5. Z6 topology magnitude check

Z6 geometry is

```text
ns = 60
ls = 200 mm
b = 12000 mm = ns*ls
h = 130 mm
ts = 4 mm
tc = 122 mm
```

The exact equality `b=ns*ls` supports the geometric interpretation that the source object consists of 60 cells across the width. If 60 cells are separated by at least 59 internal partition webs, an **internal-web-only lower-bound accounting** is

\[
A_{web,int}^{LB}=(n_s-1)t_st_c
=59\times4\times122
=28792\ \mathrm{mm^2}.
\]

The two retained faceplates have

\[
A_s^{red}=2bt_s=96000\ \mathrm{mm^2}.
\]

Hence the omitted internal-web steel area is at least approximately

\[
\frac{28792}{96000}=29.99\%
\]

of the retained outer-faceplate steel area, before counting any boundary closing plates not represented by the `59` internal-web lower bound.

This is a geometric inference from the Table-5.1 `ns,ls,b,h,ts` identity, not a quoted source area table.

If one performs only a strength bookkeeping sensitivity — replacing this inferred web volume by concrete in the reduced object versus steel in the original object — the difference is

\[
\Delta P_{yth}^{web,LB}
=(f_y-f'_c)A_{web,int}^{LB}
=(355-30.4)\times28792
\approx9.3459\ \mathrm{MN}.
\]

The current reduced Z6 section baseline is

\[
P_{yth}^{red}=78.5856\ \mathrm{MN}.
\]

So the omitted-web strength bookkeeping alone is not tiny. More importantly, a strength replacement cannot reproduce the web contribution to orthotropic bending/shear/torsional stiffness and the discrete support of the outer plates.

No `+9.3459 MN` correction is applied to NZ-SCCM or to the comparator; this calculation is an identity/magnitude audit only.

---

## 6. Why Z6 is especially unsafe for transferred-comparator interpretation

The current transferred Z6 comparator uses

```text
Pyth_red = 78.5856 MN
Pcr_diag = 40.9128479451 MN
lambda_diag = 1.3859310694
phi_N = 0.5693206233
Pu_transferred = 44.7404027752 MN
```

Z6 is the only representative case deep in the `lambda>1` branch and is the most slender geometry in the batch. Consequently, errors in the reduced `Pcr` identity and any topology-dependence of `phi_N(lambda)` are magnified precisely where Z6 is being used as the main discrepancy diagnostic.

A simple **comparator sensitivity only** illustrates the scale without claiming a correction. Holding `Pyth_red` fixed while changing the diagnostic `Pcr` gives approximately:

|Pcr/Pcr_diag|lambda|transferred Pu MN|
|---:|---:|---:|
|0.8|1.5495|44.5415|
|0.9|1.4609|44.1798|
|1.0|1.3859|44.7404|
|1.1|1.3214|45.6343|
|1.2|1.2652|46.6895|
|1.3|1.2155|47.8323|
|1.5|1.1316|50.2490|
|2.0|0.9800|56.3406|

Because the empirical relation is piecewise/nonlinear, this is not a monotonic linear uncertainty band and must not be used as a fitted correction. It demonstrates only that a source-exact reduced stability operator matters materially.

---

## 7. Consequence for interpreting the Z0–Z6 errors

The previous statements

```text
Z0 error = ... vs Zhou
...
Z6 error = -23.4% vs Zhou
```

must now be read as

```text
error vs CURRENT TRANSFERRED REDUCED EMPIRICAL COMPARATOR
```

not

```text
error vs SOURCE-EXACT SAME-OBJECT ZHOU CAPACITY
```

Therefore Z6's `-23.4%`, or about `-16.2%` after the a/500 + local-yield sensitivity, cannot be assigned entirely to NZ-SCCM model error.

There are at least three distinct quantities:

1. NZ-SCCM reduced-object prediction;
2. Zhou original full-MCFSTW source prediction/FE database;
3. project-transferred reduced comparator constructed from reduced `Pyth`, reduced isotropic `Pcr`, and the original Zhou empirical curve.

They must not be collapsed into one identity.

---

## 8. D1 gate decision

```text
D1_PYTH_REDUCED_SAME_OBJECT_SECTION_REPLAY = PASS
D1_REDUCED_DEI_SANDWICH_BENDING_DEGENERATION = PASS_AS_DIAGNOSTIC
D1_SOURCE_EXACT_REDUCED_Dx_Dy_H = NOT COMPLETE
D1_SOURCE_EXACT_REDUCED_EQ5_79_Pcr = NOT COMPLETE
D1_PHI_N_TOPOLOGY_INVARIANCE_AFTER_WEB_DELETION = NOT DEMONSTRATED
D1_CURRENT_NUMERIC_ZHOU_COMPARATOR_SAME_OBJECT_CLAIM = FAIL / RELABEL REQUIRED
D1_CURRENT_NUMERIC_COMPARATOR_IDENTITY = TRANSFERRED_REDUCED_EMPIRICAL_COMPARATOR
D1_Z6_ERROR_AS_PURE_NZSCCM_MODEL_ERROR = PROHIBITED
```

No Zhou source formula is rejected; only the project transfer identity is corrected.

---

## 9. Required next action

There are two clean routes:

### Route D1-R — stay with the reduced NZ object

Re-derive for the reduced two-faceplate + continuous-core object the complete source-consistent

\[
D_x^{red},\quad D_y^{red},\quad D_{xy}^{red},\quad D_\mu^{red},\quad H^{red},
\]

then evaluate Zhou/Navier Eq. (5-79) on that exact reduced object. Only after this may a reduced `lambda_n` be called source-consistent. Even then, transferability of the empirical `phi_N` curve remains a separate validation question.

### Route D1-F — compare with Zhou original full object

Restore the internal web topology in the NZ structural object and compare against Zhou's original MCFSTW stiffness/capacity identity. This is a different structural model and must not be achieved by adding only a scalar web axial-force term.

Current priority recommendation:

```text
NEXT = D1-R_REDERIVE_REDUCED_Dx_Dy_H_AND_SOURCE_CONSISTENT_Pcr
```

because it preserves the current reduced NZ-SCCM object and isolates comparator error without reopening the parent concrete material theory.
