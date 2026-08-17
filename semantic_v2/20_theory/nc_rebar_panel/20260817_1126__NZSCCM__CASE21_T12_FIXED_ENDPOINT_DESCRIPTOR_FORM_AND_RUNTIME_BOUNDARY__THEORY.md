# NZ-SCCM — Case21 T12 fixed-endpoint descriptor form and runtime boundary

**Timestamp:** 2026-08-17 11:26 +08:00  
**Status:** STRUCTURAL DESCRIPTOR FORM CLOSED / EXECUTABLE FORMAL PERIOD RUNTIME OPEN

## 0. Identity

This is an internal substage of the continuing end-to-end task

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

and is not a new physical route.

The frozen state remains

\[
r=\lambda M a(\nu),\qquad
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right).
\]

Formal counters remain

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

---

## 1. Compact source-level R10 stress identity

Retain the source-regular matrix objects `C`, `T`, and `U` from frozen R10. Let

\[
d_C=\det C,\qquad d_T=\det T,\qquad t_T=\operatorname{tr}T.
\]

For the 2x2 tension matrix, Cayley-Hamilton gives

\[
T^n=b_nT-d_Tb_{n-1}I,
\]

with

\[
b_7=t_T^6-5t_T^4d_T+6t_T^2d_T^2-d_T^3,
\]

\[
b_8=t_T^7-6t_T^5d_T+10t_T^3d_T^2-4t_Td_T^3.
\]

Hence the complete normalized R10 matrix stress is kept in the compact form

\[
\boxed{
S=U-a_{cc}d_CC+C\operatorname{adj}T
-\rho a_td_T(b_8I-b_7T).
}
\]

This removes explicit matrix `T^7` from the production graph and does not require a material-series approximation.

An independent pointwise audit at the current Case21 Airy-scalar peak compared this compact expression against the direct spectral R10 source law at five representative `(X,Y,zeta)` states. The maximum absolute physical-stress mismatch was

```text
7.11e-15 MPa
```

(roundoff level).

At the representative point `(X,Y,zeta)=(pi/4,pi/3,-0.2)`, centered finite-difference derivatives of compact and direct source stresses agree to

```text
D      : max abs mismatch = 1.78e-9
q      : max abs mismatch = 2.78e-8
lambda : max abs mismatch = 3.55e-9
```

These derivative comparisons are audit-only; the formal derivative remains the same-source Fréchet/Sylvester tangent.

Decision:

```text
COMPACT_R10_POINTWISE_VALUE_IDENTITY = PASS
COMPACT_R10_POINTWISE_PARAMETER_DERIVATIVE_IDENTITY = PASS_AUDIT
```

---

## 2. T12 structural descriptor

Define

\[
N_x^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\sigma_x\,d\zeta,
\quad
N_y^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\sigma_y\,d\zeta,
\]

\[
N_{xy}^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\tau_{xy}\,d\zeta.
\]

For a weight `w(X,Y)`, define

\[
J_{\alpha,k}[w]=\int_0^\pi\int_0^\pi w(X,Y)N_\alpha^{(k)}(X,Y)\,dYdX.
\]

The current Airy-scalar concrete value package is

\[
\boxed{
\begin{aligned}
T_{12}=\{&J_{x,0}[1],J_{x,0}[\cos2X],J_{x,0}[\cos2Y],J_{x,0}[\cos2X\cos2Y],\\
&J_{y,0}[1],J_{y,0}[\cos2X],J_{y,0}[\cos2Y],J_{y,0}[\cos2X\cos2Y],\\
&J_{xy,0}[\sin2X\sin2Y],\\
&J_{x,1}[\sin X\sin Y],J_{y,1}[\sin X\sin Y],J_{xy,1}[\cos X\cos Y]\}.
\end{aligned}}
\]

Use shorthand

```text
Jx00 Jx20 Jx02 Jx22c
Jy00 Jy20 Jy02 Jy22c
Jxy22s
Jx11s_1 Jy11s_1 Jxy11c_1
```

Then

\[
\boxed{P_c=-\frac{bt}{2\pi^2}\frac{J_{y00}}{1000}}
\]

and, with

\[
C_{vol}=\frac{\varepsilon_0b\ell t}{2\pi^2\,1000},
\]

\[
\boxed{
R_A^c=C_{vol}\left[
-\frac{1+\nu}{4}J_{x00}
-\frac{1-\nu}{4}J_{x20}
+\frac14J_{x22c}
-\frac{1-\nu}{4}J_{y02}
+\frac14J_{y22c}
-\frac12J_{xy22s}
\right].}
\]

Define

\[
F_0=J_{x00}+J_{x20}-J_{x02}-J_{x22c}
+J_{y00}-J_{y20}+J_{y02}-J_{y22c}+2J_{xy22s},
\]

\[
F_1=J_{x11s}^{(1)}+J_{y11s}^{(1)}-2J_{xy11c}^{(1)}.
\]

Then

\[
\boxed{
R_q^c=C_{vol}\left(\frac{M_q}{4}F_0+B_qF_1\right),
}
\]

where

\[
M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),
\qquad
B_q=\frac{\pi^2}{2\varepsilon_0}\frac tb.
\]

The steel terms remain separately exact and closed-form on the current elastic branch.

---

## 3. Direct-source T12 oracle at the current peak

At

```text
D      = 0.7887924801
q      = 0.0018083572562965242
lambda = 0.08623596353826937
```

an independent `128 x 128 x 68` direct-R10 Gauss-Legendre audit gives the following T12 vector in the current physical stress convention:

```text
Jx00      = +8.145683883609898
Jx20      = +3.016950875199921
Jx02      = -2.679407839983953
Jx22c     = -2.254762879355014
Jy00      = -283.28939507865266
Jy20      = +3.835282428608082
Jy02      = -41.48567515226086
Jy22c     = -11.58460291071195
Jxy22s    = +1.1983236728328215
Jx11s_1   = +5.713143459849670
Jy11s_1   = +33.494712972857826
Jxy11c_1  = -2.0187784124555597
```

Contracting these 12 numbers through the equations above and adding the exact steel package reconstructs

```text
P  = 366.7677699713608 kN
Rq = 7.34324899e-5
RA = 9.46700778e-5
```

at the fixed state. The small nonzero residuals are exactly the expected difference between evaluating the `144x144x76`-refined state on the independent `128x128x68` audit executor.

Thus the T12 contraction contains the complete value information needed by `P`, `Rq`, and `RA`.

Decision:

```text
T12_STRUCTURAL_VALUE_COMPLETENESS = PASS_AUDIT
```

The audit values above are read-only oracles and are not formal target values.

---

## 4. T12 same-source derivative oracle

At the same fixed state, the `128x128x68` direct-source audit derivative vectors are:

### with respect to D

```text
[-0.0724534844565,
 -0.0356009029145,
 -0.0157724323824,
 -0.00603940000232,
 -86.4399171689,
 -0.332976926032,
 -17.9337623646,
 -2.19668963766,
 -1.19520051820,
 -0.00591020961060,
 +7.50618607128,
 +1.90715023880]
```

### with respect to q

```text
[+3559.46562420,
 +2928.05850102,
 -314.627791065,
 -1833.55629559,
 +59001.7377192,
 +15042.8896756,
 -10585.3716072,
 -11931.1034648,
 +916.393641726,
 +1885.65788095,
 +6879.89994148,
 -843.044530119]
```

### with respect to lambda

```text
[-8.26010273611,
 -3.02470222486,
 -0.556181681621,
 +2.06294940908,
 -63.2196909407,
 -28.3272344692,
 +1.11075954017,
 +17.9062273274,
 -0.670527062252,
 +0.106608203732,
 -2.28268631410,
 -0.269671766273]
```

After structural contraction plus exact steel derivatives, the audit Jacobian

\[
\partial(P,R_q,R_A)/\partial(D,q,\lambda)
\]

is

\[
\boxed{
\begin{bmatrix}
140.018581456 & -70568.2046060 & 75.4118798682\\
-1587.61924962 & 920300.975844 & -1212.90901511\\
6.41470800273 & -10552.0560544 & 25.2473101371
\end{bmatrix}.}
\]

Solving the two equilibrium derivative equations gives

```text
dq/dD      = 0.003095179742
dlambda/dD = 1.03954845051
dP/dD      = -0.008393 kN
```

which is near zero at the retained direct-source peak, as required.

Decision:

```text
T12_DERIVATIVE_CONTRACT = PASS_AUDIT
FINITE_TANGENT_THICKNESS_BOUND_k_LE_2 = RETAINED
```

Again, this is an audit oracle and not a formal derivative implementation.

---

## 5. Fixed-endpoint formal descriptor that is required

The production object must evaluate the same T12 values and derivatives from the factorised source-level R10 algebra **without** numerical integration.

Conceptually, for each target `j` the required period is

\[
\boxed{
\mathcal P_j(D,q,\lambda)
=\int_0^\pi\int_0^\pi\int_{-1}^{1}
W_j(X,Y,\zeta)\,S_{\alpha_j}[E(D,q,\lambda;X,Y,\zeta)]
\,d\zeta\,dY\,dX,
}
\]

with a finite target weight from the T12 list.

The retained production representation is specifically:

```text
source-regular matrix R10 DAG
 -> projector-free positive-part powers
 -> 2x2 Cayley-Hamilton compact stress
 -> fixed physical zeta endpoints -1,+1
 -> target-side contraction
 -> fixed finite algebraic-period descriptor
```

The event-resolved `<=8-state` representation remains local exact/audit only because its event roots vary over `(X,Y)` and would reintroduce forbidden spatial subdivisions or equivalent clipped-root bookkeeping.

---

## 6. Runtime boundary found in this execution

The repository contains all of the following completed mathematical pieces:

```text
source-level R10 regularity = PASS
compact CH stress = PASS
finite global algebraic-state bound = PASS (<=64)
fixed-endpoint global representation = SELECTED
T12 structural contraction = PASS
finite same-source derivative target family = PASS
```

However, there is still no executable production routine that takes the factorised source-level algebraic object and numerically evaluates the complete fixed-endpoint algebraic periods `P_j` for actual Case21 **without** one of the prohibited escapes:

```text
numerical spatial/thickness quadrature
moving-event XY subdivisions
material-point grids/history
high-order coefficient enumeration / flattened N48+ tensor production
explicit giant rational-coefficient canonicalization
```

The 01:00 historical execution had already shown that explicit canonical rational-annihilator construction becomes intractable even for a real degree-4 compression subtarget, and the 01:43 execution explicitly left the fixed-endpoint three-resultant descriptor as the next unimplemented object.

Therefore the current obstruction is accurately classified as

```text
FORMAL_FIXED_ENDPOINT_ALGEBRAIC_PERIOD_NUMERIC_RUNTIME
  = NOT IMPLEMENTED
```

not as

```text
T12 theory failure
R10 mechanics failure
Airy-scalar failure
proof that an analytic period does not exist
```

No alternative backend is opened automatically in this execution.

---

## 7. Formal Case21 ultimate state remains downstream, not replaced by another task

Once the fixed-endpoint period runtime exists, this **same end-to-end task** continues immediately to

\[
R_q(D,q,\lambda)=0,
\qquad
R_A(D,q,\lambda)=0,
\]

\[
L_3=\det
\begin{bmatrix}
P_D&P_q&P_\lambda\\
R_{q,D}&R_{q,q}&R_{q,\lambda}\\
R_{A,D}&R_{A,q}&R_{A,\lambda}
\end{bmatrix}=0,
\]

with the internal admissibility condition

\[
R_{A,\lambda}>0.
\]

There is no new project-level task between the period runtime and the Case21 solve.

## 8. Verdict

```text
CURRENT_END_TO_END_TASK = CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
COMPACT_R10_VALUE_IDENTITY = PASS
T12_VALUE_CONTRACT = PASS_AUDIT
T12_DERIVATIVE_CONTRACT = PASS_AUDIT
FORMAL_FIXED_ENDPOINT_PERIOD_REPRESENTATION = RETAINED
FORMAL_FIXED_ENDPOINT_PERIOD_NUMERIC_RUNTIME = BLOCKING / NOT IMPLEMENTED
FORMAL_CASE21_Pu = NOT RUN
DIRECT_SOURCE_MECHANICS_ORACLE = 366.767829 kN
```
