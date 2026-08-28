# NZ-SCCM — Nguyen finite generalized resultants → current terminal N–M bypass gate R01

**Date:** 2026-08-28  
**Identity:** THEORY AUDIT / DIAGNOSTIC ONLY / NOT PRODUCTION  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Discipline:** THEORY FIRST / NO FEM / NO TEST / FAIL FAST / NO SPATIAL COLLOCATION / NO MATERIAL APPROXIMATION

---

## 0. Question under audit

After the previous zero-spatial-integration audit reached the Hu tensile exponential branch, do **not** immediately open a new exponential/confluent special-function backend.

Instead test the more fundamental proposed bypass:

\[
\boxed{
\text{Nguyen compatible kinematics}
\to
\text{finite generalized resultants}
\to
\text{existing current terminal }N\! -\! M
}
\]

with the hope that the current UHPC material law need not be distributed over the complete halfwave.

The required standard is not “a reduced model can be written”. The gate asks whether the existing terminal section operator can be reused to produce the **exact generalized equilibrium forces of the chosen Nguyen finite kinematic ansatz**, without full-halfwave current-material projection and without a new approximation.

Stop at the first failed theoretical gate.

---

## G0 — finite compatible Nguyen/project kinematics

Use the already recovered finite coordinates

\[
\mathbf a=(D,\alpha,q).
\]

The compatible strains have the form

\[
\varepsilon_i(x,y,z;\mathbf a)
=A_i(x,y;\mathbf a)+zB_i(x,y;\mathbf a),
\qquad i\in\{x,y\},
\]

with

\[
B_x=\frac{\pi^2q}{b}\sin X\sin Y,
\qquad
B_y=\frac{\pi^2k^2q}{b}\sin X\sin Y,
\]

and `A_i` finite trigonometric polynomials containing the uniform, redistribution, and von-Karman terms.

Therefore compatibility is satisfied by construction and all generalized virtual-strain kernels

\[
\partial_D\varepsilon,
\quad
\partial_\alpha\varepsilon,
\quad
\partial_q\varepsilon
\]

are finite analytic fields.

```text
G0_NGUYEN_FINITE_COMPATIBLE_KINEMATICS = PASS
```

---

## G1 — existing UHPC terminal is a local section constitutive map, not a global generalized map

The frozen SSUHPC terminal defines, at a given section/location,

\[
\boxed{
\mathcal C_i^{U}:(A_i,B_i)\mapsto(N_i^U,M_i^U)
}
\]

through

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

This map is exact through the thickness. It accepts a **local pair** `(A_i,B_i)`.

Under Nguyen kinematics those arguments are fields:

\[
A_i=A_i(x,y;D,\alpha,q),
\qquad
B_i=B_i(x,y;q).
\]

Hence the exact current sectional resultants are themselves fields

\[
N_i^U(x,y)=\mathcal N_i[A_i(x,y),B_i(x,y)],
\]

\[
M_i^U(x,y)=\mathcal M_i[A_i(x,y),B_i(x,y)].
\]

```text
G1_EXISTING_TERMINAL_IDENTITY = PASS
TERMINAL_SCOPE = LOCAL_SECTION_NM_MAP
TERMINAL_SCOPE_IS_NOT_GLOBAL_GENERALIZED_FORCE_MAP = YES
```

---

## G2 — can generalized equilibrium forces be obtained by “generalize strain first, then apply terminal” without area projection?

For a displacement-based finite ansatz, the exact generalized internal force conjugate to coordinate `a_r` is

\[
\boxed{
Q_r^{int}
=
\iint_\Omega
\left[
\mathbf N^T(x,y)\,\frac{\partial\boldsymbol\varepsilon^0}{\partial a_r}
+
\mathbf M^T(x,y)\,\frac{\partial\boldsymbol\kappa}{\partial a_r}
\right]dA.
}
\]

Consider only the **simplest UHPC normal channel**; no shear, steel face, web, local buckling, or tensile branch is needed for this gate.

For the axial coordinate `D`, the Nguyen/project field has a constant `D`-virtual normal-strain kernel, e.g.

\[
\varepsilon_{y,D}^0=-\varepsilon_0.
\]

Therefore even this simplest generalized force already contains

\[
Q_D^{U}
\supset
-\varepsilon_0
\iint_\Omega
\mathcal N_y\bigl(A_y(x,y),B_y(x,y)\bigr)\,dA.
\]

The proposed bypass would require an identity of the type

\[
\boxed{
\iint_\Omega
\mathcal N(A(x,y),B(x,y))\,dA
\stackrel{?}{=}
\widetilde{\mathcal N}(\bar A_1,\ldots,\bar A_m,\bar B_1,\ldots,\bar B_n)
}
\]

where the right-hand side is obtained from a **finite number of generalized kinematic quantities and the existing terminal map**, without performing the current-material area projection.

For the existing nonlinear UHPC terminal, this commutation does not hold.

### G2.1 Nonlinear constitutive map and projection do not commute

Take a scalar notation `F(A,B)=mathcal N(A,B)` and decompose

\[
A=\bar A+\delta A,
\qquad
B=\bar B+\delta B.
\]

For a nonlinear analytic branch,

\[
\begin{aligned}
\langle F(A,B)\rangle
={}&F(\bar A,\bar B)
+\frac12F_{AA}\langle\delta A^2\rangle
+F_{AB}\langle\delta A\delta B\rangle
+\frac12F_{BB}\langle\delta B^2\rangle\\
&+\frac1{3!}F_{AAA}\langle\delta A^3\rangle+\cdots .
\end{aligned}
\]

Thus the average/generalized force depends on the spatial distribution through higher moments. In general

\[
\boxed{
\langle F(A,B)\rangle\neq F(\langle A\rangle,\langle B\rangle).
}
\]

The Hu compression map is already nonlinear and rational, so this failure occurs **even if the entire core is compression-only**. It is not caused by the Hu tensile exponential branch.

### G2.2 Finite Nguyen strain modes do not imply finite current-stress/resultant modes

`A_i(x,y)` and `B_i(x,y)` are finite trigonometric polynomials, but composing them with a non-polynomial constitutive map generally generates an infinite Fourier/harmonic content:

\[
\text{finite trig field}
\xrightarrow{\text{nonlinear rational/exponential }\mathcal C}
\text{not a finite trig field in general}.
\]

Therefore the exact current `N(x,y),M(x,y)` cannot be reconstructed from a finite set of terminal values or from the original finite kinematic coefficients by an identity already present in the terminal theory.

### G2.3 Naming the projected object a “generalized terminal” does not remove the integral

One may define a new map formally by

\[
\mathcal C_G(D,\alpha,q)
:=
\left\{
Q_D^{int},Q_\alpha^{int},Q_q^{int}
\right\}.
\]

But its definition is precisely

\[
\mathcal C_G
=
\iint_\Omega
\mathbf B^T(x,y)
\mathcal C_{sec}[A(x,y),B(x,y)]\,dA.
\]

This is the full-halfwave current-material projection under a new name. It is **not** the existing terminal `N-M` map and does not bypass the spatial analytic closure problem.

### G2.4 Finite control-section evaluation would be a new approximation

Replacing the exact projection by antinode, finite stations, or finite weighted terminal samples would be

- collocation / quadrature, or
- an assumed stress/resultant harmonic closure.

That can define a reduced theory, but it is not an exact consequence of the Nguyen kinematic ansatz plus the existing terminal operator. It would need a separately authorized approximation doctrine. Under the present gate it is prohibited.

Therefore:

```text
G2_FINITE_GENERALIZED_RESULTANT_THEN_EXISTING_TERMINAL_EXACT_BYPASS = FAIL
FAIL_TYPE = NONCOMMUTATION_OF_NONLINEAR_CONSTITUTIVE_MAP_AND_SPATIAL_PROJECTION
FAIL_OCCURS_IN_COMPRESSION_ONLY_SCALAR_NORMAL_CHANNEL = YES
HU_TENSION_REQUIRED_FOR_FAILURE = NO
SPATIAL_QUADRATURE_USED = NO
COLLOCATION_USED = NO
NEW_APPROXIMATION_USED = NO
```

---

# STOP — fail fast at G2

Execution stops here.

Not executed:

```text
new exponential/confluent period backend
UHPC tensile-area closure
steel faces / R02 / R06
web
full generalized current operator
Jacobian / tangent singularity
terminal envelope intersection
Pu
BH032/BH050
FEM/test comparison
```

---

## Consequence of the gate

There is no exact third route of the form

\[
\boxed{
\text{Nguyen kinematics}
\to
\text{a few generalized strains/resultants}
\to
\text{reuse the existing local terminal once/finitely many times}
}
\]

that simultaneously preserves:

1. Nguyen kinematic compatibility;
2. the existing nonlinear current terminal constitutive relation;
3. exact generalized equilibrium;
4. zero full-halfwave current-material projection;
5. no new approximation.

The exact choices remain logically separated:

- **Full current route:** evaluate/project the current terminal field over the complete halfwave. This is mechanically unified; its previous analytic gate first stopped at the Hu tensile exponential spatial function class.
- **Capacity-contact route:** retain an independently closed structural front (e.g. initial-elastic Airy) and use terminal only as finite capacity/contact equations. This remains explicit but is not the same as a fully current constitutively unified displacement formulation.
- **New reduced closure:** use finite control sections/harmonic stress assumptions/generalized constitutive approximations. This may be useful, but it is a new approximation and is not authorized by the present gate.

No choice among these alternatives is made in this audit.

---

## Final status

```text
THEORY_ONLY = YES
PRODUCTION_CHANGED = NO
FEM_USED = NO
TEST_USED = NO
NGUYEN_FINITE_KINEMATICS = PASS
EXISTING_TERMINAL_LOCAL_SECTION_NM = PASS
EXACT_GENERALIZED_FORCE_WITHOUT_CURRENT_AREA_PROJECTION = FAIL
FIRST_FAILED_GATE = G2
FAIL_REASON = nonlinear constitutive projection does not commute with finite kinematic reduction
FAIL_ALREADY_PRESENT_IN_UHPC_COMPRESSION = YES
HU_TENSION_IS_NOT_THE_ROOT_CAUSE_OF_THIS_BYPASS_FAILURE = YES
EXECUTION_STOPPED_AT_FIRST_FAILED_GATE = YES
```
