# 20260924 correction — UHPC tensile input is strain-based, not displacement-based

User corrected the Abaqus CDP tension-stiffening definition: **Type = STRAIN**.

Therefore the previous displacement/characteristic-length interpretation is rejected. No characteristic length is required.

Abaqus input is cracking stress versus cracking strain:
```
5.571309,0
6.203384,0.000246
6.631260,0.000333
6.919437,0.000424
7.107793,0.000517
7.222692,0.000611
7.282395,0.000707
7.3,0.000804
7.285159,0.000901
7.245135,0.000999
7.18549,0.001098
7.110544,0.001197
7.02369,0.001296
6.92762,0.001396
6.824487,0.001495
6.716025,0.001595
6.603636,0.001695
6.488463,0.001794
5.898099,0.002294
5.3246,0.002793
4.793703,0.003292
4.312849,0.003789
2.851377,0.005766
```

For the Eq.(47)–(60) signed-C1 law, the independent variable is total tensile strain. With Ec=43400 MPa:
[
\varepsilon_t=\varepsilon_t^{ck}+\sigma_t/E_c.
]

Initial cracking total strain:
[
\varepsilon_{cr}=5.571309/43400=1.283711751152074\times10^{-4}.
]

Peak:
[
f_t=7.3\ {m MPa},
\quad
\varepsilon_{tp}=0.000804+7.3/43400
=9.722027649769585\times10^{-4}.
]

Thus:
[
\varepsilon_{tp}/2=4.861013824884793\times10^{-4},
\quad
2\varepsilon_{tp}=1.944405529953917\times10^{-3}.
]

Linear interpolation on the total-strain-converted tabulation gives:
[
f_{t,1/2}=6.632167188513625\ {m MPa},
\quad
f_{t,2}=6.487368472559167\ {m MPa}.
]

The signed-C1 tensile coefficients then are:
[
a_t=2.1176777744062334,
\quad
b_t=4.5344984475477235,
\quad
c_t=1.6085712902696916,
\quad
d_t=0.7545532420682709.
]

Tensile denominator roots in x=r/eps_tp:
[
-0.23844474,
\quad
-0.94668737\pm2.15912761i.
]
Therefore there is **no positive real tensile pole for r>=0**.

Status:
- old displacement/characteristic-length blocker: REJECTED
- old ft2 unresolved blocker: RESOLVED by the corrected strain input
- nine-BH Eq.(1)–(149) stationary-root solve may proceed with this corrected C1 tensile branch.
