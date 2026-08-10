# NZ-SCCM MATERIAL-NATIVE 1D PRIMITIVE REFORMULATION R05

**Date:** 2026-08-10  
**Status:** `PASS_DOMAIN_AND_COMPACTIFICATION_SCREEN__HOLD_FINAL_NC_SCALAR`  
**Route switch:** NO

## 1. Identity

Same G18/G20/G27 current-map route. No 2D surface refit, no formal spatial quadrature, no Case21/Swartz Pu calibration.

R05 begins from the R04 correction that the production scalar compiler must be qualified on the material constitutive domain, not the Swartz24 reachable spectrum.

## 2. Material-native NC scalar domain

Use

\[
\lambda=\varepsilon_u/\varepsilon_{p,c},
\]

with compression negative.

Source landmarks are

\[
\lambda_{c,res}=-\gamma_2=-10,
\quad
\lambda_{c,peak}=-1,
\quad
\lambda_0=0,
\]

\[
\lambda_{cr}=\rho/\kappa,
\quad
\lambda_{t,res}=\alpha_1\rho/\kappa,
\]

with `alpha1=10`, source `gamma2=10`, and project-conservative `alpha2=0.30`.

For the current ordinary-concrete material instance

```text
fc     = 21.23 MPa
E0     = 20321 MPa
eps_p  = 0.00209
rho    = ft/fc = 0.10
kappa  = E0 eps_p / fc = 2.0005129533678754
lambda_cr = 0.04998717945397425
```

therefore

\[
\boxed{
\Lambda_{M,NC}^{active}
=[-10,\ 0.49987179453974245]
}
\]

This interval is defined by material source landmarks. It is not derived from Case21 or Swartz24 geometry.

## 3. Hard landmarks and allowed regularization

Hard:

- `sigma(0)=0`;
- initial elastic tangent;
- compression peak position/value and zero tangent;
- tensile cracking/peak scale.

Governed C1/C2 conservative regularization remains allowed for:

- source postcrush evolution toward the residual level;
- Foster tension-stiffening transition toward the residual level;
- finite source state handoff jumps/history that are deliberately not retained as a runtime material-state machine.

## 4. New material-level blocker exposed by the correct domain

A pure Saenz continuation is not a valid final deep-postpeak closure over the full source-native interval.

At

\[
\lambda=-\gamma_2=-10,
\]

its normalized stress is

\[
\sigma_{Saenz}/f_c=-0.1980605304506671,
\]

while the Nguyen source postcrush residual landmark is approximately

\[
\sigma_{res}/f_c=-0.10.
\]

The Saenz continuation therefore retains about `1.980605` times the magnitude of the source residual at this endpoint.

This does **not** reopen the discarded history-state machine. It means that the G21-approved smooth conservative postpeak replacement must now be frozen explicitly as a one-dimensional material target before any final production coefficients are accepted.

## 5. Representation candidates actually executed

The frozen smooth source-shaped `U(lambda)` is used here only as a representation benchmark/oracle. It is not promoted to source truth.

### Candidate A — one global polynomial in lambda

A single Chebyshev polynomial is fitted directly on the full material-native active interval.

Observed behavior: the large interval together with narrow tensile features produces slow convergence and poor tangent behavior. It is not preferred.

### Candidate B — material-scale compactification

Define

\[
\boxed{
\chi(\lambda)=\frac{\lambda}{\sqrt{\lambda^2+1}}
}
\]

where the scale `1` is the normalized compression-peak material scale, not a structurally calibrated parameter.

Then use

\[
\boxed{
U_n(\lambda)=\sum_{j=0}^{n}a_jT_j(z(\chi))
}
\]

where `z` maps the finite `chi` interval corresponding to `Lambda_M,NC^active` linearly to `[-1,1]`.

This changes the approximation geometry without introducing a material-state partition.

### Candidate C — degree-9 landmark Hermite polynomial in chi

Values and tangents were enforced exactly at five material landmarks. The resulting global polynomial oscillated severely and is rejected.

## 6. Executed material benchmark results

### Direct lambda polynomial

```text
n=16: stress P95=2.0004% fc, max=8.4155% fc; tangent P95=13.4949% of initial tangent
n=24: stress P95=0.9286% fc, max=5.4155% fc; tangent P95= 6.9042%
n=32: stress P95=0.6004% fc, max=4.0395% fc; tangent P95= 6.4718%
```

### Compactified softsign coordinate

```text
n=16: stress P95=0.4118% fc, max=2.4134% fc; tangent P95=3.5923%
n=24: stress P95=0.1276% fc, max=1.5627% fc; tangent P95=2.3531%
n=32: stress P95=0.0692% fc, max=1.1274% fc; tangent P95=1.9274%
```

The local maximum tangent error remains much larger than P95 because the benchmark itself contains narrow transition ridges. Therefore `n=24` is retained only as the preferred **material representation screen candidate**, not as a production material law.

### Landmark Hermite

```text
stress P95 = 278.871%
stress max = 637.629%
predicted stress range = [-2.858, 5.658] fc
```

Hence:

```text
LANDMARK_HERMITE_CHI_DEG9 = FAIL_SHAPE_OSCILLATION
```

## 7. Explicit n=24 compactified candidate coefficients

For

\[
U_{24}(\lambda)=\sum_{j=0}^{24}a_jT_j(z(\chi)),
\]

the executed coefficients are

```text
[-0.38049750626801876,
  0.46214650922308365,
  0.16581119072094055,
 -0.29885874435694976,
  0.06595966423250248,
 -0.007932761229459124,
  0.04809867363422755,
 -0.015510262890830547,
 -0.0009227675022769609,
 -0.017198305779106214,
  0.007239746262201731,
  0.002654531018208474,
  0.008264778907591685,
 -0.0038280445595166098,
 -0.002091827649876472,
 -0.003822952548261491,
  0.0030487174840213623,
  0.0022965627142429892,
  0.002470546046856801,
 -0.0017322946952345714,
 -0.0012636996252178288,
 -0.0007135708194736261,
  0.0020709420416114193,
  0.001625585937042219,
  0.0015281764663161055]
```

These coefficients are **not production coefficients**. They belong to the frozen smooth benchmark screen only.

## 8. Why compactification is a genuine complexity reduction

`chi=lambda/sqrt(lambda^2+1)` generates only one quadratic algebraic extension. Any finite polynomial in `chi` remains in the same degree `<=2` scalar field; increasing polynomial degree does not increase the algebraic field degree.

After the structural substitution

\[
\lambda_\pm=\mu\pm\sqrt{Q},
\]

the generic algebraic extension upper bound becomes `<=4`.

R04 found the old `Pi+H1+H10` source-shaped `U` to have scalar upper degree `<=8` and structural upper degree `<=16`. Thus the compactified candidate lowers the algebraic nesting substantially.

This is a representation reduction, not a new material theory.

## 9. Relation to G27 production grammar

G27 remains

\[
\boldsymbol\sigma
=U(\mathbf E_u)+J_2[A(J_1,J_2)\mathbf I+B(J_1,J_2)\mathbf E_u].
\]

Production does **not** require permanent retention of the old source-shaped `C,T,T^8` primitive grammar. Those primitives remain benchmark/reference objects. R05 therefore focuses first on the compact uniaxial scalar master `U`; the low-parameter multiaxial interaction layer `A,B` remains a separate later material-closure task.

## 10. R05 decision

```text
MATERIAL_NATIVE_1D_PRIMITIVE_REFORMULATION_R05
= PASS_DOMAIN_AND_COMPACTIFICATION_SCREEN__HOLD_FINAL_NC_SCALAR

MATERIAL_NATIVE_DOMAIN_CONTRACT = PASS
GLOBAL_LAMBDA_POLYNOMIAL = NOT_PREFERRED
LANDMARK_HERMITE_CHI_DEG9 = FAIL_SHAPE_OSCILLATION
SOFTSIGN_DELTA1_N24 = PREFERRED_MATERIAL_SCREEN_CANDIDATE_NOT_PRODUCTION
SOFTSIGN_DELTA1_N32 = DIAGNOSTIC_UPPER_ORDER_ONLY
FINAL_NC_SCALAR_U = OPEN
CASE21_PU = NOT_RUN
SWARTZ24_PU = NOT_RUN
ROUTE_SWITCH = NO
```

The final NC scalar stays open specifically because the deep-postpeak smooth-conservative closure has not yet been uniquely frozen on the newly correct material-native domain.

## 11. Unique next task

```text
NC_POSTPEAK_SCALAR_CLOSURE_AND_SOFTSIGN_D15_KERNEL_PRECHECK_R06
```

R06 must do two things before any structural Pu calculation:

1. freeze a low-parameter C1/C2 conservative NC postpeak scalar continuation consistent with the source peak/residual landmarks;
2. substitute the compactified `P_n(chi)` representation into the Case21 invariant algebra and determine whether its degree-4 structural algebra reduces to finite D15/Beta or a genuinely small Carlson/Appell/other named kernel.

If the compactified kernel again requires a large PF/ODE system, it fails Gate C immediately.
