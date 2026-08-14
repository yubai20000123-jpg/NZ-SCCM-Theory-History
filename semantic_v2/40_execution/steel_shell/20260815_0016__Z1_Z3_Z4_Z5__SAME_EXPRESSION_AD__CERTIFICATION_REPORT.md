# Z1/Z3/Z4/Z5 strict same-expression Rq=0, L=0 certification

**Timestamp:** 2026-08-15 00:16 +08:00  
**Parent batch:** `20260814_2240__NZSCCM_Z0_Z6__VS_ZHOU__EXECUTION_REPORT.md`  
**Identity:** `STRICT_SAME_EXPRESSION_AD_RQ_L_ENGINEERING_CERTIFICATE`

## 1. Purpose

The preceding Z0-Z6 batch localized Z1, Z3, Z4 and Z5 by a smooth connected-branch load maximum, but did not yet promote those four states to the canonical same-expression `Rq=0 + L=0` derivative certificate. This execution closes exactly that gap without changing geometry, material parameters, R10, N48 order, compiler interval, Nguyen kinematics, D15 moments, or the reduced ideal-EP steel-shell continuation.

Formal structural spatial identity remains:

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
EXPERIMENTAL_LOAD_USED_FOR_TUNING = NO
```

## 2. Same-expression derivative construction

The canonical limit function is

\[
L=P_D R_{q,q}-P_qR_{q,D}.
\]

For this certification, `P`, `Rq`, `P_D`, `P_q`, `Rq,D`, and `Rq,q` are propagated from the **same finite coefficient-space expression** by forward automatic differentiation through:

```text
R10 primitive coefficients
-> N48-C1/MM
-> Cayley-Hamilton recurrence
-> Nguyen D,q finite field
-> coefficient-space products/contractions
-> general-D15 exact moments
-> concrete + reduced steel-shell P,Rq
-> same-expression first derivatives
```

No branch-load finite-difference slope is substituted for `L`; no experimental or Zhou load participates in the root.

The canonical numerical gates used are

\[
R_{norm}=\frac{|R_q|}{\max(R_{mat},|R_{q,c}|+|R_{q,s}|)}\le10^{-5},
\]

\[
L_{norm}=\frac{P_D R_{q,q}-P_qR_{q,D}}{|P_D R_{q,q}|+|P_qR_{q,D}|},\qquad |L_{norm}|\le10^{-5}.
\]

## 3. Certified roots

|Case|D|q|Pu (MN)|Zhou (MN)|error|Rnorm|Lnorm|decision|
|---|---:|---:|---:|---:|---:|---:|---:|---|
|Z1|0.6076158841|0.001631384062|20.89868703|22.20814719|-5.8963%|4.39e-10|-8.59e-7|PASS|
|Z3|0.8469249001|0.001408113142|42.33906044|41.15814543|+2.8692%|7.89e-10|+2.74e-8|PASS|
|Z4|0.9497834233|0.000594936054|62.03715150|62.04302600|-0.00947%|1.76e-9|+4.02e-7|PASS|
|Z5|0.9886228551|0.000119178791|12.87876017|13.09760000|-1.6708%|3.89e-8|+5.16e-9|PASS|

All four roots are therefore inside both frozen engineering residual gates.

## 4. Same-expression derivative audit values

|Case|P_D (N)|P_q (N)|Rq,D (N mm)|Rq,q (N mm)|
|---|---:|---:|---:|---:|
|Z1|1.009165e7|-3.470712e9|-1.296344e9|4.458368e11|
|Z3|6.497084e6|-6.379654e9|-1.088771e9|1.069092e12|
|Z4|3.699843e6|-1.650824e10|-1.941555e9|8.662982e12|
|Z5|3.448338e5|-6.895601e9|-1.455353e8|2.910253e12|

The two large terms in `L` cancel to the normalized residuals listed above; the result is not inferred from a visually flat load curve.

## 5. Effect relative to the previous smooth-peak localization

The strict derivative roots barely change the reported capacity:

|Case|previous smooth peak (MN)|strict Rq-L root (MN)|change (kN)|
|---|---:|---:|---:|
|Z1|20.89862728|20.89868703|+0.05975|
|Z3|42.33904065|42.33906044|+0.01979|
|Z4|62.03712974|62.03715150|+0.02176|
|Z5|12.87840902|12.87876017|+0.35115|

Thus the prior branch-max localization was already extremely close in load; this execution mainly upgrades its **mathematical identity**, not its numerical capacity.

## 6. Certification boundary

```text
Z1_SAME_EXPRESSION_RQ_L = PASS
Z3_SAME_EXPRESSION_RQ_L = PASS
Z4_SAME_EXPRESSION_RQ_L = PASS
Z5_SAME_EXPRESSION_RQ_L = PASS
SPATIAL_QUADRATURE = 0
STRUCTURAL_CALIBRATION = NO
```

This file certifies the requested same-expression `Rq=0,L=0` condition and the frozen `Rnorm/Lnorm` gates. A separate two-independent-backend `d_ij` repeatability exercise is not relabelled as completed here; it is distinct from the requested same-expression derivative closure.
