# NZ-SCCM — Case21 Airy-scalar current-R10 continuation

**Timestamp:** 2026-08-17 02:10 +08:00  
**Status:** EXECUTED / MECHANICS CLOSURE SELECTED / DIRECT-SOURCE RESULT CONVERGED / FORMAL ZERO-QUADRATURE RELEASE STILL OPEN

## 1. Why the five-free-coordinate route was not continued

The current task was resumed from the exact-R10 / General-D15 development line with the requirement to obtain an actual Case21 structural result rather than another intermediate integration gate.

A direct frozen-R10 continuation was first executed with the five membrane coordinates

\[
r=(r_0,r_{20},r_{22},s_{02},s_{22})
\]

all released independently through `Rm=0`.

That branch reproduced the previously identified nonlinear over-relaxation mechanism: it departs strongly from the classical Airy/FvK direction, develops very large coupled membrane coordinates, and ceases to represent the small membrane perturbation expected for Case21. This behavior is not a CAS or integration failure; it is a mechanics closure failure of the unconstrained five-coordinate nonlinear release.

Therefore the five functions are retained as the exact elastic Airy span, but they are no longer released as five independent nonlinear amplitudes for Case21 production development.

## 2. Selected membrane closure

For a square complete halfwave define

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right)
\]

and the exact classical Airy direction

\[
\mathbf a(\nu)=
\left[
-\frac{1+\nu}{4},
-\frac{1-\nu}{4},
\frac14,
-\frac{1-\nu}{4},
\frac14
\right]^T.
\]

The current membrane redistribution is represented by one internal generalized amplitude

\[
\boxed{\mathbf r=\lambda M\mathbf a(\nu)}.
\]

For `nu=0.18`,

```text
a = [-0.295,-0.205,+0.25,-0.205,+0.25]
```

This closure has three important properties:

1. in the linear-elastic limit its generalized equilibrium gives exactly `lambda=1` and reproduces the classical Airy/FvK solution;
2. it preserves the physically generated compatibility direction instead of allowing the five amplitudes to rotate into unrelated nonlinear softening modes;
3. `lambda` is still solved from the same frozen current material response; it is not fitted to Case21 capacity.

The internal scalar equilibrium is

\[
\boxed{R_A=\mathbf a^T\mathbf R_m=0}.
\]

Because `lambda` is an internal stationary coordinate, the outer amplitude equilibrium is still evaluated from the same current state and satisfies the envelope identity. The coupled path is obtained from

\[
R_q(D,q,\lambda)=0,
\qquad
R_A(D,q,\lambda)=0.
\]

The ultimate point is the first maximum of `P(D)` on the origin-connected branch.

## 3. Frozen Case21 data

```text
b = ell = 1220 mm
t = 19.30 mm
fc = 21.23 MPa
E0 = 20321 MPa
eps0 = 0.00209
nu = 0.18
q0 = 0.0025
A0 = 3.05 mm
rho_sx = rho_sy = 0.00375
Es = 200000 MPa
eps_y = 0.00265
kappa = 2.0005129533678754
rho = 0.1
eta = 0.0024993589726987125
R10 energy-smoothed peak h = 0.09799750427197301
R10 residual tension = 0.03
acc = 0.1072329249362415
at = 1-2^(-1/8)
```

The R10 current law is evaluated directly from the frozen source functions; no N48 coefficients are used in the direct-source audit reported below.

## 4. Direct-source continuation result

A deterministic full-halfwave Gauss-Legendre executor was used only as an independent continuum oracle. It is not promoted to the formal production operator.

The origin-connected `(Rq=0, RA=0)` path has a smooth first peak near

```text
D ~= 0.78879
q ~= 0.00180836
lambda ~= 0.08624
```

At the refined representative peak state (`144 x 144 x 76` audit):

```text
D = 0.7887924801
q = 0.0018083573
lambda = 0.08623596
M = 0.02907033478
Cb = 0.06754686155
A_increment = q*b = 2.20619585 mm
A_total = A0 + A_increment = 5.25619585 mm
```

The membrane coordinates are

```text
r0   = -0.00073954
r20  = -0.00051392
r22  = +0.00062673
s02  = -0.00051392
s22  = +0.00062673
```

and the load decomposition is

```text
Pc = 337.92303037 kN
Ps =  28.84479832 kN
Pu = 366.76782869 kN
```

Equilibrium checks at the same state:

```text
Rq = +6.25e-13 kN mm
RA = a^T Rm = +3.55e-15 (same residual units)
```

The five individual `Rm` components are not set to zero because the selected nonlinear membrane approximation space is intentionally one-dimensional; their Airy projection is the variational equation for the retained internal coordinate.

## 5. Numerical convergence of the direct-source oracle

At `D ~= 0.78887`, re-solving `(q,lambda)` on increasingly fine independent full-halfwave audit grids gave:

| audit grid | q | lambda | P / kN |
|---|---:|---:|---:|
| 64 x 64 x 36 | 0.00180813 | 0.08596091 | 366.771341 |
| 72 x 72 x 40 | 0.00180828 | 0.08608059 | 366.770509 |
| 80 x 80 x 44 | 0.00180839 | 0.08616005 | 366.769423 |
| 96 x 96 x 52 | 0.00180850 | 0.08624767 | 366.768496 |
| 112 x 112 x 60 | 0.00180856 | 0.08628935 | 366.768080 |
| 128 x 128 x 68 | 0.00180858 | 0.08630669 | 366.767919 |
| 144 x 144 x 76 | 0.00180859 | 0.08631512 | 366.767823 |

A separate local `D` scan on the 112 x 112 x 60 executor gave the fitted peak

```text
D_peak ~= 0.78879248
P_peak ~= 366.768085 kN
```

and the 144 x 144 x 76 evaluation at that `D` gave `366.767829 kN`. The remaining oracle discretization change is far below the material/model uncertainty and is used only to establish the current physical result.

## 6. Reinforcement state at the peak

The steel mesh remains elastic throughout the representative peak state.

```text
x-direction strain range:
+0.00029496 ... +0.00035355

y-direction strain range:
-0.00164881 ... -0.00159022

yield strain magnitude = 0.00265
```

Therefore no steel yield event or post-yield branch affects this Case21 result.

## 7. Comparison with experiment and with the old constrained r=0 backbone

Experiment:

```text
P_exp = 368.31274974 kN
```

Current Airy-scalar result:

```text
P_u = 366.76782869 kN
Delta = -1.54492106 kN
error = -0.419459 %
```

For comparison, a direct frozen-R10 `r=0` backbone audit using the same material source and high-order executor gives approximately

```text
D_peak ~= 0.84323
q_peak ~= 0.00178316
P_r0 ~= 368.73146 kN
```

Hence the compatibility-driven membrane redistribution changes the old constrained backbone by only

```text
Delta P = -1.96363 kN
relative = -0.53254 %
```

for Case21.

This resolves an earlier conceptual confusion: the classical membrane term is positive relative to the elastic buckling load, but releasing compatible in-plane redistribution does not have to increase capacity relative to the old `r=0` kinematic constraint. For Case21 the actual correction is small, as required by its small membrane driver, but it is slightly capacity-reducing relative to the constrained baseline.

## 8. Formal zero-spatial-integration status

The mechanics result above is now fixed independently of the exact integration backend. The direct-source Gauss executor is audit-only.

The formal project counters remain

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

The remaining production implementation task is narrower than before because the nonlinear membrane state is now `(D,q,lambda)` rather than `(D,q,r1..r5)`. The exact source-level R10 compact material DAG and General-D15 moment philosophy remain available for this final representation step.

No experimental load was used to choose `lambda`, any R10 parameter, or the peak state.

## 9. Current decision

```text
FIVE_FREE_CURRENT_MEMBRANE_AMPLITUDES = REJECTED_FOR_CASE21_NONLINEAR_PRODUCTION
AIRY_DIRECTION_SHAPE = RETAIN_EXACT
AIRY_SCALAR_INTERNAL_AMPLITUDE_lambda = ACTIVE_CASE21_CURRENT_MEMBRANE_CLOSURE
DIRECT_SOURCE_CASE21_RESULT = CONVERGED
CASE21_CURRENT_Pu_AUDIT = 366.768 kN
CASE21_EXPERIMENT_ERROR = -0.4195 percent
STEEL_AT_PEAK = ELASTIC
FORMAL_ZERO_QUADRATURE_NUMERIC_RELEASE = OPEN
Z6_BOUNDARY = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```
