# NZ-SCCM R18 — C2 mask-derivative cancellation contract

This note fixes how the already verified R17 spectral-Heaviside representation is differentiated when constructing the same-source `P`, `Rq`, `Ralpha`, and `Jlim` operators.

## 1. Existing R17 fact

The three exact scalar tension branches `p0`, `p1`, `p2` satisfy at both normalized thresholds `r=1` and `r=10`:

```text
left value  = right value
left d/dr   = right d/dr
left d2/dr2 = right d2/dr2
```

The R17 endpoint audit has already passed all six checks. Thus `u_R(t)` is globally `C2` across the only spline-state boundaries.

## 2. Consequence for the six spectral states

A transition among the ordered states

```text
00, 10, 11, 20, 21, 22
```

changes only which `C2` polynomial branch is evaluated for `u_R(t_plus)` and/or `u_R(t_minus)`. The projector, compression function, smooth projector `Pi_eta`, and spectral return are unchanged.

Therefore, away from the separate repeated-eigenvalue removable limit, each physical stress component is `C2` across every R17 threshold surface.

## 3. Distributional Heaviside differentiation

Write any global stress/integrand quantity as

```text
F = sum_s I_s F_s
```

or, equivalently, using the nine reusable products,

```text
F = sum_m H_m G_m.
```

A formal derivative of a Heaviside factor produces delta-supported terms proportional to the jump of the adjoining smooth branch quantity. Because the branch values agree at every threshold, the first derivative has no surviving delta term. Differentiating again produces coefficients proportional to the jump of the first derivative; those also vanish because `u_R` is `C2`.

Hence, for the derivative orders needed by the R15 direct limit system,

```text
dF/dg      = sum_s I_s dF_s/dg,
d2F/dgdh  = sum_s I_s d2F_s/dgdh,
```

with no additional threshold-surface distribution terms.

Equivalently, the same nine R17 masks can be reused for the smooth branch stress, material tangent, `P_h`, `R_{g,h}`, and any second smooth derivative needed to construct the direct `Jlim` residual system.

## 4. Scope

This cancellation statement applies specifically to the R10 spline thresholds at `r=1,10`, whose `C2` identities are already exact-audited. It is **not** a blanket rule allowing arbitrary discontinuous material branches to drop Heaviside derivatives.

The repeated principal-value case remains handled by the continuous spectral limit already required by R15.

## 5. Governance

No spatial cells or threshold subdomains are created. Threshold surfaces remain implicit in one global Heaviside formula.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_material_points = 0
FINITE_PREFIX = 0
```
