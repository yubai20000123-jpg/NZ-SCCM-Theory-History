# NZ-SCCM Swartz24 — second-order kinematics and halfwave provenance audit

**Timestamp:** 2026-08-13 17:56 +08:00  
**Identity:** KINEMATICS-LAYER AUDIT / SOURCE-GROUNDED + AUDIT-ONLY NUMERICAL CROSSCHECK  
**R10 change:** NO  
**Compiler change:** NO  
**Formal D15 change:** NO  
**Structural calibration:** NO

## 0. Question

Could the systematic Swartz24 error pattern arise from the current Nguyen second-order kinematics rather than, or in addition to, material/compiler issues?

This audit separates two different hypotheses:

1. `KINEMATIC_ORDER_TRUNCATION`: the von-Karman/Nguyen second-order strain-displacement expansion omits third- and higher-order geometric terms that matter materially.
2. `KINEMATIC_SUBSPACE_TRUNCATION`: the current NZ-SCCM reduction from Nguyen's general `u(x,y), v(x,y), w(x,y)` fields to two generalized coordinates `(D,q)`, a fixed sine shape, and a fixed halfwave geometry is too restrictive.

These hypotheses must not be conflated.

## 1. Source statement on Nguyen geometric order

Nguyen Chapter 2 derives nonlinear plate equilibrium/buckling equations and explicitly states in the summary that the formulas were simplified by ignoring third-order and higher terms in the displacement functions.

Nguyen Chapter 6 uses, for an initially imperfect plate,

\[
\varepsilon_{11}=u_{,x}-z w_{m,xx}+
\frac12\left(w_{m,x}^2+2w_{0,x}w_{m,x}\right),
\]

\[
\varepsilon_{22}=v_{,y}-z w_{m,yy}+
\frac12\left(w_{m,y}^2+2w_{0,y}w_{m,y}\right),
\]

with the analogous shear relation. Chapter 6 is presented for small initial imperfections and small eccentricities; the implemented tangent-modulus approximation is not claimed to be a full general nonlinear layered-shell solution.

Thus higher-order geometric terms are a legitimate theoretical question.

## 2. Order-of-magnitude check: higher-order geometric terms

Using the current Case1 material/compiler identity and the source-correct one-halfwave length `ell=2440 mm`, an independent audit-only branch reconstruction gives approximately

```text
D ~ 1.00525
q ~ 0.00067883
q0 = 0.0025
```

The maximum total geometric slope scales are then only about

```text
pi*(q0+q)             ~ 9.99e-3 rad   # x direction
pi*(b/ell)*(q0+q)     ~ 4.99e-3 rad   # y direction
```

The main axial strain scale is

```text
eps0*D ~ 2.11e-3
```

while representative included nonlinear membrane/bending strain scales are approximately

```text
pi^2*(q0*q+q^2/2)               ~ 1.90e-5
pi^2*(b/ell)^2*(q0*q+q^2/2)     ~ 4.76e-6
pi^2*(t/(2b))*q                  ~ 6.97e-5
pi^2*(t*b/(2 ell^2))*q           ~ 1.74e-5
```

A Green-strain correction of order `0.5*(eps0*D)^2` is only about `2.23e-6`; rotation terms beyond the retained slope-squared terms scale still lower, with `(slope)^4` around `1e-8`.

These are order-of-magnitude diagnostics, not a formal asymptotic proof, but they make it difficult to attribute a 10-25% load error primarily to omission of third- and higher-order geometric terms.

```text
KINEMATIC_ORDER_TRUNCATION_AS_PRIMARY_10_TO_25_PERCENT_ERROR = LOW_PROBABILITY
```

## 3. Thickness trend is not monotone in the current 24-panel result

Using Nguyen Table 5.1 thicknesses and the current stored first-load-maximum errors:

```text
Cases 1-8   : t mean ~25.43 mm, b/t~48,  mean signed error +6.313%
Cases 9-16  : t mean ~31.88 mm, b/t~38,  mean signed error -11.849%
Cases 17-24 : t mean ~19.33 mm, b/t~63,  mean signed error -2.896%
```

The physical-thickness versus signed-error Pearson correlation is only approximately `r=-0.288` for the 24 current values.

Therefore the present data do **not** support the literal rule `thicker plate -> prediction too high, thinner plate -> prediction too low`.

The more defensible observation is that error is **group-structured by thickness/slenderness and buckling-mode regime**, and is non-monotone with thickness.

Within Cases1-8 alone, where thickness stays near 25 mm, signed errors range from about `+24%` to `-12%`, which also rules out thickness alone as the sign controller.

## 4. Source mode-shape evidence makes the kinematic subspace a high-priority issue

Nguyen Chapter 5 explicitly reports:

```text
Panels 17-24 (b/t~63): two sinusoidal halfwaves
Panels 1-16  (b/t~48 to 38): approximately one half sinusoidal wave
```

The more slender group buckles at about `0.618 fc`, while the `b/t~48` and `b/t~38` groups buckle around `0.795 fc` and `0.93 fc`, respectively. Nguyen further notes that the thicker-group shapes differ from isotropic elastic plate shapes and resemble tangent-orthotropic shapes.

This supports a strong distinction between:

- a geometric/stability-dominated slender regime; and
- a high-material-nonlinearity, redistribution-sensitive thicker regime.

The current NZ-SCCM kinematic reduction has only two global coordinates `(D,q)` and fixes the out-of-plane shape. Nguyen's original equations retain independent `u(x,y)`, `v(x,y)`, and `w(x,y)` fields.

Hence the higher-priority kinematic risk is not the omission of a cubic slope term; it is the removal of independent in-plane redistribution and additional out-of-plane modal freedom.

```text
KINEMATIC_SUBSPACE_TRUNCATION = HIGH_PRIORITY_DIAGNOSTIC
```

## 5. Critical provenance conflict: Case1/14 halfwave length

The source-backed Swartz mode mapping was explicitly frozen on 2026-08-09 as

```text
Cases 1-16  : ell = 2440 mm, r=b/ell=0.5
Cases 17-24 : ell = 1220 mm, r=1
```

The generalized halfwave backend/report also encoded exactly this mapping.

However, the later 2026-08-11 three-representative-panel blind input states

```text
Case1, Case14, Case21 common input:
b = ell = 1220 mm
```

and the later Case1 reconstruction audit also used `b=ell=1220 mm`.

For Case1 and Case14 this conflicts with the earlier source-locked mode geometry.

This is not a small parameter change. In the current rectangular Nguyen coefficients,

\[
C_{my}\propto (b/\ell)^2,
\quad C_{mxy}\propto b/\ell,
\quad C_{by}\propto b/\ell^2,
\quad C_{bxy}\propto 1/\ell.
\]

Changing Case1 from `ell=2440` to `ell=1220` therefore changes these terms by factors of 4 or 2.

```text
CASE1_RECENT_RECONSTRUCTION_HALFWAVE_PROVENANCE = INCONSISTENT_WITH_SOURCE_LOCK
CASE14_RECENT_REPRESENTATIVE_INPUT_HALFWAVE_PROVENANCE = INCONSISTENT_WITH_SOURCE_LOCK
CASE21_ELL_1220 = SOURCE_CONSISTENT
```

The provenance of the stored 24-panel `608.925 kN` value must therefore be checked before it is used as evidence for or against a material/compiler hypothesis.

## 6. Audit-only direction check with source-correct Case1 halfwave

Without changing R10, the current C1/MM material coefficients, reinforcement, initial-imperfection amplitude or any experimental quantity, an independent high-order audit evaluator was rerun with only

```text
ell: 1220 -> 2440 mm
```

for Case1.

The source-correct rectangular-halfwave audit gives approximately

```text
D_L ~ 1.00525
q_L ~ 0.00067883
P_L ~ 647.50 kN
principal material coordinate ~ [-1.020, +0.035]
```

The material coordinate remains inside the declared Case1 compiler interval `[-1.12,+0.105]`.

Compared with the square-halfwave audit/current stored value near `608.9 kN`, source-correct `ell=2440` raises the Case1 load maximum by roughly 6.3% in this independent diagnostic.

Therefore:

```text
HALFWAVE_LENGTH_CORRECTION_DOES_NOT_EXPLAIN_CASE1_OVERPREDICTION
IT_ACTUALLY_WORSENS_CASE1_OVERPREDICTION_IN_THE_AUDIT
```

The number `647.5 kN` is AUDIT-ONLY because it was obtained with physical-space Gaussian integration as an independent evaluator, not formal general-D15. It must not replace the production result.

## 7. Implication for the user's hypothesis

The evidence supports a nuanced verdict:

```text
Pure higher-order geometric kinematics missing from Nguyen second order
    -> unlikely to be the dominant 10-25% error source.

Current reduced D-q / fixed-mode kinematic subspace
    -> plausible and high priority.

Incorrect or homogenized halfwave geometry
    -> proven provenance risk; must be audited immediately.

Physical thickness alone
    -> does not control the error sign across 24 panels.
```

## 8. Required isolated kinematics audit

Before changing R10 or promoting a new material compiler, the structural layer should be isolated using the same source material operator and zero-spatial analytic integration:

```text
K0: current two-coordinate D-q model, source-correct halfwave length
K1: add at least one independent in-plane Ritz redistribution coordinate
K2: add a second admissible out-of-plane Ritz mode / shape coordinate
K3: optionally test exact/higher-order strain kinematics only after K1/K2
```

Use Case1, Case14 and Case21 as source-designated representatives of the three regimes. Solve blindly without experimental load and compare only the changes in

```text
D_L, q_L, P_L, Rq, L, KZ, reachable material spectrum
```

before opening `Pf`.

All added Ritz functions can remain finite trigonometric/polynomial bases and therefore remain compatible with Cayley-Hamilton + general-D15; no formal spatial quadrature, cells or FE mesh is required.

## 9. Current verdict

```text
SECOND_ORDER_KINEMATIC_ORDER = RETAIN_PENDING_ISOLATION
HIGHER_ORDER_GEOMETRY_AS_PRIMARY_ERROR = NOT_SUPPORTED_BY_SCALE
REDUCED_KINEMATIC_SUBSPACE = OPEN_HIGH_PRIORITY
CASE1_14_HALFWAVE_INPUT_PROVENANCE = FAIL / REQUIRES_RECONCILIATION
CASE21_HALFWAVE_INPUT = PASS_SOURCE_GEOMETRY
R10_CHANGED = NO
COMPILER_CHANGED = NO
STRUCTURAL_BACKFIT = NO
```
