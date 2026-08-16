# NZ-SCCM — Z0–Z5 AR2 discrepancy localization

**Timestamp:** 2026-08-16 10:54 +08:00  
**Status:** CURRENT ERROR-LOCALIZATION REPORT

## 1. Why this audit was opened

The 10:43 AR2 run produced large reductions for Z0–Z4 relative to Zhou/Winter even though these specimens are materially stockier than Z6. The user correctly challenged whether a membrane-redistribution effect of that size is physically credible.

The purpose of this audit is not to defend the 10:43 numbers. It is to locate the first proven failure in the calculation chain.

## 2. First isolation: remove all out-of-plane redistribution

Set `q=0`. Then the state is uniform, so no structural spatial integration is required. The exact scalar R10 target can be evaluated directly, together with the uniform face-steel and web-steel elastic-perfectly-plastic caps.

The resulting flat-section maxima are:

|Case|exact flat q=0 capacity (MN)|Zhou full-section Pyth (MN)|flat/Pyth|10:43 challenged Pu (MN)|10:43 drop from flat|
|---|---:|---:|---:|---:|---:|
|Z0|45.0752|44.0449|1.0234|33.4910|-25.70%|
|Z1|31.0016|30.3196|1.0225|19.7360|-36.34%|
|Z2|51.5421|50.6221|1.0182|35.9781|-30.20%|
|Z3|55.9792|54.9488|1.0188|39.6889|-29.10%|
|Z4|80.7600|79.3861|1.0173|63.7385|-21.08%|
|Z5|15.0251|14.6816|1.0234|14.7824|-1.62%|

This is important: **the base section/material assembly itself does not explain the 20–36% loss.** With no out-of-plane deformation, the frozen R10 + steel + web model sits within roughly +1.7 to +2.3% of Zhou's full-section squash scale.

So the large drop enters only after the imperfect out-of-plane branch is activated.

## 3. Second isolation: is the q-amplitude obviously wrong?

The challenged peak amplitudes were compared with the classical imperfect-plate linear estimate

\[
\frac{A}{A_0}\approx\frac{\eta}{1-\eta},\qquad \eta=P/P_{cr}.
\]

|Case|calculated A/A0|classical estimate|A_total/tc|curvature-strain / mean axial-strain|
|---|---:|---:|---:|---:|
|Z0|0.792|0.747|0.353|0.186|
|Z1|0.898|0.957|0.495|0.254|
|Z2|1.030|0.850|0.399|0.197|
|Z3|0.913|0.943|0.376|0.215|
|Z4|0.586|0.549|0.264|0.158|
|Z5|0.095|0.068|0.072|0.061|

The q-amplitudes are of the same order as classical imperfection amplification. Therefore there is **no evidence yet of an order-of-magnitude error in the generalized out-of-plane equilibrium**.

This does not prove the nonlinear branch correct, but it prevents us from blaming the q-equation first.

A second point is also visible: because the imposed imperfection remains `A0=a/500`, once `a/b=2` we have `A0=0.004b`. For Z0–Z4 this corresponds to `A0/tc≈0.17–0.26`, and the amplified total deflection reaches `0.26–0.50 tc`. That is not mathematically infinitesimal. Thus the user's stocky-plate intuition remains a valid audit expectation, but the imposed imperfection is also not negligible relative to thickness.

## 4. Proven failure: the 10:43 material compiler

The 10:43 process reused the accepted-Z6 wide N48 interval for all Z0–Z5:

\[
\lambda\in[-2.35,+1.90].
\]

The committed wide-hull compiler diagnostics already show approximately

```text
T max error   ~= 0.704
T^7 max error ~= 0.796
```

The decisive new check is that these are **not remote full-hull errors outside the stocky cases**. Their maxima occur inside the actual Z0–Z5 reachable material ranges, at the sharp small-positive tension transition:

```text
lambda ~ +0.039:
    exact T  ~ 0.931
    N48 T    ~ 0.227
    abs error~ 0.704

lambda ~ +0.048:
    exact T^7  ~ 0.866
    N48 T^7    ~ 0.070
    abs error  ~ 0.796
```

Every challenged Z0–Z5 final envelope contains this region. For example:

```text
Z0 [-1.122,+.207]
Z1 [-.749,+.183]
Z2 [-1.389,+.270]
Z3 [-.849,+.176]
Z4 [-1.123,+.181]
Z5 [-1.064,+.074]
```

Therefore the wide N48 basis is wrong by order one precisely where mixed tension/compression activation is being evaluated.

This is not the previously relaxed `1e-10` strict-remainder issue. It is a basic material-map fidelity failure.

## 5. Why this invalidates the 10:43 strength table

The challenged differences against Zhou were only about 8–17% for Z0–Z4, and against Winter about 19–24%. A material activation basis with 70–80% scalar-function error in the visited state domain cannot support interpretation at that scale.

Hence:

```text
20260816_1043_Z0_Z5_AR2_CAPACITY_TABLE = NOT RELIABLE
```

The previous wording that Z0–Z4 show a systematic physically meaningful NZ-SCCM underprediction is withdrawn.

## 6. Can we fix it simply by shrinking the one-interval N48 hull?

A first material-coordinate-only precheck was performed with narrower one-interval N48 ranges. It improves the error, but not enough:

|Case|trial interval|max T error|max T7 error|
|---|---|---:|---:|
|Z0|[-1.25,.30]|~0.197|~0.354|
|Z1|[-.85,.25]|~0.121|~0.274|
|Z2|[-1.50,.35]|~0.256|~0.392|
|Z3|[-.95,.25]|~0.133|~0.237|
|Z4|[-1.25,.25]|~0.170|~0.214|
|Z5|[-1.15,.15]|~0.104|~0.217|

So simply taking the same N48 formula and narrowing its global interval is still insufficient for a 10% capacity-comparison problem. The sharp positive-tension activation requires a better material-coordinate representation.

## 7. Current conclusion

The user's concern is justified. The first proven problem is **the new calculation process**, specifically:

\[
\boxed{\text{reusing the Z6 wide single N48 material compiler for Z0–Z5 was wrong.}}
\]

At this stage we have **not** proven that the underlying one-halfwave Nguyen/D15 geometry is wrong. The amplitude check is broadly classical. The exact flat-state check is also healthy.

Therefore the current status is:

```text
Z0-Z5 10:43 Pu values = RETRACTED_PENDING_RECALCULATION
Z0-Z5 Zhou/Winter error percentages = RETRACTED_PENDING_RECALCULATION
Z6 51.30 MN = retained because user explicitly accepted it
```

## 8. Mandatory next calculation

The next step is not another Pu sweep. It is:

```text
Z0_Z5_AR2_CURRENT_OPERATOR_FIDELITY_REBUILD_ZERO_SPATIAL_INTEGRATION
```

The material compiler must be rebuilt so the original R10 current operator is represented faithfully in the actually reached mixed tension/compression range while retaining:

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
```

Only after that material gate passes are Z0–Z5 to be recalculated.
