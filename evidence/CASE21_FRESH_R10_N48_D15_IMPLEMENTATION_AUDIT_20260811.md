# Case21 fresh R10-N48-D15 implementation audit

**Date:** 2026-08-11

This note records implementation details of the fresh calculation only. It does not introduce another theory stage.

## Finite analytic coefficient representation

Material coordinate order:

\[
N_M=48.
\]

For the structural coefficient algebra used in this Case21 execution, the retained tensor-Chebyshev coefficient indices were

\[
0\le i,j,k\le28.
\]

This is a finite analytic coefficient representation, not a spatial integration grid. No value of the physical integrand was evaluated at a spatial Chebyshev node, Gauss point, Simpson point, or material point.

Coefficient multiplication used only the algebraic product identity

\[
\mathcal C_m\mathcal C_n
=\frac12(\mathcal C_{m+n}+\mathcal C_{|m-n|}),
\]

with coefficient-index convolution. Dense products were accelerated as Laurent/coefficient-index convolution; this does not create physical-space samples.

Formal spatial identity therefore remains

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

## Fresh D15 contractions at the final state

At

\[
D\approx0.8359179832,\qquad
q\approx0.00178978948,
\]

the exact-moment contraction of the normalized axial stress coefficient field is

\[
\sum p_{ijk}M_iM_jZ_k\approx-13.33113967.
\]

The axial-force prefactor is

\[
\frac{f_cb t_p}{2\pi^2}\frac1{1000}
\approx25.32429668\ \mathrm{kN},
\]

hence

\[
P_c\approx337.601736\ \mathrm{kN}.
\]

For the amplitude-work coefficient field,

\[
\sum r_{ijk}M_iM_jZ_k\approx4.82108472,
\]

and

\[
\frac{f_c\varepsilon_0J_\Omega}{1000}
\approx64.57189168\ \mathrm{kN\,mm},
\]

so

\[
R_{q,c}\approx311.306561\ \mathrm{kN\,mm}.
\]

These numbers are outputs of coefficient contraction, not numerical spatial quadrature sums.
