# NZ-SCCM — Engineering operator R05 material-domain correction

**Date:** 2026-08-20 00:25 +08  
**Status:** `R05 = ACTIVE`; R04 is retained as an auditable rejected production candidate.

## 0. Why R04 is superseded

The first R04 Case21 equilibrium/limit diagnostic reached a principal equivalent strain of approximately

\[
\lambda_{max}\approx0.79,
\]

whereas R04 had only been certified to

\[
\lambda_t=10x_{cr}\approx0.50.
\]

Therefore the R04 structural limit candidate is **rejected before acceptance**. It is not a valid Case21 result and must not be reported as final Pu.

This is a material-domain failure discovered by post-solve audit; no trial/experimental load was involved.

## 1. R05 certified domain

Use the material-only normalized pre-peak domain

\[
\boxed{-1\le\lambda\le1.}
\]

The endpoints depend only on the normalized material strain scale `eps0`, not specimen geometry.

## 2. R05 scalar chains

Define

\[
h(\lambda)=1-\left(\frac{\lambda+1}{2}\right)^2.
\]

Compression activation:

\[
\boxed{
\widetilde C_{05}(\lambda)
=(2\lambda+\lambda^2)^2h(\lambda)^4.
}
\]

Tension utilization:

\[
\boxed{
\widetilde T_{05}(\lambda)
=\frac{U_R}{4\rho}\lambda^2(\lambda+1)^2.
}
\]

This gives

\[
\widetilde T_{05}(1)=U_R/\rho=0.3.
\]

Uniaxial master:

\[
\boxed{
\widetilde U_{05}(\lambda)
=\frac{\kappa}{6}\lambda(1-\lambda^2)^3
-\widetilde C_{05}(\lambda)
+\rho\widetilde T_{05}(\lambda).
}
\]

Degrees:

```text
deg C05 = 12
deg T05 = 4
deg U05 = 12
```

## 3. Exact source identities

\[
C_{05}(0)=0,
\quad C_{05}(-1)=1,
\quad C'_{05}(-1)=0,
\]

\[
T_{05}(0)=T_{05}(-1)=0,
\quad T_{05}(1)=U_R/\rho,
\]

\[
U_{05}(0)=0,
\quad U'_{05}(0)=\kappa/6,
\quad U_{05}(-1)=-1,
\quad U'_{05}(-1)=0,
\quad U_{05}(1)=U_R.
\]

Thus R05 preserves the uniaxial compression peak value/location/zero peak tangent and the high-tension R13 plateau value, while deliberately reducing the small-strain tangent and tensile work.

## 4. Scalar stress/work audit against frozen R10/R13

On `[-1,0]`, `U05` is no more compressive than the frozen R10 uniaxial master. On `[0,1]`, `U05` is no more tensile than the frozen R10/R13 master.

For the current material constants the material-work audits are

```text
compression work ratio Wc05/WcR10 ≈ 0.732
tension work ratio     Wt05/WtR10 ≈ 0.448
origin tangent ratio              = 1/6
```

The exact R10 CC/TC/TT interaction identity and constants remain active; only the scalar chains are replaced.

## 5. Multiaxial conservatism statement

The following claims are made, and only these claims:

```text
uniaxial stress envelope conservatism = PASS
initial tangent conservatism          = PASS
uniaxial material-work conservatism   = PASS
same-source tangent identity          = PASS
```

Because the frozen TC and TT interaction terms contain competing signs, scalar ordering alone does **not** mathematically imply componentwise ordering of every biaxial principal stress. Therefore R05 does not falsely claim a universal pointwise biaxial stress-order theorem. This issue is carried as an explicit mechanics audit item to the final structural Pu check.

No material-coordinate finite scan is used as formal constitutive evidence; diagnostic evaluations only verify the closed-form formula implementation.

## 6. Production identity

The full interaction remains

\[
S=\widetilde U_{05}
-a_{cc}\det(\widetilde C_{05})\widetilde C_{05}
+\widetilde C_{05}\operatorname{adj}(\widetilde T_{05})
-\rho a_t\det(\widetilde T_{05})\operatorname{adj}(\widetilde T_{05}^7).
\]

All 2x2 Cayley–Hamilton and D15 formulas from the preceding exact-integral ledger remain unchanged after replacing the scalar coefficient arrays by R05.

## 7. Unique resume point

Recompile the already-derived finite CH/D15 Case21 ledger with R05, solve the connected physical branch, enforce the `[-1,1]` material-domain gate, and then solve `Rq=0,Ralpha=0,det(Jlim)=0`.