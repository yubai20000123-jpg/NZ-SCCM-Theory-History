# CORRECTION — steel-face LE cannot yet certify the generalized section curvature path

**Date:** 2026-08-26  
**Status:** `SUPERSEDES_H1_HIGH_CONFIDENCE_AS_CAUSAL_DIAGNOSIS / NO_THEORY_CHANGE`

## 1. Why the prior H1 conclusion is too strong

The ODB extraction itself remains valid: BH050 upper and lower steel-face area-weighted `LE22` both become more compressive to the FEM peak, and their mean stresses also become more compressive. That proves a real FEM steel-face material-strain/stress trend.

However, the inference

```text
steel-face area-weighted LE22
    -> eps_y0,FEM
    -> kappa_y,FEM
    -> direct comparison with theoretical generalized eps_y0,kappa_y
```

is not yet an established apples-to-apples observable contract after R02/R06 postbuckling and local-yield projection.

R02 does not use the gross face strain directly as the mean material strain. For compression-positive `ex,ey`, its condensed membrane strains are

```text
mx = ex - cx*(U^2-A0^2)
my = ey - cy*(U^2-A0^2)
```

and the mean stress is evaluated from `mx,my`. Thus local postbuckling geometric strain changes the relation between the generalized/gross face strain and the material strain observable.

R06 further evaluates a local-buckling-first face resultant at the radial projected state

```text
eps_f(eta_y) = eta_y * eps_f
```

and returns the R02 mean stress/resultant at that projected state. Therefore the full terminal generalized face strain is not, after the R06 cap, a direct material-strain observable that should equal the area-weighted Abaqus `LE22`.

## 2. BH032 is the decisive control warning

Frozen BH032 theory root:

```text
eps_y0 = -0.00249442810080108
kappa_y = +4.78843761523297e-5 1/mm
z_f = 23 mm
```

Therefore

```text
chi_y,theory = 23*abs(kappa_y)/abs(eps_y0)
             = 0.4415203
```

while the ODB steel-LE reconstruction at the BH032 FEM peak gave

```text
chi_y,FEM_from_steel_LE = 0.0309536
```

—a factor of about 14.3 difference—despite the current R06 load prediction being approximately

```text
Pu,theory = 10.9405345 MN
Pu,FEM    = 10.99048 MN
error     ≈ -0.45%
```

Hence a large discrepancy between theoretical generalized `kappa_y` and the quantity reconstructed from averaged steel `LE22` exists even in the successful BH032 control case. It cannot therefore be used by itself as the causal explanation for the BH050 +9.3% load error.

For BH050 the analogous numbers are

```text
chi_y,theory_terminal ≈ 0.69985
chi_y,FEM_from_steel_LE_peak ≈ 0.09092
```

but the BH032 control shows that this mismatch must first be interpreted through a correct observable mapping.

## 3. What remains proven

```text
BH050 FEM upper steel LE22: MORE_COMPRESSIVE post-LY -> peak = PROVEN
BH050 FEM upper steel mean stress: MORE_COMPRESSIVE = PROVEN
BH050 theory terminal gross upper-face strain tends toward unloading = PROVEN
Direct identification of steel-LE-derived kappa with theoretical generalized kappa = NOT PROVEN
H1 as primary cause of Pu error = NOT YET PROVEN
R02/R06 as primary cause = ALSO NOT PROVEN
```

The prior report's ODB data are retained; only the causal interpretation is downgraded.

## 4. Correct next observable

The theoretical UHPC core N-M operator uses the through-thickness linear strain field directly:

```text
eps_y(z) = eps_y0 + kappa_y*z
```

without the R06 radial face projection. Therefore the cleanest FEM quantity for identifying the generalized section kinematics is the UHPC core `LE33` field, not the yielded/postbuckled steel `LE22` field.

At the same fixed section, project the area-weighted UHPC `LE33` field onto the best-fit linear through-thickness form

```text
eps_FE(z) = A_FE + B_FE*z
```

using integral moments, not point selection:

```text
A_FE = integral_A(eps dA) / integral_A(dA)
B_FE = integral_A(z*eps dA) / integral_A(z^2 dA)
```

for a symmetric core coordinate about its midsurface. Also report the weighted RMS residual of this linear projection. Then compare

```text
A_FE <-> theoretical eps_y0
B_FE <-> theoretical kappa_y
```

for BH032 and BH050.

If the UHPC-derived generalized curvature also shows the BH050-specific theory/FEM divergence while BH032 is compatible, then an upstream section-demand/equilibrium audit is justified. If the UHPC-derived curvature does not support the steel-derived H1 result, the previous H1 diagnosis must be rejected as an observable-mapping artifact.

## 5. Current decision boundary

```text
MARGUERRE_AIRY_REPAIR = NOT AUTHORIZED
SECTION_EQUILIBRIUM_REPAIR = NOT AUTHORIZED
R02_R06_REPAIR = NOT AUTHORIZED
NEXT_TASK = UHPC_CORE_LINEAR_STRAIN_PROJECTION_OBSERVABLE_AUDIT
```

No comparator may be used to retune theory or select roots.