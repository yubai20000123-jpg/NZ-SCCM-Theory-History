# NZ-SCCM — Airy–SSUHPC force-first terminal-capacity system R01

**Date:** 2026-08-28  
**Identity:** THEORY REORGANIZATION / DIAGNOSTIC ONLY / NOT PRODUCTION  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Objective:** prioritize ultimate load and constituent resultant allocation; do not require Airy deformation coordinate or terminal curvature coordinates to reproduce the actual deformation field.

---

## 0. Governing decision

The active diagnostic direction returns to the frozen 2026-08-25 architecture:

\[
\boxed{
\text{initial full-composite Marguerre–Airy structural demand}
\rightarrow
\text{current terminal section resultant allocation/capacity}
\rightarrow P_u
}
\]

The roles are now explicit:

```text
Airy q              = structural demand coordinate
Airy                 = generator of P, Nx, Ny, Mx, My demand
terminal Ax,Ay,Bx,By = section/capacity coordinates
UHPC/R02/R06/web     = current constituent resultant operators
Pu                   = first admissible Airy-demand / terminal-capacity contact
primary outputs      = Pu + phase resultants/load sharing
secondary/non-gating = deflection, curvature and strain-field fidelity
```

The following are NOT part of this route:

```text
Nguyen full-current halfwave virtual work
current material tangent inserted into Airy compatibility
forcing Bx,By = Airy q-curvature
current-moment antinode-as-modal-amplitude feedback
formal spatial quadrature/material points
effective width/area
FEM/test in root selection
```

This file does not modify production.

---

## 1. Frozen Airy demand front

Define

\[
Q_q=q(q+2q_0).
\]

The frozen postbuckling load family remains

\[
\boxed{
P^A(q)=P_{cr}\frac{q}{q+q_0}+C Q_q.
}
\]

For the current one-harmonic terminal family, the normal/bending demands are

\[
\boxed{N_x^A(q,s)=K_xQ_q,}
\]

\[
\boxed{
N_y^A(q,s)=-\left[\frac{P^A(q)}{b}+GQ_q(1-2s^2)\right],
}
\]

\[
\boxed{M_x^A(q,s)=J_x q s,\qquad M_y^A(q,s)=J_y q s.}
\]

Thus

\[
\mathbf d^A(q,s)=
[N_x^A,M_x^A,N_y^A,M_y^A]^T.
\]

The demand coordinate `q` is not promoted to a measured-deflection observable. The terminal coordinates `B_x,B_y` are not constrained to equal a curvature inferred from `q`.

For the frozen Airy family with `q0>0` and `C>0`,

\[
\frac{dP^A}{dq}
=\frac{P_{cr}q_0}{(q+q_0)^2}+2C(q+q_0)>0
\quad(q\ge0),
\]

so first contact along the admissible branch is equivalently the smallest admissible positive `q`.

---

## 2. Terminal section state

Use the common terminal section coordinates

\[
\boxed{\mathbf z_t=(A_x,A_y,B_x,B_y).}
\]

For the core,

\[
\varepsilon_x(z)=A_x+B_xz,
\qquad
\varepsilon_y(z)=A_y+B_yz.
\]

The steel-face centroid strains follow from the same terminal state at the face offsets. R02 local amplitudes, R06 radial projection factors and web branch variables are internal condensed variables; they are not new global deformation coordinates.

---

## 3. Phase resultant operators

### 3.1 UHPC core

For `i in {x,y}`,

\[
N_i^U(A_i,B_i)
=(1-\rho_w)\int_{-t_c/2}^{t_c/2}
\sigma_U(A_i+B_i z)\,dz,
\]

\[
M_i^U(A_i,B_i)
=(1-\rho_w)\int_{-t_c/2}^{t_c/2}
z\sigma_U(A_i+B_i z)\,dz.
\]

The already-frozen exact primitives are retained; no thickness quadrature is introduced.

### 3.2 External steel faces

For each face `f in {+,-}`:

1. obtain the common terminal face strain;
2. condense the existing R02 local amplitude from its finite cubic/minimum-energy rule;
3. classify by the intrinsic R06 selector `sigma_cr,s^E` versus `fy`;
4. yield-first: `R06 == R04` exactly;
5. local-buckling-first: if the full R02 local field exceeds yield, find the first radial local-Mises boundary from the complete finite algebraic candidate set and return the whole-width R02 mean resultant at that projected state.

The gross/full-area face resultants remain

\[
\mathbf N_f=t_s\bar{\boldsymbol\sigma}_f,
\qquad
\mathbf M_f=z_f\mathbf N_f
\]

with the appropriate signed face offset.

### 3.3 Longitudinal web

The frozen exact ideal-EP web resultant is retained. For the current BH architecture the web contributes the y-direction resultant/moment; if the parent phase definition assigns no x-resultant,

\[
N_x^w=M_x^w=0.
\]

### 3.4 Section assembly

\[
\boxed{
N_x^{sec}=N_x^U+N_{x,+}^s+N_{x,-}^s+N_x^w,
}
\]

\[
\boxed{
M_x^{sec}=M_x^U+M_{x,+}^s+M_{x,-}^s+M_x^w,
}
\]

\[
\boxed{
N_y^{sec}=N_y^U+N_y^w+N_{y,+}^s+N_{y,-}^s,
}
\]

\[
\boxed{
M_y^{sec}=M_y^U+M_y^w+M_{y,+}^s+M_{y,-}^s.
}
\]

---

## 4. Demand matching — the force-first bridge

For a prescribed Airy pair `(q,s)`, the terminal state must reproduce the complete resultant demand:

\[
\boxed{
\begin{aligned}
F_{Nx}&=N_x^{sec}(\mathbf z_t)-N_x^A(q,s)=0,\\
F_{Ny}&=N_y^{sec}(\mathbf z_t)-N_y^A(q,s)=0,\\
F_{Mx}&=M_x^{sec}(\mathbf z_t)-M_x^A(q,s)=0,\\
F_{My}&=M_y^{sec}(\mathbf z_t)-M_y^A(q,s)=0.
\end{aligned}}
\]

This is a force/resultant compatibility bridge, not a deformation-compatibility statement. In particular, no equation `B_i = kappa_i(q)` is added.

---

## 5. Terminal candidate registry

The registry must distinguish **outer plate endpoint candidates** from **internal constituent gates**.

### 5.1 Outer UHPC first-compression-peak candidates

The current SSUHPC production family uses first UHPC compression-peak contact as the outer active endpoint. Because the directional terminal strain is linear through thickness, the exhaustive face candidates for the two directional maps are

\[
\boxed{
g_{U,i,\delta}
=A_i+\delta\frac{t_c}{2}B_i+\varepsilon_{c0}=0,
\qquad i\in\{x,y\},\ \delta\in\{-1,+1\}.}
\]

Each candidate is admissible only with the corresponding face in compression and with no earlier registered endpoint already crossed. The use of the first compression peak is inherited from the frozen terminal architecture; it is not a claim that the Hu compression law ceases to exist beyond the peak.

For BH032 and BH050 the active candidate is

\[
\boxed{g_{U,y,-}=A_y-\frac{t_c}{2}B_y+\varepsilon_{c0}=0.}
\]

### 5.2 Steel R06 is an internal capacity/resultant gate, not automatically plate Pu

For a local-buckling-first face,

\[
g_{R06,f}(\eta)
=\max_{(u,v)\in[-1,1]^2}\Phi_f(u,v;\eta)-f_y^2=0
\]

defines the first radial local-yield projection when needed. It changes the face resultant returned to the four balance equations. It does **not**, by itself, terminate the global Airy demand path.

This distinction is required by the existing BH032/BH050 roots: the lower face is R06-local-yield active while the outer plate endpoint remains the UHPC compression-peak contact.

### 5.3 Web yielding is also an internal constitutive gate

The web ideal-EP yield front selects/caps the exact web resultant branch. It is not promoted to a plate ultimate condition unless a separate parent-theory rule explicitly registers such an endpoint.

### 5.4 UHPC tension

The frozen Hu tensile law remains available inside the local terminal N-M integral when a terminal section contains tension. The present source contract does not provide a separate tensile-failure plate endpoint to be added here. Therefore no new `g_t` is invented.

### 5.5 No local Jacobian singularity as plate endpoint

`det(Jsec)=0` is not an outer `g_a` in this architecture. The RC regressions already rejected local section singularity as a primary plate-Pu gate.

---

## 6. Control-location candidates

For a fixed Airy station endpoint `s=s_e` (e.g. `s=0` or `s=1`), each outer material candidate produces the finite five-equation system

\[
\boxed{
F_{Nx}=F_{Ny}=F_{Mx}=F_{My}=g_a=0
}
\]

in the five unknowns

\[
(A_x,A_y,B_x,B_y,q).
\]

If the controlling station is interior, `s` is added as an unknown and the existing terminal-contact stationarity condition `F_S=0` (same-source derivative of the contact load along the terminal manifold) must also be satisfied. No finite spatial sampling is substituted for this condition.

For the currently frozen BH032/BH050 branch the governing station is the endpoint

\[
\boxed{s=1.}
\]

---

## 7. Root enumeration and first-contact selection

For every registered outer candidate and every allowed control-location class:

1. solve the complete finite system for **all real roots**;
2. require `q>=0` and `P^A(q)>0`;
3. enforce UHPC branch/domain admissibility;
4. enforce the R02 nonnegative-real/minimum-energy local-amplitude rule;
5. enforce the intrinsic R06 branch selector and complete finite-algebraic local-Mises maximum certificate;
6. enforce the exact web branch/cap;
7. require all four resultant balance residuals within the prescribed algebraic/numerical solve tolerance;
8. do not use experiment/FEM/comparator information in root generation, filtering or selection;
9. because frozen `P^A(q)` is monotone for `q>=0`, select the admissible candidate with the smallest positive `q` (equivalently smallest positive `P^A`).

If several candidates occur at the same first-contact state, record them as co-active.

---

## 8. Mandatory output ledger

For every accepted root report:

```text
case
Airy candidate / control station
q_A, s, Pu=P^A(q_A)
Ax,Ay,Bx,By
active outer terminal candidate(s)
UHPC branch states
upper/lower R02 amplitude and R06 identity/projection status
web branch status
Nx_U,Ny_U,Mx_U,My_U
Nx_top,Ny_top,Mx_top,My_top
Nx_bottom,Ny_bottom,Mx_bottom,My_bottom
Nx_web,Ny_web,Mx_web,My_web
Nx_sec,Ny_sec,Mx_sec,My_sec
Nx_A,Ny_A,Mx_A,My_A
four balance residuals
```

For force sharing, the primary longitudinal local terminal-section ratio is

\[
\eta_{\phi}^{N_y}=\frac{N_{y,\phi}}{N_y^{sec}}.
\]

When all longitudinal phase resultants are compressive this is a direct positive compression share. If any phase is tensile, signed resultants must be shown and a naive percentage must not be interpreted as a gross compressive-force fraction.

For bending, because the two external-face offset moments can strongly cancel, report the combined external-face couple

\[
M_i^{faces}=M_{i,+}+M_{i,-}
\]

rather than misleading independent absolute percentages.

**Scope warning:** these are load shares at the governing terminal section. They are not global spatially integrated phase-load fractions over the entire halfwave.

---

# 9. BH032 force-first regression and phase ledger

The authoritative blind R06 execution already solved exactly the force-first five-equation system at `s=1`, so no new root or changed Airy equation is needed for this regression.

Frozen state:

\[
q_A=0.00137889961633743,
\qquad
\boxed{P_u=10.9405345132294\ \mathrm{MN}}.
\]

Direct Airy reevaluation with the frozen coefficients returns the same load.

Terminal coordinates:

\[
A_x=+1.60605822952534\times10^{-4},
\quad
B_x=2.07125070401497\times10^{-5}\ \mathrm{mm}^{-1},
\]

\[
A_y=-0.00249442810080108,
\quad
B_y=4.78843761523297\times10^{-5}\ \mathrm{mm}^{-1},
\]

with active

\[
A_y-21B_y=-0.0035.
\]

Airy demand:

\[
N_x^A=+37.4812947953\ \mathrm{N/mm},
\]

\[
N_y^A=-6798.60232003\ \mathrm{N/mm},
\]

\[
M_x^A=13412.3427833\ \mathrm N,
\qquad
M_y^A=13626.7706431\ \mathrm N.
\]

Exact phase resultants from the frozen execution:

UHPC

\[
N_x^U=+9.56201202007,
\quad
N_y^U=-4367.14036120\ \mathrm{N/mm},
\]

\[
M_x^U=2095.33545853,
\quad
M_y^U=11594.81057147\ \mathrm N.
\]

Web

\[
N_y^w=-293.194029786\ \mathrm{N/mm},
\qquad
M_y^w=+45.388284391\ \mathrm N.
\]

External steel-face total, obtained from the frozen exact section closure,

\[
N_x^{faces}=+27.91928277523\ \mathrm{N/mm},
\]

\[
N_y^{faces}=-2138.267929044\ \mathrm{N/mm},
\]

\[
M_x^{faces}=11317.00732477\ \mathrm N,
\qquad
M_y^{faces}=1986.571787239\ \mathrm N.
\]

The printed upper/lower R06 mean stresses imply, to printed precision,

\[
N_{y,+}\approx-1025.94762132,
\qquad
N_{y,-}\approx-1112.32030772\ \mathrm{N/mm}.
\]

The upper face remains uncapped R02 (`max VM = 317.237 MPa < fy`); the lower face is R06 local-yield projected with

\[
\eta_{y,-}=0.425379325768,
\qquad
\max\sigma_{VM,loc}=355\ \mathrm{MPa}.
\]

Longitudinal terminal-section compression shares:

```text
UHPC        = 64.2359 %
web         =  4.3126 %
steel faces = 31.4516 %
  upper     ≈ 15.0906 %
  lower     ≈ 16.3610 %
```

Moment allocation:

```text
Mx: UHPC 15.6224 %, external-face couple 84.3776 %
My: UHPC 85.0885 %, web 0.3331 %, external-face couple 14.5784 %
```

The four source execution balances close to order `1e-10` or better.

```text
BH032_FORCE_FIRST_REGRESSION = PASS
BH032_PHASE_RESULTANT_LEDGER = PASS
```

---

# 10. BH050 force-first regression and phase ledger

The authoritative blind BH050 execution also solved the same five-equation terminal system at `s=1`.

Frozen state:

\[
q_A=0.004772819645833164,
\qquad
\boxed{P_u=13.3563763545430\ \mathrm{MN}}.
\]

Direct Airy reevaluation with the frozen `Pcr,C,q0` returns the same load.

Terminal coordinates:

\[
A_x=+2.820431413\times10^{-5},
\quad
B_x=4.402758337803803\times10^{-5}\ \mathrm{mm}^{-1},
\]

\[
A_y=-0.00213545799,
\quad
B_y=6.497819104663830\times10^{-5}\ \mathrm{mm}^{-1},
\]

with active

\[
A_y-21B_y=-0.0035.
\]

Airy demand:

\[
N_x^A=+199.305955403735\ \mathrm{N/mm},
\]

\[
N_y^A=-5137.30935871948\ \mathrm{N/mm},
\]

\[
M_x^A=29756.6988970160\ \mathrm N,
\qquad
M_y^A=30060.7058605883\ \mathrm N.
\]

UHPC:

\[
N_x^U=-313.907222827064,
\quad
N_y^U=-3775.20864050157\ \mathrm{N/mm},
\]

\[
M_x^U=6458.07382899297,
\quad
M_y^U=16306.0755102416\ \mathrm N.
\]

Web:

\[
N_y^w=-170.904638861559\ \mathrm{N/mm},
\qquad
M_y^w=293.915178045378\ \mathrm N.
\]

External steel faces:

\[
N_x^{faces}=+513.213178230797\ \mathrm{N/mm},
\]

\[
N_y^{faces}=-1191.19607935637\ \mathrm{N/mm},
\]

\[
M_x^{faces}=23298.6250680230\ \mathrm N,
\qquad
M_y^{faces}=13460.7151723014\ \mathrm N.
\]

The frozen upper/lower mean stresses give

\[
N_{y,+}\approx-302.9737968,
\qquad
N_{y,-}\approx-888.2222826\ \mathrm{N/mm}.
\]

The upper face remains uncapped R02 (`max VM = 239.873 MPa < fy`); the lower face is R06 local-yield projected with

\[
\eta_{y,-}=0.38446506838,
\qquad
\max\sigma_{VM,loc}=355\ \mathrm{MPa}.
\]

Longitudinal terminal-section compression shares:

```text
UHPC        = 73.4861 %
web         =  3.3267 %
steel faces = 23.1872 %
  upper     ≈  5.8975 %
  lower     ≈ 17.2896 %
```

Moment allocation:

```text
Mx: UHPC 21.7029 %, external-face couple 78.2971 %
My: UHPC 54.2438 %, web 0.9777 %, external-face couple 44.7784 %
```

The source execution reports all four resultant balances closing to about `1e-11` or better.

```text
BH050_FORCE_FIRST_REGRESSION = PASS
BH050_PHASE_RESULTANT_LEDGER = PASS
```

---

# 11. Immediate mechanical interpretation from the force ledger

The two cases do not merely differ in predicted Pu; their terminal force allocation changes substantially:

1. BH032 longitudinal compression at the governing section is approximately `64.2% UHPC / 31.5% external faces / 4.3% web`.
2. BH050 shifts to approximately `73.5% UHPC / 23.2% external faces / 3.3% web`.
3. The BH050 upper face carries much less longitudinal compression than the BH032 upper face, while the lower face remains strongly compression-bearing and R06-local-yield active.
4. The y-bending share carried by the external-face couple rises from about `14.6%` in BH032 to about `44.8%` in BH050; the UHPC y-bending share correspondingly falls from about `85.1%` to about `54.2%`.
5. Thus BH050's different response is already visible in the force/resultant partition itself; no deformation mismatch is needed to identify that change.

These observations are theory-output diagnostics, not comparator-based calibration.

---

# 12. Validation boundary

This execution establishes **internal force closure and phase allocation**, not experimental truth of the phase allocation.

```text
Pu source-blind regression identity        = PASS
four-resultant terminal closure            = PASS
phase resultant extraction BH032/BH050     = PASS
FEM/test used in root selection             = NO
phase-sharing external measurement check    = NOT EXECUTED / NO SUCH SOURCE USED HERE
deflection/curvature fidelity gate          = DISABLED BY CURRENT OBJECTIVE
production changed                          = NO
```

If later validation data for constituent forces/stresses are used, they are post-checks only and may diagnose whether the error lies primarily in the Airy total demand or in the terminal phase allocation. They may not be used to fit a correction factor into this R01 system.

---

# 13. Status

```text
FORCE_FIRST_AIRY_TERMINAL_ARCHITECTURE = CLOSED
AIRY_DEMAND = RETAINED
TERMINAL_AX_AY_BX_BY = RETAINED_AS_CAPACITY_COORDINATES
Q_AS_PHYSICAL_DEFLECTION_REQUIREMENT = OFF
Q_TO_TERMINAL_CURVATURE_EQUALITY = OFF
R06 = INTERNAL FACE RESULTANT CAPACITY GATE
WEB_YIELD = INTERNAL CONSTITUTIVE GATE
OUTER_CURRENT_BH_ENDPOINT = UHPC_FIRST_COMPRESSION_PEAK CONTACT
LOCAL_detJsec_AS_Pu = PROHIBITED
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
BH032_FORCE_LEDGER = PASS
BH050_FORCE_LEDGER = PASS
PRODUCTION_PROMOTION = NOT PERFORMED
```
