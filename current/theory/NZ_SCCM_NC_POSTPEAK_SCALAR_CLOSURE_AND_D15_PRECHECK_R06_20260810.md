# NZ-SCCM NC POSTPEAK SCALAR CLOSURE AND D15 PRECHECK R06

**Date:** 2026-08-10

## 1. Identity and source basis

This is a continuation of the existing G18/G20/G27 unified current-map route. No 2D material refit, no spatial quadrature, no Case21/Swartz Pu calibration.

Nguyen Eqs. 3.69–3.73 use a post-crushing bilinear law: `sigma=sigma_p` at `eps=eps_p`, linear descent to `0.1 sigma_p` at `eps=gamma2 eps_p`, followed by a residual plateau with zero tangent. Current source baseline uses `gamma2=10`.

The exact source contains tangent jumps at the peak and residual onset. G20/G21 already authorize C1/C2 regularization for the memoryless analytic current surface.

## 2. R06 C2 postpeak compression closure

Use

```text
s=(-lambda-1)/9,      0<=s<=1
sigma/fc=-1+0.9 q(s)
```

The exact Nguyen source branch is `q=s`.

R06 retains that source line exactly except for two endpoint C2 bridges of width

```text
delta_s=0.05
Delta_lambda=0.45 per endpoint
```

The normalized start bridge is

```text
g(tau)=3 tau^5-8 tau^4+6 tau^3
```

satisfying

```text
g(0)=g'(0)=g''(0)=0
g(1)=1, g'(1)=1, g''(1)=0
```

and the end bridge is symmetric.

The width was selected only by a material-level gate: local additional compression relative to the exact source line must remain <=1% fc.

Executed values:

```text
max additional compression = 0.888889% fc
max conservative reduction = 0.888889% fc
U(-1)=-1
U'(-1)=0
U(-10)=-0.1
U'(-10)=0
```

Therefore:

```text
NC_POSTPEAK_C2_SCALAR_TARGET = PASS
```

This C2 target is a material target for later unified compilation, not a runtime material-state branch.

## 3. Full R06 scalar target used in representation screening

```text
[-10,-1]             R06 C2 source-faithful postcrush target
[-1,0]               normalized Saenz compression skeleton
[0,alpha1*xcr]       retained current smooth tensile benchmark
```

No structural Pu was used.

## 4. Direct polynomial candidate

A degree-64 direct polynomial in `lambda` is the first tested direct polynomial to satisfy the simple R06 material screen:

```text
max stress error              = 1.981970% fc
stress P95                    = 0.185018% fc
tangent P95                   = 3.365831% of initial tangent
local tangent max             = 185.101% in narrow transition neighborhoods
```

The main advantage is formal: a polynomial scalar matrix function has guaranteed finite polynomial/Beta-D15 closure after invariant reduction.

The main disadvantage is Gate-C footprint. Generic Cayley-Hamilton reduction of degree 64 produces:

```text
A(J1,J2) unique invariant pairs = 1025
B(J1,J2) unique invariant pairs = 1056
union unique (J1,J2) pairs      = 1088
A+B pair count                   = 2081
```

Thus:

```text
GLOBAL_LAMBDA_N64 = PASS_MATERIAL_SCREEN / HOLD_GATE_C
```

## 5. Softsign compactification

```text
chi_s=lambda/sqrt(1+lambda^2)
```

At degree 48:

```text
max stress error = 0.988210% fc
tangent P95      = 1.991297% of initial tangent
```

It reduces scalar approximation order, but direct D15 closure of the resulting algebraic degree-4 structural kernel has not been demonstrated.

```text
SOFTSIGN_N48 = PASS_MATERIAL_SCREEN / HOLD_KERNEL
```

## 6. Möbius compactification

Define

```text
chi_M=lambda/(1-lambda)
```

with material pole `lambda_p=1`, which lies outside the current NC material-native tension domain (`lambda_M,max=0.49987179454`).

For the 2x2 equivalent-uniaxial tensor `E`:

\[
\boxed{\chi_M(E)=E(I-E)^{-1}=\frac{E-J_2 I}{1-J_1+J_2}}
\]

Therefore the entire spectral denominator becomes one invariant scalar:

\[
\boxed{\Delta_M=1-J_1+J_2=(1-\lambda_+)(1-\lambda_-)}.
\]

On the full NC material square:

```text
Delta_M >= (1-lambda_M,max)^2 = 0.250128221897 > 0
```

so there is no pole inside the material-admissible domain and no eigenvalue-state partition is required.

Material screens:

```text
Möbius n=24:
  max stress error = 2.081055% fc
  tangent P95      = 4.417013%

Möbius n=48:
  max stress error = 0.984912% fc
  tangent P95      = 2.369704%
```

After Case21 substitution:

\[
\Delta_M=1-I_1+I_2=A_0(s,t)+A_1(s,t)\zeta+A_2(s,t)\zeta^2,
\]

where `s=sin^2 X`, `t=sin^2 Y`. Explicitly, with `r=sqrt(s t)`:

```text
A0 = -D^2 nu - D M nu s t + D M nu s + D M s t - D M t
     - D nu + D + 2 M s t - M s - M t + 1

A1 = B D nu r - B D r - B M r s - B M r t + 2 B M r - 2 B r

A2 = B^2(s+t-1)
```

For fixed `s,t`, integer-power thickness integrals

\[
\int\frac{d\zeta}{(a+b\zeta+c\zeta^2)^m}
\]

are elementary-recursive and reduce to rational endpoint terms plus the `m=1` log/atan/artanh master.

However, the remaining in-plane master contains the quadratic discriminant as a nontrivial polynomial in `s,t`. R06 has not proved a small Beta/Appell/Carlson closure.

Therefore:

```text
MOBIUS_COMPACTIFICATION = PROMOTED_FOR_KERNEL_SCREEN
MOBIUS_D15_KERNEL = HOLD_NOT_YET_CLOSED
```

## 7. R06 head-to-head interpretation

```text
Direct lambda polynomial:
  integration identity = solved
  material representation = acceptable at n=64
  Gate C footprint = high

Softsign:
  material representation = efficient
  exact structural kernel = unresolved

Möbius:
  no spectral square root in matrix form
  one invariant denominator Delta_M
  exact remaining 2D master = unresolved
```

There is no justification to choose a compiler from material error alone.

## 8. Formal R06 decision

```text
R06 = PASS_POSTPEAK_C2__HOLD_FINAL_COMPILER
NC_POSTPEAK_C2_SCALAR_TARGET = PASS
GLOBAL_LAMBDA_N64 = PASS_MATERIAL_SCREEN / HOLD_GATE_C
SOFTSIGN_N48 = PASS_MATERIAL_SCREEN / HOLD_KERNEL
MOBIUS_N24_N48 = PROMISING / HOLD_KERNEL
CASE21_PU = NOT_RUN
SWARTZ24_PU = NOT_RUN
ROUTE_SWITCH = NO
```

## 9. Next task

```text
R07_HEAD_TO_HEAD_KERNEL_COMPLEXITY_DECISION_GLOBAL_POLY64_VS_MOBIUS24
```

R07 is not allowed to fit a new material family. It must compare only two already executed candidates:

1. degree-64 direct polynomial: exact moment recurrence and actual D15 operation/term footprint without naive full expansion;
2. degree-24 Möbius: exact thickness elimination of `Delta_M^{-m}`, parity/symmetry reduction, then a hard classification of the remaining 2D master.

Decision rule:

```text
if Möbius requires PF / large ODE / large master connection -> FAIL
if direct polynomial has an auditable finite recurrence of acceptable size -> prefer direct polynomial
otherwise HOLD and return to material target, not blind compiler search
```
