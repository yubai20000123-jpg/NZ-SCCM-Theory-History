# NZ-SCCM — Engineering operator R04 D15 production lock

**Date:** 2026-08-20 00:02 +08  
**Status:** final engineering scalar law for the present Case21 ledger. This supersedes the provisional R02 scalar formulas only; all earlier checkpoints remain historical evidence.

The first conservative polynomial replacement was algebraically valid but generated unnecessary degree in the exact D15 compiler. A second ablation at the **material-scalar polynomial degree only** found a lower-degree law that preserves the same source identities and remains conservative on the certified pre-peak material domain.

## 1. Certified material domain

\[
\boxed{-1\le\lambda\le\lambda_t,\qquad \lambda_t=10x_{cr}.}
\]

A request for `lambda<-1` is a compression-peak material-domain failure; R04 is not silently extrapolated.

## 2. Final R04 scalar chains

Define

\[
h(\lambda)=1-\left(\frac{\lambda+1}{\lambda_t+1}\right)^2,
\]

\[
\boxed{\widetilde C_{04}(\lambda)=(2\lambda+\lambda^2)^2h(\lambda)^2,}
\]

\[
\boxed{\widetilde T_{04}(\lambda)=5\rho\lambda^2(\lambda+1)^2,}
\]

and

\[
g(\lambda)=\left[\frac{(\lambda+1)(\lambda_t-\lambda)}{\lambda_t}\right]^3.
\]

The uniaxial master is

\[
\boxed{\widetilde U_{04}(\lambda)=\frac13\kappa\lambda g(\lambda)-\widetilde C_{04}(\lambda)+\rho\widetilde T_{04}(\lambda).}
\]

Polynomial degrees:

```text
deg C04 = 8
deg T04 = 4
deg U04 = 8
```

Full R10 interaction identity remains unchanged:

\[
S=\widetilde U-a_{cc}\det(\widetilde C)\widetilde C
+\widetilde C\operatorname{adj}(\widetilde T)
-\rho a_t\det(\widetilde T)\operatorname{adj}(\widetilde T^7).
\]

Hence the maximum scalar interaction degree is 36 (from the TT term), while the CC term falls to degree 24.

## 3. Source identities retained

\[
\widetilde C_{04}(0)=0,
\qquad
\widetilde C_{04}(-1)=1,
\qquad
\widetilde C'_{04}(-1)=0.
\]

\[
\widetilde T_{04}(0)=\widetilde T_{04}(-1)=0.
\]

\[
\widetilde U_{04}(0)=0,
\qquad
\widetilde U'_{04}(0)=\kappa/3,
\qquad
\widetilde U_{04}(-1)=-1,
\qquad
\widetilde U'_{04}(-1)=0.
\]

Thus the compression peak location/value and zero tangent at the compression peak are preserved; the origin tangent is deliberately reduced to one-third of the R10 tangent.

## 4. Conservative audit against frozen R10/R13

For the current ordinary-concrete material constants:

```text
min[U04-U_R10] on [-1,0]  = +7.30e-6 (normalized stress)
max[U04-U_R10] on [0,lt]  = -1.27e-5
compression work ratio     = 0.93084
tension work ratio         = 0.29847
origin tangent ratio        = 1/3
```

Therefore the R04 scalar uniaxial stress envelope and integrated material work are both conservative on the certified domain. The tangent is same-source and continuous but, as already stated in the previous decision, no claim is made that every nonzero pointwise tangent component is ordered below the reference tangent.

## 5. Why this is not a new fit

R04 uses only the fixed R10/R13 material quantities `kappa,rho,xcr` and universal low-order algebraic factors. No Case21 geometry, panel identifier, trial load, spatial samples, N48/N96 coordinates, or 2D invariant fit enters any coefficient.

The adjustment from the provisional R02 to R04 was made **before** the Case21 limit solve and solely to reduce exact polynomial degree while preserving the reference-material conservative envelope. No trial Pu was used.

## 6. Production lock

```text
ENGINEERING_OPERATOR = R04
SCALAR_DEGREES = C8 / T4 / U8
FULL_CC_TC_TT = ACTIVE
CH_REDUCTION = ACTIVE
D15_EXACT_MOMENTS = NEXT
```

**Unique resume point:** use R04 to construct the Case21 finite D15 P/Rq/Ralpha ledger and solve the direct limit system.