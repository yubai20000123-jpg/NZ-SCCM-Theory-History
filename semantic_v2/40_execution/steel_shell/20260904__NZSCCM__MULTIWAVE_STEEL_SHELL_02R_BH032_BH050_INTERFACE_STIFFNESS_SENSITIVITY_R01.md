# NZ-SCCM Multiwave Steel Shell 02R — BH032/BH050 averaged-slip sensitivity R01

**Date:** 2026-09-04  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `DIAGNOSTIC EXECUTION / NOT PRODUCTION R14`  
**Theory:** `20260904__NZSCCM__MULTIWAVE_STEEL_SHELL_02R_NIE_AVERAGED_SLIP_UNPERFORATED_RIB_FULL_DERIVATION_R01.md`

---

## 1. Execution contract

- frozen R14/global backbone;
- BH global mode remains \(m=2\);
- one complete global halfwave \(L_G=a/2=b\);
- standard local wave counts remain 3/4/5;
- balanced standard-bay pattern: TOP 1/1/1, BOTTOM 1/2/1;
- TOP and BOTTOM edge bays are checked with their own widths instead of being forced to ideal-EP;
- R02 cubic root selected by minimum local potential;
- R06 finite seven-harmonic first-local-yield cap retained;
- UHPC and web analytic thickness operators unchanged;
- no FEM load used in solving or interface-parameter selection.

---

## 2. Interface reference values

Current rib height:

\[
h_r=37\ \mathrm{mm}.
\]

Per rib:

\[
k_{\ell,r}=2h_rK_t=74K_t\ \mathrm{N/mm^2}.
\]

BH TOP/BOTTOM:

\[
k_{\ell,+}=4(74K_t)=296K_t,
\]

\[
k_{\ell,-}=5(74K_t)=370K_t.
\]

Three diagnostic values were evaluated:

\[
K_t=13\ \mathrm{N/mm^3}
\]

(soft published connector-free interface reference),

\[
K_t=510.987\ \mathrm{N/mm^3}
\]

(exploratory smooth-strength-scaled proxy), and

\[
K_t=696\ \mathrm{N/mm^3}
\]

(stiff published sandblasted connector-free interface reference).

The no-slip limit was also recalculated after the edge-bay correction.

---

# 3. BH032 averaged interaction factors

Geometry used for each face/half-core reduction subsystem:

\[
b=1600\ \mathrm{mm},\quad a=3200\ \mathrm{mm},
\]

\[
A_s=bt_s=6400\ \mathrm{mm^2},
\]

\[
A_c=b(t_c/2)=33600\ \mathrm{mm^2},
\]

\[
n_E=E_s/E_c=4.74654378,
\]

\[
I_s=8533.3333\ \mathrm{mm^4},
\]

\[
I_c=1234800\ \mathrm{mm^4},
\]

\[
I_0=268680.5178\ \mathrm{mm^4},
\]

\[
A_0=3361.16169\ \mathrm{mm^2},
\]

\[
A_1=236.186802\ \mathrm{mm^2}.
\]

For \(K_t=13\):

TOP

\[
k_{\ell,+}=3848\ \mathrm{N/mm^2},
\]

\[
\alpha l=10.5034,
\quad
\zeta_+=0.117917,
\quad
\boxed{\chi_+=0.840558}.
\]

BOTTOM

\[
k_{\ell,-}=4810\ \mathrm{N/mm^2},
\]

\[
\alpha l=11.7431,
\quad
\zeta_-=0.0957101,
\quad
\boxed{\chi_-=0.867962}.
\]

For \(K_t=510.987\):

\[
\boxed{\chi_+=0.995159},
\qquad
\boxed{\chi_-=0.996123}.
\]

For \(K_t=696\):

\[
\boxed{\chi_+=0.996441},
\qquad
\boxed{\chi_-=0.997151}.
\]

---

# 4. BH050 averaged interaction factors

\[
b=2500\ \mathrm{mm},\quad a=5000\ \mathrm{mm},
\]

\[
A_s=10000\ \mathrm{mm^2},
\]

\[
A_c=52500\ \mathrm{mm^2},
\]

\[
I_s=13333.3333\ \mathrm{mm^4},
\]

\[
I_c=1929375\ \mathrm{mm^4},
\]

\[
I_0=419813.3091\ \mathrm{mm^4},
\]

\[
A_0=5251.81514\ \mathrm{mm^2},
\]

\[
A_1=236.186802\ \mathrm{mm^2}.
\]

For \(K_t=13\):

\[
\boxed{\chi_+=0.891344},
\qquad
\boxed{\chi_-=0.911052}.
\]

For \(K_t=510.987\):

\[
\boxed{\chi_+=0.996896},
\qquad
\boxed{\chi_-=0.997515}.
\]

For \(K_t=696\):

\[
\boxed{\chi_+=0.997719},
\qquad
\boxed{\chi_-=0.998174}.
\]

---

# 5. Edge-bay correction

BH TOP edge bay width:

\[
b_e^+=0.1625b,
\quad n_e^+=6.
\]

BH BOTTOM edge bay width:

\[
b_e^-=0.05b,
\quad n_e^-=20.
\]

For BH032 TOP edge:

\[
\sigma_{cr,e}\approx470.5\ \mathrm{MPa}>355\ \mathrm{MPa},
\]

so it remains yield-first.

For BH050 TOP edge:

\[
\sigma_{cr,e}\approx192.7\ \mathrm{MPa}<355\ \mathrm{MPa},
\]

so it is local-first and is evaluated through R02/R06.

After this correction, the no-slip values are:

\[
P_{u,NS}^{BH032}=11.32879036\ \mathrm{MN},
\]

\[
P_{u,NS}^{BH050}=13.85771124\ \mathrm{MN}.
\]

The BH050 change relative to the previous 01 value 13.85846 MN is only about 0.005%, so the edge-bay correction is required for self-consistency but is not the principal source of the BH050 capacity gap.

---

# 6. BH032/BH050 Pu sensitivity

Latest FEM comparison values used only after the roots were obtained:

\[
P_{FEM}^{BH032}=10.884984\ \mathrm{MN},
\]

\[
P_{FEM}^{BH050}=12.572657\ \mathrm{MN}.
\]

| Model / interface stiffness | BH032 Pu (MN) | BH032 vs FEM | BH050 Pu (MN) | BH050 vs FEM |
|---|---:|---:|---:|---:|
| old Multiwave 02, deprecated \(K_r=75.835\) | 10.951649 | +0.61% | 13.154412 | +4.63% |
| 02R, \(K_t=13\) | 11.275384 | +3.59% | 13.801852 | +9.78% |
| 02R, \(K_t=510.987\) proxy | 11.327222 | +4.06% | 13.856152 | +10.21% |
| 02R, \(K_t=696\) | 11.327638 | +4.07% | 13.856566 | +10.21% |
| 02R no-slip limit | 11.328790 | +4.08% | 13.857711 | +10.22% |

Relative to the no-slip limit:

BH032:

\[
K_t=13:\ -0.471\%,
\]

\[
K_t=510.987:\ -0.0138\%,
\]

\[
K_t=696:\ -0.0102\%.
\]

BH050:

\[
K_t=13:\ -0.403\%,
\]

\[
K_t=510.987:\ -0.0113\%,
\]

\[
K_t=696:\ -0.0083\%.
\]

Thus even the very soft published connector-free reference changes the current capacity by less than about 0.5% in these two specimens; the stiffer published/reference interfaces are practically indistinguishable from the no-slip result.

---

# 7. Detailed solved states for the exploratory proxy

For \(K_t=510.987\ \mathrm{N/mm^3}\):

BH032:

\[
\boxed{P_u=11.32722195\ \mathrm{MN}}
\]

\[
[\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y,q]
=
[1.45412282\times10^{-4},
1.99871137\times10^{-5},
-2.49584565\times10^{-3},
4.78168738\times10^{-5},
1.45560667\times10^{-3}].
\]

BH050:

\[
\boxed{P_u=13.85615189\ \mathrm{MN}}
\]

\[
[\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y,q]
=
[1.92370281\times10^{-5},
4.48581780\times10^{-5},
-2.12992966\times10^{-3},
6.52414446\times10^{-5},
5.25774443\times10^{-3}].
\]

The nonlinear five-equation material-boundary solves converged to scaled residual norms on the order of \(10^{-14}\) in the independent execution.

---

# 8. Interpretation

The large capacity reductions previously produced by old Multiwave 02 are **not reproduced** when the slip correction is based on an averaged reduced-rigidity framework and connector-free steel-UHPC interface stiffness scales.

Therefore the old 02 agreement with FEM cannot be used as evidence that

\[
\gamma=\frac{K_P}{K_P+K_{eq}}
\]

was physically correct. The improved agreement was at least partly caused by an artificially soft stiffness source and its concentrated-spring embedding.

The 02R result indicates that, for the current unperforated-rib problem, **initial elastic interface stiffness alone is unlikely to explain the BH050/BH060/BH070 capacity deficit**. If interface behavior is later found to matter strongly near ultimate load, the next interface quantities requiring physical investigation are bond strength, debonding/fracture energy, and post-bond friction rather than further tuning of initial \(K_t\).

This conclusion is diagnostic; no production R14 change is made.
