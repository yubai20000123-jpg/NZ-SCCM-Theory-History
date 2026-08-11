# NZ-SCCM Case21 — N48-C1/MM + D15 fresh blind theory result

**Identity:** FRESH BLIND THEORY RESULT — NO HISTORICAL CASE21 COMPUTED VALUE / NO EXPERIMENT IN SOLVE

## Source specimen/material input
- \(b=\ell=1220\) mm; \(t_p=19.30\) mm
- \(f_c=21.23\) MPa; \(E_0=20321\) MPa; \(\varepsilon_0=0.00209\); \(\nu=0.18\)
- \(q_0=1/400=0.0025\)
- total two-way reinforcement ratio \(=0.75\%\); each direction \(=0.375\%\)
- one reinforcement layer at the mid-plane
- \(E_s=200000\) MPa; \(\varepsilon_y=0.00265\); \(f_y=530\) MPa

```text
R10 = frozen
compiler order = 48
U,C,T7 = N48-C1
T = N48-C1 constrained minimax
formal spatial sampling = 0
formal spatial quadrature = 0
formal spatial subdomains = 1
historical Case21 roots/loads/paths used = NO
experiment used during solve = NO
```

## Fresh R10
\[
\kappa=2.000512953368,\quad x_{cr}=0.049987179454,\quad \eta=0.002499358973.
\]
\[
\int_0^{10}T_{src}(r)dr=6.349875213599,\quad
W_{src}=0.031741235181,\quad h=0.097997504272.
\]

## Fresh compiler
\[
\lambda\in[-1.15,0.12],\quad
\lambda_c=-0.515000000000,\quad \lambda_h=0.635000000000,\quad \xi_0=0.811023622047.
\]

Independent 1D material maximum errors:
- U: 0.002453604
- C: 0.014012978
- T: 0.089860050
- T7: 0.112735998
- T constrained-minimax objective: 0.089569236

Strict C1 anchors are satisfied to machine precision.

## Fresh theoretical limit state
\[
D_u=0.78234000,\quad q_u=0.0017704700,\quad A_u=2.159973\ {\rm mm}.
\]
\[
C_m=0.028302894588,\quad C_b=0.066131673686.
\]

Continuous spectral certificate:
\[
-0.874981134\le\lambda\le0.092641134\subset[-1.15,0.12].
\]

Steel:
\[
\max|\varepsilon_s|=0.001635091<0.00265,
\]
so the final steel branch is elastic.

D15 contractions:
\[
\mathscr D[S_{yy}]=-13.307143369080,\qquad
\mathscr D[Q_q]=4.479986884859.
\]

\[
P_c=336.994047\ {\rm kN},\qquad
P_s=28.613729\ {\rm kN},
\]
\[
\boxed{P_{u,th}=365.607776\ {\rm kN}}.
\]

\[
R_{q,c}=289.281228,\qquad
R_{q,s}=-289.268074,
\]
\[
R_q=1.315371e-02\ {\rm kN\,mm},\qquad
R_{norm}=2.273568e-05.
\]

Same-expression derivatives:
\[
P_{,D}=144.713767326,\quad
P_{,q}=-79494.930315266,
\]
\[
R_{q,D}=-1865.424753305,\quad
R_{q,q}=1024243.336025845.
\]

\[
L=P_{,D}R_{q,q}-P_{,q}R_{q,D}=-69698.957493,
\]
\[
L_{norm}=-2.350613e-04,\qquad
\left.\frac{dP}{dD}\right|_{R_q=0}=-0.068049.
\]

No experimental failure load appears in this blind result.
