# Zhou Table 5.1 representative Z0-Z6 — batch comparison report

**Timestamp:** 2026-08-14 21:52 +08:00

## 1. Scope

Seven representative parameter combinations were selected within the parameter ranges of Zhou Table 5.1 so that material-strength, wall-thickness, width, height and aspect-ratio extremes are represented. They are calculation cases Z0-Z6, not claimed to be literal specimen IDs or literal rows from Zhou's FE matrix.

For every comparison, the same reduced object is used on both sides:

```text
concrete core + two outer steel faceplates
internal web steel bearing contribution = deleted
```

No experimental load is used to tune any parameter.

## 2. Representative cases

|case|role|ns|ls mm|h mm|ts mm|fy MPa|fcu MPa|a mm|b mm|
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
|Z0|baseline|30|200|130|4|355|40|6000|6000|
|Z1|low fy + thin wall|30|200|100|4|235|40|6000|6000|
|Z2|high fy|30|200|130|4|460|40|6000|6000|
|Z3|high concrete strength|30|200|130|4|355|60|6000|6000|
|Z4|thick/wide wall|40|200|200|4|355|40|6000|8000|
|Z5|compact geometric extreme|10|200|130|4|355|40|3000|2000|
|Z6|wide/slender geometric extreme|60|200|130|4|355|40|9000|12000|

## 3. Zhou empirical Eqs. 5-87 to 5-88

The reduced-section reference is

\[
P_{yth}=f'_cA_c+f_yA_s,\qquad f'_c=0.76f_{cu}.
\]

For the reduced elastic diagnostic,

\[
D_{EI}=E_c\frac{(h-2t_s)^3}{12}+E_s\frac{h^3-(h-2t_s)^3}{12}.
\]

For each whole-wall integer halfwave number m,

\[
\alpha=\pi/b,\qquad\beta=m\pi/a,
\]

\[
P_{cr}(m)=bD_{EI}\frac{(\alpha^2+\beta^2)^2}{\beta^2}.
\]

The minimizing integer is retained and the representative complete-halfwave length is `ell=a/m*`.

Then

\[
\lambda_n=\sqrt{P_{yth}/P_{cr}}.
\]

Zhou empirical curve:

\[
\phi_N=1\quad (\lambda_n\le0.55),
\]

otherwise

\[
\phi_N=[\Phi_N+\sqrt{\Phi_N^2-\lambda_n^2}]^{-1},
\]

with

\[
\Phi_N=0.454+0.192\lambda_n+0.416\lambda_n^2\quad(\lambda_n\le1),
\]

\[
\Phi_N=-0.140+1.387\lambda_n-0.186\lambda_n^2\quad(\lambda_n>1).
\]

Finally

\[
P_{u,Zhou}=\phi_NP_{yth}.
\]

## 4. Full Zhou batch numerical output

|case|Pyth MN|m*|ell mm|Pcr MN|lambda_n|Phi_N|phi_N|Pu,Zhou empirical MN|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|Z0|39.2928|1|6000|75.410561|0.721839|0.809351|0.850770|33.429123|
|Z1|28.0608|1|6000|38.873977|0.849612|0.917411|0.791430|22.208147|
|Z2|44.3328|1|6000|75.410561|0.766737|0.845774|0.831412|36.858842|
|Z3|50.4192|1|6000|78.888169|0.799451|0.873370|0.816319|41.158145|
|Z4|69.4144|1|6000|187.405054|0.608603|0.724937|0.893806|62.043026|
|Z5|13.0976|2|1500|245.477088|0.230989|0.520546|1.000000|13.097600|
|Z6|78.5856|1|9000|40.912848|1.385931|1.425017|0.569321|44.740403|

## 5. NZ-SCCM status and comparison

The repository was checked for actual NZ-SCCM values for Z0-Z6. The only persisted same-object numerical NZ value is Z0 = 26.1085 MN, with identity `historical diagnostic branch-peak neighbourhood`, not a newly certified production `Rq=0 + L=0` root.

No legal persisted NZ-SCCM Pu/diagnostic load exists for Z1-Z6. Therefore this report does not fill them by scaling Z0, by multiplying Pyth by a common coefficient, or by borrowing Zhou's curve.

|case|Pu NZ-SCCM MN|Pu Zhou empirical MN|NZ-Zhou %|status|
|---|---:|---:|---:|---|
|Z0|26.1085|33.429123|-21.8989|persisted NZ diagnostic, not certified production root|
|Z1|—|22.208147|—|NZ not yet calculated; no legal persisted value|
|Z2|—|36.858842|—|NZ not yet calculated; no legal persisted value|
|Z3|—|41.158145|—|NZ not yet calculated; no legal persisted value|
|Z4|—|62.043026|—|NZ not yet calculated; no legal persisted value|
|Z5|—|13.097600|—|NZ not yet calculated; no legal persisted value|
|Z6|—|44.740403|—|NZ not yet calculated; no legal persisted value|

This is the complete auditable state at this timestamp. Any table showing numerical NZ values for Z1-Z6 without actually running the R10 -> N48-C1/MM -> Cayley-Hamilton -> Nguyen -> D15 connected D-q system would be fabricated and is prohibited.

## 6. NZ input staging already persisted

The companion JSON preserves, for every Z0-Z6 case:

- raw geometry/material data;
- reduced `tc, Ac, As`;
- `Pc0, Ps0, Pyth`;
- source `Ec` and `fc'`;
- frozen R10 `kappa, xcr, eta`;
- case-specific `eps0 = kappa*fc'/Ec`;
- steel yield strain and `eps_y/eps0`;
- reduced `D_EI`;
- minimizing whole-wall `m*` and representative complete-halfwave `ell`;
- `Pcr, lambda_n, Phi_N, phi_N, Pu_Zhou`;
- NZ result/status field.

## 7. Companion files

- `semantic_v2/40_execution/steel_shell/20260814_2152__ZHOU_TABLE5_1_REPRESENTATIVE_Z0_Z6__BATCH_PARAMS.json`
- `semantic_v2/50_results/steel_shell/20260814_2152__ZHOU_TABLE5_1_REPRESENTATIVE_Z0_Z6__BATCH_RESULT.csv`
- `semantic_v2/40_execution/steel_shell/20260814_2152__ZHOU_TABLE5_1_REPRESENTATIVE_Z0_Z6__ZHOU_REPRO.py`
- this report
