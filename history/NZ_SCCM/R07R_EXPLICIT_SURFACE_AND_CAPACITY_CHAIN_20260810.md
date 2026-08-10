# R07R HISTORY — deliberate material under-use -> explicit global capacity chain

**Date:** 2026-08-10

## Why R07R was created

The user clarified that smoothing is only one data-processing method. A measured/source material peak or cusp need not be used at its full sharp value. The project may deliberately under-use local material capacity if the resulting model is transparent and mechanically controlled.

The only highest-priority requirement is that the final ultimate capacity be obtained from **explicit formulas and explicit derivatives of the same formulas**.

This clarification demoted the earlier exclusive focus on `GLOBAL_POLY64 vs MOBIUS24` kernel selection. R07R therefore returned to the simplest end-to-end experiment.

## Material candidates frozen before structural validation

Three low-parameter scalar candidates were defined before looking at Case21 experimental capacity:

```text
A_FC100_FT90 : fc peak retention 100%, ft peak retention 90%
B_FC97_FT90  : fc peak retention 97%,  ft peak retention 90%
C_FC95_FT80  : fc peak retention 95%,  ft peak retention 80%
```

Common formula:

\[
u(\lambda)=\lambda\frac{N_5(\lambda)}{D_6(\lambda)}
\]

with explicit quotient-rule derivative. The minimal current surface is `sigma = fc u(Eu)` with 2x2 matrix-function reconstruction and no runtime TT/TC/CC state classification.

This intentionally omits extra biaxial enhancement in the first pass. The purpose is to determine whether extra multiaxial complexity is actually needed after a simple explicit model is tested.

## Whole-structure explicit target experiment

For each frozen material candidate, a finite global target was identified:

\[
P(D,q)=\sum_{i,j=0}^{10}p_{ij}T_i(\xi_D)T_j(\xi_q),
\]

\[
R_q(D,q)=\sum_{i,j=0}^{10}r_{ij}T_i(\xi_D)T_j(\xi_q).
\]

All derivatives and

\[
L=P_{,D}R_{q,q}-P_{,q}R_{q,D}
\]

are analytic derivatives of those same arrays.

Important audit boundary: coefficient identification used high-accuracy full-halfwave numerical integration offline. Runtime evaluation is fully explicit, but this is not yet the older pure-D15 zero-quadrature coefficient derivation. This remains visible as a HOLD boundary.

## Executed concrete-only Case21 stationary roots

```text
A_FC100_FT90 : D*=0.914265, q*=0.0210447, A*=25.6745 mm, Pu=317.4186 kN
B_FC97_FT90  : D*=0.912204, q*=0.0211055, A*=25.7487 mm, Pu=309.8781 kN
C_FC95_FT80  : D*=0.886755, q*=0.0206359, A*=25.1758 mm, Pu=306.1928 kN
```

Independent evaluation of the underlying explicit material surface at the same roots gives approximately 317.84, 310.28 and 306.65 kN respectively.

These are **concrete-only diagnostics**, not final RC Case21 predictions. Reinforcement has not been appended after the fact and must enter the same `P,Rq,L` equations before a final RC root is solved.

Case21 experimental RC capacity, inspected only after all material candidates were frozen:

\[
P_f=368.312750\ \mathrm{kN}.
\]

Compared with historical G31 crack-free concrete-only baseline

\[
476.935634\ \mathrm{kN},
\]

deliberate under-use/smoothing alone lowers the concrete-only stationary prediction to roughly 306–318 kN. Thus surface simplification has a major mechanical consequence rather than being only a numerical smoothing operation.

## R07R status

```text
R07R = PASS_PROOF_OF_CONCEPT_EXPLICIT_END_TO_END_CHAIN
MATERIAL_PEAK_UNDERUSE = EXECUTED_BEFORE_STRUCTURAL_VALIDATION
CASE21_RESULTS = CONCRETE_ONLY_DIAGNOSTIC_NOT_FINAL_RC
STEEL = OPEN
EXTRA_MULTAXIAL_ENHANCEMENT = OMITTED_IN_MINIMAL_R07R
FORMAL_ZERO_QUADRATURE_PRODUCTION_STATUS = HOLD
```

## Next

```text
R08_EXPLICIT_REINFORCEMENT_AND_MINIMUM_MULTAXIAL_CORRECTION
```

Insert reinforcement into the same explicit equations first. Only after the RC result exists should a small source-grounded multiaxial correction be introduced, and only if the simplified scalar surface shows a specific deficiency.
