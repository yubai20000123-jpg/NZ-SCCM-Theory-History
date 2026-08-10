# NZ-SCCM USER-SKETCH SMOOTH MATERIAL + EXPLICIT REINFORCEMENT R08

**Date:** 2026-08-10

## 1. Correction to R07R

The R07R rational candidates were smoother than the source in a global fitting sense, but they still created an artificial tensile overshoot / dip / rebound sequence. That is not the intended material-data simplification.

The preferred processing is:

```text
source/reference data
-> deliberately discard the sharp local peak/cut
-> replace it by a low-parameter monotone smooth cap
-> then assess the structural consequence
```

## 2. Explicit user-sketch scalar target

Compression:

- `lambda < -10`: residual `-0.10 fc`;
- `-10 <= lambda < -1`: retained R06 C2 source-faithful postpeak target;
- `-1 <= lambda < 0`: Saenz compression.

Tension:

- `0 <= lambda <= lambda_p`: quintic Hermite rise;
- `lambda_p <= lambda <= lambda_r`: quintic Hermite decay;
- `lambda >= lambda_r`: residual `0.03 fc`.

Material anchors:

\[
\lambda_p=x_{cr}=0.049987179454,
\qquad u(\lambda_p)=0.09,
\]

\[
\lambda_r=10x_{cr}=0.49987179454,
\qquad u(\lambda_r)=0.03.
\]

At the origin:

\[
u(0)=0,
\qquad u'(0)=\kappa=2.00051295337.
\]

At `lambda_p` and `lambda_r`, the tangent is zero.

With local coordinate `tau`, the actual quintic coefficients are:

```text
rise: [0, 0.1, 0, 0.3, -0.55, 0.24]
fall: [0.09, 0, 0, -0.6, 0.9, -0.36]
```

Executed shape audit:

```text
rise monotone non-decreasing = PASS
fall monotone non-increasing = PASS
peak = 0.09 fc
residual = 0.03 fc
slope at origin = kappa
slope at peak = 0
slope at residual = 0
```

Therefore the tensile target has no secondary undershoot or rebound.

## 3. Explicit reinforcement

Case21 source mapping:

```text
rho_x = rho_y = 0.00375
Es = 200000 MPa
fy = 530 MPa
```

Let

\[
S=q_0q+\frac12q^2,
\qquad
C_m=\frac{\pi^2S}{\varepsilon_0}.
\]

The loading-direction steel load is exactly

\[
P_s(D,q)
=
\frac{\rho_y t b E_s\varepsilon_0}{1000}
\left(D-\frac{C_m}{4}\right)
\quad [\mathrm{kN}].
\]

The steel amplitude residual is exactly

\[
R_s(D,q)
=
\frac{\rho_y tE_s\pi^2(q_0+q)b\ell}{1000}
\left[
\frac{\varepsilon_0D(\nu-1)}4
+
\frac{9\pi^2S}{32}
\right]
\quad [\mathrm{kN\,mm}].
\]

Steel enters the SAME limit equations:

\[
P=P_c+P_s,
\qquad
R=R_c+R_s,
\]

\[
L=P_D R_q-P_qR_D.
\]

No after-the-fact `As fy` addition is used.

## 4. First coarse whole-structure target — rejected

A first degree-(11,11) Chebyshev target on

```text
D in [0.35,1.30]
q in [0.001,0.030]
```

was generated, but its `Rc` off-grid error was too large and the predicted stationary root did not close the underlying total residual closely enough.

The resulting coarse value `335.047660 kN` is therefore **REJECTED** and must not be used as the R08 result.

## 5. Mandatory local explicit refinement

The mechanically located low-q branch was found from an audit-only solution of the same material + reinforcement equations, not from the experimental load. The local explicit box was then fixed as

```text
D in [0.60,0.84]
q in [0.012,0.0215]
```

and degree sequence `12,14,16,18` was executed.

| degree | Pc max abs (kN) | Pc P95 (kN) | Rc max abs (kN mm) | explicit Pu (kN) | audit P at same root (kN) | audit R at same root (kN mm) |
|---:|---:|---:|---:|---:|---:|---:|
|12|0.114036|0.072741|17.907647|335.674859|335.738639|10.625278|
|14|0.092249|0.057296|16.933842|335.632742|335.659526|4.644755|
|16|0.090718|0.067868|17.484157|335.598945|335.595458|-0.467684|
|18|0.087275|0.059938|15.998997|335.589783|335.585377|-1.021793|

Degree 18 is retained as the final R08 explicit local target.

## 6. Final explicit RC Case21 result

\[
D_u=0.708108615160,
\]

\[
q_u=0.0166001000745,
\qquad
A_u=q_ub=20.252122\ \mathrm{mm}.
\]

\[
P_c=317.266522\ \mathrm{kN},
\]

\[
P_s=18.323261\ \mathrm{kN},
\]

\[
\boxed{P_u=335.589783\ \mathrm{kN}}.
\]

Case21 experiment:

\[
P_f=368.312750\ \mathrm{kN}.
\]

Therefore

\[
\boxed{
\frac{P_u}{P_f}-1=-8.884560\%
}
\]

for this **minimal scalar current-surface + analytic reinforcement** model.

Independent underlying-material audit at the same root gives

```text
P_total_audit = 335.585377 kN
R_total_audit = -1.021793 kN mm
```

so the explicit target and the audit response at the retained root agree closely in load.

## 7. Reinforcement elasticity check

At the final state:

```text
y-rebar strain range = [-0.00147995, +0.00028949]
x-rebar strain range = [+0.00026639, +0.00203583]
yield strain = 0.00265
```

Thus all reinforcement remains elastic, and the exact elastic steel expressions used above are consistent.

## 8. Interpretation

The user's sketch is smoother than the R07R rational curves in the intended physical sense:

- R07R rational regression: globally smooth but introduced a local tensile undershoot / rebound;
- R08 user-sketch target: one rounded tensile peak followed by one monotone decay to residual, with no secondary local oscillation.

Therefore the R07R rational tensile oscillation is rejected as unnecessary.

The current Case21 result remains below experiment by about `8.88%`. This should **not** be repaired by restoring a sharper tensile peak. The next physical question is whether a small source-grounded multiaxial compression / TC enhancement is required.

## 9. Formal-status boundary

Runtime evaluation of the retained local `Pc(D,q), Rc(D,q)` target and all derivatives is explicit and finite.

However, the coefficients were still identified offline from high-accuracy full-halfwave numerical integration. Therefore:

```text
R08_EXPLICIT_RC_CHAIN = PASS_DIAGNOSTIC
FORMAL_ZERO_SPATIAL_QUADRATURE_PRODUCTION = HOLD
```

This is the same disclosed proof-of-concept boundary as R07R.

## 10. Next task

```text
R09_MINIMUM_SOURCE_GROUNDED_MULTIAXIAL_CORRECTION
```

Do not restore the full historical CC/TC/TT complexity. Add only the smallest multiaxial correction needed by source mechanics and then re-evaluate the same explicit `P,R,L` chain.
