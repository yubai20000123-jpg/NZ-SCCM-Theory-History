# NZ-SCCM — BH050 / BH032 classical `w -> kappa -> eps(z)` kinematic reconstruction R01

**Time:** 2026-08-27 20:52 +08:00  
**Status:** `KINEMATIC_CONTRACT_RECONSTRUCTED / qU PRODUCTION RETIRED / NO NEW Pu FIT`  
**Scope:** classical thin-plate kinematics + existing frozen Airy/R06 roots + read-only FEM diagnostics. No comparator-dependent parameter fit, no new current-moment feedback, no numerical spatial quadrature in the formal theory.

---

## 0. Decision and question

This audit implements the current project decision:

```text
qU_GL_LOCAL_STEEL = ARCHIVED_SENSITIVITY_ONLY
qU_IN_PRODUCTION = NO
COMMON_R06_qU_OFF = PRODUCTION_BASELINE
```

The reason is numerical economy: the formally certified BH050 qU correction changes `Pu` from `13.3563763545430 MN` to `13.2934844671869 MN`, i.e. only about `-0.47%`, while it requires a materially heavier GL+LL finite-Fourier local-Mises backend.

The remaining question is more fundamental:

> Why do FEM section observables look membrane-compression dominated while the terminal theory had been read as a strong compression-bending state? Is the global out-of-plane amplitude `q` too large, or are distinct curvature objects being conflated?

The answer from the present reconstruction is:

```text
EXCESSIVE_GLOBAL_q_AS_PRIMARY_CAUSE = NOT SUPPORTED
AIRY_STRUCTURAL_BENDING_IS_ALREADY_q_KINEMATIC = YES
TERMINAL_By_AS_ACTUAL_GLOBAL_CURVATURE = INVALID
STEEL_MEAN_APPARENT_CURVATURE_AS_GLOBAL_CURVATURE = INVALID AFTER LOCAL SHELL DEFORMATION
BH050_q_TO_FE_UHPC_NEAR_MATCH = CASE-SPECIFIC, NOT A UNIVERSAL IDENTITY
```

---

# 1. Classical reference: stress-free imperfection versus load-induced curvature

The frozen explicit Marguerre–Airy theory defines

\[
\phi(x,y)=\sin(\alpha x)\sin(\beta y),
\]

\[
w_i=bq_0\phi,
\qquad
w_d=bq\phi.
\]

`w_i` is the stress-free initial imperfection and `w_d` is the load-induced added deflection. Therefore two different geometric objects must be kept separate.

The **current geometric shape** is

\[
w_{geom}=w_i+w_d=b(q_0+q)\phi,
\]

but the **stress-producing incremental Kirchhoff–Love bending curvature** relative to the stress-free initial geometry is generated only by `w_d`:

\[
\Delta\kappa_x=-w_{d,xx}=bq\alpha^2\sin(\alpha x)\sin(\beta y),
\]

\[
\Delta\kappa_y=-w_{d,yy}=bq\beta^2\sin(\alpha x)\sin(\beta y),
\]

\[
\Delta\kappa_{xy}=-2w_{d,xy}
=-2bq\alpha\beta\cos(\alpha x)\cos(\beta y).
\]

This is fully consistent with the existing Marguerre membrane term

\[
Q_q=q(q+2q_0),
\]

because the nonlinear membrane strain depends on the change of squared slopes between the imperfect initial geometry and the loaded geometry, whereas the incremental bending strain depends on the curvature change.

At the control antinode `s=sin(alpha x)=1` and the longitudinal halfwave center,

\[
\boxed{\Delta\kappa_x=bq\alpha^2},
\qquad
\boxed{\Delta\kappa_y=bq\beta^2},
\qquad
\boxed{\Delta\kappa_{xy}=0}.
\]

For the BH032 and BH050 control modes, `ell=b`, so

\[
\boxed{\Delta\kappa_x=\Delta\kappa_y=\frac{\pi^2q}{b}}.
\]

---

# 2. The Airy structural moment is already exactly the classical q-curvature moment

The frozen explicit theory uses

\[
M_y^d=J_y q s,
\qquad
J_y=b(D_\mu\alpha^2+D_y\beta^2).
\]

Substituting the classical antinode curvature gives

\[
D_\mu\Delta\kappa_x+D_y\Delta\kappa_y
=
D_\mu(bq\alpha^2s)+D_y(bq\beta^2s)
=
J_yqs.
\]

Hence

\[
\boxed{M_y^d=D_\mu\Delta\kappa_x+D_y\Delta\kappa_y}.
\]

This is important: the structural front did **not** create a second independent physical curvature. Its bending demand is already the classical bending moment associated with the same `q` that appears in `w_d`.

Therefore imposing

```text
terminal By = pi^2*q/b
```

inside the terminal capacity system is not a missing kinematic correction. It would identify a capacity-surface coordinate with a structural deformation coordinate and would destroy the original demand-capacity-contact architecture. That prior common-kappa detour remains retracted.

---

# 3. Four curvature objects must no longer share one symbol

From this node onward the following objects are formally distinct.

### K1 — global structural geometric curvature

\[
\kappa_y^{geo}(q)=\frac{\pi^2q}{b}
\]

at the BH control antinode. This is an actual kinematic prediction of the one-mode structural ansatz.

### K2 — terminal N-M capacity coordinate

The existing terminal affine parameter historically called `B_y` is renamed in interpretation as

\[
\boxed{B_y^{cap}}
\]

with

\[
\varepsilon_y^{cap}(z)=A_y^{cap}+B_y^{cap}z.
\]

It parameterizes a point on the terminal N-M capacity surface. It is **not** claimed to be the actual global deformation curvature and is not compared directly with FEM kinematics.

### K3 — FEM UHPC through-thickness fitted curvature

Existing read-only ODB diagnostics define

\[
LE33(y)\approx\varepsilon_{0,U}^{FE}
+\kappa_{U}^{FE}(y-y_{mid}).
\]

This is an observable extracted from a weighted through-thickness fit of UHPC total logarithmic strain. It is approximately first-order but not an exact plane-section field at peak.

### K4 — FEM steel-face mean apparent curvature

Existing diagnostics also define

\[
\kappa_{s,mean}^{FE}
=
\frac{\bar\varepsilon_{s,+}-\bar\varepsilon_{s,-}}{2z_f}.
\]

After local shell deformation this is only an **apparent mean face-strain difference**, not a validated generalized plate curvature. Existing steel/UHPC compatibility checks already show 41–45% lower-face discrepancies when the UHPC fit is extrapolated to the steel-face location.

These four objects must not be substituted for one another without a separate observable/kinematic proof.

---

# 4. BH050 reconstruction

Frozen qU-off common-R06 production baseline:

```text
b = ell = 2500 mm
q0 = 0.0025
q = 0.004772819645833164
Pu = 13.3563763545430 MN
Ny_d = -5137.30935871948 N/mm
My_d = 30060.7058605883 N
B_y^cap = 6.49781910466383e-5 1/mm
```

Classical deformation quantities are

\[
W_d=bq=11.9320491146\;\mathrm{mm},
\]

\[
W_0=bq_0=6.25\;\mathrm{mm},
\]

\[
W_{geom}=18.1820491146\;\mathrm{mm}.
\]

The maximum slope scale of the total one-mode shape is

\[
\pi(q+q_0)=0.0228482\;\mathrm{rad}=1.3091^\circ.
\]

Thus the global shape is shallow; there is no geometrical evidence that the prescribed one-mode deflection is excessively steep.

The load-induced antinode curvature is

\[
\boxed{\kappa_y^{geo}=1.88423367128\times10^{-5}\;\mathrm{mm}^{-1}}.
\]

The old terminal capacity coordinate is

\[
B_y^{cap}=6.49781910466\times10^{-5}\;\mathrm{mm}^{-1}
=3.4485\,\kappa_y^{geo}.
\]

So reading `B_y^cap` as the actual shape curvature would imply a geometry that is incompatible with the theory's own `q`; that interpretation is now formally prohibited.

Existing **old special-comparator ODB** diagnostics at its FEM peak `12.21981 MN` give

\[
\kappa_U^{FE}=1.83974\times10^{-5}\;\mathrm{mm}^{-1},
\]

\[
\kappa_{s,mean}^{FE}=6.25281537\times10^{-6}\;\mathrm{mm}^{-1}.
\]

Ratios are

\[
\frac{\kappa_U^{FE}}{\kappa_y^{geo}}=0.9764,
\qquad
\frac{\kappa_{s,mean}^{FE}}{\kappa_y^{geo}}=0.3318,
\]

\[
\frac{B_y^{cap}}{\kappa_U^{FE}}=3.5319.
\]

The near equality `kappa_U^FE ~ kappa_geo` is striking for BH050, but it is **not promoted to a general identity** because the BH032 cross-check below fails that identity. Also, these BH050 strain/curvature data come from the old special ODB; the later equal-contract BH050 model has a verified peak `12.591227 MN` but no archived equal-contract through-thickness curvature path in the present source set.

The actual structural demand eccentricity is only

\[
e_d=\left|\frac{M_y^d}{N_y^d}\right|
=5.85145\;\mathrm{mm}.
\]

With total thickness `h=50 mm`,

\[
\frac{e_d}{h/2}=0.2341.
\]

Thus the structural demand itself is compression dominated. The visually much stronger `compression+bending` impression came from treating `B_y^cap` and its capacity-state face strains as an actual deformation-path prediction.

---

# 5. BH032 cross-check

Frozen common-R06 root:

```text
b = ell = 1600 mm
q0 = 0.0025
q = 0.00137889961633743
Pu = 10.9405345132294 MN
Ny_d = -6798.60232003 N/mm
My_d = 13626.7706431 N
B_y^cap = 4.78843761523297e-5 1/mm
```

Classical deformation quantities are

\[
W_d=bq=2.20623938614\;\mathrm{mm},
\]

\[
W_0=4.0\;\mathrm{mm},
\]

\[
W_{geom}=6.20623938614\;\mathrm{mm},
\]

and the total maximum slope scale is

\[
\pi(q+q_0)=0.0121859\;\mathrm{rad}=0.6982^\circ.
\]

Again the global one-mode deformation is shallow, and even smaller than BH050.

The load-induced antinode curvature is

\[
\boxed{\kappa_y^{geo}=8.50574607629\times10^{-6}\;\mathrm{mm}^{-1}}.
\]

The old terminal capacity coordinate is

\[
B_y^{cap}=4.78843761523\times10^{-5}\;\mathrm{mm}^{-1}
=5.6297\,\kappa_y^{geo}.
\]

Existing BH032 FEM peak diagnostics give

\[
\kappa_U^{FE}=1.93135\times10^{-5}\;\mathrm{mm}^{-1},
\]

\[
\kappa_{s,mean}^{FE}=3.48530867\times10^{-6}\;\mathrm{mm}^{-1}.
\]

Thus

\[
\frac{\kappa_U^{FE}}{\kappa_y^{geo}}=2.2706,
\qquad
\frac{\kappa_{s,mean}^{FE}}{\kappa_y^{geo}}=0.4098,
\]

\[
\frac{B_y^{cap}}{\kappa_U^{FE}}=2.4793.
\]

This cross-check is decisive for interpretation: the BH050 `kappa_geo ~ kappa_U^FE` agreement cannot be used to assert that the theory's `q` is already a quantitatively validated FEM displacement amplitude. BH032 has an almost exact Pu comparison but its FEM UHPC fitted curvature is about 2.27 times the q-derived antinode incremental curvature. A direct FEM displacement-mode projection is therefore required before `q` is used as a validated local observable rather than a reduced structural generalized coordinate.

The BH032 structural demand eccentricity is

\[
e_d=\left|\frac{M_y^d}{N_y^d}\right|
=2.00435\;\mathrm{mm},
\]

or only

\[
\frac{e_d}{h/2}=0.08017.
\]

So BH032 is even more clearly membrane-compression dominated at the structural-demand level.

---

# 6. Why the FEM steel faces look more nearly pure compression

Existing ODB diagnostics at the FEM peaks give steel-face mean apparent curvatures far below the q-derived center-antinode curvature in both cases:

```text
BH032: kappa_s,mean^FE / kappa_geo = 0.4098
BH050: kappa_s,mean^FE / kappa_geo = 0.3318
```

This is a reproducible same-direction observation across both cases. However it must not be converted into an empirical curvature-reduction coefficient. The archived diagnostics already show that extrapolating the fitted UHPC strain plane to the steel-face location differs from actual steel mean LE22 by about 41.3% on the BH032 lower face and 44.6% on the BH050 lower face. Local shell deformation, spatial averaging, and phase-specific kinematics therefore break the naive identification

\[
\kappa_{s,mean}^{FE}=\kappa_{global}.
\]

Hence the current supported statement is:

\[
\boxed{\text{FEM steel mean strains are more membrane-dominated than a common plane-section reading,}}
\]

but not

\[
\boxed{\text{the global plate has zero or one-third curvature.}}
\]

No empirical `0.33*kappa` or `0.40*kappa` factor is introduced.

---

# 7. What is actually corrected now

The correction is not to change the Airy equation and not to force the terminal capacity coordinate to equal q-curvature. It is to repair the kinematic contract.

```text
1. qU production branch -> OFF; certified result retained as archive/sensitivity only.
2. q remains the sole global postbuckling amplitude in the structural Airy front.
3. kappa_geo(q) is the only actual curvature implied by the one-mode structural ansatz.
4. Airy My_d=Jy*q*s is retained because it is exactly the classical D*kappa_geo moment.
5. terminal Bx,By are henceforth Bx_cap,By_cap in interpretation: N-M capacity-surface coordinates only.
6. B_cap is not an FEM deformation observable and is not set equal to pi^2*q/b.
7. FEM UHPC fitted curvature and FEM steel mean apparent curvature remain separate observables.
8. No current-moment feedback and no common-kappa terminal constraint are reopened.
```

This removes the false logical chain

```text
large terminal By -> large actual plate curvature -> theory globally over-bends the FEM plate
```

while preserving the valid chain

```text
q -> classical incremental curvature -> initial-ABD Airy moment demand
  -> N-M demand
  -> terminal capacity-surface contact
  -> Pu.
```

---

# 8. Remaining observable gate before any further kinematic modification

The current remote source set contains section strains/stresses/resultants, but it does not contain a direct projection of the FEM load-induced out-of-plane displacement field onto the theoretical global sine mode.

Therefore the next kinematic evidence gate is uniquely defined:

\[
U_{oop}^{FE}(x,y)
\rightarrow
W_{FE}=\frac{\langle U_{oop}^{FE},\phi\rangle}{\langle\phi,\phi\rangle}
\rightarrow
q_{FE}=W_{FE}/b
\rightarrow
\kappa_{FE}^{geom}=bq_{FE}\beta^2.
\]

This is a **diagnostic comparator only**; it does not enter root selection or calibration.

It should be performed for BH032 and the equal-contract BH050 ODB at the respective FEM peaks. Only that direct displacement projection can distinguish:

- true one-mode amplitude mismatch;
- different FEM mode shape / multimode content;
- UHPC warping/shear-induced strain-gradient mismatch;
- steel local-shell kinematic decoupling.

Until that gate is available, no additional curvature coefficient or phase-reduction factor is justified.

---

# 9. Current result

```text
qU_PRODUCTION = NO
qU_FORMAL_CERTIFICATE = RETAIN_ARCHIVE_ONLY
CURRENT_PRODUCTION_BH050_qU_OFF = 13.3563763545430 MN
AIRY_q = RETAIN
AIRY_MOMENT_FORMULA = RETAIN
PHYSICAL_CURVATURE = kappa_geo(q)
TERMINAL_Bx_By_IDENTITY = CAPACITY_COORDINATES_ONLY
TERMINAL_B_EQUALS_GLOBAL_KAPPA = NO
BH050_EXCESSIVE_q_HYPOTHESIS = NOT_SUPPORTED
BH050_q_TO_OLD_FEM_UHPC_NEAR_MATCH = OBSERVED_BUT_NOT_GENERAL
BH032_CROSSCHECK = DIRECT_q_TO_FE_UHPC_IDENTITY_FAILS
STEEL_MEAN_CURVATURE_REDUCTION_COEFFICIENT = NOT_INTRODUCED
NEXT_ONLY = DIRECT_FEM_OUT_OF_PLANE_MODE_PROJECTION_BH032_AND_EQUAL_CONTRACT_BH050
```
