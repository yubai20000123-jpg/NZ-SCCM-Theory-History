# Hiew et al. 2024 — direct-tension evidence

## Source identity

- file: `Hiew_2024_UHPC_unified_tension_2pct.pdf`
- ChatGPT File Library ID: `file_0000000087e882079606fbbb13dd1e2d`
- paper: S.Y. Hiew et al., *A unified tensile constitutive model for mono/hybrid fibre-reinforced ultra-high-performance concrete (UHPC)*, Cement and Concrete Composites 150 (2024) 105553.
- DOI: `10.1016/j.cemconcomp.2024.105553`
- official OA locator: `https://research.monash.edu/files/599317955/589510091_oa.pdf`
- evidence identity: `PRIMARY_SOURCE / UNIAXIAL_MONOTONIC_DIRECT_TENSION`

## Effective evidence retained

The paper uses direct-tension testing and proposes an idealized tensile stress–strain model organized into three main regimes:

`elastic -> strain-hardening -> strain-softening`, with the strain-softening regime further passing through peak -> localisation -> fibre pull-out decay.

The source explicitly defines the elastic branch (Eq. 14):

```text
sigma_t(epsilon_t) = E_t * epsilon_t
```

for `epsilon_t <= epsilon_t,cr`.

For the first strain-softening segment, from peak to localisation, Eq. (16) is:

```text
sigma_t(epsilon_t)
= f_t,peak
+ (f_t,loc - f_t,peak)/(epsilon_t,loc - epsilon_t,peak)
  * (epsilon_t - epsilon_t,peak)
```

for `epsilon_t,peak < epsilon_t <= epsilon_t,loc`.

Beyond localisation the paper uses a decreasing exponential fibre-pullout relation, Eq. (17), with fitted coefficients `C1` and `C2`. Table 7 supplies the relevant fitted coefficients and goodness-of-fit for individual UHPC fibre series. `C1/C2` are therefore **material/fibre-series parameters**, not structure-level fitting coefficients.

The paper also provides mechanics-/empirical-based predictive equations for effective cracking strength/strain, peak strength/strain, localisation strength/strain and tensile strain limit as functions of fibre characteristics/content. Table 6 contains the experimental tensile parameters by series.

## 2%-fibre experimental evidence — Table 6

The following values are source-table means, retained because the project repeatedly considers a 2% steel-fibre UHPC but has **not** frozen one fibre geometry as universally representative.

| series | fibre system | Et (GPa) | ft,el (MPa) | ft,cr (MPa) | eps_t,cr (%) | ft,peak (MPa) | eps_t,peak (%) | ft,loc (MPa) | eps_t,loc (%) | eps_t,lim (%) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SL-2.0 | 2% straight | 47.8 | 9.6 | 9.8 | 0.041 | 11.6 | 0.386 | 9.9 | 0.619 | 0.752 |
| HL-2.0 | 2% hooked-end | 48.9 | 10.1 | 10.3 | 0.040 | 11.4 | 0.664 | 10.8 | 0.855 | 0.990 |
| SL-HL-2.0 | 1% straight + 1% hooked-end | 48.2 | 9.3 | 10.2 | 0.041 | 11.2 | 0.374 | 10.6 | 0.675 | 0.741 |

These values show why the project must not silently collapse “2% steel fibre” into a single universal tensile law: peak strengths are relatively close, but peak/localisation strains and post-peak capacity differ materially with fibre geometry/hybridisation.

## Constitutive-model parameters — Table 7

The paper then feeds predictive/model parameters into its unified constitutive law. For the same 2% series:

| series | Et (GPa) | eps_t,cr (%) | ft,cr (MPa) | eps_t,peak (%) | ft,peak (MPa) | eps_t,loc (%) | ft,loc (MPa) | eps_t,lim (%) | C1 | C2 | R2 for Eq.(17) fit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SL-2.0 | 47.8 | 0.040 | 10.0 | 0.380 | 11.7 | 0.624 | 9.9 | 0.759 | 0.289 | 0.456 | 0.979 |
| HL-2.0 | 49.0 | 0.042 | 10.3 | 0.674 | 11.1 | 0.872 | 10.8 | 1.000 | -1.092 | 0.401 | 0.987 |
| SL-HL-2.0 | 48.3 | 0.042 | 10.1 | 0.380 | 11.0 | 0.690 | 10.7 | 0.741 | 0.326 | 0.403 | 0.976 |

Important distinction: Table 6 contains measured/derived experimental tensile parameters; Table 7 contains the parameters used by the proposed constitutive model, including fitted Eq.(17) coefficients. The two tables must not be mixed without labeling.

## Project consequence

The old historical UHPC-C0 use of one 2%-fibre representative anchor remains a calculable baseline only. If a future production UHPC operator needs one fixed tensile branch, it must either:

- specify the intended fibre system (SL / HL / hybrid) and use a source-consistent parameter set; or
- explicitly define and justify a material-level representative/uncertainty rule.

It may not choose the branch or interpolate its parameters by matching Case21, Swartz24 or UCFT structural ultimate loads.

## USED FOR

- selecting the physical form of the UHPC monotonic uniaxial tensile branch;
- direct-tension crack/peak/localisation/softening source constraints;
- fibre-series material parameters and trend checks;
- preventing ordinary-concrete Foster tension-stiffening from being copied blindly into UHPC.

## NOT USED FOR

- full biaxial TC/TT/CC stress update;
- arbitrary loading-history closure;
- shear-transfer law;
- triaxial failure surface;
- calibration from Case21/Swartz/UCFT ultimate load.

## Current identity

`SOURCE_ONLY_FOR_UHPC_TENSION / HIGH_PRIORITY`

Any project current-state simplification derived from this source must be labelled as a project transformation. Hiew's paper itself considers monotonic direct tension and does not by itself define the complete two-dimensional UHPC material operator.
