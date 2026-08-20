# NZ-SCCM — Scope correction: global R_m, P, R_A analytic integration

时间：2026-08-20 17:26 +08:00

状态：`ACTIVE_SCOPE_CORRECTION / GLOBAL_INTEGRATION_ONLY`

## Correction

The previous turn drifted back into a TC/CT thickness-integration subproblem after TC/CT direction handling had already been accepted through the derived principal direction angle theta. That is not the current project task.

The current task is now fixed as:

`Nguyen second-order kinematics -> theta/principal strains -> frozen NC-M4 unique current operator -> explicit sigma_x, sigma_y, tau_xy -> global analytic evaluation of R_m, P, R_A -> same-source derivatives -> final 3-equation system`.

No further theory redesign of TC/CT is allowed unless the direct global integration itself produces a concrete failure that is specifically attributable to the TC/CT material law.

## Frozen local operator

- CC/TC/CT/TT nine-grid current operator is considered defined for purposes of the present integration task.
- theta is a derived current principal direction and is not a structural unknown.
- membrane force and bending moment contributions are both retained.
- b and ell remain independent.
- formal spatial quadrature, material-point grid, and artificial spatial cells remain zero.

## Actual remaining task

Starting from

\[
R_m=K_0\int_0^\pi\int_0^\pi\int_{-1}^{1}\sigma_x\,d\zeta\,dY\,dX,
\]

\[
P=-\frac{K_0}{\ell}\int_0^\pi\int_0^\pi\int_{-1}^{1}\sigma_y\,d\zeta\,dY\,dX,
\]

\[
R_A=K_0\int_0^\pi\int_0^\pi\int_{-1}^{1}
(\sigma_xG_x+\sigma_yG_y+\tau_{xy}G_\gamma)\,d\zeta\,dY\,dX,
\]

with all local stresses supplied by the frozen NC-M4 current operator, the next work must explicitly perform the remaining analytic integrations and produce closed expressions depending only on

\[
(\Delta,A,\varepsilon_m;b,\ell,h,A_0,f_c,f_t,\varepsilon_{c0},\varepsilon_{t0}).
\]

The task is not complete merely by rewriting the integrands, nor by proving that one local state is integrable. Completion requires explicit global R_m, P, R_A expressions (or a clearly defined finite exact special-function expression with all coefficients/arguments enumerated, not anonymous placeholders).

## Final target

\[
R_A(\Delta,A,\varepsilon_m)=0,
\qquad
R_m(\Delta,A,\varepsilon_m)=0,
\]

and

\[
\det
\begin{bmatrix}
P_{,\Delta}&P_{,A}&P_{,m}\\
R_{A,\Delta}&R_{A,A}&R_{A,m}\\
R_{m,\Delta}&R_{m,A}&R_{m,m}
\end{bmatrix}=0,
\]

where all entries must come from the same globally integrated NC-M4 operator.
