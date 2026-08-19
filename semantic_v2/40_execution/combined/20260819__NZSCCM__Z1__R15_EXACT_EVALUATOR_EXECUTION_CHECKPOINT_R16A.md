# NZ-SCCM Z1 — R15 exact evaluator execution checkpoint R16A

**Date:** 2026-08-19  
**Identity:** EXECUTION CHECKPOINT / ZERO DISCRETIZATION / NOT A THEORY PROMOTION

## 0. Governance

```text
spatial sampling       = 0
spatial quadrature     = 0
material points        = 0
finite-prefix evidence = 0
numerical ODE stepping = 0
```

No historical Z1 nonlinear root or Pu is used as solve input, calibration target, or root-selection criterion.

## 1. Z1 front end already independently closed

```text
a_phys = 12000 mm
b      = 6000 mm
tc     = 92 mm
ts     = 4 mm per face
rho_w  = 0.02
fc     = 30.4 MPa
eps0   = 0.0018712490394580678
Es     = 206000 MPa
fy     = 235 MPa
```

Exact/R15 front-end execution gives

```text
Dx = 5.90813599999987e9 N mm
Dy = 6.13330661333320e9 N mm
H  = 6.24427058738729e9 N mm
j0 = 1.98138534989740
m_phys = 2
ell = 6000 mm
k = 1
q0 = 0.004
Pcr,j=2 = 40.3502059923 MN
```

This does not yet constitute Pu.

## 2. Full R13 master A* was actually reconstructed

Source manifest:

`semantic_v2/40_execution/combined/20260819__NZSCCM__CASE21__R13__FULL_THREE_BRANCH_SPLINE_GKZ_COLUMN_MANIFEST.csv`

Exact integer/rational reconstruction report:

`semantic_v2/40_execution/combined/20260819__NZSCCM__Z1__R15_R13_ASTAR_EXACT_AUDIT_REPORT.json`

Results:

```text
A* shape       = 227 x 403
rank_Q(A*)     = 227
nullity_Q(A*)  = 176
full row rank  = PASS
Z1 generic support = same 403 columns
identically-zero specialized support columns = none
```

Hence Z1 concrete does not require a new monomial-support family.

## 3. Target-specific multi-residue data was reconstructed

Report:

`semantic_v2/40_execution/combined/20260819__NZSCCM__Z1__R15_R13_TARGET_PERIOD_EXACT_AUDIT_REPORT.json`

The 115 monomial-space variables split exactly into

```text
3 physical variables (r,s,u)
+ 112 auxiliary outputs
```

and the 112 auxiliary equations are strictly triangular.  Every diagonal residue derivative is a monomial.

For Pc, the exact residue-Jacobian monomial is

\[
J_{res}\propto
Del^5 Sig^3\,absdetX1\,absdetX10\,dK^2\,
sigAbsX1^3\,sigAbsX10^3\,w.
\]

Since the physical transformed integrand contains `Syy/w`, the `w` factor cancels and the residue numerator is

\[
Del^5 Sig^3 Syy\,absdetX1\,absdetX10\,dK^2\,
sigAbsX1^3\,sigAbsX10^3.
\]

All 112 denominator powers are one.

## 4. Strong reduction: 112 auxiliaries collapse to seven quadratic radicals

Exact audit report:

`semantic_v2/40_execution/combined/20260819__NZSCCM__Z1__R15_R13_SEVEN_RADICAL_TOWER_AUDIT_REPORT.json`

The circuit contains

```text
linear auxiliary outputs    = 105
quadratic radical outputs   = 7
```

The seven radical generators are exactly

```text
w
Del
Sig
absdetX1
sigAbsX1
absdetX10
sigAbsX10
```

`Syy` depends on all seven.  Therefore the full global three-branch R10 stress lies in a finite nested quadratic extension over the rational base field with generic algebraic degree bounded by

\[
2^7=128.
\]

This is a materially smaller exact evaluator target than the raw 227x403 GKZ configuration: the 105 linear auxiliary equations can be treated as a straight-line rational circuit, while only seven algebraic generators require branch data.

## 5. OpenXM/sm1 backend was operationally verified

Exact backend smoke-test report:

`semantic_v2/40_execution/combined/20260819__NZSCCM__OPENXM_SM1_EXACT_BACKEND_PROBE.txt`

It successfully executed both

```text
sm1.gkz(...)
sm1.integration(...)
```

on exact test systems.

## 6. One constructor was tested and crossed out

For the first physical geometry radical

\[
w^2=a(r,s),\qquad a=r(1-r)s(1-s),
\]

the selected positive residue is exactly

\[
\operatorname{Res}_{w=+\sqrt a}\frac{2}{w^2-a}=\frac1{\sqrt a}.
\]

Hence its physical branch satisfies

\[
[2r(1-r)\partial_r+(1-2r)]y=0,
\]

\[
[2s(1-s)\partial_s+(1-2s)]y=0.
\]

An independent exact CAS residue calculation returned `1/Sqrt[a]` and both operators reduced identically to zero.

However, feeding the rational module of `1/(w^2-a)` directly to `sm1.integration(...,[w])` returned

```text
[[2,[]],[1,[-dv,-dr]]]
```

rather than the selected positive-residue branch operators.  Therefore

```text
NAIVE_SM1_DIRECT_IMAGE_OF_RATIONAL_1/G_WITHOUT_CYCLE_SELECTOR = CROSSED_OUT
```

This is a constructor/cycle-selection issue, not a failure of R15 or of exact D-module methods.

The correct next representation is

```text
triangular algebraic residue elimination
-> selected algebraic branch / seven-radical tower
-> exact holonomic annihilator / differential system
-> physical bounded-chain integration
```

rather than asking an unqualified direct-image operation to infer the local residue cycle.

## 7. Current status

```text
Z1_RAW_TO_HALFWAVE                         = PASS
R13_ASTAR_ACTUAL_RECONSTRUCTION            = PASS
R13_Z1_SHARED_SUPPORT                      = PASS
R13_TARGET_MULTIRESIDUE_DATA               = PASS
R13_112_AUX_TO_7_RADICAL_TOWER             = PASS
OPENXM_SM1_BACKEND_OPERATIONAL             = PASS
NAIVE_RATIONAL_DIRECT_IMAGE_CYCLE_SELECTOR = FAIL / CROSSED OUT
FULL_Z1_Pc_EXACT_BOUNDED_PERIOD_EVALUATOR  = OPEN
FULL_Z1_Rq_Ralpha_Jlim_EVALUATOR           = OPEN
FULL_Z1_NONLINEAR_LIMIT_ROOT               = NOT YET SOLVED
Z1_Pu                                      = NOT YET RELEASED
```

This checkpoint deliberately does not copy the historical Z1 nonlinear root/Pu into the new R15 execution.
