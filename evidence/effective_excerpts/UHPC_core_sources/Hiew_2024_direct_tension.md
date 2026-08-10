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

## 2%-fibre project relevance

The source includes SL-2.0, HL-2.0 and SL-HL-2.0 series. The project previously used a 2%-fibre representative anchor set in the historical G31 UHPC-C0 baseline; that historical set is preserved elsewhere but is **not automatically a final production parameter set** because fibre geometry and other UHPC parameters were subsequently reopened.

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
