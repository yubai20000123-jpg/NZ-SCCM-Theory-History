# NZ-SCCM — Z6 TC-R2 s=0 / s→0+ direct roots + general-s steel active-set diagnostic

**Date:** 2026-08-22 14:40 +08:00  
**Status:** `EXECUTED / DIRECT_NO_QUADRATURE_ENDPOINTS_RESOLVED / GENERAL_S_NUMERICAL_DIAGNOSTIC_OFF_MAINLINE / FINAL_PU_OPEN`

## 0. Formal boundary

Formal results in Sections 1–3 use only finite algebraic roots and uniform-section phase equilibrium.

```text
formal spatial sampling = 0
formal spatial quadrature = 0
material points = 0
load steps = 0
history states = 0
comparator in root selection = 0
```

A high-order through-thickness numerical integration was used later only as an **OFF_MAINLINE_DIAGNOSTIC** to identify the next active-set obstruction. No number produced by that integration is frozen as final Pu.

---

# 1. TC-R2 used in this execution

Tension uses the finite Foster/Nguyen piecewise relation with

\[
\alpha_1=10,\qquad \alpha_2=0.3,
\qquad \varepsilon_{cr}=f_t/E_0.
\]

Compression uses

\[
\gamma_c(\lambda_t)
=\min\left(1,\frac1{0.8+0.34\lambda_t}\right)
\]

and

\[
\sigma_c^{TC}(\lambda_t,\lambda_c)
=\gamma_c(\lambda_t)\sigma_{c0}(\lambda_c),
\]

where \(\sigma_{c0}\) is the fixed-peak Saenz + bounded postpeak NC backbone.

Z6 structural coefficients remain

\[
P_{cr}=39.2880147150\ \mathrm{MN},
\]

\[
C=86071.5974582\ \mathrm{MN},
\]

\[
G=7.4692093263\times10^6\ \mathrm{N/mm},
\]

\[
K_x=6.876056916767441\times10^6\ \mathrm{N/mm},
\]

\[
J=1.2419245217\times10^7\ \mathrm{N}.
\]

---

# 2. Direct symmetric s=0 TC-R2 endpoint

At \(s=0\),

\[
m=Jqs=0,
\]

and the full section is uniform through thickness. The finite unknown set is

\[
(\lambda_t,\lambda_c,q).
\]

The equations are:

\[
N_x^{sec}=K_xq(q+2q_0),
\]

\[
N_y^{sec}
=-\left[\frac{P_{pb}(q)}b+Gq(q+2q_0)\right],
\]

and the longitudinal-web compression-yield equality

\[
E_s\varepsilon_y+f_y=0.
\]

The direct root is

\[
\boxed{\lambda_t=0.72375111146},
\]

\[
\boxed{\lambda_c=-0.79066099525},
\]

\[
\boxed{q=0.012018755437},
\]

\[
\boxed{P_{s=0}^{TC-R2}=50.1863826545\ \mathrm{MN}}.
\]

At this state the Foster tension law is on its residual plateau and

\[
\gamma_c\approx0.95595406.
\]

The concrete stresses are approximately

\[
\sigma_x^c=+0.9120\ \mathrm{MPa},
\qquad
\sigma_y^c=-28.2776\ \mathrm{MPa}.
\]

The two external faces are radially capped and the web is at \(-355\) MPa.

This value is an exact current **symmetric endpoint candidate**, not the final global general-s Pu.

---

# 3. Direct s→0+ asymmetric face-yield limit — no quadrature

The general-s diagnostic revealed that for arbitrarily small positive s, one face is already on the radial cap while the second face approaches first yield. As \(s\to0^+\), the curvature parameter \(\chi\to0\), so the limiting section becomes uniform and the limit itself can be solved without any thickness integration.

At the limiting state:

- concrete is uniform TC-R2;
- the web is elastic;
- both external-face elastic trial states satisfy exactly \(\sigma_{VM}=f_y\);
- no radial scaling is yet required at the second-face event;
- \(N_x,N_y\) equilibrium is enforced at \(s=0\).

The finite root is

\[
\boxed{\lambda_t=0.53638962\ \text{(approx.)}},
\]

\[
\boxed{\lambda_c=-0.63294763\ \text{(approx.)}},
\]

\[
\boxed{q=0.01163665\ \text{(approx.)}},
\]

\[
\boxed{P_{s\to0^+}^{face-yield}=48.9055510040\ \mathrm{MN}}.
\]

The external-face elastic trial stress is approximately

\[
(\sigma_x^s,\sigma_y^s)
=(+182.77168,-226.37332)\ \mathrm{MPa},
\]

with

\[
\boxed{\sigma_{VM}=355\ \mathrm{MPa}}.
\]

The equilibrium residual is below numerical root precision (`~1e-12` force-equation scale in the direct solve).

A one-sided implicit-function check on the branch with one face capped and the second face elastic gives a nonsingular local 4×4 Jacobian. The local event branch satisfies approximately

\[
\boxed{
P_{terminal}(s)
=48.9055510+4.68s+O(s^2)\ \mathrm{MN}
}
\]

for \(s\to0^+\). Therefore the asymmetric terminal branch exists locally and rises away from the boundary limit.

This establishes a formal **local boundary-limit candidate**, not the global minimum over all s.

---

# 4. OFF-MAINLINE general-s diagnostic

To identify whether the remaining difficulty was concrete integration or phase admissibility, a high-order through-thickness numerical diagnostic was run. This calculation is explicitly excluded from the formal operator.

The compatible material-coordinate field used only for this diagnostic was

\[
\lambda_t(z)=\lambda_{t0}+\nu_c\chi z,
\qquad
\lambda_c(z)=\lambda_{c0}+\chi z,
\]

with finite section equilibrium for \(N_x,N_y,M_y\).

## 4.1 Second-face terminal event approaching s=0

|s|second-face terminal diagnostic / MN|
|---:|---:|
|0.020|49.0028788|
|0.010|48.9532937|
|0.005|48.9291909|
|0.001|48.9102418|
|0.00001|48.9055978|

These values converge to the direct no-quadrature limit in Section 3.

## 4.2 Representative finite-s active-set sequence

At approximately

\[
s=0.444855,
\]

the diagnostic gives:

1. first compressed web edge reaches \(-f_y\) near
   \[
   P\approx48.72244\ \mathrm{MN},
   \]
   but the section can continue through a partial web-yield front;
2. the second external face reaches the radial cap near
   \[
   q\approx0.01245718,
   \qquad
   P\approx51.67326\ \mathrm{MN}.
   \]

At the second-face event the one-sided derivative of

\[
h=\sigma_{VM,trial}^{(+)}-f_y
\]

is approximately

\[
\frac{dh}{dq}>0
\]

on the one-face-capped / second-face-elastic branch (`~+1.42e5`), but

\[
\frac{dh}{dq}<0
\]

on the doubly-capped continuation (`~-2.65e6`).

Thus the capped continuation immediately points back across the active surface: a terminal complementarity kink for that fixed s.

---

# 5. Interpretation

The compact TC-R2 law removes the eighth-degree concrete primitive problem. The next obstruction is not another NC material integral; it is the **memoryless elastic-perfectly-plastic radial-cap steel-face law**.

The exactly symmetric s=0 state permits both faces to remain on the cap and continue to the web-yield endpoint at `50.18638 MN`, while an arbitrarily small bending asymmetry produces a different face-yield terminal family whose limit is `48.905551 MN`.

Therefore:

```text
TC_R2_CONCRETE_GENERAL_S_COMPACTNESS = PASS
Z6_TC_R2_S0_ENDPOINT = 50.1863826545 MN / DIRECT CANDIDATE
Z6_TC_R2_S0PLUS_FACE_YIELD_LIMIT = 48.9055510040 MN / DIRECT LOCAL-LIMIT CANDIDATE
Z6_GLOBAL_GENERAL_S_PU = OPEN
STEEL_FACE_ACTIVESET_NONUNIFORMITY = IDENTIFIED
```

The global minimum over the full continuous interval \(0<s\le1\) has not been formally certified. The off-mainline scan suggests the second-face terminal event rises away from s=0, but that scan is not a production proof.

---

# 6. Comparator discipline

No Zhou, Winter, FEM or experiment value was used in either direct root.

Comparator proximity, if inspected later, has no role in choosing between the symmetric endpoint and the asymmetric boundary-limit family.

---

# 7. Next gate

Before replacing NC concrete again, audit the steel-face material identity:

1. determine whether the source steel contract is genuinely elastic-perfectly-plastic;
2. determine whether a source-grounded monotonic hardening/deformation-theory law exists;
3. if hardening exists, require an explicit plane-stress current map and re-run the finite active-set audit without fitting to Z6;
4. if no such source exists, retain the perfect-plastic law and treat the nonuniform limit as an explicit limitation/feature rather than hiding it.

Cedolin–Mulas remains an NC alternative, but changing concrete alone cannot repair the steel active-set topology identified here.
