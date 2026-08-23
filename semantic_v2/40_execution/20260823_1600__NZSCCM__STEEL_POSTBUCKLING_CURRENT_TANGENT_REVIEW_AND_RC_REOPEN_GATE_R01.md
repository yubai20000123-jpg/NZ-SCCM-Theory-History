# NZ-SCCM — steel postbuckling current-tangent review and RC reopen gate R01

**Time:** 2026-08-23 16:00 +08:00  
**Status:** `LITERATURE_REVIEW / REOPEN_GATE / DIAGNOSTIC_ONLY / NO_CURRENT_STATE_CHANGE / NO_SWARTZ_Pu_EXECUTION`

## 0. Correction of the previous narrow route

The preceding Attard-inspired transverse-gate route is not adopted as the next production step. In particular, Attard's `E_t,transverse≈0.4Ec` is a simplifying cracked-transverse assumption for his approximate analytical model and is **not** transferred into NZ-SCCM. No transverse stiffness/restraining coefficient may be fitted or prescribed without specimen/source closure.

The present review instead asks a broader question: how do mature steel plate/stiffened-plate methods actually carry a plate from elastic buckling through postbuckling, plastic redistribution and ultimate load, and can the same architecture be transplanted to RC using the already available Nguyen/Foster constitutive tangent plus Zhou/Navier orthotropic plate skeleton?

The answer is: `YES IN PRINCIPLE`. The previous difficulty was architectural, not a proof of impossibility.

---

## 1. Two distinct traditions in steel plated-structure postbuckling

### 1.1 Elastic large-deflection + external strength criterion

Examples include PULS-type and several simplified semi-analytical formulations. The nonlinear plate equilibrium is solved geometrically, but material plasticity is not fully embedded in the governing plate equilibrium. Ultimate strength is estimated by a membrane-yield or other collapse criterion.

This family is useful for design but is **not** the closest analogue to the user's proposed RC route.

### 1.2 Elastic-plastic large-deflection equilibrium path

The closer analogue is the Ueda–Rashed–Paik incremental Galerkin line and later Paik/Lee ALPS-SPINE development.

Key features:

1. initial imperfection is retained;
2. large-deflection plate equations supply geometric nonlinearity;
3. current plastic state is updated as load grows;
4. current stiffness/equilibrium is re-formed after material yielding;
5. the equilibrium path is continued into the postbuckling/plastic range;
6. the ultimate load is obtained from the global load-carrying response rather than first local yield alone.

Paik/Lee explicitly describe simultaneous geometric and material nonlinear governing equations as difficult but not impossible; their practical semi-analytical method treats geometric nonlinearity analytically and progressing plasticity numerically.

Thus steel plate theory provides direct precedent for

\[
\text{current constitutive state}\to\text{current tangent stiffness}\to\text{redistributed plate equilibrium}\to\text{global ULS}.
\]

---

## 2. Why first yield/local material events are not automatically ULS in steel

Brubak–Hellesland show that stiffened plates may continue to carry increasing load after outer-fibre yielding because plastic zones and membrane stresses redistribute. Their semi-analytical equilibrium path is traced through the postbuckling range; simplified yield criteria are approximations to the true limit point, not a general identity `first yield = Pu`.

The full elastic-plastic Galerkin/FEM tradition goes further: plasticity participates in the current equilibrium and stiffness, so the load maximum can emerge naturally from the coupled material-geometric response.

This distinction mirrors the RC problem: crack onset, concrete peak strain, crushing onset and bar yield should primarily update the current constitutive state/tangent unless a source-defined terminal failure occurs.

---

## 3. Direct RC precedent already exists: Attard and Nguyen tangent stiffness

Attard's RC-wall buckling equation is already written with orthotropic **tangent bending rigidities** rather than fixed elastic rigidities. His scalar transverse `0.4Ec` treatment is merely one approximate closure and is not required by the tangent-rigidity architecture itself.

Nguyen Chapter 4 is stronger. The full nonlinear-material RC stability formulation constructs a current material tangent contribution and a current-stress geometric/stability contribution, schematically

\[
\boxed{K_T=K_{mat}+K_{geo}}.
\]

The second variation and stability problem use the current concrete tangent (including cracked-direction/dilation effects) plus current membrane forces. Reinforcement has corresponding tangent/stability contributions.

Therefore a nonlinear RC plate with current tangent stiffness is not a speculative analogy imported from steel; it is already present in the Nguyen source at FE level.

The open project question is how to **project this current-tangent physics onto the low-dimensional Zhou/Navier/Marguerre analytical backbone without reverting to formal spatial material-point discretization**.

---

## 4. Correct role of Zhou Siming in the reopened path

Zhou supplies the four-edge simply-supported orthotropic plate stiffness language and Navier modal skeleton. In the elastic orthotropic degeneration, the modal bending contribution has the familiar form

\[
D_x\alpha^4+2H\alpha^2\beta^2+D_y\beta^4.
\]

For nonlinear material this should not be interpreted as 'replace E by one scalar Et'. The correct generalization is tensorial.

Given the current plane-stress material tangent

\[
\mathbb C_t=\frac{\partial\boldsymbol\sigma}{\partial\boldsymbol\varepsilon},
\]

form current generalized section tangents

\[
\boxed{A_t=\int \mathbb C_t\,dz},
\qquad
\boxed{B_t=\int z\mathbb C_t\,dz},
\qquad
\boxed{D_t^{sec}=\int z^2\mathbb C_t\,dz},
\]

including discrete reinforcement contributions and phase-volume correction.

Important consequences:

- initially symmetric sections have `B=0`, but asymmetric cracking/crushing through thickness may produce `B_t != 0`;
- rotating principal cracking can produce current coupling terms analogous to `D16,D26`; therefore the simple global-axis `Dx-Dy-H` form is a degeneration/check, not necessarily the complete current tangent;
- when the current tangent remains globally orthotropic, the projected modal stiffness reduces back to the Zhou form.

Thus Zhou should be the **modal projection / elastic-degeneration skeleton**, not a separate empirical ultimate-load solver.

---

## 5. Proposed common RC current-tangent postbuckling architecture

This is a reopen gate, not yet the production theory.

### 5.1 Kinematics

Retain the source-supported initial imperfection/waveform and Marguerre/von-Karman second-order geometry. Use a low-dimensional generalized coordinate vector, initially

\[
\mathbf z=(\delta,q)
\]

for axial shortening/control and one current source-supported out-of-plane amplitude; finite additional modal amplitudes are allowed only if source/equilibrium evidence requires them.

### 5.2 Current material operator

At the current strain state,

\[
\boldsymbol\sigma=\mathcal M(\boldsymbol\varepsilon;H),
\qquad
\mathbb C_t=\frac{\partial\boldsymbol\sigma}{\partial\boldsymbol\varepsilon},
\]

using the same Nguyen/Foster NC states and reinforcement law. Crack/crush/yield events change `M` and `C_t`; they do not automatically terminate the plate.

No `0.4Ec`, no fitted transverse coefficient, and no specimen-dependent material retuning.

### 5.3 Current resultants

\[
\mathbf N=\int\boldsymbol\sigma\,dz+\mathbf N_s,
\qquad
\mathbf M=\int z\boldsymbol\sigma\,dz+\mathbf M_s.
\]

These are current nonlinear resultants, not resultants from an initial-elastic Airy field followed by an independent terminal section check.

### 5.4 Structural residual

Construct the finite Galerkin/virtual-work residual

\[
\boxed{\mathbf R(\delta,\mathbf q)=0}
\]

from the current stresses/resultants and current geometry. This is the semi-analytical counterpart of the steel incremental Galerkin equilibrium and of Nguyen's nonlinear FE residual.

### 5.5 Consistent structural tangent

\[
\boxed{K_{ij}=\frac{\partial R_i}{\partial q_j}=K_{mat,ij}+K_{geo,ij}}
\]

where the material term is generated from the same current `C_t`, and the geometric term from the same current stresses/resultants. This is the low-dimensional analogue of Nguyen's `Ke+Se` and the tangent-stiffness structure used in nonlinear steel plate analysis.

The Zhou/Navier expression is recovered in the elastic orthotropic limit.

### 5.6 Current reaction

The axial reaction is recovered from current stress resultants,

\[
\boxed{P=P(\delta,\mathbf q)}.
\]

Therefore material softening/plasticity can reduce reaction even while geometric amplitude grows.

### 5.7 Ultimate load

The physical ultimate load is the maximum reaction on an admissible equilibrium branch,

\[
\boxed{P_u=\max_{\mathbf R=0}P}.
\]

For one modal amplitude `q`, a direct non-incremental peak solve is possible. If

\[
R(\delta,q)=0,
\]

then along equilibrium

\[
\frac{dq}{d\delta}=-\frac{R_\delta}{R_q}.
\]

Hence

\[
\frac{dP}{d\delta}=P_\delta-P_q\frac{R_\delta}{R_q}.
\]

The regular-branch peak condition is therefore

\[
\boxed{L=P_\delta R_q-P_qR_\delta=0}.
\]

A production candidate can thus solve directly

\[
\boxed{R(\delta,q)=0,\qquad L(\delta,q)=0}
\]

and set

\[
P_u=P(\delta,q).
\]

This preserves the project objective of avoiding hundreds of load increments while retaining the same physics as an incrementally traced steel elastic-plastic equilibrium path.

A tangent singularity `R_q=0` is a bifurcation/limit event and must be handled by the corresponding bordered system; it is not automatically the global `Pu` because a postbuckling branch may continue.

---

## 6. Transverse restraint must come from boundary conditions, not a coefficient

The current in-plane transverse response must be solved from the actual Swartz support/loading boundary conditions and equilibrium/compatibility. No full transverse restraint is assumed unless the source says so.

Thus transverse membrane strain/resultant becomes either:

- a generalized unknown constrained by zero/external transverse resultant, or
- a quantity determined by the exact in-plane kinematic boundary condition.

The nonlinear material tangent then generates the current Poisson/dilation coupling naturally.

---

## 7. Why previous project routes failed without proving this route impossible

1. fixed elastic Airy backbone prevented material cracking/crushing from redistributing the structural demand;
2. terminal `N-M` or attempted 4D capacity contact forced local-section failure logic onto a global postbuckling problem;
3. `det Jsec=0` confused a local section singularity with plate ultimate;
4. treating `Mx` as an independent transverse beam-section capacity over-penalized a plate bending field;
5. demanding a closed-form ultimate result before closing the current constitutive tangent made the material nonlinearity appear structurally intractable.

Steel incremental Galerkin/GMNIA and Nguyen Chapter 4 show that none of these difficulties is a theorem of impossibility.

---

## 8. Validation governance

No panel, including Case21, is allowed to identify a private rule.

First validation set remains the accepted common-analysis set

\[
\boxed{4,5,6,8,9,14,21,23}.
\]

The same material operator, tangent construction, boundary-condition treatment and root/peak rule must be applied to all eight.

Required group gates include:

- no use of `Pf` in coefficient/root selection;
- Case5/6 near-pair consistency;
- no degradation of valid wavelength evidence;
- all excluded/high-scatter panels remain secondary robustness checks rather than fitting targets.

---

## 9. Reopen decision

```text
FOUR_DIMENSIONAL_SECTION_CAPACITY_SURFACE = PAUSED / NOT_REQUIRED
ATTARD_0P4Ec_TRANSVERSE_MODULUS = DO_NOT_IMPORT
PULS_MEMBRANE_YIELD_SHORTCUT = NOT_THE_TARGET_ANALOGUE
STEEL_INCREMENTAL_GALERKIN_ELASTOPLASTIC_PATH = PRIMARY_ARCHITECTURAL_PRECEDENT
NGUYEN_CURRENT_MATERIAL_TANGENT_PLUS_GEOMETRIC_STIFFNESS = DIRECT_RC_PRECEDENT
ZHOU_NAVIER_ORTHOTROPIC_STIFFNESS = ELASTIC_DEGENERATION_AND_MODAL_PROJECTION_SKELETON
CURRENT_MATERIAL_FEEDBACK_TO_GLOBAL_EQUILIBRIUM = REOPEN_FOR_GATE
GLOBAL_PEAK_REACTION = TARGET_Pu_DEFINITION
DIRECT_R_EQ_0_PLUS_L_EQ_0_PEAK_SOLVE = NEXT_ANALYTIC_GATE
SWARTZ8_COMMON_VALIDATION = REQUIRED
CURRENT_STATE_FILE = NOT_CHANGED
```

The next task is not a Case21 calculation. It is to derive the **single-common low-dimensional residual/tangent/reaction operator** for the eight-panel validation set, first in symbolic form and with exact degeneration checks, before any Pu numbers are accepted.