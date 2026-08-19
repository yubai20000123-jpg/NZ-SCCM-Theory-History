# NZ-SCCM Z1 R18 — nine-mask primitive-atom contract

This file only makes explicit the bit ordering already used by the R17 exact spectral-Heaviside compiler. It does **not** introduce a new state partition or material law.

Let, for the normalized spectral thresholds `chi1` and `chi10`,

```text
a1  = H(A_chi1)
b1  = H(Delta_chi1)
a10 = H(A_chi10)
b10 = H(Delta_chi10)
```

with

```text
A_chi   = mu/xcr - chi
Delta_chi = A_chi^2 - rE^2/xcr^2
```

and with the already verified strictly-positive rational denominators cleared, so the Heaviside arguments passed to Oaku/OpenXM are the corresponding exact polynomial numerators.

The R17 mask bit order is exactly:

```text
(a1, b1, a10, b10)
```

Hence the nine reusable products are

```text
0000 = 1
0001 = b10
0011 = a10*b10
0100 = b1
0101 = b1*b10
0111 = b1*a10*b10
1100 = a1*b1
1101 = a1*b1*b10
1111 = a1*b1*a10*b10
```

The minus-principal threshold indicator at a threshold is therefore

```text
M(chi) = H(A_chi) H(Delta_chi)
```

so `1100` is `M(chi1)` and `0011` is `M(chi10)`.

The plus-principal threshold indicator remains the R17 identity

```text
P(chi) = 1 - H(-A_chi) H(Delta_chi),
```

but after the six-state idempotent expansion no extra primitive beyond `a1,b1,a10,b10` is required.

Together with `20260819__NZSCCM__Z1__R18_GLOBAL_MASK_COEFFICIENT_ASSEMBLY.json`, every global smooth material/integrand quantity has the form

```text
F_global = sum_{mask in nine masks} G_mask * H_mask
```

where `G_mask` is a finite linear combination of the six smooth spectral branch values. This is one global formula over one complete halfwave; it is not a spatial subdivision.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_material_points = 0
FINITE_PREFIX = 0
```
