# NZ-SCCM — Case21 R04 exact D15 integral ledger

**Date:** 2026-08-20 00:10 +08  
**Identity:** `CASE21_D15_EXACT_INTEGRAL_LEDGER`  
**Material lock:** `R04`, commit `1a94a7c7218502bd339520244378363ecd9657ab`

## 1. Case21 structure and variables

```text
a_phys = 2440 mm
b      = 1220 mm
t      = 19.30 mm
m*     = 2
ell    = 1220 mm
k      = b/ell = 1
q0     = 0.0025
nu     = 0.18
```

The formal structural unknowns are

\[
\boxed{(D,q,\alpha)}.
\]

Let

\[
U=\sin^2X,\qquad V=\sin^2Y,\qquad H=\sin X\sin Y.
\]

Define

\[
M(q)=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\qquad
M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),
\qquad
M_{qq}=\frac{\pi^2}{\varepsilon_0},
\]

\[
\beta(q)=\frac{\pi^2q}{\varepsilon_0b},
\qquad
\beta_q=\frac{\pi^2}{\varepsilon_0b}.
\]

With physical thickness coordinate `z` and normalized thickness `zeta=2z/t`, define

\[
B(q)=\beta\frac t2,
\qquad
B_q=\beta_q\frac t2.
\]

The retained R15 strain field is

\[
e_x=\nu D+M F_x+\alpha A_x+B H\zeta,
\]

\[
e_y=-D+M F_y+\alpha A_y+B H\zeta,
\]

\[
\gamma=2\cos X\cos Y[(M-\alpha)H-B\zeta],
\]

where

\[
F_x=(1-U)V,
\qquad
F_y=U(1-V),
\]

\[
A_x=-\frac14-\frac\nu2U-\frac12V+UV,
\]

\[
A_y=\frac\nu4-\frac12U-\frac\nu2V+UV.
\]

Physical strains are `eps0*e`.

## 2. R10 equivalent-strain matrix without principal coordinates

\[
E_{11}=\frac{e_x+\nu e_y}{1-\nu^2},
\qquad
E_{22}=\frac{\nu e_x+e_y}{1-\nu^2},
\]

\[
E_{12}=\frac{\gamma}{2(1+\nu)}.
\]

The invariant pair is

\[
J_1=E_{11}+E_{22},
\qquad
J_2=E_{11}E_{22}-E_{12}^2.
\]

For exact polynomial compilation, the shear square is written directly as

\[
\boxed{
E_{12}^2=
\frac{(1-U)(1-V)}{(1+\nu)^2}
\left[
(M-\alpha)^2UV
-2(M-\alpha)BH\zeta
+B^2\zeta^2
\right].
}
\]

Thus `J1,J2` live exactly in the finite basis described below; no explicit cosine radical is introduced.

## 3. Exact finite algebra basis

Use the monomial family

\[
\boxed{U^aV^b\zeta^kH^h,\qquad h\in\{0,1\}.}
\]

Multiplication is finite because

\[
\boxed{H^2=UV.}
\]

Therefore each R04 CH coefficient, each stress component and each virtual-work integrand is a finite sum in this basis.

This basis is an algebraic bookkeeping device only. It is not spatial sampling, a spatial cell, or a material point.

## 4. Exact D15 moment for each basis monomial

For

\[
U^aV^b\zeta^kH^h
=\sin^{2a+h}X\sin^{2b+h}Y\zeta^k,
\]

define

\[
I_n=\int_0^\pi\sin^nX\,dX
=\frac{\sqrt\pi\,\Gamma((n+1)/2)}{\Gamma(n/2+1)}.
\]

Thickness moment:

\[
Z_k=\int_{-1}^1\zeta^k\,d\zeta
=\begin{cases}
0,&k\text{ odd},\\
\dfrac2{k+1},&k\text{ even}.
\end{cases}
\]

Hence

\[
\boxed{
\mathscr D_{15}[U^aV^b\zeta^kH^h]
=I_{2a+h}I_{2b+h}Z_k.
}
\]

This is the formal structure integral. Therefore

```text
N_formal_spatial_sampling     = 0
N_formal_spatial_quadrature   = 0
N_formal_spatial_subdomains   = 1
N_formal_material_points      = 0
N_formal_thickness_quadrature = 0
```

## 5. R04 material lift

The final scalar source polynomials are

\[
\widetilde C=(2\lambda+\lambda^2)^2
\left[1-\left(\frac{\lambda+1}{\lambda_t+1}\right)^2\right]^2,
\]

\[
\widetilde T=5\rho\lambda^2(\lambda+1)^2,
\]

\[
\widetilde U=\frac13\kappa\lambda
\left[\frac{(\lambda+1)(\lambda_t-\lambda)}{\lambda_t}\right]^3
-\widetilde C+\rho\widetilde T.
\]

Lift each polynomial by the exact 2x2 Cayley–Hamilton recurrence

\[
E^n=a_nI+b_nE,
\]

\[
a_{n+1}=-J_2b_n,
\qquad
b_{n+1}=a_n+J_1b_n.
\]

The complete R10 interaction identity remains

\[
\boxed{
S=\widetilde U-a_{cc}\det(\widetilde C)\widetilde C
+\widetilde C\operatorname{adj}(\widetilde T)
-\rho a_t\det(\widetilde T)\operatorname{adj}(\widetilde T^7).
}
\]

Write

\[
S=A_SI+B_SE.
\]

Then

\[
S_{xx}=A_S+B_SE_{11},
\quad
S_{yy}=A_S+B_SE_{22},
\quad
S_{xy}=B_SE_{12}.
\]

## 6. Concrete generalized forces

Physical volume transformation:

\[
dV=\frac{b\ell t}{2\pi^2}\,dX\,dY\,d\zeta.
\]

Concrete axial force:

\[
\boxed{
P_c=-\frac{f_cb t}{2\pi^2}\mathscr D_{15}[S_{yy}].
}
\]

The normalized q-direction strain derivatives are

\[
e_{x,q}=M_qF_x+B_qH\zeta,
\]

\[
e_{y,q}=M_qF_y+B_qH\zeta.
\]

The shear product can be compiled without an explicit cosine basis:

\[
\boxed{
E_{12}\frac{\gamma_{,q}}{\varepsilon_0}
=
\frac{2(1-U)(1-V)}{1+\nu}
[(M-\alpha)H-B\zeta][M_qH-B_q\zeta].
}
\]

Consequently

\[
\boxed{
R_q^c=\frac{f_c\varepsilon_0b\ell t}{2\pi^2}
\mathscr D_{15}[S_{xx}e_{x,q}+S_{yy}e_{y,q}+B_S\,E_{12}\gamma_{,q}/\varepsilon_0].
}
\]

For the Airy coordinate,

\[
e_{x,\alpha}=A_x,
\qquad
e_{y,\alpha}=A_y,
\]

and

\[
\boxed{
E_{12}\frac{\gamma_{,\alpha}}{\varepsilon_0}
=-\frac{2(1-U)(1-V)}{1+\nu}
[(M-\alpha)H-B\zeta]H.
}
\]

Thus

\[
\boxed{
R_\alpha^c=\frac{f_c\varepsilon_0b\ell t}{2\pi^2}
\mathscr D_{15}[S_{xx}A_x+S_{yy}A_y+B_S\,E_{12}\gamma_{,\alpha}/\varepsilon_0].
}
\]

## 7. Reinforcement layers — exact analytic interface

The workbook interface is general:

```text
(rho_x1,z_x1), (rho_x2,z_x2)
(rho_y1,z_y1), (rho_y2,z_y2)
```

For an x-oriented layer

\[
e_{s,x}=\nu D+MF_x+\alpha A_x+\beta z_sH.
\]

For a y-oriented layer

\[
e_{s,y}=-D+MF_y+\alpha A_y+\beta z_sH.
\]

On the elastic branch

\[
\sigma_s=E_s\varepsilon_0e_s.
\]

All layer forces/residuals are exact two-dimensional moments of finite `U,V,H` polynomials. In particular a y layer contributes

\[
P_{s,y}=-\rho_stbE_s\varepsilon_0\langle e_{s,y}\rangle,
\]

where

\[
\langle f\rangle=\frac1{\pi^2}\int_0^\pi\int_0^\pi f\,dX\,dY.
\]

The same exact moments generate `Rq_s,Ralpha_s` and their same-source derivatives.

Case21 uses

```text
rho_sx = rho_sy = 0.00375
z_sx   = z_sy   = 0
Es      = 200000 MPa
fy      = 530 MPa
```

The second layer of each direction is retained in the general ledger with zero Case21 density.

The reinforcement constitutive sheet must explicitly check

\[
\max|\varepsilon_s|\le f_y/E_s.
\]

If this gate fails, the workbook switches to its finite analytic post-yield branch; elastic response is never silently extended through yield.

## 8. Same-source Jacobian

All derivatives come from the same R04 polynomial circuit and the same R15 kinematics. For each `g in {D,q,alpha}`,

\[
J_{1,g}=\operatorname{tr}E_{,g},
\]

\[
J_{2,g}=E_{22}E_{11,g}+E_{11}E_{22,g}-2E_{12}E_{12,g},
\]

and

\[
a_{n+1,g}=-J_{2,g}b_n-J_2b_{n,g},
\]

\[
b_{n+1,g}=a_{n,g}+J_{1,g}b_n+J_1b_{n,g}.
\]

Product rule through the same pair circuit gives the exact derivatives of `S`, hence the derivatives of `P,Rq,Ralpha` after the same D15 operator.

The formal limit matrix is

\[
\boxed{
J_{lim}=\begin{bmatrix}
P_D&P_q&P_\alpha\\
R_{q,D}&R_{q,q}&R_{q,\alpha}\\
R_{\alpha,D}&R_{\alpha,q}&R_{\alpha,\alpha}
\end{bmatrix}.
}
\]

The direct production equations are

\[
\boxed{R_q=0,\qquad R_\alpha=0,\qquad\det J_{lim}=0.}
\]

## 9. Status

```text
R04 finite operator                = LOCKED
Case21 R15 continuous kinematics   = LOCKED
finite U/V/H/zeta algebra          = COMPLETE
D15 exact moment                   = COMPLETE
concrete P/R formulas              = COMPLETE
reinforcement analytic interface   = COMPLETE
same-source derivative recurrence  = COMPLETE
formal spatial quadrature          = ZERO
```

**Unique resume point:** solve the physical equilibrium branch and the direct limit equations, then write the same formulas into the final Excel ledger.