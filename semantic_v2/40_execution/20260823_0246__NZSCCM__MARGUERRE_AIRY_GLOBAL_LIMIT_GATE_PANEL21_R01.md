# NZ-SCCM — Marguerre–Airy global-limit gate + Panel21 full calculation R01

**Time:** 2026-08-23 02:46 +08:00  
**Scope:** structural regression only; no material tuning; no experimental load in root selection.  
**Formal spatial quadrature:** 0.  
**Material points:** 0.  
**Load stepping / continuation:** 0.

## 0. Executive result

The current locked structural mainline is the existing
`20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`.
The Airy field is retained.  The previous idea of simply deleting the local
section terminal rule and replacing it by a global fold of the *same V1*
was tested exactly.

For the V1 postbuckling backbone

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
\frac{dP_{pb}}{dq}
=P_{cr}\frac{q_0}{(q+q_0)^2}+2C(q+q_0).
\]

For every admissible RC plate in this V1,

\[
q\ge0,\quad q_0>0,\quad P_{cr}>0,\quad C>0,
\]

hence

\[
\boxed{dP_{pb}/dq>0\quad\forall q\ge0}.
\]

Therefore

\[
\boxed{\text{MA-V1 geometric global fold does not exist.}}
\]

A finite ultimate load in the present V1 necessarily comes from the later
capacity/terminal layer.  If the local terminal layer is removed without adding
**global current-material degradation/work conjugacy**, V1 has no finite `Pu`.

This is an architecture result, not a Panel21 calibration result.

---

# 1. Current Marguerre–Airy structure retained

The locked V1 uses

\[
\phi=\sin(\alpha x)\sin(\beta y),
\qquad
w_i=bq_0\phi,
\qquad
w=bq\phi.
\]

Airy membrane resultants are

\[
N_x=\theta_{,yy},\qquad
N_y=\theta_{,xx},\qquad
N_{xy}=-\theta_{,xy},
\]

with

\[
\theta=\theta_h+\theta_p,
\qquad
\theta_h=-\frac12\frac{P}{b}x^2.
\]

The orthotropic compatibility equation is

\[
\bar A_{22}\theta_{,xxxx}
+(2\bar A_{12}+\bar A_{66})\theta_{,xxyy}
+\bar A_{11}\theta_{,yyyy}
=\mathcal G(w,w_i),
\]

and for the single physical mode

\[
\mathcal G
=\frac12b^2q(q+2q_0)\alpha^2\beta^2
[\cos(2\alpha x)+\cos(2\beta y)].
\]

With

\[
\Delta_A=A_{11}A_{22}-A_{12}^2,
\]

\[
\bar A_{11}=\frac{A_{22}}{\Delta_A},\quad
\bar A_{22}=\frac{A_{11}}{\Delta_A},\quad
\bar A_{12}=-\frac{A_{12}}{\Delta_A},\quad
\bar A_{66}=\frac1{A_{66}},
\]

the exact Airy particular solution gives the V1 membrane redistribution and the
Galerkin projection gives

\[
K_b=D_x\alpha^4+2H\alpha^2\beta^2+D_y\beta^4,
\]

\[
K_m=\frac{\Delta_A}{16}
\left(\frac{\alpha^4}{A_{22}}+\frac{\beta^4}{A_{11}}\right),
\]

\[
P_{cr}=\frac{bK_b}{\beta^2},
\qquad
C=\frac{b^3K_m}{\beta^2},
\]

and finally

\[
\boxed{P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0)}.
\]

Nothing in this derivation uses a local material point or a spatial quadrature.

---

# 2. Global-fold theorem for the existing V1

Take the V1 equilibrium manifold in reduced form

\[
R(P,q)=P-P_{pb}(q)=0.
\]

A one-coordinate load fold requires

\[
\left.\frac{\partial R}{\partial q}\right|_P=0
\iff
\frac{dP_{pb}}{dq}=0.
\]

But

\[
\frac{dP_{pb}}{dq}
=P_{cr}\frac{q_0}{(q+q_0)^2}+2C(q+q_0).
\]

The elastic halfwave front has positive-definite `D`, so `Pcr>0`.  Positive-definite
`A` gives `A11>0`, `A22>0`, `DeltaA>0`, hence `Km>0` and `C>0`.  With a positive
initial imperfection `q0>0`, both derivative terms are strictly positive.

Thus

\[
\boxed{\nexists q\ge0:\ dP_{pb}/dq=0}.
\]

This proves that merely changing the terminal criterion from local to global
without changing the material participation cannot create a finite ultimate load.

---

# 3. Panel21 — complete structural calculation

## 3.1 Raw inputs

\[
a_{phys}=2440\ \mathrm{mm},\quad
b=1220\ \mathrm{mm},\quad
t=19.30\ \mathrm{mm},
\]

\[
E_0=20321\ \mathrm{MPa},\quad
\nu=0.18,\quad
E_s=200000\ \mathrm{MPa},
\]

\[
p_{tot}=0.0075,\qquad q_0=1/400=0.0025.
\]

Correct two-way reinforcement mapping:

\[
\rho_x=\rho_y=\frac{p_{tot}}2=0.00375.
\]

One mid-plane layer gives

\[
a_x=a_y=\rho_{dir}t
=0.00375\times19.30
=0.072375\ \mathrm{mm}.
\]

Concrete phase thickness after area replacement:

\[
t_c^*=19.30-0.072375-0.072375
=19.15525\ \mathrm{mm}.
\]

## 3.2 Plane-stress constants

\[
Q_c=\frac{20321}{1-0.18^2}
=21001.4468789\ \mathrm{MPa},
\]

\[
Q_{c12}=3780.26043820\ \mathrm{MPa},
\qquad
Q_{c66}=8610.59322034\ \mathrm{MPa}.
\]

## 3.3 Extensional matrix

\[
A_{11}=A_{22}
=Q_ct_c^*+E_sa_x
=416762.9653266\ \mathrm{N/mm},
\]

\[
A_{12}=Q_{c12}t_c^*
=72411.8337588\ \mathrm{N/mm},
\]

\[
A_{66}=Q_{c66}t_c^*
=164938.0657839\ \mathrm{N/mm},
\]

\[
\Delta_A=A_{11}A_{22}-A_{12}^2
=1.6844789559949536\times10^{11}\ (\mathrm{N/mm})^2.
\]

## 3.4 Bending matrix

The reinforcement is at `z=0`, so its layer-position contribution to `D` is zero.

\[
I=\frac{t^3}{12}=599.088083333\ \mathrm{mm^3}.
\]

\[
D_x=D_y=Q_cI
=1.25817165578924\times10^7\ \mathrm{N\,mm},
\]

\[
D_\mu=2.26470898042063\times10^6\ \mathrm{N\,mm},
\]

\[
D_{66}=5.15850378873588\times10^6\ \mathrm{N\,mm},
\]

\[
H=D_\mu+2D_{66}
=1.25817165578924\times10^7\ \mathrm{N\,mm}.
\]

## 3.5 Elastic halfwave selection

\[
\alpha=\frac{\pi}{1220}=0.0025750759455654\ \mathrm{mm^{-1}}.
\]

For

\[
\beta_j=\frac{j\pi}{2440},
\]

\[
P_{cr,j}
=b\frac{D_x\alpha^4+2H\alpha^2\beta_j^2+D_y\beta_j^4}{\beta_j^2}.
\]

The first six integer candidates are:

| j | halfwave ell (mm) | Pcr (kN) |
|---:|---:|---:|
|1|2440.000|636.150436|
|2|1220.000|407.136279|
|3|813.333|477.819661|
|4|610.000|636.150436|
|5|488.000|856.004027|
|6|406.667|1130.934108|

Therefore

\[
\boxed{m_*=2},\qquad
\boxed{\ell=1220\ \mathrm{mm}},
\]

and

\[
\boxed{P_{cr}=407.136279059\ \mathrm{kN}}.
\]

This independently recovers the same two-halfwave scale already identified in the
Panel21 geometry audit.

## 3.6 Airy coefficients

For `alpha=beta`:

\[
K_b=0.00221289117351513,
\]

\[
K_m=2.22150170761958\times10^{-6},
\]

\[
\boxed{C=608339.560102679\ \mathrm{kN}}.
\]

The longitudinal membrane redistribution is

\[
n(x;P,q)=\frac{P}{b}
+Gq(q+2q_0)\cos(2\alpha x),
\]

with

\[
\boxed{G=498638.983690721\ \mathrm{N/mm}}.
\]

The Airy particular-solution scalar coefficient for each square-halfwave cosine
term is

\[
\frac{\Delta_A}{16A_{11}}=25261.3460188781\ \mathrm{N/mm}.
\]

## 3.7 Explicit postbuckling path

Panel21 therefore has

\[
\boxed{
P_{pb}(q)
=407.136279059\frac{q}{q+0.0025}
+608339.560103\,q(q+0.005)
\quad[\mathrm{kN}].
}
\]

Selected points, computed only to display the path:

| q | Ppb (kN) | dP/dq (kN per unit q) |
|---:|---:|---:|
|0|0|165896.209424|
|0.002|189.466211|55738.794196|
|0.004|272.445627|31999.318368|
|0.006|327.540726|24429.533043|
|0.008|373.466384|22007.245934|
|0.010|416.959957|21722.669468|
|0.020|666.068695|29385.829731|

At every displayed point the tangent is positive, but the decisive result is the
analytic inequality, not the sample table.

Hence the attempted global limit equation

\[
\boxed{dP_{pb}/dq=0}
\]

has no admissible root.

Therefore the Panel21 result of the *current V1 after deleting all local terminal
criteria* is

```text
PANEL21_MA_V1_GLOBAL_FOLD = NONE
PANEL21_FINITE_Pu = NOT_DEFINED
```

This must not be replaced by the experiment, by the historical `368.189 kN`, or by
a local section root.

---

# 4. Why the finite Pu disappeared

The current V1 Airy/Galerkin backbone uses **fixed elastic A and D** in the global
compatibility and transverse equilibrium.  Concrete cracking/softening, steel
yield and the current NC-M6 law do not reduce those global coefficients.  Material
nonlinearity was introduced later only through local capacity/current-section
checks.

Consequently:

1. the Marguerre–Airy geometric path itself hardens monotonically;
2. a finite `Pu` is supplied only by the terminal material layer;
3. deleting that terminal layer exposes that the V1 global backbone has no
   material-driven limit point.

Thus the previous statement

> retain V1 unchanged and merely replace the local terminal rule by a global fold

is rejected.

---

# 5. Minimal mathematically consistent MA global-limit extension

The next theory must retain Airy membrane equilibrium but allow the *global current
material law* to participate in the equilibrium/tangent operator.

At minimum a second global loading coordinate must re-enter.  Denote the mean
axial strain/loading coordinate by `D` and the physical deflection amplitude by
`q`.  Let the exact current-material global transverse residual be

\[
R_q(D,q)=0
\]

and the reaction be

\[
P=P(D,q).
\]

Along the equilibrium manifold,

\[
\frac{dq}{dD}=-\frac{R_{q,D}}{R_{q,q}},
\]

so

\[
\frac{dP}{dD}
=\frac{P_{,D}R_{q,q}-P_{,q}R_{q,D}}{R_{q,q}}.
\]

Therefore the generic global load-limit condition is

\[
\boxed{
L_{global}
=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0.
}
\]

The determinant form is generic mechanics; its reappearance does **not** by itself
mean that the old D15 structural derivation has been reinstated.

However, to call the new route genuinely Marguerre–Airy, the current-material
closure must also satisfy the Airy membrane equilibrium/compatibility structure.
The fixed-elastic V1 coefficients cannot simply be reused once material tangent
varies over the plate.

This is the next operator-recovery task.

---

# 6. Locked decisions after this gate

```text
STRUCTURAL_MAINLINE = MARGUERRE_AIRY_EXPLICIT_RETAINED
AIRY_FUNCTION = RETAINED
MA_V1_ELASTIC_GEOMETRIC_BACKBONE = VALID_AS_POSTBUCKLING_BACKBONE
MA_V1_GEOMETRIC_GLOBAL_FOLD = PROVEN_ABSENT
DELETE_LOCAL_TERMINAL_AND_USE_dPpb_dq_EQ_0 = FAIL
FINITE_Pu_WITHOUT_GLOBAL_MATERIAL_DEGRADATION = NOT_DEFINED
LOCAL_detJsec_AS_PRIMARY_PLATE_Pu = NOT_ACCEPTED
MATERIAL_TUNING = PAUSED

NEXT_TASK = DERIVE_NONLINEAR_CURRENT_MATERIAL_GLOBAL_WORK_CLOSURE_UNDER_MARGUERRE_AIRY
NEXT_GATE_1 = AIRY_MEMBRANE_EQUILIBRIUM_RETAINED
NEXT_GATE_2 = CURRENT_MATERIAL_PARTICIPATES_IN_GLOBAL_RESIDUAL_AND_TANGENT
NEXT_GATE_3 = SAME_LAW_JACOBIAN
NEXT_GATE_4 = ZERO_FORMAL_SPATIAL_QUADRATURE
NEXT_GATE_5 = PANEL21_PURE_M2_REDUCTION_CHECK
NEXT_GATE_6 = NO_Pf_IN_OPERATOR_OR_ROOT_SELECTION
```

## Reproduction driver

`semantic_v2/40_execution/rc/20260823_0246__NZSCCM__PANEL21_MARGUERRE_AIRY_GLOBAL_FOLD_GATE.py`
