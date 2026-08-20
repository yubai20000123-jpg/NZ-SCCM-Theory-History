# NZ-SCCM — R123 forensic correction: R3 withdrawn, Poisson role reclassified

Time: 2026-08-20 20:14 +08:00

Status: `R3_AS_NGUYEN_EQUIVALENT_STRAIN = WITHDRAWN`; `POISSON_CONSISTENCY_REQUIREMENT = RETAINED`; `R1/R2_REAUDIT_REQUIRED`

## 1. Main correction

The previous R3 repair was framed as: the reconstructed NC-M4 current operator had lost Poisson coupling, therefore restore Nguyen's equivalent-uniaxial strain transformation. This repair is not justified for the current restructured-material program.

The historical/current successful Case21 reduced kinematic ansatz already contains a Poisson baseline in the physical strain field. In the unbuckled state it has

\[
e_x=\nu D,\qquad e_y=-D,\qquad \gamma=0.
\]

The older R10 material backend also contained its own plane-stress/equivalent-strain transform. Those are two different roles: the first is a chosen in-plane kinematic baseline; the second is a constitutive mapping device used by R10 to build multiaxial behavior from scalar primitives.

For the new explicitly reconstructed 2D material law, there is no requirement to inherit Nguyen's equivalent-uniaxial variable definition. Therefore the previous R3 transformation

\[
\widehat\varepsilon_1=(\varepsilon_1+\nu\varepsilon_2)/(1-\nu^2),\qquad
\widehat\varepsilon_2=(\varepsilon_2+\nu\varepsilon_1)/(1-\nu^2)
\]

is withdrawn as a formal NC-M4 repair.

## 2. What remains physically required

Poisson consistency is still real, but it must be imposed as a direct small-strain constraint on the reconstructed 2D current material operator, not necessarily by an equivalent-uniaxial transformation:

\[
\left.\frac{\partial(\sigma_1,\sigma_2)}{\partial(\varepsilon_1,\varepsilon_2)}\right|_{0}
=\frac{E_0}{1-\nu^2}
\begin{bmatrix}1&\nu\\\nu&1\end{bmatrix}.
\]

This is the clean constitutive acceptance condition.

## 3. Kinematic correction to be reaudited

The recent three-variable field used

\[
\varepsilon_x=\varepsilon_m+\text{second-order geometric terms}+\text{bending term},
\]

thereby replacing, rather than augmenting, the historical Poisson baseline. A more consistent three-variable decomposition is

\[
\varepsilon_x=\nu\frac{\Delta}{\ell}+\varepsilon_m+\text{second-order geometric terms}+\text{bending term},
\]

\[
\varepsilon_y=-\frac{\Delta}{\ell}+\text{second-order geometric terms}+\text{bending term}.
\]

Here `epsilon_m` is interpreted as an additional nonlinear transverse membrane correction, not the whole transverse strain.

Under the direct small-strain plane-stress material tangent above, the unbuckled linear state gives

\[
\sigma_x=\frac{E_0}{1-\nu^2}\varepsilon_m,
\]

so `R_m=0` yields `epsilon_m=0`; the physical transverse strain remains the correct Poisson strain `nu Delta/ell`.

## 4. Provenance of the previously listed hidden issues

- raw-strain grid vs equivalent-strain grid conflict: introduced only by R3; disappears when R3 is withdrawn.
- constant-dilation vs full Nguyen issue: introduced only by R3; disappears when R3 is withdrawn.
- gamma_c C0/not-C1 threshold: introduced by the R2 remedy (Nguyen capped compression-softening law), not by R3.
- tangent asymmetry / absence of a proven hyperelastic potential: already present in base NC-M4 interaction laws; not caused by R3.
- missing cracked shear-retention channel: pre-existing omission in NC-M4; not caused by R1/R2/R3.
- T4 peak-strain inconsistency: pre-existing NC-M4 issue; not caused by R1/R2/R3.
- compression initial-tangent compatibility `E0 eps_c0/fc≈2`: pre-existing consequence of the selected compression skeleton; not caused by R1/R2/R3.

## 5. Status of R1 and R2 after R3 withdrawal

R1 diagnosis remains valid: the internal scale of the T4 tensile curve must not be silently reused as the scale of a separate TC compression-interaction law.

R2 diagnosis also remains valid: the old `1/(1+0.15 t^2)` TC reduction was excessively strong for reachable Case21 mixed states. However, the specific Nguyen capped replacement used in R2 is not automatically retained; it introduced a new non-C1 threshold and should be reaudited against the project's goal of a smooth restructured material law.

## 6. Immediate next theory identity

The current material baseline should revert conceptually from `NC-M4-R123` to `NC-M4-R12-REAUDIT`, with:

1. restored Poisson baseline in the physical reduced kinematics;
2. `epsilon_m` retained only as an additional transverse membrane correction;
3. material grid retained on raw physical principal strains;
4. no Nguyen equivalent-uniaxial R3 transform;
5. direct 2D material operator required to satisfy the small-strain plane-stress tangent constraint;
6. R1 retained;
7. R2 functional form reopened for smoothness/source consistency before lock.
