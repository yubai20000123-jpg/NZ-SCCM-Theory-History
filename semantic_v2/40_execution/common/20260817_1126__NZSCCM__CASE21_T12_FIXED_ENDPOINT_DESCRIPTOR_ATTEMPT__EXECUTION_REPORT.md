# NZ-SCCM — Case21 T12 fixed-endpoint descriptor attempt

**Timestamp:** 2026-08-17 11:26 +08:00  
**Status:** EXECUTED TO TRUE RUNTIME BOUNDARY / FORMAL Pu NOT RELEASED

## 0. Scope and execution identity

This execution is an internal stage of the already-promised end-to-end task

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

It is **not** a new theory route and was not created because of the user's question. The user explicitly asked that the route remain unchanged and asked why the previous reply appeared to insert another task before Case21. That presentation inconsistency is corrected in the companion 11:26 governance lock.

The execution goal is to advance the formal zero-spatial Case21 calculation as far as the current repository actually permits, while preserving

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
R10 = FROZEN
reinforcement before solve = REQUIRED
Airy-scalar r=lambda*M*a = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

No experiment is used in any implementation choice.

---

## 1. Compact source-level R10 identity audit

The current compact source-level stress representation is

\[
S=U-a_{cc}\det(C)C+C\operatorname{adj}(T)
-\rho a_t\det(T)(b_8I-b_7T),
\]

with the exact 2x2 Cayley-Hamilton recurrences

\[
b_7=t^6-5t^4d+6t^2d^2-d^3,
\]

\[
b_8=t^7-6t^5d+10t^3d^2-4td^3,
\]

where `t=tr(T)` and `d=det(T)`.

At the current Case21 Airy-scalar peak, five representative `(X,Y,zeta)` points were evaluated by both:

1. the direct spectral frozen-R10 source law used by the continuum oracle;
2. the compact CH source-level expression above.

The maximum physical-stress discrepancy was

```text
max abs stress mismatch = 7.11e-15 MPa
```

which is roundoff-level.

At `(X,Y,zeta)=(pi/4,pi/3,-0.2)`, centered finite-difference parameter sensitivities of compact and direct source stresses differed by at most

```text
D      : 1.78e-9
q      : 2.78e-8
lambda : 3.55e-9
```

These derivative checks are audit-only. Production differentiation remains the same-source Fréchet/Sylvester tangent.

Verdict:

```text
COMPACT_SOURCE_R10_VALUE_IDENTITY = PASS
COMPACT_SOURCE_R10_PARAMETER_DERIVATIVE_IDENTITY = PASS_AUDIT
```

---

## 2. T12 value audit at the current peak

Retain the current peak state

```text
D      = 0.7887924801
q      = 0.0018083572562965242
lambda = 0.08623596353826937
```

and use an independent `128 x 128 x 68` direct-R10 Gauss-Legendre executor **only as an oracle** for the already-derived T12 structural contract.

The resulting physical-stress T12 vector is

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

Contracting only these 12 values to `Pc`, `RAc`, `Rqc` and adding the already-closed exact steel package reconstructs

```text
P  = 366.7677699713608 kN
Rq = +7.34324899e-5
RA = +9.46700778e-5
```

at the fixed state.

The state itself was refined on the independent `144 x 144 x 76` oracle; therefore the small nonzero residuals on the `128 x 128 x 68` oracle are expected and do not indicate a contraction error.

Verdict:

```text
T12_VALUE_COMPLETENESS = PASS_AUDIT
```

---

## 3. T12 same-source derivative audit

The 128-grid oracle gives the following T12 derivative vectors.

### dT12/dD

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

### dT12/dq

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

### dT12/dlambda

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

After T12 contraction and addition of exact steel derivatives, the resulting audit Jacobian is

\[
\boxed{
\frac{\partial(P,R_q,R_A)}{\partial(D,q,\lambda)}
=
\begin{bmatrix}
140.018581456 & -70568.2046060 & 75.4118798682\\
-1587.61924962 & 920300.975844 & -1212.90901511\\
6.41470800273 & -10552.0560544 & 25.2473101371
\end{bmatrix}.
}
\]

Solving the two equilibrium derivative equations gives

```text
dq/dD      = 0.003095179742
dlambda/dD = 1.03954845051
dP/dD      = -0.008393 kN
```

at the retained direct-source peak. The residual derivative is already very close to zero, consistent with the fact that the peak state was refined by a different higher-order oracle.

Verdict:

```text
T12_SAME_SOURCE_DERIVATIVE_CONTRACT = PASS_AUDIT
FINITE_TANGENT_THICKNESS_FAMILY_k_LE_2 = RETAINED
```

---

## 4. Historical runtime boundary re-audit

The current repository already contained the exact reason why a formal Case21 `Pu` could not immediately follow the 11:05 mechanics qualification.

The 01:00 execution had established:

```text
source-level matrix regularity = PASS
real compression target algebraic degree = 4 / PASS
explicit canonical rational annihilator = FAIL_TRACTABILITY
surviving representation = factorised algebraic-period / descriptor object
```

and explicitly left an executable full compact R10 algebraic-period target evaluator open.

The 01:43 execution then closed the actual structural thickness-to-XY interface and selected

```text
GLOBAL_FIXED_ENDPOINT_POSITIVE_PART_FACTORISED_PERIOD
```

for production, but its unique next implementation was still the common fixed-endpoint stress-moment descriptor.

Therefore the absence of a current formal Pu is not caused by the 11:05 qualification step and not caused by the user's present question. The numerical fixed-endpoint algebraic-period runtime was already unfinished before the Airy-scalar mechanics correction was finalized.

---

## 5. Actual execution attempt and fail-fast boundary

The current task advanced the already-selected compact route through:

```text
source-level compact stress identity -> PASS
T12 value contraction               -> PASS_AUDIT
T12 derivative contraction          -> PASS_AUDIT
```

The next operation required for a formal result is an executable map

```text
(D,q,lambda)
  -> source-regular factorised R10 period
  -> T12 values + same-source derivatives
```

with no numerical `zeta/X/Y` quadrature and no high-order coefficient enumeration.

The repository does not yet contain such a numeric period runtime. The historical 01:00 implementation evidence further shows that naively canonicalizing the algebraic object into large rational annihilators is not tractable and is explicitly not an authorized production representation.

Accordingly, this execution stops at the genuine implementation boundary rather than pretending that the audit T12 values are formal values or silently falling back to Gauss/N48/cells.

```text
FORMAL_FIXED_ENDPOINT_ALGEBRAIC_PERIOD_NUMERIC_RUNTIME = NOT IMPLEMENTED
FORMAL_T12_NUMERIC_VALUE = NOT RELEASED
FORMAL_T12_NUMERIC_DERIVATIVES = NOT RELEASED
FORMAL_CASE21_Rq_RA_L3_SOLVE = NOT RUN
FORMAL_CASE21_Pu = NOT RELEASED
```

---

## 6. Why no new project task is created

The correct end-to-end identity remains

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

The fixed-endpoint period runtime is an internal unresolved implementation layer of this same task.

If it becomes executable, the same task must continue directly to

\[
R_q=0,\qquad R_A=0,\qquad L_3=0,
\]

without waiting for a newly named user task.

If it remains blocked, the project status stays blocked at this implementation layer; the blocker must not be converted into another theory route or another endless backend chain.

---

## 7. Final status

```text
CURRENT_END_TO_END_TASK = CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
ROUTE_CHANGED_DUE_TO_USER_QUESTION = NO
COMPACT_SOURCE_R10 = PASS
T12_VALUE_CONTRACT = PASS_AUDIT
T12_DERIVATIVE_CONTRACT = PASS_AUDIT
FORMAL_PERIOD_REPRESENTATION = RETAINED
FORMAL_PERIOD_NUMERIC_RUNTIME = BLOCKING / NOT IMPLEMENTED
FORMAL_CASE21_Pu = NOT RUN
DIRECT_SOURCE_MECHANICS_ORACLE = 366.767829 kN
CASE21_Pf_EXP = 368.312750 kN
```
