# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-25  
**Status:** `MARGUERRE_AIRY_EXPLICIT_RETAINED / AIRY_USES_INITIAL_FULL_COMPOSITE_ABD / Z0-Z6_OFFSET_AUDIT_PASS / R07_COEFFICIENTS_RETAIN / SSNC_R02_AVAILABLE / SSNC_R04_IDEAL_EP_TERMINAL_AVAILABLE / Z6_R05_COMMON_ENDPOINT_STRAIN_BRIDGE_CLOSED / Z6_R05_INDEPENDENT_ROOT_FIXED / R02-R04_DIRECT_INTERFACE_BLOCKER_SUPERSEDED_FOR_Z6_ENDPOINT / R03_UNTOUCHED`

> R05 closes the previously missing R02→R04 face-strain interface at the governing **Z6 symmetric endpoint**.  The endpoint has `s=0`, `My=0`, a uniform common terminal state `Y=eps_y/eps0=-1`, `gamma_xy=0`, and one remaining section strain coordinate `X=eps_x/eps0`.  This state drives NC-M6, R02, R04, web steel, and both external faces simultaneously.  No historical provisional `Pu/X/q`, Zhou, or Winter value enters root selection.

## 0. Hard architecture

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
AIRY_FUNCTION = RETAINED
AIRY_STIFFNESS = INITIAL_FULL_COMPOSITE_ABD
CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO
GLOBAL_ULTIMATE_STATE_CRITERION = UNCHANGED
TERMINAL_OBJECT = CURRENT/CAPACITY RESULTANTS

D15 = NO
GLOBAL_MATERIAL_VIRTUAL_WORK_RJ = NO
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
EFFECTIVE_WIDTH_OR_AREA_AS_PRODUCTION = PROHIBITED
FORMAL_Z_COMPARATORS = ZHOU_SIMING + WINTER ONLY
R03_CURRENT_6X6_TANGENT_AS_Pu_GATE = NO
R03_REOPENED_IN_R05 = NO
```

## 1. Initial steel offset stiffness remains closed

The 2026-08-25 Z0–Z6 audit independently reconstructed

\[
D_{EI}^{calc}
=E_c\frac{t_c^3}{12}
+E_s\left(2t_sz_f^2+2\frac{t_s^3}{12}\right)
\]

for every Z specimen.  The maximum discrepancy from the archived Airy stiffness was only floating-point roundoff.  Therefore

```text
Z0_Z6_INITIAL_OFFSET_D = PASS
R07_AIRY_OFFSET_CORRECTION_NEEDED = NO
ADD_STEEL_OFFSET_AGAIN = PROHIBITED_DOUBLE_COUNTING
R07_STRUCTURAL_COEFFICIENTS = RETAIN
```

R05 does not alter `Pcr,C,G,Jy,Kx` because no missing eccentric face stiffness exists.

## 2. R05 common endpoint bridge

At the governing Z6 endpoint,

\[
\boxed{s=0,\qquad M_y^d=0},
\]

and R05 freezes the common current terminal strain state

\[
\boxed{
Y\equiv\frac{\varepsilon_y}{\varepsilon_0}=-1,
\qquad
\gamma_{xy}=0,
\qquad
X\equiv\frac{\varepsilon_x}{\varepsilon_0}.
}
\]

The NC-M6 Poisson-neutral principal coordinates are therefore

\[
\lambda_t=\frac{X-\nu_c}{1-\nu_c^2},
\qquad
\lambda_c=\frac{-1+\nu_cX}{1-\nu_c^2}.
\]

The same physical mean strain is supplied to the upper and lower external faces.  R02 uses its compression-positive convention

\[
(e_x,e_y,\gamma)_{R02}=(-\varepsilon_x,-\varepsilon_y,0),
\]

then R04 converts the resulting R02 trial mean stress back to the physical tension-positive convention and applies its frozen ideal-EP radial Mises cap.

This is the common section strain bridge that was absent from the 09:10 gate.

## 3. R05 independent root

The preceding broad multi-seed endpoint search, performed without any old provisional `Pu/X/q` seed, produced one positive root cluster near `X=0.97579742, q=0.01180088`.  R05 uses only that independent cluster as the refinement seed.

High-precision refinement gives

\[
\boxed{X=0.975797415476470457703134943536555645461},
\]

\[
\boxed{q=0.01180088028170258636542452885480436575091},
\]

\[
\boxed{U_{R02}=0.1270986806879544830159288254178676823454\ \mathrm{mm}},
\]

\[
\boxed{P_u^{R05}=49.4543983371962435941\ \mathrm{MN}}.
\]

The common physical strain is

\[
\varepsilon_x=+0.00182595997641601044644,
\]

\[
\varepsilon_y=-0.0018712490394580678,
\qquad
\gamma_{xy}=0.
\]

and

\[
\lambda_t=0.822444621203462647482,
\qquad
\lambda_c=-0.851959968183376723453.
\]

## 4. Current material state at the R05 root

NC-M6:

```text
TC branch            = TC-B
compression base sc  = -30.01405759865349 MPa
fcr                   = 0.1157827204039525 MPa
tension branch        = RESID
gamma-active          = YES
gamma                 = 0.9262422451919473
sigma_x_concrete      = +0.03473481612118574 MPa
sigma_y_concrete      = -27.80028809749724 MPa
```

R02 at the fixed common face strain:

```text
L0 = 0.00493280024998645449729
B3 = 1.17975350735700040389
B1 = 2.29419452855441005419
B0 = -0.294011322388344352684
```

so

\[
\boxed{
1.17975350735700040389U^3
+2.29419452855441005419U
-0.294011322388344352684=0.
}
\]

Its derivative is strictly positive for all real `U`, so the cubic has exactly one real root.  That root is the `U_R02` reported above; its R02 condensed-energy functional is

\[
2.16666537729371273899
\]

in the source normalization.

R04:

```text
trial stress [MPa]  = (+286.3263780231887, -299.5390506460883, 0)
trial Mises [MPa]   = 507.4173519518590
radial scale        = 0.6996213248018378
capped stress [MPa] = (+200.3200399182951, -209.5639074429011, 0)
capped Mises [MPa]  = 355.0
```

The 2% longitudinal web is at y-compression yield `sigma_y^w=-355 MPa`.

## 5. Phase resultants and Airy equilibrium

Physical tension-positive resultants per unit width:

```text
phase                         Nx [N/mm]          Ny [N/mm]
concrete core                 +4.15289461545     -3323.80244493677
2% equivalent web             0                  -866.20000000000
upper external face           +801.28015967318   -838.25562977160
lower external face           +801.28015967318   -838.25562977160
section total                 +1606.71321396181  -5866.51370447998
Airy demand                   +1606.71321396181  -5866.51370447998
```

For `zf=63 mm`, the two faces give equal/opposite parallel-axis moments:

```text
upper Mparallel_x = +50480.65005941037 N
upper Mparallel_y = -52810.10467561107 N
lower Mparallel_x = -50480.65005941037 N
lower Mparallel_y = +52810.10467561107 N
total Mparallel   = (0,0)
```

Thus `My=0` is satisfied without a through-thickness plastic bending partition.  The own-skin elastic `Et_s^3/12` contribution remains only in the initial Airy stiffness, as required by R04.

High precision:

```text
R02 cubic residual < 1e-68
|Rx|               < 2e-68 N/mm
|Ry|               < 1e-68 N/mm
```

Independent ordinary-double reevaluation gives force residuals of order `1e-12 N/mm`.

## 6. Comparator opened after root fixation only

Only after the R05 root and all phase resultants were fixed:

\[
P_{Zhou}=49.48676675\ \mathrm{MN},
\qquad
P_{Winter}=50.18585413\ \mathrm{MN}.
\]

Therefore

\[
\boxed{R05-Zhou=-0.0654082\%},
\]

\[
\boxed{R05-Winter=-1.4574940\%}.
\]

No parameter or root is changed after this comparison.

## 7. Supersession

The earlier state

```text
R02-R04_DIRECT_INTERFACE_BLOCKED_AT_FACE_STRAIN_MAP
```

is now recorded as

```text
R02-R04_DIRECT_INTERFACE_BLOCKED_AT_FACE_STRAIN_MAP = SUPERSEDED_FOR_Z6_R05_ENDPOINT
R02_R04_Z6_COMMON_ENDPOINT_INTERFACE = CLOSED
Z6_R05_ROOT = FIXED
Z6_R05_GATE = PASS
```

This supersession is specific to the Z6 symmetric endpoint reduction.  It does not silently assert that arbitrary `s!=0` states or Z0–Z5 share the same uniform-section degeneration.

## 8. R05 artifacts

- executable: `semantic_v2/40_execution/steel_shell/20260825_1120__NZSCCM__Z6_R05_COMMON_ENDPOINT_R02_R04_REFINEMENT.py`
- manual recomputation: `semantic_v2/40_execution/20260825_1120__NZSCCM__Z6_R05_COMMON_ENDPOINT_R02_R04_MANUAL_RECALC.md`

## 9. Next task

```text
NEXT =
KEEP Z6 R05 FIXED;
DO NOT REOPEN R03 OR OFFSET STIFFNESS;
IF A NEW Z-FAMILY BATCH IS REQUESTED,
APPLY THE R05 COMMON-TERMINAL LOGIC CASE BY CASE,
WITH COMPARATORS CLOSED UNTIL EACH THEORETICAL ROOT IS FIXED.
```
