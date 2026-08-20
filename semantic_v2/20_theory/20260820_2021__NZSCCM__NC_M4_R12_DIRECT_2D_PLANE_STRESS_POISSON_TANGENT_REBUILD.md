# NZ-SCCM — NC-M4-R12 direct 2D rebuild after deleting R3

Time: 2026-08-20 20:21 +08:00

Status: `ACTIVE_MATERIAL_CANDIDATE / R3_DELETED / DIRECT_2D_POISSON_TANGENT_GATE_PASS`

## 1. Governance correction

Delete R3 completely. No equivalent-uniaxial material coordinates, no Nguyen dilation variables, no second state grid. The material state grid returns to raw physical principal strains `(eps1,eps2)`.

Restore the project kinematic Poisson baseline:

\[
\varepsilon_x=\nu\Delta/\ell+\varepsilon_m+\text{von-Karman membrane term}+\text{bending term},
\]

with `epsilon_m` now interpreted as the additional nonlinear transverse membrane correction, not the whole transverse strain.

However, the direct 2D material map itself must still satisfy the plane-stress tangent at the origin.

## 2. Required origin tangent

In principal coordinates the unique isotropic plane-stress tangent is

\[
D_0^{(p)}=\frac{E_0}{1-\nu^2}
\begin{bmatrix}1&\nu\\\nu&1\end{bmatrix}.
\]

In engineering plate coordinates:

\[
D_0=\frac{E_0}{1-\nu^2}
\begin{bmatrix}
1&\nu&0\\
\nu&1&0\\
0&0&(1-\nu)/2
\end{bmatrix}.
\]

## 3. Tension primitive

\[
U_T(\varepsilon)=f_t T_4(\varepsilon/\varepsilon_{t0}),\quad \varepsilon\ge0,
\]

\[
T_4(t)=1.07515\frac{t(t+0.09)}{1-0.83t+1.04t^2+0.14t^3}.
\]

Since `T4'(0)=0.0967635`, enforce

\[
\varepsilon_{t0}=0.0967635\frac{f_t}{E_0},
\]

so `U_T'(0)=E0`.

## 4. Compression primitive generalized without empirical parameter

Let

\[
m_c=\frac{E_0\varepsilon_{c0}}{f_c}.
\]

Define

\[
C_m(c)=\frac{m_c c}{1+(m_c-2)c+c^2},\qquad c=-\varepsilon/\varepsilon_{c0}\ge0,
\]

and

\[
U_C(\varepsilon)=-f_c C_m(-\varepsilon/\varepsilon_{c0}),\quad \varepsilon\le0.
\]

Then exactly

\[
C_m(0)=0,\quad C_m'(0)=m_c,\quad C_m(1)=1,\quad C_m'(1)=0,
\]

hence

\[
U_C'(0)=E_0.
\]

For `m_c=2`, this reduces to the previous `2c/(1+c^2)`.

## 5. Minimal direct 2D Poisson correction

Define

\[
K_\nu=\frac{\nu E_0}{1-\nu^2},
\]

\[
\Pi_1=K_\nu(\varepsilon_2+\nu\varepsilon_1),\qquad
\Pi_2=K_\nu(\varepsilon_1+\nu\varepsilon_2).
\]

This is not an equivalent-strain transformation. It is an explicit linear cross-coupling term added directly to the 2D current stress map.

## 6. Smooth R2 candidate retained symbolically

To preserve a single smooth rational TC law and avoid the R2 cap/front, define

\[
\Gamma_T(\varepsilon_t)=\frac{1}{1+k_{tc}(\varepsilon_t/\varepsilon_{c0})^2},
\]

where `k_tc` remains a material-shape parameter pending source/physics audit. The tangent proof below is independent of its numerical value because

\[
\Gamma_T(0)=1,\qquad \Gamma_T'(0)=0.
\]

The old use of `epsilon_t0` as the TC reduction scale is prohibited.

CC enhancement remains

\[
\eta(c_1,c_2)=1+k_\eta C_m(c_1)C_m(c_2),
\]

with current candidate `k_eta=0.16`; this factor has zero first derivative contribution at the origin.

## 7. Four explicit raw-principal-strain regions

### TT: eps1>0, eps2>0

\[
\sigma_1=U_T(\varepsilon_1)+\Pi_1,
\qquad
\sigma_2=U_T(\varepsilon_2)+\Pi_2.
\]

### TC: eps1>0, eps2<0

\[
\sigma_1=U_T(\varepsilon_1)+\Pi_1,
\]

\[
\sigma_2=\Gamma_T(\varepsilon_1)U_C(\varepsilon_2)+\Pi_2.
\]

### CT: eps1<0, eps2>0

\[
\sigma_1=\Gamma_T(\varepsilon_2)U_C(\varepsilon_1)+\Pi_1,
\]

\[
\sigma_2=U_T(\varepsilon_2)+\Pi_2.
\]

### CC: eps1<0, eps2<0

Let `c_i=-eps_i/eps_c0`. Then

\[
\sigma_1=\eta(c_1,c_2)U_C(\varepsilon_1)+\Pi_1,
\]

\[
\sigma_2=\eta(c_1,c_2)U_C(\varepsilon_2)+\Pi_2.
\]

No equivalent-strain state grid remains.

## 8. Exact plane-stress tangent proof

Because

\[
U_T(0)=U_C(0)=0,\quad U_T'(0)=U_C'(0)=E_0,
\]

and

\[
\Gamma_T(0)=1,\quad \Gamma_T'(0)=0,
\]

while

\[
\eta(0,0)=1,\quad \nabla\eta(0,0)=0,
\]

every quadrant has the same first-order tangent.

For example in any quadrant,

\[
\frac{\partial\sigma_1}{\partial\varepsilon_1}\Big|_0
=E_0+\nu K_\nu
=\frac{E_0}{1-\nu^2},
\]

\[
\frac{\partial\sigma_1}{\partial\varepsilon_2}\Big|_0
=K_\nu
=\frac{\nu E_0}{1-\nu^2},
\]

and symmetrically for sigma2. Thus all TT/TC/CT/CC approach exactly the same plane-stress tangent.

For pure engineering shear at the origin, the spectral rotation gives

\[
\tau_{12}=\frac{E_0}{2(1+\nu)}\gamma_{12},
\]

which equals the third diagonal component of the engineering plane-stress matrix.

Therefore

`DIRECT_2D_POISSON_TANGENT_GATE = PASS`.

## 9. Restored structural kinematic interface

The corrected transverse strain field is

\[
\varepsilon_x=
\nu\frac{\Delta}{\ell}+\varepsilon_m
+S\frac{\pi^2}{b^2}\cos^2X\sin^2Y
+zA\frac{\pi^2}{b^2}\sin X\sin Y,
\]

\[
\varepsilon_y=
-\frac{\Delta}{\ell}
+S\frac{\pi^2}{\ell^2}\sin^2X\cos^2Y
+zA\frac{\pi^2}{\ell^2}\sin X\sin Y,
\]

\[
\gamma_{xy}=
2S\frac{\pi^2}{b\ell}\cos X\sin X\sin Y\cos Y
-2zA\frac{\pi^2}{b\ell}\cos X\cos Y,
\]

where `S=A0*A+A^2/2`.

At `A=0` and in the linear regime, `Rm=0` gives exactly `epsilon_m=0`, hence the physical transverse strain is `nu*Delta/ell`; the added epsilon_m is only the nonlinear correction.

## 10. Analytic-integration compatibility

The only principal-strain radical remains

\[
d_\varepsilon=\sqrt{(\varepsilon_x-\varepsilon_y)^2+\gamma_{xy}^2}.
\]

`U_T`, `U_C`, `Gamma_T`, `eta`, and `Pi_i` are rational functions of raw principal strains and parameters. No second radical, no local material Newton, no equivalent-strain branch grid, no min/max cap, and no new spatial discretization are introduced.

Hence the existing half-angle -> algebraic lift -> residue -> relative/incomplete GKZ architecture remains valid. The old master dimensions must be recompiled; they are not assumed unchanged.

## 11. Case21 constants for audit

For Case21 (`E0=20321 MPa`, `nu=0.18`, `fc=21.23 MPa`, `eps_c0=0.00209`):

\[
m_c=2.00051295337,
\]

so the generalized compression primitive is almost identical to the old `2c/(1+c^2)` while now matching `E0` exactly.

\[
K_\nu=3780.26043820\ \text{MPa},
\]

\[
\frac{E_0}{1-\nu^2}=21001.4468789\ \text{MPa},
\]

\[
G_0=\frac{E_0}{2(1+\nu)}=8610.59322034\ \text{MPa}.
\]

## 12. Current status

- R3 equivalent-strain repair: rejected and deleted.
- Raw CC/TC/CT/TT grid: restored.
- Poisson baseline in structural kinematics: restored.
- Direct 2D plane-stress tangent: exact in all four quadrants.
- Compression primitive initial tangent: generalized exactly without a fitted parameter.
- R2 TC softening strength parameter `k_tc`: intentionally left symbolic pending separate material audit.
- Analytic integration architecture: preserved.
