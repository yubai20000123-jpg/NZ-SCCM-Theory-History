# NZ-SCCM 多波钢壳02R——聂/规范式平均滑移、无孔纵向加劲肋版本 R01

**Date:** 2026-09-04  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `DIAGNOSTIC THEORY / NOT PRODUCTION R14`  
**Parent 1:** `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_01_NO_SHEAR_SLIP_FULL_DERIVATION_R01.md`  
**Parent 2:** `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_02_FIXED_RIB_SLIP_STIFFNESS_R01.md`

---

## 0. Decision

This revision keeps the useful hierarchy of Multiwave 02 but deletes two unsupported ingredients of 02-R01:

1. delete the diagnostic rib stiffness
   \[
   K_r=75.835\ \mathrm{kN/mm/rib}
   \]
   derived from the pure-shear yield force of a 4 mm × 37 mm steel rib;
2. delete the concentrated-spring transfer rule
   \[
   \gamma=\frac{K_P}{K_P+K_{eq}}.
   \]

The replacement is an **averaged partial-interaction correction** based on the reduced-rigidity framework used in Chinese steel-concrete composite-beam theory and the Nie/Cai line of work. The slip correction is not tied to the local shell wave count and does not re-select the global shell mode.

Locked hierarchy:

\[
\boxed{\text{R14 global stability backbone}\to m=2\to L_G=a/2}
\]

then, independently,

\[
\boxed{L_G/s\to n_0\to n_0-1,n_0,n_0+1\to R02/R06}
\]

and

\[
\boxed{\text{unperforated steel-UHPC interface}\to K_t\to k_{\ell,f}\to \chi_f}
\]

with the two modules merging only at the steel-face section stress/resultant level.

No FEM load is used to identify \(K_t\) or \(\chi_f\).

---

# 1. Why 02-R01 stiffness is deleted

The old 02 diagnostic quantity

\[
K_r=\frac{0.5(t_rh_rf_y/\sqrt3)}{0.2\ \mathrm{mm}}
\]

uses the **pure shear-yield capacity of the steel rib plate** to construct a **steel-UHPC load-slip stiffness**. These are different physical objects. It remains useful historically as a sensitivity parameter, but it has no acceptable source identity as an interface stiffness and is removed from 02R.

Current specimen geometry is an **unperforated longitudinal rib**, not a PBL connector. Therefore PBL formulas involving hole diameter and transverse rebar are not used in 02R.

---

# 2. Source framework: averaged slip/reduced rigidity

For a conventional steel-concrete composite beam, the reduced-rigidity form is

\[
B=\frac{E_sI_{FC}}{1+\zeta},
\]

where \(\zeta\) is the slip-induced rigidity reduction coefficient.

The engineering formula family can be written as

\[
\boxed{
\zeta=\max\left\{0,\eta\left[0.4-\frac{3}{(\alpha l)^2}\right]\right\}
}
\]

\[
\boxed{
\eta=\frac{36E_sd_{sc}pA_0}{n_skhl^2}
}
\]

\[
\boxed{
\alpha=0.81\sqrt{\frac{n_skA_1}{E_sI_0p}}
}
\]

\[
\boxed{
A_0=\frac{A_cA_s}{n_EA_s+A_c}
}
\]

\[
\boxed{
A_1=\frac{I_0+A_0d_{sc}^2}{A_0}
}
\]

\[
\boxed{
I_0=I_s+\frac{I_c}{n_E}
}
\]

with

\[
n_E=\frac{E_s}{E_c}.
\]

The combination \(n_sk/p\) is the unit-length shear stiffness of the connection. Therefore, for a continuous interface, define directly

\[
\boxed{k_{\ell}=\frac{n_sk}{p}}
\qquad [k_{\ell}]=\mathrm{N/mm^2}.
\]

The formulas become

\[
\boxed{
\eta=\frac{36E_sd_{sc}A_0}{k_{\ell}hl^2}
}
\]

and

\[
\boxed{
\alpha=0.81\sqrt{\frac{k_{\ell}A_1}{E_sI_0}}
}.
\]

This is the form used below.

---

# 3. Mapping the current unperforated rib to unit-length interface stiffness

Let the local tangential traction-slip law of a steel-UHPC bonded surface in the initial branch be

\[
\boxed{\tau=K_t\delta}
\]

with

\[
[K_t]=\mathrm{N/mm^3}.
\]

Current longitudinal rib net height:

\[
h_r=37\ \mathrm{mm}.
\]

Only the two rib side surfaces are counted in 02R-R01. The direct steel-face/UHPC natural-bond area is deliberately omitted until its actual interface treatment is source-locked.

For 1 mm longitudinal length of one rib, the two bonded side surfaces have area

\[
dA=2h_r\,dy.
\]

Therefore

\[
dV=\tau\,dA=(K_t\delta)(2h_rdy).
\]

Hence the shear flow is

\[
q=\frac{dV}{dy}=2h_rK_t\delta.
\]

Thus one rib has unit-length slip stiffness

\[
\boxed{k_{\ell,r}=2h_rK_t}.
\]

For a face with \(N_r^f\) longitudinal ribs,

\[
\boxed{k_{\ell,f}=N_r^f(2h_rK_t)}.
\]

For the current BH layout:

\[
N_r^+=4,
\qquad
N_r^-=5.
\]

Therefore

\[
\boxed{k_{\ell,+}=8h_rK_t}
\]

and

\[
\boxed{k_{\ell,-}=10h_rK_t}.
\]

This interface stiffness depends on the connector/interface construction, not on \(m\), \(n\), \(L_G\), or the local bulge direction.

---

# 4. Two reduced-rigidity subsystems used only to identify average composite action

The TOP face is paired with the adjacent upper half-core; the BOTTOM face is paired with the adjacent lower half-core. This is a reduced-order identification device, not a statement that the UHPC core is physically cut into independent layers.

For either face:

Steel-face area:

\[
\boxed{A_s=bt_s}.
\]

Adjacent UHPC half-core area:

\[
\boxed{A_c=b\frac{t_c}{2}}.
\]

Steel-face own inertia:

\[
\boxed{I_s=\frac{bt_s^3}{12}}.
\]

Half-core own inertia:

\[
\boxed{I_c=\frac{b(t_c/2)^3}{12}}.
\]

UHPC-half centroid:

\[
\boxed{z_c=\frac{t_c}{4}}.
\]

Steel-face centroid:

\[
\boxed{z_f=\frac{t_c+t_s}{2}}.
\]

Face-to-adjacent-half-core centroid distance:

\[
\boxed{d_{sc}=z_f-z_c=\frac{t_c}{4}+\frac{t_s}{2}}.
\]

Subsystem height:

\[
\boxed{h=t_s+\frac{t_c}{2}}.
\]

The physical transfer length used by the averaged-slip model is the specimen/member length

\[
\boxed{l=a}.
\]

It is deliberately **not** \(L_G=a/m\) and not \(L_G/n\), because 02R does not make interface composite action a function of shell buckling wavelength.

With current dimensions

\[
t_c=42\ \mathrm{mm},\qquad t_s=4\ \mathrm{mm},
\]

so

\[
\boxed{z_c=10.5\ \mathrm{mm}}
\]

\[
\boxed{z_f=23.0\ \mathrm{mm}}
\]

\[
\boxed{d_{sc}=12.5\ \mathrm{mm}}
\]

\[
\boxed{h=25.0\ \mathrm{mm}}.
\]

This removes the old 02 inconsistency in which half-core axial stiffness was used together with the full 23 mm core-midplane lever arm.

---

# 5. Derivation of a lever-arm composite-action fraction

The full-interaction transformed inertia of one face/half-core subsystem is

\[
\boxed{I_{FC}=I_0+A_0d_{sc}^2}.
\]

The reduced-rigidity formula gives

\[
\boxed{I_{PI}=\frac{I_{FC}}{1+\zeta}}.
\]

Slip should release the **relative axial-force-couple contribution** while the two components' own bending inertias remain. Define \(\chi_f\) through

\[
\boxed{I_{PI}=I_0+\chi_fA_0d_{sc}^2}.
\]

Equating the two expressions gives

\[
I_0+\chi_fA_0d_{sc}^2
=
\frac{I_0+A_0d_{sc}^2}{1+\zeta_f}.
\]

Therefore

\[
\boxed{
\chi_f=
\frac{
\dfrac{I_0+A_0d_{sc}^2}{1+\zeta_f}-I_0
}{A_0d_{sc}^2}
}.
\]

For execution it is constrained to

\[
\boxed{0\le\chi_f\le1}.
\]

Interpretation:

- \(\chi_f=1\): full average composite action;
- \(\chi_f=0\): no face-to-half-core axial-force-couple contribution in this reduced operator;
- intermediate values: the average relative curvature strain transferred by the connection.

This \(\chi_f\) is a derived adaptation of the reduced-rigidity method to the present face/core section operator. It is not claimed to be an equation printed directly in the cited beam design standard.

---

# 6. Averaged steel-face longitudinal strain mapping

The adjacent half-core centroid strains under the frozen R14 section variables are

TOP:

\[
\boxed{\varepsilon_{y,c}^{+}=\varepsilon_y^0+z_c\kappa_y}
\]

BOTTOM:

\[
\boxed{\varepsilon_{y,c}^{-}=\varepsilon_y^0-z_c\kappa_y}.
\]

Under full interaction, the additional face-to-half-core strain difference is

\[
\pm d_{sc}\kappa_y.
\]

Under 02R, only fraction \(\chi_f\) of this relative strain is transferred. Hence

\[
\boxed{
\varepsilon_{y,s}^{+}
=
\varepsilon_y^0+
\left(z_c+\chi_+d_{sc}\right)\kappa_y
}
\]

and

\[
\boxed{
\varepsilon_{y,s}^{-}
=
\varepsilon_y^0-
\left(z_c+\chi_-d_{sc}\right)\kappa_y
}.
\]

The transverse face strains remain

\[
\boxed{\varepsilon_{x,s}^{+}=\varepsilon_x^0+z_f\kappa_x}
\]

\[
\boxed{\varepsilon_{x,s}^{-}=\varepsilon_x^0-z_f\kappa_x}.
\]

No-slip check:

\[
\chi_+=\chi_-=1
\]

gives

\[
z_c+d_{sc}=z_f,
\]

therefore

\[
\varepsilon_{y,s}^{\pm}
=
\varepsilon_y^0\pm z_f\kappa_y,
\]

which is exactly Multiwave 01.

The UHPC and web fields remain the frozen R14/01 fields

\[
\varepsilon_y^U(z)=\varepsilon_y^0+z\kappa_y,
\]

\[
\varepsilon_y^w(z)=\varepsilon_y^0+z\kappa_y.
\]

Thus 02R is explicitly an **average section force-sharing correction on the frozen R14 backbone**, not a new distributed slip-field theory.

---

# 7. Global stability and local shell wavelength remain independent of the slip coefficient

The R14 global mode is not re-solved by 02R.

For the current BH family:

\[
\boxed{m=2}
\]

and therefore

\[
\boxed{L_G=a/2=b}.
\]

Standard same-side rib spacing:

\[
\boxed{s=0.225b}.
\]

Therefore

\[
\boxed{n_0=\left\lfloor\frac{L_G}{s}\right\rfloor=4}
\]

and the standard equal-width buckling candidates remain

\[
\boxed{n=3,4,5}.
\]

None of \(K_t,k_{\ell,f},\zeta_f,\chi_f\) appears in this wave-count rule.

---

# 8. Edge bays are checked by the same local buckling gate

The previous execution specialization treated all non-standard edge strips as ideal-EP steel. 02R removes that shortcut.

TOP has three standard 0.225b bays, leaving

\[
b-3(0.225b)=0.325b.
\]

The two TOP edge bays each have

\[
\boxed{b_e^+=0.1625b}.
\]

With \(L_G=b\), their own baseline longitudinal wave count is

\[
\boxed{n_e^+=\left\lfloor\frac{b}{0.1625b}\right\rfloor=6}.
\]

BOTTOM has four standard 0.225b bays, leaving 0.1b, so each BOTTOM edge bay has

\[
\boxed{b_e^-=0.05b}
\]

and

\[
\boxed{n_e^-=20}.
\]

Every standard or edge bay is checked with

\[
\sigma_{cr}^{E}
=
\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}
\frac{4(3r_c^4+2r_c^2+3)}{3r_c^2},
\qquad
r_c=\frac{L_y}{L_x}.
\]

If

\[
\sigma_{cr}^{E}\ge f_y,
\]

use the full-thickness ideal-EP branch.

If

\[
\sigma_{cr}^{E}<f_y,
\]

use the unchanged R02/R06 local operator.

For BH032 TOP edge, the check gives approximately

\[
\sigma_{cr,e}\approx470.5\ \mathrm{MPa}>355\ \mathrm{MPa},
\]

so it remains yield-first.

For BH050 TOP edge,

\[
\sigma_{cr,e}\approx192.7\ \mathrm{MPa}<355\ \mathrm{MPa},
\]

so the TOP edge bays are local-first in 02R.

---

# 9. R02/R06, UHPC, web and R4 are otherwise unchanged

For each local-first cell, 02R retains the finite R02 cubic equation

\[
\boxed{B_3U^3+B_1U+B_0=0}
\]

with all non-negative real roots evaluated by the same local potential and the minimum-energy root retained.

The finite seven-harmonic R06 field is unchanged. Its present identity is a **first-local-yield capped reduced operator**; 02R does not claim it is a full distributed J2 plastic-zone return.

Steel-face average stresses are aggregated over the real standard and edge widths, then

\[
\boxed{N_x^s=t_s(\bar\sigma_x^++\bar\sigma_x^-)}
\]

\[
\boxed{M_x^s=t_sz_f(\bar\sigma_x^+-\bar\sigma_x^-)}
\]

\[
\boxed{N_y^s=t_s(\bar\sigma_y^++\bar\sigma_y^-)}
\]

\[
\boxed{M_y^s=t_sz_f(\bar\sigma_y^+-\bar\sigma_y^-)}.
\]

UHPC and web resultants remain the existing analytic-thickness operators.

The outer Airy/R14 demand remains frozen:

\[
Q=q(q+2q_0)
\]

\[
P(q)=P_{cr}\frac{q}{q+q_0}+CQ
\]

and

\[
R_{N_x}=R_{M_x}=R_{N_y}=R_{M_y}=0.
\]

No new outer slip unknown is introduced.

---

# 10. Interface stiffness values used only for diagnostic execution

There is not yet a source-locked tangential stiffness for the exact current 4 mm unperforated, untreated longitudinal rib/UHPC interface.

02R therefore keeps \(K_t\) parameterized and uses published connector-free steel-UHPC interface values only as diagnostic references:

1. **soft connector-free reference:**
   \[
   K_t=13\ \mathrm{N/mm^3}
   \]
   from an epoxy/aggregate interface constitutive identification;
2. **stiff connector-free reference:**
   \[
   K_t=696\ \mathrm{N/mm^3}
   \]
   from a sandblasted steel-UHPC interface constitutive identification;
3. **exploratory smooth-interface proxy only:**
   smooth constrained shear strength \(0.58\) MPa and sandblasted shear strength \(0.79\) MPa give
   \[
   K_t^{proxy}=696\frac{0.58}{0.79}=510.99\ \mathrm{N/mm^3}.
   \]
   This assumes similar characteristic initial slip and is **not** a published smooth-interface stiffness law.

The proxy is used only to test sensitivity, not as a frozen production parameter.

---

# 11. Theoretical status

```text
MULTIWAVE_02R_STATUS = DIAGNOSTIC / THEORY-DEVELOPMENT
GLOBAL_MODE_RESELECTION_BY_SLIP = PROHIBITED
GLOBAL_R14_BACKBONE = FROZEN
LOCAL_STANDARD_WAVE_COUNTS_BH = 3/4/5
INTERFACE_TYPE = UNPERFORATED_RIB / NO PBL HOLE MODEL
OLD_75.835_KN_PER_MM_RIB_STIFFNESS = DEPRECATED
OLD_GAMMA_KP_OVER_KP_PLUS_KEQ = DEPRECATED
FEM_BACK_CALIBRATION = NO
```

The central diagnostic question for 02R is no longer whether a deliberately soft \(K_r\) can improve FEM agreement. It is whether a source-plausible average interface stiffness produces enough reduction in steel-face/core composite action to materially change the section resultants.
