# BH060 — Eq.(1)–(149) strict specimen substitution record

## Real specimen binding
```text
b = a_h = 3000 mm
L = 6000 mm
t_c = 42 mm
t_s+ = t_s- = 4 mm
steel face center = ±23 mm; -2 <= zeta <= 2 mm
A_w = 1332 mm^2
core UHPC area factor = 0.989428571428571
q0 = 0.0025
global imperfection b/400 = 7.5 mm
N+ = N- = m+ = m- = 4
A0+ = A0- = 0.421875 mm
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
W_0=7.5sin(\pi x/3000)sin(\pi y/3000),
quad
W=3000(0.0025+q)sin(\pi x/3000)sin(\pi y/3000).
]
[
\varepsilon^0_{x,yy}+\varepsilon^0_{y,xx}-\gamma^0_{xy,xy}
=
\frac{\pi^4(q^2+0.005q)}{2(3000)^2}
[\cos(2\pi x/3000)+\cos(2\pi y/3000)].
]
[
N_x=\Phi_{,yy},quad N_y=\Phi_{,xx},quad N_{xy}=-\Phi_{,xy}.
]
No Nxy=0 or gamma_xy^0=0 condition is introduced.

## Eq.(41)–(67): UHPC current field
[
\kappa_x=\kappa_y=\frac{\pi^2q}{3000}\sin(\pi x/3000)\sin(\pi y/3000),
quad
\kappa_{xy}=-\frac{2\pi^2q}{3000}\cos(\pi x/3000)\cos(\pi y/3000).
]
For -21<=z<=21:
[
\varepsilon_x^U=\varepsilon_x^0+z\frac{\pi^2q}{3000}\sin(\pi x/3000)\sin(\pi y/3000),
]
[
\varepsilon_y^U=\varepsilon_y^0+z\frac{\pi^2q}{3000}\sin(\pi x/3000)\sin(\pi y/3000),
]
[
\gamma_{xy}^U=\gamma_{xy}^0-z\frac{2\pi^2q}{3000}\cos(\pi x/3000)\cos(\pi y/3000).
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
W_s^+=W+(0.421875+A^+)[1-\cos(8\pi x/3000)][1-\cos(8\pi y/3000)],
]
[
W_s^-=W-(0.421875+A^-)[1-\cos(8\pi x/3000)][1-\cos(8\pi y/3000)].
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
\Phi_{,yy}=0.989428571428571\int_{-21}^{21}\sigma_x^Udz+\int_{-2}^{2}\sigma_x^{s,+}d\zeta+\int_{-2}^{2}\sigma_x^{s,-}d\zeta,
]
[
\Phi_{,xx}=0.989428571428571\int_{-21}^{21}\sigma_y^Udz+\int_{-2}^{2}\sigma_y^{s,+}d\zeta+\int_{-2}^{2}\sigma_y^{s,-}d\zeta
+\frac{1332}{3000\times42}\int_{-21}^{21}\sigma_y^w dz,
]
[
-\Phi_{,xy}=0.989428571428571\int_{-21}^{21}\tau_{xy}^Udz+\int_{-2}^{2}\tau_{xy}^{s,+}d\zeta+\int_{-2}^{2}\tau_{xy}^{s,-}d\zeta.
]
Eq.(93)–(95) use exact thickness bounds and steel lever arms 23+zeta / -23+zeta.

## Eq.(96)–(119): global and local equilibrium
Eq.(97), Eq.(105)–(109), and Eq.(110)–(119) are retained without reduction. Since a_h=b, global arguments are pi*x/b and pi*y/b; local arguments are 8*pi*x/b and 8*pi*y/b.

## Eq.(120)–(127): shortening / load
[
\Delta=-\frac{2}{3000}\int_0^{3000}\int_0^{3000}\varepsilon_y^0,dy,dx
+\frac{\pi^2(3000)}{4}(q^2+0.005q).
]
[
P=-\frac1{3000}\int_0^{3000}\int_0^{3000}\Phi_{,xx},dy,dx.
]

## Eq.(128)–(149): path sensitivity / peak
[
\partial_{yy}\varepsilon^0_{x,\Delta}+\partial_{xx}\varepsilon^0_{y,\Delta}-\partial_{xy}\gamma^0_{xy,\Delta}
=
\frac{\pi^4}{(3000)^2}(q+0.0025)\frac{dq}{d\Delta}
[\cos(2\pi x/3000)+\cos(2\pi y/3000)].
]
[
1=-\frac2{3000}\int_0^{3000}\int_0^{3000}\partial_\Delta\varepsilon_y^0,dy,dx
+\frac{\pi^2(3000)}{2}(q+0.0025)\frac{dq}{d\Delta}.
]
[
\frac{dP}{d\Delta}=-\frac1{3000}\int_0^{3000}\int_0^{3000}\partial_{xx}(\partial_\Delta\Phi),dy,dx=0.
]
[
\frac{d^2P}{d\Delta^2}=-\frac1{3000}\int_0^{3000}\int_0^{3000}\partial_{xx}(\partial^2_\Delta\Phi),dy,dx<0.
]

## Execution status
Strict substitutions are complete through Eq.(149). Certified stationary-root solving is blocked by the unresolved formal signed-C1 tensile anchor f_t,2. No value is invented.
Reference FEM peak for post-solve comparison only: 13.09011 MN; it is not used in root selection.
