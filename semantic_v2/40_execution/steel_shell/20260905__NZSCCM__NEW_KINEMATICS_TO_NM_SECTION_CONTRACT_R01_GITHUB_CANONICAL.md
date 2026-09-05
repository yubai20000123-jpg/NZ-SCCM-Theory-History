# NZ-SCCM new-kinematics → N/M section contract R01 — GitHub canonical text

Date: 2026-09-05

## Locked scope

This contract stops at

\[
(\lambda,u_2,v_2,q,x,y)\rightarrow N_x(x,y),M_x(x,y),N_y(x,y),M_y(x,y).
\]

No area integration, no Gauss, no virtual work, no replacement R4/J4, no current-stability solve, no ultimate-load solve.

The only upstream change relative to the old section module is the origin of strain and curvature: they now come directly from the displacement field. The original 01 UHPC compression law, four-segment Hermite tension law and exact `F_0/F_1` thickness primitives remain the material/section backend. The tension anchors are only nondimensionalized; this is a coordinate transformation, not a new constitutive law.

## Kinematics

\[
u=\frac{u_2}{2\alpha}\sin 2\alpha x,
\qquad
v=-\lambda y+\frac{v_2}{2\beta}\sin2\beta y,
\]

\[
w_0=bq_0\sin\alpha x\sin\beta y,
\qquad
w_d=bq\sin\alpha x\sin\beta y.
\]

With

\[
Q=q^2+2q_0q,
\]

\[
\varepsilon_x^0=u_2\cos2\alpha x+
\frac{b^2\alpha^2}{2}Q\cos^2\alpha x\sin^2\beta y,
\]

\[
\varepsilon_y^0=-\lambda+v_2\cos2\beta y+
\frac{b^2\beta^2}{2}Q\sin^2\alpha x\cos^2\beta y,
\]

\[
\kappa_x=bq\alpha^2\sin\alpha x\sin\beta y,
\qquad
\kappa_y=bq\beta^2\sin\alpha x\sin\beta y.
\]

No Airy stress function is used to generate these strains or curvatures.

## UHPC compression — original 01 source law

For

\[
-\varepsilon_{c0}\le\varepsilon\le0,
\]

\[
A_c=\frac{E_c\varepsilon_{c0}}{f_c},
\quad
B_c=6-5A_c,
\quad
C_c=4A_c-5,
\]

\[
\sigma_c(\varepsilon)=E_c\varepsilon+
\frac{f_cB_c}{\varepsilon_{c0}^5}\varepsilon^5-
\frac{f_cC_c}{\varepsilon_{c0}^6}\varepsilon^6.
\]

\[
F_0^c(\varepsilon)=\frac{E_c}{2}\varepsilon^2+
\frac{f_cB_c}{6\varepsilon_{c0}^5}\varepsilon^6-
\frac{f_cC_c}{7\varepsilon_{c0}^6}\varepsilon^7,
\]

\[
F_1^c(\varepsilon)=\frac{E_c}{3}\varepsilon^3+
\frac{f_cB_c}{7\varepsilon_{c0}^5}\varepsilon^7-
\frac{f_cC_c}{8\varepsilon_{c0}^6}\varepsilon^8.
\]

## UHPC tension — original four Hermite segments, nondimensionalized

Define

\[
\xi=\varepsilon/\varepsilon_{tu},
\qquad
\widehat\sigma=\sigma/f_{tp},
\]

and anchor parameters

\[
r_0=0,\ r_4=1,
\qquad
s_0=0,\ s_2=1,\ s_4=0,
\]

with independent shape inputs

\[
r_1,r_2,r_3,s_1,s_3.
\]

For segment `i=0,1,2,3`,

\[
\Delta r_i=r_{i+1}-r_i,
\qquad
\widehat\delta_i=\frac{s_{i+1}-s_i}{\Delta r_i}.
\]

\[
\widehat d_0=\frac{E_c\varepsilon_{tu}}{f_{tp}},
\qquad
\widehat d_4=0.
\]

For internal node `i=1,2,3`, if

\[
\widehat\delta_{i-1}\widehat\delta_i\le0,
\]

then

\[
\widehat d_i=0;
\]

otherwise

\[
\widehat d_i=
\frac{3(\Delta r_i+\Delta r_{i-1})}
{(2\Delta r_i+\Delta r_{i-1})/\widehat\delta_{i-1}
+(\Delta r_i+2\Delta r_{i-1})/\widehat\delta_i}.
\]

With

\[
\theta_i=\frac{\xi-r_i}{\Delta r_i},
\]

\[
a_{0i}=s_i,
\quad
a_{1i}=\Delta r_i\widehat d_i,
\]

\[
a_{2i}=3(s_{i+1}-s_i)-\Delta r_i(2\widehat d_i+\widehat d_{i+1}),
\]

\[
a_{3i}=2(s_i-s_{i+1})+\Delta r_i(\widehat d_i+\widehat d_{i+1}),
\]

so

\[
\widehat\sigma_t=a_{0i}+a_{1i}\theta_i+a_{2i}\theta_i^2+a_{3i}\theta_i^3,
\]

\[
\sigma_t=f_{tp}\widehat\sigma_t.
\]

The two tension primitives are scaled as

\[
F_0^t=f_{tp}\varepsilon_{tu}\widehat F_0^t,
\qquad
F_1^t=f_{tp}\varepsilon_{tu}^2\widehat F_1^t,
\]

where `\widehat F_0^t` and `\widehat F_1^t` are the exact quartic/quintic segment primitives and cumulative segment sums. Therefore the nondimensionalization changes no stress value and no section resultant.

## UHPC exact section resultants

\[
\varepsilon_j^{U,\pm}=\varepsilon_j^0\pm\frac{t_c}{2}\kappa_j,
\qquad j=x,y.
\]

For `\kappa_j\ne0`,

\[
N_j^U=(1-\rho_w)
\frac{F_0(\varepsilon_j^{U,+})-F_0(\varepsilon_j^{U,-})}{\kappa_j},
\]

\[
M_j^U=(1-\rho_w)
\frac{F_1(\varepsilon_j^{U,+})-F_1(\varepsilon_j^{U,-})
-\varepsilon_j^0[F_0(\varepsilon_j^{U,+})-F_0(\varepsilon_j^{U,-})]}
{\kappa_j^2}.
\]

For `\kappa_j=0`, use the analytic limit

\[
N_j^U=(1-\rho_w)t_c\sigma_U(\varepsilon_j^0),
\qquad
M_j^U=0.
\]

No thickness quadrature is used.

## Steel shell interface to existing Multiwave module

\[
e_{x,s}^{\pm}=\varepsilon_x^0\pm z_f\kappa_x,
\qquad
e_{y,s}^{\pm}=\varepsilon_y^0\pm z_f\kappa_y.
\]

Each strip keeps the existing automatic yield-first/local-buckling gate. In the local-buckling branch the stationary amplitude obeys

\[
B_3U^3+B_1U+B_0=0,
\]

all nonnegative real stationary roots plus `U=0` are finite candidates, and the minimum-energy candidate is selected. R06 local first yield remains a clearly identified one-dimensional scalar root; it is not renamed as a pure explicit formula.

Weighted face stresses give

\[
N_x^s=t_s(\bar\sigma_x^++\bar\sigma_x^-),
\quad
N_y^s=t_s(\bar\sigma_y^++\bar\sigma_y^-),
\]

\[
M_x^s=t_sz_f(\bar\sigma_x^+-\bar\sigma_x^-),
\quad
M_y^s=t_sz_f(\bar\sigma_y^+-\bar\sigma_y^-).
\]

## Web/PBL exact section resultants

\[
e_y^w(z)=\varepsilon_y^0+z\kappa_y
\]

with ideal elastic-perfectly-plastic steel. Using exact primitives `W_0' = \sigma_w` and `W_1'=e\sigma_w`,

\[
N_y^w=\rho_w\frac{W_0(e_y^+)-W_0(e_y^-)}{\kappa_y},
\]

\[
M_y^w=\rho_w\frac{W_1(e_y^+)-W_1(e_y^-)-\varepsilon_y^0[W_0(e_y^+)-W_0(e_y^-)]}{\kappa_y^2},
\]

with the analytic `\kappa_y\to0` limit. No thickness quadrature is used.

## Terminal output of this contract

\[
N_x=N_x^U+N_x^s,
\]

\[
M_x=M_x^U+M_x^s,
\]

\[
N_y=N_y^U+N_y^s+N_y^w,
\]

\[
M_y=M_y^U+M_y^s+M_y^w.
\]

Stop here. The next-stage virtual-work/current-tangent theory is intentionally not part of this contract.

## Exact source snapshot audit

The exact local source snapshot from which this canonical GitHub text was prepared is recorded in `20260905__NZSCCM__NM_SECTION_CONTRACT_ARTIFACT_MANIFEST_R01.md` with SHA-256 `75d2ad39ec96153aea5a91e50039f89f74316b04f9b9f969347f4ec1fa8850bd`.
