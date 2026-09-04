# NZ-SCCM 多波钢壳04——考虑剪切滑移的平均组合版本 R01

**Date:** 2026-09-04  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `DIAGNOSTIC THEORY / NOT PRODUCTION R14`  
**Parent 1:** `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_01_NO_SHEAR_SLIP_FULL_DERIVATION_R01.md`  
**Parent 2:** `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_02_FIXED_RIB_SLIP_STIFFNESS_R01.md`  
**Supersedes for slip treatment:** old 02 fixed-`K_r` / direct-`gamma` slip reduction and the later distributed-harmonic slip experiments that were allowed to reselect the global halfwave number.  
**Does not supersede:** frozen R14 global mechanics, Multiwave 01 local-cell mechanics, R02/R06, UHPC/web constitutive primitives, or the connected-branch terminal rule.

---

# 0. Purpose and scope

Multiwave Steel Shell 04 is the corrected averaged-partial-interaction version for the current UCFT steel-shell/UHPC plate.

The purpose is narrow:

> account for finite longitudinal shear transfer between the steel shell and UHPC through the actual connector/interface stiffness, without introducing a new slip wave, without changing the already established global buckling halfwave, and without coupling the connector stiffness to the local 3/4/5 bulge count.

The governing hierarchy is therefore

```text
R14 global mode and one representative global halfwave
        ↓
Multiwave 01 local-cell classification and R02/R06
        ↓
04 averaged steel–UHPC partial interaction
        ↓
face-average steel stresses
        ↓
steel-shell N/M + UHPC N/M + web N/M
        ↓
existing R4 equilibrium and existing connected-branch terminal rule
```

The slip module is a **section-level / composite-action correction layer**. It does not own the global mode number `m`, the local bulge number `n`, the R02 amplitude equation, the R06 finite harmonic set, the UHPC material law, or the Airy `P(q)` skeleton.

---

# 1. What is retained and what is deleted from Multiwave 02

## 1.1 Retained

The following concepts from Multiwave 02 are retained:

1. steel and UHPC are allowed to have finite longitudinal shear interaction;
2. the slip effect is represented by an **averaged composite-action coefficient**, not by a spatial material-point slip mesh;
3. no new outer equilibrium unknown is introduced;
4. the final effect of slip enters the steel/UHPC force and moment distribution before the existing `R4=0` equilibrium is evaluated;
5. the rigid-interface limit must return exactly to Multiwave 01.

## 1.2 Deleted

The following old-02 constructs are formally deleted from the active slip theory:

\[
K_r=75.835\ \mathrm{kN/mm/rib}
\]

derived from a thin-rib steel shear-yield force divided by an assumed 0.2 mm slip, and

\[
\gamma=\frac{K_P}{K_P+K_{eq}}.
\]

The reason is not that averaged slip is invalid. The reason is that these two quantities had the wrong physical identity:

- `K_r` was a concentrated force/slip spring assigned to one complete rib even though the actual transfer is distributed along its length;
- its source was steel net-section shear yielding rather than a steel–UHPC load-slip relation;
- `gamma` directly reduced `z_f kappa_y` without a source-based composite-beam stiffness relation;
- the old `K_c` used half of the UHPC core while the curvature lever arm was taken as the steel-face distance to the whole-core midplane, which mixed two different geometries.

---

# 2. Distinction between the old `K_r` and the current shear-transfer stiffness

This distinction is fundamental.

## 2.1 Old `K_r`

The deleted old parameter was

\[
\boxed{K_r^{old}=75.835\ \mathrm{kN/mm/rib}}.
\]

Its dimension was

\[
[K_r^{old}]=\mathrm{N/mm}.
\]

Its intended meaning was:

> one complete longitudinal rib is replaced by one concentrated force–slip spring.

The old face spring was

\[
K_P=N_rK_r^{old}.
\]

Therefore `K_r` contained no explicit longitudinal length scaling.

## 2.2 Current unperforated-rib interface stiffness `K_t`

For the present model, the longitudinal stiffener is **unperforated**. The relevant physical object is not a PBL dowel and not the steel shear yield of the rib. It is the steel–UHPC tangential interface relation

\[
\boxed{\tau=K_t\delta}
\]

where

- `tau` = tangential interface traction, N/mm^2;
- `delta` = local relative slip, mm;
- `K_t` = tangential interface stiffness per unit bonded area, N/mm^3.

Thus

\[
\boxed{[K_t]=\mathrm{N/mm^3}}.
\]

This is a constitutive interface parameter, not a whole-rib spring constant.

Published steel–UHPC interface work without mechanical shear connectors has used exactly this traction–separation form. Two reported calibrated values that may be used only as **reference sensitivity points**, not as the current specimen value, are:

- sandblasted steel–UHPC interface: `K_t = 696 N/mm^3`;
- epoxy adhesive with sprinkled basalt aggregate interface: `K_t = 13 N/mm^3`.

The present UCFT unperforated stiffener surface treatment is not yet source-locked to either of those interfaces. Therefore 04 does **not** freeze a production value of `K_t`.

## 2.3 From `K_t` to one-rib unit-length shear stiffness

Current rib net height:

\[
h_r=37\ \mathrm{mm}.
\]

04 initially counts the two vertical rib side surfaces only. For a rib segment of longitudinal length `dy`, bonded area is

\[
dA_b=2h_r\,dy.
\]

The transferred shear force is

\[
dV=\tau dA_b=K_t\delta\,2h_rdy.
\]

Hence the force transferred per unit longitudinal length is

\[
q_r=\frac{dV}{dy}=2h_rK_t\delta.
\]

Define

\[
\boxed{k_{\ell,r}^{plain}=2h_rK_t}
\]

so

\[
\boxed{q_r=k_{\ell,r}^{plain}\delta}.
\]

Its dimension is

\[
[k_{\ell,r}]=\mathrm{N/mm^2}.
\]

For a face with `N_r` active longitudinal ribs,

\[
\boxed{k_{\ell,f}^{plain}=N_r\,2h_rK_t}.
\]

For the present BH arrangement,

\[
N_r^+=4,\qquad N_r^-=5,
\]

therefore

\[
\boxed{k_{\ell,+}^{plain}=8h_rK_t=296K_t}
\]

and

\[
\boxed{k_{\ell,-}^{plain}=10h_rK_t=370K_t}.
\]

The unit is N/mm^2 when `K_t` is in N/mm^3.

## 2.4 Explanatory comparison with old `K_r`

The current `k_{\ell,r}` must not be numerically compared directly with old `K_r` because they have different dimensions and different mechanical topology.

If, only for interpretation, a uniform slip is assumed along a rib length `L`, the current distributed law corresponds to an equivalent concentrated stiffness

\[
K_{r,eq}^{plain}=k_{\ell,r}^{plain}L=2h_rK_tL.
\]

For `h_r=37 mm` and `K_t=13 N/mm^3`:

- at `L=3200 mm`, `K_{r,eq}=3078.4 kN/mm/rib`;
- at `L=5000 mm`, `K_{r,eq}=4810.0 kN/mm/rib`.

Both are already far larger than the deleted `75.835 kN/mm/rib`.

For `K_t=696 N/mm^3`, the equivalent values are much larger again. These equivalent values are **not used in the 04 equations**; they are shown only to explain why old 02 produced unrealistically large slip release.

---

# 3. 04 connector-source module: unperforated rib now, PBL later

The central design decision in 04 is that all connector types must enter through the same unit-length shear stiffness interface

\[
\boxed{k_{\ell,r}}.
\]

Everything after `k_{\ell,r}` is connector-type independent.

## 3.1 Current unperforated rib

Use

\[
\boxed{k_{\ell,r}=2h_rK_t}.
\]

## 3.2 Future perforated/PBL rib

If the stiffener is later changed to an actual perforated plate with discrete holes, define the single-hole shear stiffness

\[
\boxed{k_{ps}\ [\mathrm{N/mm/hole}]}.
\]

For a hole pitch `p_h`, homogenize the discrete holes into a longitudinal unit-length stiffness

\[
\boxed{k_{\ell,r}^{PBL}=\frac{k_{ps}}{p_h}}.
\]

Then for one steel face

\[
\boxed{k_{\ell,f}^{PBL}=N_r\frac{k_{ps}}{p_h}}.
\]

The user-supplied design formula may be used as one source for `k_ps`:

\[
\boxed{k_{ps}=23.4\sqrt{(d-d_s)d_sE_cf_{ck}}}
\]

with

- `d` = PBL hole diameter, mm;
- `d_s` = transverse rebar diameter through the hole, mm;
- `E_c` = concrete elastic modulus, MPa;
- `f_ck` = concrete compressive strength standard value, MPa;
- `k_ps` = N/mm per hole.

If both the steel–UHPC bond and the mechanical PBL dowel action are represented separately and the adopted source relations do not already include the same bond contribution, the generalized connector model may be written

\[
\boxed{k_{\ell,r}=2h_rK_t+\frac{k_{ps}}{p_h}}.
\]

However, this additive form is **not automatic**. Before using it, one must check that the `k_ps` source formula represents mechanical hole/dowel action rather than a total measured connection stiffness that already contains bond/friction. Otherwise the bond term would be double-counted.

## 3.3 Geometric warning for the present 4 mm × 37 mm rib

The current rib geometry is not automatically suitable for conversion into a real PBL rib.

Existing PBL design research recommends substantially thicker perforated rib plates and gives minimum hole-spacing requirements. In particular, the current uploaded PBL tower research recommends a PBL stiffener plate thickness not less than 10 mm and recommends the circular-hole center spacing at approximately `2.5d–3.5d`.

Therefore:

\[
\boxed{\text{04 can accept a PBL stiffness law without changing its mechanics,}}
\]

but

\[
\boxed{\text{the current 4 mm thick rib should not simply be drilled and called a valid PBL detail.}}
\]

A future PBL version requires a new geometric design of `t_r,d,d_s,p_h`, followed by replacement of the connector-source module only.

---

# 4. Global/local wave hierarchy remains the parent theory

04 does not allow shear-slip parameters to select a new global mode.

For the current BH family, retain the established R14/Multiwave-01 global mode

\[
\boxed{m=2}.
\]

Thus the one representative complete global halfwave is

\[
\boxed{L_G=\frac{a}{2}}.
\]

For the BH geometry `a=2b`:

\[
\boxed{L_G=b}.
\]

For equal-width standard cells with

\[
s=0.225b,
\]

the nominal local wave count is

\[
\boxed{n_0=\left\lfloor\frac{L_G}{s}\right\rfloor=4}.
\]

The only standard equal-width candidates are

\[
\boxed{n\in\{3,4,5\}}.
\]

The slip quantities

\[
K_t,\quad k_{\ell,r},\quad k_{\ell,f},\quad \zeta_f,\quad \chi_f
\]

are prohibited from changing `m`, `L_G`, `n_0`, or the candidate set `{3,4,5}` in 04.

---

# 5. Averaged partial-interaction subsystem

04 uses the engineering concept of an equivalent reduced composite stiffness, consistent with the steel–concrete composite-beam shear-slip framework developed from equilibrium and curvature compatibility and with the reduced-stiffness form used in Chinese steel/composite design provisions.

The standard reduced stiffness has the form

\[
\boxed{B=\frac{EI_{un}}{1+\zeta}}.
\]

For a steel face and the adjacent half of the UHPC core, define the following transformed-section quantities.

## 5.1 Geometry and transformed section

Steel-face area:

\[
\boxed{A_s=bt_s}.
\]

Adjacent half-core area:

\[
\boxed{A_c=b\frac{t_c}{2}}.
\]

Elastic modulus ratio:

\[
\boxed{n_E=\frac{E_s}{E_c}}.
\]

Steel-face own-centroid inertia:

\[
\boxed{I_s=\frac{bt_s^3}{12}}.
\]

Half-core own-centroid inertia:

\[
\boxed{I_c=\frac{b(t_c/2)^3}{12}}.
\]

Transformed own-centroid inertia:

\[
\boxed{I_0=I_s+\frac{I_c}{n_E}}.
\]

Equivalent axial area parameter:

\[
\boxed{A_0=\frac{A_cA_s}{n_EA_s+A_c}}.
\]

The physical steel-face centroid is

\[
z_f=\frac{t_c+t_s}{2}.
\]

The centroid of the adjacent half-core is

\[
z_c=\frac{t_c}{4}.
\]

Therefore the actual centroid separation used by the partial-interaction subsystem is

\[
\boxed{d_{sc}=z_f-z_c=\frac{t_c}{4}+\frac{t_s}{2}}.
\]

For `t_c=42 mm`, `t_s=4 mm`:

\[
\boxed{z_f=23\ \mathrm{mm}},
\]

\[
\boxed{z_c=10.5\ \mathrm{mm}},
\]

\[
\boxed{d_{sc}=12.5\ \mathrm{mm}}.
\]

Equivalent subsystem depth:

\[
\boxed{h=t_s+\frac{t_c}{2}}.
\]

And

\[
\boxed{A_1=\frac{I_0+A_0d_{sc}^2}{A_0}}.
\]

## 5.2 Physical transfer length

The reduced-stiffness relation uses a structural transfer length/span `l`. In 04 this is **not** the local buckling wavelength and is **not** `L_G/n`.

For the current specimen-level averaged slip calculation, use

\[
\boxed{l=a}.
\]

This keeps the connection problem at the member/composite-action level and prevents a local bulge count from creating an artificial new interface stiffness.

---

# 6. Continuous-interface substitution into the reduced-stiffness formula

The design-form reduced-stiffness expression for discrete connectors contains the combination

\[
\frac{n_sk}{p},
\]

which is the connector shear stiffness per unit longitudinal length.

In 04 this is replaced directly by the physically obtained face unit-length stiffness

\[
\boxed{\frac{n_sk}{p}\longrightarrow k_{\ell,f}}.
\]

Therefore define

\[
\boxed{\alpha_f=0.81\sqrt{\frac{k_{\ell,f}A_1}{E_sI_0}}}.
\]

The corresponding parameter

\[
\boxed{\eta_f=\frac{36E_sd_{sc}A_0}{k_{\ell,f}h\,l^2}}.
\]

Then

\[
\boxed{\zeta_f=\eta_f\left[0.4-\frac{3}{(\alpha_fl)^2}\right]}.
\]

If

\[
\zeta_f\le0,
\]

set

\[
\boxed{\zeta_f=0}.
\]

The resulting reduced transformed inertia is

\[
\boxed{I_{PI,f}=\frac{I_{FC}}{1+\zeta_f}},
\]

where

\[
\boxed{I_{FC}=I_0+A_0d_{sc}^2}.
\]

04 is an engineering averaged-partial-interaction model. The coefficients `0.81`, `36`, `0.4`, and `3` belong to the adopted reduced-stiffness formulation; they are not newly fitted to the present FEM data.

---

# 7. Conversion from reduced stiffness to an average composite-action coefficient

The own-centroid part

\[
I_0
\]

exists even when the two materials do not develop the full axial couple.

The additional full-composite axial-couple part is

\[
A_0d_{sc}^2.
\]

Define an average composite-action coefficient

\[
\boxed{\chi_f}
\]

such that

\[
\boxed{I_{PI,f}=I_0+\chi_fA_0d_{sc}^2}.
\]

Equating this with the reduced-stiffness result gives

\[
I_0+\chi_fA_0d_{sc}^2
=
\frac{I_0+A_0d_{sc}^2}{1+\zeta_f}.
\]

Therefore

\[
\boxed{
\chi_f
=
\frac{
\dfrac{I_0+A_0d_{sc}^2}{1+\zeta_f}-I_0
}{A_0d_{sc}^2}
}.
\]

Numerically enforce

\[
\boxed{0\le\chi_f\le1}.
\]

There are two face-specific values:

\[
\boxed{\chi_+\ \text{from}\ k_{\ell,+}},
\]

\[
\boxed{\chi_-\ \text{from}\ k_{\ell,-}}.
\]

No FEM peak load enters these formulas.

---

# 8. Limit checks of the 04 averaged slip module

## 8.1 Rigid-interface limit

As the physical connector/interface becomes sufficiently stiff,

\[
k_{\ell,f}\uparrow,
\]

then

\[
\zeta_f\downarrow0,
\]

and

\[
I_{PI,f}\rightarrow I_{FC}.
\]

Therefore

\[
\boxed{\chi_f\rightarrow1}.
\]

04 must then return exactly to Multiwave 01.

## 8.2 Weak-connection warning

The adopted reduced-stiffness equation was developed for composite-member stiffness reduction, not for complete debonding and frictional contact after interface failure. Therefore it is not extrapolated to represent

- interface cracking/debonding;
- traction softening;
- fracture energy;
- post-debond residual friction.

Those require a different interface-failure module if later activated.

04 covers the **pre-failure averaged slip stiffness effect only**.

---

# 9. How `chi` modifies the steel-face longitudinal strain

The UHPC field continues to use the common section generalized variables

\[
\varepsilon_x^U(z)=\varepsilon_x^0+z\kappa_x,
\]

\[
\varepsilon_y^U(z)=\varepsilon_y^0+z\kappa_y.
\]

The transverse steel-face strains remain

\[
\boxed{\varepsilon_{x,s}^{+}=\varepsilon_x^0+z_f\kappa_x},
\]

\[
\boxed{\varepsilon_{x,s}^{-}=\varepsilon_x^0-z_f\kappa_x}.
\]

For longitudinal bending, decompose the full-composite steel-face distance into

\[
z_f=z_c+d_{sc}.
\]

The adjacent half-core centroid follows the core strain at `z=±z_c`. The relative steel/core axial-couple contribution is reduced by `chi`.

Therefore TOP steel face:

\[
\boxed{
\varepsilon_{y,s}^{+}
=
\varepsilon_y^0
+
\left(z_c+\chi_+d_{sc}\right)\kappa_y
}.
\]

BOTTOM steel face:

\[
\boxed{
\varepsilon_{y,s}^{-}
=
\varepsilon_y^0
-
\left(z_c+\chi_-d_{sc}\right)\kappa_y
}.
\]

Define the effective steel-face curvature lever arms

\[
\boxed{z_{eff,+}=z_c+\chi_+d_{sc}},
\]

\[
\boxed{z_{eff,-}=z_c+\chi_-d_{sc}}.
\]

Then

\[
\varepsilon_{y,s}^{+}=\varepsilon_y^0+z_{eff,+}\kappa_y,
\]

\[
\varepsilon_{y,s}^{-}=\varepsilon_y^0-z_{eff,-}\kappa_y.
\]

If `chi=1`, `z_eff=z_f` and the no-slip strain field is recovered exactly.

---

# 10. Local-cell geometry and buckling classification

For every physical steel-shell cell, use its real width `L_x` and the already fixed representative global halfwave `L_G`.

For standard equal-width cells:

\[
L_x=s=0.225b.
\]

For candidate local wave count `n`:

\[
\boxed{L_y=\frac{L_G}{n}}.
\]

Wave numbers:

\[
\boxed{k_x=\frac{2\pi}{L_x}},
\]

\[
\boxed{k_y=\frac{2\pi}{L_y}=\frac{2n\pi}{L_G}}.
\]

The local C1-admissible mode remains

\[
\boxed{\phi(\xi,y)=(1-\cos k_x\xi)(1-\cos k_yy)}.
\]

Local initial imperfection:

\[
\boxed{A_{0\ell}=\frac{L_x}{1600}}.
\]

Current local deflection:

\[
\boxed{w_{\ell}=U\phi}.
\]

## 10.1 Elastic local-buckling gate

Let

\[
r_c=\frac{L_y}{L_x}.
\]

Use

\[
\boxed{k_{cr}=\frac{4(3r_c^4+2r_c^2+3)}{3r_c^2}}.
\]

Then

\[
\boxed{
\sigma_{cr}^E
=
\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}k_{cr}
}.
\]

If

\[
\sigma_{cr}^E\ge f_y,
\]

the cell follows the nonbuckling full-thickness ideal-EP branch.

If

\[
\sigma_{cr}^E<f_y,
\]

the cell follows R02/R06.

## 10.2 Non-standard edge cells

Edge strips are no longer automatically assigned to the E branch. Their actual `L_x` is used and the same `sigma_cr^E` gate is applied.

For the current BH layout:

- TOP standard bays occupy `3×0.225b=0.675b`; each TOP edge strip is `0.1625b`;
- BOTTOM standard bays occupy `4×0.225b=0.9b`; each BOTTOM edge strip is `0.05b`.

With `L_G=b`, their nominal counts are

\[
n_e^+=\left\lfloor\frac{b}{0.1625b}\right\rfloor=6,
\]

\[
n_e^-=\left\lfloor\frac{b}{0.05b}\right\rfloor=20.
\]

Their actual local-buckling gate still decides whether they buckle or remain ideal-EP.

---

# 11. R02 local amplitude operator, fully explicit

For a steel cell, convert the current physical face strains to compression-positive quantities

\[
e_x^c=-\varepsilon_{x,s},
\qquad
 e_y^c=-\varepsilon_{y,s}.
\]

Define

\[
\boxed{d=U^2-A_{0\ell}^2}.
\]

Exact averaged geometric coefficients:

\[
\boxed{c_x=\frac{3k_x^2}{8}},
\]

\[
\boxed{c_y=\frac{3k_y^2}{8}}.
\]

Mean membrane measures:

\[
\boxed{m_x=e_x^c-c_xd},
\]

\[
\boxed{m_y=e_y^c-c_yd}.
\]

Steel plane-stress modulus:

\[
\boxed{Q_s=\frac{E_s}{1-\nu_s^2}}.
\]

Plate bending rigidity:

\[
\boxed{D_s=\frac{E_st_s^3}{12(1-\nu_s^2)}}.
\]

Local bending coefficient:

\[
\boxed{
K_b
=
D_s
\left[
\frac34(k_x^4+k_y^4)
+
\frac12k_x^2k_y^2
\right]
}.
\]

Let

\[
r_k=\frac{k_x}{k_y}.
\]

Define

\[
\begin{aligned}
P_{16}(r_k)=&
272r_k^{16}+2856r_k^{14}+11273r_k^{12}+23146r_k^{10}\\
&+31506r_k^8+23146r_k^6+11273r_k^4+2856r_k^2+272.
\end{aligned}
\]

Then

\[
\boxed{
K_A
=
k_y^4
\frac{P_{16}(r_k)}
{256(r_k^2+1)^2(r_k^2+4)^2(4r_k^2+1)^2}
}.
\]

Define

\[
\boxed{
L_0
=
Q_s\left[
c_x(e_x^c+\nu_se_y^c)+c_y(e_y^c+\nu_se_x^c)
\right]
}.
\]

\[
\boxed{
C_g
=
Q_s(c_x^2+c_y^2+2\nu_sc_xc_y)
}.
\]

The cubic coefficients are

\[
\boxed{B_3=4t_sE_sK_A+2t_sC_g},
\]

\[
\boxed{B_1=K_b-2t_sL_0-B_3A_{0\ell}^2},
\]

\[
\boxed{B_0=-K_bA_{0\ell}}.
\]

The local amplitude equation is

\[
\boxed{B_3U^3+B_1U+B_0=0}.
\]

All nonnegative real roots are retained as candidates.

For each candidate,

\[
\boxed{
\Pi(U)
=
\frac12K_b(U-A_{0\ell})^2
+
\frac12t_sQ_s(m_x^2+m_y^2+2\nu_sm_xm_y)
+
t_sE_sK_Ad^2
}.
\]

Select

\[
\boxed{U^*=\arg\min_{U\ge0}\Pi(U)}.
\]

The R02 mean stresses are

\[
\boxed{\bar\sigma_x^{R02}=-Q_s(m_x+\nu_sm_y)},
\]

\[
\boxed{\bar\sigma_y^{R02}=-Q_s(m_y+\nu_sm_x)}.
\]

---

# 12. R06 finite-harmonic first-local-yield cap

The retained harmonic set is

\[
\mathcal H=
\{(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)\}.
\]

Coefficients:

\[
h_{01}=\frac12,
\quad
h_{02}=-\frac12,
\quad
h_{10}=\frac12,
\quad
h_{11}=-1,
\quad
h_{12}=\frac12,
\quad
h_{20}=-\frac12,
\quad
h_{21}=\frac12.
\]

For each `(p,q)`:

\[
\boxed{
A_{pq}
=
E_sd\,h_{pq}
\frac{k_x^2k_y^2}
{[(pk_x)^2+(qk_y)^2]^2}
}.
\]

Let

\[
u=\cos\theta_x,
\qquad
v=\cos\theta_y.
\]

Harmonic stresses:

\[
\boxed{
\widetilde\sigma_x
=-\sum_{(p,q)\in\mathcal H}(qk_y)^2A_{pq}
\cos(p\theta_x)\cos(q\theta_y)
},
\]

\[
\boxed{
\widetilde\sigma_y
=-\sum_{(p,q)\in\mathcal H}(pk_x)^2A_{pq}
\cos(p\theta_x)\cos(q\theta_y)
},
\]

\[
\boxed{
\widetilde\tau_{xy}
=-\sum_{(p,q)\in\mathcal H}(pk_x)(qk_y)A_{pq}
\sin(p\theta_x)\sin(q\theta_y)
}.
\]

Total stress field:

\[
\sigma_x=\bar\sigma_x^{R02}+\widetilde\sigma_x,
\]

\[
\sigma_y=\bar\sigma_y^{R02}+\widetilde\sigma_y,
\]

\[
\tau_{xy}=\widetilde\tau_{xy}.
\]

Von Mises function:

\[
\boxed{
\Phi=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2
}.
\]

If

\[
\max_{u,v\in[-1,1]}\Phi\le f_y^2,
\]

use the R02 mean stresses.

If

\[
\max\Phi>f_y^2,
\]

solve a scalar reduction factor `eta_l` such that

\[
\boxed{
\max_{u,v}\Phi(
\eta_l\varepsilon_{x,s},
\eta_l\varepsilon_{y,s}
)=f_y^2,
\qquad 0<\eta_l\le1
}.
\]

The associated R02 mean stress is then the cell average used by 04.

This operator is formally named

\[
\boxed{\text{FIRST-LOCAL-YIELD CAPPED REDUCED OPERATOR}}
\]

and is not claimed to be a complete J2 plastic-zone expansion model.

---

# 13. Face aggregation and steel-shell resultants

After classifying all standard and edge cells and evaluating each actual-width cell, obtain face-average stresses

\[
\bar\sigma_x^+,
\quad
\bar\sigma_y^+,
\quad
\bar\sigma_x^-,
\quad
\bar\sigma_y^-.
\]

The steel thickness remains the full physical thickness `t_s`. No effective width or effective area is introduced.

Steel-shell resultants:

\[
\boxed{N_x^s=t_s(\bar\sigma_x^++\bar\sigma_x^-)},
\]

\[
\boxed{N_y^s=t_s(\bar\sigma_y^++\bar\sigma_y^-)},
\]

\[
\boxed{M_x^s=t_sz_f(\bar\sigma_x^+-\bar\sigma_x^-)},
\]

\[
\boxed{M_y^s=t_sz_f(\bar\sigma_y^+-\bar\sigma_y^-)}.
\]

`z_f=23 mm` remains the correct lever arm here because these are the actual steel-face forces acting at the actual steel-face locations. The partial-interaction distance `d_sc=12.5 mm` is used only when determining how much of the steel/adjacent-core **relative axial couple** is transferred.

---

# 14. UHPC analytic thickness integration

The UHPC strain field remains

\[
\varepsilon_i^U(z)=\varepsilon_i^0+\kappa_i z,
\qquad i=x,y.
\]

For compression, let

\[
\xi=-\frac{\varepsilon}{\varepsilon_{c0}},
\]

and

\[
a_c=\frac{E_c\varepsilon_{c0}}{f_c},
\qquad
b_c=6-5a_c,
\qquad
c_c=4a_c-5.
\]

The compressive stress law is

\[
\boxed{
\sigma_c=-f_c(a_c\xi+b_c\xi^5+c_c\xi^6)
}.
\]

The corresponding first primitive is

\[
\boxed{
F_0^c
=f_c\varepsilon_{c0}
\left[
\frac{a_c}{2}\xi^2
+
\frac{b_c}{6}\xi^6
+
\frac{c_c}{7}\xi^7
\right]
}.
\]

The second primitive is

\[
\boxed{
F_1^c
=-f_c\varepsilon_{c0}^2
\left[
\frac{a_c}{3}\xi^3
+
\frac{b_c}{7}\xi^7
+
\frac{c_c}{8}\xi^8
\right]
}.
\]

The currently frozen tensile side remains the existing four-piece explicit cubic primitive and is not changed by 04.

For a direction `i`, define

\[
\varepsilon_i^+=\varepsilon_i^0+\kappa_i\frac{t_c}{2},
\]

\[
\varepsilon_i^-=\varepsilon_i^0-\kappa_i\frac{t_c}{2}.
\]

Then

\[
\boxed{
N_i^U
=(1-\rho_w)
\frac{F_0(\varepsilon_i^+)-F_0(\varepsilon_i^-)}{\kappa_i}
}.
\]

And

\[
\boxed{
M_i^U
=(1-\rho_w)
\frac{
F_1(\varepsilon_i^+)-F_1(\varepsilon_i^-)
-\varepsilon_i^0[F_0(\varepsilon_i^+)-F_0(\varepsilon_i^-)]
}{\kappa_i^2}
}.
\]

The correct continuous limit is used as `kappa_i -> 0`.

---

# 15. Longitudinal web resultants

For the longitudinal web/PBL steel area represented by `A_w`, the web strain is

\[
\boxed{\varepsilon_w(z)=\varepsilon_y^0+\kappa_yz}.
\]

Yield strain:

\[
\boxed{\varepsilon_Y=\frac{f_y}{E_s}}.
\]

Ideal elastic-perfectly-plastic stress:

\[
\boxed{
\sigma_w=
\begin{cases}
-f_y,&\varepsilon_w\le-\varepsilon_Y,\\
E_s\varepsilon_w,&|\varepsilon_w|<\varepsilon_Y,\\
+f_y,&\varepsilon_w\ge+\varepsilon_Y.
\end{cases}
}
\]

Use exact piecewise primitives over `z` to obtain

\[
\boxed{N_y^w}
\]

and

\[
\boxed{M_y^w}.
\]

04 does not modify the web material law.

---

# 16. Airy demand and outer equilibrium

The R14 outer skeleton is unchanged.

Define

\[
\boxed{Q=q(q+2q_0)}.
\]

The axial load branch remains

\[
\boxed{
P(q)=P_{cr}\frac{q}{q+q_0}+CQ
}.
\]

Demand resultants:

\[
\boxed{N_x^A=K_xQ},
\]

\[
\boxed{M_x^A=J_xq},
\]

\[
\boxed{N_y^A=-\left(\frac{P(q)}{b}-GQ\right)},
\]

\[
\boxed{M_y^A=J_yq}.
\]

Section resultants:

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

The four equilibrium equations are

\[
\boxed{R_{N_x}=N_x-N_x^A=0},
\]

\[
\boxed{R_{M_x}=M_x-M_x^A=0},
\]

\[
\boxed{R_{N_y}=N_y-N_y^A=0},
\]

\[
\boxed{R_{M_y}=M_y-M_y^A=0}.
\]

No fifth slip equilibrium equation is introduced.

---

# 17. Outer unknowns, branch and terminal condition

At each branch coordinate `q`, the outer section variables remain

\[
\boxed{
\varepsilon_x^0,
\quad
\kappa_x,
\quad
\varepsilon_y^0,
\quad
\kappa_y
}.
\]

The physical solution is the branch continuously connected to the unloaded state.

The terminal rule is unchanged from the active R14 governance:

> first admissible closed material-domain event or admissible structural `J4` fold, whichever occurs first.

04 does not use FEM peak loads to select roots, tune `K_t`, tune `k_ps`, tune `chi`, or select the terminal state.

---

# 18. Current numerical identity of the 04 shear stiffness

04 deliberately separates the **parameter identity** from the **parameter value**.

Current source parameter for the unperforated rib:

\[
\boxed{K_t=\text{steel–UHPC tangential interface stiffness per bonded area}}.
\]

Status:

```text
CURRENT_UNPERFORATED_RIB_STIFFNESS_PARAMETER = K_t [N/mm^3]
SOURCE_TYPE = steel-UHPC interface traction-separation / bond-slip
PRODUCTION_VALUE = NOT YET SOURCE-LOCKED
FEM_BACK_CALIBRATION = PROHIBITED
```

Reference sensitivity values already examined:

```text
K_t = 13 N/mm^3  : published non-mechanical steel-UHPC EA-type interface reference
K_t = 696 N/mm^3 : published non-mechanical sandblasted steel-UHPC interface reference
```

The previously used `510.987 N/mm^3` value was only an interpolation/sensitivity proxy and is **not** a source-locked 04 parameter.

A later source-matched value for the actual unperforated rib surface may replace `K_t` without changing any downstream 04 equations.

---

# 19. Replacement by perforated stiffener: exact theory interface

If the physical stiffener detail is redesigned from unperforated to PBL, only Section 3 of this theory changes.

## 19.1 Plain-rib 04

\[
K_t
\rightarrow
k_{\ell,r}^{plain}=2h_rK_t.
\]

## 19.2 PBL 04

\[
(d,d_s,E_c,f_{ck},\text{source law})
\rightarrow
k_{ps}
\rightarrow
k_{\ell,r}^{PBL}=\frac{k_{ps}}{p_h}.
\]

Then both go through the same chain:

\[
\boxed{
 k_{\ell,r}
\rightarrow
k_{\ell,f}
\rightarrow
\alpha_f,\eta_f,\zeta_f
\rightarrow
\chi_f
\rightarrow
z_{eff,f}
\rightarrow
\varepsilon_{y,s}^{\pm}
\rightarrow
R02/R06
\rightarrow
N_s,M_s
\rightarrow
R_4.
}
\]

Therefore the answer to the design-replacement question is:

\[
\boxed{\text{YES: 04 is explicitly designed so that the unperforated connector law can be replaced by a PBL law.}}
\]

But the PBL geometry must itself be designed and checked; the current 4 mm rib geometry is not automatically accepted as a PBL rib.

---

# 20. Formal prohibitions in Multiwave Steel Shell 04

04 explicitly prohibits:

1. using `K_r=75.835 kN/mm/rib` as a physical connector stiffness;
2. using `gamma=K_P/(K_P+K_eq)` as the active composite-transfer law;
3. fitting `K_t`, `k_ps`, `chi`, or any connector parameter to FEM `P_u`;
4. using connector stiffness to reselect the global mode number `m`;
5. using local bulge count `n` to define the connector stiffness;
6. introducing a slip spatial grid or connector material-point mesh into the formal theory;
7. treating the actual unperforated rib as a PBL connector without changing its geometry;
8. adding `2h_rK_t` and `k_ps/p_h` unless the source definitions are checked to avoid double counting;
9. replacing the full steel thickness with effective width or effective area;
10. changing the R14 outer equilibrium or terminal rule.

---

# 21. Execution sequence

The complete 04 calculation sequence for one specimen is:

### Step 1 — fixed parent geometry and global mode

Input

\[
b,a,t_c,t_s,h_r,N_r^+,N_r^-,A_w,
\]

retain the parent global mode `m` and compute

\[
L_G=a/m.
\]

### Step 2 — connector-source calculation

For an unperforated rib:

\[
K_t
\rightarrow
k_{\ell,r}=2h_rK_t
\rightarrow
k_{\ell,+}=N_r^+k_{\ell,r}
\rightarrow
k_{\ell,-}=N_r^-k_{\ell,r}.
\]

For a future PBL rib:

\[
k_{ps}
\rightarrow
k_{\ell,r}=k_{ps}/p_h
\rightarrow
k_{\ell,\pm}.
\]

### Step 3 — average partial-interaction coefficient

For each face calculate

\[
A_s,A_c,n_E,I_s,I_c,I_0,A_0,z_f,z_c,d_{sc},h,A_1,l,
\]

then

\[
\alpha_f,\eta_f,\zeta_f,I_{PI,f},\chi_f,z_{eff,f}.
\]

### Step 4 — outer section state at given `q`

Solve the existing four `R4` equations for

\[
\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y.
\]

### Step 5 — steel-face current strains

\[
\varepsilon_{x,s}^{\pm}=\varepsilon_x^0\pm z_f\kappa_x,
\]

\[
\varepsilon_{y,s}^{+}=\varepsilon_y^0+z_{eff,+}\kappa_y,
\]

\[
\varepsilon_{y,s}^{-}=\varepsilon_y^0-z_{eff,-}\kappa_y.
\]

### Step 6 — actual cell classification

Use actual cell width and the fixed `L_G` to compute `sigma_cr^E`. Standard equal-width cells use `{n0-1,n0,n0+1}`; edge cells use their actual width and their own buckling gate.

### Step 7 — local R02/R06

For each local-first cell:

\[
\varepsilon_s
\rightarrow
B_3U^3+B_1U+B_0=0
\rightarrow
U^*
\rightarrow
\bar\sigma^{R02}
\rightarrow
R06
\rightarrow
\bar\sigma^{cell}.
\]

### Step 8 — face aggregation and steel resultants

Actual-width averaging gives

\[
\bar\sigma^{+},\bar\sigma^{-}
\rightarrow
N_s,M_s.
\]

### Step 9 — UHPC and web analytic resultants

Use the unchanged exact thickness primitives to obtain

\[
N_U,M_U,N_w,M_w.
\]

### Step 10 — outer equilibrium and connected branch

Assemble

\[
R_4=0
\]

and continue from the unloaded branch until the first admissible terminal event.

---

# 22. Current theory status

The current formal status is

```text
MODEL = MULTIWAVE STEEL SHELL 04
GLOBAL_MODE = inherited/frozen from R14 parent mechanics
GLOBAL_REPRESENTATIVE_DOMAIN = one complete global halfwave
LOCAL_STANDARD_WAVE_COUNTS = n0-1, n0, n0+1
SLIP_TREATMENT = averaged partial interaction
CURRENT_CONNECTOR_TYPE = unperforated longitudinal rib
CURRENT_CONNECTOR_PARAMETER = K_t [N/mm^3]
CURRENT_PARAMETER_VALUE = not source-locked
PLAIN-RIB MAP = k_l,r = 2 h_r K_t
PBL-REPLACEMENT MAP = k_l,r = k_ps / p_h
OLD_Kr_75.835 = DELETED AS PHYSICAL STIFFNESS
OLD_DIRECT_GAMMA = DELETED
FEM_BACK_CALIBRATION = PROHIBITED
PRODUCTION_R14 = UNCHANGED
STATUS = DIAGNOSTIC THEORY / THEORY-DEVELOPMENT
```

---

# 23. References and source identity

1. Nie, J.G.; Cai, C.S. (2003). *Steel–Concrete Composite Beams Considering Shear Slip Effects*. Journal of Structural Engineering, 129(4), 495–506. DOI: 10.1061/(ASCE)0733-9445(2003)129:4(495). Used to support the equivalent-rigidity / averaged-slip modeling level.
2. Chinese steel/composite design reduced-stiffness provisions: `B = EI_un/(1+zeta)` and the associated `zeta, eta, alpha, A0, A1, I0` equations. Used as the explicit engineering average-partial-interaction closure in 04.
3. *Constitutive Behavior of the Interface between UHPC and Steel Plate without Shear Connector: From Experimental to Numerical Study* (2024), CMES 140(2), 1863–1888. Used only to identify the traction–separation stiffness parameter `K_t` and published sensitivity reference values for non-mechanical steel–UHPC interfaces.
4. User-supplied design formula for PBL connection shear stiffness: `k_ps=23.4 sqrt((d-d_s)d_s E_c f_ck)`. Used as an allowed future PBL connector-source option, not as the current unperforated-rib law.
5. Uploaded `钢-预制UHPC开孔板组合桥面板界面抗剪性能研究_胡文旭.pdf`: used as supporting evidence that connector shear stiffness can be defined by load-slip secant methods or design formulas and that PBL/stud connector stiffness has a different physical identity from an unperforated interface stiffness.
6. Uploaded `PBL加劲型薄壁钢管混凝土...塔的计算理论与设计方法研究_孙立鹏.pdf`: used for the PBL geometric-design caution, including perforated-rib thickness and hole-spacing recommendations.

---

# 24. Final governing statement

Multiwave Steel Shell 04 does **not** assume that shear slip has the same wavelength as local shell buckling, and it does **not** allow shear slip to create a new global buckling mode. It treats slip in the same engineering hierarchy as composite-member reduced stiffness: connector/interface mechanics are first homogenized into a face-level average composite-action coefficient, and that coefficient changes only the steel/core longitudinal axial-couple transfer before the existing local shell and section-equilibrium calculations are performed.

The definitive 04 chain is therefore

\[
\boxed{
\text{connector/interface source}
\rightarrow
k_{\ell,r}
\rightarrow
k_{\ell,f}
\rightarrow
\chi_f
\rightarrow
\varepsilon_{y,s}^{\pm}
\rightarrow
\text{Multiwave R02/R06}
\rightarrow
N_s,M_s
\rightarrow
R_4.
}
\]

This architecture is deliberately connector-modular: the present unperforated rib uses `K_t`, while a future perforated/PBL rib can replace only the first source block with `k_ps/p_h` without rebuilding the steel-shell, UHPC, web, or R4 theory.