# GOVERNANCE CLARIFICATION — R10 MATERIAL CHANGE VS R10B ANALYTIC COMPILATION

**Date:** 2026-08-11 14:28 +08:00  
**Status:** CURRENT GOVERNING INTERPRETATION CLARIFICATION  
**Scope:** identity/interpretation only; does not alter the frozen R10/R10B numerical results.

## 1. Why this clarification is necessary

Recent recovery discussion mixed three different objects:

1. the source Foster multidimensional current operator;
2. the R10 material-target modification;
3. the R10B finite analytic compiler representation.

This produced incorrect or unsupported statements such as:

- treating `material degree = 48` as a total coefficient count;
- inferring `147` coefficients from an assumed implementation layout;
- treating a forensic least-squares/DCT hypothesis as the historical R10B coefficient generator;
- describing R10 as only a tiny local `lambda`-patch when the executed R10 formula reconstructs the retained tensile scalar interval in the internal coordinate `t`;
- blurring material-model change with finite-representation truncation.

These interpretations are revoked as governing statements.

---

## 2. Evidence hierarchy for R10/R10B recovery

Apply the repository source-of-truth policy strictly:

```text
current/ + current governance
> original execution artifacts / source code / original conversation
> audit / recovery note
> handoff / summary / model memory
```

The current governing files remain:

- `current/CURRENT_STATE.md`
- `governance/R10_1D_ENERGY_SMOOTHING_DECISION_20260810.md`
- `current/theory/NZ_SCCM_R10_1D_ENERGY_SMOOTHING_REINSERTION_CASE21_20260810.md`
- `governance/R10B_ZERO_SPATIAL_CASE21_DECISION_20260811.md`
- `current/theory/NZ_SCCM_R10B_ZERO_SPATIAL_D15_CASE21_20260811.md`

Any recovery note that conflicts with those files is non-governing.

---

## 3. First transformation: Foster source -> R10 material target

This is a **material-target change**.

The source ordinary-concrete current operator remains a multidimensional spectral current map:

```text
strain tensor
-> equivalent-uniaxial tensor
-> lambda+, lambda-
-> same 1D primitives C(lambda), T_Foster(lambda), U(lambda)
-> SAME CC/TC/TT interaction
-> spectral return
```

R10 does not replace the multidimensional interaction architecture. It modifies only the tensile scalar used inside that architecture.

The source tensile scalar is

\[
u_{t,src}(t)=\rho T_{Foster}(t),
\qquad
 t=\Pi_\eta(\lambda),
\]

with retained tensile interval

\[
0\le t\le 10x_{cr}.
\]

The source work is

\[
\boxed{W_{src}=0.031741235181249904.}
\]

R10 replaces the source tensile scalar over this retained interval by two C2 quintic branches.

For

\[
0\le t\le x_{cr},\qquad \tau=t/x_{cr},
\]

\[
\boxed{
 u_{rise}=\rho\tau+(10h-6\rho)\tau^3
 +(8\rho-15h)\tau^4+(6h-3\rho)\tau^5.
}
\]

For

\[
x_{cr}\le t\le 10x_{cr},\qquad
\tau_f=(t-x_{cr})/(9x_{cr}),
\]

\[
\boxed{
 u_{fall}=h+(u_r-h)(10\tau_f^3-15\tau_f^4+6\tau_f^5),
\qquad u_r=0.03.
}
\]

The energy condition

\[
\int_0^{10x_{cr}}u_{sm}(t)\,dt=W_{src}
\]

fixes

\[
\boxed{h=0.09799750427197301.}
\]

Thus the executed R10 should be described as:

```text
source Foster tensile scalar
-> broad two-piece C2 reconstruction over the retained 0..10*xcr tensile interval
-> same multidimensional U/C/T + CC/TC/TT + spectral architecture
```

The motivation is removal of the sharp Foster transition, but the executed formula is not merely an infinitesimal local patch around one `lambda` point.

This distinction matters because R10 changes the distribution of tensile material work even while retaining the total work, origin tangent, rounded peak location, residual level and endpoint regularity.

R10 is therefore the only step in the R10/R10B chain that changes the material target.

---

## 4. R10 reinsertion identity

After R10 smoothing,

\[
\boxed{T_i^{new}=u_{sm}(t_i)/\rho.}
\]

The same current master remains

\[
U_i=\kappa\lambda_i-C_i+\kappa c_i+\rho T_i-\kappa t_i,
\]

and the same interactions remain

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_--\rho a_tT_+T_-^8,
\]

\[
s_-=U_--a_{cc}C_-^2C_++C_-T_+-\rho a_tT_-T_+^8.
\]

There is no 2D/4D material refit in R10.

The global-energy-potential replacement route remains revoked as the wrong mathematical object.

---

## 5. Second transformation: R10 material target -> R10B finite analytic representation

This is **not a second material-model modification**.

R10B starts from the frozen R10 scalar and performs only analytic compilation/reintegration:

```text
frozen R10 u_sm(t)
-> 1D material-coordinate finite Chebyshev representation
-> SAME U/C/T + CC/TC/TT current map
-> Cayley-Hamilton coefficient algebra
-> finite spatial coefficient representation
-> exact complete-halfwave moments
-> P(D,q), R(D,q)
-> same-expression derivatives
-> limit root
```

R10B changes no R10 material parameter and may not be interpreted as a second material calibration.

However, finite-order analytic compilation is still an approximation to the frozen R10 material function. Therefore distinguish:

```text
material-physics change          : R10 only
material representation error    : R10B finite compiler order
spatial numerical quadrature     : zero in the formal R10B operator
finite-representation integration: exact moment contraction
```

The statement that the R10 interaction is retained "exactly at the finite compiler level" means:

> once the finite 1D compiler functions are fixed, CC/TC/TT and spectral reconstruction are generated algebraically without an additional multidimensional fit.

It does **not** mean that a finite-order compiler is pointwise identical to the untruncated R10 scalar.

---

## 6. Meaning of the two R10B orders

The current formal result records:

```text
material degree = 48
spatial Chebyshev degree = 28
```

Governing interpretation:

\[
\boxed{N_M=48=\text{1D material-coordinate analytic representation order}}
\]

\[
\boxed{N_S=28=\text{structural spatial coefficient-representation order}}
\]

They are not:

- numbers of material parameters;
- numbers of material points;
- numbers of spatial integration points;
- counts such as `147` inferred from an assumed internal array layout.

Actual coefficient-array counts and storage layout are implementation facts and must be recovered from the original R10B core/coefficient artifacts before being asserted.

---

## 7. R10B coefficient-generator evidence boundary

The canonical R10B theory establishes only that material-coordinate samples are used to derive finite 1D analytic compiler coefficients and that those samples are not spatial samples or free material parameters.

The current repository does **not** contain the byte-exact original contents of:

- `07_R10B_zero_spatial_compiler_core.py`;
- the executed N48 coefficient arrays;
- the complete original coefficient-generation convention.

Therefore none of the following may currently be asserted as historical R10B fact without new original evidence:

- DCT-I as the unique executed generator;
- DCT-II as the unique executed generator;
- a particular continuous Chebyshev projection;
- a particular least-squares sampling/weighting rule;
- a particular total coefficient count.

Such constructions may be used later as transparent reproducible replacement conventions, but only after being explicitly frozen as a new reproducibility contract and revalidated against the current Case21 baseline. They must not be back-labelled as the historical R10B implementation.

---

## 8. R09A -> R10 -> R10B lineage

The correct lineage is:

```text
R09A diagnostic
  -> showed that tensile-shape complexity can be reduced
  -> showed that retained tensile-capacity level is not negligible
  -> SAT03/SAT05/SAT07 remain sensitivity brackets only

R10 material target
  -> uses source material work and physical/C2 anchors
  -> replaces the source Foster tensile scalar by a broad two-piece C2 retained-interval reconstruction
  -> retains the same multidimensional interaction

R10B analytic compilation
  -> makes no further material change
  -> represents frozen R10 in finite analytic form
  -> reconstructs the same interaction algebraically
  -> performs zero-spatial exact moment contraction
```

---

## 9. Interpretation of the large R10 structural shift

The same-equation R10 audit gives approximately

```text
SOURCE_FOSTER Pu      = 342.334029 kN
R10_ENERGY_SMOOTH Pu  = 368.723464 kN
Delta                 = +26.389435 kN
```

while the tensile peak itself changes only modestly.

This is not, by itself, evidence of calibration or error. R09A already showed that the tensile branch can shift the coupled stationary coordinates and therefore indirectly alter the compression-side contribution.

Nevertheless, because the executed R10 reconstructs the entire retained tensile scalar interval rather than only an infinitesimal local peak neighborhood, the R10 material target deserves a dedicated material-level interpretation/audit before any attempt to reconstruct historical N48 coefficient-generation details.

This audit must not retune `h` using Case21 or Swartz structural capacities.

---

## 10. Required order for further recovery work

Until the R10/R10B recovery is complete, use the following order:

```text
STEP 1  Audit the frozen R10 material target itself
        - source Foster scalar vs R10 scalar
        - work redistribution over 0..10*xcr
        - scalar stress/tangent differences
        - reconstructed multidimensional material-surface differences
        - no structural recalibration

STEP 2  Audit R10B representation fidelity
        - frozen R10 exact target vs finite N_M representation
        - separate material-coordinate representation error from spatial coefficient truncation
        - no change to R10 physics

STEP 3  Recover or explicitly re-freeze the coefficient-generation convention
        - only original core/artifacts may define the historical convention
        - otherwise create a new transparent reproducibility contract and label it as new

STEP 4  Generate coefficient tables / supplementary reproducibility material
        - only after STEP 1-3 are resolved
```

Do not reverse this order.

---

## 11. Current project-state effect

This clarification does not revoke the executed engineering result:

```text
R10_1D_ENERGY_SMOOTHING                    = PASS
R10B_1D_MATERIAL_RECOMPILE                 = PASS
R10B_ZERO_SPATIAL_CASE21                   = PASS_ENGINEERING
CASE21_N48_LIMIT_ROOT                       = PASS
SWARTZ24                                   = NOT_STARTED
```

No value of `h`, `D_u`, `q_u`, `Pc`, `Ps` or `Pu` is changed by this clarification.

What changes is the recovery/interpretation discipline:

```text
R10  = material-target modification
R10B = finite analytic compilation of frozen R10
N_M  = material representation order, not parameter count
N_S  = spatial coefficient order, not quadrature count
historical R10B coefficient generator = unresolved until original evidence is recovered
```
