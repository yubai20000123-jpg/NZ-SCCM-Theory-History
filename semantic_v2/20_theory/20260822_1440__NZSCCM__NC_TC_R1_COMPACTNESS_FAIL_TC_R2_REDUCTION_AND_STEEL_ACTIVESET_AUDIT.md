# NZ-SCCM — NC TC-R1 general-s compactness fail → TC-R2 compact reduction + steel active-set audit

**Date:** 2026-08-22 14:40 +08:00  
**Status:** `TC_R1_GENERAL_S_COMPACTNESS_FAIL / TC_R2_COMPACT_PASS_CANDIDATE / Z6_STEEL_ACTIVESET_BLOCKER_IDENTIFIED / FINAL_PU_OPEN`

## 0. Hard boundary

The structural backbone is unchanged.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURAL_BACKBONE_CHANGED = FALSE
```

This audit executes the previously frozen fail-fast rule: TC-R1 receives one compact general-s closure attempt; if that attempt requires a large opaque primitive/compiler layer, TC-R1 is retired rather than expanded indefinitely.

---

# 1. TC-R1 general-s compactness test — FAIL

TC-R1 used:

1. the [8/8] rational T5 tensile compilation;
2. the current softening factor
   \[
   \gamma_c(\lambda_t)=\min\left(1,\frac1{0.8+0.34\lambda_t}\right);
   \]
3. a softened compressive peak stress **and** a softening-dependent shifted peak strain;
4. Saenz with that current shifted peak.

For a general section point under bending, material coordinates are affine in thickness coordinate z:

\[
\lambda_t(z)=a_t+b_tz,
\qquad
\lambda_c(z)=a_c+b_cz.
\]

The T5 tensile stress is therefore an [8/8] rational function of z. Its exact zeroth/first moments require handling an eighth-degree denominator.

More importantly, after inserting

\[
\gamma_c=(A+Bz)^{-1}
\]

into the Nguyen peak-strain polynomial

\[
\varepsilon_{cp}/\varepsilon_0
=-(0.35\gamma_c+2.25\gamma_c^2-1.6\gamma_c^3)
\]

and then into Saenz, symbolic cancellation gives a rational compression integrand with

```text
numerator degree in z   = 5
denominator degree in z = 8
```

on the softened ascending branch.

Hence an exact general-s implementation would require candidate-dependent eighth-degree root sets, RootSum-style objects or an equivalently opaque partial-fraction compiler. This is mathematically finite, but it fails the project's **small auditable primitive set** criterion.

```text
TC_R1_MATERIAL_POINTLESS_MAP = PASS
TC_R1_GENERAL_S_MATHEMATICAL_INTEGRABILITY = YES_IN_PRINCIPLE
TC_R1_GENERAL_S_COMPACTNESS = FAIL
TC_R1_GENERAL_S_PRODUCTION = RETIRED
```

This retirement is based on analytic complexity, not on Zhou/Winter/experiment/FEM agreement.

---

# 2. Compact replacement inside the same source physics: TC-R2

A full jump to another biaxial concrete theory is not necessary yet. The same source physics can be represented much more transparently by removing two project compilations that caused most of the algebraic growth.

## 2.1 Tension: use the literal finite Foster/Nguyen piecewise law

Let

\[
\varepsilon_{cr}=\frac{f_t}{E_0},
\qquad
\alpha_1=10,
\qquad
\alpha_2=0.3.
\]

The project uses the conservative lower end of Foster's reported \(\alpha_2\) range; it is not identified from structural Pu.

For the current tensile equivalent/material strain \(\varepsilon_t^u\):

\[
\boxed{
\sigma_t=
\begin{cases}
E_0\varepsilon_t^u,&0\le\varepsilon_t^u\le\varepsilon_{cr},\\[1mm]
 f_t\left[1-\dfrac{(1-\alpha_2)(\varepsilon_t^u/\varepsilon_{cr}-1)}{\alpha_1-1}\right],
 &\varepsilon_{cr}<\varepsilon_t^u<\alpha_1\varepsilon_{cr},\\[3mm]
\alpha_2f_t,&\varepsilon_t^u\ge\alpha_1\varepsilon_{cr}.
\end{cases}}
\]

This replaces the T5 rational compiler only in TC-R2. It leaves only linear/constant tensile primitives and finite source kinks.

## 2.2 Compression softening amplitude

Retain the current Nguyen/MCFT source-style reduction:

\[
\boxed{
\gamma_c(\lambda_t)
=\min\left(1,\frac1{0.8+0.34\lambda_t}\right).
}
\]

The Poisson-free material-coordinate measure remains:

\[
\widehat\varepsilon_t
=\frac{\varepsilon_t+\nu\varepsilon_c}{1-\nu^2}
=\varepsilon_0\lambda_t.
\]

Thus pure uniaxial compression has \(\lambda_t=0\Rightarrow\gamma_c=1\).

## 2.3 Compression: scale the fixed NC backbone, do not move the peak strain

Let \(\sigma_{c0}(\lambda_c)\) be the existing uniaxial NC compression law:

- fixed-peak Saenz ascending branch with peak \((-\varepsilon_0,-f_c)\);
- existing bounded source-style postpeak continuation to the residual branch.

Define the TC-R2 compression law by

\[
\boxed{
\sigma_c^{TC}(\lambda_t,\lambda_c)
=\gamma_c(\lambda_t)\,\sigma_{c0}(\lambda_c).
}
\]

This is explicitly a `PROJECT-DERIVED CURRENT-STRENGTH REDUCTION`; it is not claimed to be Nguyen's literal shifted-peak-strain law.

It preserves:

\[
\lambda_t=0\Rightarrow\sigma_c^{TC}=\sigma_{c0},
\]

is bounded, memoryless, and has same-source analytic tangents on every branch.

---

# 3. Why TC-R2 general-s primitives are compact

Use the compatible affine material-coordinate field

\[
\boxed{
\lambda_t(z)=\lambda_{t0}+\nu_c\chi z,
\qquad
\lambda_c(z)=\lambda_{c0}+\chi z.
}
\]

Then physical transverse strain is constant through thickness while longitudinal strain is affine:

\[
\varepsilon_x=\varepsilon_0(\lambda_{t0}-\nu_c\lambda_{c0}),
\]

\[
\varepsilon_y(z)
=\varepsilon_0\left[(\lambda_{c0}-\nu_c\lambda_{t0})+(1-\nu_c^2)\chi z\right].
\]

All material fronts are roots of affine equations in z:

- Foster cracking: \(\lambda_t=x_{cr}\);
- Foster residual onset: \(\lambda_t=\alpha_1x_{cr}\);
- compression-softening onset: \(\lambda_t=10/17\);
- compression peak: \(\lambda_c=-1\);
- residual compression onset: \(\lambda_c=-\gamma_2\);
- web yield fronts: affine physical \(\varepsilon_y\) equals \(\pm f_y/E_s\).

Within each interval:

1. Foster tension is linear or constant;
2. unsoftened Saenz is linear-over-quadratic;
3. softened ascending compression is
   \[
   \frac{\text{linear}}{\text{linear}\times\text{quadratic}},
   \]
   i.e. a **factored cubic denominator**, requiring only logarithmic/arctangent rational primitives;
4. softened postpeak compression is linear-over-linear or constant-over-linear;
5. web force/moment primitives are polynomial between finite yield fronts;
6. the two external steel faces are discrete face evaluations, not a through-thickness steel quadrature.

Therefore the concrete/web section moment set is finite and small; no eighth-degree root compiler is required.

```text
TC_R2_GENERAL_S_PRIMITIVE_COMPACTNESS = PASS
TC_R2_FORMAL_SPATIAL_QUADRATURE_REQUIRED = NO
TC_R2_MATERIAL_POINTS_REQUIRED = NO
```

---

# 4. TC-R2 material seven-gate result

|Gate|Status|Reason|
|---|---|---|
|G1|PASS|uniaxial compression exactly recovered at lambda_t=0|
|G2|PASS_WITH_FOSTER_PROJECT_PARAMETER_CHOICE|finite source-style tension law; alpha2=0.3 declared|
|G3|PASS_CANDIDATE|TC weakening uses Nguyen/MCFT source physics; multiplicative current reduction declared project-derived|
|G4|PASS|Poisson-free material-coordinate softening measure|
|G5|PASS_WITH_FINITE_SOURCE/PROJECT_KINKS|stress and tangent from same branch equations|
|G6|PASS_CANDIDATE|small finite primitive family, no history or spatial quadrature|
|G7|PASS|no structural Pu used for any coefficient|

```text
NC_TC_R2_MATERIAL_7GATE = PASS_CANDIDATE
NC_TC_R2_PRODUCTION_FREEZE = PENDING_SECTION_STEEL_AUDIT
```

---

# 5. New obstruction exposed by the general-s diagnostic: steel active-set nonuniformity

After TC-R2 removed the concrete primitive explosion, an off-mainline high-order through-thickness numerical diagnostic was used **only to identify the next obstruction**. Its spatially integrated numbers are not formal production results.

At finite \(s>0\), one external face reaches the plane-stress radial yield cap first. The branch can continue with that face capped. When the second face reaches the cap, one-sided active-set derivatives show a terminal kink: the assumed doubly-capped continuation points back across the second-face yield surface.

At approximately \(s=0.444855\):

- first web-edge compression yield occurs near `48.72244 MN`, but partial web yielding can continue;
- the second outer-face yield event occurs near
  \[
  P\approx51.67326\ \mathrm{MN};
  \]
- for the second-face yield function \(h=\sigma_{VM,trial}^{(+)}-f_y\), one-sided derivatives are approximately
  \[
  dh/dq\approx+1.42\times10^5
  \]
  on the one-face-capped / second-face-elastic branch, and
  \[
  dh/dq\approx-2.65\times10^6
  \]
  on the doubly-capped continuation.

The more important observation is the limit toward the symmetric endpoint:

|s|diagnostic second-face terminal load / MN|
|---:|---:|
|0.020|49.00288|
|0.010|48.95329|
|0.005|48.92919|
|0.001|48.91024|
|0.00001|48.90560|

whereas the exactly symmetric \(s=0\) TC-R2 branch continues with both faces capped to the later web-yield endpoint near `50.18638 MN`.

Thus the current memoryless elastic-perfectly-plastic radial-cap face law produces a nonuniform active-set limit:

\[
\lim_{s\to0^+}P_{terminal}(s)\ne P_{terminal}(0).
\]

This is now the primary general-s blocker. Merely changing the NC concrete law to Cedolin–Mulas would not remove this steel-phase singularity.

---

# 6. The s→0+ limit itself is a finite no-quadrature root

The limit can be written without any thickness quadrature because \(\chi\to0\). At the limiting uniform section:

1. concrete is uniform TC-R2;
2. the equivalent web is still elastic;
3. both outer faces are exactly at first plane-stress von-Mises yield, so radial scale = 1;
4. \(N_x,N_y\) equilibrium holds at \(s=0\).

The resulting finite three-unknown root is

\[
\boxed{\lambda_t\approx0.53638962},
\]

\[
\boxed{\lambda_c\approx-0.63294763},
\]

\[
\boxed{q\approx0.01163665},
\]

\[
\boxed{P_{s\to0^+}^{face-yield}\approx48.9055510\ \mathrm{MN}}.
\]

At this root the face elastic trial stress is approximately

\[
(\sigma_x^s,\sigma_y^s)
=(+182.772,-226.373)\ \mathrm{MPa},
\]

and exactly

\[
\sigma_{VM}=355\ \mathrm{MPa}.
\]

A one-sided implicit-function audit of the asymmetric branch at \(s=0^+\) gives a nonsingular local Jacobian and

\[
\frac{dP_{terminal}}{ds}\Big|_{0^+}\approx+4.68\ \mathrm{MN},
\]

so the branch exists locally and rises away from the limit. This establishes the boundary-limit candidate locally without using a spatial grid.

It does **not** yet prove that no other finite s gives a lower terminal load over the whole interval \(0<s\le1\).

```text
Z6_TC_R2_S0PLUS_FACE_YIELD_LIMIT = 48.9055510 MN / FORMAL_LOCAL_LIMIT_CANDIDATE
Z6_TC_R2_GLOBAL_S_MINIMUM = NOT_YET_CERTIFIED
```

---

# 7. Constitutive pivot decision updated

The previous rule was to switch to Cedolin–Mulas if TC-R1 became opaque. TC-R1 did become opaque, so it is retired. However the compact TC-R2 replacement closes the **concrete** general-s primitive problem with a much smaller source-transparent law.

The remaining obstruction is now the steel face active-set law, not concrete integration complexity.

Therefore:

```text
TC_R1_GENERAL_S = RETIRED
TC_R2 = ACTIVE_COMPACT_NC_TC_CANDIDATE
CEDOLIN_MULAS_1984 = DEFERRED_ALTERNATIVE / NOT_NEEDED_TO_FIX_CURRENT_STEEL_BLOCKER
NEXT_HARD_GATE = STEEL_FACE_CURRENT_LAW_SOURCE_AUDIT
```

The steel audit must first determine whether the actual source contract supports any monotonic hardening / deformation-theory current law. No hardening modulus or Ramberg–Osgood coefficient may be chosen from Z6, Zhou, Winter, FEM, or experiment.

If the steel source is genuinely ideal elastic-perfectly-plastic, then the nonuniform active-set limit must be treated as a real limitation/feature of the current low-dimensional total-strain capacity formulation rather than hidden by an invented hardening parameter.

---

# 8. Current stop/go

Closed in this step:

- TC-R1 compactness test: **FAIL / retired**;
- TC-R2 material law: **PASS candidate**;
- TC-R2 general-s concrete/web primitive compactness: **PASS**;
- Z6 symmetric s=0 TC-R2 endpoint: direct finite solution exists;
- Z6 s→0+ second-face-yield limit: direct finite local-limit solution exists.

Still open:

\[
\boxed{Z6\text{ and }Z0\text{--}Z6\text{ final global general-s }P_u}
\]

because the external steel current law now controls the admissibility topology.

Next task:

\[
\boxed{\text{source-grounded steel-face constitutive audit before any further NC-model replacement}.}
\]
