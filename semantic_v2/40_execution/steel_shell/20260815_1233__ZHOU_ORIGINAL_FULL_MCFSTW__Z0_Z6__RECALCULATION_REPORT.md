# Zhou original full-MCFSTW Z0-Z6 recalculation

**Timestamp:** 2026-08-15 12:33 +08:00  
**Identity:** USER-DIRECTED ORIGINAL-SOURCE FORMULA REPLAY / CROSS-REPRESENTATION COMPARISON  
**Governance lock:** `semantic_v2/10_governance/20260815_1233__NZSCCM_REDUCED_VS_ZHOU_ORIGINAL_FULL__COMPARISON_IDENTITY__LOCK.md`

---

## 0. Purpose

The previous project comparator reduced Zhou's section together with the NZ-SCCM object. The user corrected that convention:

- NZ-SCCM keeps its reduced representation, with internal steel webs equivalent/absorbed into the continuous concrete core;
- Zhou's side is **not reduced** and is recalculated using the original MCFSTW section/topology and original source equations.

Therefore this report is intentionally a cross-representation reference comparison:

```text
NZ = reduced/equivalent-core analytical model
ZHOU = original full MCFSTW formula
```

It is not labelled a same-object comparison.

Z0-Z6 are representative calculation combinations selected from the parameter ranges of Zhou Table 5.1; they are not asserted to be literal FE-row or specimen IDs.

---

## 1. Input cases

|case|ns|ls mm|h mm|ts mm|fy MPa|fcu MPa|a mm|b mm|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|Z0|30|200|130|4|355|40|6000|6000|
|Z1|30|200|100|4|235|40|6000|6000|
|Z2|30|200|130|4|460|40|6000|6000|
|Z3|30|200|130|4|355|60|6000|6000|
|Z4|40|200|200|4|355|40|6000|8000|
|Z5|10|200|130|4|355|40|3000|2000|
|Z6|60|200|130|4|355|40|9000|12000|

All satisfy `b=ns*ls`.

Material constants:

```text
Es = 206000 MPa
nu_s = 0.30
nu_c = 0.20
Ec(C40) = 32500 MPa
Ec(other fcu) = 1e5 / (34.7/fcu + 2.2) MPa
fc' = 0.76 fcu
```

For C60 this gives `Ec=35992.8014397121 MPa`.

---

## 2. Original full-section strength bookkeeping

Zhou defines

\[
P_{yth}=f_yA_s+f'_cA_c,\qquad f'_c=0.76f_{cu}.
\]

The source defines `ls` as the centerline-to-centerline distance between internal web plates. Retaining the original web-steel topology therefore gives the concrete area

\[
A_c=n_s(l_s-t_s)(h-2t_s),
\]

and, for the complete rectangular multi-cell wall cross-section,

\[
A_s=bh-A_c.
\]

No steel web is converted to concrete on the Zhou side.

The resulting full-section baselines are:

|case|Ac mm²|As mm²|steel strength MN|concrete strength MN|Pyth MN|
|---|---:|---:|---:|---:|---:|
|Z0|717360|62640|22.237200|21.807744|44.044944|
|Z1|540960|59040|13.874400|16.445184|30.319584|
|Z2|717360|62640|28.814400|21.807744|50.622144|
|Z3|717360|62640|22.237200|32.711616|54.948816|
|Z4|1505280|94720|33.625600|45.760512|79.386112|
|Z5|239120|20880|7.412400|7.269248|14.681648|
|Z6|1434720|125280|44.474400|43.615488|88.089888|

---

## 3. Original Zhou stiffness chain

### 3.1 Secondary-direction bending stiffness Dx

Using Zhou's original two-skin + concrete-layer expression,

\[
D_x
=E_s\frac{h^3-(h-2t_s)^3}{12}
+E_c\frac{(h-2t_s)^3}{12}.
\]

### 3.2 Main-direction bending stiffness Dy

With the internal web topology retained,

\[
D_{y,s}
=\frac{E_s}{b}
\left[
\frac{bh^3}{12}
-\frac{n_s(l_s-t_s)(h-2t_s)^3}{12}
\right],
\]

\[
D_{y,c}
=\frac{E_c}{b}
\frac{n_s(l_s-t_s)(h-2t_s)^3}{12},
\]

\[
D_y=D_{y,s}+D_{y,c}.
\]

### 3.3 Free-torsion stiffness Dxy

With

\[
G_s=\frac{E_s}{2(1+\nu_s)},\qquad
G_c=\frac{E_c}{2(1+\nu_c)},
\]

outer-tube centreline area and perimeter are

\[
A_0=(b-t_s)(h-t_s),
\]

\[
s=2[(b-t_s)+(h-t_s)].
\]

For uniform steel thickness,

\[
\int_s\frac{ds}{t_s}=\frac{s}{t_s}.
\]

The rectangular concrete torsion shape coefficient is replayed as

\[
\beta_{shape}
=\frac13\left[
1-0.63\frac{h-2t_s}{b-2t_s}
+0.052\left(\frac{h-2t_s}{b-2t_s}\right)^5
\right].
\]

Then

\[
D_t=\frac1b\left[
\frac{4G_sA_0^2}{\int_s ds/t_s}
+G_c\beta_{shape}(b-2t_s)(h-2t_s)^3
\right],
\]

and Zhou's relation `Dt=2Dxy` gives

\[
D_{xy}=\frac{D_t}{2}.
\]

### 3.4 Poisson coupling and H

\[
D_\mu=\nu_sD_{y,s}+\nu_cD_{y,c},
\]

\[
H=D_{xy}+D_\mu.
\]

Calculated stiffnesses are:

|case|Dx N·mm|Dy,s N·mm|Dy,c N·mm|Dy N·mm|Dxy N·mm|Dmu N·mm|H N·mm|
|---|---:|---:|---:|---:|---:|---:|---:|
|Z0|1.1461031e10|7.1665502e9|4.8195635e9|1.1986114e10|8.9649351e9|3.1138778e9|1.2078813e10|
|Z1|5.9081360e9|4.0665386e9|2.0667680e9|6.1333066e9|4.6109554e9|1.6333152e9|6.2442706e9|
|Z2|1.1461031e10|7.1665502e9|4.8195635e9|1.1986114e10|8.9649351e9|3.1138778e9|1.2078813e10|
|Z3|1.1989564e10|7.1665502e9|5.3375259e9|1.2504076e10|9.3991500e9|3.2174703e9|1.2616620e10|
|Z4|3.4998869e10|1.8259660e10|1.8785894e10|3.7045559e10|2.7594573e10|9.2350781e9|3.6829652e10|
|Z5|1.1461031e10|7.1665502e9|4.8195635e9|1.1986114e10|8.6476257e9|3.1138778e9|1.1761503e10|
|Z6|1.1461031e10|7.1665502e9|4.8195635e9|1.1986114e10|9.0467988e9|3.1138778e9|1.2160677e10|

All unrounded values are retained in the companion JSON.

---

## 4. Zhou Eq. (5-79): original four-edge SSSS elastic buckling

For each positive integer halfwave count `m`,

\[
N_{cr,m}=\pi^2\left[
\frac{D_xa^2}{m^2b^4}
+\frac{2H}{b^2}
+\frac{D_ym^2}{a^2}
\right].
\]

The total critical force is

\[
P_{cr,m}=bN_{cr,m}.
\]

For each Z case, all integer candidates `m=1...50` were evaluated and retained in the JSON. The minimum is selected without using an NZ load or any observed/test mode.

Selected results:

|case|m*|Pcr MN|
|---|---:|---:|
|Z0|1|78.306709|
|Z1|1|40.350206|
|Z2|1|78.306709|
|Z3|1|81.797440|
|Z4|1|196.411220|
|Z5|2|253.049173|
|Z6|1|42.831476|

Sanity check of the first candidates:

```text
Z0: m1=78.3067, m2=123.3163, m3=219.2797 MN
Z1: m1=40.3502, m2=63.3280 MN
Z2: same elastic stiffness as Z0
Z3: m1=81.7974, m2=128.7111 MN
Z4: m1=196.4112, m2=421.9455 MN
Z5: m1=269.6252, m2=253.0492, m3=366.8173 MN -> m*=2
Z6: m1=42.8315, m2=91.4317 MN
```

---

## 5. Original Zhou axial stability curve

Normalized slenderness is evaluated as

\[
\lambda_n=\sqrt{\frac{P_{yth}}{P_{cr}}}.
\]

For the original four-edge MCFSTW fitted axial stability curve, Eqs. (5-87)-(5-88),

\[
\phi_N=1\qquad(\lambda_n\le0.55),
\]

otherwise

\[
\phi_N=\frac1{\Phi_N+\sqrt{\Phi_N^2-\lambda_n^2}},
\]

with

\[
\Phi_N=0.454+0.192\lambda_n+0.416\lambda_n^2,
\qquad \lambda_n\le1,
\]

\[
\Phi_N=-0.140+1.387\lambda_n-0.186\lambda_n^2,
\qquad \lambda_n>1.
\]

Finally,

\[
P_{u,Zhou}^{orig}=\phi_NP_{yth}.
\]

This is Zhou's original formula chain applied to the original full MCFSTW representation of each Z parameter combination. It is not a newly generated Zhou FE result.

---

## 6. Final recalculation and comparison to current NZ diagnostic

The NZ values below are the current `a/500 + local-progressive-cap`, degree-32 engineering diagnostic values. Zhou values are the original full-MCFSTW formula results from Sections 2-5.

|case|lambda_n|phi_N|Zhou original full Pu MN|NZ current D32 MN|NZ-Zhou original|
|---|---:|---:|---:|---:|---:|
|Z0|0.749978|0.838815|**36.945541**|36.619330|**-0.883%**|
|Z1|0.866840|0.782380|**23.721432**|23.190470|**-2.238%**|
|Z2|0.804027|0.814137|**41.213379**|40.208070|**-2.439%**|
|Z3|0.819614|0.806574|**44.320271**|45.022780|**+1.585%**|
|Z4|0.635754|0.884125|**70.187272**|66.886850|**-4.702%**|
|Z5|0.240871|1.000000|**14.681648**|13.177570|**-10.245%**|
|Z6|1.434107|0.563884|**49.672436**|37.509426|**-24.486%**|

Summary:

\[
\boxed{MAPE_{Z0-Z5}=3.6821\%}
\]

\[
\boxed{MAPE_{Z0-Z6}=6.6541\%}
\]

Mean signed error for all seven is approximately `-6.2013%`.

The important distribution is:

```text
Z0-Z4 = all within +/-5%
Z5 = moderate underprediction, -10.245%
Z6 = dominant outlier, -24.486%
```

---

## 7. Difference from the superseded transferred-reduced comparator

The old comparator reduced Zhou's section and used a reduced isotropic diagnostic Pcr. Replaying Zhou on the original full MCFSTW gives:

|case|old transferred-reduced MN|new Zhou-original-full MN|increase|
|---|---:|---:|---:|
|Z0|33.429123|36.945541|+10.519%|
|Z1|22.208147|23.721432|+6.814%|
|Z2|36.858842|41.213379|+11.814%|
|Z3|41.158145|44.320271|+7.683%|
|Z4|62.043026|70.187272|+13.127%|
|Z5|13.097600|14.681648|+12.094%|
|Z6|44.740403|49.672436|+11.024%|

Thus the previous reduced comparator systematically understated the Zhou-original formula result by about 6.8%-13.1% for these seven representative combinations.

---

## 8. Interpretation

The user-directed comparison convention resolves the prior governance ambiguity without rederiving either theory:

1. **NZ-SCCM:** keep the internal-web-to-concrete equivalence already embedded in the reduced analytical object.
2. **Zhou:** retain the actual full MCFSTW steel-web topology and use the original formulas without reduction.
3. Compare the resulting capacities as two model representations of the same nominal parameter family, not as mathematically identical structural objects.

Under this convention, the pattern becomes particularly clear:

- Z0-Z4 show strong agreement at engineering scale;
- Z5 becomes a secondary geometric outlier;
- Z6 remains the unique major outlier and is even lower relative to Zhou's original formula (`-24.49%`) than relative to the superseded reduced comparator.

Therefore the earlier proposal to spend the next step rederiving a reduced Zhou `Dx-Dy-H` operator is no longer justified and is cancelled. The remaining technical question, if pursued, is why the NZ reduced theory departs specifically at the compact Z5 and especially the extreme wide/slender Z6 geometry after the comparison identity has been corrected.

No parameter was tuned to produce these agreements or discrepancies.

---

## 9. Companion artifacts

- `semantic_v2/40_execution/steel_shell/20260815_1233__ZHOU_ORIGINAL_FULL_MCFSTW__Z0_Z6__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260815_1233__ZHOU_ORIGINAL_FULL_MCFSTW__Z0_Z6__REPRO.py`
- `semantic_v2/50_results/steel_shell/20260815_1233__ZHOU_ORIGINAL_FULL_MCFSTW__Z0_Z6__RESULT.csv`
- `semantic_v2/10_governance/20260815_1233__NZSCCM_REDUCED_VS_ZHOU_ORIGINAL_FULL__COMPARISON_IDENTITY__LOCK.md`
