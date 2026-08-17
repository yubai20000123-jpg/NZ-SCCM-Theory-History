# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-17 15:17 +08:00  
**Status:** TRUE INFINITE R10 SOURCE SEQUENCE + GENERAL-N CH + EXACT D15 J_n DERIVED / FULL INFINITE TARGET SUM NEXT

## Controlling governance

`semantic_v2/10_governance/20260817_1449__NZSCCM__TRUE_INFINITE_SERIES_TO_FINITE_INTEGRAL_SOLUTION__CANONICAL_CORRECTION_LOCK.md`

The governing theory remains one continuous chain:

```text
actual geometry / boundary
 -> complete representative halfwave
 -> frozen R10 or unified UHPC current target
 -> TRUE infinite analytic material sequence
 -> membrane-redistributed Nguyen field
 -> same-source directional tangent
 -> exact nth-term CH/D15 structural moments
 -> n->infinity target summation
 -> finite coupled equilibrium/limit system
 -> Pu
 -> case-specific post-solve comparison
```

## Formal counters

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

---

# Stage I — material infinite-sequence law: PASS

The frozen R10 positive/negative coordinate kernel has been reduced to

\[
t=\frac{\lambda^2}{2}(\lambda^2+\eta^2)^{-1/2}
+\frac{\lambda^3}{2}(\lambda^2+\eta^2)^{-1},
\]

\[
c=\frac{\lambda^2}{2}(\lambda^2+\eta^2)^{-1/2}
-\frac{\lambda^3}{2}(\lambda^2+\eta^2)^{-1}.
\]

For `lambda=c0+h*cos(theta)`, the universal square-root Chebyshev coefficients obey the true infinite five-term recurrence

\[
\frac{h^2}{4}(n-1)a_{n-2}
+h c_0(n-\tfrac12)a_{n-1}
+A_0na_n
+h c_0(n+\tfrac12)a_{n+1}
+\frac{h^2}{4}(n+1)a_{n+2}=0.
\]

For the current Z6 material guard `[-1.75,+1.45]`:

```text
c0=-.15
h=1.6
h^2/4=.64
h*c0=-.24
A0=1.30250624679527
```

The rational kernel has a corresponding finite-band recurrence.

Compression has the exact global source identity

\[
C=\kappa\sum_{m=1}^{\infty}(4-\kappa)^{m-1}s^m,
\qquad s=c/(1+c)^2,
\]

with uniform ratio bound

```text
(4-kappa)/4 = .499871761658031 < .5.
```

The global compression sequence also has a quadratic-field first-order ODE with cleared polynomial degrees `(17,16,14)`.

The frozen tensile source has exact cubic contact at both material knots, hence is `C2`; its low/mid quadratic-field ODE degree triples are

```text
T_low = (25,24,23)
T_mid = (25,24,24)
```

with knots

```text
lambda_1=.0500805176491376
theta_1=1.44541777411337
lambda_10=.499881166745393
theta_10=1.15253121911414.
```

The global Chebyshev coefficients of `T,U,T^7` obey the explicit physical-knot asymptotic law

\[
a_n=\frac{2}{\pi n^4}
[\Delta g'''_1\cos(n\theta_1)+\Delta g'''_{10}\cos(n\theta_{10})]
+O(n^{-5})+a_n^{analytic}.
\]

Thus

```text
value coefficient tail = O(n^-4)
first same-source tangent series = absolutely convergent
```

The nearby square-root complex branch point for Z6 has

```text
Bernstein rho_eta = 1.0015702405147586,
```

which analytically explains the historical broad finite-N48 difficulty without redefining the theory as a degree sweep.

Stage-I artifacts:

- `semantic_v2/20_theory/nc_rebar_panel/20260817_1456__NZSCCM__R10_TRUE_INFINITE_CHEBYSHEV_SEQUENCE_AND_D15_LIMIT__THEORY_STAGE1.md`
- `semantic_v2/40_execution/case21/20260817_1456__NZSCCM__R10_TRUE_INFINITE_SERIES_STAGE1__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/case21/20260817_1456__NZSCCM__R10_TRUE_INFINITE_SERIES_STAGE1__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/case21/20260817_1456__NZSCCM__R10_TRUE_INFINITE_SERIES_STAGE1__REPRO.py`

---

# Stage II — general-n matrix CH and exact D15 moment sequence: PASS

For

\[
\widehat E=(E-c_0I)/h,
\qquad
\tau=tr(\widehat E),
\qquad
\delta=det(\widehat E),
\]

2x2 Cayley-Hamilton gives

\[
\widehat E^2=\tau\widehat E-\delta I.
\]

Every nth matrix Chebyshev term reduces exactly to

\[
T_n(\widehat E)=p_nI+q_n\widehat E
\]

with

\[
p_0=1,q_0=0,p_1=0,q_1=1,
\]

\[
\boxed{p_{n+1}=-2\delta q_n-p_{n-1}},
\]

\[
\boxed{q_{n+1}=2p_n+2\tau q_n-q_{n-1}}.
\]

If

\[
p_n=\sum P_n[r,s]\tau^r\delta^s,
\quad
q_n=\sum Q_n[r,s]\tau^r\delta^s,
\]

the sparse invariant coefficient recurrence is

\[
P_{n+1}[r,s]=-2Q_n[r,s-1]-P_{n-1}[r,s],
\]

\[
Q_{n+1}[r,s]=2P_n[r,s]+2Q_n[r-1,s]-Q_{n-1}[r,s].
\]

For any required finite analytic structural weight `W`, define exact D15 invariant moments

\[
A_{rs}^{(W)}=D15[(W:I)\tau^r\delta^s],
\]

\[
B_{rs}^{(W)}=D15[(W:Ehat)\tau^r\delta^s].
\]

Then the exact nth target moment is

\[
\boxed{
J_n^{(W)}
=\sum P_nA_{rs}^{(W)}+\sum Q_nB_{rs}^{(W)}.
}
\]

This is the target-first general-D15 recurrence requested by the canonical theory.

The nth same-source directional tangent is also explicit from the same `p_n,q_n` functions:

\[
\begin{aligned}
dT_n[H]
={}&(p_{n,\tau}d\tau+p_{n,\delta}d\delta)I\\
&+(q_{n,\tau}d\tau+q_{n,\delta}d\delta)Ehat+q_nH,
\end{aligned}
\]

\[
d\tau=tr(H),
\qquad
d\delta=\tau tr(H)-tr(Ehat H).
\]

## Z6 complete-halfwave regression

At the current corrected Z6(a=24000) Airy checkpoint

```text
D=1.36180798
q=.026485404
lambda_Airy=.786915819
M=2.408685395361047
B=.7101062675531937
```

the complete 12000-mm halfwave was represented in exact Fourier-zeta coefficient algebra.

Direct matrix Chebyshev recurrence and the CH `p_n,q_n` recurrence agree coefficientwise to approximately `10^-15` for `n=2...8`.

Representative exact D15 moments

\[
J_n^{22}=\iiint[T_n(Ehat)]_{22}
\]

are

```text
n0  +19.739208802178716
n1   -7.173602554575800
n2  -10.247726468551589
n3   +9.354398819495076
n4   -1.222249829995828
n5   +0.842870566522749
n6   -1.086442907510144
n7   -3.528124457179138
n8   +4.734202130498469
```

These are basis moments only, not Pu values. They use zero spatial quadrature.

Stage-II artifacts:

- `semantic_v2/20_theory/nc_rebar_panel/20260817_1517__NZSCCM__TRUE_INFINITE_SERIES_CH_D15_TARGET_RECURRENCE__THEORY_STAGE2.md`
- `semantic_v2/40_execution/steel_shell/20260817_1517__NZSCCM__Z6_TRUE_INFINITE_CH_D15_NTH_TERM__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260817_1517__NZSCCM__Z6_TRUE_INFINITE_CH_D15_NTH_TERM__REPRO.py`

---

# Infinite target sum status

The formal target is now explicitly

\[
\boxed{
J_\infty^{(W)}=\sum_{n=0}^{\infty}a_nJ_n^{(W)}.
}
\]

Stage I supplies the source `a_n` sequence and convergence law; Stage II supplies the exact structural `J_n` sequence.

The leading physical-knot `n^-4` tail has the closed tail function

\[
\sum_{n=N+1}^{\infty}\frac{e^{in\theta}}{n^4}
=e^{i(N+1)\theta}\Phi(e^{i\theta},4,N+1),
\]

with `Phi` the Lerch transcendent. The smooth analytic-kernel component is controlled by its Stage-I recurrence/singularity law.

What remains is implementation connection, not a new theoretical route:

```text
full R10 U,C,T,T7 coefficient stream
 -> physical P,Rq,RA and tangent W-target streams
 -> source-derived n->infinity summation
 -> finite target functions
 -> coupled solve.
```

## Current Z6 and Case21 identities remain locked

Z6:

```text
a=24000 mm
b=12000 mm
m*=2
ell=12000 mm
q0=.004
```

After final Pu solve compare only with Zhou empirical formula and Winter.

Case21:

After final Pu solve compare only with

\[
P_{f,exp}=368.312750\ \mathrm{kN}.
\]

Existing finite-order/raw-source capacities remain regression checkpoints, not definitions of the true-infinite result.

## Current next executable task

```text
CONNECT_FULL_R10_INFINITE_COEFFICIENT_STREAMS
 -> PHYSICAL TARGET-FIRST CH/D15 J_n STREAMS
 -> N_TO_INFINITY SUMMATION
 -> FINITE P,Rq,RA,FULL_DIRECTIONAL_TANGENT
 -> Z6(a=24000) COUPLED Pu
 -> Zhou/Winter comparison
 -> Case21 same-chain Pu
 -> Pf comparison
```
