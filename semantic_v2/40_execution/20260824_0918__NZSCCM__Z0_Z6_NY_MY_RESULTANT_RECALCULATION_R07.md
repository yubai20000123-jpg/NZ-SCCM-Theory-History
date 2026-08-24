# NZ-SCCM — Z0–Z6 selected `Ny-My` resultant-terminal recalculation R07

**Date:** 2026-08-24 09:18 +08:00  
**Status:** `EXECUTED / Z_RESULTANT_BASELINE_REPRODUCED / Z3_COEFFICIENT_PROVENANCE_DELTA_EXPOSED`

## 0. Locked architecture

Structural front remains the frozen full 2D Marguerre–Airy field. The terminal object is the axial y-normal local section cut:

\[
\boxed{(N_y,M_y)}.
\]

`Nx` and `Mx` remain in the full 2D structural solution but are not imposed as independent hard equalities on this terminal cut.

No Zhou/Winter value is used in mode selection, coefficient generation, root solution, or control-location selection.

---

## 1. Input and elastic front

Common:

\[
a_{phys}=2b,\quad t_s=4\ \mathrm{mm/face},\quad \rho_w=0.02,
\]
\[
E_s=206000\ \mathrm{MPa},\quad q_0=0.004.
\]

The integer elastic-front scan gives for all Z0–Z6:

\[
\boxed{m_*=2,\qquad \ell=b,\qquad \alpha=\beta=\pi/b}.
\]

The structural law is

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m(s;q)=J_yqs.
\]

---

## 2. Finite steel-shell concrete `N-M` capacity

Compression is positive. Define

\[
h_c=t_c/2,\qquad z_f=h_c+t_s/2,
\]
\[
a_c=(1-\rho_w)f_c,
\]
\[
N_0=(a_c+\rho_wf_y)t_c,
\qquad
N_p=N_0+2f_yt_s.
\]

For `0 <= n <= N0`, the neutral axis lies in the core:

\[
z_n=\frac{a_ch_c-n}{a_c+2\rho_wf_y},
\]

\[
M_u^A(n)=
\frac{a_c+2\rho_wf_y}{2}h_c^2
-\frac{(a_ch_c-n)^2}{2(a_c+2\rho_wf_y)}
+2f_yt_sz_f.
\]

For `N0 <= n <= Np`, let

\[
x=\frac{n-N_0}{2f_y},
\]

then

\[
\boxed{
M_u^B(n)=f_y[(h_c+t_s)^2-(h_c+x)^2].
}
\]

This is the same finite plastic resultant envelope previously embedded in the explicit Z theory. No pointwise concrete strain/stress field or thickness quadrature is used.

The ultimate candidate satisfies

\[
M_u[n(s,q)]-J_yqs=0.
\]

Finite candidates are the spatial endpoints plus stationary interior roots; the minimum positive admissible `q` is selected without comparator information.

---

## 3. Forward-regenerated structural coefficients

Using the current raw material inputs and current stiffness formulas gives:

|Case|m*|ell mm|Pcr MN|C MN|G N/mm|Jy N|
|---|---:|---:|---:|---:|---:|---:|
|Z0|2|6000|78.306708780|43035.7987291|7.469209326e6|2.483849043e7|
|Z1|2|6000|40.350205992|35478.2371349|6.135882615e6|1.277558082e7|
|Z2|2|6000|78.306708780|43035.7987291|7.469209326e6|2.483849043e7|
|Z3|2|6000|**81.797439948**|**46129.6231949**|7.985091427e6|2.586090719e7|
|Z4|2|8000|179.754773113|80875.4296536|1.057837757e7|5.709644703e7|
|Z5|2|2000|231.788407677|14345.2662430|7.469209326e6|7.451547130e7|
|Z6|2|12000|39.288014715|86071.5974582|7.469209326e6|1.241924522e7|

### Z3 provenance note

The 2026-08-22 reproduction kernel carried the same current raw Z3 input

\[
E_c=35992.801439712057\ \mathrm{MPa},
\]

but also stored older rounded/pre-generated structural constants

\[
P_{cr}=81.78821\ \mathrm{MN},\qquad C=46121.44731\ \mathrm{MN}.
\]

Forward regeneration from the raw input produces the table above. The difference is only about `0.01%`, but R07 uses the forward-regenerated values rather than silently mixing raw inputs with older hard-coded coefficients.

```text
Z3_RAW_INPUT = RETAINED
Z3_OLD_HARDCODED_Pcr_C = NOT_USED_IN_R07
Z3_FORWARD_REGENERATED_COEFFICIENTS = USED
```

---

## 4. R07 ultimate roots

|Case|control s|q_u|n_u N/mm|Pu MN|capacity branch|
|---|---:|---:|---:|---:|---|
|Z0|1.000000|0.003428230723|6011.6512|**37.825706787**|B|
|Z1|0.840294805|0.004996679885|3954.7775|**24.714128548**|B|
|Z2|1.000000|0.004321772846|6762.0856|**42.959011131**|B|
|Z3|1.000000|0.004613406152|7284.6167|**46.495651955**|B|
|Z4|1.000000|0.002445428167|8513.0056|**70.265718566**|B|
|Z5|1.000000|0.000258841897|7043.1296|**14.118193577**|B|
|Z6|0.298387170|0.013807412938|6546.8131|**56.379421090**|B|

The pure-compression `s=0` squash candidates occur later than the reported controlling roots for all seven cases.

Except for the deliberately exposed tiny Z3 coefficient provenance difference, R07 reproduces the historical explicit `Ny-My` Z baseline.

---

## 5. Comparator opened only after predictions were fixed

|Case|R07 Pu MN|Zhou MN|error vs Zhou|Winter MN|error vs Winter|
|---|---:|---:|---:|---:|---:|
|Z0|37.82571|36.9455|+2.382%|41.5008|−8.855%|
|Z1|24.71413|23.7214|+4.185%|26.1001|−5.310%|
|Z2|42.95901|41.2134|+4.236%|45.7333|−6.066%|
|Z3|46.49565|44.3203|+4.908%|49.0469|−5.202%|
|Z4|70.26572|69.3399|+1.335%|79.3861|−11.489%|
|Z5|14.11819|14.6816|−3.838%|14.6816|−3.838%|
|Z6|56.37942|49.4868|+13.928%|50.1859|+12.341%|

Against Zhou:

\[
\text{mean signed}=+3.877\%,\qquad MAE=4.973\%.
\]

Against Winter:

\[
\text{mean signed}=-4.060\%,\qquad MAE=7.586\%.
\]

No correction is applied to Z6 here. The previously attempted 2D TC re-cut belongs to a different material-capacity gate and is not part of the selected pure `Ny-My` resultant baseline.

---

## 6. Decision

```text
Z0_Z6_NY_MY_RESULTANT_RECALCULATION = EXECUTED
Z0_Z6_STRUCTURAL_MODE = m=2 / ell=b
Z0_Z6_RESULTANT_CAPACITY = FINITE_CLOSED_FORM
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
COMPARATOR_IN_ROOT_SELECTION = 0
Z_BASELINE_REPRODUCTION = PASS
Z6_HIGH_BIAS = RETAINED_AS_VALIDATION_SIGNAL
```

Proceed to steel-shell UHPC with the same resultant-allocation architecture, without tuning the Z family.