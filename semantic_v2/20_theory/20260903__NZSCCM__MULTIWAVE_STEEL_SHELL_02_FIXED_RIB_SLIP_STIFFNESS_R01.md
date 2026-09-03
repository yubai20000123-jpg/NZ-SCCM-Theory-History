# NZ-SCCM 多波钢壳02——考虑固定单加劲肋剪切滑移刚度版本 R01

**Date:** 2026-09-03  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `DIAGNOSTIC THEORY / NOT PRODUCTION R14`  
**Parent:** `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_01_NO_SHEAR_SLIP_FULL_DERIVATION_R01.md`

---

## 0. Scope and locked boundaries

This file archives the user-visible Multiwave Steel Shell 02 formulation already executed in chat. It is an additive diagnostic extension of Multiwave Steel Shell 01.

Retained from 01:

- one complete global halfwave only;
- cell classes `E`, `n0-1`, `n0`, `n0+1`;
- `n0=floor(L_G/s)`;
- R02/R06 steel-cell operator;
- full physical steel thickness; no effective width or effective area;
- unchanged UHPC material primitives;
- unchanged web law;
- unchanged global Airy `P(q), N^A, M^A` skeleton;
- no 99 independent local amplitudes;
- no FEM load fitting.

New in 02 only:

- a fixed equivalent shear-slip stiffness is assigned to each longitudinal PBL/rib;
- this finite connection stiffness reduces the steel-face longitudinal curvature-induced strain relative to the fully bonded 01 limit.

This version is deliberately simple. It is **not** a full continuous partial-interaction field theory and does not yet solve a distributed interface-slip differential equation.

---

# 1. Fixed single-rib diagnostic shear stiffness

Current thin longitudinal rib net section:

\[
t_r=4\ \mathrm{mm},\qquad h_r=37\ \mathrm{mm},
\]

so

\[
A_r=t_rh_r=148\ \mathrm{mm^2}.
\]

With steel yield stress

\[
f_y=355\ \mathrm{MPa},
\]

the shear-yield estimate is

\[
\tau_y=\frac{f_y}{\sqrt3}=204.96\ \mathrm{MPa},
\]

and the corresponding rib shear force is

\[
V_r=A_r\tau_y=30.334\ \mathrm{kN}.
\]

Using the diagnostic initial stiffness convention

\[
K_r=\frac{0.5V_r}{0.2\ \mathrm{mm}},
\]

gives

\[
\boxed{K_r=75.835\ \mathrm{kN/mm/rib}}.
\]

Identity of this number:

```text
FIXED_RIB_SLIP_STIFFNESS = 75.835 kN/mm/rib
STATUS = engineering diagnostic estimate
FEM_BACK_CALIBRATION = NO
PRODUCTION_MATERIAL_PARAMETER = NO
```

It is an order-of-magnitude engineering estimate for the current 4 mm × 37 mm thin rib, not a source-locked measured stiffness for BH032/BH050.

---

# 2. Axial stiffnesses over one complete global halfwave

Let the representative global halfwave length be

\[
L_G=\frac{a}{m^*}.
\]

Steel-face axial stiffness over this halfwave is approximated by

\[
\boxed{K_s=\frac{E_sbt_s}{L_G}}.
\]

Assign one-half of the UHPC core to each face for the present two-face slip reduction:

\[
\boxed{K_c=\frac{E_cb(t_c/2)}{L_G}}.
\]

The relative axial stiffness is

\[
\boxed{K_{eq}=\frac{K_sK_c}{K_s+K_c}}.
\]

For a face with `N_r` active longitudinal ribs,

\[
\boxed{K_P=N_rK_r}.
\]

Define the dimensionless composite-transfer factor

\[
\boxed{\gamma=\frac{K_P}{K_P+K_{eq}}}.
\]

It satisfies

\[
K_r\rightarrow\infty\Rightarrow\gamma\rightarrow1,
\]

so Multiwave 02 degenerates exactly to Multiwave 01 in the rigid-interface limit, while

\[
K_r\rightarrow0\Rightarrow\gamma\rightarrow0.
\]

---

# 3. Only the steel longitudinal face strain is modified

The common UHPC section field remains

\[
\varepsilon_x^U(z)=\varepsilon_x^0+\kappa_xz,
\qquad
\varepsilon_y^U(z)=\varepsilon_y^0+\kappa_yz.
\]

The steel transverse face strains remain the no-slip 01 values:

\[
\boxed{e_{x,s}^{+}=\varepsilon_x^0+z_f\kappa_x},
\]

\[
\boxed{e_{x,s}^{-}=\varepsilon_x^0-z_f\kappa_x}.
\]

Only the longitudinal curvature-induced steel-face strain is reduced:

\[
\boxed{e_{y,s}^{+}=\varepsilon_y^0+\gamma_+z_f\kappa_y},
\]

\[
\boxed{e_{y,s}^{-}=\varepsilon_y^0-\gamma_-z_f\kappa_y}.
\]

The mean axial strain `eps_y0` remains common. The present 02 model therefore represents finite shear transfer only through the face separation contribution to longitudinal bending/curvature compatibility.

---

# 4. Multiwave cell mechanics are unchanged

For each face:

\[
n_0=\left\lfloor\frac{L_G}{s}\right\rfloor,
\]

and equal-width buckling cells use only

\[
n\in\{n_0-1,n_0,n_0+1\}.
\]

Nonbuckling cells use the full-thickness ideal elastic-perfectly-plastic steel branch.

For a buckling cell the same 01 R02/R06 chain is retained:

\[
n\to L_y=L_G/n\to k_y\to c_y,K_b,K_A\to R_U=0\to U^*\to\bar\sigma_x,\bar\sigma_y\to R06.
\]

No qU term, new local shape function, or new local material law is added in 02.

---

# 5. Face aggregation and steel-shell section resultants

After classifying the cells on each face exactly as in Multiwave 01, obtain the face-average stresses

\[
\bar\sigma_x^+,\ \bar\sigma_y^+,\ \bar\sigma_x^-,\ \bar\sigma_y^-.
\]

Then

\[
\boxed{N_x^s=t_s(\bar\sigma_x^++\bar\sigma_x^-)},
\]

\[
\boxed{M_x^s=t_sz_f(\bar\sigma_x^+-\bar\sigma_x^-)},
\]

\[
\boxed{N_y^s=t_s(\bar\sigma_y^++\bar\sigma_y^-)},
\]

\[
\boxed{M_y^s=t_sz_f(\bar\sigma_y^+-\bar\sigma_y^-)}.
\]

UHPC and web resultants remain those of 01, evaluated from the common section variables.

---

# 6. Global section equilibrium remains R4

For a given global amplitude `q`, solve

\[
R_{N_x}=N_x^U+N_x^s-N_x^A(q)=0,
\]

\[
R_{M_x}=M_x^U+M_x^s-M_x^A(q)=0,
\]

\[
R_{N_y}=N_y^U+N_y^s+N_y^w-N_y^A(q)=0,
\]

\[
R_{M_y}=M_y^U+M_y^s+M_y^w-M_y^A(q)=0.
\]

No new outer equilibrium equation is introduced.

---

# 7. BH-family specialization used in the first execution

For BH032 and BH050,

\[
L_G=b,
\]

so

\[
K_s=E_st_s=824.0\ \mathrm{kN/mm},
\]

\[
K_c=E_ct_c/2=911.4\ \mathrm{kN/mm},
\]

and

\[
\boxed{K_{eq}=432.750\ \mathrm{kN/mm}}.
\]

TOP face uses 4 ribs:

\[
K_P^+=4K_r=303.340\ \mathrm{kN/mm},
\]

\[
\boxed{\gamma_+=0.41210}.
\]

BOTTOM face uses 5 ribs:

\[
K_P^-=5K_r=379.175\ \mathrm{kN/mm},
\]

\[
\boxed{\gamma_-=0.46701}.
\]

The direct adjacent multiwave classification remains

```text
TOP regular bays:    3 / 4 / 5
BOTTOM regular bays: 3 / 4 / 5 / 4
non-standard edge residual strips: ideal-EP E branch
```

---

# 8. Interpretation boundary

This model is to be read as

\[
\boxed{\text{Multiwave 01} + \text{one fixed finite composite-transfer factor per face}}.
\]

It is useful for diagnosing the sensitivity of gross steel-shell `N/M` and Pu to finite longitudinal shear transfer. It is **not yet** a source-locked PBL constitutive model and must not be promoted to production solely because one diagnostic stiffness improves agreement with BH032/BH050.

Production R14 remains unchanged.
