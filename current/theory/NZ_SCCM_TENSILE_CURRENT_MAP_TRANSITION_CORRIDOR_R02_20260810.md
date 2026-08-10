# NZ-SCCM TENSILE CURRENT MAP TRANSITION CORRIDOR R02

**Date:** 2026-08-10

## 0. Identity
Same-route G18/G20/G27 current-map reformulation. No route switch, no structural Pu calibration, no formal spatial quadrature, no runtime TT/TC/CC partition.

## 1. Candidate definition actually executed
Baseline reference uses the frozen material-coordinate smoothings

\[
\eta_{\Pi,0}=x_{cr}/20,
\qquad
\eta_{H,0}=0.05.
\]

For a common widening factor k:

\[
\eta_\Pi(k)=k\eta_{\Pi,0},
\qquad
\eta_H(k)=k\eta_{H,0}.
\]

The tensile utilization is

\[
T_k(\lambda)=\alpha_T(k)\left[r+(m_t-1)H_k(r;1)-m_tH_k(r;10)\right],
\]

where `alpha_T(k)` is determined only from the material operator so that the uniaxial tensile peak remains equal to the baseline reference peak. Case21/Swartz Pu is not used.

## 2. Stage A — originally planned k=1,2,4,8 screen
The originally planned common-width family was actually executed first. Results:

| k | alpha_T | curvature ratio near lambda=0 | r=1 | r=10 | CC P95 stress change / fc | TC P95 | TT P95 |
|---:|---:|---:|---:|---:|---:|---:|---:|
|1|1.000000|1.0000|1.0000|1.0000|0|0|0|
|2|1.007465|0.5027|0.5096|0.5038|0.002112|0.007913|0.001030|
|4|1.012051|0.2504|0.2671|0.2531|0.009385|0.035605|0.002970|
|8|0.988484|0.1184|0.1446|0.1237|0.025275|0.121299|0.008094|

Thus k=4 and 8 reduce curvature strongly but create excessive TC/CC drift. The screen was therefore fail-fast refined to 1<k<=2 rather than continuing to larger widths.

## 3. Stage B — refined material-only width screen

| k | alpha_T | mean peak-curvature ratio | CC stress P95/fc | TC stress P95/fc | TT stress P95/fc | CC tangent P95/kappa | TC tangent P95/kappa | TT tangent P95/kappa |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1.00|1.000000|1.000000|0|0|0|0|0|0|
|1.25|1.002227|0.802271|0.000401|0.002103|0.000270|0.002555|0.043840|0.019649|
|1.50|1.004208|0.670381|0.000888|0.004029|0.000530|0.005657|0.097338|0.035763|
|1.75|1.005952|0.576116|0.001457|0.005792|0.000783|0.009291|0.160056|0.047437|
|2.00|1.007465|0.505370|0.002112|0.007913|0.001030|0.013436|0.231306|0.055203|

Interpretation:

- `k=1.25`: about 19.8% mean reduction of the three curvature peaks; TC stress P95 change only about 0.210% fc; TC tangent P95 change about 4.38% of the initial normalized tangent.
- `k=1.5`: about 33.0% curvature reduction, but TC tangent P95 change rises to about 9.73%.
- `k>=1.75`: tangent disturbance grows too rapidly for this to remain a low-risk material regularization.

Therefore `k=1.25` is retained as the moderate physical regularization candidate, `k=1.5` as a stronger diagnostic candidate, and `k>=1.75` is HOLD.

## 4. Crucial negative result — reasonable widening alone does not solve the compiler problem
Using the same full qualification interval

\[
\lambda\in[-2.4390243902,\,0.7317073171],
\]

we repeated the same global Chebyshev least-squares material-coordinate approximation screen for `T(lambda)`.

At degree 32:

- baseline k=1 max normalized error = 31.806%;
- k=2 max normalized error = 31.324%.

At degree 64 the baseline remains about 17.59%, and k=2 remains about 17.62%.

Thus halving the local curvature peaks does **not** materially repair the single-global-polynomial representation over the full historical qualification interval. This is the key R02 conclusion: pure physical widening is insufficient as the sole solution.

## 5. Dimensional/spectral-domain reduction diagnostic
An existing Case21 zero-spatial audit already identified separated principal spectra at the diagnostic state `D=0.75, q=0.002`:

\[
\lambda_+\in[-0.1051,\,0.13584],
\]

\[
\lambda_-\in[-0.86569,\,-0.62473].
\]

These intervals are used here only as a diagnostic demonstration; they are not frozen as the production Swartz-family domain.

For the **same baseline material function** and the **same degree-32 polynomial screen**:

- full historical interval: max normalized T error = 31.806%;
- separated `lambda+` interval: max normalized T error = 2.283%.

For the compression-only `lambda-` interval, degree 6 already gives max absolute T error about `5.19e-12`.

This is a much larger complexity reduction than reasonable physical smoothing.

## 6. Meaning of “dimensional reduction” in the current theory
The 4D graph `(epsilon1,epsilon2,sigma1,sigma2)` is not a 4D input problem. The current map is still a 2->2 map. Safe reductions are representation/domain reductions, not deletion of physics:

1. **Invariant reduction already active:** `(epsilon1,epsilon2)` -> `(J1,J2)` with the G18/G27 coaxial tensor basis.
2. **Spectral-branch reduction:** if a positive global spectral gap is proven over the relevant structural parameter box, `lambda+` and `lambda-` are globally continuous branches and may use separate scalar analytic approximants of the same material function on disjoint spectral intervals. This is not a spatial/material-state partition.
3. **Reachable-domain reduction:** qualify the current map on the analytically reachable union of material states for the target plate family rather than on an unnecessarily large oracle square. This domain must be derived from kinematics/parameter bounds, never from test Pu calibration.
4. **Low-rank invariant representation:** after the reachable `(J1,J2)` domain is established, test whether `A(J1,J2),B(J1,J2)` admit a small separated polynomial rank. This preserves the same current-map architecture and remains D15-compatible.

## 7. R02 decision

```text
TENSILE_CURRENT_MAP_TRANSITION_CORRIDOR_R02 = PASS_DIAGNOSTIC_WITH_REFRAME
ROUTE_SWITCH = NO
PURE_WIDTH_WIDENING = INSUFFICIENT_AS_SOLE_SOLUTION
K_1P25 = RETAIN_MODERATE_MATERIAL_CANDIDATE_NOT_FROZEN
K_1P5 = RETAIN_STRONGER_DIAGNOSTIC
K_GE_1P75 = HOLD_DUE_TANGENT_DISTURBANCE
SPECTRAL_REACHABLE_DOMAIN_REDUCTION = PROMOTE_TO_NEXT_MAIN_ACTION
CASE21_PU = NOT_RUN
SWARTZ24 = NOT_RUN
```

## 8. Next main action

```text
CURRENT_RECOMMENDED_NEXT_TASK = SPECTRAL_REACHABLE_DOMAIN_REDUCTION_R03
```

R03 must stay on the same G18/G20/G27/G26/G28/G30 route. It must:

1. derive analytic/worst-case bounds for `lambda+` and `lambda-` over the actual Case21/Swartz production parameter box;
2. prove whether a nonzero branch gap holds over that box;
3. map the resulting reachable region into `(J1,J2)`;
4. quantify polynomial/order reduction on separated branches and reachable invariant domain;
5. only then decide whether the mild `k=1.25` physical regularization is still needed;
6. keep zero formal spatial quadrature and no runtime state partition.
