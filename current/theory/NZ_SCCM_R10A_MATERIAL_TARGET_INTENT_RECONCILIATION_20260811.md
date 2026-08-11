# NZ-SCCM R10A — MATERIAL-TARGET INTENT RECONCILIATION

**Date:** 2026-08-11 15:53 +08:00  
**Identity:** CURRENT MATERIAL-TARGET GOVERNING RECONCILIATION.  
**Scope:** choose the formal 1D tensile material target on material/source/analytic grounds only. No Case21/Swartz structural load is used as a selection criterion.

---

## 0. Question to be decided

The preceding R10 audit established a mismatch between the stated design intent and the actually executed R10 target.

The two admissible identities were:

```text
A. retain the executed whole-retained-branch C2 energy reconstruction;

or

B. restore a genuinely local source-preserving regularization that changes only
   the minimum necessary 1D sharp-feature region and leaves the source Foster
   scalar unchanged elsewhere.
```

R10A decides this question before any further R10B coefficient reconstruction or publication.

---

# 1. Fixed source material object

The ordinary-concrete source operator remains the explicit Foster current operator already frozen in

`current/theory/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`.

Its tensile scalar is

\[
t=\Pi_\eta(\lambda),\qquad r=t/x_{cr},
\]

\[
T_{src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10),
\]

\[
u_{src}(t)=\rho T_{src}(t/x_{cr}).
\]

The multidimensional interaction

\[
U,\qquad CC,\qquad TC,\qquad TT,
\]

and the spectral return are not reopened in R10A.

---

# 2. What the executed R10 actually did

The executed R10 replaced the complete retained tensile interval

\[
0\le t\le10x_{cr}
\]

with two C2 quintic branches, preserving total source work and selected anchors.

That target is internally consistent, but the material-coordinate audit found approximately

```text
max |u_R10-u_source|                       ~= 0.01831
absolute redistributed work/source work   ~= 9.89 %
positive relocated work/source work       ~= 4.95 %
first-moment shift of tensile work        ~= -5.90 %
```

Therefore the executed R10 is a broad equivalent tensile-law reconstruction, not merely a local regularization of the sharp Foster transition.

This distinction is independent of the later Case21 structural result.

---

# 3. Selection criteria

R10A uses the following ordered criteria.

## 3.1 Source fidelity

If the analytic difficulty is localized in a narrow scalar transition, material physics outside that transition must remain source-defined unless a material-level source independently justifies changing it.

## 3.2 Minimum intervention

An analytic regularization should change no more of the source material law than is necessary to remove the identified sharp/high-curvature feature.

## 3.3 Material-only constraints

Any new patch constants must be derived from source material quantities, endpoint matching, continuity and local material-work constraints. They may not be selected from Case21/Swartz capacity.

## 3.4 Multiaxial invariance

The existing U/C/T + CC/TC/TT interaction and spectral reconstruction remain unchanged.

## 3.5 Analytic compatibility

The selected target must remain suitable for finite analytic compilation and exact complete-halfwave moment contraction. This requirement may determine the local regularization width/order, but it may not justify a broad material-law redesign when a local source-preserving construction is sufficient.

---

# 4. Option A assessment — whole retained branch reconstruction

Option A has a real advantage: it is algebraically simple and already demonstrated compatibility with the zero-spatial D15 backend after compilation.

However, it has three material-governance disadvantages.

1. It modifies the entire retained tensile branch rather than the localized transition that motivated the regularization.
2. Equal total work does not preserve the distribution of tensile stress/material work along the source coordinate; the audit measured non-negligible work redistribution and first-moment shift.
3. There is no separate material-level source currently in the repository that requires the whole Foster tensile branch to be replaced by the executed two-piece C2 curve.

Therefore Option A is a valid **executed equivalent-model reference**, but it is not the preferred formal material target when source preservation is the governing principle.

---

# 5. Option B assessment — local source-preserving regularization

Option B changes only source-defined neighborhoods of the sharp/high-curvature Foster transitions and imposes exact source identity elsewhere:

\[
\boxed{
 u_{B}(t)=u_{src}(t),\qquad t\notin\mathcal I_{reg}.
}
\]

For each local regularization interval

\[
I_k=[a_k,b_k]\subset\mathcal I_{reg},
\]

the patch must be determined from source quantities only.

The minimum formal matching contract is

\[
p_k(a_k)=u_{src}(a_k),\qquad
p_k'(a_k)=u_{src}'(a_k),\qquad
p_k''(a_k)=u_{src}''(a_k),
\]

\[
p_k(b_k)=u_{src}(b_k),\qquad
p_k'(b_k)=u_{src}'(b_k),\qquad
p_k''(b_k)=u_{src}''(b_k),
\]

plus **local** material-work preservation

\[
\boxed{
\int_{a_k}^{b_k}p_k(t)\,dt
=
\int_{a_k}^{b_k}u_{src}(t)\,dt.
}
\]

These are seven scalar constraints. Therefore a degree-6 polynomial is the minimum polynomial degree that can satisfy this complete C2 + local-work contract without a free fitting coefficient. Higher degree is permitted only if required by monotonicity/no-overshoot/analytic-quality gates; additional coefficients must remain uniquely constrained, not structurally calibrated.

The exact interval endpoints \(a_k,b_k\) are **not frozen in R10A**. They must be derived in the next material-only gate from the source transition scale/curvature and analytic-compiler requirement. They may not be chosen from Case21 Pu.

---

# 6. Decision matrix

| criterion | A: whole retained branch C2 rebuild | B: local source-preserving regularization |
|---|---|---|
| source identity outside sharp feature | FAIL | PASS by construction |
| minimum material intervention | FAIL | PASS |
| total/local material-work control | global total only | local exact work required |
| no structural calibration | PASS | PASS required |
| same CC/TC/TT interaction | PASS | PASS |
| immediate algebraic simplicity | PASS | lower, but manageable |
| risk of unintended tensile-law redistribution | higher | lower |
| consistency with stated project intent | lower | higher |

---

# 7. Governing R10A selection

\[
\boxed{
\text{R10A selects Option B: LOCAL SOURCE-PRESERVING REGULARIZATION.}
}
\]

The reason is not that Option B gives a preferable Case21 load; no structural capacity is used in the decision.

The reason is that Option B is the only option that simultaneously satisfies:

- the source-fidelity hierarchy;
- the original material-modification intent;
- minimum intervention;
- local material-work preservation;
- no new free material calibration;
- retention of the existing multidimensional interaction;
- compatibility in principle with the analytic compiler/D15 architecture.

---

# 8. Consequence for the already executed R10/R10B records

The prior whole-branch R10 and its R10B result are **not deleted** and are not re-labelled as numerical errors.

Their new identity is:

```text
R10_WHOLE_BRANCH_C2_TARGET
= EXECUTED_REFERENCE_BASELINE

R10B_ZERO_SPATIAL_RESULT_FOR_WHOLE_BRANCH_TARGET
= EXECUTED_REFERENCE_BASELINE
```

They remain important evidence that the zero-spatial analytic architecture can close a reinforced Case21 problem.

But they are no longer the final governing material target after R10A selects Option B.

Accordingly, the previously reported

\[
P_u=368.31955249587696\ \mathrm{kN}
\]

must be described as the R10-whole-branch/R10B executed-reference value, not as the final capacity of the not-yet-implemented R10A local-source-preserving target.

---

# 9. What is retained unchanged

R10A does **not** reopen or reject:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
m = 1
NGUYEN_SECOND_ORDER
same U/C/T + CC/TC/TT multidimensional architecture
same spectral return
Cayley-Hamilton coefficient algebra
D15 exact complete-halfwave moments
same-expression derivatives
reinforcement embedded before root solving
zero formal spatial sampling/quadrature/subdomains=1
```

The change is strictly the identity of the 1D tensile material target that must be compiled next.

---

# 10. Mandatory next gate

The next task is

```text
R10A1_LOCAL_SOURCE_PRESERVING_PATCH_CONSTRUCTION_AND_MATERIAL_GATE
```

R10A1 must, without structural calibration:

1. identify the source-defined sharp/high-curvature transition neighborhood(s) from the Foster scalar itself;
2. derive deterministic interval endpoints from source/analytic quantities only;
3. construct the lowest-complexity local C2 + local-work-preserving patch;
4. prove exact identity with the Foster source outside the patch interval(s);
5. check monotonicity, no overshoot/rebound, derivative signs and curvature behavior;
6. quantify local maximum error and redistributed work, which should be confined to the patch by construction;
7. determine whether the resulting scalar is materially and analytically acceptable for finite R10B-style compilation;
8. stop before structural Case21 re-solution if the material gate fails.

Only after R10A1 passes may the frozen local material target be recompiled and the R10B coefficient-generation process be reconstructed or newly frozen transparently.
