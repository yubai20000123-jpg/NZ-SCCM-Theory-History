# NZ-SCCM — 单一路径显式 BH/SSUHPC current-moment 一阶谐波闭合 R01

**Time:** 2026-08-27 17:10 +08:00  
**Status:** `SINGLE_EXPLICIT_METHOD_FROZEN / NO_NEW_MATERIAL_LAW / NO_FULL_HALFWAVE_CURRENT_INTEGRAL / BH050_SOLVER_READY`  
**Purpose:** 将已经存在于 GitHub 的 Marguerre–Airy、common curvature、qU-R02/R06、UHPC exact N–M、web exact resultant 统一成一套不再分叉、不再升级成 full-current 2D virtual-work 的显式极限承载力计算方法。

---

## 0. 冻结裁决

本文件只保留一条生产候选路线：

```text
initial full-composite Airy membrane skeleton
+ exact global q -> common curvature
+ exact qU GL augmentation inside steel-face R02/R06
+ unchanged UHPC directional exact N-M
+ unchanged exact web resultant
+ current normal-bending moments fed back through the SAME retained global harmonic
+ initial elastic twisting term retained
+ finite material endpoint candidates
+ zero formal spatial quadrature
```

明确禁止：

```text
independent kappa_x/kappa_y
full nonlinear UHPC shear/tensor upgrade
full-halfwave current-material area integration
D15/Chebyshev/Gauss/Simpson/material-point fallback
fitted curvature factor
fitted qU factor
effective width
FEM/test in root selection
```

关键修正不是增加一个新材料模型，而是把 20260827 13:35 已经证明缺失的 `current section bending -> global q equilibrium` 用**同一个保留的一阶全局谐波**闭合，而不是升级成全场 current virtual work。

---

# 1. Global Airy membrane skeleton

Global mode

\[
\psi=\sin\alpha x\sin\beta y,\qquad
\alpha=\pi/b,\qquad\beta=\pi/\ell.
\]

Stress-free imperfection and added deflection

\[
w_0=bq_0\psi,\qquad w_m=bq\psi.
\]

Define

\[
Q_q=q(q+2q_0).
\]

Retain the existing initial-composite extensional Airy coefficients

\[
K_x=\frac{\alpha^2b^2\Delta_A}{8A_{22}},
\qquad
G=\frac{\beta^2b^2\Delta_A}{8A_{11}},
\]

\[
K_m=\frac{\Delta_A}{16}
\left(\frac{\alpha^4}{A_{22}}+\frac{\beta^4}{A_{11}}\right),
\]

\[
C=\frac{b^3K_m}{\beta^2}.
\]

At longitudinal antinode and transverse station `s=sin(alpha x)`:

\[
N_x^d=K_xQ_q,
\]

\[
N_y^d=-\left[\frac{P}{b}+GQ_q(1-2s^2)\right].
\]

No current material tangent is inserted into this Airy compatibility skeleton.

---

# 2. Common global curvature is fixed by q

\[
\kappa_x^g=b\alpha^2qs,
\qquad
\kappa_y^g=b\beta^2qs.
\]

For BH, `ell=b`, hence at the governing antinode `s=1`:

\[
\boxed{
B_x=B_y=\kappa(q)=\frac{\pi^2q}{b}.
}
\]

No other curvature unknown exists.

---

# 3. Current section resultants

Let the two membrane offsets be

\[
A_x=\varepsilon_x^0,
\qquad
A_y=\varepsilon_y^0.
\]

Then core strains are

\[
\varepsilon_x(z)=A_x+B_xz,
\qquad
\varepsilon_y(z)=A_y+B_yz.
\]

The current section resultants are assembled as

\[
N_x^{sec}=N_x^U+N_{x,+}^s+N_{x,-}^s,
\]

\[
M_x^{sec}=M_x^U+z_fN_{x,+}^s-z_fN_{x,-}^s,
\]

\[
N_y^{sec}=N_y^U+N_y^w+N_{y,+}^s+N_{y,-}^s,
\]

\[
M_y^{sec}=M_y^U+M_y^w+z_fN_{y,+}^s-z_fN_{y,-}^s.
\]

Local R02 plate-bending moment is not added to gross composite moment.

---

# 4. UHPC exact directional N-M remains unchanged

Compression, tension-positive strain convention:

\[
\xi=-\varepsilon/\varepsilon_{c0},
\qquad
n_h=E_c\varepsilon_{c0}/f_c,
\]

\[
\sigma_U=-f_c\frac{n_h\xi-\xi^2}{1+(n_h-2)\xi},
\qquad 0\le\xi\le1.
\]

Tension uses the already frozen Hu-source branch.

Let `S0'(eps)=sigma_U(eps)` and `S1'(eps)=eps sigma_U(eps)` be the already derived exact primitives.
For `i=x,y`, with

\[
\varepsilon_\pm=A_i\pm B_it_c/2,
\]

and `B_i != 0`:

\[
N_i^U=(1-\rho_w)
\frac{S_0(\varepsilon_+)-S_0(\varepsilon_-)}{B_i},
\]

\[
M_i^U=(1-\rho_w)
\frac{S_1(\varepsilon_+)-S_1(\varepsilon_-)
-A_i[S_0(\varepsilon_+)-S_0(\varepsilon_-)]}{B_i^2}.
\]

No thickness quadrature.

---

# 5. Exact web resultant remains unchanged

The longitudinal web uses

\[
\varepsilon_y^w(z)=A_y+B_yz
\]

and ideal elastic-perfectly-plastic steel stress. Its `N_y^w,M_y^w` are exact piecewise polynomial endpoint integrals over the core/web height. No web x-resultant is added.

---

# 6. Steel faces: exact qU-augmented R02/R06

For each registered local cell

\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta),
\qquad k_x=2\pi/L_x,\quad k_y=2\pi/L_y.
\]

Define

\[
d=U^2-A_0^2,
\]

\[
\Delta=b[(q_0+q)U-q_0A_0].
\]

Exact GL means:

\[
m_x=e_x-c_xd-h_x\Delta,
\]

\[
m_y=e_y-c_yd-h_y\Delta,
\]

\[
m_\gamma=\gamma-h_\gamma\Delta.
\]

With

\[
C_{cc}=Q_s(c_x^2+2\nu_sc_xc_y+c_y^2),
\]

\[
C_{ch}=Q_s(c_xh_x+\nu_sc_xh_y+\nu_sc_yh_x+c_yh_y),
\]

\[
C_{hh}=Q_s(h_x^2+2\nu_sh_xh_y+h_y^2)+G_sh_\gamma^2,
\]

\[
L_c=Q_s[c_x(e_x+\nu_se_y)+c_y(e_y+\nu_se_x)],
\]

\[
L_h=Q_s[h_x(e_x+\nu_se_y)+h_y(e_y+\nu_se_x)]+G_s\gamma h_\gamma,
\]

and `a=A0`, `W=b(q0+q)`, `W0=bq0`, the local amplitude is the minimum-energy admissible nonnegative real root of

\[
B_3U^3+B_2U^2+B_1U+B_0=0,
\]

\[
B_3=2t_s(2E_sK_A+C_{cc}),
\]

\[
B_2=3Wt_s(2E_sK_{d\Delta}+C_{ch}),
\]

\[
B_1=K_b-B_3a^2
-2aW_0t_s(2E_sK_{d\Delta}+C_{ch})
+W^2t_s(2E_sK_{\Delta\Delta}+C_{hh})-2t_sL_c,
\]

\[
B_0=-aK_b-a^2Wt_s(2E_sK_{d\Delta}+C_{ch})
-aWW_0t_s(2E_sK_{\Delta\Delta}+C_{hh})-Wt_sL_h.
\]

R06 remains:

- if elastic local critical stress `>= fy`, yield-first/R04;
- if `< fy`, local-buckling-first;
- along radial state `q(eta)=eta q`, `eps_f(eta)=eta eps_f`, keep `q0,A0` fixed;
- determine the first finite-algebraic continuous local Mises maximum equal to `fy`;
- return the whole-width augmented-R02 mean resultant at that projected state.

No effective width and no spatial grid are part of the formal operator.

---

# 7. The missing closure: current moments enter the SAME one-harmonic q equation

This is the only new structural equation in R01.

The full-current 2D material field is **not** integrated over the halfwave. Instead, the current gross section moments are projected onto the only global harmonic retained by the theory:

\[
M_x(x,y)\approx\widehat M_x\sin\alpha x\sin\beta y,
\]

\[
M_y(x,y)\approx\widehat M_y\sin\alpha x\sin\beta y.
\]

The harmonic amplitudes are the current antinode section moments

\[
\widehat M_x=M_x^{sec}(q,A_x,A_y),
\qquad
\widehat M_y=M_y^{sec}(q,A_x,A_y).
\]

No nonlinear twist material law is introduced. The twisting harmonic retains the initial full-composite elastic term

\[
\widehat M_{xy}=-2bqD_{66}^0\alpha\beta.
\]

With

\[
\kappa_{x,q}=b\alpha^2\sin\alpha x\sin\beta y,
\]

\[
\kappa_{y,q}=b\beta^2\sin\alpha x\sin\beta y,
\]

\[
\kappa_{xy,q}=-2b\alpha\beta\cos\alpha x\cos\beta y,
\]

the retained-harmonic bending virtual-work numerator is exactly

\[
\boxed{
\mathcal B_{cur}
=\alpha^2\widehat M_x
+\beta^2\widehat M_y
+4bqD_{66}^0\alpha^2\beta^2.
}
\]

This is the current replacement of the old elastic scalar

\[
K_b b q.
\]

The global q-equilibrium therefore becomes

\[
K_mb^3q(q+q_0)(q+2q_0)
+\mathcal B_{cur}
-P\beta^2(q+q_0)=0.
\]

Hence the load is still explicit:

\[
\boxed{
P(q,A_x,A_y)
=\frac{\mathcal B_{cur}}{\beta^2(q+q_0)}
+Cq(q+2q_0).
}
\]

### Exact elastic regression

If the current section is elastic,

\[
\widehat M_x=bq(D_x\alpha^2+D_\mu\beta^2),
\]

\[
\widehat M_y=bq(D_\mu\alpha^2+D_y\beta^2),
\]

then

\[
\mathcal B_{cur}
=bq[D_x\alpha^4+2(D_\mu+2D_{66}^0)\alpha^2\beta^2+D_y\beta^4]
=K_b bq.
\]

Therefore

\[
P\to P_{cr}\frac q{q+q_0}+Cq(q+2q_0)
\]

exactly. No fitted degradation factor exists.

---

# 8. BH simplification

For the BH family

\[
\ell=b,\qquad \alpha=\beta=\pi/b.
\]

At `s=1`:

\[
\boxed{B_x=B_y=\pi^2q/b.}
\]

The current load formula collapses to

\[
\boxed{
P
=\frac{M_x^{sec}+M_y^{sec}+4bqD_{66}^0\alpha^2}{q+q_0}
+Cq(q+2q_0).
}
\]

The membrane demands are

\[
\boxed{N_x^d=K_xq(q+2q_0),}
\]

\[
\boxed{N_y^d=-P/b+Gq(q+2q_0).}
\]

Thus the old `Pcr q/(q+q0)` term is not separately retained once current moments are active; it is recovered automatically in the elastic regression above.

---

# 9. Ultimate-state equations: finite material endpoint candidates only

For each existing legitimate material endpoint `g_a=0`, solve only

\[
\boxed{R_x=N_x^{sec}-N_x^d=0,}
\]

\[
\boxed{R_y=N_y^{sec}-N_y^d=0,}
\]

\[
\boxed{g_a=0.}
\]

`P` in `N_y^d` is the current-moment load formula of Section 7/8.

No independent moment equation is added because the normal current moments have already entered the work-conjugate global q equation.

For the BH branch observed in all preceding blind solves, the finite UHPC candidate is

\[
\boxed{A_y-\frac{t_c}{2}\frac{\pi^2q}{b}=-\varepsilon_{c0}.}
\]

Therefore

\[
\boxed{A_y(q)=-\varepsilon_{c0}+\frac{t_c\pi^2}{2b}q.}
\]

The BH governing solve is reduced to only two unknowns

\[
\boxed{(q,A_x)}
\]

through

\[
R_x(q,A_x)=0,
\qquad
R_y(q,A_x)=0.
\]

At every trial `(q,A_x)`:

1. compute `A_y(q)`;
2. compute common curvature;
3. condense upper/lower `U` from the augmented cubic;
4. apply R06 if required;
5. evaluate UHPC/web/steel `N_x,N_y,M_x,M_y`;
6. compute `P` from the current-moment harmonic equation;
7. evaluate the two membrane residuals.

This is a finite algebraic/special-function root problem. No load stepping or spatial integration is required.

All other four UHPC compressed-face endpoints are solved in the same finite manner and the smallest admissible positive `P` is selected without comparator information.

---

# 10. BH050 constants already available

For BH050:

\[
b=2500\;\mathrm{mm},\quad t_s=4\;\mathrm{mm},\quad t_c=42\;\mathrm{mm},\quad z_f=23\;\mathrm{mm},
\]

\[
q_0=0.0025,
\qquad
L_x=562.5\;\mathrm{mm},
\qquad
L_y=555.5555556\;\mathrm{mm},
\]

\[
A_0=L_x/1600=0.3515625\;\mathrm{mm}.
\]

Global coefficients already frozen:

\[
K_x\approx4.272925966\times10^6\;\mathrm{N/mm},
\]

\[
G\approx4.400171479\times10^6\;\mathrm{N/mm},
\]

\[
C\approx10841.3718065234\;\mathrm{MN}.
\]

With the current phase geometry,

\[
D_{66}^0\approx4.46379928\times10^8\;\mathrm{N\,mm}.
\]

R02 geometry:

\[
c_x=4.67892356792\times10^{-5}\;\mathrm{mm^{-2}},
\]

\[
c_y=4.79662773893\times10^{-5}\;\mathrm{mm^{-2}}.
\]

TOP GL coefficients:

\[
h_x=h_y=1.530251331862\times10^{-6}\;\mathrm{mm^{-2}},
\]

\[
h_\gamma=0,
\]

\[
K_A=2.658832895996\times10^{-9}\;\mathrm{mm^{-4}},
\]

\[
K_{d\Delta}=6.028529628699\times10^{-11}\;\mathrm{mm^{-4}},
\]

\[
K_{\Delta\Delta}=1.461159027099\times10^{-12}\;\mathrm{mm^{-4}}.
\]

BOTTOM GL coefficients:

\[
h_x=h_y=1.435668541336\times10^{-6}\;\mathrm{mm^{-2}},
\]

\[
|h_\gamma|=1.867817909316\times10^{-7}\;\mathrm{mm^{-2}},
\]

\[
K_{d\Delta}=5.655914265997\times10^{-11}\;\mathrm{mm^{-4}},
\]

\[
K_{\Delta\Delta}=1.297175736660\times10^{-12}\;\mathrm{mm^{-4}}.
\]

The local elastic buckling stress is about `100.45 MPa < fy`, so BH050 uses the R06 local-buckling-first face operator.

No theoretical coefficient remains undefined for the BH050 two-unknown terminal system except the already-existing finite-algebraic GL+LL local-Mises maximum evaluation inside R06.

---

# 11. Sanity check against the failed 13:35 endpoint state

The 13:35 endpoint candidate had

\[
q=0.011215527128,
\]

\[
M_x^{sec}=23688.65\;\mathrm N,
\qquad
M_y^{sec}=12528.23\;\mathrm N.
\]

If those same section moments are inserted into the new current-moment load equation **without re-solving the membrane equations**, the load drops from the frozen-elastic-front value `17.9843 MN` to approximately

\[
P\approx10.38\;\mathrm{MN}.
\]

This is not a new BH050 prediction because the membrane equilibrium must be re-solved after `P` changes. It is only an algebraic direction/magnitude check showing that the missing current bending feedback acts on exactly the term that caused the 13:35 hard moment deficit. It is not a fitted correction.

---

# 12. Root discipline

For every active endpoint:

1. enumerate all real roots of the finite terminal system;
2. require `q>0`;
3. require all R02 amplitudes admissible and minimum-energy selected;
4. require R06 branch consistency;
5. require no other UHPC compressed endpoint has already exceeded `-eps_c0`;
6. require finite stress/resultants;
7. choose the smallest admissible positive load/root without FEM/test information.

No continuation/load history is part of the formal solver.

---

# 13. Why this is the intended reduced explicit method

The 13:35 failure established only one missing structural relation: current bending resistance was disconnected from the global q equilibrium. It did **not** establish a need for:

- full nonlinear UHPC shear;
- full 2D current-material field integration;
- independent section curvatures;
- D15 or spatial quadrature;
- a new steel law.

The present closure inserts the current normal section moments into the exact work-conjugate scalar occupied by the old `K_b b q` term, while retaining the only global harmonic already present in the theory. It therefore solves the missing-relation problem at the same reduced-order level as the original Marguerre–Airy theory.

The model limitation is explicit: nonlinear higher spatial harmonics of the current moment field are discarded. That is a deliberate single-harmonic reduced-theory approximation, not an unresolved computational blocker.

---

# 14. Frozen current status

```text
GLOBAL_MODE = ONE_RETAINED_SINE_HALFWAVE
AIRY_MEMBRANE = INITIAL_FULL_COMPOSITE
COMMON_CURVATURE = q_DERIVED_ONLY
STEEL_LOCAL = qU_AUGMENTED_R02_R06
UHPC = EXISTING_DIRECTIONAL_EXACT_NM
WEB = EXISTING_EXACT_AFFINE_EP
CURRENT_NORMAL_MOMENT_FEEDBACK = FIRST_HARMONIC_EXPLICIT
CURRENT_NONLINEAR_TWIST = NOT_INTRODUCED
TWIST_TERM = INITIAL_D66_RETAINED
FULL_HALFWAVE_CURRENT_MATERIAL_INTEGRAL = NO
FORMAL_SPATIAL_QUADRATURE = 0
BH050_TERMINAL_UNKNOWN_COUNT = 2
BH050_THEORY_BLOCKER = NONE
COMPARATOR_IN_ROOT_SELECTION = 0
```
