# NZ-SCCM — Panel1/14/21 source-waveform two-slope full-2D material-limit diagnostic

**Time:** 2026-08-22 19:27 +08:00  
**Status:** `EXECUTED / TWO_SLOPE_SECTION_INTERFACE_PASS / SOURCE_WAVEFORM_FIXED / MATERIAL_FUNCTIONS_UNCHANGED / MATERIAL_DIAGNOSTIC_EVENTS_RESOLVED / NOT_PRODUCTION_Pu`

## 0. Purpose and hard boundary

This execution performs exactly the previously authorized step:

\[
(\lambda_{t0},\lambda_{c0},\chi)
\quad\longrightarrow\quad
(a_x,a_y,b_x,b_y)
\]

with two independent affine through-thickness material coordinates,

\[
\boxed{\lambda_x(z)=a_x+b_xz,\qquad \lambda_y(z)=a_y+b_yz.}
\]

The material functions themselves are not changed. The prescribed Nguyen source-waveform representations for Panels 1, 14 and 21 are also unchanged.

The purpose is not to predict the irregular waveform. The waveform is treated as an exogenous casting/initial-imperfection geometry input and is used to expose the full biaxial bending material state.

```text
OBSERVED_WAVEFORM = PRESCRIBED_INPUT
SELF_GROWN_WAVEFORM = OFF
MATERIAL_FUNCTIONS_CHANGED = FALSE
MATERIAL_PARAMETER_REFIT = FALSE
Pf_IN_ROOT_SELECTION = 0
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
```

The reported theoretical loads below are **current-map terminal/material-diagnostic events under the frozen current material law**. They are not promoted as final production ultimate loads because this audit is specifically intended to identify where the current material constraints fail.

---

# 1. Frozen source waveforms

The normalized longitudinal source-wave shapes remain:

\[
\Phi_1(u)=1.04276809\sin\pi u-0.09582984\sin2\pi u+0.08299371\sin3\pi u,
\]

\[
\Phi_{14}(u)=1.05654776\sin\pi u-0.03901107\sin2\pi u+0.06242867\sin3\pi u,
\]

\[
\Phi_{21}(u)=-0.12203066\sin\pi u-0.76471804\sin2\pi u+0.18158893\sin3\pi u+0.25675995\sin4\pi u,
\]

with

\[
u=y/a,\qquad a=2440\ \mathrm{mm},\qquad b=1220\ \mathrm{mm}.
\]

No waveform coefficient is identified from failure load.

The generalized explicit structural front end remains

\[
\boxed{
P_\Phi(q)=P_{cr,\Phi}\frac{q}{q+q_0}+C_\Phi q(q+2q_0)
}
\]

with the full source-wave resultants

\[
N_x,\ N_y,\ N_{xy},\ M_x,\ M_y,\ M_{xy}.
\]

All three controlling sections in the present audit occur at the transverse centre `s=1`, where

\[
N_{xy}=M_{xy}=0,
\]

so the full normal-bending section demand is the four-vector

\[
\boxed{\mathbf r_d=(N_x,N_y,M_x,M_y)^T.}
\]

---

# 2. Two-independent-slope phase-compatible section interface

The physical strains corresponding to the current plane-stress material coordinates are

\[
\boxed{
\varepsilon_x(z)=\varepsilon_0[\lambda_x(z)-\nu\lambda_y(z)]
}
\]

and

\[
\boxed{
\varepsilon_y(z)=\varepsilon_0[\lambda_y(z)-\nu\lambda_x(z)].
}
\]

Thus the four section variables

\[
\boxed{(a_x,a_y,b_x,b_y)}
\]

can independently carry the two membrane strains and the two normal curvatures required by `Nx,Ny,Mx,My`.

The section equilibrium is

\[
\boxed{
\begin{aligned}
N_x^{sec}(a_x,a_y,b_x,b_y)&=N_x^d(q,u),\\
N_y^{sec}(a_x,a_y,b_x,b_y)&=N_y^d(q,u),\\
M_x^{sec}(a_x,a_y,b_x,b_y)&=M_x^d(q,u),\\
M_y^{sec}(a_x,a_y,b_x,b_y)&=M_y^d(q,u).
\end{aligned}}
\]

The reinforcement phases share the compatible physical strains. Concrete displaced by each reinforcement layer is explicitly subtracted, and x/y reinforcement stresses are evaluated in their own directions using the unchanged elastic-perfectly-plastic steel law.

---

# 3. Exact no-quadrature affine section primitives

For either material coordinate

\[
\lambda(z)=a+bz,
\]

all current scalar NC branch fronts are affine roots in z. The finite front set used here is

\[
\lambda=-10,-1,0,x_{cr},10x_{cr},
\qquad
x_{cr}=\frac{f_t}{E_0\varepsilon_0}.
\]

The current material functions are unchanged:

- compression: Saenz ascending branch, current bounded postpeak line to `0.1fc` at `lambda=-10`, then residual;
- tension: elastic to cracking, Foster finite softening with `alpha1=10`, `alpha2=0.3`, then `0.3ft` residual;
- `ft=0.1fc` remains the current common Swartz tensile-input assumption.

Every subinterval therefore has an elementary primitive. Saenz requires only the usual finite `log/atan` rational primitive; all remaining branches are polynomial/linear.

Consequently

\[
N=\int_{-h}^{h}\sigma(a+bz)\,dz,
\qquad
M=\int_{-h}^{h}z\sigma(a+bz)\,dz
\]

are evaluated exactly after a finite branch-front split. No through-thickness Gauss/material-point rule is used.

## 3.1 Same-law exact Jacobian

The section Jacobian is also not formed by numerical differentiation. For

\[
N(a,b)=\int_{-h}^{h}\sigma(a+bz)\,dz,
\qquad
M(a,b)=\int_{-h}^{h}z\sigma(a+bz)\,dz,
\]

define endpoint stresses

\[
\sigma_- = \sigma(a-bh),\qquad \sigma_+=\sigma(a+bh).
\]

Then for `b != 0`:

\[
\boxed{N_{,a}=\frac{\sigma_+-\sigma_-}{b}},
\]

\[
\boxed{N_{,b}=M_{,a}=\frac{h(\sigma_++\sigma_-)-N}{b}},
\]

\[
\boxed{M_{,b}=\frac{h^2(\sigma_+-\sigma_-)-2M}{b}}.
\]

The `b -> 0` limits are supplied directly from the same material tangent. Reinforcement derivative terms are added analytically with the same active-set steel law.

Thus the four-dimensional phase-compatible section has a same-law analytic Jacobian while preserving

```text
N_formal_spatial_quadrature = 0
N_material_points = 0
```

---

# 4. Event definition

For a fixed longitudinal source-wave location u, the origin-connected section equilibrium branch is followed algebraically in q. A current-map section fold satisfies

\[
\boxed{\det\mathbf J_{sec}=0.}
\]

The controlling u is then localized by the stationarity of the finite event root in u. This is a scalar location optimization, not a spatial quadrature or material grid.

If a steel active-set boundary terminates the origin-connected branch before a concrete/current-map fold, that event is retained explicitly instead of forcing a continuation through an inadmissible active set.

No experimental load is used in either event definition.

---

# 5. Main results

|Panel|controlling u|q_event|current theoretical event|P_event / kN|Pf / kN|post-solution error|
|---:|---:|---:|---|---:|---:|---:|
|1|0.63783259|0.001528057|current-map section fold|**589.0817**|490.1940|**+20.173%**|
|14|0.74558237|0.000934579|lower y-rebar compression-yield active-set terminal|**770.5483**|716.1637|**+7.594%**|
|21|0.35726580|0.001585108|current-map section fold|**192.6906**|368.3127|**−47.683%**|

These are diagnostic terminal events under the current material functions, not a newly calibrated Pu set.

---

# 6. Panel 1 — TC/postcrack interaction becomes the primary concrete diagnostic

At the current-map fold:

\[
\boxed{P_{event,1}=589.0817\ \mathrm{kN}}
\]

and

\[
(a_x,a_y,b_x,b_y)
\approx
(0.0520240,-0.5175504,0.0141352,0.00585784).
\]

The structural demand is approximately

\[
(N_x,N_y,M_x,M_y)
=(+6.034,-480.905,+395.774,+166.433).
\]

The two concrete coordinate fields run across the faces as

\[
\lambda_x:\ -0.12749\to+0.23154,
\]

\[
\lambda_y:\ -0.59195\to-0.44316.
\]

Hence the equilibrated thickness topology is

\[
\boxed{CC\to TC}
\]

with no TT zone.

The current TC-R2 compression-softening factor activates only when

\[
\lambda_t>10/17\approx0.588235.
\]

The maximum tensile material coordinate at the fold is only

\[
\boxed{\lambda_{t,max}\approx0.23154<0.588235},
\]

so

\[
\boxed{\gamma_c=1\quad\text{everywhere at the terminal state}.}
\]

In other words, the current TC-R2 compression weakening is completely inactive throughout the Panel1 diagnostic branch up to its fold.

At the exact tensile cracking front `lambda_x=x_cr`, the Nguyen/Foster source TC transition measure on the tension-axis segment is approximately

\[
\boxed{\Phi_{TC}\approx1.4086>1.}
\]

so the section has long crossed the source TC cracking/transition boundary before the current-map fold.

The singular section-Jacobian mode is approximately

\[
\boxed{(-1.000,-0.0071,-0.1392,+0.00013)},
\]

in `(a_x,a_y,b_x,b_y)` order. Thus the fold is overwhelmingly controlled by the **transverse tensile section tangent**, not by longitudinal compression.

## 6.1 Post-solution check at the measured failure load

Only after the theoretical event is fixed, insert the measured load

\[
P_f=490.194\ \mathrm{kN}
\]

into the already-fixed structural relation. It corresponds to

\[
q\approx0.001159407.
\]

The full two-slope section equilibrium still exists and gives approximately

\[
(a_x,a_y,b_x,b_y)
=(0.003880,-0.392393,0.005152,0.003191).
\]

At the tensile cracking front,

\[
\boxed{\Phi_{TC}\approx1.3213>1},
\]

while the maximum positive material coordinate is only about `0.069`, still far below the current `gamma_c` activation threshold.

### Panel1 diagnostic conclusion

The observed waveform plus the complete two-slope section does **not** remove the overprediction. More importantly, it shows exactly where the present TC treatment is weak:

\[
\boxed{
\text{source TC cracking state is already strongly active}
\quad\text{but current TC-R2 compression degradation remains exactly zero.}
}
\]

Therefore the next NC material audit should examine **postcrack TC coupling / compression degradation tied to the current cracked-TC state**, rather than only the present high tensile-strain threshold `lambda_t>10/17`.

No new TC coefficient is fitted in this execution.

---

# 7. Panel 14 — current terminal is a steel active-set event, not a clean concrete test

The first origin-connected terminal is

\[
\boxed{P_{event,14}=770.5483\ \mathrm{kN}}
\]

at

\[
(a_x,a_y,b_x,b_y)
\approx
(-0.015557,-1.180213,0.004197,0.019734).
\]

The concrete face coordinates are approximately

\[
\lambda_x:\ -0.08325\to+0.05213,
\]

\[
\lambda_y:\ -1.49852\to-0.86190,
\]

so the thickness state is

\[
\boxed{CC\to TC},
\]

again with no TT zone.

The maximum positive coordinate is only

\[
0.05213<0.588235,
\]

so TC-R2 gamma softening is inactive here as well.

However the terminal is controlled by the lower longitudinal reinforcement layer at

\[
z=-12.63\ \mathrm{mm}
\]

reaching

\[
\boxed{\sigma_{sy}=-530\ \mathrm{MPa}}.
\]

The upper y-rebar remains at approximately `-350.7 MPa`.

A one-sided active-set audit of the lower-bar yield function gives approximately

\[
\frac{dh}{dq}\bigg|_{elastic}\approx+4.57\times10^6,
\]

\[
\frac{dh}{dq}\bigg|_{capped}\approx-5.06\times10^6.
\]

Thus the perfect-plastic capped continuation points back across its own yield surface. This is an active-set topology/kink problem in the reduced steel section law, analogous in character to the earlier steel-face active-set issue.

### Panel14 diagnostic conclusion

Panel14 cannot presently be used as a clean CC/TC concrete discriminator because the steel active-set boundary intervenes first.

At its measured load `716.164 kN`, the reconstructed section remains primarily CC with only a near-tension face and the lower y-bar has not yet reached the terminal yield boundary. The remaining `+7.6%` theoretical terminal difference is therefore not sufficient evidence to modify the NC CC envelope.

---

# 8. Panel 21 — full equilibrium removes the earlier TT diagnosis and exposes a severe transverse-tension deficiency

The origin-connected current-map fold occurs at

\[
\boxed{P_{event,21}=192.6906\ \mathrm{kN}}
\]

with

\[
(a_x,a_y,b_x,b_y)
\approx
(0.085708,-0.180567,-0.024585,-0.013369).
\]

The coordinate fields across the faces are

\[
\lambda_x:\ +0.32295\to-0.15154,
\]

\[
\lambda_y:\ -0.05155\to-0.30958.
\]

Therefore the **equilibrated** thickness topology at the actual current-map terminal is

\[
\boxed{TC\to CC},
\]

not the earlier elastic-recovery diagnostic `CC -> TC -> TT`.

This is an important correction:

```text
PANEL21_TT_AT_ELASTIC_RECOVERY_DIAGNOSTIC = YES
PANEL21_TT_AT_FULL_TWO_SLOPE_EQUILIBRATED_TERMINAL = NO
```

The maximum tensile coordinate is

\[
0.32295<0.588235,
\]

so current TC-R2 gamma compression softening is again inactive.

At the tensile cracking front,

\[
\Phi_{TC}\approx1.1923>1.
\]

The singular section-Jacobian mode is approximately

\[
\boxed{(+1.000,+0.0140,-0.1803,+0.0002)},
\]

again overwhelmingly dominated by the **transverse tensile material coordinate/tangent**.

The mid-plane rebars are still elastic at the fold, approximately

\[
\sigma_{sx}\approx+49.4\ \mathrm{MPa},
\qquad
\sigma_{sy}\approx-81.9\ \mathrm{MPa}.
\]

## 8.1 Post-solution check at the measured failure load

The measured load

\[
P_f=368.313\ \mathrm{kN}
\]

corresponds, through the already-fixed source-wave structural relation, to approximately

\[
q(P_f)=0.00553715.
\]

There is **no origin-connected equilibrium of the frozen current two-slope material section at this q**. The current map has already folded near `192.69 kN`.

Thus Panel21 is not a small calibration discrepancy. Under the observed-wave geometry, the current transverse-tension section law loses admissibility far too early.

### Panel21 diagnostic conclusion

This panel has a high reinforcement ratio (`p=0.0075`) while Panel1 has `p=0.0020`. The source/mechanism audit already records that Foster's postcrack tension-stiffening parameter `alpha2` is reinforcement-dependent, whereas the current project uses the same conservative `alpha2=0.3` for all Swartz panels while modelling the steel explicitly.

The severe Panel21 underprediction, together with its tension-dominated Jacobian null mode, therefore gives strong evidence to reopen

\[
\boxed{\text{reinforcement/bond-dependent NC tension stiffening}}
\]

as a material constraint/input issue.

This audit does **not** choose a new `alpha2` and does not infer it from `Pf`.

---

# 9. What the three panels collectively say about CC / TC / TT

The observed-waveform, full-two-slope diagnostic changes the priority ordering substantially.

## 9.1 TT — do not reopen first

The earlier one-way elastic material-coordinate recovery suggested Panel21 crossed `CC -> TC -> TT`. Once full two-slope phase equilibrium is solved, Panel21's actual origin-connected terminal is `TC -> CC` and contains no TT region.

Therefore:

```text
TT_AS_PRIMARY_MISSING_CONSTRAINT = NOT_SUPPORTED_BY_CURRENT_3PANEL_AUDIT
```

TT remains required in the general material family, but it is not the first explanation for the present three-panel failure pattern.

## 9.2 CC — no present evidence for a CC retune

Panel14 contains strong CC/postpeak coordinates, but its branch is terminated first by the longitudinal reinforcement active-set kink. Panels1/21 are transverse-tension tangent controlled.

Therefore:

```text
NC_CC_REOPEN_FROM_THIS_AUDIT = NO
```

## 9.3 TC — missing cracked-state interaction is directly exposed by Panel1

Panel1 is the cleanest evidence that the current TC-R2 rule is too late to activate its compression weakening. The source TC state is already substantially beyond its cracking/transition boundary at the measured failure load while `gamma_c` remains exactly 1.

Thus:

```text
NC_TC_POSTCRACK_INTERACTION_BEFORE_GAMMA_ONSET = PRIMARY_OPEN_MATERIAL_ISSUE
```

## 9.4 Reinforcement-dependent tensile stiffening — strongly exposed by Panel21

The current universal `alpha2=0.3` is source-conservative but suppresses the source dependence on reinforcement/bond. Panel21's very early transverse-tension fold under high reinforcement ratio makes this the second primary material issue.

Thus:

```text
NC_TENSION_STIFFENING_REINFORCEMENT_DEPENDENCE = PRIMARY_OPEN_MATERIAL_ISSUE
```

## 9.5 Steel active-set topology — Panel14 must be separated from concrete diagnosis

Panel14 terminates at a longitudinal rebar compression-yield active-set kink. Concrete material conclusions from this panel are therefore blocked until the reduced steel redistribution/current-law representation is made admissible through the yield event.

---

# 10. Relation to the previous source-wave 1D capacity values

Previous source-wave 1D capacity roots were:

|Panel|previous source-wave 1D / kN|full-two-slope diagnostic event / kN|change in numerical level|
|---:|---:|---:|---:|
|1|676.103|589.082|−12.87%|
|14|738.319|770.548|+4.36%|
|21|327.924|192.691|−41.24%|

These are **not** a uniform `2D correction factor`. The former values were parabolic one-dimensional N-M capacity roots; the latter are terminal events of the frozen two-slope current material section. They are shown only to quantify how strongly the omitted transverse-bending dimension mattered.

---

# 11. Decision

```text
TWO_INDEPENDENT_AFFINE_SLOPE_SECTION_INTERFACE = PASS
FULL_NORMAL_BENDING_Nx_Ny_Mx_My = INCLUDED
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
MATERIAL_FUNCTIONS_CHANGED = FALSE
MATERIAL_PARAMETER_REFIT = FALSE

PANEL1_EVENT = CURRENT_MAP_SECTION_FOLD
PANEL1_EVENT_LOAD = 589.0817 kN
PANEL1_ERROR_VS_Pf = +20.173%
PANEL1_PRIMARY_DIAGNOSTIC = TC_POSTCRACK_INTERACTION_MISSING_BEFORE_CURRENT_GAMMA_ONSET

PANEL14_EVENT = LOWER_Y_REBAR_COMPRESSION_YIELD_ACTIVESET_TERMINAL
PANEL14_EVENT_LOAD = 770.5483 kN
PANEL14_ERROR_VS_Pf = +7.594%
PANEL14_CONCRETE_DIAGNOSTIC = BLOCKED_BY_REBAR_ACTIVESET

PANEL21_EVENT = CURRENT_MAP_SECTION_FOLD
PANEL21_EVENT_LOAD = 192.6906 kN
PANEL21_ERROR_VS_Pf = -47.683%
PANEL21_TT_AT_EQUILIBRATED_TERMINAL = NO
PANEL21_PRIMARY_DIAGNOSTIC = TRANSVERSE_TENSION_STIFFENING_TOO_WEAK / REINFORCEMENT_DEPENDENCE_MISSING

TC_R2_GAMMA_ACTIVE_AT_TERMINALS = NO_ALL_3
TT_REOPEN_PRIORITY = LOW_FROM_CURRENT_3PANEL_EVIDENCE
CC_REOPEN_PRIORITY = LOW_FROM_CURRENT_3PANEL_EVIDENCE
PRIMARY_MATERIAL_REOPEN_1 = REINFORCEMENT_DEPENDENT_TENSION_STIFFENING
PRIMARY_MATERIAL_REOPEN_2 = POSTCRACK_TC_INTERACTION_BEFORE_GAMMA_ONSET
STEEL_REBAR_ACTIVESET_REPRESENTATION = OPEN_FOR_PANEL14
```

The next material task should therefore **not** be a global constitutive retune. It should be a source-only audit of two narrowly identified NC mechanisms:

1. restore/quantify the Foster reinforcement/bond dependence of tension stiffening without using panel failure loads;
2. examine whether the current TC-R2 compression weakening should begin from a cracked-TC measure/state rather than only after `lambda_t>10/17`.

Panel14's rebar active-set topology should be treated separately as a structural phase-current-law issue.

Reproduction script:

`semantic_v2/40_execution/rc/20260822_1927__NZSCCM__PANEL1_14_21_TWO_SLOPE_FULL2D_SECTION_DIAGNOSTIC.py`
