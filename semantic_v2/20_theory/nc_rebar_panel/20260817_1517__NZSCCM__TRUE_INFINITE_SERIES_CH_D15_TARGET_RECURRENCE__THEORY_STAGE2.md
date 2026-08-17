# NZ-SCCM — true-infinite R10 series: 2x2 CH term recurrence and target-first D15 moment recurrence, Stage II

**Timestamp:** 2026-08-17 15:17 +08:00  
**Status:** THEORY STAGE-II DERIVATION PASS / FULL INFINITE SUM Pu NOT YET RELEASED

## 0. Purpose

Stage I derived the genuine infinite R10 material coefficient architecture and its convergence law. Stage II now pushes the general `n`th material term through the matrix current map and the exact structural integration engine without introducing a finite final material degree.

The key question is:

> Given the infinite scalar material sequence `a_n`, can the `n`th matrix term and its exact D15 structural moment be generated recursively and audited without reconstructing a giant full stress-field tensor?

For the 2x2 current map the answer is yes.

Formal counters remain

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

---

# 1. Normalized matrix argument

For a geometry-certified material interval `[L,U]`, define

\[
c_0=(L+U)/2,
\qquad
h=(U-L)/2,
\]

and for the symmetric 2x2 normalized effective-strain matrix `E`,

\[
\boxed{
\widehat E=\frac{E-c_0I}{h}.
}
\]

The certified spectral condition is

\[
\operatorname{spec}(\widehat E)\subset[-1,1].
\]

Let

\[
\tau=\operatorname{tr}\widehat E,
\qquad
\delta=\det\widehat E.
\]

The exact 2x2 Cayley-Hamilton identity is

\[
\boxed{
\widehat E^2=\tau\widehat E-\delta I.
}
\]

---

# 2. Exact nth matrix Chebyshev term in a two-scalar CH basis

The scalar material series uses Chebyshev terms `T_n`. For the matrix argument,

\[
T_{n+1}(\widehat E)
=2\widehat E\,T_n(\widehat E)-T_{n-1}(\widehat E).
\]

Because every matrix polynomial of a 2x2 matrix reduces to the basis `{I,Ehat}`, write

\[
\boxed{
T_n(\widehat E)=p_n(\tau,\delta)I+q_n(\tau,\delta)\widehat E.
}
\]

Initial conditions are

\[
\boxed{
p_0=1,\ q_0=0,\qquad p_1=0,\ q_1=1.}
\]

Substituting Cayley-Hamilton gives the exact recurrence

\[
\boxed{
p_{n+1}=-2\delta q_n-p_{n-1},}
\]

\[
\boxed{
q_{n+1}=2p_n+2\tau q_n-q_{n-1}.}
\]

This recurrence contains no material fitting and no spatial operation. It is the exact matrix lift of the true infinite scalar basis.

---

# 3. Coefficient-array recurrence in invariant monomials

Expand

\[
p_n(\tau,\delta)=\sum_{r,s\ge0}P_n[r,s]\,\tau^r\delta^s,
\]

\[
q_n(\tau,\delta)=\sum_{r,s\ge0}Q_n[r,s]\,\tau^r\delta^s.
\]

Then the matrix recurrence becomes an integer sparse recurrence:

\[
\boxed{
P_{n+1}[r,s]
=-2Q_n[r,s-1]-P_{n-1}[r,s],
}
\]

\[
\boxed{
Q_{n+1}[r,s]
=2P_n[r,s]+2Q_n[r-1,s]-Q_{n-1}[r,s],
}
\]

where out-of-range indices are zero.

Thus the `n`th CH term can be streamed using only the previous two sparse coefficient ledgers. There is no need to store a pre-expanded material coefficient tensor for all orders.

---

# 4. Target-first D15 exact moment sequence

Let `W(X,Y,zeta)` denote any finite analytic structural weight needed by the generalized equations: axial-force selector, `q` virtual strain, membrane virtual strain, or a tangent/stability test direction.

Define two families of exact invariant moments:

\[
\mathcal A_{r,s}^{(W)}
=\mathscr D_{15}\left[(W:I)\tau^r\delta^s\right],
\]

\[
\mathcal B_{r,s}^{(W)}
=\mathscr D_{15}\left[(W:\widehat E)\tau^r\delta^s\right].
\]

Because `tau`, `delta`, `W` and `Ehat` are finite trigonometric-thickness fields under Nguyen second-order kinematics plus admissible membrane redistribution, every individual `A_rs` and `B_rs` is a finite exact D15 moment.

The exact `n`th structural moment is then

\[
\boxed{
J_n^{(W)}
=\sum_{r,s}P_n[r,s]\mathcal A_{r,s}^{(W)}
+\sum_{r,s}Q_n[r,s]\mathcal B_{r,s}^{(W)}.
}
\]

This is the target-first form. The implementation may memoize only those invariant moments actually requested by the streamed `P_n,Q_n` recurrence.

The formal infinite material-to-structure contraction is

\[
\boxed{
J_\infty^{(W)}
=\sum_{n=0}^{\infty}a_nJ_n^{(W)}.
}
\]

The material sequence index remains an analytic-series index, not a structural degree of freedom.

---

# 5. Same-source directional tangent of the nth term

Let `H=dEhat` be an arbitrary admissible normalized strain perturbation. Since

\[
T_n=p_nI+q_n\widehat E,
\]

its exact Fréchet derivative is

\[
\boxed{
\begin{aligned}
dT_n[H]
={}&\left(p_{n,\tau}\,d\tau+p_{n,\delta}\,d\delta\right)I\\
&+\left(q_{n,\tau}\,d\tau+q_{n,\delta}\,d\delta\right)\widehat E
+q_nH,
\end{aligned}
}
\]

where

\[
\boxed{d\tau=\operatorname{tr}H}
\]

and, for 2x2 matrices,

\[
\boxed{
d\delta
=\operatorname{tr}(\operatorname{adj}\widehat E\,H)
=\tau\operatorname{tr}H-\operatorname{tr}(\widehat EH).
}
\]

Therefore the tangent of the infinite material identity is obtained from the same streamed `p_n,q_n` objects; no independent tangent approximation is needed.

An equivalent direct recurrence is

\[
L_0[H]=0,\qquad L_1[H]=H,
\]

\[
\boxed{
L_{n+1}[H]
=2\left(H T_n(\widehat E)+\widehat E L_n[H]\right)-L_{n-1}[H].
}
\]

This provides an independent implementation audit for the invariant-derivative formula.

---

# 6. Infinite target limit and tail structure

Stage I established for the physical C2 tensile joins

\[
a_n=O(n^{-4}),
\]

with an explicit leading oscillatory formula

\[
a_n
=\frac{2}{\pi n^4}
\left[
\Delta g'''_1\cos(n\theta_1)
+\Delta g'''_{10}\cos(n\theta_{10})
\right]
+O(n^{-5})+a_n^{analytic}.
\]

For a symmetric `Ehat` with spectrum in `[-1,1]`,

\[
\|T_n(\widehat E)\|_2\le1.
\]

Hence every finite structural target weight has a constant `C_W` with

\[
|J_n^{(W)}|\le C_W.
\]

Therefore

\[
\sum |a_nJ_n^{(W)}|<\infty.
\]

For first-tangent targets, the Chebyshev derivative bound gives the controlling sum

\[
\sum n^2|a_n|<\infty.
\]

The leading physical-knot coefficient tail itself has an exact special-function summation:

\[
\sum_{n=N+1}^{\infty}\frac{e^{in\theta}}{n^4}
=e^{i(N+1)\theta}\Phi\!\left(e^{i\theta},4,N+1\right),
\]

where `Phi` is the Lerch transcendent. Thus the leading `n^-4` material tail is not estimated by repeatedly trying higher polynomial degrees; it has an explicit mathematical tail function.

The remaining analytic-kernel component is controlled by the source singularity/recurrence law from Stage I. The production summation must combine the exact streamed finite terms with these source-derived tail laws or an equivalent stable recurrence-to-infinity evaluation.

---

# 7. Z6 complete-halfwave exact recurrence audit

A direct Stage-II audit was run at the current Z6(a=24000) constrained-Airy mechanics checkpoint

```text
D = 1.36180798
q = .026485404
lambda_Airy = .786915819
b = ell = 12000 mm
q0 = .004
```

using the one complete 12000-mm halfwave.

At this state

```text
M = 2.408685395361047
B = .7101062675531937
```

for the normalized concrete membrane/bending scales.

The complete finite trigonometric-thickness `Ehat` field was generated analytically in Fourier-zeta coefficient space. Two independent recurrences were then evaluated:

1. direct matrix recurrence `T_{n+1}=2 Ehat T_n-T_{n-1}`;
2. CH recurrence through `p_n,q_n` above.

For `n=2...8`, the maximum coefficientwise differences were

```text
n=2 : 1.11e-16
n=3 : 2.22e-16
n=4 : 5.00e-16
n=5 : 6.38e-16
n=6 : 1.92e-15
n=7 : 1.78e-15
n=8 : 2.72e-15
```

so the streamed CH recurrence reproduces the direct matrix polynomial to floating roundoff.

As a representative exact D15 target, define

\[
J_n^{22}=\int_0^\pi\int_0^\pi\int_{-1}^{1}
[T_n(\widehat E)]_{22}\,d\zeta\,dY\,dX.
\]

The exact Fourier-zeta/D15 moments were

```text
n=0 : +19.739208802178716
n=1 :  -7.173602554575800
n=2 : -10.247726468551589
n=3 :  +9.354398819495076
n=4 :  -1.222249829995828
n=5 :  +0.842870566522749
n=6 :  -1.086442907510144
n=7 :  -3.528124457179138
n=8 :  +4.734202130498469
```

These are dimensionless representative basis moments, not a stress or capacity prediction. No spatial quadrature was used; every Fourier mode and thickness power was integrated by its closed endpoint formula.

```text
CH_NTH_TERM_RECURRENCE = PASS
D15_NTH_TERM_EXACT_MOMENT_GENERATOR = PASS
```

---

# 8. What Stage II changes in the implementation architecture

The formal implementation should no longer construct

```text
large finite material polynomial
 -> fully expand giant stress tensor
 -> integrate afterward.
```

Instead it should stream

```text
material coefficient a_n
 + CH invariant term (p_n,q_n)
 -> only the required D15 target moments J_n
 -> accumulate exact target series
 -> close the n->infinity tail using the source convergence law.
```

This is the `moment-first` interpretation in its true infinite-series form.

---

# 9. Stage-II decision

```text
GENERAL_N_CH_RECURRENCE = PASS
SPARSE_INVARIANT_COEFFICIENT_RECURRENCE = PASS
TARGET_FIRST_D15_Jn_FORMULA = PASS
SAME_SOURCE_NTH_TANGENT_FORMULA = PASS
Z6_COMPLETE_HALFWAVE_CH_D15_REGRESSION = PASS
INFINITE_TARGET_SUM_RUNTIME = NEXT
NEW_Pu_RELEASE = NO
```

## Unique next executable task

```text
CONNECT_STAGE_I_MATERIAL_SEQUENCE_GENERATORS
 -> STAGE_II_CH_D15_Jn_STREAM
 -> SOURCE_DERIVED TAIL / RECURRENCE-TO-INFINITY SUMMATION
 -> FINITE P,Rq,RA AND FULL DIRECTIONAL-TANGENT TARGETS
 -> COUPLED Z6(a=24000) Pu SOLVE
 -> ZHOU/WINTER POST-SOLVE COMPARISON
 -> CASE21 SAME-CHAIN SOLVE
 -> Pf POST-SOLVE COMPARISON
```
