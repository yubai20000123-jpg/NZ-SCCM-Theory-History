# NZ-SCCM — 全局 R_m、P、R_A 无积分符号 shared-GKZ master

时间：2026-08-20 18:25 +08:00

状态：`ACTIVE_DERIVATION / GLOBAL_INTEGRAL_SYMBOLS_REMOVED / SAME_MASTER_FAMILY`

## 0. Scope

本节点继续执行 18:10 节点，不重新讨论 TC/CT，不改变 NC-M4。目标是把三个全局对象

- `R_m = ∭ sigma_x dV`
- `P = -(1/ell) ∭ sigma_y dV`
- `R_A = ∭(sigma_x G_x + sigma_y G_y + tau_xy G_gamma)dV`

全部编译为**同一 explicit relative-GKZ master family**上的三个参数移位，不再保留空间积分符号。

## 1. Unified NC-M4 operator

继续采用与九宫格逐状态完全等价的全局写法：

\[
E=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix},
\quad R=(E^2)^{1/2},
\]

\[
E_+=(R+E)/2,\qquad E_c=(R-E)/2,
\]

\[
T=E_+/\varepsilon_{t0},\qquad C=E_c/\varepsilon_{c0},
\]

\[
\mathcal T(T)=1.07515\,T(T+0.09I)[I-0.83T+1.04T^2+0.14T^3]^{-1},
\]

\[
\mathcal C(C)=2C(I+C^2)^{-1},
\]

\[
\alpha=\frac1{1+0.15(\operatorname{tr}T)^2}+0.16\det\mathcal C(C),
\]

\[
\boxed{\Sigma=f_t\mathcal T(T)-f_c\alpha\mathcal C(C).}
\]

This is representation-only and exactly reproduces TT, TC/CT and CC.

## 2. Shared circuit variables

Variable order is fixed as 51 variables:

`u,v,z,U,V,Cx,Cy,D,Ex,Ey,Eg,tau,delta,r0,r1,t0,t1,c0,c1,t20,t21,t30,t31,dt0,dt1,nt0,nt1,kc0,kc1,trt,T0,T1,C0,C1,beta,detC,alpha,S0,S1,sx,Rdet,JT,JC,JB,sy,txy,Gx,Gy,Gg,rA,Jaux`.

The first three are physical transformed coordinates. The other 48 are exact auxiliary variables.

Relations 1–41 are exactly the same as the 18:10 R_m compiler through `JB`.

The additional/shared-target relations are:

42. `sy D-S0 D-S1 Ey=0`

43. `2 txy D-S1 Eg=0`

With

\[
H=A_0+A,
\]

\[
g_{x0}=\pi^2H/b^2,\quad g_{x1}=h\pi^2/(2b^2),
\]

\[
g_{y0}=\pi^2H/\ell^2,\quad g_{y1}=h\pi^2/(2\ell^2),
\]

\[
g_{g0}=2\pi^2H/(b\ell),\quad g_{g1}=h\pi^2/(b\ell),
\]

44. `Gx D-4 gx0 v^2 Cx^2-4 gx1 z u v U V=0`

45. `Gy D-4 gy0 u^2 Cy^2-4 gy1 z u v U V=0`

46. `Gg D-4 gg0 u v Cx Cy+gg1 z Cx Cy U V=0`

47. `rA-sx Gx-sy Gy-txy Gg=0`

For the 48-variable auxiliary residue, the exact auxiliary Jacobian is

\[
J_{aux}^{master}
=512\varepsilon_{t0}^2\varepsilon_{c0}^2D^9Rdet\,JT\,JC\,JB.
\]

Therefore relation 48 is

48. `Jaux-512 eps_t0^2 eps_c0^2 D^9 Rdet JT JC JB=0`.

The three residue numerators are now **single monomials**:

- `Jaux*sx` -> R_m
- `Jaux*sy` -> P
- `Jaux*rA` -> R_A

No CC/TC/TT state-domain split remains in the integration backend.

## 3. Shared Cayley configuration

For every relation

\[
F_j=\sum_k c_{jk}x^{m_{jk}},\qquad j=1,\ldots,48,
\]

the Cayley column is

\[
a_{jk}=\begin{bmatrix}e_j\\m_{jk}\end{bmatrix},
\]

with `e_j in Z^48` and `m_jk in Z^51` according to the fixed variable order.

Actual symbolic compilation gives:

- variables = 51
- relations = 48
- total Cayley rows = 99
- total Cayley columns = 155
- maximum relation monomial support = 5

Hence

\[
\boxed{A^*_{M4,global}\in\mathbb Z^{99\times155}.}
\]

This supersedes the 18:10 R_m-only `87 x 137` compiler as the production **shared target master**. The earlier `61 x 84` state-split support remains a diagnostic pilot only.

## 4. Euler exponents

All 48 relations occur to first denominator power, so the first GKZ block is `-1_48`.

The physical half-angle Jacobian contributes `U^{-1}V^{-1}`.

### R_m

For numerator `Jaux*sx`, the 51-vector `nu_m` equals 1 for every variable except

- `U=0`, `V=0`,
- `sx=2`,
- `Jaux=2`.

Therefore

\[
\boxed{\beta_m=(-\mathbf 1_{48},-\nu_m)^T\in\mathbb Z^{99}.}
\]

### P

For numerator `Jaux*sy`, `nu_P` equals 1 for every variable except

- `U=0`, `V=0`,
- `sy=2`,
- `Jaux=2`.

Thus

\[
\boxed{\beta_P=(-\mathbf 1_{48},-\nu_P)^T.}
\]

### R_A

For numerator `Jaux*rA`, `nu_A` equals 1 for every variable except

- `U=0`, `V=0`,
- `rA=2`,
- `Jaux=2`.

Thus

\[
\boxed{\beta_A=(-\mathbf 1_{48},-\nu_A)^T.}
\]

## 5. No-integral standard-function results

Let

\[
\operatorname{RGKZ}_{A^*_{M4,global}}(\beta;\mathbf c\mid\Gamma_{phys})
\]

mean the physical relative/incomplete A-hypergeometric branch uniquely defined by:

1. the explicit `99 x 155` Cayley configuration generated from the 48 circuit relations;
2. coefficient vector `c` consisting of all 155 printed circuit monomial coefficients;
3. Euler parameter `beta`;
4. fixed physical branch `u,v in [0,infinity)`, `z in [-1,1]`, and the principal-real CH square-root branch `R=(E^2)^(1/2)`.

This is a standard-function call with all defining data fixed, analogous in status to a high-dimensional Appell/Lauricella evaluation; it is not an anonymous material placeholder.

Since

\[
4K_0=2b\ell h/\pi^2,
\]

we obtain

\[
\boxed{
R_m(\Delta,A,\varepsilon_m)
=\frac{2b\ell h}{\pi^2}
\operatorname{RGKZ}_{A^*_{M4,global}}
(\beta_m;\mathbf c\mid\Gamma_{phys}).
}
\]

The axial force is

\[
\boxed{
P(\Delta,A,\varepsilon_m)
=-\frac{2bh}{\pi^2}
\operatorname{RGKZ}_{A^*_{M4,global}}
(\beta_P;\mathbf c\mid\Gamma_{phys}).
}
\]

The amplitude residual is

\[
\boxed{
R_A(\Delta,A,\varepsilon_m)
=\frac{2b\ell h}{\pi^2}
\operatorname{RGKZ}_{A^*_{M4,global}}
(\beta_A;\mathbf c\mid\Gamma_{phys}).
}
\]

No expression on the right contains an unevaluated spatial `Integral` operator.

## 6. Final equilibrium equations at this stage

The two balance equations are now literally

\[
\boxed{
\operatorname{RGKZ}_{A^*_{M4,global}}(\beta_A;\mathbf c\mid\Gamma_{phys})=0,
}
\]

\[
\boxed{
\operatorname{RGKZ}_{A^*_{M4,global}}(\beta_m;\mathbf c\mid\Gamma_{phys})=0.
}
\]

and the load along that equilibrium manifold is

\[
\boxed{
P=-\frac{2bh}{\pi^2}\operatorname{RGKZ}_{A^*_{M4,global}}(\beta_P;\mathbf c\mid\Gamma_{phys}).
}
\]

## 7. Status

`GLOBAL_RM_INTEGRAL_SYMBOL_REMOVED = PASS`

`GLOBAL_P_INTEGRAL_SYMBOL_REMOVED = PASS`

`GLOBAL_RA_INTEGRAL_SYMBOL_REMOVED = PASS`

`SAME_MASTER_CIRCUIT = PASS`

`MASTER_ASTAR_SIZE = 99 x 155`

`MAX_RELATION_SUPPORT = 5`

`FORMAL_SPATIAL_QUADRATURE = 0`

This is **not** a claim that the generic function reduces to elementary, Appell F1, or a short Lauricella FD. The exact generic result is the explicit relative-GKZ standard function above.

Next task: differentiate this same master with respect to `(Delta,A,epsilon_m)` by coefficient differentiation / GKZ parameter-contiguity, produce all nine Jacobian entries with no spatial integral signs, and substitute them into the expanded limit determinant.