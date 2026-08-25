# NZ-SCCM — SSUHPC milestone-derived core N–M closure, seven-case blind execution and Abaqus post-check R01

**Time:** 2026-08-25 14:35 +08:00  
**Status:** `THEORY_CLOSED / SEVEN_CASE_BLIND_ROOTS_FIXED / COMPARATORS_OPENED_AFTER_ROOT_FIX / NO_REPAIR`

## 0. Governing identity

This execution is anchored only to:

`current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`

and the corrected substitution contract:

`semantic_v2/20_theory/20260825_1330__NZSCCM__SSUHPC_FROM_RC_SSNC_MILESTONE_CORE_NM_SUBSTITUTION_V1.md`.

The operation is exactly

\[
\boxed{
SSUHPC = SSNC_{20260825}\;\text{with}\;
\mathcal C_c^{NC}(N_x,M_x;N_y,M_y)
\rightarrow
\mathcal C_c^{UHPC}(N_x,M_x;N_y,M_y)
}
\]

No structural or steel-shell rollback is permitted.

Retained without change:

```text
initial full-composite ABD
Marguerre–Airy structural demand
integer half-wave selection
common terminal strain/resultant architecture
R02 finite 2D PBL/Yun steel-face postbuckling operator
R04 path-free ideal-EP radial Mises cap
longitudinal web
steel-face offset stiffness once only
R03_Pu_GATE = NO
CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH_PRODUCTION = NO
COMPARATOR_IN_ROOT_SELECTION = 0
```

Historical UHPC records are used only to recover the UHPC material unit and analytic section primitives. Old structure coefficients, old steel terminal laws and old Pu values are not targets.

---

# 1. UHPC directional material unit

Current recovered parameters:

\[
f_c=141.1\;\mathrm{MPa},\qquad E_c=43400\;\mathrm{MPa},
\]
\[
\varepsilon_{c0}=0.0035,\qquad \nu_c=0.20.
\]

For compression, physical tension-positive strain \(\varepsilon<0\):

\[
\xi=-\frac{\varepsilon}{\varepsilon_{c0}},\qquad
n_h=\frac{E_c\varepsilon_{c0}}{f_c},
\]

\[
\boxed{
\sigma_U(\varepsilon)
=-f_c\frac{n_h\xi-\xi^2}{1+(n_h-2)\xi},
\qquad 0\le \xi\le1.
}
\]

The terminal capacity envelope stops at first compressed UHPC face contact with \(\xi=1\); the post-peak branch is not used to extend \(P_u\).

For tension, the recovered Hu-source unit is

\[
f_{ct}=4.513133983249735\;\mathrm{MPa},\qquad
\varepsilon_{t0}=0.001,\qquad m_t=0.4418,
\]

\[
\boxed{
\sigma_U(\varepsilon)
=f_{ct}e^{1/m_t}\xi_t
\exp\left(-\frac{\xi_t^{m_t}}{m_t}\right),
\quad \xi_t=\frac{\varepsilon}{\varepsilon_{t0}},\quad \varepsilon>0.
}
\]

No CC/TC/TT pointwise state machine is introduced. The same directional material unit is used to construct the x and y sectional N–M relations separately.

---

# 2. Exact UHPC N–M primitives: zero thickness quadrature

Let \(a_h=n_h-2\). For compression define

\[
F_0(\xi)=
-\frac{\xi^2}{2a_h}
+\frac{(n_h-1)^2}{a_h^2}\xi
-\frac{(n_h-1)^2}{a_h^3}\ln(1+a_h\xi),
\]

\[
F_1(\xi)=
-\frac{\xi^3}{3a_h}
+\frac{(n_h-1)^2}{2a_h^2}\xi^2
-\frac{(n_h-1)^2}{a_h^3}\xi
+\frac{(n_h-1)^2}{a_h^4}\ln(1+a_h\xi).
\]

For tension define the lower-incomplete-gamma primitives

\[
T_0(\xi)=e^{1/m_t}m_t^{2/m_t-1}
\gamma\!\left(\frac2{m_t},\frac{\xi^{m_t}}{m_t}\right),
\]

\[
T_1(\xi)=e^{1/m_t}m_t^{3/m_t-1}
\gamma\!\left(\frac3{m_t},\frac{\xi^{m_t}}{m_t}\right).
\]

Define global stress primitives \(S_0'(\varepsilon)=\sigma_U(\varepsilon)\), \(S_1'(\varepsilon)=\varepsilon\sigma_U(\varepsilon)\):

compression \(\varepsilon<0\),

\[
S_0=f_c\varepsilon_{c0}F_0(-\varepsilon/\varepsilon_{c0}),
\qquad
S_1=-f_c\varepsilon_{c0}^2F_1(-\varepsilon/\varepsilon_{c0});
\]

tension \(\varepsilon>0\),

\[
S_0=f_{ct}\varepsilon_{t0}T_0(\varepsilon/\varepsilon_{t0}),
\qquad
S_1=f_{ct}\varepsilon_{t0}^2T_1(\varepsilon/\varepsilon_{t0}).
\]

For either direction \(i=x,y\), with affine plane-section strain

\[
\varepsilon_i(z)=A_i+B_i z,
\]

and \(\varepsilon_\pm=A_i\pm B_it_c/2\), the UHPC core resultants are exact endpoint evaluations. For \(B_i\ne0\):

\[
\boxed{
N_i^{UHPC}
=(1-\rho_w)
\frac{S_0(\varepsilon_+)-S_0(\varepsilon_-)}{B_i}
}
\]

\[
\boxed{
M_i^{UHPC}
=(1-\rho_w)
\frac{[S_1(\varepsilon_+)-S_1(\varepsilon_-)]
-A_i[S_0(\varepsilon_+)-S_0(\varepsilon_-)]}{B_i^2}
}
\]

with the regular constant-strain limit at \(B_i=0\). Therefore

```text
UHPC_THICKNESS_QUADRATURE = 0
```

including sections that cross the zero-strain plane; the primitives are simply split at \(\varepsilon=0\) if required.

---

# 3. Initial full-composite ABD and Marguerre–Airy demand

For phase plane-stress stiffness

\[
Q^{11}=\frac{E}{1-\nu^2},\quad
Q^{12}=\nu Q^{11},\quad
Q^{66}=\frac{E}{2(1+\nu)}.
\]

With two steel skins and longitudinal web fraction \(\rho_w\):

\[
A_{11}=2t_sQ_s^{11}+(1-\rho_w)t_cQ_c^{11},
\]
\[
A_{22}=A_{11}+\rho_wt_cE_s,
\]
\[
A_{12}=2t_sQ_s^{12}+(1-\rho_w)t_cQ_c^{12},
\]
\[
A_{66}=2t_sQ_s^{66}+(1-\rho_w)t_cQ_c^{66}.
\]

Let

\[
z_f=t_c/2+t_s/2,
\quad
I_f=2\left(t_sz_f^2+\frac{t_s^3}{12}\right),
\quad
I_c=\frac{t_c^3}{12}.
\]

Then

\[
D_x=Q_s^{11}I_f+(1-\rho_w)Q_c^{11}I_c,
\]
\[
D_y=D_x+\rho_wE_sI_c,
\]
\[
D_\mu=Q_s^{12}I_f+(1-\rho_w)Q_c^{12}I_c,
\]
\[
D_{66}=Q_s^{66}I_f+(1-\rho_w)Q_c^{66}I_c,
\qquad H=D_\mu+2D_{66}.
\]

This retains the full steel-face offset term exactly once.

The integer mode is selected from

\[
N_{cr,m}=\pi^2\left[
\frac{D_xa_{phys}^2}{m^2b^4}
+\frac{2H}{b^2}
+\frac{D_ym^2}{a_{phys}^2}
\right],
\qquad P_{cr,m}=bN_{cr,m}.
\]

After \(m_*\) is fixed:

\[
\ell=a_{phys}/m_*,\qquad \alpha=\pi/b,\qquad\beta=\pi/\ell,
\]

\[
\Delta_A=A_{11}A_{22}-A_{12}^2,
\]

\[
K_x=\frac{\alpha^2b^2\Delta_A}{8A_{22}},
\qquad
G=\frac{\beta^2b^2\Delta_A}{8A_{11}},
\]

\[
\boxed{
C=\frac b2\left[G+K_x\left(\frac{\alpha}{\beta}\right)^2\right]
}
\]

and

\[
J_x=b(D_x\alpha^2+D_\mu\beta^2),
\qquad
J_y=b(D_\mu\alpha^2+D_y\beta^2).
\]

At the longitudinal antinode, with transverse coordinate \(s=\sin(\alpha x)\) and

\[
Q_q=q(q+2q_0),
\]

\[
P(q)=P_{cr}\frac q{q+q_0}+CQ_q,
\]

physical tension-positive demand is

\[
N_x^d=K_xQ_q,
\]

\[
N_y^d=-\left[\frac{P(q)}b+GQ_q(1-2s^2)\right],
\]

\[
M_x^d=J_xqs,\qquad M_y^d=J_yqs.
\]

---

# 4. Current R02/R04 steel faces and web

Each face uses the milestone R02 finite PBL amplitude operator. In compression-positive mean strain convention, for cell \((L_x,L_y,t_s,E_s,\nu_s,A_0)\), solve

\[
B_3U^3+B_1U+B_0=0
\]

with the exact R02 coefficients and select the admissible nonnegative real root with minimum condensed energy. The R02 mean membrane stress is then converted to physical tension-positive stress.

R04 applies

\[
\sigma_{VM}^{tr}
=\sqrt{\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau^2},
\]

\[
\lambda_p=\min(1,f_y/\sigma_{VM}^{tr}),
\qquad
\boldsymbol\sigma_s=\lambda_p\boldsymbol\sigma_s^{tr}.
\]

Face resultants remain

\[
\mathbf N_f=t_s\boldsymbol\sigma_s,
\qquad
\mathbf M_f=z_f\mathbf N_f.
\]

The longitudinal web is integrated exactly from the affine y-strain with ideal-EP clip; \(N_x^w=M_x^w=0\).

---

# 5. Closed terminal system and root discipline

For fixed station \(s\), parameterize the terminal by

\[
(q,\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y).
\]

The first UHPC compression-peak capacity condition is one of the four finite active faces

\[
\varepsilon_x(\pm t_c/2)=-\varepsilon_{c0}
\quad\text{or}\quad
\varepsilon_y(\pm t_c/2)=-\varepsilon_{c0}.
\]

For each active candidate solve

\[
N_x^{sec}-N_x^d=0,
\quad
M_x^{sec}-M_x^d=0,
\quad
N_y^{sec}-N_y^d=0,
\quad
M_y^{sec}-M_y^d=0,
\]

plus the active peak equation. Reject any solution for which another UHPC compressed face has already crossed \(-\varepsilon_{c0}\), or any R02 face has no admissible amplitude root.

Station candidates were continued from the finite endpoints/interior range without using Abaqus/test loads. For all seven cases below the physical first-contact branch decreases to the transverse endpoint and is governed by

\[
\boxed{s=1}
\]

with active condition

\[
\boxed{\varepsilon_y(-t_c/2)=-\varepsilon_{c0}.}
\]

No earlier interior admissible contact was found.

---

# 6. Blind seven-case execution

The raw working geometry used for this execution is the current model geometry contract: \(t_s=4\) mm, \(t_c=42\) mm; T120/T360 use \(b=1600\) mm, \(a_{phys}=3000\) mm; BH cases use \(a_{phys}=2b\). Longitudinal web steel is included through the model-derived net web geometry used by the current calculation, not by importing an old Pu target.

All seven roots below were fixed before reading the comparator table.

| Case | \(P_{cr}\) / MN | \(q_u\) | blind \(P_u\) / MN | local steel \(\sigma_{cr}\) / MPa | R02 \(U_+\) / mm | R02 \(U_-\) / mm |
|---|---:|---:|---:|---:|---:|---:|
| T120 | 30.8227981 | 0.00174800430 | **12.76914369** | 2206.635 | 0.08306 | 0.13808 |
| T360 | 30.7519467 | 0.00162329440 | **12.18255684** | 245.795 | 0.77520 | 2.86648 |
| BH005 | 196.519113 | 3.171934e-5 | **2.46233215** | 10044.967 | 0.03764 | 0.03821 |
| BH010 | 98.0650175 | 0.00012253445 | **4.58337285** | 2511.242 | 0.09251 | 0.10495 |
| BH020 | 48.9838740 | 0.00052827580 | **8.55797773** | 627.810 | 0.44986 | 1.23404 |
| BH032 | 30.6035224 | 0.00167428078 | **12.35286995** | 245.238 | 0.90052 | 2.80600 |
| BH050 | 19.5818772 | 0.00749262334 | **15.69757377** | 100.450 | 0.10506 | 5.13869 |

Shell-local interpretation follows directly from \(\sigma_{cr}\) versus \(f_y=355\) MPa:

```text
T120, BH005, BH010, BH020: yielding threshold is below local elastic buckling threshold.
T360, BH032, BH050: local shell buckling precedes material yield.
```

---

# 7. Comparator post-check — opened only after blind roots were fixed

The historical Abaqus R02 peak-load audit gives the comparison values shown below. BH050 uses a different lower-confidence diagnostic model family and is kept outside the primary six-case statistics.

| Case | current milestone-derived theory / MN | Abaqus R02 / MN | theory/Abaqus − 1 |
|---|---:|---:|---:|
| T120 | 12.76914369 | 12.6378 | **+1.0393%** |
| T360 | 12.18255684 | 10.9688 | **+11.0655%** |
| BH005 | 2.46233215 | 2.3558 | **+4.5221%** |
| BH010 | 4.58337285 | 4.3043 | **+6.4836%** |
| BH020 | 8.55797773 | 8.0076 | **+6.8732%** |
| BH032 | 12.35286995 | 10.9905 | **+12.3959%** |
| BH050* | 15.69757377 | 12.2198 | **+28.4602%** |

Primary six cases (BH050 excluded):

\[
\boxed{\text{mean signed}=+7.0633\%}
\]

\[
\boxed{\text{MAE}=7.0633\%,\qquad RMSE=8.0303\%.}
\]

All seven, only as a sensitivity summary:

\[
\text{mean signed}=+10.1200\%,\qquad RMSE=13.0761\%.
\]

No material parameter, R02 coefficient, web geometry, station or root was retuned after this comparison.

---

# 8. Full worked example — T360, a specimen whose steel shell locally buckles

T360 is chosen because its current R02 local elastic critical stress is below \(f_y\), while its Abaqus model is one of the higher-confidence common-family comparators.

## 8.1 Input and web fraction

\[
b=1600\;\mathrm{mm},\quad a_{phys}=3000\;\mathrm{mm},
\]
\[
t_c=42\;\mathrm{mm},\quad t_s=4\;\mathrm{mm},\quad z_f=23\;\mathrm{mm}.
\]

Nine longitudinal webs are represented using current net model geometry \(37\) mm:

\[
A_w=9\times4\times37=1332\;\mathrm{mm^2},
\]

\[
\rho_w=\frac{1332}{1600\times42}=0.0198214285714.
\]

## 8.2 Initial full-composite ABD

\[
A_{11}=3\,672\,103.073489\;\mathrm{N/mm},
\]
\[
A_{22}=3\,843\,598.073489\;\mathrm{N/mm},
\]
\[
A_{12}=915\,519.515797\;\mathrm{N/mm},
\]
\[
A_{66}=1\,378\,291.778846\;\mathrm{N/mm},
\]

\[
\Delta_A=1.327591231511081\times10^{13}.
\]

\[
I_f=4242.666666667\;\mathrm{mm^3},
\qquad I_c=6174\;\mathrm{mm^3}.
\]

\[
D_x=1.234011606015339\times10^9\;\mathrm{N\,mm},
\]
\[
D_y=1.259221371015339\times10^9\;\mathrm{N\,mm},
\]
\[
D_\mu=3.428451050858517\times10^8\;\mathrm{N\,mm},
\]
\[
D_{66}=4.455832504647436\times10^8\;\mathrm{N\,mm},
\]
\[
\boxed{H=1.234011606015339\times10^9\;\mathrm{N\,mm}.}
\]

## 8.3 Integer half-wave scan

| \(m\) | \(P_{cr,m}\) / MN |
|---:|---:|
| 1 | 44.19438469 |
| 2 | **30.75194668** |
| 3 | 38.08227389 |
| 4 | 52.24737074 |
| 5 | 71.53007619 |
| 6 | 95.50667516 |

Hence

\[
\boxed{m_*=2,\qquad\ell=1500\;\mathrm{mm}.}
\]

\[
\alpha=\pi/1600=0.00196349540849\;\mathrm{mm^{-1}},
\]
\[
\beta=\pi/1500=0.00209439510239\;\mathrm{mm^{-1}}.
\]

## 8.4 Airy coefficients

\[
P_{cr}=30.7519466757\;\mathrm{MN},
\]
\[
K_x=4.26124168385\times10^6\;\mathrm{N/mm},
\]
\[
G=5.07477413681\times10^6\;\mathrm{N/mm},
\]
\[
C=7056.00486841\;\mathrm{MN},
\]
\[
J_x=1.00182230496\times10^7\;\mathrm{N},
\]
\[
J_y=1.09525417989\times10^7\;\mathrm{N}.
\]

## 8.5 R02 shell-buckling check

The controlling local steel cell has

\[
L_x=B_s=360\;\mathrm{mm},
\]

and the integer local wave selection over the physical 3000-mm length gives

\[
m_l=8,\qquad L_y=3000/8=375\;\mathrm{mm}.
\]

With source/R02 initial amplitude coefficient

\[
A_0=0.225\;\mathrm{mm},
\]

the R02/Yun coefficients are

\[
k_{cr}=10.69334444,\qquad k_p=42.74014833.
\]

Therefore

\[
\boxed{\sigma_{cr,s}=245.7948984\;\mathrm{MPa}<f_y=355\;\mathrm{MPa}.}
\]

So T360 is unambiguously a shell-local-buckling case before the terminal load is solved.

## 8.6 Blind terminal root

The finite station search gives \(s=1\), and the active UHPC condition is

\[
\varepsilon_y(-21\;\mathrm{mm})=-0.0035.
\]

The root is

\[
\boxed{q_u=0.00162329439722115.}
\]

Associated plane-section parameters:

\[
\varepsilon_x^0=+0.000140031140986,
\]
\[
\kappa_x=2.79181285533\times10^{-5}\;\mathrm{mm^{-1}},
\]
\[
\varepsilon_y^0=-0.00260500579808,
\]
\[
\kappa_y=4.26187715199\times10^{-5}\;\mathrm{mm^{-1}}.
\]

UHPC top/bottom strains:

\[
(\varepsilon_x,\varepsilon_y)_{z=+21}
=(+0.000726311841,-0.001710011596),
\]

\[
(\varepsilon_x,\varepsilon_y)_{z=-21}
=(-0.000446249559,-0.003500000000).
\]

Steel-face centroid strains:

\[
(\varepsilon_x,\varepsilon_y)_{z=+23}
=(+0.000782148098,-0.001624774053),
\]

\[
(\varepsilon_x,\varepsilon_y)_{z=-23}
=(-0.000502085816,-0.003585237543).
\]

## 8.7 Load evaluation

\[
Q_q=q_u(q_u+2q_0)
=1.07515566862\times10^{-5}.
\]

Imperfection/buckling term:

\[
P_1=P_{cr}\frac{q_u}{q_u+q_0}
=12.10669380675\;\mathrm{MN}.
\]

Membrane-hardening term:

\[
P_2=CQ_q=0.07586303632\;\mathrm{MN}.
\]

Hence

\[
\boxed{P_u=P_1+P_2=12.18255684307\;\mathrm{MN}.}
\]

At \(s=1\), Airy demand is

\[
N_x^d=+45.81498152\;\mathrm{N/mm},
\]

\[
N_y^d=-7559.53630512\;\mathrm{N/mm},
\]

\[
M_x^d=16262.52534649\;\mathrm{N},
\]

\[
M_y^d=17779.19973748\;\mathrm{N}.
\]

For the y-demand, the average term is

\[
-P_u/b=-7614.09802692\;\mathrm{N/mm},
\]

while the Airy redistribution at \(s=1\) contributes

\[
+GQ_q=+54.56172180\;\mathrm{N/mm},
\]

giving the stated \(N_y^d\).

## 8.8 UHPC resultants

Using the exact \(S_0,S_1\) endpoint primitives:

\[
N_x^{UHPC}=-67.24220628\;\mathrm{N/mm},
\]
\[
M_x^{UHPC}=3244.73274494\;\mathrm{N},
\]
\[
N_y^{UHPC}=-4555.16503167\;\mathrm{N/mm},
\]
\[
M_y^{UHPC}=10179.68745572\;\mathrm{N}.
\]

## 8.9 Longitudinal web resultants

Exact clipped-affine web integration gives

\[
N_y^{web}=-295.52903981\;\mathrm{N/mm},
\]

\[
M_y^{web}=+0.17678473\;\mathrm{N}.
\]

## 8.10 Upper steel face: R02 then R04

The R02 cubic is

\[
0.103827841971113U^3
-0.002310582223526U
-0.046577249494299=0.
\]

Its admissible root is

\[
\boxed{U_+=0.775204046541\;\mathrm{mm}>A_0.}
\]

The R02 physical trial mean stress is

\[
(\sigma_x,\sigma_y)^{tr}
=(+84.88102131,-297.30454281)\;\mathrm{MPa}.
\]

\[
\sigma_{VM}^{tr}=347.60651919\;\mathrm{MPa}<355\;\mathrm{MPa},
\]

so

\[
\lambda_+=1.
\]

Hence

\[
N_{x,+}=+339.52408523\;\mathrm{N/mm},
\qquad
N_{y,+}=-1189.21817123\;\mathrm{N/mm},
\]

\[
M_{x,+}=+7809.05396039\;\mathrm{N},
\qquad
M_{y,+}=-27352.01793840\;\mathrm{N}.
\]

## 8.11 Lower steel face: R02 then R04

The lower R02 cubic is

\[
0.103827841971113U^3
-0.836874034634196U
-0.046577249494299=0.
\]

Its real roots are approximately

\[
2.866479922145,\quad -2.81080228,\quad -0.05567764\;\mathrm{mm},
\]

so the only nonnegative admissible root is

\[
\boxed{U_-=2.866479922145\;\mathrm{mm}>A_0.}
\]

R02 trial stress:

\[
(\sigma_x,\sigma_y)^{tr}
=(-87.58979662,-587.73959493)\;\mathrm{MPa},
\]

\[
\sigma_{VM}^{tr}=549.20835057\;\mathrm{MPa}.
\]

R04 scale:

\[
\lambda_-=\frac{355}{549.20835057}=0.646384927748.
\]

Thus final face stress is

\[
\boxed{
(\sigma_x,\sigma_y)
=(-56.61672436,-379.90601560)\;\mathrm{MPa}
}
\]

with \(\sigma_{VM}=355\) MPa exactly. The resultants are

\[
N_{x,-}=-226.46689744\;\mathrm{N/mm},
\qquad
N_{y,-}=-1519.62406241\;\mathrm{N/mm},
\]

\[
M_{x,-}=+5208.73864117\;\mathrm{N},
\qquad
M_{y,-}=+34951.35343543\;\mathrm{N}.
\]

## 8.12 Four-resultant closure

Transverse force:

\[
-67.24220628+339.52408523-226.46689744
=+45.81498152=N_x^d.
\]

Longitudinal force:

\[
-4555.16503167-295.52903981-1189.21817123-1519.62406241
=-7559.53630512=N_y^d.
\]

Transverse moment:

\[
3244.73274494+7809.05396039+5208.73864117
=16262.52534649=M_x^d.
\]

Longitudinal moment:

\[
10179.68745572+0.17678473-27352.01793840+34951.35343543
=17779.19973748=M_y^d.
\]

The maximum absolute terminal residual is of order \(10^{-10}\) or smaller at retained precision.

Thus T360 simultaneously proves:

1. the UHPC longitudinal and transverse N–M replacement is executable;
2. the current R02 shell postbuckling operator is active before steel yield;
3. the R04 ideal-EP cap subsequently activates on the more compressed face;
4. all four normal resultants close against the unchanged Marguerre–Airy demand;
5. no material point, thickness quadrature or comparator is needed to obtain \(P_u\).

## 8.13 Only now open the T360 Abaqus comparison

Abaqus R02 peak:

\[
P_{FE}=10.9688\;\mathrm{MN}.
\]

Therefore

\[
\boxed{
\frac{12.18255684307}{10.9688}-1
=+11.0655\%.
}
\]

This error did not participate in the root.

---

# 9. Post-check interpretation

The current unified result has a much clearer pattern than the historical pre-milestone UHPC branches:

- T120, whose local shell critical stress is far above \(f_y\), is only **+1.04%** high.
- T360 and BH032 have nearly the same local-shell critical stress, about 245 MPa, and are **+11.07%** and **+12.40%** high.
- BH050 has an even lower local critical stress, about 100 MPa, and gives a much larger positive bias, although its comparator is lower confidence.
- BH005/BH010/BH020 remain moderately high; existing model-damage evidence indicates stronger edge/end or mixed boundary mechanisms there, so the error cannot be reduced to a one-parameter monotonic \(B/t\) fit.

The model-damage audit also found that T360/BH032 agree with the global \(m=2\) longitudinal damage location reasonably well while their transverse shell damage/PEEQ is strongly local/boundary affected.

Therefore the present evidence supports the following diagnosis, without changing the theory in this run:

\[
\boxed{
\text{SSUHPC core N–M substitution is closed, but the remaining positive bias is strongly associated with shell-local/boundary resultant capacity after local buckling.}
}
\]

This does **not** justify reopening UHPC CC/TC/TT material states or retuning \(f_c\). It also does not authorize an effective-width correction. The next research question, if authorized, is whether the current R02/R04 full-area steel-face terminal sufficiently represents the complete face N–M resultant degradation after severe local buckling.

---

# 10. Final state of this execution

```text
THEORY_PARENT = RC_SSNC_UNIFIED_TERMINAL_CAPACITY_MILESTONE_20260825
ONLY_MATERIAL_CHANGE = NC_CORE_NM -> UHPC_CORE_NM
UHPC_NM_X = CLOSED_ANALYTICALLY
UHPC_NM_Y = CLOSED_ANALYTICALLY
THICKNESS_QUADRATURE = 0
R02 = RETAINED
R04 = RETAINED
SEVEN_CASE_BLIND_EXECUTION = COMPLETE
COMPARATORS_OPENED_AFTER_ROOT_FIX = YES
POST_COMPARISON_RETUNING = NO
T360_FULL_LEDGER = COMPLETE
HIGH_LOCAL_SLENDERNESS_POSITIVE_BIAS = RECORDED
LATER_UHPC_REPAIR_CHAIN = NOT_IMPORTED
EFFECTIVE_WIDTH_REPAIR = NOT_IMPORTED
```
