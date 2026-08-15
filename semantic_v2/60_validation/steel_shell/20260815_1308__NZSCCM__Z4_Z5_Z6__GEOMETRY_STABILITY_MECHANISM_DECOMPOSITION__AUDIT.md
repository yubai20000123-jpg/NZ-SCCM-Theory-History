# NZ-SCCM Z4-Z5-Z6 geometry/stability mechanism decomposition

**Timestamp:** 2026-08-15 13:08 +08:00  
**Identity:** CURRENT CAUSAL AUDIT / NO THEORY CHANGE / NO CALIBRATION  
**Parent current state:** `semantic_v2/00_index/20260815_1233__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md`

---

## 0. Purpose

After the user-directed comparison correction, the two sides are intentionally different representations:

```text
NZ-SCCM = reduced analytical object; internal steel webs absorbed/equivalent into continuous concrete core
ZHOU = original full MCFSTW; internal steel webs retained; original Zhou formulas
```

The current numerical comparison is:

|case|NZ current MN|Zhou original full MN|NZ-Zhou|
|---|---:|---:|---:|
|Z4|66.886850|70.187272|-4.702%|
|Z5|13.177570|14.681648|-10.245%|
|Z6|37.509426|49.672436|-24.486%|

This audit does not change either model. Its goal is to decompose the apparent load gap into:

1. the intended section-strength representation change caused by absorbing web steel into concrete on the NZ side;
2. the additional difference in stability/path retention after each model is normalized by its own section-strength baseline.

---

## 1. Exact decomposition identity

Define

\[
\rho_s=\frac{P_{yth,NZ}^{red}}{P_{yth,Zhou}^{orig}},
\]

\[
\phi_{NZ}=\frac{P_{u,NZ}}{P_{yth,NZ}^{red}},
\qquad
\phi_Z=\frac{P_{u,Zhou}}{P_{yth,Zhou}^{orig}}.
\]

Then, without fitting or approximation,

\[
\boxed{
\frac{P_{u,NZ}}{P_{u,Zhou}}
=\rho_s\frac{\phi_{NZ}}{\phi_Z}
}
\]

The first factor is the section-representation effect. The second factor isolates the relative stability/path retention.

For an additive load decomposition, define the intermediate quantity

\[
P_{red|\phi_Z}=P_{yth,NZ}^{red}\phi_Z.
\]

Then

\[
P_{u,Zhou}-P_{u,NZ}
=
\underbrace{\left(P_{u,Zhou}-P_{red|\phi_Z}\right)}_{\text{section representation}}
+
\underbrace{\left(P_{red|\phi_Z}-P_{u,NZ}\right)}_{\text{stability/path difference}}.
\]

No experimental/comparator load enters the NZ root solution; this is post-processing of already persisted roots.

---

## 2. Z4-Z5-Z6 decomposition

|quantity|Z4|Z5|Z6|
|---|---:|---:|---:|
|a/h|30.000|23.077|69.231|
|b/h|40.000|15.385|92.308|
|a/b|0.750|1.500|0.750|
|local `ls/ts`|50|50|50|
|Zhou original lambda_n|0.635754|0.240871|1.434107|
|NZ reduced Pyth / MN|69.4144|13.0976|78.5856|
|Zhou original Pyth / MN|79.386112|14.681648|88.089888|
|strength ratio rho_s|0.874390|0.892107|0.892107|
|NZ Pu / MN|66.886850|13.177570|37.509426|
|Zhou original Pu / MN|70.187272|14.681648|49.672436|
|phi_NZ|0.963588|1.006106|0.477307|
|phi_Zhou|0.884125|1.000000|0.563884|
|phi_NZ / phi_Zhou|1.089877|1.006106|0.846463|

### Z5

For Z5,

\[
P_{red|\phi_Z}=13.0976\ \mathrm{MN},
\]

because Zhou has `phi_Z=1`.

Total gap:

\[
14.681648-13.177570=1.504078\ \mathrm{MN}.
\]

Section-representation contribution:

\[
14.681648-13.097600=1.584048\ \mathrm{MN}.
\]

Stability/path contribution:

\[
13.097600-13.177570=-0.079970\ \mathrm{MN}.
\]

Thus the Z5 underprediction is **not a stability failure**. The intended web-steel-to-concrete reduction already explains slightly more than the entire Z5 gap; NZ's normalized path retention is actually about `0.61%` higher than Zhou's.

Decision:

```text
Z5_PRIMARY_GAP = SECTION REPRESENTATION
Z5_STABILITY_PATH_DEFICIENCY = NOT SUPPORTED
```

### Z4

For Z4,

\[
P_{red|\phi_Z}=61.371029\ \mathrm{MN}.
\]

The intended section representation alone would reduce Zhou's load by

\[
70.187272-61.371029=8.816243\ \mathrm{MN}.
\]

But NZ's normalized retention is higher:

\[
\phi_{NZ}=0.963588>\phi_Z=0.884125,
\]

which recovers

\[
66.886850-61.371029=5.515821\ \mathrm{MN}.
\]

Hence the apparently good `-4.70%` agreement for Z4 contains a **large cancellation** between lower reduced section strength and higher NZ stability/path retention.

Decision:

```text
Z4_GOOD_TOTAL_AGREEMENT = PARTLY CANCELLATION
Z4_STABILITY_RETENTION = HIGHER THAN ZHOU
```

### Z6

For Z6,

\[
P_{red|\phi_Z}
=78.5856\times0.5638835179
=44.313125\ \mathrm{MN}.
\]

The total difference is

\[
49.672436-37.509426
=12.163010\ \mathrm{MN}.
\]

Section-representation contribution:

\[
49.672436-44.313125
=5.359311\ \mathrm{MN},
\]

or about

\[
44.1\%\ \text{of the total load gap}.
\]

Additional stability/path contribution:

\[
44.313125-37.509426
=6.803698\ \mathrm{MN},
\]

or about

\[
55.9\%\ \text{of the total load gap}.
\]

Therefore accepting the user's intended web-equivalence rule does **not** remove the Z6 anomaly. Roughly half of the apparent 24.5% cross-representation gap is expected from the section representation, but the other half is a genuine additional difference in normalized stability/path retention.

Equivalently,

\[
\frac{\phi_{NZ}}{\phi_Z}=0.846463,
\]

so NZ retains about `15.35%` less normalized resistance than Zhou after each model is divided by its own section-strength baseline.

Decision:

```text
Z6_SECTION_REPRESENTATION_EFFECT = MATERIAL BUT INSUFFICIENT
Z6_ADDITIONAL_STABILITY_PATH_DEFICIT = CONFIRMED
```

---

## 3. Z4 versus Z6 is the cleanest geometric control pair

Z4 and Z6 share:

```text
fy = 355 MPa
fcu = 40 MPa
ts = 4 mm
ls = 200 mm
ls/ts = 50
a/b = 0.75
```

Thus local steel-subpanel slenderness, material strengths and plan aspect ratio are unchanged.

The principal change is global slenderness:

```text
Z4: a/h = 30.000, b/h = 40.000
Z6: a/h = 69.231, b/h = 92.308
```

Both `a/h` and `b/h` increase by a factor of about `2.3077`.

Zhou's original stability factor changes from

\[
0.884125\rightarrow0.563884,
\]

so the Z6/Z4 retention ratio is

\[
0.637787.
\]

NZ changes from

\[
0.963588\rightarrow0.477307,
\]

so the Z6/Z4 retention ratio is only

\[
0.495343.
\]

The ratio of these two degradation ratios is

\[
\frac{0.495343}{0.637787}=0.776660.
\]

Hence the current NZ path degrades about `22.33%` more strongly than Zhou when moving from Z4 to geometrically similar but much more globally slender Z6.

This isolates the remaining causal target to a **global-slenderness / finite-amplitude / stability-path mechanism**, not local plate `ls/ts`, steel yield strength, concrete strength, or the intended web-equivalence strength bookkeeping.

---

## 4. Source consistency of the geometric diagnosis

Zhou's Chapter 5 summary states that four-edge simply-supported axial stability is jointly governed by `Dy`, `Dx` and `H` and is closely related to `a/h` and `b/h`. It reports elastic critical ratios around `a/h=36` and `b/h=60`; in the elastoplastic discussion the reported critical width ratio is around `b/h=40` and the critical height ratio is below 20.

Against those source markers:

```text
Z5: a/h=23.08, b/h=15.38, lambda=0.241, phi_Z=1.0 -> strength-controlled source result
Z4: a/h=30, b/h=40, lambda=0.636 -> transition / moderate-stability regime
Z6: a/h=69.23, b/h=92.31, lambda=1.434 -> deep stability-sensitive regime
```

This source trend matches the decomposition: Z5 has essentially no normalized stability discrepancy, while Z6 is the unique case with a large negative `phi_NZ/phi_Z - 1`.

---

## 5. Finite-amplitude state audit

With the current `A0=a/500` identity and `q=A_increment/b`, the peak-state deformation scales are:

|case|A0/h|A_increment/h|(A0+A_increment)/h|
|---|---:|---:|---:|
|Z4|0.0600|0.01881|0.07881|
|Z5|0.04615|0.00225|0.04840|
|Z6|0.13846|0.54439|0.68286|

The Z6 connected branch therefore reaches a finite-amplitude state qualitatively unlike Z4/Z5. This is not itself proof of an error; it identifies where the next audit must act. In particular, any mechanism that is harmless near small finite amplitude but too soft in the deep postbuckling regime can remain hidden in Z0-Z5 and appear only in Z6.

---

## 6. All-seven sign audit

Using the same exact decomposition for Z0-Z6:

```text
Z0 phi_NZ/phi_Z = 1.1110
Z1 phi_NZ/phi_Z = 1.0563
Z2 phi_NZ/phi_Z = 1.1140
Z3 phi_NZ/phi_Z = 1.1071
Z4 phi_NZ/phi_Z = 1.0899
Z5 phi_NZ/phi_Z = 1.0061
Z6 phi_NZ/phi_Z = 0.8465
```

Z6 is the **only representative case in which the normalized NZ stability/path retention is below Zhou's**. This sign reversal is stronger evidence than the raw cross-representation load error alone.

Therefore:

```text
UNIVERSAL_R10_MATERIAL_DEFECT = NOT SUPPORTED
UNIVERSAL_STEEL_STRENGTH_DEFECT = NOT SUPPORTED
LOCAL_SUBPANEL_SLENDERNESS_AS_Z6_UNIQUE_CAUSE = REJECTED (ls/ts=50 for Z4-Z6)
GLOBAL_SLENDERNESS_REGIME = PRIMARY ACTIVE CAUSAL AXIS
```

---

## 7. Next executable task

The cleanest next test is a paired Z4/Z6 same-branch stability audit, because the pair holds material data, `ls/ts` and `a/b` fixed while strongly changing only global slenderness.

```text
NEXT = Z4_Z6_PAIRED_SAME_BRANCH_KZ_HALFWAVE_AUDIT
```

Execution requirements:

1. retain `A0=a/500` and the current local progressive radial-cap diagnostic on both cases;
2. retain the user's web-steel-to-concrete equivalence on the NZ side;
3. do not modify R10/N48/D15;
4. evaluate the current-tangent Zhou/Navier `KZ` along the connected `Rq=0` branch for Z4 and Z6;
5. explicitly compare the event ordering `first yield -> KZ=0 -> load maximum/fold`;
6. independently check admissible integer halfwaves for the NZ reduced object, without using Zhou Pu, observed FE bulge count, or experimental mode to choose a halfwave;
7. determine whether Z6's `D≈0.705` load maximum is preceded by a tangent-stability loss or whether the load-path softening itself is the controlling mechanism.

No empirical correction is authorized by this audit.

---

## 8. Companion result

- `semantic_v2/50_results/steel_shell/20260815_1308__NZSCCM__Z0_Z6__STRENGTH_VS_STABILITY_DECOMPOSITION__RESULT.csv`
