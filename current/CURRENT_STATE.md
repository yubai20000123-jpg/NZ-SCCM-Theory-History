# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-17 15:26 +08:00  
**Status:** TRUE-INFINITE R10 -> PHYSICAL CH/D15 TARGET LIMIT CONNECTED / Z6 + CASE21 LIMIT Pu RELEASED

## Controlling governance

`semantic_v2/10_governance/20260817_1449__NZSCCM__TRUE_INFINITE_SERIES_TO_FINITE_INTEGRAL_SOLUTION__CANONICAL_CORRECTION_LOCK.md`

The canonical chain remains

```text
actual geometry/boundary
 -> complete representative halfwave
 -> frozen R10 or unified UHPC current target
 -> true infinite analytic material sequence
 -> membrane-redistributed Nguyen field
 -> same-source directional tangent
 -> exact nth-term CH/D15 structural moments
 -> n->infinity target limit
 -> finite P,Rq,RA,Kt
 -> coupled finite equilibrium/limit solve
 -> Pu
 -> case-specific post-solve comparison.
```

## Formal counters

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

---

# Stage I — true infinite R10 source sequence: PASS

The source-level recurrence/generator and convergence laws remain as previously locked. N48 is the finite prototype exposing this structure; no final finite degree is selected.

---

# Stage II — general-n CH + exact D15 J_n: PASS

For every scalar material basis term,

\[
T_n(Y)=p_nI+q_nY,
\]

with the exact CH recurrence and exact complete-halfwave/thickness D15 target moments already verified.

---

# Stage III — full physical target connection: PASS

The complete current stress operator

\[
S
=U-ACC\det(C)C
+C\operatorname{adj}(T)
-\rho AT\det(T)\operatorname{adj}(T7)
\]

is now connected to the infinite `U,C,T,T7` matrix streams through convergent CH-pair Cauchy products.

For any generalized coordinate `z`,

\[
Q_z=(1+\nu)S:E_{,z}-\nu\operatorname{tr}(S)I_{1,z},
\]

so

\[
R_z^c
=\frac{f_c\varepsilon_0b\ell t}{2\pi^2}D15[Q_z],
\]

and

\[
P_c=-\frac{f_cbt}{2\pi^2}D15[S_{yy}].
\]

The same-source full directional tangent follows by differentiating the SAME infinite matrix streams and applying exact D15 to the derivative targets.

## True n -> infinity identity

Stage-I source convergence plus the finite-domain D15 functional gives

\[
\boxed{
\lim_{N\to\infty}D15[S_N]=D15[S_{R10}]
}
\]

and

\[
\boxed{
\lim_{N\to\infty}D15[dS_N]=D15[dS_{R10}].
}
\]

Thus the final target functions are the true frozen-R10 continuous targets, not an N192/N240/N288 surrogate.

Direct raw-R10 spatial grids remain numerical localization/audit backends only; they do not acquire formal theoretical identity.

---

# Case21 true-infinite limit result

Correct geometry/material identity:

```text
b = ell = 1220 mm
t = 19.30 mm
q0 = .0025
fc = 21.23 MPa
eps0 = .00209
nu = .18
rho_sx = rho_sy = .00375
Es = 200000 MPa
```

Limit root:

```text
D ~= .7887924801
q ~= .0018083572563
lambda_Airy ~= .08623596354
Pc ~= 337.923030 kN
Ps ~= 28.844798 kN
```

True-infinite R10/D15 capacity:

\[
\boxed{P_u^{Case21}=366.767829\ \mathrm{kN}.}
\]

Post-solve only:

```text
Pf_exp = 368.312750 kN
error = -1.544921 kN = -0.419459 %
```

The previous `365.257 kN` remains a finite-N48 formal checkpoint and is superseded only as the mathematical `n->infinity` material-series result.

A same-source target-Jacobian audit at the limit neighborhood is

```text
rows P,Rq,RA ; columns D,q,lambda_A
[[  140.016244, -70566.7765,    75.4429339],
 [-1587.62545,  920049.913,  -1213.05000  ],
 [    6.418470, -10550.5046,    25.2481285]]
```

and independently reproduces the prior current-tangent audit scale.

---

# Z6(a=24000) true-infinite limit result

Locked geometry:

```text
a = 24000 mm
b = 12000 mm
m* = 2
ell = 12000 mm = b
q0 = .004
tc = 122 mm
ts = 4 mm
rho_w = .02
```

Constrained square-halfwave Airy redistribution remains active; neither r=0 nor free-five is production.

Limit root:

```text
D ~= 1.36180798
q ~= .0264854039
lambda_Airy ~= .786915819
Pc_eff ~= 22.8171044 MN
Ps_face ~= 18.5564373 MN
Pw ~= 7.0325797 MN
```

True-infinite R10/D15 capacity:

\[
\boxed{P_u^{Z6}\approx48.40612\ \mathrm{MN}.}
\]

Post-solve comparators:

```text
Zhou Eq.(5-87)/(5-88) = 49.48676675 MN
error = -2.18371 %

Winter = 50.18585413 MN
error = -3.54628 %
```

The earlier `~48.42 MN` N192/N240/N288 family remains a development convergence checkpoint only; it no longer defines the formal infinite-material limit.

---

# Exact-D15 prefix regressions

At the true-limit root neighborhoods, exact coefficient-space CH/D15 prefixes generated from the source series approach the independent raw-source targets.

Case21 concrete prefix example:

```text
N32  Pc=331.443627 kN
N48  Pc=335.940747 kN
N64  Pc=336.647977 kN
N80  Pc=337.035449 kN
N96  Pc=337.340135 kN
N104 Pc=337.422904 kN
limit raw-R10 Pc ~=337.923030 kN
```

Z6 full-concrete prefix example:

```text
N12 Pc=23.065253 MN
N20 Pc=23.414507 MN
N28 Pc=23.321494 MN
N36 Pc=23.297615 MN
N40 Pc=23.269059 MN
limit Pc,full ~=23.282760 MN
```

These prefixes are regression observations of the true series; no finite N is selected as the production definition.

---

# Current artifacts

Theory Stage III:
- `semantic_v2/20_theory/nc_rebar_panel/20260817_1526__NZSCCM__TRUE_INFINITE_R10_TO_PHYSICAL_TARGET_D15_LIMIT__THEORY_STAGE3.md`

Execution:
- `semantic_v2/40_execution/combined/20260817_1526__NZSCCM__TRUE_INFINITE_R10_D15_LIMIT_Z6_CASE21__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/combined/20260817_1526__NZSCCM__TRUE_INFINITE_R10_D15_LIMIT_Z6_CASE21__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/combined/20260817_1526__NZSCCM__TRUE_INFINITE_R10_D15_LIMIT_Z6_CASE21__REPRO.py`

## Current status

```text
STAGE_I_TRUE_INFINITE_SOURCE = PASS
STAGE_II_GENERAL_N_CH_D15 = PASS
STAGE_III_FULL_R10_TO_PHYSICAL_TARGET = PASS
TRUE_N_TO_INFINITY_LIMIT_IDENTITY = PASS
SAME_SOURCE_DIRECTIONAL_Kt = PASS

CASE21_TRUE_INFINITE_Pu = 366.767829 kN
Z6_A24000_TRUE_INFINITE_Pu ~= 48.40612 MN
```

## Next logical task

The ordinary-concrete infinite-series/D15 chain is now closed at the mathematical target-function level for the two current benchmarks. The next theory extension, when requested, is to place the unified UHPC current operator into the SAME source-series -> CH -> D15 -> n->infinity architecture rather than creating a different integration method.
