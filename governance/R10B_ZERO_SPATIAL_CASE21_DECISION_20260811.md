# R10B ZERO-SPATIAL CASE21 DECISION

Date: 2026-08-11

## Decision

```text
R10B_ZERO_SPATIAL_CASE21 = PASS_ENGINEERING
```

R10B keeps the frozen R10 one-dimensional energy smoothing unchanged and recompiles it through a Case21-local spectral/material compiler, the same multiaxial current map, Nguyen second-order kinematics, Cayley-Hamilton tensor-Chebyshev coefficient algebra, and exact complete-halfwave moments.

Formal counts:

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

The numerical FFT backend is used only for coefficient-index convolution. It does not evaluate the physical-space integrand and is not spatial quadrature/collocation.

The 1D material-coordinate Chebyshev compiler may use material-coordinate samples to derive fixed finite representation coefficients. Those coefficients are not free material parameters and are never chosen from Case21/Swartz Pu.

## Formal Case21 root

```text
Nmat = 48
Nspatial-Cheb = 28
D_u  = 0.8449505
q_u  = 0.001779254542005754
A_u  = 2.1706905412470197 mm
Pc   = 337.39660909142 kN
Ps   = 30.922943404456966 kN
Pu   = 368.31955249587696 kN
R    = -2.2383016926141863e-05 kN mm
L_normalized = 4.029999719717427e-07
```

Experiment is used after material freeze only:

```text
Pf = 368.312750 kN
error = +0.0018469346708655486 %
```

This agreement must not be used to retune R10.

## Derivative gate

`P_D,P_q,R_D,R_q` are propagated through the same retained coefficient algebra by forward chain-rule jets. Finite-difference production derivatives are not used.

The equilibrium-branch identity

\[
\frac{dP}{dD}\bigg|_{R=0}
=\frac{P_DR_q-P_qR_D}{R_q}
=\frac{L}{R_q}
\]

is used to select the branch maximum and audit the same explicit limit equation.

## Order gate

A higher-order N96 equilibrium check at the N48 stationary D gives `P=368.50804285212683 kN`, differing by `0.18849035625 kN = 0.0511757671%` from the N48 formal root. N96 is not a separately optimized stationary root.

Under the current governance, theorem-level tight remainder certification is not an engineering hard gate. The 0.051% order sensitivity is accepted for continued development but remains recorded transparently.

## Prohibitions retained

- do not modify the R10 scalar because Case21 agrees with experiment;
- do not use structural capacity to choose material/compiler parameters;
- do not replace coefficient algebra by spatial Gauss/Simpson/adaptive quadrature;
- do not fit whole-structure P/R/U surfaces from spatial samples;
- do not copy the Case21 spectral intervals directly into Swartz24 production;
- do not start Swartz24 capacity calculation until a common 24-panel spectral/search-domain precheck is passed.

## Next task

```text
CURRENT_RECOMMENDED_NEXT_TASK
= R11_SWARTZ24_COMMON_SPECTRAL_DOMAIN_AND_ZERO_SPATIAL_BATCH_PRECHECK
```

R11 must establish a common or panel-governed analytic D-q/spectral contract for all 24 source panels before any batch Pu calculation.