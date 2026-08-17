# NZ-SCCM — 零空间离散 / 有限 current operator / 真无限解析表示 / exact-D15 当前理论总锁定

**Timestamp:** 2026-08-17 18:24 +08:00  
**Status:** CURRENT_GOVERNING / CANONICAL_LOCK  
**User judgement:** 当前成型过程作为现阶段最完善理论锁定。

## 1. 一句话定义

NZ-SCCM 当前正式理论是：

> **连续域、零空间离散、零空间数值积分的解析级数—精确矩计算。**

形式链：

```text
actual specimen geometry / SSSS boundary
-> choose the mechanically controlling complete representative halfwave
-> ONE_CONTINUOUS_COMPLETE_HALFWAVE
-> Nguyen second-order finite trigonometric-thickness strain field
-> finite current material operator M(epsilon)
-> exact true-infinite analytic representation of the composed continuous material field
-> nth analytic term
-> exact 2x2 Cayley-Hamilton reduction
-> exact General-D15 continuous-domain moment
-> n -> infinity target sum
-> finite P, Rq, RA and same-source tangent/Jacobian
-> finite coupled equilibrium/limit solve
-> Pu
-> comparator / experiment only after theoretical result is frozen
```

## 2. Formal spatial counters

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

`N_formal_spatial_subdomains=1` means one continuous complete representative halfwave. It does **not** mean one numerical cell.

## 3. Continuous integration remains part of mechanics

Axial force and generalized residuals remain continuum integrals, e.g.

\[
P=-\int_\Omega \sigma_y\,d\Omega,
\qquad
R_q=\int_\Omega \boldsymbol\sigma:\boldsymbol\varepsilon_{,q}\,d\Omega.
\]

The project prohibition is **not** against the mathematical integral. The prohibition is against replacing it by spatial-point sums such as Gauss, Simpson, adaptive quadrature, collocation, material-point grids or spatial cells.

General-D15 evaluates the continuous integral analytically through exact trigonometric/thickness moments.

## 4. Material operator is finite

R10 ordinary-concrete material physics is a finite current operator

\[
\boldsymbol S=\mathcal M_{R10}(\boldsymbol E).
\]

Likewise an admissible steel current map is a finite function of its local strain/current trial state.

The word `infinite` does **not** describe the material law. It describes an exact analytic representation of the finite nonlinear composition

\[
\mathcal M(\boldsymbol E(X,Y,z)).
\]

Any statement treating “R10 itself” as an infinite nonlinear constitutive model is superseded by this lock.

## 5. True-infinite analytic representation is not spatial discretization

For a material function

\[
F(\lambda)=\sum_{n=0}^{\infty}f_nT_n(\widehat\lambda),
\]

`n` is a function-series index. It is not a spatial point, structural node, element, material point, thickness layer, or Ritz/spectral structural DOF.

A computational partial sum

\[
F^{(N)}=\sum_{n=0}^{N}f_nT_n
\]

is only a numerical evaluation of the formally defined infinite sum. It does not create a formal material order `N48/N96/...`, and it does not create spatial discretization.

The correct terminology is `series summation / analytic-series evaluation`, not `spatial discretization`.

## 6. Cayley-Hamilton recurrence is exact algebra

For

\[
Y=(E-c_0I)/h,\quad \tau=\operatorname{tr}Y,\quad \delta=\det Y,
\]

\[
Y^2=\tau Y-\delta I.
\]

Hence

\[
T_n(Y)=p_nI+q_nY,
\]

with

\[
p_{n+1}=-2\delta q_n-p_{n-1},
\qquad
q_{n+1}=2p_n+2\tau q_n-q_{n-1}.
\]

This is an exact 2x2 matrix identity. High-order `T_n(Y)` generation is algebraic recursion, not spatial discretization.

## 7. D15 exact moments are analytical integration, not quadrature

For every analytic term, General-D15 evaluates exact moments such as

\[
\int_0^\pi\sin^mX\,dX
=\sqrt\pi\frac{\Gamma((m+1)/2)}{\Gamma((m+2)/2)},
\]

and

\[
\int_{-1}^{1}\zeta^k\,d\zeta
=0\quad(k\ \text{odd}),
\qquad
=\frac{2}{k+1}\quad(k\ \text{even}).
\]

Thus `D15[W:S_n]` generation is exact symbolic/analytic moment contraction. It is not numerical quadrature.

## 8. Infinite target and finite physical solve

If

\[
S=\sum_{n=0}^{\infty}S_n,
\]

then for a D15 target functional

\[
J=\sum_{n=0}^{\infty}D15[W:S_n].
\]

Under the established convergence of the source series,

\[
\lim_{N\to\infty}D15[W:S_N]
=D15[W:S_{current}].
\]

After the infinite analytic sum is evaluated, the series index disappears. The remaining structural unknowns are low-dimensional generalized coordinates such as

\[
D,\ q,\ \alpha\quad(\text{or }\lambda_A=\alpha/M).
\]

The ultimate state is obtained from the same current operator through finite equilibrium/limit equations, e.g.

\[
R_q=0,\qquad R_A=0,
\]

plus the connected-branch first limit / bordered-Jacobian condition.

## 9. Steel/reinforcement rule

Steel or reinforcement enters the total `P`, `Rq`, `RA` and same-source derivatives **before** solving the coupled equations. A final scalar post-addition of independently solved material capacities is not the governing theory.

For finite steel maps with yield/current caps, the material function may also be represented by a true analytic series and contracted by exact D15 moments. This does not authorize spatial elastic/plastic cells.

## 10. Production prohibitions retained

The following remain prohibited in the formal production operator:

- spatial Gauss / Simpson / adaptive quadrature;
- spatial Chebyshev collocation;
- material-point production grid;
- spatial cells / adaptive spatial subdivision;
- FE-like spatial discretization;
- experiment-guided root/order/parameter selection;
- panel-level surrogate;
- treating a finite analytic-series evaluation order as a new material model;
- Zhou/Winter/experiment as a second Pu solver.

Direct continuum numerical quadrature may exist only as an independent audit oracle and cannot produce or select the formal result.

## 11. Current terminology lock

Use:

```text
CONTINUUM INTEGRAL                 = YES
FORMAL SPATIAL NUMERICAL INTEGRAL  = NO
FORMAL SPATIAL DISCRETIZATION      = NO
ANALYTIC MATERIAL SERIES           = YES
SERIES NUMERICAL EVALUATION        = YES, evaluation only
CAYLEY-HAMILTON                     = EXACT ALGEBRA
GENERAL-D15                         = EXACT CONTINUOUS-DOMAIN MOMENTS
FINAL STRUCTURAL SOLVE              = LOW-DIMENSIONAL COUPLED ROOT
```

Preferred description:

> **NZ-SCCM：零空间离散、零空间数值积分的 continuous-domain / analytic-series / exact-moment matrix theory.**

## 12. Supersession

This lock supersedes any earlier wording that:

1. describes R10 itself as an “infinite nonlinear target sequence”;
2. describes the analytic-series index `n` as a spatial discretization degree;
3. interprets finite partial-sum evaluation as a formal N48/N96 material model;
4. implies that computer-assisted analytic calculation requires spatial numerical quadrature.

The mathematical content of the 2026-08-17 Stage-I/II/III true-infinite derivations and the Case21/Z6 joint execution is retained, but interpreted under the precise identities above.
