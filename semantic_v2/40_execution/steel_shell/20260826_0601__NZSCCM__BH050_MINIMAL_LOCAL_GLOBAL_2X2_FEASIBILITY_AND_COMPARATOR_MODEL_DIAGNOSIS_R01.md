# NZ-SCCM — BH050 minimal local-global 2×2 feasibility + comparator-model diagnosis R01

**Time:** 2026-08-26 06:01 +08:00  
**Scope:** theory audit only; no R02/R06/Airy modification; no FEM calibration.

## 1. Question

Check whether the already-frozen Marguerre–Airy global amplitude `q` and R02 local plate amplitude `U` can immediately form a genuinely coupled 2×2 local-global stability matrix capable of producing a new zero before the current material terminal state.

## 2. Existing residuals

The current global Airy branch is

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

so under a load-parameter residual

\[
R_q(P,q)=P-P(q),
\]

\[
\frac{\partial P}{\partial q}
=\frac{P_{cr}q_0}{(q+q_0)^2}+2C(q+q_0)>0\qquad(q\ge0).
\]

R02 uses a condensed-energy stationarity equation

\[
R_U(U;e_x,e_y)=B_3U^3+B_1U+B_0=0,
\]

where the source code shows `R_U=d Pi_R02/dU`. Therefore

\[
\frac{\partial R_U}{\partial U}=3B_3U^2+B_1
\]

is the local second-energy derivative on the selected amplitude branch.

Crucially, in the frozen architecture the Airy global equilibrium does **not** contain `U`; R02 is explicitly a local steel-face operator and `GLOBAL_AIRY_CHANGED=False`. Hence

\[
\frac{\partial R_q}{\partial U}=0.
\]

The naive `q-U` tangent is therefore triangular:

\[
\mathbf K_{qU}=\begin{bmatrix}
-\,P'(q)&0\\
\partial R_U/\partial q&\partial R_U/\partial U
\end{bmatrix},
\]

and

\[
\det\mathbf K_{qU}=-P'(q)\,\frac{\partial R_U}{\partial U}.
\]

Thus it cannot create a new local-global coupled zero. A zero can arise only from (a) `P'(q)=0`, analytically impossible for q>=0, or (b) the already-local R02 amplitude tangent becoming zero.

## 3. BH050 numerical checks

Frozen BH050:

```text
Pcr = 19.5818772367311 MN
C   = 10841.3718065234 MN
q0  = 0.0025
```

The Airy q values corresponding to key loads are:

```text
P = 8.83278 MN  -> q = 0.001991246691
P = 12.2198 MN  -> q = 0.003833709144
P = 13.35637635 MN -> q = 0.004772819646
```

and

```text
P'(q) at 8.83278 MN  = 2524.33 MN per unit q
P'(q) at 12.2198 MN  = 1357.66 MN per unit q
P'(q) at 13.35638 MN = 1083.22 MN per unit q
```

all strictly positive.

At the frozen BH050 final upper R02 face:

```text
B3 = 0.0193334947724247
B1 = +0.0795041275744123
U  = 0.169266885792264 mm
3 B3 U^2 + B1 = 0.0811659156110 > 0
```

At the active lower R06 projected local-yield state:

```text
B3 = 0.0193334947724247
B1 = -0.162483993492182
U  = 2.93984591447788 mm
3 B3 U^2 + B1 = 0.338796444364 > 0
```

At the lower full unprojected final strain:

```text
U = 4.99939554163993 mm
3 B3 U^2 + B1 = 0.969151590178 > 0
```

So no relevant local tangent zero is present at these states.

## 4. Consequence

The originally suggested `q-U` 2×2 gate is **not immediately available as a genuinely coupled stability gate** from the frozen equations. The data are sufficient to close the algebra, but that closure proves the matrix is triangular and contains no new local-global feedback.

A genuinely coupled gate would require a new term by which local plate amplitude/energy affects the global equilibrium, e.g. a consistent total-potential or analytically condensed global residual containing R02 local-mode energy. That coupling is **not currently present** in the frozen Airy architecture and should not be invented as a hidden coefficient.

Therefore:

```text
NAIVE_Q_U_2X2 = CLOSED_BUT_DEGENERATE_AS_LOCAL_GLOBAL_GATE
NEW_ZERO_FROM_CURRENT_2X2 = NO_EVIDENCE
MISSING_ITEM = GLOBAL_RESIDUAL_DEPENDENCE_ON_LOCAL_AMPLITUDE_U
```

This is not a numerical-data shortage.

## 5. BH050 comparator-model hypothesis

The alternative hypothesis that the existing BH050 Abaqus comparator itself is not equal-contract is technically credible and predates R06.

Existing repository audit already states:

```text
BH050_EQUAL_CONTRACT_COMPARISON = NO
```

and records that BH050 uses a different diagnostic model family. The audited historical R02 comparison already had approximately the same anomaly (`13.5946 MN theory` versus `12.2198 MN Abaqus`) before the current R06 repair, while BH005–BH032/T120/T360 were much closer.

Known model-contract differences include imperfection construction, side-boundary treatment, mass scaling, local boundary/contact identity, and a special BH050 diagnostic model path. Therefore the 12.2198 MN peak must not be treated as an equal-contract proof that the analytical severe-local-buckling theory is wrong.

## 6. Recommended decisive sequence

1. Do **not** search numerically for a zero of the naive triangular `q-U` matrix; the structural reason for absence is already identified.
2. Do **not** modify R06 or UHPC.
3. Before creating a new local-global energy coupling theory, perform one equal-contract BH050 FEM rerun using the same canonical model family/imperfection/boundary/contact policy as BH032, changing only BH050 geometry.
4. If equal-contract BH050 remains near 12.22 MN, then the missing local-to-global feedback becomes a strong theory-development target.
5. If equal-contract BH050 rises materially toward the 13.3–13.6 MN analytical range, the prior BH050 special comparator model is the dominant source of the discrepancy.

No comparator value may be used to tune the theory in either branch.
