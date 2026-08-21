# NZ-SCCM PMV1-C73 — FINAL COMPLETE CALCULATION THEORY

时间：2026-08-21 15:43 +08:00
状态：`FINAL FORMAL CALCULATION THEORY / NO MEMBRANE-RITZ EXTENSION / NO EMPIRICAL FIT`

本文件从 Nguyen 二阶运动学开始，到直接极限联立方程结束。正式极限不使用 load stepping / pseudo-arclength 作为定义。

## 0. 输入与未知量

几何：`b, ell, tc`；钢壳另有每侧面板厚 `tf`、内部纵向腹板厚 `tw`、腹板节距 `ls`；RC 另有各方向/各层钢筋率 `rho_s,d,l` 和层坐标 `z_l`。

混凝土：`fc,E0,eps0,nu`。钢：`Es,nu_s,fy`。

初始缺陷 `A0` 为来源输入，`q0=A0/b`；当前附加幅值 `A=bq`。正式结构未知量只有 `D,q`。

## 1. Nguyen 二阶增量运动学

\[
\phi=\sin(\pi x/b)\sin(\pi y/\ell),\quad w_0=A_0\phi,\quad w_m=A\phi.
\]

相对初始缺陷参考面的二阶增量应变：

\[
\varepsilon_x=\nu\varepsilon_0D+\frac12[(w_0+w_m)_{,x}^2-w_{0,x}^2]-zw_{m,xx},
\]
\[
\varepsilon_y=-\varepsilon_0D+\frac12[(w_0+w_m)_{,y}^2-w_{0,y}^2]-zw_{m,yy},
\]
\[
\gamma_{xy}=[(w_0+w_m)_{,x}(w_0+w_m)_{,y}-w_{0,x}w_{0,y}]-2zw_{m,xy}.
\]

完全展开：

\[
\varepsilon_x=\nu\varepsilon_0D+\pi^2(q_0q+q^2/2)\cos^2X\sin^2Y+\frac{\pi^2zq}{b}\sin X\sin Y,
\]
\[
\varepsilon_y=-\varepsilon_0D+\frac{\pi^2b^2}{\ell^2}(q_0q+q^2/2)\sin^2X\cos^2Y+\frac{\pi^2bzq}{\ell^2}\sin X\sin Y,
\]
\[
\gamma_{xy}=\frac{2\pi^2b}{\ell}(q_0q+q^2/2)\sin X\cos X\sin Y\cos Y-\frac{2\pi^2zq}{\ell}\cos X\cos Y,
\]
where `X=pi*x/b, Y=pi*y/ell`.

Normalized strains are `e_x=eps_x/eps0`, etc. Their q derivatives are obtained directly; no numerical differencing.

## 2. Core polynomial form

Put `u=sin X,v=sin Y,zeta=2z/tc`. Then

\[
e_x^c=\nu D+\frac{\pi^2q(q+2q_0)}{2\varepsilon_0}(v^2-u^2v^2)+\frac{\pi^2t_cq}{2\varepsilon_0b}uv\zeta,
\]
\[
e_y^c=-D+\frac{\pi^2b^2q(q+2q_0)}{2\varepsilon_0\ell^2}(u^2-u^2v^2)+\frac{\pi^2bt_cq}{2\varepsilon_0\ell^2}uv\zeta.
\]

The shear-square polynomial is

\[
(g_{xy}^c)^2=\frac{\pi^4}{\varepsilon_0^2\ell^2}(1-u^2)(1-v^2)[bq(q+2q_0)uv-t_cq\zeta]^2.
\]

q derivatives:

\[
e_{x,q}^c=\frac{\pi^2(q+q_0)}{\varepsilon_0}(v^2-u^2v^2)+\frac{\pi^2t_c}{2\varepsilon_0b}uv\zeta,
\]
\[
e_{y,q}^c=\frac{\pi^2b^2(q+q_0)}{\varepsilon_0\ell^2}(u^2-u^2v^2)+\frac{\pi^2bt_c}{2\varepsilon_0\ell^2}uv\zeta,
\]
\[
g_q^c=\frac{\pi^2}{\varepsilon_0\ell}\sqrt{1-u^2}\sqrt{1-v^2}[2b(q+q_0)uv-t_c\zeta],
\]
\[
e_{x,qq}^c=\frac{\pi^2}{\varepsilon_0}(v^2-u^2v^2),
\]
\[
e_{y,qq}^c=\frac{\pi^2b^2}{\varepsilon_0\ell^2}(u^2-u^2v^2),
\]
\[
g_{qq}^c=\frac{2\pi^2b}{\varepsilon_0\ell}uv\sqrt{1-u^2}\sqrt{1-v^2}.
\]

D derivatives: `e_x,D=nu`, `e_y,D=-1`, `g_D=0`.

## 3. R10 source material

Constants: `rho=1/10, ur=3/100, eta_r=1/20, mt=-7/90`.

\[
H(r,r_0)=\frac12[(r-r_0)+\sqrt{(r-r_0)^2+1/400}]-\frac12[-r_0+\sqrt{r_0^2+1/400}],
\]
\[
T_{src}(r)=r-\frac{97}{90}H(r,1)+\frac7{90}H(r,10).
\]

Let `I_H(r0)=integral_0^10 H(r,r0)dr`; its explicit formula is

\[
I_H(r_0)=\frac14\left[(10-r_0)^2-r_0^2+(10-r_0)\sqrt{(10-r_0)^2+1/400}+r_0\sqrt{r_0^2+1/400}
+\frac1{400}\ln\frac{10-r_0+\sqrt{(10-r_0)^2+1/400}}{-r_0+\sqrt{r_0^2+1/400}}\right]
-5[-r_0+\sqrt{r_0^2+1/400}].
\]

Then

\[
h=\frac15\left\{\frac1{10}\left[50-\frac{97}{90}I_H(1)+\frac7{90}I_H(10)\right]-\frac1{100}-\frac{27}{200}\right\}.
\]

For each concrete:

\[
\kappa=E_0\varepsilon_0/f_c,\quad x_{cr}=f_c/(10E_0\varepsilon_0),\quad \eta=f_c/(200E_0\varepsilon_0).
\]

\[
\Pi(z)=\frac{z^2[\sqrt{z^2+(f_c/(200E_0\varepsilon_0))^2}+z]}{2[z^2+(f_c/(200E_0\varepsilon_0))^2]}.
\]

Set `c=Pi(-lambda), t=Pi(lambda), r=t/xcr=10E0 eps0 Pi(lambda)/fc`.

\[
C(\lambda)=\frac{(E_0\varepsilon_0/f_c)\Pi(-\lambda)}{1+(E_0\varepsilon_0/f_c-2)\Pi(-\lambda)+\Pi(-\lambda)^2}.
\]

For `0<=r<=1`,
\[
u_R=\frac1{10}r+(10h-3/5)r^3+(4/5-15h)r^4+(6h-3/10)r^5.
\]
For `1<r<=10`, with the displayed `r=10E0 eps0 Pi(lambda)/fc`,
\[
u_R=h+(3/100-h)\left[10((r-1)/9)^3-15((r-1)/9)^4+6((r-1)/9)^5\right].
\]
For `r>10`, `u_R=3/100`.

\[
T(\lambda)=10u_R(\Pi(\lambda)),
\]
\[
U(\lambda)=\frac{E_0\varepsilon_0}{f_c}\lambda-C(\lambda)+\frac{E_0\varepsilon_0}{f_c}\Pi(-\lambda)+u_R(\Pi(\lambda))-\frac{E_0\varepsilon_0}{f_c}\Pi(\lambda).
\]

## 4. N48-C1/MM coefficient generation

Material interval `[lambda_a,lambda_b]` is fixed by source/material-domain preflight, never by test/comparator load.

For j=0..48:
\[
\theta_j=(j+1/2)\pi/49,
\]
\[
\lambda_j=(\lambda_a+\lambda_b)/2+(\lambda_b-\lambda_a)\cos\theta_j/2.
\]

`V_jn=cos(n theta_j)`. At lambda=0,
\[
\xi_0=-(\lambda_a+\lambda_b)/(\lambda_b-\lambda_a).
\]

Constraint rows:
\[
A_{1n}=C_n(\xi_0),
\]
\[
A_{2,0}=0,\quad A_{2n}=\frac{2n}{\lambda_b-\lambda_a}U_{n-1}(\xi_0),\ n>=1.
\]

Root-grid Gram values are `h_0=49, h_n=49/2 (n>=1)`. For a target F define
\[
g_n^{(F)}=\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),
\]
\[
G_{ab}=\sum_{m=0}^{48}A_{am}h_m^{-1}A_{bm}.
\]

For F=U,C,T^7, every coefficient is
\[
a_n^{(F)}=h_n^{-1}g_n^{(F)}-h_n^{-1}\sum_{a=1}^2A_{an}\sum_{b=1}^2(G^{-1})_{ab}
\left[\sum_{m=0}^{48}A_{bm}h_m^{-1}g_m^{(F)}-b_b^{(F)}\right].
\]

Constraint vectors:
\[
b^{(U)}=(0,E_0\varepsilon_0/f_c)^T,\quad b^{(C)}=(0,0)^T,\quad b^{(T^7)}=(0,0)^T.
\]

For T, coefficients are the unique C1-constrained minimax solution:
\[
\min_{a_0...a_{48}}\max_{\lambda\in[\lambda_a,\lambda_b]}|T(\lambda)-\sum_{n=0}^{48}a_nC_n((2\lambda-\lambda_a-\lambda_b)/(\lambda_b-\lambda_a))|,
\]
subject to the same two zero value/zero derivative constraints at lambda=0.

No stored numeric coefficient array is part of the theory.

## 5. 2D Cayley-Hamilton construction

\[
X_{xx}=(e_x+\nu e_y)/(1-\nu^2),\quad X_{yy}=(\nu e_x+e_y)/(1-\nu^2),\quad X_{xy}=g/[2(1+\nu)].
\]

\[
I_1=trX=(e_x+e_y)/(1-\nu),
\]
\[
I_2=detX=\frac{\nu e_x^2+(1+\nu^2)e_xe_y+\nu e_y^2}{(1-\nu^2)^2}-\frac{g^2}{4(1+\nu)^2}.
\]

\[
K_1=\frac{2[I_1-(\lambda_a+\lambda_b)]}{\lambda_b-\lambda_a},
\]
\[
K_2=\frac{4I_2-2(\lambda_a+\lambda_b)I_1+(\lambda_a+\lambda_b)^2}{(\lambda_b-\lambda_a)^2},
\]
\[
Y_{yy}=\frac{2X_{yy}-(\lambda_a+\lambda_b)}{\lambda_b-\lambda_a}.
\]

For matrix Chebyshev polynomial `C_n(Y)=A_n I+B_nY`:
\[
A_0=1,B_0=0,A_1=0,B_1=1,
\]
\[
A_{n+1}=-2K_2B_n-A_{n-1},
\]
\[
B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
\]

For F=U,C,T,T7:
\[
A_F=\sum_{n=0}^{48}a_n^{(F)}A_n,\quad B_F=\sum_{n=0}^{48}a_n^{(F)}B_n.
\]

For any pair `(A,B)` representing `AI+BY`:
\[
tr=2A+BK_1,\quad det=A^2+ABK_1+B^2K_2.
\]
Product pairs F,G:
\[
A_{FG}=A_FA_G-B_FB_GK_2,
\]
\[
B_{FG}=A_FB_G+B_FA_G+B_FB_GK_1.
\]

Concrete interaction pairs:
\[
(A_{CC},B_{CC})=(detC\,A_C,detC\,B_C),
\]
\[
(A_{TC},B_{TC})=(trT\,A_C-A_{CT},trT\,B_C-B_{CT}),
\]
\[
(A_{TT},B_{TT})=(detT[A_{T7}+B_{T7}K_1],-detT B_{T7}).
\]

With `a_cc=0.1072329249362415` and `a_t=1-2^(-1/8)`,
\[
A_S=A_U-a_{cc}A_{CC}+A_{TC}-(1/10)a_tA_{TT},
\]
\[
B_S=B_U-a_{cc}B_{CC}+B_{TC}-(1/10)a_tB_{TT}.
\]

\[
S_{yy}=A_S+B_SY_{yy}.
\]

The normalized q-work density is
\[
Q_c=(1+\nu)\left[A_SI_{1,q}+\frac{2B_S}{\lambda_b-\lambda_a}
\left(I_1I_{1,q}-I_{2,q}-\frac{\lambda_a+\lambda_b}{2}I_{1,q}\right)\right]
-\nu I_{1,q}(2A_S+B_SK_1).
\]

## 6. Exact coefficient algebra / D15 moments

Every scalar field is represented as
\[
F(u,v,\zeta)=\sum_{ijk}f_{ijk}u^iv^j\zeta^k.
\]
Product coefficients are exactly
\[
(f*g)_{ijk}=\sum_{p=0}^i\sum_{r=0}^j\sum_{s=0}^k f_{prs}g_{i-p,j-r,k-s}.
\]

Exact moments:
\[
M_i=\int_0^\pi\sin^iX\,dX=\sqrt\pi\,\Gamma((i+1)/2)/\Gamma((i+2)/2),
\]
\[
Z_k=\int_{-1}^1\zeta^kd\zeta=(1+(-1)^k)/(k+1).
\]
Hence
\[
\iiint F=\sum_{ijk}f_{ijk}M_iM_jZ_k.
\]

Concrete resultants:
\[
P_c^{full}=-\frac{f_cb t_c}{2\pi^2}\sum_{ijk}[S_{yy}]_{ijk}M_iM_jZ_k,
\]
\[
R_{q,c}^{full}=\frac{f_c\varepsilon_0b\ell t_c}{2\pi^2}\sum_{ijk}[Q_c]_{ijk}M_iM_jZ_k.
\]

## 7. CAP-C73 steel compiler

Physical target:
\[
\alpha(r)=1\ (r\le1),\quad \alpha(r)=r^{-1/2}\ (1<r\le25/4).
\]

Production approximation:
\[
\alpha_{73}(r)=\sum_{n=0}^{73}d_nC_n(8r/25-1).
\]

\[
d_0=\frac1\pi\left[\frac45\ln\frac{5+\sqrt{21}}2+\pi-2\arccos\frac25\right].
\]

For n>=1:
\[
d_n=\frac2\pi\left\{\frac25\left[2(-1)^n\ln\frac{5+\sqrt{21}}2+4\sum_{j=1}^n(-1)^{n-j}\frac{\sin[(2j-1)\arccos(2/5)]}{2j-1}\right]-\frac{\sin[2n\arccos(2/5)]}{n}\right\}.
\]

Material-only gate gives degree 72 fail and degree 73 pass at `max error<=0.005`; no material fitting nodes remain.

For any polynomial `r(u,v,zeta)`, set `G0=1, G1=8r/25-1`,
\[
G_{n+1}=2(8r/25-1)G_n-G_{n-1},
\]
then `alpha_73=sum d_n G_n`; all coefficients are produced by the displayed finite convolution.

## 8. Outer faceplate steel

For face `s=+1,-1`, local coordinate eta_s in [-1,1]:
\[
z_s=s(t_c+t_f)/2+(t_f/2)\eta_s.
\]

Use the full Nguyen normalized strains at this physical z:
\[
e_x^s=\nu D+\frac{\pi^2q(q+2q_0)}{2\varepsilon_0}(v^2-u^2v^2)+\frac{\pi^2qz_s}{\varepsilon_0b}uv,
\]
\[
e_y^s=-D+\frac{\pi^2b^2q(q+2q_0)}{2\varepsilon_0\ell^2}(u^2-u^2v^2)+\frac{\pi^2bqz_s}{\varepsilon_0\ell^2}uv.
\]

Elastic trial:
\[
\sigma_x^{tr}=E_s\varepsilon_0(e_x^s+\nu_se_y^s)/(1-\nu_s^2),
\]
\[
\sigma_y^{tr}=E_s\varepsilon_0(\nu_se_x^s+e_y^s)/(1-\nu_s^2),
\]
\[
\tau^{tr}=E_s\varepsilon_0g^s/[2(1+\nu_s)].
\]

\[
r_s=\{(\sigma_x^{tr})^2-\sigma_x^{tr}\sigma_y^{tr}+(\sigma_y^{tr})^2+3(\tau^{tr})^2\}/f_y^2.
\]

Capped stresses are `alpha_73(r_s)` times the trial stresses.

Define the exact trial q-work polynomial
\[
Q_s^{tr}=\frac{E_s\varepsilon_0^2}{1-\nu_s^2}\left[(e_x^s+\nu_se_y^s)e_{x,q}^s+(\nu_se_x^s+e_y^s)e_{y,q}^s+\frac{1-\nu_s}{2}g^sg_q^s\right].
\]

If coefficient tensors of `alpha_73(r_s)*sigma_y^tr` and `alpha_73(r_s)*Q_s^tr` are respectively `p^s_ijk` and `r^s_ijk`,
\[
P_{sh}=-\frac{bt_f}{2\pi^2}\sum_{s=\pm1}\sum_{ijk}p^s_{ijk}M_iM_jZ_k,
\]
\[
R_{q,sh}=\frac{b\ell t_f}{2\pi^2}\sum_{s=\pm1}\sum_{ijk}r^s_{ijk}M_iM_jZ_k.
\]

## 9. Homogenized longitudinal web-steel phase

\[
\rho_w=t_w/l_s,
\]
\[
A_w=\rho_wbt_c=(b/l_s)t_wt_c,
\]
\[
A_c=(1-\rho_w)bt_c.
\]

Web trial stress at the core field:
\[
\sigma_w^{tr}=E_s\varepsilon_0e_y^c,
\]
\[
r_w=(E_s\varepsilon_0e_y^c/f_y)^2,
\]
\[
\sigma_w=\alpha_{73}(r_w)E_s\varepsilon_0e_y^c.
\]

With coefficient tensors of `sigma_w` and `sigma_w*eps0*e_y,q^c` denoted `w_ijk` and `v_ijk`,
\[
P_w=-\frac{\rho_wbt_c}{2\pi^2}\sum_{ijk}w_{ijk}M_iM_jZ_k,
\]
\[
R_{q,w}=\frac{\rho_wb\ell t_c}{2\pi^2}\sum_{ijk}v_{ijk}M_iM_jZ_k.
\]

## 10. RC reinforcement phase

For each direction d=x,y and layer l at z_l, define `rho_s,d,l` as its smeared volume ratio relative to gross concrete plate volume. Total replaced fraction:
\[
\rho_{s,tot}=\sum_l(\rho_{s,x,l}+\rho_{s,y,l}).
\]

Bar strain uses the same Nguyen field evaluated at z=z_l. Uniaxial trial/cap:
\[
\sigma_{s,d,l}^{tr}=E_s\varepsilon_0e_d(z_l),
\]
\[
r_{s,d,l}=(E_s\varepsilon_0e_d(z_l)/f_y)^2,
\]
\[
\sigma_{s,d,l}=\alpha_{73}(r_{s,d,l})E_s\varepsilon_0e_d(z_l).
\]

Using exact 2D moments `M_iM_j`,
\[
P_s=-\frac{bt_p}{\pi^2}\sum_l\rho_{s,y,l}\sum_{ij}[\sigma_{s,y,l}]_{ij}M_iM_j,
\]
\[
R_{q,s}=\frac{b\ell t_p}{\pi^2}\sum_l\sum_{d=x,y}\rho_{s,d,l}\sum_{ij}[\sigma_{s,d,l}\varepsilon_0e_{d,q}(z_l)]_{ij}M_iM_j.
\]

## 11. Phase-volume-conserving assembly

Steel-shell/web family:
\[
P=(1-t_w/l_s)P_c^{full}+P_w+P_{sh},
\]
\[
\mathcal R=(1-t_w/l_s)R_{q,c}^{full}+R_{q,w}+R_{q,sh}.
\]

RC family:
\[
P=[1-\sum_l(\rho_{s,x,l}+\rho_{s,y,l})]P_c^{full}+P_s,
\]
\[
\mathcal R=[1-\sum_l(\rho_{s,x,l}+\rho_{s,y,l})]R_{q,c}^{full}+R_{q,s}.
\]

## 12. Source-consistent analytic derivatives

No finite differences are formal. For `p=D or q`, differentiate all displayed polynomial recurrences.

CH derivative recurrence:
\[
A_{n+1,p}=-2(K_{2,p}B_n+K_2B_{n,p})-A_{n-1,p},
\]
\[
B_{n+1,p}=2A_{n,p}+2(K_{1,p}B_n+K_1B_{n,p})-B_{n-1,p}.
\]

CAP derivative recurrence: `G1,p=(8/25)r_p`,
\[
G_{n+1,p}=2[(8/25)r_pG_n+(8r/25-1)G_{n,p}]-G_{n-1,p}.
\]

All resultant derivatives are exact moment sums of derivative coefficient tensors.

## 13. Direct ultimate equations — no path tracking definition

After coefficient compilation, P(D,q) and R(D,q) are finite analytic/algebraic functions. Define
\[
L(D,q)=P_{,D}\mathcal R_{,q}-P_{,q}\mathcal R_{,D}.
\]

The ultimate state is obtained directly from
\[
\boxed{
\begin{cases}
\mathcal R(D,q)=0,\\
P_{,D}(D,q)\mathcal R_{,q}(D,q)-P_{,q}(D,q)\mathcal R_{,D}(D,q)=0.
\end{cases}}
\]

No Zhou/test load enters these equations. Formal solution may eliminate q by
\[
Res_q(\mathcal R,L)=0,
\]
then recover all real q roots. Admissibility uses only: `D>0`, chosen sign convention `q>=0`, `P>0`, compiler-domain checks, and local-maximum condition along R=0. For regular `R_q !=0`,
\[
q'=-\mathcal R_D/\mathcal R_q,
\]
\[
q''=-[\mathcal R_{DD}+2\mathcal R_{Dq}q'+\mathcal R_{qq}(q')^2]/\mathcal R_q,
\]
\[
P''=P_{DD}+2P_{Dq}q'+P_{qq}(q')^2+P_q q''<0.
\]

Under monotonic axial compression, if multiple admissible local maxima exist, choose the admissible maximum with smallest positive D; this is a root-selection rule, not load-path tracking and uses no experiment/comparator information.

Finally
\[
\boxed{P_u=P(D_u,q_u)}.
\]

## 14. Locked exclusions

No new membrane redistribution DOF; no Ritz H2/H4/...; no spatial Gauss/Simpson/cells; no empirical load scale; no test/comparator-based root selection; no extrapolation of N48 or CAP-C73 beyond its declared material domain.