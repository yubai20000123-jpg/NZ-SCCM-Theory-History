# NZ-SCCM — unified q–U explicit kinematic ledger, generalized work and blind-preflight R01

**Time:** 2026-08-27 11:35 +08:00  
**Parent contract:** `20260827_1114 unified global/local q–U + common-curvature rebuild R00`  
**Status:** `R1 PASS / R2 PASS_PRE_R06 / R3 PASS / BH032_BH050_BLIND_NUMERICAL_BRANCH BLOCKED_BY_TWO_MISSING_FROZEN_INPUTS / FEM_NOT_OPENED_FOR_ROOT_SELECTION`

This execution follows the user-approved rule that the missing global/local `qU` relation and the missing common `q -> kappa` relation are **both** restored from the same explicit kinematics. Neither is treated as an empirical correction.

Frozen exclusions remain:

```text
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH_PRODUCTION = NO
FEM_OR_TEST_IN_ROOT_SELECTION = 0
INTERFACE_SLIP = OFF
FITTED_qU_COEFFICIENT = NONE
FITTED_CURVATURE_FACTOR = NONE
```

---

## 1. Explicit global base recovered

Use the already-existing explicit Nguyen/Marguerre half-wave variables

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad k=b/\ell,
\]

\[
s_X=\sin X,\;c_X=\cos X,\;s_Y=\sin Y,\;c_Y=\cos Y,\qquad H_s=s_Xs_Y .
\]

The stress-free initial global imperfection and current added displacement are

\[
w_g^0=bq_0H_s,\qquad \Delta w_g=bqH_s,
\]

so the total current global amplitude is

\[
W=b(q_0+q),\qquad W_0=bq_0.
\]

The retained compatible in-plane basis is

\[
A_x=-\frac14-\frac{\nu k^2}{2}s_X^2-\frac12s_Y^2+s_X^2s_Y^2,
\]

\[
A_y=\frac{\nu}{4}-\frac{k^2}{2}s_X^2-\frac{\nu}{2}s_Y^2+k^2s_X^2s_Y^2,
\]

\[
A_\gamma=-2kH_sc_Xc_Y.
\]

Let

\[
S_q=q_0q+\frac12q^2.
\]

The old explicit global/common strain field is

\[
\boxed{
\varepsilon_x^g
=
\varepsilon_0\nu D+\varepsilon_0\alpha A_x
+\pi^2S_q(s_Y^2-s_X^2s_Y^2)
+\frac{\pi^2q}{b}zH_s
}
\]

\[
\boxed{
\varepsilon_y^g
=
-\varepsilon_0D+\varepsilon_0\alpha A_y
+\pi^2k^2S_q(s_X^2-s_X^2s_Y^2)
+\frac{\pi^2k^2q}{b}zH_s
}
\]

\[
\boxed{
\gamma_{xy}^g
=
-2\varepsilon_0\alpha kH_sc_Xc_Y
+2\pi^2kS_qH_sc_Xc_Y
-\frac{2\pi^2kq}{b}z c_Xc_Y .
}
\]

This field already contains two distinct global pieces:

1. `GG membrane`: the \(S_q=q_0q+q^2/2\) terms;
2. `common bending`: the terms linear in \(zq\).

Therefore the common curvature was **already present in the original explicit theory**. The later SSUHPC terminal bridge lost this kinematic identity when it allowed independent terminal \(\kappa_x,\kappa_y\).

The q-virtual kernels are

\[
\varepsilon_{x,q}^{g}
=
\pi^2(q_0+q)(s_Y^2-s_X^2s_Y^2)+\frac{\pi^2}{b}zH_s,
\]

\[
\varepsilon_{y,q}^{g}
=
\pi^2k^2(q_0+q)(s_X^2-s_X^2s_Y^2)+\frac{\pi^2k^2}{b}zH_s,
\]

\[
\gamma_{q}^{g}
=
2\pi^2k(q_0+q)H_sc_Xc_Y-\frac{2\pi^2k}{b}z c_Xc_Y.
\]

The \(\alpha\)-kernels are

\[
\varepsilon_{x,\alpha}=\varepsilon_0A_x,\quad
\varepsilon_{y,\alpha}=\varepsilon_0A_y,\quad
\gamma_{\alpha}=\varepsilon_0A_\gamma .
\]

---

# 2. Full two-scale kinematic ledger

For steel face \(f\in\{+,-\}\), introduce a physical local-cell registration
\((x_{0f},y_{0f})\) and orientation/sign \(s_f=\pm1\), and retain the R02 local shape

\[
\phi_f(\xi,\eta)
=
(1-\cos k_x\xi)(1-\cos k_y\eta),
\]

\[
\xi=x-x_{0f},\qquad \eta=y-y_{0f},
\qquad k_x=2\pi/L_x,\quad k_y=2\pi/L_y.
\]

Initial and current local fields are

\[
w_{\ell f}^0=s_fA_0\phi_f,\qquad
w_{\ell f}=s_fU_f\phi_f.
\]

The steel-face total out-of-plane field is

\[
\boxed{w_f=w_g+w_{\ell f}.}
\]

Define

\[
d_f=U_f^2-A_0^2
\]

and the global/local cross amplitude

\[
\boxed{
\Delta_f
=s_f(WU_f-W_0A_0)
=s_fb\,[qU_f+q_0(U_f-A_0)].
}
\]

## 2.1 Core

Under the first perfect-composite reconstruction contract, the UHPC core has no local steel subscale \(w_\ell\). Hence

\[
\boxed{
\boldsymbol\varepsilon_c
=
\boldsymbol\varepsilon^g(D,\alpha,q,z).
}
\]

Its ledger is therefore:

```text
in-plane compatible field    PRESENT
GG membrane q(q+2q0)         PRESENT
common q-curvature            PRESENT
GL qU                         NOT APPLICABLE to core
LL U^2                        NOT APPLICABLE to core
local steel bending           NOT APPLICABLE to core
```

## 2.2 Steel-face membrane geometric increments

Expanding the total von-Karman slope exactly gives

\[
\Delta\varepsilon_{xx,f}^{geom}
=
\Delta\varepsilon_{xx}^{GG}
+\Delta\varepsilon_{xx,f}^{GL}
+\Delta\varepsilon_{xx,f}^{LL},
\]

\[
\boxed{
\Delta\varepsilon_{xx,f}^{GL}
=\Delta_f\psi_x\phi_{f,x},
\qquad
\Delta\varepsilon_{xx,f}^{LL}
=\frac12d_f\phi_{f,x}^2
}
\]

and

\[
\boxed{
\Delta\varepsilon_{yy,f}^{GL}
=\Delta_f\psi_y\phi_{f,y},
\qquad
\Delta\varepsilon_{yy,f}^{LL}
=\frac12d_f\phi_{f,y}^2.
}
\]

For engineering shear,

\[
\boxed{
\Delta\gamma_{xy,f}^{GL}
=
\Delta_f(\psi_x\phi_{f,y}+\psi_y\phi_{f,x}),
}
\]

\[
\boxed{
\Delta\gamma_{xy,f}^{LL}
=
d_f\phi_{f,x}\phi_{f,y}.
}
\]

Thus the gross steel-face midsurface strain is

\[
\boxed{
\boldsymbol\varepsilon_f^{mid}
=
\boldsymbol\varepsilon^g(D,\alpha,q,z_f)
+
\boldsymbol\varepsilon_f^{GL}
+
\boldsymbol\varepsilon_f^{LL}.
}
\]

The global/common strain includes its own GG membrane and common bending; these are not added a second time.

## 2.3 Common bending versus local bending

The common incremental curvature is generated only by the global added displacement

\[
\boxed{
\boldsymbol\kappa^g(q)
=
-bq\{\psi_{,xx},\psi_{,yy},2\psi_{,xy}\}.
}
\]

For the BH family, \(a=2b,m_*=2,\ell=b\); at the global antinode,

\[
\boxed{\kappa_x^g=\kappa_y^g=\pi^2q/b.}
\]

The local steel curvature is a separate subscale quantity. With local face-thickness coordinate \(\zeta_f\),

\[
\boxed{
\Delta\kappa_{\ell,xx}
=-s_f(U_f-A_0)\phi_{f,xx},
}
\]

\[
\boxed{
\Delta\kappa_{\ell,yy}
=-s_f(U_f-A_0)\phi_{f,yy},
}
\]

\[
\boxed{
\Delta\kappa_{\ell,xy}
=-2s_f(U_f-A_0)\phi_{f,xy}.
}
\]

Conceptually the full steel shell strain through its own thickness is

\[
\boldsymbol\varepsilon_f(\zeta_f)
=
\boldsymbol\varepsilon_f^{mid}
+
\zeta_f\boldsymbol\kappa_\ell .
\]

In the retained R02 condensation, however, this local bending contribution is represented by the existing local bending energy \(U_b\). It must **not** be integrated again through thickness and also retained as \(U_b\).

---

# 3. Old-theory audit: what existed, what was lost

| relation | original explicit global theory | R02/R06 | later SSUHPC terminal bridge | rebuilt status |
|---|---|---|---|---|
| GG \(q_0q+q^2/2\) membrane | YES | external face strain input only | Airy demand retained | retain once |
| common \(q\to\kappa^g\) | YES, explicit \(zq\) terms | no ownership | LOST by independent \(\kappa_x,\kappa_y\) | restore |
| LL \(U^2-A_0^2\) mean shortening | no | YES, \(c_xd,c_yd\) | inherited | retain once |
| LL incompatibility/Airy fluctuation | no | YES, `HARMONICS` + \(U_a\) | inherited | retain once |
| local bending \(U-A_0\) | no | YES, \(U_b\) | inherited | retain once |
| GL \(qU\) membrane | NO | NO, PBLCell has no global phase/q | absent | add |
| GL incompatibility/Airy fluctuation | NO | NO | absent | add |
| reciprocal \(U\to q\) generalized work | NO in terminal Airy bridge | NO | absent | add |
| independent pointwise \(M_x=M_x^d,M_y=M_y^d\) | not needed in original full virtual work | n/a | YES | remove from rebuilt global closure |

The crucial anti-double-counting result is:

\[
\boxed{\text{do not add another standalone }U^2\text{ correction.}}
\]

The existing R02 already contains the LL mean and LL incompatibility energy.

---

# 4. R02 LL regression and the correct GL extension

For

\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta),
\]

the exact local-cell means are

\[
\boxed{
\frac12\langle\phi_x^2\rangle=\frac{3k_x^2}{8}=c_x,
\qquad
\frac12\langle\phi_y^2\rangle=\frac{3k_y^2}{8}=c_y,
}
\]

\[
\boxed{\langle\phi_x\phi_y\rangle=0.}
\]

These are exactly the coefficients used by R02:

\[
m_x=e_x-c_xd,\qquad m_y=e_y-c_yd.
\]

More strongly, the current R02 term

\[
U_a=tE K_A d^2
\]

is exactly the plane-stress complementary strain energy of the LL Airy fluctuation generated by the incompatibility

\[
\boxed{
\nabla^4F_{LL}
=
-E\,d_f
(\phi_{,xx}\phi_{,yy}-\phi_{,xy}^2).
}
\]

The finite harmonic coefficients generated by this source are exactly the current R02 harmonic set

```text
(0,1) +1/2
(0,2) -1/2
(1,0) +1/2
(1,1) -1
(1,2) +1/2
(2,0) -1/2
(2,1) +1/2
```

with the same biharmonic divisors.

Therefore the correct unified extension is not

```text
old full R02 stress + ad-hoc Hooke qU stress.
```

It is

\[
\boxed{
\nabla^4F_{\ell}
=
\nabla^4F_{LL}
+
\nabla^4F_{GL}
}
\]

where

\[
\boxed{
\nabla^4F_{GL}
=
-E\,\Delta_f
[
\psi_{,xx}\phi_{,yy}
+\phi_{,xx}\psi_{,yy}
-2\psi_{,xy}\phi_{,xy}
].
}
\]

The resulting local compatibility energy contains

\[
\boxed{
\Pi_{\ell}^{Airy}
=
\Pi_{LL}
+
2\Pi_{GL,LL}
+
\Pi_{GL},
}
\]

schematically proportional to

\[
d_f^2,\qquad d_f\Delta_f,\qquad \Delta_f^2.
\]

Thus `GL -> 0` returns R02 exactly, while the mixed energy appears automatically without duplicating LL.

---

# 5. Generalized residual architecture recovered from the explicit base

The original explicit theory already used axial shortening \(D\) as a continuation/control coordinate and solved the internal generalized equilibria. Therefore the minimal rebuilt state does not need independent section curvatures.

For prescribed \(D\), use

\[
\boxed{
\mathbf y=[q,\alpha,U_+,U_-]^T.
}
\]

Before any active R06 projection, define

\[
\boxed{
R_\alpha
=
\delta W_{int}[\partial\boldsymbol\varepsilon/\partial\alpha]=0,
}
\]

\[
\boxed{
R_q
=
\delta W_{int}[\partial\boldsymbol\varepsilon/\partial q]
-\frac{\partial W_{ext}}{\partial q}=0,
}
\]

\[
\boxed{
R_{U_+}=0,\qquad R_{U_-}=0.
}
\]

The axial reaction remains

\[
\boxed{
P(D,q,\alpha,U_+,U_-)
=
-\frac1\ell\iiint \sigma_y\,dV
}
\]

with the steel-local terms included in the current stress/resultant field.

No independent \(\kappa_x,\kappa_y\) appear. No separate pointwise

\[
M_x^{sec}=M_x^d,\qquad M_y^{sec}=M_y^d
\]

are retained.

---

# 6. Explicit q-U kernels and reciprocal coupling

Since

\[
\Delta_f=s_f(WU_f-W_0A_0),
\]

\[
\boxed{
\frac{\partial\Delta_f}{\partial q}=s_fbU_f,
\qquad
\frac{\partial\Delta_f}{\partial U_f}=s_fW,
\qquad
\frac{\partial^2\Delta_f}{\partial q\partial U_f}=s_fb.
}
\]

Therefore the GL q-kernels are

\[
\boxed{
\varepsilon_{xx,q}^{GL}
=s_fbU_f\,\psi_x\phi_x,
}
\]

\[
\boxed{
\varepsilon_{yy,q}^{GL}
=s_fbU_f\,\psi_y\phi_y,
}
\]

\[
\boxed{
\gamma_{xy,q}^{GL}
=s_fbU_f(\psi_x\phi_y+\psi_y\phi_x).
}
\]

The U-kernels are

\[
\boxed{
\varepsilon_{xx,U}^{GL+LL}
=s_fW\psi_x\phi_x+U_f\phi_x^2,
}
\]

\[
\boxed{
\varepsilon_{yy,U}^{GL+LL}
=s_fW\psi_y\phi_y+U_f\phi_y^2,
}
\]

\[
\boxed{
\gamma_{xy,U}^{GL+LL}
=s_fW(\psi_x\phi_y+\psi_y\phi_x)
+2U_f\phi_x\phi_y .
}
\]

The mixed kinematic kernels are explicitly

\[
\boxed{
\varepsilon_{xx,qU}=s_fb\psi_x\phi_x,
}
\]

\[
\boxed{
\varepsilon_{yy,qU}=s_fb\psi_y\phi_y,
}
\]

\[
\boxed{
\gamma_{xy,qU}
=s_fb(\psi_x\phi_y+\psi_y\phi_x).
}
\]

For the pre-R06 conservative R02 branch, with consistent material tangent \(\mathbf C_t\),

\[
\frac{\partial R_q}{\partial U_f}
=
\int
\left[
\boldsymbol\varepsilon_{,q}^T\mathbf C_t\boldsymbol\varepsilon_{,U_f}
+
\boldsymbol\sigma:\boldsymbol\varepsilon_{,qU_f}
\right]dV
+\text{local-Airy/bending terms},
\]

and the same common energy gives

\[
\boxed{
\frac{\partial R_q}{\partial U_f}
=
\frac{\partial R_{U_f}}{\partial q}
}
\]

where the material operator is conservative and the state is smooth.

Most importantly,

\[
\boxed{
\partial R_q/\partial U_f\ne0,\qquad
\partial R_{U_f}/\partial q\ne0
}
\]

whenever the physical GL harmonic moment is nonzero.

Hence the previously observed triangular q-U matrix was a consequence of the old separated global residual, not a property of the actual total kinematics.

Once R06 radial projection is active, tangent symmetry is **not assumed**. The active-set residual can remain algebraically coupled but may be nonconservative. This is a later constitutive/work-conjugacy audit, not grounds to delete qU.

---

# 7. Exact direct-limit condition for the rebuilt state

For fixed \(D\), solve

\[
\mathbf R(D,\mathbf y)=
[R_q,R_\alpha,R_{U_+},R_{U_-}]^T=0.
\]

Along a regular branch,

\[
\mathbf R_{\mathbf y}\,\frac{d\mathbf y}{dD}
=-\mathbf R_D.
\]

The ultimate load is a stationary axial reaction along that constrained branch,

\[
\frac{dP}{dD}=0.
\]

Without explicitly inverting \(\mathbf R_{\mathbf y}\), this condition is the bordered determinant

\[
\boxed{
L_5=
\det
\begin{bmatrix}
P_D&P_q&P_\alpha&P_{U_+}&P_{U_-}\\
R_{q,D}&R_{q,q}&R_{q,\alpha}&R_{q,U_+}&R_{q,U_-}\\
R_{\alpha,D}&R_{\alpha,q}&R_{\alpha,\alpha}&R_{\alpha,U_+}&R_{\alpha,U_-}\\
R_{U_+,D}&R_{U_+,q}&R_{U_+,\alpha}&R_{U_+,U_+}&R_{U_+,U_-}\\
R_{U_-,D}&R_{U_-,q}&R_{U_-,\alpha}&R_{U_-,U_+}&R_{U_-,U_-}
\end{bmatrix}=0.
}
\]

This is the direct extension of the old explicit 3-state \(L\) condition. It does not require a symmetric tangent and does not reuse the superseded independent-section \(J_4\) fold.

---

# 8. Zero-quadrature exact harmonic backend

For any real frequency \(\omega\), interval \([x_0,x_0+L]\),

\[
\boxed{
\frac1L\int_{x_0}^{x_0+L}e^{i\omega x}\,dx
=
e^{i\omega(x_0+L/2)}
\operatorname{sinc}\!\left(\frac{\omega L}{2}\right),
}
\]

where

\[
\operatorname{sinc}z=\frac{\sin z}{z},\qquad \operatorname{sinc}0=1.
\]

Every GG/GL/LL term is a finite product of sines/cosines and therefore a finite sum of complex exponentials. Every cell integral is an exact finite harmonic moment. A two-dimensional separable term is the product of two such one-dimensional moments.

For a repeating local grid, the half-wave integral is a finite exact sum of the registered cell moments. No Gauss point, Simpson point, material point, or spatial collocation is introduced.

The companion backend file in this commit implements these identities and the R02 LL regression.

---

# 9. R3 numerical regression checks

The backend was executed for the frozen BH cell geometries.

## BH032

\[
b=1600,\quad L_x=360,\quad L_y=355.5555556\ {\rm mm},
\]

\[
k_x=0.01745329252,\qquad k_y=0.01767145868\ {\rm mm^{-1}}.
\]

Exact LL means:

\[
\boxed{c_x=1.14231532420\times10^{-4}\ {\rm mm^{-2}}},
\]

\[
\boxed{c_y=1.17105169407\times10^{-4}\ {\rm mm^{-2}}}.
\]

R02 formula gives

\[
K_A=1.58478790282955\times10^{-8}\ {\rm mm^{-4}}.
\]

Independent exact harmonic Airy-energy evaluation gives exactly the same numerical value,

\[
\boxed{
K_A^{Airy}=1.58478790282955\times10^{-8}
}
\]

at machine precision.

## BH050

\[
b=2500,\quad L_x=562.5,\quad L_y=555.5555556\ {\rm mm},
\]

\[
k_x=0.01117010721,\qquad k_y=0.01130973355\ {\rm mm^{-1}}.
\]

\[
\boxed{c_x=4.67892356792\times10^{-5}\ {\rm mm^{-2}}},
\]

\[
\boxed{c_y=4.79662773893\times10^{-5}\ {\rm mm^{-2}}}.
\]

\[
K_A=2.65883289599584\times10^{-9}\ {\rm mm^{-4}},
\]

\[
\boxed{
K_A^{Airy}=2.65883289599584\times10^{-9}
}
\]

with relative difference \(1.6\times10^{-16}\).

Thus

```text
R02_LL_MEAN_REGRESSION = PASS
R02_LL_AIRY_ENERGY_REGRESSION = PASS
NO_U2_DOUBLE_COUNT = PASS
```

## 9.1 Exact GL phase-sensitivity preflight

For the BH family,

\[
\alpha/k_x=9/80=0.1125,\qquad
\beta/k_y=1/9.
\]

Using exact cell harmonic moments, the maximum normalized phase amplitudes are

\[
\max_{\rm phase}
\frac{|\langle\psi_x\phi_x\rangle|}
{\alpha k_x}
=0.11069910295,
\]

\[
\max_{\rm phase}
\frac{|\langle\psi_y\phi_y\rangle|}
{\beta k_y}
=0.10933244736.
\]

These values are nonzero and their signs change with the physical cell registration/orientation.

Therefore:

\[
\boxed{\text{GL cell-average work does not vanish identically.}}
\]

and

\[
\boxed{\text{the missing }(x_0,y_0,s_f)\text{ data cannot be ignored.}}
\]

---

# 10. Blind BH032/BH050 branch preflight

The requested numerical blind branch was **not** allowed to invent a root. Two frozen inputs required by the newly completed equations are presently absent from the current SSUHPC contract.

## 10.1 Blocker A — physical PBL-cell registration

The current `PBLCell` contract contains only

```text
Lx, Ly, t, E, nu, fy, A0
```

and no global registration \((x_0,y_0)\) or local sign/orientation \(s_f\).

That was sufficient for LL because the old \(U^2\) operator is phase-insensitive after cell averaging. It is insufficient for GL because the exact work contains terms such as

\[
\langle\psi_x\phi_x\rangle,\quad
\langle\psi_y\phi_y\rangle,\quad
\langle\psi_x\phi_y+\psi_y\phi_x\rangle,
\]

whose values and signs depend on registration.

A repository search during this execution did not recover a validated BH032/BH050 full-cell origin/phase contract. No antinode-centered or favorable sign is substituted.

## 10.2 Blocker B — current UHPC shear law for full-halfwave virtual work

The current SSUHPC substitution contract supplies directional current UHPC \(N_x-M_x\) and \(N_y-M_y\) laws from exact thickness primitives.

The recovered explicit global residual, however, contains nonzero shear virtual kernels over the continuous half-wave:

\[
\gamma_\alpha=\varepsilon_0A_\gamma,
\]

\[
\gamma_q=
2\pi^2k(q_0+q)H_sc_Xc_Y
-\frac{2\pi^2k}{b}z c_Xc_Y.
\]

Therefore the full current virtual work contains

\[
\int \tau_{xy}^{UHPC}\gamma_{\alpha}\,dV,
\qquad
\int \tau_{xy}^{UHPC}\gamma_q\,dV.
\]

The currently frozen SSUHPC directional N-M source does not define a current \(\tau_{xy}^{UHPC}\) operator for these states.

It would be an unapproved material change to silently set

```text
tau_UHPC = 0
```

or

```text
tau_UHPC = Gc * gamma
```

or to import an unrelated NC shear degradation law.

Hence a unique rebuilt numerical \(R_q,R_\alpha\) cannot yet be evaluated.

## 10.3 R06 note

R06 can remain an admissibility concept for the first reconstruction. But once it is active, its radial projection evaluates the returned steel resultant at a projected state. Its exact work-conjugacy with the new q-U generalized coordinates must be audited. This does not block the pre-R06 derivation above, but it prevents claiming a globally conservative post-R06 potential without a separate proof.

---

# 11. Execution gates

```text
STEP_1_FULL_KINEMATIC_LEDGER = PASS
STEP_2_OLD_THEORY_DUPLICATION_OMISSION_AUDIT = PASS
STEP_3_Rq_RU_RECIPROCAL_COUPLING_DERIVATION = PASS_PRE_R06
STEP_4_ZERO_QUADRATURE_HARMONIC_BACKEND = PASS
R02_LL_REGRESSION = PASS
GL_NONZERO_PHASE_SENSITIVITY = PASS

STEP_5_BH032_BLIND_NEW_ROOT = BLOCKED_NOT_INVENTED
STEP_5_BH050_BLIND_NEW_ROOT = BLOCKED_NOT_INVENTED
FEM_POSTCHECK_FOR_NEW_ROOTS = NOT_OPENED

BLOCKER_A = PBL_CELL_GLOBAL_REGISTRATION_PHASE_NOT_FROZEN
BLOCKER_B = SSUHPC_CURRENT_UHPC_SHEAR_OPERATOR_NOT_FROZEN
```

No new \(P_u\) is reported because doing so before resolving A and B would require exactly the sort of hidden assumption/calibration prohibited by the project.

---

# 12. Next executable inputs, without reopening the architecture

Only two source closures are needed before the new blind solve:

1. **geometry closure:** recover the actual BH032/BH050 PBL cell origins/registration/orientation from the accepted equal-contract geometry/model scripts or CAE construction contract;
2. **UHPC material closure:** recover/authorize a source-consistent current in-plane shear response compatible with the retained UHPC x/y current operator, so the already-recovered explicit \(R_q,R_\alpha\) can be evaluated over the full continuous half-wave.

After those are frozen, the next numerical solve is uniquely defined:

\[
[R_\alpha,R_q,R_{U_+},R_{U_-}]=0
\]

for each prescribed \(D\), followed by

\[
P(D)
\]

and the bordered direct-limit event

\[
L_5=0
\]

plus competing admissibility events.

At that point BH032 and BH050 can be rerun blind with no independent section \(\kappa\), no separate pointwise \(M_x/M_y\) closure, and no omitted qU term.
