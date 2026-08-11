# NZ-SCCM R10B COEFFICIENT-GENERATION CONTRACT V1

**Updated:** 2026-08-11 16:38 +08:00  
**Status:** CURRENT GOVERNING SIMPLE CONTRACT

## 1. Principle

The material theory is the closed R10 scalar/current relation itself. Chebyshev coefficients are only a finite analytic compiler for D15; they are not material parameters and are not to be printed as long decimal coefficient lists in the theory.

The project restores the already successful engineering order

\[
\boxed{N_M=48}.
\]

No N112 requirement is governing. The previous N112 re-freeze is superseded by this simplicity decision.

## 2. Closed R10 material formula

Define

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad x_{cr}=\frac{\rho}{\kappa}.
\]

For the source Foster tensile scalar

\[
T_{src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10),\qquad r=t/x_{cr},
\]

let

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr.
\]

The R10 peak parameter is obtained directly from the work condition:

\[
\boxed{
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right)
}.
\]

Rise branch, with \(\tau=t/x_{cr}\):

\[
\boxed{
u_1(\tau)=
\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5
}.
\]

Fall branch, with \(s=(t-x_{cr})/(9x_{cr})\):

\[
\boxed{
u_2(s)=h+(u_r-h)(10s^3-15s^4+6s^5)
}.
\]

Thus the material law is already a compact parameter formula. In the theory, write \(10h-6\rho\), \(8\rho-15h\), \(6h-3\rho\), etc.; do not replace them by long decimal constants.

The multidimensional current map remains exactly the same:

\[
U_i=\kappa\lambda_i-C_i+\kappa c_i+\rho T_i-\kappa t_i,
\]

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8,
\]

\[
s_-=U_- -a_{cc}C_-^2C_+ + C_-T_+ -\rho a_tT_-T_+^8.
\]

## 3. N48 compiler formula

Use the same scalar hull

\[
\lambda\in[\lambda_a,\lambda_b]=[-1.01,0.105],
\]

\[
\lambda_c=\frac{\lambda_a+\lambda_b}{2},\qquad
\lambda_h=\frac{\lambda_b-\lambda_a}{2},\qquad
\xi=\frac{\lambda-\lambda_c}{\lambda_h}.
\]

For each scalar object

\[
F\in\{U,C,T,T^7\},
\]

write only

\[
\boxed{F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi)}.
\]

Here \(\mathcal C_n\) denotes the first-kind Chebyshev polynomial, so it is not confused with the tensile utilization symbol \(T\).

The complete coefficient formula is

\[
\theta_j=\frac{(j+\tfrac12)\pi}{49},\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j,
\]

\[
\boxed{
a_n^{(F)}=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),
\qquad n=0,\ldots,48.
}
\]

This one formula defines every one of the 49 coefficients. The theory does not need to print 49 decimal values.

Equivalent continuous-projection notation may be used only as a compact theoretical reference:

\[
a_0^{(F)}=\frac1\pi\int_0^\pi F[\lambda(\theta)]d\theta,
\]

\[
a_n^{(F)}=\frac2\pi\int_0^\pi F[\lambda(\theta)]\cos(n\theta)d\theta,\qquad n\ge1,
\]

with

\[
\lambda(\theta)=\lambda_c+\lambda_h\cos\theta.
\]

The discrete N48 root formula above is the governing production compiler rule.

## 4. Engineering acceptance

Historical R10B already achieved a complete N48 zero-spatial Case21 stationary root. The archived N96 fixed-D audit differed by about 0.051%, which is accepted as an engineering truncation scale and is far below the material/model uncertainty relevant to the project.

Therefore:

```text
MATERIAL_COMPILER_ORDER = 48
N112_REQUIREMENT = SUPERSEDED
LONG_DECIMAL_COEFFICIENT_TABLE_IN_THEORY = PROHIBITED
MATERIAL_FORM = CLOSED_PARAMETER_FORMULA
COEFFICIENTS = DERIVED_BY_ONE_GENERAL_FORMULA
```

If a future material law cannot be compiled adequately at N48, the first response is to recover/use a simpler already-closed material law, not to escalate the compiler order without user approval.