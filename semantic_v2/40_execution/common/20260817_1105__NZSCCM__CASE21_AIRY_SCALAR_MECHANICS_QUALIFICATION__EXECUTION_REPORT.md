# NZ-SCCM — Case21 Airy-scalar mechanics qualification execution report

**Timestamp:** 2026-08-17 11:05 +08:00  
**Status:** EXECUTED / MECHANICS QUALIFICATION PASS / NO NEW FORMAL Pu

## 0. Scope

This execution implements the planned pre-production qualification task. It does **not** publish a new ultimate load and does **not** change the current mechanics oracle.

The active structure/material identity is retained:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
R10 physical current operator = FROZEN
reinforcement before coupled solve = REQUIRED
Airy-scalar membrane closure r=lambda*M*a(nu) = ACTIVE
formal spatial sampling/quadrature/subdivision = 0 / 0 / 1
formal thickness quadrature = 0
```

The direct-source Gauss-Legendre executor is used only as an audit oracle for the nonlinear internal-stability check.

---

## 1. Case21 load identity correction

The repeatedly confused experimental loads are separated as follows:

```text
experimental buckling load  Pcr_exp = 75.6 kip = 336.2855541137 kN
experimental failure load   Pf_exp  = 82.8 kip = 368.3127497436 kN
Nguyen FE buckling load                = 298 kN
```

Therefore the current `Pu` oracle is correctly compared with `Pf_exp=368.312750 kN`.

Current direct-source mechanics oracle retained:

```text
Pu = 366.767828685 kN
Delta(Pu-Pf_exp) = -1.544921058 kN
error = -0.419459 %
```

No experiment entered the solve.

---

## 2. Exact Airy-scalar virtual-work qualification

For the restricted coordinate

\[
r=\lambda M(q)a,
\]

the generalized residual transformation is

\[
R_\lambda=M R_A,
\]

\[
R_q^{restricted}=R_q^{base}+\lambda M_qR_A.
\]

Hence the current solver pair

```text
Rq_base = 0
RA      = 0
```

is exactly row-equivalent to the residual pair in `(q,lambda)` coordinates for `M>0`.

This closes the concern that the current direct-source solver might be omitting the `q` derivative of `r=lambda*M*a`: the omitted term is exactly proportional to `RA` and vanishes on the retained internal equilibrium. At equilibrium, the Jacobian change is a nonsingular row operation, so the bordered load-stationarity determinant has the same zero locus.

Result:

```text
SCALAR_VIRTUAL_WORK_EQUIVALENCE = PASS_EXACT
```

---

## 3. Elastic benchmark qualification

### 3.1 Pure isotropic continuum

Direct complete-halfwave integration gives the reduced scalar residual

\[
\widetilde R_A^c
=\frac{\pi^2M(2\nu^2+3)}{16(1-\nu^2)}(\lambda-1).
\]

Therefore

```text
pure isotropic plane-stress continuum -> lambda = 1 exactly
internal scalar stiffness -> positive for |nu|<1 and M>0
```

At `lambda=1`, the classical membrane stresses are recovered exactly:

\[
\sigma_x/(E\varepsilon_0)=-M\cos2Y/4,
\]

\[
\sigma_y/(E\varepsilon_0)=-D+(M/2)\sin^2X,
\]

\[
\tau_{xy}=0.
\]

### 3.2 Reinforced linear scalar subspace

The previous shorthand statement `lambda=1 in linear elasticity` is too broad once the reinforcement phases are included before the solve.

For the actual equal directional reinforcement ratio, the exact linear scalar result is

\[
\lambda_{lin,RC}=0.999266844854884
+0.0096124785693025\,D/M.
\]

Thus `lambda != 1` in a reinforced linear state is expected; the exact `lambda=1` benchmark belongs to the single isotropic continuum limit.

Audit-only low-load regression:

```text
D = 0.001
q_direct_R10 = 6.1576802417e-6
M = 7.2785542134e-5
lambda_direct_R10 = 1.1312936303
lambda_linear_RC  = 1.1313326135
absolute difference = 3.8983e-5
```

This demonstrates that the direct frozen-R10 scalar branch approaches the derived reinforced linear scalar limit.

Result:

```text
PURE_CONTINUUM_AIRY_LIMIT = PASS_EXACT
REINFORCED_LINEAR_SCALAR_LIMIT = PASS_EXACT
OLD_UNSCOPED_LAMBDA_EQ_1_WORDING = CORRECTED
```

---

## 4. Nonlinear scalar internal-stability audit

Inherited scalar stability condition:

\[
R_{A,\lambda}>0
\]

for every active `M>0` state.

The actual residual conjugate to `lambda` has tangent

\[
K_{\lambda\lambda}=M R_{A,\lambda}.
\]

A centered finite derivative of the **direct frozen-R10 oracle** was used only to audit this mechanics sign. It is not a formal derivative implementation.

### 4.1 Connected-branch checkpoints (`96 x 96 x 52` audit oracle)

| D | q | lambda | P (kN) | M | dRA/dlambda | M*dRA/dlambda |
|---:|---:|---:|---:|---:|---:|---:|
|0.100000|0.0005340721|0.77739552|95.652916|0.0069785983|3.85160654|0.026878815|
|0.300000|0.0010471136|0.22710179|239.280371|0.0149508338|10.56676105|0.157981888|
|0.500000|0.0013251286|0.02618487|323.618582|0.0197902304|16.74379200|0.331363501|
|0.700000|0.0016079168|0.02598698|362.084855|0.0250871666|22.27051452|0.558704108|
|0.78879248|0.0018082686|0.08616850|366.768500|0.0290685301|25.24259138|0.733765028|

All sampled active states are positive.

A denser `64 x 64 x 36` origin-connected audit from `D=.05` to `.79` also remained positive; the smallest sampled `dRA/dlambda` was about `1.96004` at `D=.05`.

### 4.2 Peak-state derivative convergence

At the frozen peak coordinate `D=0.7887924801`, re-solving `(q,lambda)` on increasingly fine audit grids gives:

| audit grid | q | lambda | P (kN) | dRA/dlambda | M*dRA/dlambda |
|---|---:|---:|---:|---:|---:|
|64x64x36|0.0018078932|0.08588180|366.771335|25.23434831|0.733332709|
|80x80x44|0.0018081530|0.08608094|366.769422|25.24033169|0.733640014|
|96x96x52|0.0018082686|0.08616850|366.768500|25.24259138|0.733765028|
|112x112x60|0.0018083235|0.08621019|366.768085|25.24522567|0.733869847|
|128x128x68|0.0018083461|0.08622754|366.767924|25.24720029|0.733938822|
|144x144x76|0.0018083573|0.08623596|366.767829|25.24850924|0.733982616|

At the `144x144x76` state the centered-difference sensitivity is stable across step sizes:

```text
h=2e-4  -> dRA/dlambda = 25.2485090876
h=1e-4  -> dRA/dlambda = 25.2485092067
h=5e-5  -> dRA/dlambda = 25.2485092364
h=2e-5  -> dRA/dlambda = 25.2485092449
h=1e-5  -> dRA/dlambda = 25.2485092459
```

Hence:

```text
SCALAR_INTERNAL_STABILITY_BEFORE_CURRENT_PEAK = PASS_DIRECT_SOURCE_AUDIT
NO_INTERNAL_MEMBRANE_STABILITY_EVENT_FOUND_BEFORE_PEAK
```

The formal fixed-endpoint evaluator must later reproduce the same positive sign using the source-consistent tangent rather than a finite-difference audit.

---

## 5. Small-driver audit

At the current direct-source peak:

```text
D = 0.7887924801
q = 0.0018083573
M = 0.02907033478
(M/4)/D = 0.0092135563 = 0.921356 %
lambda = 0.0862359635
r = [-0.00073954,-0.00051392,+0.00062673,-0.00051392,+0.00062673]
```

Relative to the same frozen-R10 `r=0` direct-source backbone:

```text
Pu_r0 = 368.73145691 kN
Pu_Airy_scalar = 366.76782869 kN
Delta = -1.96362822 kN = -0.532536 %
```

The correction remains a small perturbation for Case21, consistent with its small membrane driver.

Result:

```text
CASE21_SMALL_M_DRIVER_SCALING = PASS
```

---

## 6. Closed-form reinforcement package

Because the Case21 reinforcement remains elastic at the current peak, no steel spatial compiler is required.

With

```text
Cs = 36.908355 kN
CR = 2.94090386184375
```

the exact steel load is

\[
P_s=C_s(D-M/4).
\]

At the current peak:

```text
Ps_closed_form = 28.84479831 kN
Ps_direct_oracle = 28.84479832 kN
```

The exact scalar residual terms are

\[
R_A^s=-C_R[8D\nu(\nu+1)+M\{5-(4\nu^2+5)\lambda\}],
\]

\[
R_q^s=C_RM_q[8D(\nu-1)+M(9-5\lambda)].
\]

Therefore steel values and their `(D,q,lambda)` derivatives are algebraically closed for the current supported branch.

---

## 7. Formal concrete target preparation

The current concrete value-level structural interface is reduced to the 12 independent direct target moments documented in the companion theory file:

```text
Jx00, Jx20, Jx02, Jx22c
Jy00, Jy20, Jy02, Jy22c
Jxy22s
Jx11s_1, Jy11s_1, Jxy11c_1
```

They are sufficient for

```text
Pc
RAc
Rqc
```

without reconstructing a full stress surface.

For same-source derivatives, the already-established finite thickness bound is retained:

```text
stress moments:  k = 0,1
tangent kernels: k = 0,1,2
```

The `q` derivative is the only one that requires the `k=2` tangent layer because the Nguyen `epsilon_,q` field contains both `zeta^0` and `zeta^1` parts.

No high-order coefficient enumeration is needed by the structural contract.

---

## 8. Gate verdict

```text
CASE21_LOAD_IDENTITY = PASS / CORRECTED
SCALAR_VIRTUAL_WORK_EQUIVALENCE = PASS_EXACT
PURE_ISOTROPIC_AIRY_DEGENERATION = PASS_EXACT
REINFORCED_LINEAR_SCALAR_BENCHMARK = PASS_EXACT
CURRENT_NONLINEAR_SCALAR_INTERNAL_STABILITY_TO_PEAK = PASS_AUDIT
CASE21_SMALL_DRIVER_SCALING = PASS
STEEL_FORMAL_PACKAGE = CLOSED_FORM
CONCRETE_VALUE_TARGET_CONTRACT = T12
TANGENT_THICKNESS_BOUND = k<=2
NEW_Pu = NOT_RUN
CURRENT_DIRECT_SOURCE_MECHANICS_TARGET_Pu = 366.767829 kN
FORMAL_ZERO_SPATIAL_NUMERIC_RELEASE = OPEN
```

## 9. Unique next task

```text
CASE21_AIRY_SCALAR_FORMAL_T12_FIXED_ENDPOINT_DESCRIPTOR_GATE
```

Required next output:

1. source-regular fixed-endpoint R10 evaluation of the concrete `T12` package;
2. same-source derivatives with respect to `(D,q,lambda)`;
3. no spatial numerical quadrature or subdivision;
4. no material-point grid/history;
5. no high-order coefficient enumeration;
6. no new Pu until the descriptor itself passes identity and derivative audits.