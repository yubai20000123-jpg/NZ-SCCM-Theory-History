# NZ-SCCM — steel-shell UHPC `Ny-My` resultant baseline R08

**Date:** 2026-08-24 09:35 +08:00  
**Status:** `EXECUTED / RESULTANT_BASELINE_COMPLETE / UHPC_TERMINAL_VALIDATION_FAILS_HIGH-BIAS GATE`

## 0. Purpose

R08 applies the same axial y-normal resultant-terminal architecture used in the RC R03/R05 branch and Z R07 to steel-shell UHPC.

This is intentionally a **resultant-only terminal baseline**. It does not restore pointwise UHPC material states, thickness quadrature, Zhang/Hiew strain integration, or Liu CC/TC material-point gates.

The purpose is to test whether the common resultant capacity architecture itself transfers across material families before any further terminal-law refinement.

---

## 1. Structural front

For every case:

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]
\[
n(s;q)=\frac{P(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m(s;q)=J_yqs.
\]

with

\[
q_0=0.0025.
\]

### T120/T360 physical-length correction

R06 has locked

\[
b=1600\ \mathrm{mm},\qquad a_{phys}=3000\ \mathrm{mm},
\]

and the independent elastic scan gives

\[
\boxed{m_*=2,\qquad \ell=1500\ \mathrm{mm}}.
\]

The old 1600-mm axial analytical length is not used in R08.

The resulting R08 structural coefficients are:

|Case|Pcr MN|C MN|G N/mm|Jy N|
|---|---:|---:|---:|---:|
|T120|30.822799056|7284.21452557|5.412338111e6|1.118592686e7|
|T360|30.751943803|7055.99557435|5.074760452e6|1.095253234e7|

### BH005–BH050

The current 37-mm web rebase is retained:

\[
A_{w,total}=9\times4\times37=1332\ \mathrm{mm^2},
\qquad
\rho_w=\frac{1332}{42B}.
\]

The already-regenerated 37-mm structural coefficients are used without comparator-based modification:

|Case|Pcr MN|C MN|G N/mm|Jy N|
|---|---:|---:|---:|---:|
|BH005|197.5373|1179.2700|5.3614e6|6.7473e7|
|BH010|98.3195|2253.6479|4.8274e6|3.2496e7|
|BH020|49.0475|4400.9325|4.5604e6|1.5938e7|
|BH032|30.6284|6977.1939|4.4603e6|9.8889e6|
|BH050|19.5920|10841.3718|4.4002e6|6.3010e6|

All BH cases have `m*=2` and representative complete halfwave `ell=B`.

---

## 2. Common resultant capacity law

Per unit width, compression is positive. Let

\[
h_c=t_c/2,
\]

and define the admissible longitudinal stress-resultant densities:

### UHPC core

\[
0\le r_c(z)\le (1-\rho_w)f_c.
\]

### longitudinal web steel

\[
-\rho_wf_y\le r_w(z)\le +\rho_wf_y.
\]

### each external steel face

\[
-f_y\le r_f(z)\le f_{c,s},
\]

where `f_c,s` is the current compression cap of that steel-face local branch.

Define

\[
w_f=f_{c,s}+f_y,
\qquad
w_c=(1-\rho_w)f_c+2\rho_wf_y,
\]

\[
N_L=-\rho_wf_yt_c-2f_yt_s,
\qquad
\Delta=n-N_L.
\]

Maximizing positive bending moment at fixed `n` is a finite bounded-resultant allocation problem: starting from the lower bounds, allocate `Delta` from the largest `z` downward.

### Stage I — top face

For

\[
0\le\Delta\le w_ft_s,
\]

\[
x=\Delta/w_f,
\]

\[
M_u=
\frac{w_f}{2}
[(h_c+t_s)^2-(h_c+t_s-x)^2].
\]

### Stage II — core + web

Let

\[
M_1=w_ft_s(h_c+t_s/2),
\]

and

\[
\Delta_2=\Delta-w_ft_s.
\]

For

\[
0\le\Delta_2\le w_ct_c,
\]

\[
x=\Delta_2/w_c,
\]

\[
M_u=M_1+rac{w_c}{2}[h_c^2-(h_c-x)^2].
\]

### Stage III — bottom face

For

\[
\Delta_3=\Delta-w_ft_s-w_ct_c,
\qquad
0\le\Delta_3\le w_ft_s,
\]

\[
x=\Delta_3/w_f,
\]

\[
\boxed{
M_u=M_1+rac{w_f}{2}[h_c^2-(h_c+x)^2].
}
\]

The upper axial bound is

\[
N_U=(1-\rho_w)f_ct_c+\rho_wf_yt_c+2f_{c,s}t_s.
\]

This finite allocation law exactly reduces to the Z R07 two-regime plastic envelope when `f_c,s=fy`.

No material points or thickness quadrature are introduced.

---

## 3. R08 material/resultant inputs

UHPC and steel:

\[
f_c=141.1\ \mathrm{MPa},\quad t_c=42\ \mathrm{mm},
\]
\[
f_y=355\ \mathrm{MPa},\quad t_s=4\ \mathrm{mm/face}.
\]

Current web fractions:

|Case|rho_w|
|---|---:|
|T120|0.05506|
|T360|0.01982|
|BH005|0.12685714|
|BH010|0.06342857|
|BH020|0.03171429|
|BH032|0.01982143|
|BH050|0.01268571|

Steel-face compression caps are frozen before opening FEM comparators:

|Case|f_c,s MPa|identity|
|---|---:|---|
|T120|355.000|yield before local buckling|
|T360|301.87133|current Yun local-postbuckling cap|
|BH005|355.000|yield before local buckling|
|BH010|355.000|yield before local buckling|
|BH020|355.000|yield before local buckling|
|BH032|295.42|current Yun local-postbuckling working cap|
|BH050|250.07|current Yun local-postbuckling working cap|

No cap is adjusted using Abaqus peak load.

---

## 4. R08 roots

For all seven current UHPC cases, the minimum admissible resultant root occurs at

\[
\boxed{s=1}
\]

and on capacity allocation Stage III.

|Case|q_u|n_u N/mm|M_u N|Pu MN|
|---|---:|---:|---:|---:|
|T120|0.001927917118|8376.1803|21565.5399|**13.517551912**|
|T360|0.001695227167|7758.9490|18567.0304|**12.506475456**|
|BH005|0.000031463802|9820.7368|2122.9571|**2.455396391**|
|BH010|0.000122376977|9176.2399|3976.7622|**4.589632993**|
|BH020|0.000539392342|8703.8443|8596.8352|**8.717470347**|
|BH032|0.001710760341|7776.2310|16917.5379|**12.523899913**|
|BH050|0.007797578630|5927.8650|49132.5429|**15.917403879**|

These are the predictions frozen before the FEM comparator table below is opened.

---

## 5. Comparator opened only after R08 predictions were fixed

|Case|R08 Pu MN|Abaqus comparator MN|R08 error|
|---|---:|---:|---:|
|T120|13.51755|12.6378|+6.961%|
|T360|12.50648|10.9688|+14.019%|
|BH005|2.45540|2.3558|+4.228%|
|BH010|4.58963|4.3043|+6.629%|
|BH020|8.71747|8.0076|+8.865%|
|BH032|12.52390|10.9905|+13.952%|
|BH050|15.91740|12.2198*|+30.259%|

`*` BH050 comparator remains lower-confidence because it belongs to a different diagnostic model family.

For the six higher-confidence comparators T120/T360/BH005–BH032:

\[
\boxed{\text{mean signed error}=+9.109\%},
\]

\[
\boxed{MAE=9.109\%,\qquad RMSE=9.832\%}.
\]

All six errors are positive.

---

## 6. Interpretation

This is an informative failure, not a solver failure.

The common finite resultant architecture is fully calculable for steel-shell UHPC, but the simplest UHPC rectangular compression block

\[
0\le r_c\le(1-\rho_w)f_c
\]

is systematically too generous relative to the higher-confidence FEM comparators, especially when local/global stability becomes more important.

The trend is:

- BH005: +4.23%;
- BH010: +6.63%;
- BH020: +8.86%;
- BH032: +13.95%.

T360 is likewise much more overpredicted than T120 despite the Yun compression cap already being retained.

Therefore the remaining discrepancy cannot be removed merely by saying `steel local buckling was omitted`; the current local steel cap is already active in T360/BH032/BH050.

The first suspect is the **UHPC resultant compression-block law / attainable stress distribution**, not the Marguerre–Airy structural front and not a need to restore material-point quadrature.

No parameter is modified in R08.

---

## 7. Decision

```text
STEEL_SHELL_UHPC_NY_MY_RESULTANT_BASELINE = EXECUTED
T120_T360_PHYSICAL_LENGTH = 3000 mm
T120_T360_MODE = m=2 / ell=1500 mm
BH_37MM_WEB = RETAINED
LOCAL_STEEL_POSTBUCKLING_CAPS = RETAINED
MATERIAL_POINTS = 0
THICKNESS_QUADRATURE = 0
COMPARATOR_IN_ROOT_SELECTION = 0

CALCULABILITY_GATE = PASS
TRANSFER_ACCURACY_GATE = FAIL_HIGH_BIAS
FAILURE_LOCATION = UHPC_RESULTANT_TERMINAL_LAW_FIRST
STRUCTURAL_FRONT_REOPEN = NO
PARAMETER_TUNING = NOT_PERFORMED
```

The next step must be a cross-family diagnosis of the resultant capacity law, not a return to pointwise material-state integration.