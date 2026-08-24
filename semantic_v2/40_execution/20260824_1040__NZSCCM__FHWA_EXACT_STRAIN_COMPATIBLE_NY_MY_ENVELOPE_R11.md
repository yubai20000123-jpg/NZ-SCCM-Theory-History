# NZ-SCCM — FHWA exact strain-compatible UHPC `Ny-My` envelope R11

**Date:** 2026-08-24 10:40 +08:00  
**Status:** `EXECUTED / ZERO_THICKNESS_QUADRATURE / STRAIN_COMPATIBLE_SECTION_ENVELOPE_COMPLETE / COMPRESSION_ONLY_UHPC_IS_CONSERVATIVE`

## 0. Locked architecture

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
Nx_Mx_IN_STRUCTURAL_FIELD = YES
Nx_Mx_HARD_TERMINAL_ON_Y_CUT = NO
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
COMPARATOR_IN_ROOT_SELECTION = 0
```

R11 executes the R10 next task: replace the reduced rectangular UHPC compression block by the exact FHWA compression design diagram under plane-section strain compatibility, while keeping the current no-UHPC-tension terminal so that the compression-model effect is isolated.

## 1. Source identity

FHWA-HRT-23-077 defines the UHPC compression design model by `Ec`, `fc`, `epsilon_cu`, and the reduction factor `alpha_u <= 0.85`. The response is elastic until `alpha_u fc` at

\[
\varepsilon_{cp}=\alpha_u f_c/E_c,
\]

then sustains that reduced compressive resistance until `epsilon_cu`. Without a physical test value, the project uses

\[
\alpha_u=0.85,\qquad \varepsilon_{cu}=0.0035.
\]

For the current material

\[
f_c=141.1\ \mathrm{MPa},\qquad E_c=43400\ \mathrm{MPa},
\]

so

\[
\sigma_p=0.85f_c=119.935\ \mathrm{MPa},
\qquad
\varepsilon_{cp}=0.002763479263.
\]

FHWA also requires strain compatibility for nominal flexural resistance and its worked example uses an elastic-perfectly-plastic model for reinforcing steel. R11 therefore uses one linear axial strain field through the complete steel-shell/UHPC section.

The existing Yun local-postbuckling compression caps for T360/BH032/BH050 are retained as project steel-face caps; they are not FHWA parameters.

## 2. Exact section kinematics

Let `y=0` be the top UHPC-core surface, positive downward. Then

- top external steel face: `-ts <= y <= 0`;
- UHPC core + distributed longitudinal web: `0 <= y <= tc`;
- bottom external steel face: `tc <= y <= tc+ts`;
- moment datum: core mid-plane `z=tc/2-y`.

For the positive bending-capacity branch, the extreme compression fiber of the UHPC core reaches the FHWA limit:

\[
\boxed{\varepsilon(y)=\varepsilon_{cu}-\kappa y},\qquad \kappa\ge0.
\]

This is the compression-controlled strain-compatible envelope. UHPC tension is deliberately set to zero in R11 to isolate the compression-model replacement; adding the already-source-supported UHPC tensile branch is a separate later refinement.

## 3. Exact clipped affine stress laws

UHPC core, after web-volume subtraction:

\[
\boxed{\sigma_c(y)=(1-\rho_w)\,\operatorname{clip}\!\left(E_c\varepsilon(y),0,\alpha_u f_c\right)}.
\]

Distributed longitudinal web:

\[
\boxed{\sigma_w(y)=\rho_w\,\operatorname{clip}\!\left(E_s\varepsilon(y),-f_y,+f_y\right)}.
\]

Each external steel face:

\[
\boxed{\sigma_f(y)=\operatorname{clip}\!\left(E_s\varepsilon(y),-f_y,f_{c,s}\right)}.
\]

Here `f_c,s=fy` when yielding precedes local buckling; otherwise the frozen Yun local compression cap is used.

## 4. Zero-quadrature primitive

For any interval `[u,v]` on which the clipped stress is affine,

\[
\sigma(y)=A+By,
\]

its exact resultant and moment are

\[
\boxed{N=A(v-u)+\frac{B}{2}(v^2-u^2)},
\]

\[
\boxed{
M=\frac{t_c}{2}N
-\frac{A}{2}(v^2-u^2)
-\frac{B}{3}(v^3-u^3).
}
\]

The only breakpoints are where the linear trial stress reaches the finite clip values. For a threshold stress `sigma_*`,

\[
y_*=\frac{\varepsilon_{cu}-\sigma_*/E}{\kappa}.
\]

Therefore every phase integral is a finite sum of polynomial expressions; no thickness integration points are required.

Summing top face + UHPC + web + bottom face gives the parametric exact section envelope

\[
\boxed{N_u=N_u(\kappa),\qquad M_u=M_u(\kappa)}.
\]

On the positive-compression branch used by all seven current cases, `N_u(kappa)` was audited as monotone non-increasing, so `kappa` is uniquely determined by a prescribed `Ny` demand.

## 5. Coupling to Marguerre-Air y demand

The unchanged structural demand is

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P(q)}b+Gq(q+2q_0)(1-2s^2),
\]

\[
m(s;q)=J_yqs.
\]

The exact terminal equations are

\[
\boxed{N_u(\kappa)=n(s;q)},
\qquad
\boxed{M_u(\kappa)=J_yqs}.
\]

The finite control-location audit includes `s=0`, `s=1`, and interior stationary candidates. For an interior candidate, implicit differentiation gives

\[
\frac{dM_u}{dN_u}=\frac{M_{u,\kappa}}{N_{u,\kappa}},
\]

and the stationarity condition is

\[
\boxed{
-4Gq(q+2q_0)s\,M_{u,\kappa}
-J_yq\,N_{u,\kappa}=0.
}
\]

Because the clipped laws are continuous, their derivatives are also exact finite integrals over only the currently elastic subintervals. No spatial sampling is part of the formal candidate set.

For all seven R11 cases, no admissible interior stationary root precedes the endpoint root and the control is

\[
\boxed{s=1}.
\]

## 6. R11 roots

|Case|q_u|kappa 1/mm|n_u N/mm|M_u N|Pu MN|
|---|---:|---:|---:|---:|---:|
|T120|0.001532358583|4.979774776e-5|7312.1069|17140.8510|**11.78605439**|
|T360|0.001313428141|5.145272562e-5|6614.2643|14385.3642|**10.65015268**|
|BH005|2.882786183e-5|2.758413669e-5|9007.3651|1945.1023|**2.25203558**|
|BH010|0.0001096102950|3.239444538e-5|8259.1608|3561.8961|**4.13093221**|
|BH020|0.0004621488904|4.119300501e-5|7651.8960|7365.7290|**7.66340795**|
|BH032|0.001324938066|5.086216664e-5|6630.1118|13102.1800|**10.66798371**|
|BH050|0.004675216556|6.855138326e-5|5103.4109|29458.5395|**13.25612091**|

The `s=0` pure-axial candidates all occur later than the `s=1` roots.

## 7. Section-state interpretation

At every R11 root the complete UHPC core remains in compression. The top portion is on the FHWA `0.85fc` plateau and the lower portion remains elastic. Representative plateau depths and bottom-core stresses are:

|Case|plateau depth mm|bottom core strain|bottom UHPC stress MPa|
|---|---:|---:|---:|
|T120|14.790|0.0014085|61.13|
|T360|14.315|0.0013390|58.11|
|BH005|26.701|0.0023415|101.62|
|BH010|22.736|0.0021394|92.85|
|BH020|17.880|0.0017699|76.81|
|BH032|14.481|0.0013638|59.19|
|BH050|10.744|0.0006208|26.94|

Thus the exact FHWA envelope is materially different from a rigid `0.85fc` rectangle even though both share the same plateau stress.

BH005 is especially informative: both external faces and the distributed web are already in longitudinal compression, so its positive moment capacity is generated mainly by the UHPC stress gradient rather than by an arbitrary plastic redistribution.

## 8. Comparator opened only after roots were fixed

|Case|R08 full-fc MN|R10-A 0.85 rectangle MN|R11 exact strain-compatible MN|Abaqus MN|R11 error|
|---|---:|---:|---:|---:|---:|
|T120|13.51755|12.35805|**11.78605**|12.6378|-6.740%|
|T360|12.50648|11.28503|**10.65015**|10.9688|-2.905%|
|BH005|2.45540|2.28262|**2.25204**|2.3558|-4.405%|
|BH010|4.58963|4.18068|**4.13093**|4.3043|-4.028%|
|BH020|8.71747|7.89446|**7.66341**|8.0076|-4.298%|
|BH032|12.52390|11.28878|**10.66798**|10.9905|-2.935%|
|BH050|15.91740|14.60588|**13.25612**|12.2198*|+8.481%|

`*` BH050 comparator retains its lower-confidence identity and is excluded from the primary six-case statistics.

For T120/T360/BH005/BH010/BH020/BH032:

### R08 full-fc rectangle

`mean = +9.109%`, `MAE = 9.109%`, `RMSE = 9.832%`.

### R10-A rigid 0.85 rectangle

`mean = -0.668%`, `MAE = 2.534%`, `RMSE = 2.597%`.

### R11 exact FHWA compression + full steel strain compatibility, UHPC tension suppressed

\[
\boxed{\text{mean signed}=-4.218\%},
\]

\[
\boxed{MAE=4.218\%,\qquad RMSE=4.408\%}.
\]

R11 is substantially better than the old full-`fc` plastic upper bound but more conservative than the simple R10-A screening rectangle.

## 9. Interpretation and next gate

R11 shows that the attractive R10-A accuracy cannot by itself justify a rigid `0.85fc` plastic block as the final physical terminal. Once the actual FHWA strain-compatible compression diagram and steel strain compatibility are enforced, the six higher-confidence predictions all move to the low side by roughly 3–7%.

This does **not** justify restoring the full-`fc` rectangle or fitting a new compression factor.

The most direct missing source-supported mechanism is now visible: FHWA strain compatibility at nominal flexural strength includes UHPC tensile stress up to the applicable tensile strain/localization limit, whereas R11 deliberately sets UHPC tension to zero to isolate the compression refinement. The project already has a source-qualified UHPC tension branch. Therefore adding a finite analytic UHPC tensile resultant is a cleaner next refinement than immediately applying an additional TC compression-softening reduction to an already conservative compression-only envelope.

The Liu/Leutbecher TC softening gate remains relevant, but it should be tested **after** the two-sided strain-compatible UHPC resultant envelope is closed, otherwise tension omission and TC compression softening would be conflated.

## 10. Decision

```text
FHWA_EXACT_COMPRESSION_DIAGRAM = PASS
FULL_SECTION_STRAIN_COMPATIBILITY = PASS
ZERO_THICKNESS_QUADRATURE = PASS
FINITE_CONTROL_LOCATION_GATE = PASS
R11_CONTROL_LOCATION = s=1 FOR ALL 7

R08_FULL_FC_RECTANGLE = UPPER_BOUND_ONLY
R10A_085_RECTANGLE = HIGH_VALUE_SCREENING_BASELINE / NOT FINAL PHYSICAL LAW
R11_COMPRESSION_ONLY_EXACT_ENVELOPE = SOURCE_FAITHFUL_COMPRESSION BASELINE

R11_HIGH_CONFIDENCE_MEAN = -4.218 percent
R11_HIGH_CONFIDENCE_MAE = 4.218 percent
R11_HIGH_CONFIDENCE_RMSE = 4.408 percent

STRUCTURAL_FRONT_REOPEN = NO
Ny_My_TERMINAL_REOPEN = NO
NEW_FITTED_FACTOR = NO

NEXT_PRIMARY = ADD SOURCE-SUPPORTED UHPC TENSION TO THE SAME ANALYTIC STRAIN-COMPATIBLE RESULTANT ENVELOPE
NEXT_SECONDARY = LIU_LEUTBECHER_TC SOFTENING AFTER TWO-SIDED ENVELOPE CLOSURE
```
