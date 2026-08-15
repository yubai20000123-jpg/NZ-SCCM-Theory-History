# NZ-SCCM Z6 — zero-spatial higher-harmonic release diagnostic

**Timestamp:** 2026-08-15 16:47 +08:00  
**Status:** Q31 FIRST-VARIATION STATIONARITY FAILURE CONFIRMED / Q13 SECONDARY / FULL TWO-MODE Pu NOT YET RELEASED

## 1. Question

The preceding neighborhood sweep showed that the Z6 discrepancy is not an isolated numerical point and that Nguyen's small-slope second-order kinematics is not a plausible 20%-level error source. This execution therefore tests the next hypothesis without changing Nguyen, R10, N48, D15 or the steel material map:

> Is the accepted one-complete-halfwave / one-amplitude `q11` state actually stationary when a higher harmonic is allowed as an admissible continuous perturbation?

No structural sampling or quadrature is introduced.

## 2. Modal extension and exact algebra

Use the same continuous complete domain and write

\[
\frac{w}{b}=q_{11}\sin X\sin Y
+q_{31}\sin X\sin 3Y
+q_{13}\sin 3X\sin Y.
\]

Initial imperfection remains

\[
\frac{w_0}{b}=q_0\sin X\sin Y,
\qquad q_0=\frac{a}{500b}.
\]

The trigonometric identities

\[
\sin 3Y=3\sin Y-4\sin^3Y,
\qquad
\cos 3Y=\cos Y(1-4\sin^2Y)
\]

(and the corresponding `X` identities) make the first variations finite polynomial/trigonometric fields. Hence the existing coefficient-space exact moments remain available with zero structural points.

For the longitudinal third harmonic, evaluated at `q31=0`, define `x=sin X`, `y=sin Y`, `k=b/a`, and

\[
A_q=\frac{\pi^2}{\varepsilon_0}(q_0+q_{11}),
\qquad
B_q=\frac{\pi^2t}{2\varepsilon_0b}.
\]

The normalized strain derivatives include

\[
\varepsilon_{x,q31}
=A_q(1-x^2)y\sin3Y+B_q x\sin3Y\,\eta,
\]

\[
\varepsilon_{y,q31}
=3k^2A_qx^2(1-y^2)(1-4y^2)
+9k^2B_qx\sin3Y\,\eta.
\]

The shear work uses the exact polynomial product `gamma*gamma_,q31`; no square-root cosine field is sampled. The `q13` derivatives are obtained analogously by exchanging the third harmonic to the transverse coordinate, with the appropriate `k` scaling.

### Current material state is unchanged in the first-variation gate

At `q31=q13=0`, the concrete current stress is exactly the existing R10 -> N48 -> Cayley-Hamilton -> D15 single-mode stress field. Therefore the new generalized works are evaluated as

\[
R_{31}=\int_\Omega \boldsymbol\sigma(D,q_{11})^T
\boldsymbol\varepsilon_{,q31}\,dV,
\]

\[
R_{13}=\int_\Omega \boldsymbol\sigma(D,q_{11})^T
\boldsymbol\varepsilon_{,q13}\,dV.
\]

For the outer steel, the same local radial-cap factor `alpha_loc(r)` that generated the accepted current stress is retained; only the virtual-strain direction changes.

## 3. Implementation self-check: q11 equilibrium is recovered

The exact same machinery was first asked to recompute the current `q11` residual. This is a mandatory implementation check before interpreting any higher-harmonic residual.

At the three audited states:

```text
S0 Z6: |Rq11|/(P b) = 3.44e-7
S4:    |Rq11|/(P b) = 1.15e-6
S3:    |Rq11|/(P b) = 5.09e-6
```

Thus the evaluated states are the intended connected single-mode equilibria to engineering precision; the nonzero higher-harmonic results below are not caused by accidentally evaluating an off-branch `q11` point.

## 4. First-variation result: q31 is strongly nonzero and grows with slenderness

Define the dimensionless comparison indicator

\[
\eta_{31}=\frac{|R_{31}|}{Pb},
\qquad
\eta_{13}=\frac{|R_{13}|}{Pb}.
\]

The results are:

|case|Zhou lambda|P NZ (MN)|R31 (N mm)|eta31|R13 (N mm)|eta13|
|---|---:|---:|---:|---:|---:|---:|
|S3 `a=8000,b=10000`|1.21539|39.6080|4.0176e9|0.01014|+5.2976e8|0.00134|
|S4 `a,b -5%`|1.36251|38.1674|8.6937e9|0.01998|-4.9406e8|0.00114|
|S0 Z6|1.43411|37.5094|1.1376e10|0.02527|-1.4955e9|0.00332|

For these three controlled states, `eta31` rises almost linearly with normalized slenderness; the three-point Pearson correlation is approximately `0.9997`. This is not used as a fitted law; it is only a diagnostic observation.

The longitudinal third harmonic is also substantially more active than the transverse third harmonic. At Z6,

\[
\eta_{31}/\eta_{13}\approx7.6.
\]

Thus the first higher-harmonic deficiency exposed by the current state is not a wrong linear halfwave count and not primarily a transverse `n=3` mode; it is a finite-amplitude longitudinal-shape release direction.

## 5. Z6 branch trend

Using accepted Z6 single-mode branch states near the peak:

|D|q11|P (MN)|eta31|eta13|
|---:|---:|---:|---:|---:|
|0.680|0.00557366|37.4489|0.02417|0.00296|
|0.700|0.00583137|37.5067|0.02506|0.00326|
|0.705|0.00589760|37.5094|0.02527|0.00332|

`q31` therefore does not appear only at one peak-local numerical point; its generalized residual is already large on the approach to the accepted single-mode peak and grows mildly as the peak is approached.

## 6. Local q31 tangent predictor

A deliberately small finite `q31=+-1e-5` perturbation was used only to estimate the local slope of the `q31` residual at the Z6 single-mode state:

```text
R31(-1e-5) = 1.1030990e10 N mm
R31(+1e-5) = 1.1719843e10 N mm
```

Hence

\[
K_{33}^{loc}\approx
\frac{R_{31}(+10^{-5})-R_{31}(-10^{-5})}{2\times10^{-5}}
=3.4443\times10^{13}\;\mathrm{N\,mm}.
\]

A purely local Newton predictor would be

\[
q_{31}^{pred}=-\frac{R_{31}(0)}{K_{33}^{loc}}
\approx-3.30\times10^{-4},
\]

or about `-5.6%` of the current `q11` amplitude. This is only a tangent predictor, not a coupled equilibrium solution.

The direct local load derivative from the same `+-1e-5` perturbation implies only about `+0.26 MN` at that predictor **before** re-equilibrating `D` and `q11`; therefore it must not be interpreted as the final capacity recovery.

## 7. Fail-fast on full finite-q31 continuation

An attempt was made to continue the same current material operator to finite `q31`. At small finite amplitudes the Cayley-Hamilton/N48 coefficient tensor expands strongly in the longitudinal harmonic degree. At `q31=-3e-4`, the current naive polynomial-composition implementation returned a physically impossible `P~107 MN` and huge residuals. That state is rejected as coefficient-space breakdown, not interpreted as physical strengthening.

Therefore this execution does **not** publish a two-mode Pu. The trustworthy result is the first-variation stationarity test, because at `q31=0` the material state is exactly the already validated single-mode current field and only the virtual-strain direction is new.

## 8. Causal decision

The evidence now supports a stronger statement than the previous “single-q is a suspect” wording:

```text
NGUYEN_SECOND_ORDER_AS_PRIMARY_Z6_CAUSE = NOT SUPPORTED
WRONG_LINEAR_M=1_AS_PRIMARY_CAUSE = NOT SUPPORTED
SINGLE_Q11_STATE_STATIONARY_IN_Q31_DIRECTION = FAIL
MISSING_Q31_FINITE_AMPLITUDE_DIRECTION = CONFIRMED MODEL-SPACE DEFICIENCY
Q13_DIRECTION = SECONDARY IN THIS GATE
Q31_EXPLAINS_FULL_24.5_PERCENT_CAPACITY_GAP = NOT YET QUANTIFIED
```

The current one-amplitude model can satisfy `Rq11=0` while carrying a large nonzero generalized force in an admissible `q31` direction. Therefore it is mathematically not an equilibrium of the enlarged Nguyen displacement space.

This does **not** mean Nguyen's second-order strain-displacement relation is wrong. It means the production projection of that relation onto one finite-amplitude harmonic is too restrictive in the high-slenderness region, at least for Z6/S4/S3.

## 9. Next task

The next task is not to modify material laws. It is to stabilize an exact sparse trigonometric/coefficient representation for the `q11+q31` field so that finite `q31` does not create the naive high-degree polynomial-conditioning failure. The required gate is:

```text
CURRENT_NEXT_TASK = Z6_Q11_Q31_SPARSE_HARMONIC_EXACT_MOMENT_COUPLED_EQUILIBRIUM
```

Requirements:

1. same Nguyen second-order kinematics;
2. same R10/N48/Cayley-Hamilton material target;
3. same local radial-cap outer-shell diagnostic;
4. no structural sampling/quadrature/cells;
5. `q31=0` must reproduce the current single-mode branch exactly;
6. solve coupled `Rq11=0, Rq31=0` at fixed D and then continue in D;
7. only after a stable connected two-mode branch exists may the change in Z6 Pu be compared with S4/S3 and with Zhou/Winter envelopes.
