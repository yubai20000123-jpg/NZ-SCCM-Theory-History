# BH010 — Eq.(1)–(149) strict specimen substitution record

## Real specimen binding
```text
b = a_h = 500 mm
L = 1000 mm
t_c = 42 mm
t_s+ = t_s- = 4 mm
steel face center = ±23 mm; -2 <= zeta <= 2 mm
A_w = 1332 mm^2
core UHPC area factor = 0.936571428571429
q0 = 0.0025
global imperfection b/400 = 1.25 mm
N+ = N- = m+ = m- = 4
A0+ = A0- = 0.0703125 mm
Ec=43400 MPa; nu_c=0.20; fc=141.1 MPa; eps_cp=0.0035; f_c,1/2=75.95 MPa; f_c,2=70.55 MPa
Es=206000 MPa; nu_s=0.30; fy=355 MPa
```

C1 compression coefficients:
```text
a_c=3.9286287306087058
b_c=7.510340381132359
c_c=-11.938969111741057
d_c=8.433798921174882
```

## Eq.(1)–(40): geometry / compatibility / Airy
[
W_0=1.25sin(\pi x/500)sin(\pi y/500),
quad
W=500(0.0025+q)sin(\pi x/500)sin(\pi y/500).
]
[
\varepsilon^0_{x,yy}+\varepsilon^0_{y,xx}-\gamma^0_{xy,xy}
=
\frac{\pi^4(q^2+0.005q)}{2(500)^2}
[\cos(2\pi x/500)+\cos(2\pi y/500)].
]
[
N_x=\Phi_{,yy},quad N_y=\Phi_{,xx},quad N_{xy}=-\Phi_{,xy}.
]
No Nxy=0 or gamma_xy^0=0 condition is introduced.

## Eq.(41)–(67): UHPC current field
[
\kappa_x=\kappa_y=\frac{\pi^2q}{500}\sin(\pi x/500)\sin(\pi y/500),
quad
\kappa_{xy}=-\frac{2\pi^2q}{500}\cos(\pi x/500)\cos(\pi y/500).
]
For -21<=z<=21:
[
\varepsilon_x^U=\varepsilon_x^0+z\frac{\pi^2q}{500}\sin(\pi x/500)\sin(\pi y/500),
]
[
\varepsilon_y^U=\varepsilon_y^0+z\frac{\pi^2q}{500}\sin(\pi x/500)\sin(\pi y/500),
]
[
\gamma_{xy}^U=\gamma_{xy}^0-z\frac{2\pi^2q}{500}\cos(\pi x/500)\cos(\pi y/500).
]
With nu_c=0.20:
[
\varepsilon_{x,eq}=(\varepsilon_x^U+0.2\varepsilon_y^U)/0.96,quad
\varepsilon_{y,eq}=(\varepsilon_y^U+0.2\varepsilon_x^U)/0.96,
]
[
G_U=\frac1{4.8}[\sigma_U(\varepsilon_{x,eq})/\varepsilon_{x,eq}
+\sigma_U(\varepsilon_{y,eq})/\varepsilon_{y,eq}].
]
Compression signed-C1 is numerical. Tensile signed-C1 is kept symbolic because formal f_t,2 is unresolved.

## Eq.(68)–(77): steel-local geometry
[
W_s^+=W+(0.0703125+A^+)[1-\cos(8\pi x/500)][1-\cos(8\pi y/500)],
]
[
W_s^-=W-(0.0703125+A^-)[1-\cos(8\pi x/500)][1-\cos(8\pi y/500)].
]
Eq.(72)–(77) use tc=42, ts=4, a_h=b, N=m=4 exactly; no x/y/z point sampling.

## Eq.(78)–(95): current material / resultants
Steel elastic predictor:
[
E_s/(1-\nu_s^2)=226373.626373626,qquad E_s/[2(1+\nu_s)]=79230.7692307692 {\rm MPa}.
]
Mises limiter stays Eq.(81)–(85).

Eq.(89)–(91):
[
\Phi_{,yy}=0.936571428571429\int_{-21}^{21}\sigma_x^Udz+\int_{-2}^{2}\sigma_x^{s,+}d\zeta+\int_{-2}^{2}\sigma_x^{s,-}d\zeta,
]
[
\Phi_{,xx}=0.936571428571429\int_{-21}^{21}\sigma_y^Udz+\int_{-2}^{2}\sigma_y^{s,+}d\zeta+\int_{-2}^{2}\sigma_y^{s,-}d\zeta
+\frac{1332}{500\times42}\int_{-21}^{21}\sigma_y^w dz,
]
[
-\Phi_{,xy}=0.936571428571429\int_{-21}^{21}\tau_{xy}^Udz+\int_{-2}^{2}\tau_{xy}^{s,+}d\zeta+\int_{-2}^{2}\tau_{xy}^{s,-}d\zeta.
]
Eq.(93)–(95) use exact thickness bounds and steel lever arms 23+zeta / -23+zeta.

## Eq.(96)–(119): global and local equilibrium
Eq.(97), Eq.(105)–(109), and Eq.(110)–(119) are retained without reduction. Since a_h=b, global arguments are pi*x/b and pi*y/b; local arguments are 8*pi*x/b and 8*pi*y/b.

## Eq.(120)–(127): shortening / load
[
\Delta=-\frac{2}{500}\int_0^{500}\int_0^{500}\varepsilon_y^0,dy,dx
+\frac{\pi^2(500)}{4}(q^2+0.005q).
]
[
P=-\frac1{500}\int_0^{500}\int_0^{500}\Phi_{,xx},dy,dx.
]

## Eq.(128)–(149): path sensitivity / peak
[
\partial_{yy}\varepsilon^0_{x,\Delta}+\partial_{xx}\varepsilon^0_{y,\Delta}-\partial_{xy}\gamma^0_{xy,\Delta}
=
\frac{\pi^4}{(500)^2}(q+0.0025)\frac{dq}{d\Delta}
[\cos(2\pi x/500)+\cos(2\pi y/500)].
]
[
1=-\frac2{500}\int_0^{500}\int_0^{500}\partial_\Delta\varepsilon_y^0,dy,dx
+\frac{\pi^2(500)}{2}(q+0.0025)\frac{dq}{d\Delta}.
]
[
\frac{dP}{d\Delta}=-\frac1{500}\int_0^{500}\int_0^{500}\partial_{xx}(\partial_\Delta\Phi),dy,dx=0.
]
[
\frac{d^2P}{d\Delta^2}=-\frac1{500}\int_0^{500}\int_0^{500}\partial_{xx}(\partial^2_\Delta\Phi),dy,dx<0.
]

## Execution status
Strict substitutions are complete through Eq.(149). Certified stationary-root solving is blocked by the unresolved formal signed-C1 tensile anchor f_t,2. No value is invented.
Reference FEM peak for post-solve comparison only: 4.330169 MN; it is not used in root selection.
