# NZ-SCCM — Z6 R05 common-endpoint R02/R04 manual recomputation

**Date:** 2026-08-25  
**Identity:** `Z6_R05 / INDEPENDENT_ROOT_REFINEMENT / COMMON_ENDPOINT_STRAIN_BRIDGE / R02_R04_TERMINAL / NO_R03_REOPEN`  
**Comparator in root solve:** `NO`  
**Formal spatial quadrature:** `0`  
**Formal thickness quadrature:** `0`  
**Material points:** `0`

## 0. Decision

The broad multi-seed endpoint search completed immediately before this gate, without using any historical provisional `Pu/X/q` as seeds, produced one clustered positive root near

\[
X\approx0.97579742,\qquad q\approx0.01180088.
\]

R05 refines that independent root directly.  It does not reopen eccentric stiffness/R03, does not modify the frozen R07 Marguerre--Airy coefficients, and does not use Zhou/Winter during the solve.

The exact interface closure at the governing symmetric endpoint is

\[
s=0,\qquad M_y^d=0,
\]

\[
\boxed{Y\equiv\varepsilon_y/\varepsilon_0=-1,\qquad \gamma_{xy}=0,\qquad X\equiv\varepsilon_x/\varepsilon_0.}
\]

Hence the upper and lower external steel faces share the same current mean strain state; their parallel-axis terminal moments are equal and opposite.  This supplies the missing common terminal strain state required by R02 without using initial-elastic ABD inversion as a nonlinear terminal assumption.

Therefore the prior state

```text
R02-R04_DIRECT_INTERFACE_BLOCKED_AT_FACE_STRAIN_MAP
```

is **superseded for the Z6 R05 symmetric endpoint** by the explicit common-endpoint strain bridge above.

---

## 1. Frozen source contracts used

R05 uses the already-read/frozen sources only:

1. `semantic_v2/40_execution/steel_shell/20260825_0130__NZSCCM__SSNC_R02_PBL_2D_FULL_RESULTANT_GATE.py` — R02 finite PBL/Yun mean-face strain operator and cubic amplitude condensation.
2. `semantic_v2/40_execution/steel_shell/20260825_0851__NZSCCM__SSNC_R04_IDEAL_EP_2D_TERMINAL_RESULTANT_GATE.py` — R04 path-free 2D ideal-EP radial Mises cap and centroidal face resultant.
3. `semantic_v2/20_theory/20260820_2358__NZSCCM__NGUYEN_KINEMATICS_EXPLICIT_UV_AND_NC_M6_VIRTUAL_WORK_SYSTEM.md` plus the frozen NC-M6 TC implementation — physical strain to Poisson-neutral principal material coordinates and TC-B/gamma law.
4. `semantic_v2/40_execution/20260824_0918__NZSCCM__Z0_Z6_NY_MY_RESULTANT_RECALCULATION_R07.md` — frozen Z6 structural demand law.
5. Z-family Yun convention already frozen in the unified local-shell line: `Bs=200 mm`, `ts=4 mm`, local peak imperfection `Bs/400=0.5 mm`, hence R02 coefficient `A0=Bs/1600=0.125 mm`.

No offset stiffness is added again: the 2026-08-25 offset audit already proved that the current R07 front contains the external-face parallel-axis stiffness.

---

## 2. Z6 R07 demand at the R05 endpoint

Frozen data:

\[
b=12000\ \mathrm{mm},\quad q_0=0.004,
\]

\[
P_{cr}=39.2880147150\ \mathrm{MN},\quad C=86071.5974582\ \mathrm{MN},
\]

\[
G=7.4692093263\times10^6\ \mathrm{N/mm},
\]

\[
K_x=6.876056916767441\times10^6\ \mathrm{N/mm}.
\]

With

\[
Q_q=q(q+2q_0),
\]

\[
P(q)=P_{cr}\frac{q}{q+q_0}+CQ_q,
\]

at `s=0`:

\[
N_x^d=K_xQ_q,
\]

\[
N_y^d=-\left[\frac{P(q)10^6}{b}+GQ_q\right],\qquad M_y^d=0.
\]

---

## 3. Independent root refinement

The R05 high-precision solution is

\[
\boxed{X=0.975797415476470457703134943536555645461},
\]

\[
\boxed{q=0.01180088028170258636542452885480436575091},
\]

and the internally condensed R02 total local amplitude is

\[
\boxed{U=0.1270986806879544830159288254178676823454\ \mathrm{mm}}.
\]

The resulting load is

\[
\boxed{P_u=49.4543983371962435940880912776\ \mathrm{MN}}.
\]

The high-precision equilibrium residual norm is below `2e-68 N/mm`; ordinary double-precision reevaluation gives about `9.1e-13 N/mm` in the two force rows.

---

## 4. Physical strain and NC-M6 material coordinates

With

\[
\varepsilon_0=0.0018712490394580678,
\]

physical tension-positive engineering strain is

\[
\boxed{\varepsilon_x=+0.00182595997641601044644},
\]

\[
\boxed{\varepsilon_y=-0.00187124903945806780000},
\]

\[
\boxed{\gamma_{xy}=0}.
\]

For `nu_c=0.18`, the Poisson-neutral NC-M6 principal coordinates are

\[
\lambda_t=\frac{X-\nu_c}{1-\nu_c^2}
=\boxed{0.822444621203462647482},
\]

\[
\lambda_c=\frac{-1+\nu_cX}{1-\nu_c^2}
=\boxed{-0.851959968183376723453}.
\]

### NC-M6 TC-B / gamma audit

The uncoupled Saenz compression value at `lambda_c` is

\[
s_c=-30.0140575986534918155\ \mathrm{MPa},
\]

so

\[
r_c=-s_c/f_c=0.9873045262714964413>0.8.
\]

Therefore the active TC crack-strength branch is **TC-B**:

\[
f_{cr}=3f_t(1-r_c)=\boxed{0.115782720403952455364\ \mathrm{MPa}}.
\]

The tensile coordinate lies well beyond `10 x_cr`, so the current NC-M6 tension part is the **RESID** branch:

\[
\sigma_x^c=0.3f_{cr}
=\boxed{0.0347348161211857366092\ \mathrm{MPa}}.
\]

Since

\[
\lambda_t>10/17,
\]

the current TC gamma coupling is active:

\[
\boxed{\gamma_c=\frac1{0.8+0.34\lambda_t}=0.926242245191947267213},
\]

and

\[
\boxed{\sigma_y^c=\gamma_c s_c=-27.8002880974972355703\ \mathrm{MPa}}.
\]

Thus the root is unambiguously `TC-B / RESID / gamma-active`.

---

## 5. R02 amplitude equation at the fixed root

R02 receives compression-positive mean face strain, i.e.

\[
e_x^{R02}=-\varepsilon_x,
\qquad
e_y^{R02}=-\varepsilon_y,
\qquad\gamma^{R02}=0.
\]

For the `200 x 200 x 4 mm`, `A0=0.125 mm` Z-family local cell, the source coefficients are

\[
\boxed{L_0=0.00493280024998645449729},
\]

\[
\boxed{B_3=1.17975350735700040389},
\]

\[
\boxed{B_1=2.29419452855441005419},
\]

\[
\boxed{B_0=-0.294011322388344352684}.
\]

The complete R02 cubic is therefore

\[
\boxed{
1.17975350735700040389\,U^3
+2.29419452855441005419\,U
-0.294011322388344352684=0.
}
\]

There is no `U^2` term.  Since

\[
\frac{d}{dU}(B_3U^3+B_1U+B_0)=3B_3U^2+B_1>0,
\]

there is exactly one real root:

| real root | `U` mm | R02 condensed-energy functional |
|---|---:|---:|
| 1 | 0.127098680687954483016 | 2.16666537729371273899 |

The other two polynomial roots are a complex-conjugate pair and are not admissible real amplitude states.  The energy value above is reported in the exact source normalization of R02 `condensed_energy`; no new physical unit is assigned to that diagnostic scalar here.

The cubic residual at the high-precision root is below `1e-68`.

---

## 6. R02 trial mean stress and R04 ideal-EP cap

R02 gives the compression-positive mean normal stresses

\[
(\sigma_x,\sigma_y)_{R02}
=(-286.326378023188732292,\ +299.539050646088282145)\ \mathrm{MPa}.
\]

Converting to the R04 physical tension-positive trial convention gives

\[
\boxed{\boldsymbol\sigma^{tr}
=(+286.326378023188732292,\ -299.539050646088282145,\ 0)\ \mathrm{MPa}}.
\]

Trial Mises stress:

\[
\boxed{\sigma_{VM}^{tr}=507.417351951859018137\ \mathrm{MPa}}.
\]

Since it exceeds `fy=355 MPa`, R04 applies

\[
\boxed{\lambda_p=f_y/\sigma_{VM}^{tr}=0.699621324801837792705}.
\]

Capped face stress:

\[
\boxed{\boldsymbol\sigma_s
=(+200.320039918295114535,\ -209.563907442901070574,\ 0)\ \mathrm{MPa}},
\]

with

\[
\boxed{\sigma_{VM}=355.000000000000\ \mathrm{MPa}}.
\]

Both external faces have the same capped membrane state at `s=0`.

---

## 7. Phase-by-phase resultants

All values below use the physical tension-positive sign convention and are per unit transverse width.

| phase | `Nx` N/mm | `Ny` N/mm |
|---|---:|---:|
| concrete core `(1-rho_w)tc` | +4.15289461544897 | -3323.80244493676948 |
| 2% equivalent longitudinal web | 0 | -866.20000000000000 |
| upper external steel face | +801.28015967318046 | -838.25562977160428 |
| lower external steel face | +801.28015967318046 | -838.25562977160428 |
| **section total** | **+1606.71321396180988** | **-5866.51370447997805** |

The web reaches longitudinal ideal-EP compression yield because

\[
E_s\varepsilon_y\approx-385.48\ \mathrm{MPa}<-f_y,
\]

hence

\[
\sigma_y^w=-355\ \mathrm{MPa}.
\]

At the same root the frozen Airy demands are

\[
\boxed{N_x^d=+1606.71321396180988\ \mathrm{N/mm}},
\]

\[
\boxed{N_y^d=-5866.51370447997805\ \mathrm{N/mm}}.
\]

Thus both membrane equilibrium equations close simultaneously.

---

## 8. Parallel-axis terminal moment

For Z6

\[
z_f=\frac{t_c}{2}+\frac{t_s}{2}=63\ \mathrm{mm}.
\]

The R04 centroidal face resultants give the upper-face lever-arm moments

\[
M_{x,+}^{parallel}=+50480.65005941037\ \mathrm{N},
\]

\[
M_{y,+}^{parallel}=-52810.10467561107\ \mathrm{N},
\]

while the lower face gives exactly the opposite values:

\[
M_{x,-}^{parallel}=-50480.65005941037\ \mathrm{N},
\]

\[
M_{y,-}^{parallel}=+52810.10467561107\ \mathrm{N}.
\]

Hence

\[
\boxed{\mathbf M^{parallel}_{top+bottom}=\mathbf0}.
\]

The symmetric concrete and web states likewise have zero first moment, so the endpoint satisfies the Airy demand `My=0`.  No own-skin plastic bending block is introduced; its elastic `Et_s^3/12` contribution remains only in the initial Airy stiffness, as required by R04.

---

## 9. Final residual ledger

High precision:

```text
R02 cubic residual  < 1e-68
Rx = Nx_section - Nx_Airy  ~= -1.85e-68 N/mm
Ry = Ny_section - Ny_Airy  =   0 at displayed precision
||R_force||_inf            < 2e-68 N/mm
```

Independent ordinary double-precision reevaluation of the same fixed root gives approximately

```text
R02 cubic = 5.55e-17
Rx        = 4.55e-13 N/mm
Ry        = -9.09e-13 N/mm
```

so the root is not a tolerance artifact.

The fixed R05 prediction is

\[
\boxed{P_u^{R05}=49.45439833719624\ \mathrm{MN}}.
\]

---

## 10. Comparator opened only after the root was fixed

Only after all preceding state variables and resultants were fixed were the historical comparators opened:

\[
P_{Zhou}=49.48676675\ \mathrm{MN},
\qquad
P_{Winter}=50.18585413\ \mathrm{MN}.
\]

Therefore

\[
\boxed{\Delta_{Zhou}=-0.0654082\%},
\]

\[
\boxed{\Delta_{Winter}=-1.4574940\%}.
\]

No parameter, branch, seed, or control coordinate was changed after this comparison.

---

## 11. R05 gate decision

```text
Z6_R05_INDEPENDENT_ENDPOINT_REFINEMENT = PASS
Z6_R05_COMMON_TERMINAL_STRAIN_BRIDGE = CLOSED
Z6_R05_NC_M6_STATE = TC-B / RESID / GAMMA-ACTIVE
Z6_R05_R02_CUBIC_REAL_ROOTS = 1
Z6_R05_R04_MISES_CAP = ACTIVE
Z6_R05_WEB_Y_COMPRESSION_YIELD = ACTIVE
Z6_R05_MPARALLEL_TOTAL = 0
Z6_R05_Pu_MN = 49.45439833719624
COMPARATOR_IN_ROOT_SELECTION = 0
R03_REOPENED = NO
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
R02-R04_DIRECT_INTERFACE_BLOCKED_AT_FACE_STRAIN_MAP = SUPERSEDED_BY_R05_COMMON_ENDPOINT_STRAIN_BRIDGE
```

Scope note: this R05 gate closes the exact **Z6 symmetric endpoint** interface and justifies the present Z6 root.  It does not silently claim that every off-centre `s!=0` state or every Z0--Z5 specimen has the same uniform-section degeneration; those require their own R05-family rerun if production values are requested.
