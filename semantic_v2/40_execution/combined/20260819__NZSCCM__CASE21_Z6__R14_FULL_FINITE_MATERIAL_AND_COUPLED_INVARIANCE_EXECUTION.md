# NZ-SCCM R14 — Case21 + Z6 full finite material constructors and exact coupled-solution invariance execution

**Date:** 2026-08-19  
**Formal discretization:** NONE  
**Purpose:** finish the removal of the old material-series representation for all constituents used by Case21 and Z6, then transfer the full coupled solution by exact pointwise-operator invariance rather than by any spatial discretization or finite-prefix calculation.

## 0. Governing rule

No Gauss/Simpson/adaptive quadrature, no spatial grid/cell/material point, no collocation, no discrete oracle, no finite-prefix convergence sequence.

The only admissible operation here is exact algebraic replacement of each finite current material law by a single global finite expression, followed by exact pointwise identity and consequent equality of the continuous generalized functionals.

## 1. Case21 concrete: R13 identity

R13 already established the exact global truncated-power spline

\[
u_R(r)=p_1(r)+\sum_{j=3}^{5}A_j(r-1)_+^j+\sum_{j=3}^{5}B_j(r-10)_+^j,
\]

with \(x_+=(x+|x|)/2\), together with its spectral matrix lift. This is exactly the original frozen three-branch R10 tension law, not an approximation.

Therefore for every admissible physical strain state

\[
\mathcal M_{R13}^{c}(\varepsilon)=\mathcal M_{R10}^{c}(\varepsilon)
\]

pointwise. Since the spline is C2, the same-source first derivative is identical everywhere as well.

Case21 reinforcement was already a finite closed constitutive contribution; it never requires the removed material-series layer.

Hence for Case21

\[
P_{R14}=P_{old},\qquad R_{q,R14}=R_{q,old},\qquad R_{\alpha,R14}=R_{\alpha,old},\qquad J_{\lim,R14}=J_{\lim,old}
\]

as exact continuous functions of \((D,q,\alpha)\).

## 2. Z6 face steel: remove the old analytic-series representation completely

The frozen face-steel law is the finite radial cap

\[
\boldsymbol\sigma_f=g(r)\boldsymbol\sigma_f^{tr},\qquad
r=\frac{(\sigma_{VM}^{tr})^2}{f_y^2}\ge0,
\]

\[
g(r)=\begin{cases}1,&r\le1,\\r^{-1/2},&r>1.\end{cases}
\]

Let \(v=\sqrt r=\sigma_{VM}^{tr}/f_y\ge0\). Since

\[
\max(1,v)=\frac{1+v+|v-1|}{2},
\]

the complete radial cap is exactly the single global finite algebraic function

\[
\boxed{
 g_f(r)=\frac{2}{1+\sqrt r+|\sqrt r-1|}
}
\]

or, using radicals only,

\[
\boxed{
 g_f(r)=\frac{2}{1+\sqrt r+\sqrt{(\sqrt r-1)^2}}
}.
\]

For \(r\le1\) the denominator is 2 and \(g_f=1\). For \(r>1\) the denominator is \(2\sqrt r\) and \(g_f=r^{-1/2}\). Thus the identity is exact on the whole physical domain.

No elastic/plastic spatial partition is needed.

The same-source directional tangent is obtained from the same finite function. Away from \(r=1\),

\[
g_f'(r)=0\quad(r<1),\qquad g_f'(r)=-\frac{1}{2r^{3/2}}\quad(r>1).
\]

At the continuous yield surface \(r=1\), the stress itself is continuous. Therefore the moving yield surface introduces no stress-jump distribution term into the derivative of the continuous integral; one-sided/semismooth source derivatives give the same integrated tangent identity.

## 3. Z6 web/PBL steel: remove the old analytic-series representation completely

Let the elastic trial scalar stress be

\[
x=E_s\varepsilon_y^w.
\]

The frozen ideal elastic-perfectly-plastic law is

\[
\sigma_y^w=\operatorname{clip}(x,-f_y,f_y).
\]

This is exactly the single global algebraic absolute-value formula

\[
\boxed{
\sigma_y^w=\frac{|x+f_y|-|x-f_y|}{2}
}
\]

or

\[
\boxed{
\sigma_y^w=\frac{\sqrt{(x+f_y)^2}-\sqrt{(x-f_y)^2}}{2}.
}
\]

It reproduces \(-f_y\), \(x\), and \(+f_y\) in the three respective scalar ranges without material-region partition.

The same-source tangent is

\[
E_t^w=E_s\quad(|x|<f_y),\qquad E_t^w=0\quad(|x|>f_y),
\]

with the source-consistent one-sided/semismooth value at the two kink points. Again the stress is continuous, so no moving-boundary stress-jump term is created in the continuous generalized derivative.

## 4. Complete Z6 finite material identity

The complete Z6 constituent map is now

```text
R13 finite global R10 concrete
+ finite global face radial-cap algebraic function
+ finite global web/PBL clip algebraic function
```

with no material-series coordinate and no finite prefix.

Therefore, pointwise for every continuous halfwave state,

\[
\mathcal M_{R14}^{Z6}(\varepsilon)=\mathcal M_{old}^{Z6}(\varepsilon).
\]

Consequently the exact continuous generalized functionals satisfy

\[
P_{R14}=P_{old},\qquad
R_{q,R14}=R_{q,old},\qquad
R_{\alpha,R14}=R_{\alpha,old},
\]

and their same-source first derivatives give the identical limit Jacobian.

## 5. Exact coupled-solution invariance theorem

Let

\[
\mathbf G(D,q,\alpha)=
\begin{bmatrix}
R_q\\R_\alpha\\\det J_{\lim}
\end{bmatrix}.
\]

Since all constituent current maps and same-source derivatives are pointwise identical under the finite global constructors,

\[
\boxed{
\mathbf G_{new}(D,q,\alpha)\equiv\mathbf G_{old}(D,q,\alpha)
}
\]

and

\[
\boxed{
P_{new}(D,q,\alpha)\equiv P_{old}(D,q,\alpha).
}
\]

Hence the complete root set is invariant. This is exact functional identity, not a numerical calibration and not a discrete verification.

The previously released coupled roots therefore remain solutions of the new finite-constructor system without any re-use of the old material series as a production backend.

## 6. Case21 full coupled solution under the finite constructor

Released coupled state:

\[
D_u=0.7887924801,
\]
\[
q_u=0.0018083572562965242,
\]
\[
\alpha_u=0.002506908330448254.
\]

The corresponding finite kinematics are

\[
M=0.02907033478365149,\qquad
B=0.06754686155676540.
\]

The exact reinforcement contribution is

\[
P_s=28.844798318\ \mathrm{kN}.
\]

The invariant continuous concrete functional is

\[
P_c=337.92303037\ \mathrm{kN}.
\]

Therefore

\[
\boxed{P_u^{Case21}=366.767828685\ \mathrm{kN}}.
\]

Post-solve comparison only:

\[
P_{exp}=368.312749744\ \mathrm{kN},\qquad
\boxed{\mathrm{error}=-0.419459\%}.
\]

Compared with the rejected uniform-branch stationary value \(538.273498279\) kN, the coupled plate solution is lower by 31.8622%.

## 7. Z6 full coupled solution under the finite constructor

Released coupled state:

\[
D_u=1.36180798,
\]
\[
q_u=0.0264854039,
\]
\[
\alpha_u=1.8954326279510263.
\]

The invariant continuous component forces are

\[
P_{c,eff}=22.8171044\ \mathrm{MN},
\]
\[
P_{face}=18.5564373\ \mathrm{MN},
\]
\[
P_w=7.0325797\ \mathrm{MN}.
\]

Therefore

\[
\boxed{P_u^{Z6}=48.4061215\ \mathrm{MN}}.
\]

Post-solve comparison only:

\[
P_{Zhou}=49.4867667519\ \mathrm{MN},\qquad
\boxed{\mathrm{error}=-2.183706\%},
\]

\[
P_{Winter}=50.1858541295\ \mathrm{MN},\qquad
\boxed{\mathrm{error}=-3.546283\%}.
\]

Compared with the rejected uniform-branch stationary value \(90.150438116\) MN, the coupled plate solution is lower by 46.3052%.

## 8. Interpretation

The severe uniform-branch overprediction disappears once the correct coupled structural limit system is restored. There is no evidence of a new systematic overprediction caused by removal of the material series.

The exact finite-constructor replacement is now complete for all constituents used in the two current benchmark specimens:

```text
Case21 concrete R10      -> global finite R13 matrix spline
Case21 reinforcement     -> existing finite closed form
Z6 concrete R10          -> global finite R13 matrix spline
Z6 face steel radial cap -> global finite algebraic max/absolute-value form
Z6 web/PBL ideal EP      -> global finite algebraic clip form
```

The old infinite analytic representations may remain only as historical provenance. They are not needed to define or evaluate the material laws.

## 9. Status

```text
MATERIAL_SERIES_REPLACEMENT_CASE21 = COMPLETE
MATERIAL_SERIES_REPLACEMENT_Z6 = COMPLETE
FULL_COUPLED_FUNCTIONAL_IDENTITY = EXACT
CASE21_COUPLED_ROOT_INVARIANCE = PASS
Z6_COUPLED_ROOT_INVARIANCE = PASS
UNBUCKLED_BRANCH_AS_Pu = REJECTED
SPATIAL_DISCRETIZATION = NONE
FINITE_PREFIX = NONE
DISCRETE_ORACLE = NONE
```

This execution does not create a new theory gate. The next production step can proceed directly with the finite global material constructors as the canonical material layer.
