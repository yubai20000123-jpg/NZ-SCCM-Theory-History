# NZ-SCCM — NC + steel-shell benchmark simplification and R10 strength-scaling correction

Date: 2026-08-14
Status: CURRENT_PRIMARY / LOCKED GOVERNANCE CORRECTION

## 1. Internal steel webs in the first Zhou four-edge SSSS benchmark

For the current first NC + steel-shell benchmark, the intermediate/internal steel webs of Zhou's multi-cell wall are **not modeled as steel structural components**.

```text
INTERNAL_STEEL_WEBS_AS_STEEL = NO
INTERNAL_WEB_STEEL_LOAD = NO
INTERNAL_WEB_STEEL_KZ = NO
INTERNAL_WEB_STEEL_Rq = NO
INTERNAL_WEB_STEEL_D15_OPERATOR = NO
INTERNAL_WEB_VOLUME = TREATED_AS_CONCRETE
OUTER_STEEL_SHELL = RETAINED
```

Thus the active model is the simplified parent system

```text
continuous concrete core
+ outer bonded steel-shell layer(s)
-> same Nguyen second-order D,q field
-> concrete R10/N48-C1-MM + steel-shell Yun ideal-EP module
-> exact general-D15 moments
-> Rq=0 + local shell event equation + L/KZ
```

The original Zhou FE specimen/formula may still be quoted as an external source comparator, but any comparison shall explicitly state that the NZ-SCCM benchmark intentionally replaces internal steel webs by concrete and is therefore not a geometrically identical FE reproduction.

## 2. Ordinary-concrete strength scaling

The R10 normalized material **curve family/form is not refit specimen by specimen**. Its governing dimensional stress is

\[
\sigma=f_c S,
\]

with normalized strain tensor

\[
X=E_u/\varepsilon_0.
\]

The currently frozen R10 shape parameter is

\[
\kappa=E_0\varepsilon_0/f_c.
\]

Therefore a pure strength-amplitude scaling is exact only when the normalized R10 shape parameters, especially `kappa`, remain fixed. Under that rule,

\[
\boxed{\sigma/f_c=S(X;\kappa,\nu,\rho,\ldots)}
\]

is the same normalized curve for different concrete strengths.

For a new concrete strength `fc`, do **not** refit the R10 curve to structural Pu. Instead:

1. keep the frozen normalized R10 functional form and shape constants;
2. take `fc` from the material/source data;
3. use a source-consistent `E0` relation or measured `E0`;
4. enforce the frozen normalized shape through
   \[
   \varepsilon_0=\kappa f_c/E_0
   \]
   when `kappa` is to remain invariant;
5. rescale dimensional stress by `fc`;
6. regenerate the specimen-specific reachable normalized material interval `[lambda_a,lambda_b]` from the continuous strain field;
7. compile N48-C1/MM on that declared interval using the **same objective definition** and same normalized R10 target.

Hence:

```text
R10_NORMALIZED_FUNCTIONAL_FORM = FROZEN
R10_SHAPE_REFIT_BY_STRENGTH = NO
FC = DIMENSIONAL_STRESS_SCALE
EPS0 = STRAIN_SCALE CONSISTENT WITH E0 AND FROZEN KAPPA
COMPILER_INTERVAL = SPECIMEN-SPECIFIC
COMPILER_OBJECTIVE_DEFINITION = UNCHANGED
STRUCTURAL_PU_CALIBRATION = NO
```

If independent source data require a materially different `kappa`, that is a material-source question and must be handled explicitly; it shall not be inferred from the structural ultimate load.
