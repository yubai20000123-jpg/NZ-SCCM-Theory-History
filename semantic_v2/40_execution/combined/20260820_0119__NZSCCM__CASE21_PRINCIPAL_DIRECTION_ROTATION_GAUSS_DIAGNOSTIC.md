# NZ-SCCM — Case21 principal-direction rotation Gauss diagnostic

**Date:** 2026-08-20 01:19 +08  
**Identity:** DIAGNOSTIC ONLY / GAUSS ALLOWED BY USER / NOT FORMAL ZERO-QUADRATURE THEORY

## 1. Question

Quantify the effect of deleting local principal-direction rotation in Case21 while keeping the same second-order kinematics and the same ordinary-concrete source equations.

Two models differ only in material-frame treatment:

- **Model F:** full strain tensor -> local principal strains/directions -> Nguyen/Foster source response -> rotate stress back to x-y.
- **Model XY:** same `(eps_x,eps_y,gamma_xy)` kinematics, but material evaluation is forced to `eps1=eps_x`, `eps2=eps_y`, `sigma_x=sigma1`, `sigma_y=sigma2`, `tau_xy=0`.

Gauss integration is used only for this diagnostic and has no production-theory identity.

## 2. Inputs and source-material identity

Case21 input used:

```text
b=ell=1220 mm
t=19.30 mm
A0=3.05 mm
nu=0.18
fc=21.23 MPa
E0=20321 MPa
eps_c0=0.00209
rho_sx=rho_sy=0.00375
Es=200000 MPa
fy=530 MPa
```

The diagnostic material implementation uses the recovered Nguyen Ch.3 / Appendix-B source equations: Saenz compression, Darwin-Pecknold secant coupling, Foster/Kupfer CC/TC/TT peak envelopes, tension stiffening, TC compressive weakening, post-crushing branches, and monotonic source-state transitions.

`ft=0.10 fc=2.123 MPa` is used only as the previously used source-envelope diagnostic closure because the frozen Case21 raw block does not contain a separate measured `ft`. This is not a trial-load calibration and is not promoted to a final Case21 material parameter.

Important implementation identity: the executable used here is **source-derived diagnostic**, not claimed byte-identical/source-equivalent to the archived frozen full branch-C executable. Endpoint structural-step state transitions are used for tractability. Therefore the absolute Pu values below are diagnostic, while the F-vs-XY differential is the primary quantity of interest.

An independent 8^3 Model-F run using the more exact branch-specific recovered source equations gave `Pu_F ~= 359.424 kN`; the fast source-derived diagnostic gave `358.620 kN` at the same quadrature order, a difference of about `-0.224%`. This is used only as a baseline implementation cross-check; the exact-history XY branch was not mixed with the fast F branch for the reported differential.

## 3. Same structural path and equilibrium condition

The user-fixed continuous second-order kinematics are used without alteration. For a given axial mean shortening `d=Delta/ell`, the current total amplitude `A` is solved from the same virtual-work amplitude residual

```text
R_A = integral_V [sigma_x eps_x,A + sigma_y eps_y,A + tau_xy gamma_xy,A] dV
      + reinforcement contribution
    = 0.
```

The first reachable load maximum along the continued equilibrium branch is used as the diagnostic `Pu`. No trial load is used for root or peak selection.

## 4. Gauss-order audit

All values below use the same 5e-5 increment in `Delta/ell` and tensor-product Gauss-Legendre integration.

| Gauss order | concrete-only F (kN) | concrete-only XY (kN) | delta_P concrete | RC F (kN) | RC XY (kN) | delta_P RC |
|---:|---:|---:|---:|---:|---:|---:|
| 8^3  | 323.488 | 246.470 | -23.809% | 358.620 | 307.873 | -14.151% |
| 12^3 | 319.440 | 244.732 | -23.387% | 356.911 | 304.974 | -14.552% |
| 16^3 | 320.982 | 249.076 | -22.402% | 357.143 | 306.338 | -14.225% |
| 20^3 | 319.215 | 245.822 | -22.992% | 354.908 | 304.257 | -14.272% |

The strict 12^3->16^3 `<0.2%` criterion is met for Model-F RC (`+0.065%`) but not for every individual source-state result, because the original Nguyen source equations contain constitutive state transitions/jumps and the endpoint transition diagnostic generates order-level jitter. The 16^3->20^3 RC **differential** changes only from `-14.225%` to `-14.272%` (0.046 percentage point). The concrete-only differential remains approximately `-22%` to `-24%` across all four quadrature orders.

Thus the magnitude class of the principal-direction effect is not a quadrature artifact: it is far above the 10% decision threshold.

## 5. Principal-direction statistics at the 16^3 Model-F RC peak

At the 16^3 Model-F RC diagnostic peak:

```text
Delta/ell = 0.00210
A         = 30.705 mm
Pu_F      = 357.143 kN
```

Principal-axis rotation is reported modulo 90 degrees, i.e. as the nearest-axis angle, because an eigenvector axis has no arrow direction. Results:

```text
max |theta|                         = 44.55 deg
volume-weighted mean |theta|        = 13.00 deg
|sigma_y|-weighted mean |theta|     = 11.09 deg
volume fraction |theta| > 5 deg     = 66.57%
volume fraction |theta| > 10 deg    = 49.91%
volume fraction |theta| > 20 deg    = 25.69%
load-weighted fraction > 5 deg      = 63.93%
load-weighted fraction > 10 deg     = 45.22%
load-weighted fraction > 20 deg     = 19.21%
weighted median |gamma_xy|/|eps_y|  = 0.530
weighted 90% |gamma_xy|/|eps_y|     = 1.617
```

The rotation is therefore not confined to isolated low-stress points.

At the 16^3 concrete-only Model-F peak the corresponding values are also large: load-weighted mean `|theta| ~= 11.08 deg`, with about 63.9% / 45.4% / 19.9% of load weight above 5 / 10 / 20 degrees.

## 6. Same-kinematics comparison along the Model-F equilibrium path

To separate instantaneous stress error from the fact that the two models later follow different equilibrium paths, both materials were additionally driven through the **same sequence of `(Delta/ell,A)` states taken from the Model-F RC path**.

| state | Delta/ell | A (mm) | P_F (kN) | P_XY at same kinematics (kN) | delta P | RMS sigma_y difference / RMS F | RMS sigma_x difference / RMS F | RMS tau_F (MPa) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ~50% peak shortening | 0.00105 | 17.538 | 307.536 | 310.883 | +1.09% | 10.3% | 44.9% | 3.15 |
| ~80% peak shortening | 0.00170 | 25.878 | 356.188 | 359.056 | +0.81% | 11.1% | 59.4% | 3.90 |
| F peak state | 0.00210 | 30.705 | 357.143 | 364.864 | +2.16% | 13.8% | 69.1% | 4.05 |

At the F peak state, the full model has `max |tau_xy| ~= 10.24 MPa`; Model XY sets this field identically to zero by construction.

This table explains an important mechanism: **at one prescribed kinematic state the axial resultant can still look fairly close, even while the local stress tensor is already substantially wrong.** Once each model is allowed to satisfy its own amplitude equilibrium, the path shifts and the final Pu difference amplifies to ~14% for RC and ~23% for concrete-only.

## 7. CC / TC / TT state fractions at the same F-peak kinematics

Using only the current strain signs for the requested CC/TC/TT audit:

```text
Model F:
CC = 5.51%
TC = 83.91%
TT = 10.58%

Model XY at identical (Delta/ell,A):
CC = 7.87%
TC = 78.45%
TT = 13.36%
```

Thus fixing the axes does not merely delete a small shear stress. It also moves finite volume between the CC/TC/TT material sectors.

The source-state histories at this same kinematic state show an additional large redistribution, especially in the TCX fraction (about 28.7% in F versus 17.8% in XY in the source-derived endpoint diagnostic).

## 8. Diagnostic Pu comparison

Using 16^3 as the central reported order:

```text
concrete-only:
Pu_F  = 320.982 kN
Pu_XY = 249.076 kN
delta_P = -22.402%

RC Case21:
Pu_F  = 357.143 kN
Pu_XY = 306.338 kN
delta_P = -14.225%
```

The 20^3 RC differential is `-14.272%`, confirming the same classification.

## 9. Decision

According to the user's thresholds, both concrete-only and reinforced Case21 lie in the `|delta_P| >= 10%` category.

**Diagnostic decision: it is NOT justified to fix `(x,y)` as the concrete principal directions merely to delete the principal-strain square root.**

The principal-value square root should therefore remain on the physics side unless a different algebraic reformulation removes it without deleting local rotation. The earlier complexity-ablation result remains relevant: the principal square root alone is not the first unavoidable D15 obstruction in polynomial spectral laws, so deleting physical rotation is also not required merely for Cayley-Hamilton reduction.

## 10. Limitations and status

```text
GAUSS_DIAGNOSTIC                     = COMPLETE
FORMAL_ZERO_QUADRATURE_IDENTITY       = NO
SOURCE_EQUATION_FAMILY                = NGUYEN/FOSTER SOURCE-DERIVED
BYTE-IDENTICAL FROZEN SOURCE HISTORY  = NO
PRIMARY DIFFERENTIAL CONCLUSION       = ROBUSTLY > 10%
FIX_XY_AS_PRINCIPAL_DIRECTION         = REJECTED FOR CASE21 ANALYTIC SIMPLIFICATION
```

The diagnostic does not alter R10/R13, does not change the formal zero-spatial-quadrature project rules, and must not be cited as a new production solver.