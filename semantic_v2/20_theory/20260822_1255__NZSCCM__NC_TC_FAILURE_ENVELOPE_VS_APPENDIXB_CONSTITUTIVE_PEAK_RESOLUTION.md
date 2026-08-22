# NZ-SCCM — NC TC failure envelope vs Appendix-B constitutive peak role resolution

**Date:** 2026-08-22 12:55 +08:00  
**Status:** `SOURCE_ROLE_RESOLVED / NC_TC_CAPACITY_GATE_PASS_G6 / STRUCTURAL_PU_UNCHANGED`

## 0. Why this resolution is needed

The 12:05 addendum correctly noticed that Nguyen Appendix-B `stmoduc` computes, in the tension-compression route, both:

1. a major-direction peak `sig1p` derived from Nguyen Eqs. (3.18)-(3.19); and
2. an additional minor-compressive constitutive peak `sig2p` from the `3.28 / 0.5375` branch.

The unresolved question was whether both must be treated as simultaneous ultimate-capacity constraints in the stripped explicit 2D material gate.

A direct re-read of Nguyen Chapter 3 and the executable Appendix-B route resolves the roles.

## 1. Nguyen main-text source identity

Nguyen explicitly titles Eqs. (3.17)-(3.20) as the **Failure Envelope** and states that the biaxial strength envelope is used to determine the concrete stress field and material moduli before buckling. The four equations are described as the envelope equations for each quadrant.

For tension-compression, Eqs. (3.18)-(3.19) give the envelope coordinate `sigma_2p` as a function of

\[
\alpha=\frac{\sigma_1}{\sigma_2}.
\]

The next page defines `sigma_2p` as the peak stress in the minor principal direction.

Most importantly, Section 3.4.2 then states that **when the biaxial strength envelope is breached in the second or fourth quadrant, the concrete element changes state and cracks**. Thus Eqs. (3.18)-(3.19) are the source transition/failure boundary for TC.

## 2. Exact finite TC envelope reduction

Using positive physical magnitudes

\[
t\ge0,\qquad p\ge0,\qquad F=|f_c'|,\qquad T=f_t'>0,
\]

and Nguyen's signed compression convention `f_c'=-F`, Eqs. (3.18)-(3.19) reduce exactly to:

compression-axis segment:

\[
\boxed{
\frac{p}{F}+\frac{t}{3T}=1
}
\]

and tension-axis segment:

\[
\boxed{
\frac{p}{2F}+\frac{t}{T}=1.
}
\]

They meet at

\[
\boxed{
(p/F,t/T)=(0.8,0.6).
}
\]

The fixed-demand-ray capacity factor is therefore finite and direct:

\[
\lambda_A
=\frac{1}{p^d/F+t^d/(3T)},
\]

or

\[
\lambda_B
=\frac{1}{p^d/(2F)+t^d/T},
\]

with the finite source branch check.

No material point, load step, history field or numerical quadrature is introduced.

## 3. Appendix-B `stmoduc` role

In the executable uncracked `stmoduc` tension-compression route, the code first computes

\[
\texttt{sig1p}
=\alpha\times\sigma_{2p}^{\text{envelope}},
\]

using exactly Eqs. (3.18)-(3.19). This is the major-direction coordinate of the source failure-envelope point at the current stress ratio.

The same routine then computes a separate minor-direction peak used to construct the **equivalent-uniaxial constitutive response**:

\[
\texttt{sig2p}
=
\begin{cases}
\dfrac{1-3.28\alpha}{(1-\alpha)^2}f_c,&\alpha>-0.2,\\[2mm]
0.5375f_c,&\alpha\le-0.2.
\end{cases}
\]

It then computes the corresponding `eps2p`, calls the equivalent-uniaxial iteration, evaluates equivalent uniaxial strain, and obtains secant/tangent moduli. Therefore this branch is part of Nguyen's **constitutive peak/modulus construction after choosing the TC stress route**; it is not a second replacement definition of the main-text biaxial failure envelope.

After the TC envelope is breached and cracking occurs, Nguyen Section 3.4.2 separately introduces the modified compression-field softening in which the maximum compressive stress depends on the coexisting tensile strain. That post-breach relation remains a full constitutive/history oracle and is not imported as a material-point state machine.

## 4. Production role decision

For the current stripped explicit architecture:

- **capacity / admissibility boundary:** Nguyen Eqs. (3.18)-(3.19);
- **Appendix-B extra `sig2p` branch:** constitutive-oracle evidence for equivalent-uniaxial pre/post-transition stress-strain construction;
- **post-crack MCFT-type compression softening:** constitutive oracle, not a second runtime material solver.

Hence the complete finite TC capacity gate is now source-closed without inventing a `min()` combination of unrelated roles.

## 5. Corrected status

```text
NC_TC_FAILURE_ENVELOPE_EQ318_319 = PASS_G6
NC_TC_FAILURE_ENVELOPE_C0_JOIN = PASS
NC_TC_FAILURE_ENVELOPE_SOURCE_KINK = RETAINED
NC_TC_APPENDIXB_EXTRA_COMPRESSIVE_PEAK = CONSTITUTIVE_ORACLE_ONLY
NC_TC_POSTCRACK_COMPRESSION_SOFTENING = CONSTITUTIVE_ORACLE_ONLY
NC_TC_CAPACITY_GATE = PASS
NC_CT_CAPACITY_GATE = PASS_BY_PRINCIPAL_DIRECTION_EXCHANGE
NC_FULL_INCREMENTAL_NGUYEN = ORACLE_ONLY
```

This supersedes the temporary 12:05 status:

`NC_TC_COMPLETE_PEAK_PAIR_CAPACITY_INTERPRETATION = SOURCE_AUDIT_PENDING`.

## 6. Seven-gate implications

- `G3`: TC/CT source support = PASS.
- `G5`: capacity relation and branch derivatives are explicit; the source kink at the segment join is retained rather than hidden.
- `G6`: PASS, finite scalar algebra only.
- `G7`: PASS, no Swartz `Pf/Pu` used.

```text
STRUCTURAL_BACKBONE_CHANGED = FALSE
STRUCTURAL_PU_RERUN = NOT_AUTHORIZED
N_material_points = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
```
