# NZ-SCCM — Zhang 2023 peak-anchored exact strain-compatible UHPC `Ny-My` terminal R14

**Date:** 2026-08-24 11:51 +08:00  
**Status:** `EXECUTED / ZERO_THICKNESS_QUADRATURE / PHYSICAL_PEAK_BACKBONE_REINSERTED / PRIMARY6_BIAS_RESOLVED / STRUCTURAL_FRONT_UNCHANGED`

## 0. Governing decision inherited from R13

R13 separates the FHWA `alpha_u=0.85` compression **design** idealization from the project physical peak-response terminal.

R14 therefore makes one and only one material change relative to R11/R12:

```text
R11/R12 UHPC COMPRESSION = FHWA elastic -> 0.85fc design plateau
R14 UHPC COMPRESSION = Zhang-2023 zero-confinement ascending physical backbone
```

Everything else is frozen:

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
Nx_Mx_IN_STRUCTURAL_FIELD = YES
Nx_Mx_HARD_TERMINAL_ON_Y_CUT = NO
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
```

---

## 1. Peak-anchored plane-section kinematics

Use the same section coordinates as R11:

- top external steel face: `-ts <= y <= 0`;
- UHPC core + distributed longitudinal web: `0 <= y <= tc`;
- bottom external steel face: `tc <= y <= tc+ts`;
- moment datum: UHPC-core mid-plane `z=tc/2-y`.

The common section strain field is

\[
\boxed{
\varepsilon(y)=\varepsilon_{c0}-\kappa y,
\qquad
\varepsilon_{c0}=0.0035.
}
\]

The extreme compression UHPC fibre is therefore exactly at the Zhang uniaxial peak.

This is a **first-attainment-of-material-peak** terminal. It does not use Zhang post-peak softening to prolong capacity, because the current mainline explicitly has no load-path/post-peak continuation state machine.

For every R14 root obtained below,

\[
\varepsilon(t_c)>0,
\]

so the entire UHPC core remains in compression and Hiew tension remains inactive.

---

## 2. Zhang zero-confinement compression law

Current material values:

\[
f_c=141.1\ \mathrm{MPa},
\qquad
E_c=43.4\ \mathrm{GPa},
\qquad
\varepsilon_{c0}=0.0035,
\qquad
V_f=0.02.
\]

Let

\[
x=\varepsilon/\varepsilon_{c0},
\qquad
\kappa_U=E_c\varepsilon_{c0}/f_c=1.07654145996,
\]

\[
r=\frac{\kappa_U}{\kappa_U-1}=14.0648148148.
\]

For the R14 active range `0<=x<=1`,

\[
\boxed{
 g_a(x)=\frac{r x}{r-1+x^r},
 \qquad
 \sigma_c=f_c g_a(x).
}
\]

It exactly satisfies

\[
\sigma_c(0)=0,
\qquad
\frac{d\sigma_c}{d\varepsilon}(0)=E_c,
\qquad
\sigma_c(\varepsilon_{c0})=f_c,
\qquad
\frac{d\sigma_c}{d\varepsilon}(\varepsilon_{c0})=0.
\]

The source-retained descending branch is not deleted; it is simply not activated in this first-peak terminal.

---

## 3. Exact zero-quadrature UHPC primitives

Let

\[
A=r-1,
\]

\[
I_m(x)=
\frac{x^{m+1}}{(m+1)A}
{}_2F_1\left(1,\frac{m+1}{r};1+\frac{m+1}{r};-\frac{x^r}{A}\right).
\]

Then

\[
F_0(x)=\int g_a(x)dx=rI_1(x),
\]

\[
F_1(x)=\int xg_a(x)dx=rI_2(x).
\]

For

\[
\hat\kappa=\kappa/\varepsilon_{c0},
\qquad
x_b=1-\hat\kappa t_c,
\]

the exact UHPC core resultant is

\[
\boxed{
N_c=(1-\rho_w)f_c\frac{F_0(1)-F_0(x_b)}{\hat\kappa},
}
\]

and its first moment about the core mid-plane is obtained from the same finite endpoint pair:

\[
\boxed{
M_c=\frac{t_c}{2}N_c
-(1-\rho_w)f_c
\frac{[F_0(1)-F_0(x_b)]-[F_1(1)-F_1(x_b)]}{\hat\kappa^2}.
}
\]

No thickness Gauss points, material fibres, or numerical quadrature are present.

The distributed web and two external steel faces retain exact clipped-affine primitives from R11.

---

## 4. Coupling to the unchanged Marguerre–Airy demand

For each case,

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P(q)}b+Gq(q+2q_0)(1-2s^2),
\]

\[
m(s;q)=J_yqs,
\qquad q_0=0.0025.
\]

At a candidate control location,

\[
\boxed{N_u(\kappa)=n(s;q)},
\qquad
\boxed{M_u(\kappa)=m(s;q)}.
\]

Formal control candidates remain:

1. `s=0`;
2. `s=1`;
3. interior stationary roots satisfying

\[
\boxed{
-4Gq(q+2q_0)s\,M_{u,\kappa}
-J_yq\,N_{u,\kappa}=0.
}
\]

The code evaluates `N_{u,kappa}` and `M_{u,kappa}` analytically from the same endpoint primitives and exact elastic steel subintervals.

---

## 5. Finite control-location audit

For every current case:

- the `s=0` pure-axial candidate occurs after the `s=1` root;
- deterministic multi-seed solution of the finite interior stationarity equations finds no admissible `0<s<1` stationary root preceding `s=1`;
- therefore the controlling location remains

\[
\boxed{s=1.}
\]

The `s=0` candidates are:

|Case|`s=0` Pu / MN|`s=1` R14 Pu / MN|
|---|---:|---:|
|T120|14.677083|12.252165|
|T360|13.521630|11.133265|
|BH005|2.476251|2.422373|
|BH010|4.666474|4.462040|
|BH020|9.036815|8.155352|
|BH032|13.452514|11.163056|
|BH050|18.062894|13.650448|

---

## 6. R14 roots

|Case|`q_u`|`kappa_u` / mm^-1|`n_u` N/mm|`M_u` N|`Pu_R14` MN|bottom-core strain|
|---|---:|---:|---:|---:|---:|---:|
|T120|0.001631860743|4.831527470e-5|7599.0290|18253.8749|**12.252164525**|0.00147076|
|T360|0.001406053484|4.982350755e-5|6912.5808|15399.8463|**11.133264739**|0.00140741|
|BH005|3.103538185e-5|1.406759438e-5|9688.6546|2094.0503|**2.422372923**|0.00290916|
|BH010|0.0001188132600|2.033014987e-5|8921.1442|3860.9557|**4.462040087**|0.00264613|
|BH020|0.0004977063181|3.451133415e-5|8142.8733|7932.4433|**8.155351621**|0.00205052|
|BH032|0.001420886996|4.915344503e-5|6936.2171|14051.0094|**11.163055965**|0.00143556|
|BH050|0.005045738449|6.856127101e-5|5237.1412|31793.1980|**13.650448214**|0.00062043|

Every bottom-core strain is positive; UHPC tension is therefore inactive at all R14 roots.

---

## 7. Comparator opened only after all R14 roots were fixed

|Case|R10-A rigid `0.85fc` MN|R11/R12 exact FHWA design MN|R14 Zhang physical peak MN|Comparator MN|R14 error|
|---|---:|---:|---:|---:|---:|
|T120|12.35805|11.78605|**12.25216**|12.6378|-3.051%|
|T360|11.28503|10.65015|**11.13326**|10.9688|+1.499%|
|BH005|2.28262|2.25204|**2.42237**|2.3558|+2.826%|
|BH010|4.18068|4.13093|**4.46204**|4.3043|+3.665%|
|BH020|7.89446|7.66341|**8.15535**|8.0076|+1.845%|
|BH032|11.28878|10.66798|**11.16306**|10.9905|+1.570%|
|BH050|14.60588|13.25612|**13.65045**|12.2198*|+11.708%|

`*` BH050 retains the pre-existing lower-confidence comparator identity and is excluded from primary-six statistics.

### Primary six statistics

R10-A design screening block:

```text
mean signed = -0.668 percent
MAE = 2.534 percent
RMSE = 2.597 percent
```

R11/R12 exact FHWA compression-design section:

```text
mean signed = -4.218 percent
MAE = 4.218 percent
RMSE = 4.408 percent
```

R14 Zhang physical peak-anchored section:

\[
\boxed{\text{mean signed}=+1.392\%},
\]

\[
\boxed{MAE=2.409\%,\qquad RMSE=2.544\%}.
\]

Thus the R11/R12 systematic low bias disappears when the source role is corrected without changing the structural mechanics.

R14 also slightly improves the primary-six MAE/RMSE relative to the R10-A `0.85fc` screening block, while avoiding the need to interpret a design reduction plateau as the actual physical UHPC compression law.

---

## 8. Interpretation

The important result is not merely that R14 has smaller error. The source-role sequence is mechanically coherent:

1. R08 full-`fc` arbitrary plastic allocation was too generous.
2. R10-A showed that the source-specified FHWA design reduction has the correct scale.
3. R11 enforced the actual FHWA design stress–strain idealization and became systematically conservative against physical comparators.
4. R12 proved that omitted UHPC tension cannot explain that low bias because the whole core remains compressed.
5. R13 showed from the official source that the FHWA curve is explicitly a **compression design model**.
6. R14 restores the source-registered Zhang physical compression backbone under exactly the same strain-compatible `Ny-My` architecture and removes the systematic low bias.

Therefore the current evidence supports retaining:

\[
\boxed{
\text{Marguerre–Airy demand}
\rightarrow
\text{strain-compatible }N_y-M_y\text{ section terminal}
}
\]

without reopening the structural front.

---

## 9. What R14 does not authorize

R14 does **not** yet authorize:

- generic Liu/Leutbecher TC softening on every case;
- Zhang post-peak section continuation;
- a new fitted compression factor;
- comparator-based choice of material branch;
- material-point integration;
- numerical thickness quadrature.

The primary-six mean has now moved from `-4.218%` to `+1.392%`. A blanket TC reduction could improve some positive-bias cases but would worsen T120, which is already `-3.05%`. Therefore TC can only be reconsidered through an explicit case/state activation gate derived from the transverse Airy state, not as a universal multiplicative correction.

---

## 10. Decision

```text
R13_FHWA_DESIGN_VS_PHYSICAL_ROLE = CLOSED
R14_ZHANG_PEAK_STRAIN_COMPATIBLE_Ny_My = EXECUTED
R14_ZERO_THICKNESS_QUADRATURE = PASS
R14_MATERIAL_POINTS = 0
R14_CONTROL_LOCATION = s=1 FOR ALL 7
R14_INTERIOR_STATIONARY_PRECEDENCE = NONE_FOUND
R14_PRIMARY6_MEAN = +1.392 percent
R14_PRIMARY6_MAE = 2.409 percent
R14_PRIMARY6_RMSE = 2.544 percent

MARGUERRE_AIRY_STRUCTURAL_FRONT = RETAIN
Ny_My_TERMINAL_IDENTITY = RETAIN
FHWA_R11_R12 = DESIGN_BASELINE / NOT PHYSICAL PRODUCTION TERMINAL
ZHANG_R14 = CURRENT PHYSICAL PEAK-TERMINAL CANDIDATE
ZHANG_POSTPEAK_CONTINUATION = DEFER
BLANKET_TC_SOFTENING = NOT AUTHORIZED
NEW_FITTED_FACTOR = NO

NEXT = TRANSVERSE_AIRY_STATE_TO_TC_ACTIVATION_AUDIT_BEFORE_ANY_TC_REDUCTION
```
