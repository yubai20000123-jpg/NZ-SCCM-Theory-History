# 2026-09-27 UCFT current state backup — UHPC P11 analytic module and rigid-substrate steel-shell validation

## 0. Status

This is a diagnostic-state backup, not production. It freezes the UHPC module because that part is now analytically closed, while the steel-shell module remains under rigid-substrate validation.

## 1. Structural unknown count

The current equilibrium state remains the 10-component vector

[
z=[\bar\varepsilon_x,U_{10},U_{11},\bar\varepsilon_y,V_{01},V_{11},q,A^+,A^-,P]^T.
]

At a prescribed path parameter \(\lambda\), solve 10 equations \(F(z,\lambda)=0\).

For direct extremum search, do **not** reinterpret the optional sensitivity vector as new structural DOFs. The minimal extremum system has 11 unknowns \((z,\lambda)\):

[
F(z,\lambda)=0,
qquad
g(z,\lambda)=e_P^T J^{-1}F_{,\lambda}=0,
]

where \(J=F_{,z}\) and \(e_P=[0,0,0,0,0,0,0,0,0,1]^T\). The old 21-variable bordered form is only an implementation device.

## 2. UHPC material law: conservative P11

Use signed strain \(x=\varepsilon/0.0035\) and

[
\sigma_U=141.1\,\phi_{11}(x)\;{\rm MPa},
]

[
\begin{aligned}
\phi_{11}(x)=&
0.448663943322152x
+1.199431564300784x^2
+0.666505117875778x^3
-1.248418326596833x^4\\
&-1.131743944986424x^5
+0.794813517193524x^6
+0.653430009090885x^7
-0.405008160302494x^8\\
&-0.127627913149918x^9
+0.118909252443626x^{10}
-0.020315422065361x^{11}.
\end{aligned}
]

Definition domain currently used in UCFT: \(-0.0035\le\varepsilon\le0.007\). It has exactly the required decrease–increase–decrease topology over that domain. Compression peak is intentionally conservative (~134.13 MPa, about -4.9% vs UC141), while the tensile peak is essentially unchanged.

## 3. One-order U2 kinematics

[
X=\pi x/b,\qquad Y=\pi y/a_h,\qquad Q=q^2+2q_0q.
]

[
\varepsilon_x^0=
\bar\varepsilon_x-\frac{\pi^2Q}{8}
+U_{10}\cos2X+U_{11}\cos2X\cos2Y
+\frac{\pi^2Q}{2}\cos^2X\sin^2Y,
]

[
\varepsilon_y^0=
\bar\varepsilon_y-\frac{\pi^2b^2Q}{8a_h^2}
+V_{01}\cos2Y+V_{11}\cos2X\cos2Y
+\frac{\pi^2b^2Q}{2a_h^2}\sin^2X\cos^2Y,
]

[
\gamma_{xy}^0=
\left[-\frac{b}{a_h}U_{11}-\frac{a_h}{b}V_{11}
+\frac{\pi^2bQ}{4a_h}\right]\sin2X\sin2Y,
]

[
\kappa_x=\frac{\pi^2q}{b}\sin X\sin Y,quad
\kappa_y=\frac{\pi^2bq}{a_h^2}\sin X\sin Y,quad
\kappa_{xy}=-\frac{2\pi^2q}{a_h}\cos X\cos Y.
]

Effective normal strains:

[
e_x=\frac{\varepsilon_x^0+\nu_c\varepsilon_y^0}{1-\nu_c^2},\quad
\chi_x=\frac{\kappa_x+\nu_c\kappa_y}{1-\nu_c^2},
]

[
e_y=\frac{\varepsilon_y^0+\nu_c\varepsilon_x^0}{1-\nu_c^2},\quad
\chi_y=\frac{\kappa_y+\nu_c\kappa_x}{1-\nu_c^2}.
]

Through-thickness arguments are \(\eta_x=e_x+z\chi_x\), \(\eta_y=e_y+z\chi_y\).

## 4. Exact UHPC thickness resultants

Write

[
\sigma_U(\eta)=a_1\eta+a_2\eta^2+\cdots+a_{11}\eta^{11},
\qquad
a_n=\frac{f_c c_n}{\varepsilon_p^n}.
]

Then all thickness integrals are finite polynomials. In particular, if \(N(e,\chi)=\int\sigma_U(e+z\chi)dz\) and \(M(e,\chi)=\int z\sigma_U(e+z\chi)dz\), the explicit P11 expansions previously derived are the locked section formulas. Numerical quadrature was used only as an independent check: representative errors were ~1e-12 in N and M.

## 5. Exact section tangent quantities

Define the material tangent polynomial

[
C(\eta)=\sigma_U'(\eta)
=a_1+2a_2\eta+3a_3\eta^2+\cdots+11a_{11}\eta^{10}.
]

For each normal direction define

[
C_0=\int C(e+z\chi)dz,\quad
C_1=\int zC(e+z\chi)dz,\quad
C_2=\int z^2C(e+z\chi)dz.
]

Each is again a finite P10 thickness polynomial. Then

[
N_{,e}=C_0,\quad N_{,\chi}=C_1,\quad
M_{,e}=C_1,\quad M_{,\chi}=C_2.
]

Therefore

[
N_{x,j}=C_0^x e_{x,j}+C_1^x\chi_{x,j},
\quad
M_{x,j}=C_1^x e_{x,j}+C_2^x\chi_{x,j},
]

and the same for y.

## 6. Shear term remains analytic

Since \(\sigma_U(\eta)/\eta=a_1+a_2\eta+\cdots+a_{11}\eta^{10}\), define

[
S(\eta)=a_1+a_2\eta+\cdots+a_{11}\eta^{10},
\quad
T(\eta)=a_2+2a_3\eta+\cdots+10a_{11}\eta^9.
]

Let

[
L_r=\frac1{4(1+\nu_c)}
\int z^r[S(\eta_x)+S(\eta_y)]dz.
]

Then

[
N_{xy}=\gamma_{xy}^0L_0+\kappa_{xy}L_1,
\qquad
M_{xy}=\gamma_{xy}^0L_1+\kappa_{xy}L_2.
]

For a generalized variable \(r_j\),

[
L_{r,j}=\frac1{4(1+\nu_c)}
\left[
T_r^x e_{x,j}+T_{r+1}^x\chi_{x,j}
+T_r^y e_{y,j}+T_{r+1}^y\chi_{y,j}
\right],
]

with \(T_m^x=\int z^mT(\eta_x)dz\), etc., again finite polynomials.

## 7. Expanded UHPC Jacobian residual formula

For retained U2 variables \(r_i,r_j\),

[
\begin{aligned}
K_{ij}^U=\int_A \{&
N_{x,j}\varepsilon_{x,i}^0+N_x\varepsilon_{x,ij}^0+
M_{x,j}\kappa_{x,i}+M_x\kappa_{x,ij}\\
&+N_{y,j}\varepsilon_{y,i}^0+N_y\varepsilon_{y,ij}^0+
M_{y,j}\kappa_{y,i}+M_y\kappa_{y,ij}\\
&+N_{xy,j}\gamma_{xy,i}^0+N_{xy}\gamma_{xy,ij}^0+
M_{xy,j}\kappa_{xy,i}+M_{xy}\kappa_{xy,ij}
\}\,dA.
\end{aligned}
]

Only q-q kinematic second derivatives are nonzero:

[
\varepsilon_{x,qq}^0=\pi^2[-1/4+\cos^2X\sin^2Y],
]

[
\varepsilon_{y,qq}^0=\pi^2b^2/a_h^2[-1/4+\sin^2X\cos^2Y],
]

[
\gamma_{xy,qq}^0=\pi^2b/(2a_h)\sin2X\sin2Y.
]

All curvature second derivatives are zero. The x-y integrations are finite Fourier integrals, so the UHPC residual and Jacobian are fully analytic.

## 8. Rigid-substrate steel validation status

Yun Lu's FEM is an ideal validation problem because the concrete is used only as a fixed, nearly rigid normal support with hard contact and frictionless tangential behavior. Therefore the steel plate can and should be validated independently before coupling to deformable UHPC.

The current reduced current-state deformation theory was constructed to recover Yun Lu Eq. (2-32) exactly in the elastic limit. A width-resolved variant also used the exact critical-section Airy stress shape and Yun Lu's Q235 piecewise law. Result: b/t <= 100 peaks are within roughly 7%, but b/t=125 is still ~+11% and b/t=150 ~+24%, and the very slender post-peak descent is not reproduced.

Therefore this steel current-state reduction is **not yet accepted**. The failure is physical: a convex single-amplitude deformation-theory section retains too much post-yield reserve and cannot reproduce the localization/effective-width loss that Yun Lu FEM shows for slender plates. The next steel-only task is to derive an analytic moving plastic-zone/effective-width state from the exact Airy stress field, still without FEM calibration and without loading-history integration.

Do not couple the present steel reduction into the final UCFT direct-extremum system until that rigid-substrate gate passes.
