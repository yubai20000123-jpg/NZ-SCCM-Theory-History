# 20261006 BH100 UHPC self-consistent route — backup manifest

Branch:
`diagnostic/20261006-bh100-uhpc-we-wp-d-self-consistency`

Base branch:
`diagnostic/20261004-analytic-ninecurve-attempt`

## Commits

1. `367bab01824f92d96029868db0d3c266a43ffb3d`
   - R01: re-identify fixed total deflection as (W_T=W_0+W_P+W_E)
   - remove old one-way trial -> damage -> wP logic as correctness gate.

2. `411fb1d7353ac226bac18ebbf866cdb69eb39e01`
   - R02: derive 3-scalar self-consistent closure ((e,ho_A,ho_D))
   - use CDP-compatible plastic strain for permanent geometry
   - add BH100 (w=82.2) diagnostic result and shape-change projection audit.

3. `f7ca1bcaf1fd59683bad08a1ec82e6b96209ace2`
   - diagnostic-only deterministic area-quadrature cross-check code.
   - explicitly prohibited as production integration backend.

## Current single-point diagnostic numbers

[
w_E=54.05827 mathrm{mm},
qquad
w_P=28.14173 mathrm{mm},
]

[
ho_A=0.781741,
qquad
ho_D=0.721547,
]

[
P_U(82.2)=6.96255 mathrm{MN}.
]

Material-state extrema:

[
eta_{t,max}=0.00107531,
qquad
eta_{c,max}=0.00119319,
qquad
d_{max}=0.604961.
]

Plastic-reference modal projection:

[
w_{P,11}=28.1417 mathrm{mm},
qquad
w_{P,13}=-1.7965 mathrm{mm}.
]

Odd-mode omitted plastic bending-energy share through (n,mle7): approximately (2.7%).

## Production gate

Before this route may be used for nine-specimen production:

1. Replace diagnostic area quadrature with:
   - quartic level-set roots,
   - piecewise material active sets,
   - finite 1-D algebraic/Abelian definite integrals.
2. Reproduce the R02 single-point numbers to numerical tolerance.
3. Add only the dominant ((1,3)) plastic/recoverable pair and quantify the change.
4. Do not reconnect steel shell until the BH100 single-point gate is closed.
