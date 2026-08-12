# NZ-SCCM Case21 — NC-R1 Formal Closure Fresh Calculation
## R10 → N48-C1/MM → Cayley–Hamilton → Nguyen complete halfwave → D15 exact moments → Rebar → P,Rq,L → first +→− maximum

**Date:** 2026-08-12  
**Identity:** FRESH CURRENT-THEORY CALCULATION / BLIND UNTIL THEORY RESULT FREEZE  
**Governing theory:** `current/theory/NZ_SCCM_NC_R1_FORMAL_CLOSURE_ZHOU_STYLE_CANONICAL_20260812.md`

---

# 0. Isolation discipline

This calculation was rebuilt from the current theory and the Case21 raw-input blind contract. No prior Case21 theoretical root, D, q, P, Pu, path, FE result, Gauss result, Simpson result, material-point history or previous NZ-SCCM numerical result was used as an input, target, initial answer or root selector.

The experimental load was not read until the fresh theoretical value below had been frozen. It is used only in the final comparison section.

```text
HISTORICAL_CASE21_D_Q_P_ROOT_PATH_USED = NO
HISTORICAL_CASE21_THEORY_RESULT_USED = NO
HISTORICAL_FE_GAUSS_SIMPSON_RESULT_USED = NO
EXPERIMENT_USED_DURING_SOLVE = NO
EXPERIMENT_USED_FOR_ROOT_SELECTION = NO
EXPERIMENT_USED_FOR_PARAMETER_TUNING = NO
EXPERIMENT_READ_ONLY_AFTER_THEORY_FREEZE = YES
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

Material Chebyshev coordinates used to generate N48 coefficients are one-dimensional **material coordinates**, not structural-space sampling points.

---

# 1. Case21 raw input

The blind input contract gives

\[
\boxed{b=\ell=1220\ \mathrm{mm},\qquad t_p=19.30\ \mathrm{mm}}
\tag{C1}
\]

where \(b\) is the complete representative halfwave width, \(\ell\) is its axial length, and \(t_p\) is panel thickness.

Concrete inputs are

\[
\boxed{f_c=21.23\ \mathrm{MPa},\quad E_0=20321\ \mathrm{MPa},\quad \varepsilon_0=0.00209,\quad \nu=0.18}
\tag{C2}
\]

where \(f_c\) is the current NC compressive-strength input, \(E_0\) is initial elastic modulus, \(\varepsilon_0\) is the R10 reference compressive strain, and \(\nu\) is Poisson's ratio.

Initial imperfection is

\[
\boxed{q_0=\frac{A_0}{b}=\frac1{400}=0.0025}
\tag{C3}
\]

where \(q_0\) is the stress-free initial imperfection ratio.

The total two-way nominal reinforcement ratio is 0.75%, split equally into the two directions:

\[
\boxed{\rho_{s,x}=\rho_{s,y}=0.00375}
\tag{C4}
\]

and the single steel layer lies at the middle surface:

\[
\boxed{z_s=0,\qquad \zeta_s=0}
\tag{C5}
\]

Steel material inputs are

\[
\boxed{E_s=200000\ \mathrm{MPa},\qquad \varepsilon_y=0.00265,\qquad f_y=530\ \mathrm{MPa}}
\tag{C6}
\]

R10 project-frozen constants are

\[
\boxed{\rho=0.1,\quad m_t=-\frac7{90},\quad \eta_r=0.05,\quad u_r=0.03}
\tag{C7}
\]

\[
\boxed{a_{cc}=0.1072329249362415,\qquad a_t=1-2^{-1/8}=0.08299595679532878}
\tag{C8}
\]

The compiler interval is fixed before the root calculation:

\[
\boxed{\lambda\in[\lambda_a,\lambda_b]=[-1.15,0.12]}
\tag{C9}
\]

No experimental load is involved in any quantity in (C1)–(C9).

---

# 2. R10 derived material quantities

The dimensionless initial slope is

\[
\kappa=\frac{E_0\varepsilon_0}{f_c}
=\frac{20321\times0.00209}{21.23}
=\boxed{2.0005129533678754}.
\tag{C10}
\]

The characteristic tensile coordinate is

\[
x_{cr}=\frac{\rho}{\kappa}
=\frac{0.1}{2.0005129533678754}
=\boxed{0.04998717945397425}.
\tag{C11}
\]

The smooth one-sided scale is

\[
\eta=\frac{x_{cr}}{20}
=\boxed{0.0024993589726987125}.
\tag{C12}
\]

The Foster source function is

\[
T_{src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10),
\tag{C13}
\]

with

\[
H(r,r_0)=\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}\right]
-\frac12\left[-r_0+\sqrt{r_0^2+\eta_r^2}\right].
\tag{C14}
\]

The one-dimensional material-work integral was evaluated from the closed antiderivative of (C14), not from structural-space quadrature:

\[
\boxed{\int_0^{10}T_{src}(r)\,dr=6.34987521359851}.
\tag{C15}
\]

Therefore

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr
\tag{C16}
\]

\[
=0.1\times0.04998717945397425\times6.34987521359851
=\boxed{0.03174123518124918}.
\tag{C17}
\]

The R10 C2 tensile peak parameter follows from material-work closure:

\[
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right)
\tag{C18}
\]

\[
=\frac15\left(\frac{0.03174123518124918}{0.04998717945397425}-0.01-4.5\times0.03\right)
=\boxed{0.09799750427197022}.
\tag{C19}
\]

Thus the complete closed R10 functions \(C(\lambda),T(\lambda),T^{(7)}(\lambda),U(\lambda)\) are numerically fixed before any structural root is sought.

---

# 3. N48 material compiler

For \([\lambda_a,\lambda_b]=[-1.15,0.12]\),

\[
\lambda_c=\frac{-1.15+0.12}{2}=\boxed{-0.515},
\qquad
\lambda_h=\frac{0.12-(-1.15)}2=\boxed{0.635}.
\tag{C20}
\]

At \(\lambda=0\),

\[
\xi_0=-\frac{\lambda_c}{\lambda_h}
=\frac{0.515}{0.635}
=\boxed{0.8110236220472439}.
\tag{C21}
\]

The 49 material coordinates are

\[
\theta_j=\frac{(j+1/2)\pi}{49},\qquad
\lambda_j=-0.515+0.635\cos\theta_j,\qquad j=0,\ldots,48.
\tag{C22}
\]

For each \(F\in\{U,C,T,T^{(7)}\}\), the direct coefficient is freshly generated from the R10 target:

\[
a_n^{(F,0)}=\frac{2-\delta_{n0}}{49}\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j).
\tag{C23}
\]

The C1 coefficient correction for \(U,C,T^{(7)}\) is

\[
\mathbf a^{(F,C1)}=\mathbf a^{(F,0)}+
\mathbf H^{-1}\mathbf G^T(\mathbf G\mathbf H^{-1}\mathbf G^T)^{-1}
(\mathbf d_F-\mathbf G\mathbf a^{(F,0)}).
\tag{C24}
\]

For T, the strict-C1 constrained minimax problem is solved only in the one-dimensional material coordinate. The fresh primary minimax error is

\[
\boxed{E_T^*=0.08957188456536706},
\tag{C25}
\]

and the independent dense material-coordinate verification gives

\[
\boxed{E_{T,\mathrm{verify}}=0.08957188475607275}.
\tag{C26}
\]

The final zero anchors are

\[
\boxed{T_{48}(0)=-4.2959858081\times10^{-17}},
\tag{C27}
\]

\[
\boxed{T'_{48}(0)=3.0484718702\times10^{-15}}.
\tag{C28}
\]

The other final C1 anchors are

\[
\boxed{U_{48}(0)=-2.2862\times10^{-17},\qquad U'_{48}(0)=2.000512953367875},
\tag{C29}
\]

\[
\boxed{C_{48}(0)=-1.4662\times10^{-16},\qquad C'_{48}(0)=3.2978\times10^{-16}},
\tag{C30}
\]

\[
\boxed{T^{(7)}_{48}(0)=6.8889\times10^{-17},\qquad [T^{(7)}_{48}]'(0)=2.5397\times10^{-16}}.
\tag{C31}
\]

Final coefficient magnitudes remain O(1):

| primitive | max \(|a_n|\) | \(\sum|a_n|\) |
|---|---:|---:|
| U | 0.5941718240 | 1.5008785565 |
| C | 0.6116708790 | 1.4965249932 |
| T | 0.3327530256 | 1.8962407584 |
| T7 | 0.2572545708 | 1.6884004275 |

The complete freshly generated 49×4 coefficient table is stored separately at:

`current/case21/NZ_SCCM_CASE21_NC_R1_FRESH_N48_COEFFICIENTS_20260812.csv`

No coefficient was read from any previous Case21 computation.

---

# 4. Cayley–Hamilton two-dimensional lift

The standardized tensor is

\[
\mathbf Y=\frac{\mathbf X-\lambda_c\mathbf I}{\lambda_h},
\qquad K_1=\operatorname{tr}\mathbf Y,
\qquad K_2=\det\mathbf Y.
\tag{C32}
\]

For each material coefficient,

\[
\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y,
\tag{C33}
\]

with

\[
A_0=1,\ B_0=0,\quad A_1=0,\ B_1=1,
\tag{C34}
\]

\[
A_{n+1}=-2K_2B_n-A_{n-1},
\qquad
B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
\tag{C35}
\]

Hence the n-th material coefficient enters the two-dimensional primitive as

\[
\boxed{\mathbf F_{48}^{(n)}=a_n^{(F,*)}(A_n\mathbf I+B_n\mathbf Y)}.
\tag{C36}
\]

All products in \(\mathbf{CC},\mathbf{TC},\mathbf{TT}\) are finite coefficient convolutions. No physical-space sample is used.

---

# 5. Case21 Nguyen complete-halfwave kinematics at the final root

The fresh joint root obtained below is

\[
\boxed{D_u=0.8903314709224796},
\qquad
\boxed{q_u=0.0018331919936158214}.
\tag{C37}
\]

The physical added-deflection amplitude is therefore

\[
A_u=bq_u=1220\times0.0018331919936158214
=\boxed{2.236494232211302\ \mathrm{mm}}.
\tag{C38}
\]

For the square Case21 halfwave,

\[
C_m=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\tag{C39}
\]

so at (C37)

\[
\boxed{C_m=0.02957706248175596}.
\tag{C40}
\]

The bending coefficient is

\[
C_b=\frac{\pi^2}{2\varepsilon_0}\frac{t_p}{b}q,
\tag{C41}
\]

hence

\[
\boxed{C_b=0.06847450378988293}.
\tag{C42}
\]

The continuous normalized strain field at the root is therefore

\[
e_x=0.18(0.8903314709224796)
+0.02957706248175596\cos^2X\sin^2Y
+0.06847450378988293\sin X\sin Y\,\zeta,
\tag{C43}
\]

\[
e_y=-0.8903314709224796
+0.02957706248175596\sin^2X\cos^2Y
+0.06847450378988293\sin X\sin Y\,\zeta,
\tag{C44}
\]

\[
g_{xy}=2(0.02957706248175596)\sin X\cos X\sin Y\cos Y
-2(0.06847450378988293)\cos X\cos Y\,\zeta.
\tag{C45}
\]

Equations (C43)–(C45) are continuous fields, not material-point arrays.

---

# 6. Continuous compiler-domain certificate

The current material compiler requires both eigenvalues of \(\mathbf X\) to remain in

\[
[-1.15,0.12]
\]

over the whole complete halfwave.

For a symmetric 2×2 matrix this is certified by

\[
0.12\mathbf I-\mathbf X\succeq0,
\qquad
\mathbf X+1.15\mathbf I\succeq0.
\tag{C46}
\]

At (C37), each required principal minor is a finite polynomial in

\[
u=\sin X\in[0,1],\qquad v=\sin Y\in[0,1],\qquad w=(\zeta+1)/2\in[0,1],
\]

because the squared shear term contains only \(\cos^2X=1-u^2\) and \(\cos^2Y=1-v^2\). A Bernstein-coefficient enclosure of these exact finite polynomials gives the following global lower bounds:

\[
\boxed{0.12-X_{11}\ge0.03649450757331346>0},
\tag{C47}
\]

\[
\boxed{\det(0.12\mathbf I-\mathbf X)\ge0.03382405769135842>0},
\tag{C48}
\]

\[
\boxed{X_{11}+1.15\ge1.0664945075733134>0},
\tag{C49}
\]

\[
\boxed{\det(\mathbf X+1.15\mathbf I)\ge0.18787691102555057>0}.
\tag{C50}
\]

Therefore, continuously over the entire halfwave,

\[
\boxed{-1.15<\lambda_-(X,Y,\zeta)\le\lambda_+(X,Y,\zeta)<0.12}.
\tag{C51}
\]

This is a coefficient enclosure, not physical-space sampling.

---

# 7. D15 exact moment contraction

The coordinate Jacobian is

\[
J_\Omega=\frac{b\ell t_p}{2\pi^2}
=\frac{1220\times1220\times19.30}{2\pi^2}
=\boxed{1455282.239925916\ \mathrm{mm}^3}.
\tag{C52}
\]

Any final scalar integrand is expanded in the finite D15 trigonometric-thickness basis and integrated through exact moments. For the Case21 scalar integrands, paired cosine factors permit stable coefficient contraction in the equivalent Chebyshev-in-sine representation; this remains a degeneration of the governing general D15 trigonometric exact-moment basis, not a physical-space collocation.

At the final root the exact D15 contractions are

\[
\boxed{\mathscr D[S_{yy}]=-13.433264103910405},
\tag{C53}
\]

\[
\boxed{\mathscr D[Q_q]=5.195117174559211}.
\tag{C54}
\]

The concrete axial-load prefactor is

\[
\frac{f_cbt_p}{2\pi^2}
=\frac{21.23\times1220\times19.30}{2\pi^2}
=\boxed{25324.296683300985\ \mathrm N}.
\tag{C55}
\]

Therefore

\[
P_c=-\frac{f_cbt_p}{2\pi^2}\mathscr D[S_{yy}]
\tag{C56}
\]

\[
=-25324.296683300985\times(-13.433264103910405)
=\boxed{340187.9655925644\ \mathrm N}
=\boxed{340.187965593\ \mathrm{kN}}.
\tag{C57}
\]

The concrete generalized-residual prefactor is

\[
f_c\varepsilon_0J_\Omega
=21.23\times0.00209\times1455282.239925916
=\boxed{64571.891683080845\ \mathrm{N\,mm}}.
\tag{C58}
\]

Thus

\[
R_{q,c}=f_c\varepsilon_0J_\Omega\mathscr D[Q_q]
\tag{C59}
\]

\[
=64571.891683080845\times5.195117174559211
=\boxed{335458.5434765504\ \mathrm{N\,mm}}.
\tag{C60}
\]

No Gauss, Simpson or adaptive structural quadrature appears in (C52)–(C60).

---

# 8. Rebar branch and exact closed contribution

Because the single reinforcement layer is at \(z_s=0\), the bending terms vanish from the steel strain. The x-direction steel strain lies in

\[
\varepsilon_{s,x}\in
\left[\varepsilon_0\nu D,\ \varepsilon_0(\nu D+C_m)\right],
\tag{C61}
\]

which at the final root gives

\[
\boxed{\varepsilon_{s,x}\in[0.0003349426993610,\ 0.0003967587599479]}.
\tag{C62}
\]

The y-direction steel strain lies in

\[
\varepsilon_{s,y}\in
\left[-\varepsilon_0D,\ \varepsilon_0(-D+C_m)\right],
\tag{C63}
\]

hence

\[
\boxed{\varepsilon_{s,y}\in[-0.001860792774228,\ -0.001798976713641]}.
\tag{C64}
\]

Therefore

\[
\boxed{\max|\varepsilon_s|=0.001860792774228},
\tag{C65}
\]

and

\[
\boxed{\frac{\max|\varepsilon_s|}{\varepsilon_y}
=\frac{0.001860792774228}{0.00265}
=0.7021859525<1}.
\tag{C66}
\]

The entire reinforcement field stays on the supported elastic branch. No spatial branch partition is needed.

For Case21 the exact elastic steel axial load is

\[
P_s=\rho_sbt_pE_s\varepsilon_0\left(D-\frac{C_m}{4}\right).
\tag{C67}
\]

The constant multiplier is

\[
\rho_sbt_pE_s\varepsilon_0
=0.00375\times1220\times19.30\times200000\times0.00209
=\boxed{36908.355\ \mathrm N}.
\tag{C68}
\]

The state factor is

\[
D-\frac{C_m}{4}
=0.8903314709224796-\frac{0.02957706248175596}{4}
=\boxed{0.8829372053020406}.
\tag{C69}
\]

Thus

\[
\boxed{P_s=36908.355\times0.8829372053020406
=32587.7598159956\ \mathrm N
=32.587759816\ \mathrm{kN}}.
\tag{C70}
\]

The steel generalized residual is

\[
R_{q,s}=\rho_st_pE_s\pi^2(q_0+q)b\ell
\left[
\frac{\varepsilon_0D(\nu-1)}4
+\frac{9\pi^2}{32}\left(q_0q+\frac12q^2\right)
\right].
\tag{C71}
\]

The first multiplier is

\[
\rho_st_pE_s\pi^2(q_0+q)b\ell
=\boxed{921395127.235028\ \mathrm{N\,mm}},
\tag{C72}
\]

while the bracket is

\[
\boxed{-0.0003640767516766792}.
\tag{C73}
\]

Hence

\[
\boxed{R_{q,s}=-335458.5449344496\ \mathrm{N\,mm}}.
\tag{C74}
\]

---

# 9. Total equilibrium at the fresh root

The total load is

\[
P=P_c+P_s
\tag{C75}
\]

\[
=340187.9655925644+32587.7598159956
=\boxed{372775.7254085579\ \mathrm N}
=\boxed{372.775725409\ \mathrm{kN}}.
\tag{C76}
\]

The total generalized residual is

\[
R_q=R_{q,c}+R_{q,s}
\tag{C77}
\]

\[
=335458.5434765504-335458.5449344496
=\boxed{-1.4578992268\times10^{-3}\ \mathrm{N\,mm}}.
\tag{C78}
\]

Same-expression forward differentiation of the finite analytic coefficient system gives

\[
\boxed{P_D=82992.6673496317\ \mathrm N},
\tag{C79}
\]

\[
\boxed{P_q=-78145412.78725956\ \mathrm N},
\tag{C80}
\]

\[
\boxed{R_{q,D}=-1.034816204716338\times10^6\ \mathrm{N\,mm}},
\tag{C81}
\]

\[
\boxed{R_{q,q}=9.743606518202156\times10^8\ \mathrm{N\,mm}}.
\tag{C82}
\]

The two large terms of the limit function are

\[
P_DR_{q,q}=\boxed{8.086478945508547\times10^{13}},
\tag{C83}
\]

\[
P_qR_{q,D}=\boxed{8.086613947650353\times10^{13}}.
\tag{C84}
\]

Therefore

\[
L=P_DR_{q,q}-P_qR_{q,D}
=\boxed{-1.350021418078125\times10^9}.
\tag{C85}
\]

The normalized equilibrium residual is

\[
R_{norm}=
\frac{|R_q|}{\max(f_c\varepsilon_0J_\Omega,|R_{q,c}|+|R_{q,s}|)}
=\boxed{2.1729946248051996\times10^{-9}},
\tag{C86}
\]

which satisfies

\[
R_{norm}<10^{-5}.
\tag{C87}
\]

The normalized limit residual is

\[
L_{norm}=
\frac{L}{|P_DR_{q,q}|+|P_qR_{q,D}|}
=\boxed{-8.347329895379345\times10^{-6}},
\tag{C88}
\]

which satisfies

\[
|L_{norm}|<10^{-5}.
\tag{C89}
\]

Thus the fresh candidate simultaneously passes both production residual gates.

---

# 10. Primary-branch +→− maximum classification

The NC-R1 production identity requires the first +→− local maximum on the connected admissible branch from \((0,0)\), not the largest mathematical root.

The branch was generated freshly from the same \(R_q(D,q)=0\) expression. No previous Case21 path was supplied. A representative lower-load connected-branch state is

\[
D=0.500000,\qquad q\approx0.0013204714709,
\tag{C90}
\]

for which

\[
P\approx327.423786\ \mathrm{kN},\qquad R_{norm}\approx2.70\times10^{-10},
\tag{C91}
\]

and the branch load derivative has positive sign:

\[
\frac{dP}{dD}\bigg|_{R_q=0}>0.
\tag{C92}
\]

Near the first stationary point, the two independently equilibrated bracketing states are:

\[
D_-=0.8900000000,\qquad q_-=0.001832850289484784,
\tag{C93}
\]

\[
P_-=372.774891445848\ \mathrm{kN},\qquad
R_{norm,-}=1.87696\times10^{-10},
\tag{C94}
\]

\[
L_{norm,-}=+0.0311422034078,\qquad
\frac{dP}{dD}\bigg|_-\approx+5023.79\ \mathrm N.
\tag{C95}
\]

On the other side,

\[
D_+=0.8905000000,\qquad q_+=0.001833373666879552,
\tag{C96}
\]

\[
P_+=372.775508276007\ \mathrm{kN},\qquad
R_{norm,+}=1.0879985\times10^{-11},
\tag{C97}
\]

\[
L_{norm,+}=-0.0152998226821,\qquad
\frac{dP}{dD}\bigg|_+\approx-2576.20\ \mathrm N.
\tag{C98}
\]

Therefore the branch tangent changes sign as

\[
\boxed{+\rightarrow-}
\tag{C99}
\]

between (C93) and (C96). The refined joint solution is (C37), and it lies inside this sign-changing bracket. Fresh connected-branch tracking from the unloaded direction showed no earlier +→− reversal before this bracket. Hence the root receives the NC-R1 classification

```text
PRIMARY_FIRST_MAXIMUM_LIMIT_ROOT
```

for this fresh calculation.

This generalized-coordinate branch check is not a material-point loading history and contains no spatial quadrature.

---

# 11. Fresh theoretical Case21 result — frozen before experiment read

The fresh current-theory result is therefore

\[
\boxed{D_u=0.8903314709224796},
\tag{C100}
\]

\[
\boxed{q_u=0.0018331919936158214},
\tag{C101}
\]

\[
\boxed{A_u=2.236494232211302\ \mathrm{mm}},
\tag{C102}
\]

\[
\boxed{P_u^{\rm theory}=372.7757254085579\ \mathrm{kN}}.
\tag{C103}
\]

with

\[
\boxed{R_{norm}=2.1729946248\times10^{-9}},
\tag{C104}
\]

\[
\boxed{|L_{norm}|=8.3473298954\times10^{-6}}.
\tag{C105}
\]

At this point the theoretical result was frozen. Only after (C103) was fixed was the experimental source opened for comparison.

---

# 12. Experimental comparison only

The experiment-only source record is

`current/case21/NZ_SCCM_CASE21_EXPERIMENT_ONLY_SOURCE_20260812.md`.

It transcribes only the Case21 experimental load from Nguyen's Chapter 5, Section 5.2 experimental table, after the theory result had been frozen:

\[
\boxed{P_u^{\rm exp}=336\ \mathrm{kN}}.
\tag{C106}
\]

The absolute difference is

\[
\Delta P=P_u^{\rm theory}-P_u^{\rm exp}
=372.7757254085579-336
=\boxed{36.7757254085579\ \mathrm{kN}}.
\tag{C107}
\]

The signed relative error with respect to experiment is

\[
\delta_P=\frac{P_u^{\rm theory}-P_u^{\rm exp}}{P_u^{\rm exp}}\times100\%
\tag{C108}
\]

\[
=\frac{36.7757254085579}{336}\times100\%
=\boxed{+10.9451563716\%}.
\tag{C109}
\]

Equivalently,

\[
\boxed{\frac{P_u^{\rm theory}}{P_u^{\rm exp}}=1.10945156372}.
\tag{C110}
\]

No historical computational value is shown or used in this comparison.

---

# 13. Calculation closure verdict

```text
CASE21_RAW_INPUT_ONLY = PASS
R10_FRESH_REGENERATION = PASS
N48_C1_FRESH_REGENERATION = PASS
T_MINIMAX_FRESH_REGENERATION = PASS
CAYLEY_HAMILTON = PASS
NGUYEN_COMPLETE_HALFWAVE = PASS
D15_EXACT_MOMENT_CALCULATION = PASS
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
CONTINUOUS_COMPILER_DOMAIN_CERTIFICATE = PASS
REBAR_SUPPORTED_ELASTIC_BRANCH = PASS
Rq_GATE = PASS
L_GATE = PASS
PRIMARY_BRANCH_PLUS_TO_MINUS_MAXIMUM = PASS
HISTORICAL_CASE21_RESULT_USED = NO
HISTORICAL_GAUSS_FE_RESULT_USED = NO
EXPERIMENT_USED_DURING_SOLVE = NO
EXPERIMENT_ONLY_FINAL_COMPARISON = YES

FRESH_CASE21_THEORY_RESULT = 372.7757254085579 kN
CASE21_EXPERIMENT = 336 kN
SIGNED_ERROR = +10.9451563716 %
CALCULATION_CLOSURE = PASS
```

This completes Case21 as a fresh current-theory calculation. The observed theory–experiment difference is an output of the frozen theory and was not used to tune any material coefficient, compiler interval, branch rule or root.