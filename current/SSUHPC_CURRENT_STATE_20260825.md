# CURRENT STATE — Steel-Shell UHPC

**Updated:** 2026-08-25 13:30 +08:00  
**Status:** `RC_SSNC_MILESTONE_ANCHORED / SSNC_PARENT_RETAINED / CORE_NM_SUBSTITUTION_ONLY / NUMERICAL_EXECUTION_PENDING`

Canonical parent:

`current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`

Canonical SSUHPC derivation:

`semantic_v2/20_theory/20260825_1330__NZSCCM__SSUHPC_FROM_RC_SSNC_MILESTONE_CORE_NM_SUBSTITUTION_V1.md`

---

## 0. Supersession correction

The earlier 13:00 artifact

`semantic_v2/20_theory/20260825_1300__NZSCCM__STEEL_SHELL_UHPC_HU_EARLY_REPLACEMENT_THEORY_V1.md`

is **not** the current theory anchor. It overinterpreted the historical UHPC dialogue as permission to reconstruct an independent early-Hu branch.

Correct interpretation:

```text
HISTORICAL_UHPC_DIALOGUE_ROLE = MATERIAL_UNIT_MEMORY_ONLY
```

It may be retained as an audit artifact, but it is superseded for current-theory purposes by the 13:30 file above.

---

## 1. Unique parent theory

```text
ANCHOR = RC–SSNC Unified Terminal-Capacity Milestone, 2026-08-25
PARENT = SSNC section of that milestone
```

SSUHPC can only be formed by replacing the ordinary-concrete core terminal resultants:

\[
\boxed{
NC\ core:\ \mathcal C_c^{NC}(N_x,M_x;N_y,M_y)
\rightarrow
UHPC\ core:\ \mathcal C_c^{UHPC}(N_x,M_x;N_y,M_y)
}
\]

Everything else remains SSNC milestone theory.

---

## 2. Retained without modification

```text
FULL_2D_MARGUERRE_AIRY = RETAIN
INITIAL_FULL_COMPOSITE_ABD_FORM = RETAIN
CONTROL_HALFWAVE_LOGIC = RETAIN
COMMON_TERMINAL_STRAIN/RESULTANT_ARCHITECTURE = RETAIN
R02_STEEL_FACE = RETAIN
R04_STEEL_FACE_CAP = RETAIN
LONGITUDINAL_WEB = RETAIN
STEEL_FACE_OFFSET = RETAIN_ONCE_ONLY
R03_AS_Pu_GATE = NO
CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
COMPARATOR_IN_ROOT_SELECTION = 0
```

Changing NC to UHPC changes the core elastic constants inserted into the same initial ABD formula; it does not create a new structural front.

---

## 3. UHPC material unit recovered from history

Current historical material memory for the core:

```text
fc    = 141.1 MPa
Ec    = 43.4 GPa
epsc0 = 0.0035
nu_c  = 0.20
```

Compression backbone:

\[
\sigma_c=
\begin{cases}
f_c\dfrac{n\xi-\xi^2}{1+(n-2)\xi}, & \xi\le1,\\[8pt]
f_c\dfrac{\xi}{2(\xi-1)^2+\xi}, & \xi>1,
\end{cases}
\qquad
\xi=|\varepsilon|/\varepsilon_{c0},
\qquad
n=E_c\varepsilon_{c0}/f_c.
\]

If a section direction develops a tensile zone, use only the historical Hu-source UHPC tensile branch with its actual source/specimen parameters. Do not replace it with NC tension and do not invent missing UHPC tensile parameters.

---

## 4. Only changed terminal object

For `i=x,y`, retain the milestone section kinematics

\[
\varepsilon_i(z)=\varepsilon_i^0+z\kappa_i.
\]

Then generate the UHPC core resultant relation

\[
N_i^{UHPC}
=(1-\rho_w)\int_{-t_c/2}^{t_c/2}
\sigma_U[\varepsilon_i(z)]\,dz,
\]

\[
M_i^{UHPC}
=(1-\rho_w)\int_{-t_c/2}^{t_c/2}
z\sigma_U[\varepsilon_i(z)]\,dz.
\]

Thus the only theory substitution is

```text
NC longitudinal N-M -> UHPC longitudinal N-M
NC transverse N-M   -> UHPC transverse N-M
```

No independent CC/TC/TT state machine is added.

---

## 5. Phase assembly remains milestone SSNC

\[
N_x^{sec}=N_x^{UHPC}+N_{x,+}^{face}+N_{x,-}^{face}+N_x^{web},
\]

\[
M_x^{sec}=M_x^{UHPC}+M_{x,+}^{face}+M_{x,-}^{face}+M_x^{web},
\]

\[
N_y^{sec}=N_y^{UHPC}+N_y^{web}+N_{y,+}^{face}+N_{y,-}^{face},
\]

\[
M_y^{sec}=M_y^{UHPC}+M_y^{web}+M_{y,+}^{face}+M_{y,-}^{face}.
\]

Use the SSNC milestone web identity; if its longitudinal web has no x-resultant role, then `Nx_web=Mx_web=0`.

General terminal contact remains

\[
N_x^{sec}=N_x^d,\quad
M_x^{sec}=M_x^d,\quad
N_y^{sec}=N_y^d,\quad
M_y^{sec}=M_y^d,
\]

with the milestone endpoint/active-set degenerations applied only when independently justified for the specimen.

---

## 6. Historical dialogue exclusions

Do not import from historical UHPC calculations:

```text
old structural panel length/mode
old Airy coefficients
32/37 mm web rebase choices
old R-O/Yun-only steel terminal
old T120/T360/BH Pu values as targets
Zhang/Liu/FHWA/R08 later repair chains
```

Those records are evidence for the UHPC material unit only.

---

## 7. Next task

```text
NEXT = BUILD/VERIFY UHPC CORE LONGITUDINAL + TRANSVERSE N-M RELATIONS
       INSIDE THE MILESTONE SSNC TERMINAL ASSEMBLY
THEN = RECOMPUTE SELECTED STEEL-SHELL UHPC CASES
COMPARATORS = CLOSED UNTIL ROOTS ARE FIXED
```

Current gate:

```text
SSUHPC_PARENT_ANCHOR = PASS
CORE_NM_SUBSTITUTION_DEFINITION = PASS
NUMERICAL_RESULTS = NOT YET GENERATED UNDER THIS CORRECTED THEORY
```
