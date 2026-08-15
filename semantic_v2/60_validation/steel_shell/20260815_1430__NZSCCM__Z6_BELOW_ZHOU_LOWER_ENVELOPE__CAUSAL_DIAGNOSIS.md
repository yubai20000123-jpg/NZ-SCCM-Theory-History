# NZ-SCCM Z6 below Zhou lower envelope — causal diagnosis

**Timestamp:** 2026-08-15 14:30 +08:00  
**Identity:** CURRENT CAUSAL DIAGNOSIS / NO THEORY RETUNE / H0 NOT PRODUCTION

## 1. Benchmark bracket

The user authorizes Zhou's FE-informed design curve as the lower comparison envelope and Winter as an engineering upper envelope.

For Z6, Zhou's original full-section replay gives:

```text
Pyth = 88.089888 MN
Pcr = 42.83147561 MN
lambda_n = 1.434106851
phi_Zhou_lower = 0.563883518
P_Zhou_lower = 49.67243594 MN
```

If the commonly used classical Winter effective-width expression

`rho_W = (1 - 0.22/lambda)/lambda` for the slender branch

is used only as a provisional arithmetic upper-envelope convention with the same `lambda_n`, then:

```text
rho_W ~= 0.590328688
P_Winter ~= 52.001988 MN
```

Thus the provisional engineering bracket is approximately:

```text
49.67 MN <= Z6 reference band <= 52.00 MN
```

The Winter value is a project comparison convention, not a Zhou-source FE value.

## 2. Old reduced Z6 versus H0 activation

Current persisted old reduced/local-cap peak:

```text
A0 = a/500
D ~= 0.705
q ~= 0.00589760
P_old = 37.50942609 MN
```

This is about 24.49% below the Zhou lower envelope.

Activating the H0 homogenized web-steel material phase at the *same old state* gives:

```text
Pc,eq = 13.05503 MN
Pw = 7.26268 MN
Psh = 24.18847 MN
Pfixed,H0 = 44.50618420 MN
Rq = -1.658145e9 N mm
```

The H0 fixed-state load increase is:

```text
+6.996758 MN
```

which closes about 57.5% of the old `49.6724 - 37.5094` gap at that frozen state.

Therefore omitted web-steel axial material was a major partial cause of the old low result.

However `Pfixed,H0` is **not a new capacity**, because `Rq` is strongly nonzero.

## 3. The decisive Z6 observation is equilibrium relocation, not axial strength

For Z6 at `D=0.705`, H0 gives:

```text
q=0.005 -> Rq ~= -2.5164e9 N mm
q=0.006 -> Rq ~= -1.5459e9 N mm
```

No same-D `Rq=0` root is found before the current validated Z6 concrete N48 interval is exhausted.

A simple comparison scale

`eta_R = |Rq|/(P*b)`

at the old fixed states gives approximately:

```text
Z4 eta_R ~= 0.000932
Z6 eta_R ~= 0.003105
Z6/Z4 ~= 3.33
```

This normalization is only a comparative diagnostic, but it shows that Z6's generalized-coordinate imbalance after web activation is far stronger than the geometrically similar Z4 case.

The web material addition therefore does not merely add axial force; it pushes the Z6 equilibrium toward substantially larger finite amplitude.

## 4. Why the old outer-shell yield-cusp explanation is no longer sufficient

Under `A0=a/500`, the local progressive radial-cap continuation gives:

```text
first-yield reference P ~= 37.377765 MN
continued local-cap peak P ~= 37.509426 MN
increment beyond first yield ~= 0.131661 MN
```

Thus the former whole-shell first-yield cusp was indeed an operator artifact, but removing that cusp does **not** recover the several-MN Z6 deficit.

Therefore:

```text
FIRST_LOCAL_YIELD_GLOBALIZATION = REAL ARTIFACT
FIRST_LOCAL_YIELD_GLOBALIZATION_AS_DOMINANT_Z6_GAP = REJECTED
```

The post-yield tangent still requires same-branch KZ audit, but the missing load is not explained by the cusp alone.

## 5. Why Z6 is unique

Z4 and Z6 hold fixed:

```text
fy = 355 MPa
fcu = 40 MPa
ts = 4 mm
ls = 200 mm
ls/ts = 50
a/b = 0.75
```

but global slenderness changes from:

```text
Z4: a/h=30.00, b/h=40.00
Z6: a/h=69.23, b/h=92.31
```

The old reduced finite-amplitude states also differ strongly:

```text
Z4 (A0+Ainc)/h ~= 0.0788
Z6 (A0+Ainc)/h ~= 0.6829
```

Across Z0-Z6, Z6 was the only case with normalized NZ stability/path retention below Zhou.

This excludes `ls/ts`, material strength, and a universal R10 bias as the primary unique cause.

## 6. Strongest current structural hypothesis

H0 restores the **amount** of web steel and its loading-direction stress/tangent contribution, but its own theory contract explicitly does not restore:

- periodic lateral support of the outer faceplates;
- discrete-cell boundary restraint;
- the original full orthotropic `Dx,Dy,Dxy,Dmu,H` topology;
- local web-plate/topological stability effects.

This creates a potentially important asymmetry in a very slender panel:

```text
extra longitudinal compression / web axial force = restored
full matching orthotropic and transverse/torsional stability restraint = not restored
```

In Z0-Z5 this can remain hidden because deformation amplitudes are small or the cases are strength/moderate-stability controlled. In Z6, where geometric stiffness and large-amplitude deformation dominate, the same omission can force the `Rq=0` branch toward excessive q and depress the load/stability path.

Therefore the strongest current physical explanation is:

```text
Z6 is not primarily low because its axial section strength is missing anymore.
It is low because the current analytical representation becomes too soft in the deep global-slenderness / finite-amplitude stability path, with H0 restoring longitudinal web material without yet restoring the corresponding full orthotropic/tangent restraint.
```

This is strongly supported but not yet a completed causal proof.

## 7. What is a blocker versus what is a physical cause

```text
N48 current-domain exhaustion after H0 = COMPUTATIONAL/REPRESENTATION BLOCKER
N48 breadth as old Z6 load-gap cause = previously small (~0.2 MN sensitivity), not dominant
RAW ZHOU FE recovery = useful but no longer a causal blocker because Zhou lower/Winter upper bracket is accepted
HALFWAVE/KZ = still open and required for causal proof
```

Do not confuse the present N48 domain stop with evidence that the physical R10 law is wrong.

## 8. Required next proof

The next accepted proof must stay on one connected Z6 H0 branch and persist:

```text
D, q
Pc, Pw, Psh
Rq_c, Rq_w, Rq_sh
current material tangents
KZ_c^mat, KZ_w^mat, KZ_sh^mat, KZ_geo, KZ
L
first yield / KZ=0 / load maximum ordering
```

First resolve the required material-coordinate interval analytically without structural sampling or extrapolation. Then recover the connected `Rq=0` branch and evaluate KZ. Only after this decomposition may an orthotropic homogenized-web stability extension be promoted as necessary.
