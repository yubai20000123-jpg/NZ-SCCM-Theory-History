# NZ-SCCM — 钢壳–UHPC 显式极限承载力理论集中技术总账 R01

**Date:** 2026-08-31  
**Repository:** `yubai20000123-jpg/NZ-SCCM-Theory-History`  
**Working branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Document role:** `CENTRAL_TECHNICAL_LEDGER / THEORY–PARAMETER–ALGORITHM–CODE MAPPING / TRANSFER BASELINE`  
**Production main:** unchanged by this document.  
**Formal spatial quadrature:** `0`  
**Material-point grid:** `0`  
**Effective-width/effective-area repair:** prohibited.  
**Comparator/test/FEM in parameter calibration or root selection:** `0`.

---

## 0. What this ledger is, and what it is not

This ledger consolidates the currently recoverable steel-shell–UHPC calculation theory into one deterministic technical contract. It records parameter meaning and provenance, global Marguerre–Airy geometry/postbuckling, R02 local steel-face kinematics and finite Airy harmonics, R06 local-yield resultant gate, Zhang/Liu UHPC material/section operator, longitudinal-web constituent, section assembly, historical R4/J4 capacity-contact closure, later same-q deformation-compatible correction, Excel/AI transfer requirements and audit outputs.

This document does not use BH050 prediction error to change any equation. The deterministic state operator is reproducible. The unique physical structural ultimate-capacity terminal rule remains research-open after the 2026-08-31 BH050 diagnostic. Consequently historical/candidate terminal rules may be reproduced only under their explicit version labels.

---

# 1. Source/provenance ledger

1. `semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md` — global geometry, initial composite stiffness, integer half-wave scan, orthotropic buckling and Airy coefficients. Known blob SHA: `968f3ba1b6990bfc7a52e21de6a0047ea0866042`.
2. `semantic_v2/20_theory/20260822_1240__NZSCCM__UHPC_ZHANG_BACKBONE_AND_LIU_CC_CONTINUOUS_SOURCE_MIN_GATE.md` — Zhang-2023 UHPC compression backbone and analytic primitives; Liu-2024 capacity gate. SHA `409007a8e0aecb0c3f0ff02b66e8675aec4686bc`.
3. `semantic_v2/20_theory/20260822_1315__NZSCCM__NC_UHPC_7GATE_MATERIAL_CERTIFICATE_V1.md` — material-source/capacity-gate certificate.
4. `semantic_v2/20_theory/20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md` — authoritative R06. SHA `19ee5a7b40ae9a95d1bf4f720e6f4b1e06cf701d`.
5. `semantic_v2/20_theory/20260827_1623__NZSCCM__R02_NONNEGATIVE_AMPLITUDE_ACTIVESET_COMPLETION_R01.md` — complete R02 constrained active set. SHA `c0f680cfb83fd111cb33a2d285102071986e06d0`.
6. `20260827_1135__NZSCCM__UNIFIED_Q_U_EXPLICIT_KINEMATIC_LEDGER_AND_GENERALIZED_WORK_R01.md` — R02 q/U kinematics, LL/GL Airy harmonic ledger and generalized-work bookkeeping. This ledger retains the verified R02 kinematic/harmonic content; it does not silently reactivate superseded generalized-work closure variants.
7. `semantic_v2/40_execution/steel_shell/20260825_1622__NZSCCM__STEEL_SHELL_COMMON_R06_SSUHPC_7CASE_BH050_FULL_EXECUTION_R01.md` — source-audited BH050 input, ABD, mode scan, coefficients, exact constituent ledgers and historical five-equation capacity-contact solve. SHA `289b9dd61388ceb87a2ac9a73ab27a39ba4a419a`.
8. `semantic_v2/40_execution/steel_shell/20260831_1751__NZSCCM__BH050_CURRENT_STATE_OPEN_QUESTIONS_NEXT_CHAT_HANDOFF_R01.md` — latest variable identity and research boundary.

---

# 2. Units, coordinates, signs, ownership

Use one N–mm–MPa system. Length is mm; stress/modulus MPa; membrane resultants N/mm; bending moment resultant per unit width N; total load N; curvature mm^-1.

Global coordinates:
\[
0\le x\le b,\qquad0\le y\le a_{phys},
\]
with x transverse, y longitudinal/axial, z through thickness and positive to upper steel face. Current compression is stored with negative stress/strain in section ledgers while strengths are positive magnitudes.

Ownership:
- q = sole global structural postbuckling amplitude;
- actual kappa_geo comes from w(q);
- section membrane strains come from section equilibrium;
- R02 U comes from constrained energy condensation;
- R06 eta comes from local-yield projection;
- material parameters are source inputs only.

No comparator/test/FEM may be used for parameter identification or root selection.

---

# 3. Required new-specimen inputs

Gross geometry: b, a_phys, tc, ts, and global imperfection A0g or q0 with q0=A0g/b.

Longitudinal internal steel/web: exact web geometry or audited equivalent (count, thickness, net height, total area Aw, centroid/offset where required, rho_w=Aw/(b tc) for the distributed-core representation). Never double-count the same steel area in UHPC and web.

For every distinct R02 local-cell family: Lx, Ly, A0_local, cell origin/registration x0,y0 or an unambiguous pitch/offset generator, face sign sf, multiplicity and whole-width weighting. Gross dimensions alone are insufficient when a GL-active local-cell layout is not inferable.

Steel: Es, nu_s, fy and the declared web steel law.

UHPC: fc, Ec, eps_c0, nu_c, Vf and tensile/capacity-gate parameters required by the selected source contract.

Solver: integer mode scan range, terminal-rule ID, root/equilibrium tolerances, branch-continuation policy and calculation mode (`FULL_DERIVATION_MODE` or `FROZEN_COEFFICIENT_MODE`).

---

# 4. Global mode and postbuckling kinematics

For integer longitudinal half-wave count m:
\[
\ell_m=a_{phys}/m,\quad \alpha=\pi/b,\quad \beta_m=m\pi/a_{phys}=\pi/\ell_m.
\]

\[
\psi=\sin(\alpha x)\sin(\beta y).
\]

Initial and current deflection:
\[
w_0=A_{0,g}\psi=bq_0\psi,\qquad q_0=A_{0,g}/b,
\]
\[
w=b(q_0+q)\psi,\qquad w_d=bq\psi.
\]

Second-order amplitude:
\[
\boxed{Q(q)=q(q+2q_0)}.
\]

Actual geometric curvature increments:
\[
\kappa_x^{geo}=bq\alpha^2\psi,\qquad \kappa_y^{geo}=bq\beta^2\psi.
\]
At an antinode and ell=b:
\[
\boxed{\kappa_x^{geo}=\kappa_y^{geo}=\pi^2q/b}.
\]
Historical capacity-surface affine coordinates must not be renamed as these physical geometric curvatures.

---

# 5. Initial composite stiffness and orthotropic convention

Plane-stress constants:
\[
K_s^Z=E_s/[1-(\nu_s^Z)^2],\qquad G_s^Z=E_s/[2(1+\nu_s^Z)],
\]
\[
K_c^Z=E_c/[1-(\nu_c^Z)^2],\qquad G_c^Z=E_c/[2(1+\nu_c^Z)].
\]

With h=tc+2ts, a simple two-skin/core decomposition is
\[
D_{y,s}=2K_s^Z(t_sh^2/4+t_s^3/12),
\]
\[
D_{y,c}=K_c^Zt_c^3/12,\quad D_y=D_{y,s}+D_{y,c},
\]
\[
D_\mu=\nu_s^ZD_{y,s}+\nu_c^ZD_{y,c}.
\]
Production ABD may also contain audited longitudinal-web contributions; when present they must be retained.

Orthotropic moments:
\[
[M_x,M_y,M_{xy}]^T=
\begin{bmatrix}D_x&D_\mu&0\\D_\mu&D_y&0\\0&0&D_{66}\end{bmatrix}
[\kappa_x,\kappa_y,\kappa_{xy}]^T,
\quad \kappa_{xy}=-2w_{,xy}.
\]
Thus
\[
D_xw_{,xxxx}+2(D_\mu+2D_{66})w_{,xxyy}+D_yw_{,yyyy}=p.
\]
Project notation:
\[
\boxed{D_{xy}=2D_{66}},\qquad \boxed{H=D_\mu+D_{xy}=D_\mu+2D_{66}}.
\]
Do not identify Dxy with D12=Dmu.

---

# 6. Torsion check

External closed thin-walled steel shell:
\[
A_m=(b-t_s)(h-t_s),
\]
\[
J_s=4A_m^2/[2((b-t_s)+(h-t_s))/t_s].
\]

UHPC solid rectangular core:
\[
b_c=b-2t_s,\quad h_c=t_c,\quad r_h=h_c/b_c,
\]
\[
\beta_{shape}=\tfrac13(1-0.63r_h+0.052r_h^5),\quad J_c=\beta_{shape}b_ch_c^3.
\]

\[
D_t=(G_s^ZJ_s+G_c^ZJ_c)/b,\quad D_{xy}=D_t/2,\quad H=D_\mu+D_t/2.
\]
If a full audited ABD already supplies D66, use the torsion expression as a derivation/check and do not double-add it.

---

# 7. Initial integer-mode buckling

For every m:
\[
N_{cr,m}=[D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4]/\beta_m^2,
\]
\[
P_{cr,m}=bN_{cr,m}.
\]
Select m* as the minimum admissible Pcr,m without comparator information, then freeze ell, beta and Pcr.

---

# 8. Explicit Marguerre–Airy runtime demand

Compile deterministic coefficients Pcr,C,Kx,G,Jx,Jy once. At runtime:
\[
P^A(q)=P_{cr}q/(q+q_0)+C Q(q),
\]
\[
N_T^A=K_xQ(q)\cos(2\beta y),
\]
\[
N_L^A=-[P^A(q)/b+GQ(q)(1-2\sin^2\alpha x)],
\]
\[
M_T^A=J_xq\sin\alpha x\sin\beta y,
\]
\[
M_L^A=J_yq\sin\alpha x\sin\beta y.
\]

Example exact transverse membrane term:
\[
N_x=-\frac{\alpha^2b^2(A_{11}A_{22}-A_{12}^2)}{8A_{22}}Q(q)\cos(2\beta y).
\]
C,Kx,G,Jx,Jy are compiled theory coefficients, not fitted parameters. If a standalone implementation does not reproduce the whole Airy derivation, they must be supplied from an audited coefficient compiler and tagged `DERIVED_BY_AIRY_COMPILER`.

---

# 9. R02 local steel-face geometry and kinematics

Local coordinates 0<=xi<=Lx, 0<=eta<=Ly.
\[
k_x=2\pi/L_x,\qquad k_y=2\pi/L_y.
\]
These are geometric wave numbers, not regressions.

\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta).
\]
With X=kx xi, Y=ky eta:
\[
\phi_x=k_x\sin X(1-\cos Y),\quad
\phi_y=k_y(1-\cos X)\sin Y,
\]
\[
\phi_{xx}=k_x^2\cos X(1-\cos Y),\quad
\phi_{yy}=k_y^2(1-\cos X)\cos Y,
\]
\[
\phi_{xy}=k_xk_y\sin X\sin Y.
\]

Exact averages:
\[
c_x=3k_x^2/8,\qquad c_y=3k_y^2/8,\qquad \langle\phi_x\phi_y\rangle=0.
\]

Steel local plate stiffness:
\[
D_s=E_st_s^3/[12(1-\nu_s^2)],
\]
\[
K_b^\ell=D_s[\tfrac34(k_x^4+k_y^4)+\tfrac12k_x^2k_y^2].
\]

Local current amplitude U and imperfection A0:
\[
d=U^2-A_0^2,
\]
\[
\Delta=s_fb[(q_0+q)U-q_0A_0].
\]
Mean membrane strains:
\[
m_x=e_x-c_xd-h_x\Delta,
\]
\[
m_y=e_y-c_yd-h_y\Delta,
\]
\[
m_\gamma=\gamma-h_\gamma\Delta.
\]

---

# 10. R02 actual cell registration

Inside a cell:
\[
\psi=\sin[\alpha(x_0+\xi)]\sin[\beta(y_0+\eta)],
\]
\[
\delta_x=\alpha x_0,\qquad\delta_y=\beta y_0.
\]

\[
h_x=\langle\psi_x\phi_x\rangle,\quad
h_y=\langle\psi_y\phi_y\rangle,
\]
\[
h_\gamma=\langle\psi_x\phi_y+\psi_y\phi_x\rangle.
\]

Use exact 1D building blocks
\[
C(\omega,\delta;L)=[\sin(\omega L+\delta)-\sin\delta]/(\omega L),
\quad C(0,\delta;L)=\cos\delta,
\]
\[
S(\omega,\delta;L)=[\cos\delta-\cos(\omega L+\delta)]/(\omega L),
\quad S(0,\delta;L)=\sin\delta.
\]
A transfer package must provide x0,y0 (or an unambiguous deterministic generator) or provide audited hx,hy,hgamma. Omitting both leaves a GL-active R02 calculation under-specified.

---

# 11. R02 LL Airy compatibility

\[
\nabla^4F_{LL}=-E_sd(\phi_{xx}\phi_{yy}-\phi_{xy}^2).
\]
Exactly seven harmonics occur:
\[
(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)
\]
with coefficients
\[
1/2,-1/2,1/2,-1,1/2,-1/2,1/2.
\]

\[
\Lambda_{pq}=[(pk_x)^2+(qk_y)^2]^2,
\]
\[
F_{LL}=E_sdk_x^2k_y^2\sum c_{pq}\Lambda_{pq}^{-1}\cos(pX)\cos(qY).
\]

Airy stresses:
\[
\sigma_x=F_{,\eta\eta},\quad\sigma_y=F_{,\xi\xi},\quad\tau_{xy}=-F_{,\xi\eta}.
\]

\[
H_\nu=
\begin{bmatrix}1&-\nu_s&0\\-\nu_s&1&0\\0&0&2(1+\nu_s)\end{bmatrix}.
\]
Write sigma_LL=Es d sigmahat_LL. Then
\[
K_A=\tfrac12\langle\widehat\sigma_{LL}^TH_\nu\widehat\sigma_{LL}\rangle.
\]
Closed form:
\[
K_A=k_x^4k_y^4[17/(256k_y^4)+17/(256k_x^4)+1/(8(k_x^2+k_y^2)^2)+1/(32(k_x^2+4k_y^2)^2)+1/(32(4k_x^2+k_y^2)^2)].
\]

---

# 12. R02 GL Airy compatibility

\[
\mathcal C_{GL}=\psi_{xx}\phi_{yy}+\phi_{xx}\psi_{yy}-2\psi_{xy}\phi_{xy},
\]
\[
\nabla^4F_{GL}=-E_s\Delta\mathcal C_{GL}.
\]
Finite frequencies:
\[
\lambda\in\{\pm\alpha,\pm\alpha\pm k_x\},\quad
\mu\in\{\pm\beta,\pm\beta\pm k_y\}.
\]
For source mode c_r exp(i(lambda_r xi+mu_r eta)):
\[
F_{GL,r}=-E_s\Delta c_r(\lambda_r^2+\mu_r^2)^{-2}e^{i(\lambda_r\xi+\mu_r\eta)}.
\]
Normalized stress coefficient:
\[
\mathbf b_r=\frac{c_r}{(\lambda_r^2+\mu_r^2)^2}[\mu_r^2,\lambda_r^2,-\lambda_r\mu_r]^T.
\]
Exact cell integral:
\[
L^{-1}\int_{x_0}^{x_0+L}e^{i\omega x}dx=e^{i\omega(x_0+L/2)}\operatorname{sinc}(\omega L/2).
\]
In NumPy, project sinc(z)=sin(z)/z is `np.sinc(z/np.pi)`.

Write sigma_GL=Es Delta sigmahat_GL. Then
\[
K_{d\Delta}=\tfrac12\langle\widehat\sigma_{LL}^TH_\nu\widehat\sigma_{GL}\rangle,
\]
\[
K_{\Delta\Delta}=\tfrac12\langle\widehat\sigma_{GL}^TH_\nu\widehat\sigma_{GL}\rangle.
\]
Both are finite exact harmonic sums, not empirical constants.

---

# 13. R02 total energy and authoritative active set

\[
Q_s=E_s/(1-\nu_s^2),\qquad G_s=E_s/[2(1+\nu_s)].
\]

\[
\begin{aligned}
\Pi_{R02}(U)={}&\tfrac12K_b^\ell(U-A_0)^2\\
&+\tfrac12t_sQ_s(m_x^2+m_y^2+2\nu_sm_xm_y)\\
&+\tfrac12t_sG_sm_\gamma^2\\
&+t_sE_sK_Ad^2+2t_sE_sK_{d\Delta}d\Delta+t_sE_sK_{\Delta\Delta}\Delta^2.
\end{aligned}
\]
Pi is quartic and dPi/dU is cubic.

Authoritative condensation:
\[
\boxed{U^*=\arg\min_{U\ge0}\Pi_{R02}(U)}.
\]
Candidate set = boundary U=0 plus every positive real stationary root U>0. Compare the same energy at all candidates. At U=0 the KKT condition is B0>=0.

Do not impose U>=A0. Do not choose largest root, nearest root, or comparator-favored root. No positive stationary root does not imply a structural no-root condition because the active-set boundary U=0 may control.

---

# 14. R02 stress field

Mean stresses:
\[
\bar\sigma_x=E_s(m_x+\nu_sm_y)/(1-\nu_s^2),
\]
\[
\bar\sigma_y=E_s(m_y+\nu_sm_x)/(1-\nu_s^2),
\]
\[
\bar\tau_{xy}=G_sm_\gamma.
\]

Full field:
\[
\boldsymbol\sigma^{R02}=\bar{\boldsymbol\sigma}+\widetilde{\boldsymbol\sigma}^{LL}+\widetilde{\boldsymbol\sigma}^{GL}.
\]

\[
\sigma_{VM}=\sqrt{\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}.
\]
Return whole-width/cell-mean resultants, never an effective-width surrogate.

---

# 15. Authoritative R06 local-yield resultant gate

R06 is **not** a post-hoc scaling of a frozen fluctuation field.

Local elastic classification:
\[
\sigma_{cr,s}^{E}=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}k_{cr}(L_y/L_x).
\]
If sigma_cr_E>=fy, use yield-first parent ideal-EP/R04 terminal treatment. If sigma_cr_E<fy, activate R02/R06 local-buckling-first.

For the BH/Yun cell:
\[
r=L_y/L_x,\qquad k_{cr}=4(3r^4+2r^2+3)/(3r^2).
\]

For local-buckling-first define the generalized-strain ray
\[
\boldsymbol\varepsilon_f(\eta)=\eta\boldsymbol\varepsilon_f,\qquad0<\eta\le1.
\]
The q/U-augmented completion also records
\[
q(\eta)=\eta q,
\]
while q0 and A0 remain initial imperfection data.

For every trial eta:
1. rebuild R02 mean strains, d and Delta;
2. re-condense U*(eta)=argmin_{U>=0} Pi(U;eta);
3. reconstruct complete LL+GL local stress field;
4. evaluate the exact finite-algebraic maximum local Mises.

First local yield satisfies
\[
\max_\Omega\sigma_{VM}(\eta_y)=f_y.
\]
The face returned to the section is the whole-width R02 mean resultant at this re-condensed eta_y state.

Forbidden: pointwise clipping, effective width/area, simple fluctuation shrinkage around a frozen mean, freezing U while solving eta, comparator-dependent eta.

If a current tangent is required on R06+, it must differentiate through both U*(eta) and eta_y; finite difference is an audit oracle only.

---

# 16. UHPC Zhang compression backbone

Compression magnitude x=|eps_c|/eps_c0. Define
\[
\kappa_U=E_c\varepsilon_{c0}/f_c,
\]
\[
r=E_c/(E_c-f_c/\varepsilon_{c0})=\kappa_U/(\kappa_U-1).
\]
Ascending 0<=x<=1:
\[
\boxed{g_a(x)=rx/(r-1+x^r)},\qquad \sigma_c=f_cg_a(x).
\]
\[
g_a'(x)=r(r-1)(1-x^r)/(r-1+x^r)^2.
\]
The origin tangent is Ec.

For the source-audited 2%-fibre zero-confinement descending branch:
\[
f_{cr}/f_c=9V_f=0.18,\qquad n=2/(1+100V_f)=2/3,
\]
\[
\boxed{g_d(x)=0.18+0.82/[1+(2/3)(x-1)^2]},\quad x\ge1.
\]
\[
g_d'(x)=-2n(1-0.18)(x-1)/[1+n(x-1)^2]^2.
\]
Ascending and descending meet C1 at the peak.

---

# 17. Exact UHPC through-thickness primitives

Ascending: A=r-1,
\[
I_m(x)=\frac{x^{m+1}}{(m+1)A}{}_2F_1(1,(m+1)/r;1+(m+1)/r;-x^r/A).
\]
\[
\int g_a dx=rI_1,\qquad\int xg_a dx=rI_2.
\]

Descending:
\[
\int g_d dx=0.18x+0.82\arctan[\sqrt n(x-1)]/\sqrt n,
\]
\[
\int xg_d dx=0.09x^2+0.82[(2n)^{-1}\ln(1+n(x-1)^2)+\arctan(\sqrt n(x-1))/\sqrt n].
\]
Therefore affine thickness strain can be integrated by exact endpoint primitive differences; formal thickness Gauss points are unnecessary.

---

# 18. UHPC section operator and 2D capacity gates

For i in {x,y}:
\[
\varepsilon_i(z)=\varepsilon_i^0+\kappa_i z.
\]

\[
N_i^U=(1-\rho_w)\int_{-t_c/2}^{t_c/2}\sigma_U(\varepsilon_i^0+\kappa_i z)dz,
\]
\[
M_i^U=(1-\rho_w)\int_{-t_c/2}^{t_c/2}z\sigma_U(\varepsilon_i^0+\kappa_i z)dz.
\]

With F0'=sigma and F1'=eps sigma, eps_±=eps0±kappa tc/2:
\[
N^U=(1-\rho_w)[F_0(\varepsilon_+)-F_0(\varepsilon_-)]/\kappa,
\]
\[
M^U=(1-\rho_w)\{F_1(\varepsilon_+)-F_1(\varepsilon_-)-\varepsilon_0[F_0(\varepsilon_+)-F_0(\varepsilon_-)]\}/\kappa^2.
\]
Use analytic kappa->0 limits.

Material architecture separates current stress backbone from finite 2D capacity/admissibility gates. For UHPC CC, ordered compression ratio rc=pm/pM:
\[
K_E=1/\sqrt{r_c^2-1.49r_c+1},
\]
\[
K_P=(r_c+7.98)/(r_c+1.85)^2,
\]
\[
K_{CC,U}^{min}=\min(K_E,K_P),
\]
\[
\lambda_{CC,U}=f_cK_{CC,U}^{min}/p_M^d.
\]
The unique source-min intersection is rc*=0.576358545117484; retain its finite derivative cusp rather than inserting an arbitrary smoothing width.

UHPC TC capacity source:
\[
t/f_t=1,\quad 0\le p/f_c\le0.352,
\]
then
\[
t/f_t+1.542p/f_c-1.542=0,\quad0.352\le p/f_c\le1.
\]
Optional current softening uses only excess transverse tension:
\[
\varepsilon_{t,ex}=\max(0,\varepsilon_t+\nu\varepsilon_c),
\]
\[
\beta_{TC}=\max[0.55,(1+2500\varepsilon_{t,ex})^{-0.20].
\]

---

# 19. Longitudinal web and total section

Where physical longitudinal web steel exists it is a separate constituent. Do not reinterpret a boundary condition as material and do not double count steel.

Total section generalized resultant:
\[
\mathbf S=[N_x,M_x,N_y,M_y]^T
=\mathbf S_U+\mathbf S_{s,+}+\mathbf S_{s,-}+\mathbf S_w.
\]
Every implementation must retain all constituent ledgers before summing. A total load alone is not a sufficient audit output.

Face centroids:
\[
z_\pm=\pm(t_c/2+t_s/2).
\]

---

# 20. Versioned section/terminal closures

## 20.1 Historical R4/J4 capacity-contact map
Historical state:
\[
\mathbf x=[\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y]^T.
\]
Demand:
\[
\mathbf D^A(q)=[N_x^A,M_x^A,N_y^A,M_y^A]^T.
\]
Residual:
\[
\mathbf R_4=\mathbf S(\mathbf x,q)-\mathbf D^A(q)=0,
\]
with
\[
J_4=\partial\mathbf R_4/\partial\mathbf x.
\]
This remains a reproducible historical/candidate capacity-contact construction. Later diagnostics corrected the interpretation: its affine capacity coordinates are not automatically the geometric curvatures from w(q). A J4 section-mapping singularity is not automatically the physical structural ultimate mechanism.

## 20.2 Same-q deformation-compatible research closure
The conceptual correction assigns curvature ownership to q:
\[
q\rightarrow w_d\rightarrow\kappa_x^{geo}(q),\kappa_y^{geo}(q).
\]
At fixed q one can solve membrane strains from Nx,Ny equilibrium with geometric curvatures fixed, then read off moments instead of independently solving a second curvature pair. As of 2026-08-31 this current-section/structural-tangent endpoint is research-open, not a frozen production terminal rule.

Latest diagnostic bookkeeping also uses
\[
\varepsilon_x=\varepsilon_{x0}+\tfrac12[(g')^2-(g_0')^2],\quad
\varepsilon_y=\varepsilon_{y0},\quad
\gamma_{xy}=\gamma_{xy0},\quad
\kappa_y=-g'',
\]
and
\[
\widetilde\kappa_y=\varepsilon_{y0}-\beta\kappa_g.
\]
The tilde quantity is a combined current coordinate, not a second physical curvature.

---

# 21. Candidate terminal-rule registry

`FORCE_FIRST_CAPACITY_CONTACT_R01`: reproduce the historical source-audited Airy-N/M capacity-contact solve. In the BH050 historical execution the fifth equation was eps_y(-tc/2)=-eps_c0. Output label: `AIRY_NM_CAPACITY_CONTACT_PREDICTION`.

`J4_FIRST_FOLD_DIAGNOSTIC`: section-mapping fold candidate only. Output label: `J4_FOLD_CANDIDATE`.

`DEFORMATION_COMPATIBLE_STRUCTURAL_TERMINAL`: reserved for a future fully derived/frozen same-q structural terminal rule. Current status `NOT_FROZEN`.

Default unfamiliar-AI behavior: if no terminal rule is explicitly selected, stop and report that the physical terminal rule is not frozen rather than silently inventing one.

---

# 22. Equation-to-code map

Recommended modules:
```text
geometry.py
initial_stiffness.py
global_airy.py
local_r02_geometry.py
local_r02_harmonics.py
local_r02_energy.py
steel_r06.py
uhpc_backbone.py
uhpc_primitives.py
section_uhpc.py
section_web.py
section_assembly.py
solver_capacity_contact.py
solver_same_q.py
consistent_tangent.py
audit.py
```

R02 active set pseudo-code:
```python
roots = positive_real_roots(cubic_coefficients)
candidates = [0.0] + roots
U = argmin(candidates, key=Pi_R02)
```

R06 local-buckling-first pseudo-code:
```python
def projected_face(eta):
    e_eta = eta * face_generalized_strain
    q_eta = eta * q
    U_eta = condense_r02_active_set(q_eta, e_eta)
    field = reconstruct_exact_R02_field(q_eta, e_eta, U_eta)
    return U_eta, field, exact_global_max_mises(field)

eta_y = first_root_in_0_1(max_mises(eta) - fy)
return whole_width_mean_resultant(projected_face(eta_y))
```

The production current tangent must be differentiated from the same current operator; finite differences are independent audits only.

---

# 23. Excel implementation verdict

Pure worksheet formulas can evaluate geometry, q0/alpha/beta/ell, initial material constants, simple ABD/torsion relations, integer mode table, Pcr, Q(q), Airy demand for supplied compiled coefficients, kx/ky/cx/cy/Ds/Kb/KA, exact C/S registration building blocks, polynomial energy evaluation, UHPC scalar branches/primitives and constituent residual ledgers.

Robust full solving needs procedural logic (Solver/VBA/Office Script or equivalent) for cubic-root enumeration + active-set energy comparison, branch continuation, R06 nested eta solve with R02 re-condensation at every eta, finite-algebraic local-Mises maximum event enumeration, coupled nonlinear section solve and terminal-event selection.

Therefore:
`EXCEL_IMPLEMENTATION_FEASIBLE = YES_WITH_SOLVER_OR_SCRIPT`.
A formula-only sheet is suitable for fixed-state checks/precompiled coefficients, but should not be called a robust general-purpose production solver unless every active-set/event rule is encoded.

---

# 24. Stranger-AI transfer verdict

An unfamiliar AI can reproduce a candidate/historical capacity if it receives this ledger, the transfer contract, a complete specimen parameter file, all non-inferable local-cell registrations, material source parameters, Airy coefficients or enough derivation to compile them, the terminal-rule ID, tolerances and audit requirements.

It must not invent missing inputs, calibrate to FEM/test, replace R02 by effective width, replace R06 by clipping/simple fluctuation scaling, replace exact thickness primitives by material points as the formal theory, or select a root by comparator proximity.

---

# 25. Minimum audit output

Every predicted specimen must retain:
- raw inputs and source/version tags;
- selected m*, ell, alpha, beta;
- Pcr and Airy coefficients;
- local kx,ky,cx,cy,Kb,KA,hx,hy,hgamma,KdDelta,KDeltaDelta;
- all R02 candidate roots/energies and selected U;
- R06 branch and eta_y/U(eta_y)/certified max local Mises when active;
- UHPC face strains and active branches;
- constituent S_U, S_upper, S_lower, S_web;
- total S and Airy demand;
- raw residuals;
- terminal-rule ID;
- terminal q and P;
- output-status label.

---

# 26. Source-audited BH050 reference input

```text
b = 2500 mm
a_phys = 5000 mm
tc = 42 mm
ts = 4 mm
zf = 23 mm
9 longitudinal webs
net web height = 37 mm
Aw = 1332 mm2
rho_w = 0.0126857142857143
q0 = 0.0025
A0g = 6.25 mm

steel: Es=206000 MPa, nu_s=0.30, fy=355 MPa
UHPC: Ec=43400 MPa, nu_c=0.20, fc=141.1 MPa, eps_c0=0.0035, Vf=0.02
UHPC tension in frozen 20260825 execution: fct=4.513133983249735 MPa, eps_t0=0.001, mt=0.4418

local BH cell: Lx=562.5 mm, Ly=555.555555555556 mm, A0=0.3515625 mm
```

Audited initial stiffness:
```text
A11=3.685652010989011e6 N/mm
A22=3.795408810989011e6 N/mm
A12=9.182293032967034e5 N/mm
A66=1.383711353846154e6 N/mm
Dx=1.236003299827839e9 Nmm
Dy=1.252137549427839e9 Nmm
Dmu=3.432434438483517e8 Nmm
D66=4.463799279897436e8 Nmm
H=1.236003299827839e9 Nmm
```

Mode/Airy audit:
```text
m*=2
ell=2500 mm
alpha=beta=pi/2500
Pcr=19.5818772367311 MN
Kx=4.272925966136171e6 N/mm
G=4.400171479082513e6 N/mm
C=1.0841371806523354e10 N
Jx=6.234616244717026e6 N
Jy=6.298311709061200e6 N
sigma_cr,s^E=100.449667483867 MPa < fy
R06 branch=LOCAL_BUCKLING_FIRST
```

These are audit references, not comparator-fitted parameters.

Historical five-equation capacity-contact regression checkpoint only:
```text
q=0.004772819645833164
P=13.3563763545430 MN
label=BH050_HISTORICAL_AIRY_NM_CAPACITY_CONTACT_REGRESSION_CHECK
```
This ledger does not promote that checkpoint into a proved deformation-compatible structural ultimate load.

---

# 27. Standalone reproducibility status

```text
STATE_EVALUATION_FORMULAS_EXPLICIT = YES
R02_ACTIVE_SET_DEFINED = YES
R06_LOCAL_YIELD_PROJECTION_DEFINED = YES
UHPC_COMPRESSION_AND_SECTION_PRIMITIVES_DEFINED = YES
GLOBAL_AIRY_RUNTIME_DEMAND_DEFINED = YES
EXCEL_IMPLEMENTATION_FEASIBLE = YES_WITH_SOLVER_OR_SCRIPT
STRANGER_AI_IMPLEMENTATION_FEASIBLE = YES_WITH_COMPLETE_INPUT_CONTRACT
GROSS_GEOMETRY_ALONE_SUFFICIENT = NO
LOCAL_CELL_REGISTRATION_REQUIRED_WHEN_GL_ACTIVE = YES
COMPARATOR_CALIBRATION_ALLOWED = NO
PHYSICAL_ULTIMATE_TERMINAL_RULE_FROZEN = NO
DEFAULT_NEW_SPECIMEN_OUTPUT_STATUS = CANDIDATE_LIMIT_STATE
```

This ledger is therefore sufficient as a technical implementation contract when paired with a complete parameter package and an explicit terminal-rule version. It deliberately does not claim that the current research has frozen the unique physical Pu criterion.

**END OF CENTRAL TECHNICAL LEDGER R01**