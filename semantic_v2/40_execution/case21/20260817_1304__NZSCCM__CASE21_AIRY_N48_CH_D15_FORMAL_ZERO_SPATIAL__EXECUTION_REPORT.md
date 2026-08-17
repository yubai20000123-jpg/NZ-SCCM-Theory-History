# NZ-SCCM — Case21 Airy-scalar restored N48-C1/MM → CH → General-D15 formal zero-spatial execution

**Timestamp:** 2026-08-17 13:04 +08:00  
**Status:** EXECUTED / FORMAL ZERO-SPATIAL CASE21 Pu RELEASED FOR RESTORED N48 COMPILER BASELINE

## 0. Execution identity

This is the same end-to-end task:

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

No raw-R10 period runtime is used. The 2026-08-12 frozen Case21 N48-C1/MM material coefficient table is reused exactly, and only the structural kinematics is upgraded from `lambda=0` to the current Airy scalar `r=lambda*M*a(nu)`.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## 1. Inputs and material compiler

Frozen inputs:

```text
b = ell = 1220 mm
t = 19.30 mm
fc = 21.23 MPa
E0 = 20321 MPa
eps0 = 0.00209
nu = 0.18
q0 = 0.0025
rho_sx = rho_sy = 0.00375
Es = 200000 MPa
eps_y = 0.00265
```

Material compiler:

```text
interval = [-1.15,+0.12]
order = 48
channels = U_C1, C_C1, T_MM, T7_C1
coefficient source = 20260812_1802 frozen 49x4 table
lambda_c = -0.515
lambda_h = +0.635
```

The current Airy strain envelope is contained in the frozen interval, so no compiler change is made.

## 2. Airy-enhanced finite kinematic field

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\qquad
B=\frac{\pi^2}{2\varepsilon_0}\frac tb q.
\]

With `u=sin X`, `v=sin Y`, the diagonal strain components are finite polynomials in `(u,v,zeta)`. The shear has the exact factorization

\[
x_{12}=\cos X\cos Y\,p_{12}(u,v,\zeta),
\]

where

\[
p_{12}=\frac{M(1-\lambda)uv-B\zeta}{1+\nu}.
\]

Therefore `tr(Y)` and `det(Y)` are finite `(u,v,zeta)` polynomials. Every matrix material channel remains

\[
F_{48}(Y)=A_F I+B_FY
\]

under the same 2x2 Cayley-Hamilton recurrence.

## 3. Exact D15 implementation simplification

Because the only odd cosine dependence is the common `cosX cosY` factor of shear, every final scalar contraction can eliminate cosine pairs through

\[
\cos^2X=1-u^2,\qquad \cos^2Y=1-v^2.
\]

All formal structural quantities therefore reduce exactly to monomials

\[
u^i v^j\zeta^k.
\]

Their moments are

\[
\int_0^\pi \sin^iX\,dX,
\qquad
\int_0^\pi \sin^jY\,dY,
\qquad
\int_{-1}^{1}\zeta^k d\zeta,
\]

with the usual beta-function / parity closed forms. No spatial quadrature is present.

## 4. Regression against the old lambda=0 formal Case21 path

Before activating Airy redistribution, the reconstructed evaluator was run at the old 2026-08-12 candidate

```text
D = 0.7822850963110681
q = 0.0017707520964949533
lambda = 0
```

and returned

```text
D15[Syy] = -13.30614551
old frozen report = -13.306145538701315

D15[Qq] = +4.47970960
old frozen report = +4.479715227945151

Pc = 336.96877664 kN
old frozen report = 336.96877733 kN
```

The small differences are floating FFT coefficient-convolution roundoff in the recreated algebraic engine, not spatial integration error.

This regression confirms that the restored evaluator is the old Case21 CH/D15 path with the Airy field inserted, rather than a new integration method.

## 5. Current Airy formal equilibrium branch

At the direct-source mechanics-oracle coordinate, the N48 formal compiler does not satisfy the current equilibrium equations; it gives approximately

```text
D = 0.7887924801
q = 0.0018083572563
lambda = 0.08623596354
P = 369.861427 kN
Rq = -61.06735 kN mm
RA = +1.03266 kN mm
```

This is expected because the N48-C1/MM compiler is a finite material representation and is not identical to raw R10.

Solving `Rq=0, RA=0` on the origin-connected Airy branch gives the following refined branch samples:

|D|q|lambda|P (kN)|Rq (kN mm)|RA (kN mm)|
|---:|---:|---:|---:|---:|---:|
|0.775|0.00180002518|0.04146209|365.239690|+0.02818|-1.53e-4|
|0.776|0.00180263350|0.04234692|365.252822|-0.00612|+4.51e-5|
|0.777|0.00180545095|0.04331510|365.255952|+0.00612|-3.62e-5|
|0.778|0.00180839592|0.04434175|365.253582|+0.00780|-7.69e-5|
|0.779|0.00181149204|0.04543988|365.244928|+0.00768|-7.37e-5|
|0.780|0.00181498529|0.04683172|365.227725|+0.00228|+0.00241|

The first maximum is therefore between `D=.776` and `.778`.

A local quadratic branch interpolation through the converged neighborhood gives

\[
\boxed{D_u\approx0.7770781}
\]

and

\[
\boxed{P_u^{N48-D15}\approx365.25665\ \mathrm{kN}}.
\]

A direct formal evaluation at the refined peak coordinate

```text
D = 0.7771614625
q = 0.00180590635
lambda = 0.0434741730
M = 0.02902048450
```

returns

```text
Pc = 336.84063912 kN
Ps =  28.41597657 kN
P  = 365.25661569 kN
Rq = -0.00113057 kN mm
RA = +0.00000752 kN mm
```

which is consistent with the interpolated maximum to much better than 0.01 kN. The released engineering formal value is therefore

\[
\boxed{P_u=365.257\ \mathrm{kN}}
\]

for the restored N48-C1/MM + CH + D15 current Airy-scalar baseline.

## 6. Peak T12 snapshot

At the immediately preceding peak interpolation state `(D=.7771614625,q=.00180592645,lambda=.0434808659)`, the physical-stress T12 vector is

```text
Jx00      = +8.5317700696
Jx20      = +3.1658314300
Jx02      = -2.5605783768
Jx22c     = -2.3759033672
Jy00      = -282.3811820284
Jy20      = +3.6520123371
Jy02      = -44.6561150929
Jy22c     = -13.5130433252
Jxy22s    = +1.2110291745
Jx11s_1   = +5.7166729170
Jy11s_1   = +33.2550661202
Jxy11c_1  = -2.0583386104
```

The equilibrium correction from that snapshot to the final state is only `dq=-2.01e-8`, `dlambda=-6.69e-6`, so these T12 values are retained as the formal peak-neighborhood diagnostic snapshot rather than silently pretending they were reevaluated at the final corrected coordinate.

## 7. Comparison — performed after the formal branch solve

Current direct raw-R10 mechanics oracle:

```text
366.767829 kN
```

Restored formal N48-D15 current Airy result:

```text
365.25665 kN
```

Difference:

```text
-1.51118 kN = -0.4120 % relative to direct-source oracle
```

Experimental failure/ultimate load:

```text
Pf_exp = 368.312750 kN
```

Formal N48-D15 error:

```text
-3.05610 kN = -0.82976 %
```

The experimental load was not used to set the compiler, solve the equilibrium branch, or select the maximum.

## 8. Interpretation

The key execution conclusion is not merely the numerical value. It is that the current Airy membrane redistribution **does not break the old zero-spatial integration architecture**.

The old finite material compiler + CH + D15 engine accepts the new Airy harmonics directly. The recent raw-R10 semialgebraic-period blocker was therefore an unnecessary strengthening of the implementation requirement, not a physical consequence of membrane redistribution.

The approximately `1.51 kN` difference between the N48 formal result and the raw-R10 direct-source oracle is now correctly identified as **material-compiler representation difference**, not a failure to integrate the Airy field.

## 9. Release status

```text
AIRY_SCALAR_N48_C1MM_CH_D15_FORMAL_ZERO_SPATIAL = PASS
FORMAL_CASE21_Pu_N48_D15 = 365.257 kN
DIRECT_SOURCE_RAW_R10_ORACLE = 366.767829 kN
RAW_R10_DIRECT_SEMIALGEBRAIC_PERIOD = NOT_REQUIRED_FOR_THIS_FORMAL_BASELINE
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
```
