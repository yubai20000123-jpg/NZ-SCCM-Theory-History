# NZ-SCCM — Case21 16-state semialgebraic-period runtime attempt

**Timestamp:** 2026-08-17 11:55 +08:00  
**Status:** EXECUTED / EXACT STATE REDUCTION PASS / RUNTIME BLOCKER REFINED / FORMAL Pu NOT RELEASED

## 0. Execution scope

This is a continuation of the same end-to-end task

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

No new project task is created. The purpose is to attack the 11:26 fixed-endpoint period-runtime blocker rather than stop at its name.

Formal counters are unchanged:

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

The direct-source Gauss executor and the dense coefficient-space prototype used below are explicitly audit/development tools only.

## 1. Frozen numerical state entering the execution

```text
D      = 0.7887924801
q      = 0.0018083572562965242
lambda = 0.08623596353826937
M      = 0.02907033478365149

Pc = 337.92303037 kN
Ps =  28.84479832 kN
Pu = 366.767828685 kN   # direct-source mechanics oracle only
```

Frozen material constants:

```text
fc    = 21.23 MPa
E0    = 20321 MPa
eps0  = 0.00209
nu    = 0.18
kappa = 2.0005129533678754
rho   = 0.1
eta   = 0.0024993589726987125
H     = 0.09799750427197301
UR    = 0.03
a     = rho/kappa = 0.04998717945397425
```

Source transition eigenstrains:

```text
lambda1  = 0.05008051764913754
lambda10 = 0.49988116674539307
```

## 2. Stable conformal-source identity — exact symbolic pass

The old conformal coordinate

\[
W=E(\sqrt{E^2+\eta^2I}+\eta I)^{-1}
\]

was retained, but the smoothed positive/negative maps were re-derived before any new period machinery was attempted.

Exact scalar symbolic reduction gives

\[
\pi_\eta(E)=E W(I+W)^2(I+W^2)^{-2},
\]

\[
\pi_\eta(-E)=E W(I-W)^2(I+W^2)^{-2}.
\]

The symbolic residuals are exactly zero.

```text
STABLE_CONFORMAL_t_IDENTITY = PASS_EXACT
STABLE_CONFORMAL_c_IDENTITY = PASS_EXACT
```

Why this matters numerically: in the wider certified Case21 box the negative conformal eigenvalue can approach about `-0.9972812`, so `1+w` can be as small as about `0.0027188`. The new formulas contain only `(1+w^2)^-2`, whose real denominator is uniformly >1.

This removes an avoidable conditioning problem before the period layer.

## 3. No-spatial-sampling Bernstein enclosure at the current peak

The Airy-scalar kinematic invariants were written exactly as finite polynomials in

```text
u = sin X
v = sin Y
w = (zeta+1)/2
```

and transformed from the power basis to tensor-product Bernstein coefficients. No continuum point grid is used in this certificate.

Polynomial degrees:

```text
tr(E)    : (2,2,1)
Delta(E) : (4,4,2)
```

Bernstein coefficient extrema:

```text
tr(E)    in [-0.9516607416735428, -0.6221638560307847]
Delta(E) in [+0.5843087672642922, +0.6592312757236101]
```

Therefore:

```text
gap in [+0.7644009205019916, +0.8119305855327844]

lambda_plus  in [-0.09362991058577558, +0.09488336475099984]
lambda_minus in [-0.8817956636031636, -0.6932823882663881]
```

Applying the exact monotone smoothed-positive source map at those endpoints gives

```text
t_plus/a  in [3.3337830931618866e-4, 1.8971668284751766]
t_minus/a in [3.5429606552009475e-5, 4.506313752829062e-5]
```

Hence at the entire current peak continuum:

```text
SPECTRAL_GAP_NONZERO = CERTIFIED
t_minus<a everywhere = CERTIFIED
t_plus<10a everywhere = CERTIFIED
SECOND_TENSILE_KNOT_INACTIVE = CERTIFIED
```

## 4. Six-variable Bernstein enclosure over a formal solve neighborhood

To avoid deriving a peak-only reduction that would disappear as soon as the root solver moves, the same polynomial enclosure was repeated over

```text
D      in [0.75, 0.82]
q      in [0.00175, 0.00187]
lambda in [0.0, 0.15]
```

jointly with the three continuum variables.

The degrees become

```text
tr(E)    : (2,2,1,1,2,1)
Delta(E) : (4,4,2,2,4,2)
```

and the tensor Bernstein enclosure gives

```text
tr(E)    in [-0.9903643386854425, -0.5762231481954689]
Delta(E) in [+0.5246013442823345, +0.7152191687187780]

gap in [+0.7242936864852092, +0.8457063135147910]

lambda_plus  in [-0.13303532610011665, +0.13474158265966102]
lambda_minus in [-0.9180353261001167, -0.6502584173403391]

t_plus/a  <= 2.6948274361042803 < 10
t_minus/a <= 4.804460717539394e-5 < 1
```

Thus the current source topology reduction is valid throughout this solver neighborhood, not merely at one frozen state.

This box uses the direct-source oracle only to define a safe computational neighborhood. It contains no experimental-load calibration and does not select the formal root.

## 5. Exact algebraic state reduction: 64 -> 16 on the certified Case21 box

Because the gap is bounded away from zero, the principal projector is regular. Because the negative branch never reaches the first tensile knot and the positive branch never reaches the second knot, the complete R10 field requires only the radicals

```text
g      = sqrt(Delta_E)
splus  = sqrt(lambda_plus^2  + eta^2)
sminus = sqrt(lambda_minus^2 + eta^2)
h1     = sqrt((t_plus-a)^2) = |t_plus-a|
```

The exact field basis is bounded by

```text
g^i * splus^j * sminus^k * h1^l
for i,j,k,l in {0,1}
```

so

```text
CASE21_CERTIFIED_BOX_STATE_BOUND = 16
GENERIC_GLOBAL_BOUND = 64  # retained outside this box
```

No N48/N96 material approximation is used in this deduction.

## 6. First physical Foster knot exists inside the complete halfwave

The period-runtime attempt then checked whether the new 16-state field could be propagated by one ordinary analytic/Pfaffian system over the whole fixed thickness interval.

A single exact geometry line is already decisive. At

```text
X=Y=pi/2
```

the current peak gives

```text
lambda_plus(zeta=-1) = -0.08174749432807749
lambda_plus(zeta=+1) = +0.08300094849330153
lambda1              = +0.05008051764913754
```

so continuity forces a first-knot crossing. Direct scalar root isolation gives

```text
zeta_lambda1 = +0.60035518053598
```

This root is an audit witness only; no spatial integration or spatial subdivision is generated from it.

## 7. Why the ordinary analytic 16-state Pfaffian runtime fails

The frozen tensile source was differentiated symbolically at its first normalized knot `z=t/a=1`.

Derivative jumps `middle-low` are

```text
order 0 :  0
order 1 :  0
order 2 :  0
order 3 : -3.485446758727596
order 4 : -18.47537053630414
order 5 : -34.55903218728861
```

Therefore the source is exactly `C2` but not analytic at the knot. The first truncated-power coefficient is

```text
A3 = jump3/3! = -0.580907793121266
```

and is nonzero.

For the algebraic selector

\[
h_1=\sqrt{(t_+-a)^2}=|t_+-a|,
\]

a formal derivative gives

\[
h_1'=\frac{(t_+-a)t_+'}{h_1}.
\]

At the physical root `h1=0` this ordinary analytic field derivative is singular because the physical real branch actually switches from `h1=-(t_+-a)` to `h1=+(t_+-a)`.

Therefore:

```text
ORDINARY_SINGLE_ANALYTIC_16_STATE_PFAFFIAN_ACROSS_COMPLETE_THICKNESS = FAIL_PRECONDITION
REASON = physical positive-part gluing at a real Foster knot
```

This is not a source singularity: the assembled R10 tensile law remains C2. It is a failure of treating a semialgebraically glued function as one analytic algebraic branch.

## 8. Exact single-domain semialgebraic-period normal form

Rather than introducing cells, the complete halfwave was rationalized globally.

For each in-plane coordinate define

\[
r=\frac{\tan(X/2)}{1+\tan(X/2)}\in[0,1],
\qquad
Q(r)=r^2+(1-r)^2.
\]

Then

\[
\sin X=\frac{2r(1-r)}{Q(r)},
\quad
\cos X=\frac{1-2r}{Q(r)},
\quad
dX=\frac{2dr}{Q(r)}.
\]

Together with `zeta=2w-1`, the complete structural integration domain is exactly one unit cube `[0,1]^3`; all Nguyen/Airy factors and all T12 target weights are rational functions on that base. The current R10 source is a finite algebraic extension with a positive-part semialgebraic gluing.

Thus the correct formal object is

```text
SINGLE_FIXED_DOMAIN_SEMIALGEBRAIC_PERIOD
```

not a conventional single analytic algebraic period.

This closes a mathematical classification gap in the 11:26 runtime description.

## 9. Development-only dense spectral coefficient audit

To determine whether the new branch restriction was numerically sensible before freezing the exact reduction, a deliberately non-production coefficient-space evaluator was also run at the fixed peak state.

It uses:

```text
minus principal material interval = [-1.0,-0.55]
plus principal material interval  = [-0.10,+0.10]
material degrees: minus=18, plus=96, gap=20
multivariate structural Chebyshev cap N = 12,14,16,20,24
```

This implementation explicitly enumerates multivariate coefficient tensors, so it is prohibited as the formal production architecture. Its only role is diagnosis.

Results at the same frozen peak state:

| N | P (kN) | Rq | RA |
|---:|---:|---:|---:|
| 12 | 366.907127085 | -3.362186829 | -0.0799100253 |
| 14 | 366.773503788 | -2.202276298 | -0.0707354648 |
| 16 | 366.750133196 | -0.829944960 | -0.0531022865 |
| 20 | 366.758757710 | +0.537613666 | -0.0387778609 |
| 24 | 366.744803343 | +0.215798056 | -0.0282476160 |

The load is already close to the direct-source oracle, but `Rq` and `RA` remain visibly order-sensitive. This is exactly why this coefficient route is not promoted.

At `N=20` its T12 vector is

```text
[+8.145711101551047,
 +3.016944715517021,
 -2.6795504366296115,
 -2.2546649474707765,
 -283.281839871558,
 +3.852203187015313,
 -41.434342773851476,
 -11.593892725564054,
 +1.198229008906896,
 +5.713184638350373,
 +33.49289362590389,
 -2.01855181875721]
```

versus the independent 128-grid direct-source oracle T12

```text
[+8.145683883609898,
 +3.016950875199921,
 -2.679407839983953,
 -2.254762879355014,
 -283.28939507865266,
 +3.835282428608082,
 -41.48567515226086,
 -11.58460291071195,
 +1.1983236728328215,
 +5.713143459849670,
 +33.494712972857826,
 -2.0187784124555597]
```

Again, this is audit/development evidence only.

## 10. Runtime/tool inventory

The local execution environment used in this turn contains

```text
Python 3.x
SymPy 1.14.0
mpmath 1.3.0
```

and does not currently provide `Sage/ore_algebra/python-flint/GIAC/symengine` as importable Python modules. No installation/backend chain was opened because the active governance explicitly forbids turning the blocker into an automatic CAS-backend search.

Relevant primary literature confirms that Picard-Fuchs/Griffiths-Dwork methods are an algorithmic class for periods of rational integrals, and that compact semialgebraic volumes can be reduced to period/Picard-Fuchs computations. These references only support the mathematical classification; no external algorithm was silently substituted for the missing NZ-SCCM weighted-R10 runtime.

## 11. Final execution verdict

What advanced in this turn:

```text
STABLE_CONFORMAL_SOURCE_IDENTITY = PASS_EXACT
PEAK_BERNSTEIN_SPECTRAL_CERTIFICATE = PASS_EXACT
FORMAL_SEARCH_BOX_BERNSTEIN_CERTIFICATE = PASS_EXACT
CASE21_CERTIFIED_BOX_ALGEBRAIC_STATE_BOUND = 16
FIRST_REAL_FOSTER_KNOT_CROSSING = CONFIRMED
ORDINARY_ANALYTIC_PFAFFIAN_ACROSS_KNOT = REJECTED_BY_EXACT_PRECONDITION
SINGLE_FIXED_DOMAIN_SEMIALGEBRAIC_PERIOD_NORMAL_FORM = PASS_EXACT
DENSE_SPECTRAL_COEFFICIENT_ROUTE = DEVELOPMENT_ONLY / NOT PRODUCTION
```

What remains open:

```text
NONENUMERATIVE_SINGLE_DOMAIN_SEMIALGEBRAIC_PERIOD_NUMERIC_RUNTIME = NOT IMPLEMENTED
FORMAL_T12_VALUES = NOT RELEASED
FORMAL_T12_DERIVATIVES = NOT RELEASED
FORMAL_Rq_RA_L3_SOLVE = NOT RUN
FORMAL_CASE21_Pu = NOT RELEASED
```

The blocker is now substantially narrower and more accurately stated than at 11:26. It is not `64-state algebraic-period construction` in general; it is the lack of an executable non-enumerative **semialgebraic positive-part period** evaluator on the already-fixed one-domain Case21 problem.
