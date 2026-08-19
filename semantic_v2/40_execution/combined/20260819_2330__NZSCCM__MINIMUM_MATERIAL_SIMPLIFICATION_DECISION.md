# NZ-SCCM — Minimum material simplification decision

**Date:** 2026-08-19 23:30 +08  
**Identity:** `MINIMUM_MATERIAL_SIMPLIFICATION_DECISION`  
**Previous checkpoint:** `f7eab0d7b6c6062e80100e32258cf335acf4bbd6`

## 1. Decision

The frozen R10/R13 reference material operator is retained unchanged for audit. The production engineering operator modifies only the three one-dimensional spectral source chains

\[
C(\lambda),\qquad T(\lambda),\qquad U(\lambda),
\]

and retains the complete R10 CC/TC/TT interaction identity exactly.

This is the minimum source-level change identified by the V0→V5 ablation. No `A(J1,J2),B(J1,J2)` specimen fit is introduced.

## 2. Material-only constants

Retain

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad
\rho=0.1,\qquad
x_{cr}=\frac\rho\kappa,
\]

and define the tensile audit endpoint

\[
\boxed{\lambda_t=10x_{cr}.}
\]

The engineering operator is formally certified on the pre-compression-peak material domain

\[
\boxed{-1\le\lambda\le\lambda_t.}
\]

`lambda=-1` is the normalized compression peak. If a structural candidate requests `lambda<-1`, the engineering envelope has left its certified material domain and is rejected rather than silently extrapolated. This is a material admissibility boundary, not a spatial cell or quadrature partition.

## 3. Engineering compression chain

Define

\[
h_c(\lambda)=1-\left(\frac{\lambda+1}{\lambda_t+1}\right)^2.
\]

Then

\[
\boxed{
\widetilde C(\lambda)=
(2\lambda+\lambda^2)^2\,h_c(\lambda)^4.
}
\]

Properties:

\[
\widetilde C(0)=0,
\quad
\widetilde C(-1)=1,
\quad
\widetilde C'(-1)=0,
\quad
\widetilde C(\lambda_t)=0.
\]

On `[-1,0]` the base parabola satisfies `(2λ+λ²)^2 <= C_R10(λ)` and the factor `0<=h_c^4<=1`, so the engineering compression amplitude is reduced relative to the frozen compression chain while preserving the compression peak identity.

## 4. Engineering tensile-utilization chain

Define

\[
\boxed{
\widetilde T(\lambda)=
5\rho\,\lambda^2(\lambda+1)^2\left(\lambda+\frac12\right)^2.
}
\]

This is a finite degree-6 nonnegative polynomial. It is zero at `lambda=0,-1,-1/2`; on the certified positive interval it remains below the R13 tensile utilization. It intentionally gives up most of the R13 first-branch peak and therefore biases tensile material work downward.

## 5. Engineering uniaxial master

Define the finite bell factor

\[
\boxed{
g(\lambda)=
\left[
\frac{(\lambda+1)(\lambda_t-\lambda)}{\lambda_t}
\right]^3.
}
\]

Then

\[
\boxed{
\widetilde U(\lambda)=
\frac{2}{5}\kappa\lambda g(\lambda)
-\widetilde C(\lambda)
+\rho\widetilde T(\lambda).
}
\]

Hence

\[
\widetilde U(0)=0,
\qquad
\widetilde U'(0)=\frac25\kappa,
\]

\[
\widetilde U(-1)=-1,
\qquad
\widetilde U'(-1)=0.
\]

The reduced origin tangent is intentional; the engineering law is not calibrated to Case21 and does not preserve the reference elastic tangent exactly.

## 6. Stress / tangent / work conservatism audit

For the frozen Case21 ordinary-concrete material constants (`kappa=2.0005129533678754`, `lambda_t=0.49987179453974245`), independent direct evaluation of the frozen R10/R13 reference and the polynomial replacement gives:

### 6.1 Uniaxial stress envelope

On

\[
-1\le\lambda\le0:
\]

\[
\boxed{U_{R10}(\lambda)\le\widetilde U(\lambda)\le0,}
\]

so compression magnitude is not increased.

On

\[
0\le\lambda\le\lambda_t:
\]

\[
\boxed{0\le\widetilde U(\lambda)\le U_{R10}(\lambda).}
\]

The minimum diagnostic stress safety margin on the compression interval was approximately `+9.37e-6` in normalized stress; the tensile maximum difference was negative.

### 6.2 Tangent

At the origin

\[
\boxed{\widetilde U'(0)=0.4\,\kappa,}
\]

which is strictly below the frozen reference tangent `kappa`.

The global polynomial tangent is same-source and continuous, but is **not pointwise ordered below the R10 tangent at every nonzero strain**. For example the engineering compression slope in part of the pre-peak range may exceed the instantaneous R10 slope while the engineering stress remains below the reference envelope. Therefore the correct tangent conclusion is:

```text
initial tangent conservatism  = PASS
global pointwise tangent order= NOT CLAIMED
same-source tangent identity  = PASS
```

This limitation is explicit; no independent tangent scaling is introduced.

### 6.3 Material work

Uniaxial normalized work integrals over the certified domain gave

\[
\frac{W_{c,eng}}{W_{c,R10}}\approx0.9170,
\qquad
\frac{W_{t,eng}}{W_{t,R10}}\approx0.5847.
\]

Thus compression work and tensile work are both reduced.

The numerical evaluation above is an audit of the closed-form formulas, not a production material-coordinate compiler. Formal production uses only the finite polynomials. Interval/root certification may be retained as a separate material-law proof artifact; it is not part of structural integration.

## 7. Retained multiaxial physics

The frozen interaction constants remain

\[
a_{cc}=0.1072329249362415,
\qquad
a_t=1-2^{-1/8}.
\]

No CC/TC/TT term is deleted. The complete interaction identity is retained in the next checkpoint.

## 8. Explicitly excluded

```text
Case21 fit                              = NO
Swartz24 fit                            = NO
specimen geometry in material law      = NO
N48/N96/material-coordinate compiler   = NO
2D A(J1,J2) fitted surface             = NO
spatial numerical quadrature           = NO
independent tangent fit                 = NO
```

## 9. Unique resume point

Lift `C~,T~,U~` as polynomial matrix functions, retain the full R10 interaction identity, reduce all powers through 2x2 Cayley–Hamilton, and compile the resulting finite stress operator into exact D15 Case21 structural moments.