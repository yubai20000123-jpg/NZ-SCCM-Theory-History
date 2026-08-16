# NZ-SCCM — dual-holonomic regularity audit, 64-state local-matrix erratum, and anti-loop production pivot

**Timestamp:** 2026-08-16 21:36 +08:00  
**Executed gate:** `UNIFIED_V1_FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME_GATE`

## 0. Decision first

This gate was executed as a **decisive anti-loop gate**, not as authorization to open another indefinite symbolic-backend chain.

The denominator-gauged dual moment identity is exact for regular denominator signatures, but the currently used rationalized quadratic-tower basis has an **interior apparent singularity** even for the retained smooth noncommuting prototype. The physical algebraic atom is regular there; the singularity is introduced only by rationalizing the local basis coefficients. Therefore a production implementation that splits the compact R10 target into denominator-tagged rational pieces can create artificial non-integrable terms unless an algebraic Hermite/integral-basis regularization layer is added.

Under the explicit anti-loop instruction, that new symbolic layer is **not opened as the next production gate**. The exact-algebraic/holonomic branch is retained as a research branch, but is paused as the Pu production blocker.

Production is returned to the already successful zero-spatial N48-C1/MM + General-D15 analytic compiler chain, with the already accepted five-term membrane-stress redistribution added before Schur condensation.

```text
DUAL_DENOMINATOR_GAUGE_IDENTITY = PASS_EXACT
REGULAR_GAUGE_MOMENT_RECURRENCE = PASS_EXACT
CURRENT_QUADRATIC_TOWER_RATIONAL_BASIS_GLOBAL_REGULARITY = FAIL_APPARENT_INTERIOR_POLE
PHYSICAL_SMOOTH_ATOM_AT_POLE = REGULAR
INTEGRAL_BASIS_OR_HERMITE_REGULARIZATION = MATHEMATICALLY_RELEVANT_BUT_NOT_OPENED
EXACT_ALGEBRAIC_HOLONOMIC_Pu_PRODUCTION_ROUTE = PAUSED_RESEARCH_BRANCH
N48_C1_MM_GENERAL_D15_PRODUCTION_ROUTE = REACTIVATED
FIVE_TERM_MEMBRANE_REDISTRIBUTION = REQUIRED
NEXT_PRODUCTION_ACTION = CASE21_MEMBRANE_REDISTRIBUTED_N48_PRODUCTION
NEW_Pu = NOT_RUN_IN_THIS_GATE
```

---

## 1. Erratum to the 20:59 local four-state derivative matrix

The 20:59 text correctly stated

\[
q'=\ell_q q,
\qquad
s'=(c_0+c_1q)s,
\]

\[
(qs)'=c_1Q\,s+(\ell_q+c_0)qs.
\]

For basis

\[
\mathbf v=(1,q,s,qs)^T,
\]

the corresponding matrix must therefore be

\[
\boxed{
A_{loc}=\begin{bmatrix}
0&0&0&0\\
0&\ell_q&0&0\\
0&0&c_0&c_1\\
0&0&c_1Q&\ell_q+c_0
\end{bmatrix}.
}
\]

The 20:59 displayed matrix had the two off-diagonal factors `c1` and `c1*Q` interchanged. This is a transcription/implementation-matrix error, not a change in the stated differential equations.

Consequences:

- the local state dimension remains 4;
- the three-pair compositum dimension remains 64;
- the Kronecker-sum sparsity count remains 159/4096 because the nonzero pattern is unchanged;
- the existence of a finite derivative/moment state remains valid;
- any future implementation that uses the explicit local matrix must use the corrected placement above.

The 21:18 fiber target audit did not use this x-dependent local derivative matrix and is therefore not invalidated by this erratum.

---

## 2. Exact denominator-gauge identity

Retain a denominator-cleared holonomic system

\[
\boxed{d(x)\mathbf V'=B(x)\mathbf V},
\]

where `d` is polynomial and `B` is a polynomial matrix.

Suppose one compact dual-target term has the form

\[
\int_{-1}^{1}\frac{\mathbf p(x)^T\mathbf V(x)}{G(x)}\,dx,
\]

with polynomial vector `p` and a polynomial denominator signature `G` that is nonzero on the complete thickness interval.

Define the gauged state

\[
\boxed{\mathbf W=\mathbf V/G}.
\]

Since `V=G W`, direct differentiation gives

\[
\boxed{(dG)\mathbf W'=(BG-dG'I)\mathbf W.}
\]

No rational coefficient vector is required. Both sides are polynomial when `d,B,G` are polynomial.

Define moments

\[
\mathbf M_n^{(G)}=\int_{-1}^{1}x^n\mathbf W(x)\,dx.
\]

Writing

\[
dG=\sum_j h_jx^j,
\qquad
BG-dG'I=\sum_j H_jx^j,
\]

integration by parts gives the exact vector recurrence

\[
\boxed{
[x^ndG\,\mathbf W]_{-1}^{1}
=
\sum_j(n+j)h_j\mathbf M_{n+j-1}^{(G)}
+
\sum_jH_j\mathbf M_{n+j}^{(G)}.
}
\]

Thus the x-dependent rational dual target **would** connect exactly to the finite holonomic moment system if its denominator signatures can be represented globally without introducing artificial poles.

---

## 3. Decisive regularity audit on the retained smooth noncommuting prototype

Retain

\[
E(x)=\begin{bmatrix}
1/5+x/3&1/7+x/5\\
1/7+x/5&-1/4+2x/7
\end{bmatrix},
\qquad \eta=1/400.
\]

For the smooth quadratic tower

\[
q^2=Q(x),
\qquad
s^2=A(x)+2q,
\]

the rationalized local coefficients are

\[
\ell_q=Q'/(2Q),
\]

\[
c_0=\frac{A'A-4\ell_qQ}{2(A^2-4Q)},
\qquad
c_1=\frac{-2A'+2\ell_qA}{2(A^2-4Q)}.
\]

The discriminant factor is exactly

\[
\boxed{
A^2-4Q
=\frac{(260x-21)^2(28624x^2+47880x+50121)}{31116960000}.
}
\]

Therefore the rationalized basis coefficients contain an apparent pole at

\[
\boxed{x_*=21/260=0.080769230769\ldots},
\]

which lies inside the complete physical thickness interval `[-1,1]`.

However the physical atom is regular at this point. Exact/numerical values are

```text
Q(x*) = 0.005895909729058568681686891517153...
q(x*) = 0.076784827466489554401642313730226...
s(x*) = 0.554201506553309739021547866043520...
```

and the physically relevant logarithmic derivative combination has the finite exact limit

\[
\boxed{
\lim_{x\to x_*}(c_0+c_1q)
=\frac{29577184}{61042095}
=0.484537498262469530247937918907\ldots
}
\]

Thus the pole exists in `c0`/`c1` separately but cancels in the algebraic combination that multiplies the physical state.

This proves that a naive denominator-signature split of the rationalized basis can destroy a removable cancellation and create artificial singular terms even though the R10 source itself is smooth.

---

## 4. Regular-gauge audit still passes away from apparent poles

For denominator signatures `G` whose roots do not intersect `[-1,1]`, the gauge construction above works exactly. Using the same smooth prototype and a regular signature formed from the quadratic and quartic denominator factors, the corrected local system gives polynomial `dG` and polynomial `BG-dG'I`.

An audit-only high-precision direct integration of the resulting four-state recurrence for `n=0,1,2` gave relative residuals of order `1e-15`, limited by numerical cancellation in the audit oracle. The formal identity is algebraic and exact.

This result is important because the obstruction is **not** the gauge algebra itself. The obstruction is global regularity of the chosen rationalized algebraic basis.

---

## 5. Why the exact branch is paused instead of opening another backend layer

A mathematically standard way to continue would be to regularize the algebraic representation with an integral basis / algebraic Hermite reduction so that apparent poles are cancelled before moment reduction. That is a legitimate research direction, but it is a new symbolic-integration architecture layer.

The project no longer treats theorem-level exact-integration backend refinement as a hard engineering gate when the accepted zero-spatial analytic compiler already gives a calculable production chain. Therefore this gate applies the anti-loop rule:

```text
DO_NOT_OPEN_ANOTHER_EXACT_BACKEND_LAYER = YES
DO_NOT_START_INTEGRAL_BASIS_IMPLEMENTATION_NOW = YES
DO_NOT_RETURN_TO_RC1_POLYNOMIAL_EXPLOSION = YES
```

The exact-algebraic work remains retained evidence:

- exact R10 finite matrix source lift;
- quartic algebraic generator reduction;
- smooth quartic order-2 holonomic equation;
- 64-state quadratic compositum;
- CH elimination of matrix `T^7`;
- adjoint field-target identity.

It is not deleted or declared mathematically wrong. It is simply no longer allowed to block the production Pu calculation.

---

## 6. Production pivot: return to the successful zero-spatial compiler, now with membrane redistribution

The repository already contains the accepted production contract

`current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_PRODUCTION_THEORY_CONTRACT_20260812_2245.md`,

whose retained production identity is

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
U_COMPILER = N48-C1
C_COMPILER = N48-C1
T7_COMPILER = N48-C1
T_COMPILER = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

The reactivated production route keeps the same R10 physical source and the same zero-spatial formal identity, but inserts the already accepted five compatible membrane coordinates

\[
\boxed{r=[r_0,r_{20},r_{22},s_{02},s_{22}]}
\]

before the outer `(D,q)` root solve.

The five current-material internal equations remain

\[
R_{m,j}=0,
\qquad
K_{rr}=\partial R_m/\partial r,
\]

followed by consistent Schur condensation

\[
r_g=-K_{rr}^{-1}R_{m,g},
\]

\[
\bar P_g=P_g+P_r r_g,
\qquad
\bar R_{q,g}=R_{q,g}+R_{q,r}r_g,
\]

\[
\bar L=\bar P_D\bar R_{q,q}-\bar P_q\bar R_{q,D}.
\]

No new material mechanism, panel calibration, spatial quadrature, or post-hoc reinforcement capacity is introduced.

---

## 7. Anti-loop governance outcome

The next production gate is **not another integration-backend gate**. It is the actual structural calculation gate:

```text
UNIFIED_V1_CASE21_MEMBRANE_REDISTRIBUTED_N48_PRODUCTION_GATE
```

Required work in that gate:

1. load the frozen Case21 input and existing N48-C1/MM compiler policy;
2. build the five `Rm` targets from the same General-D15 coefficient field;
3. solve `Rm=0` for the five internal membrane coordinates at each `(D,q)` state;
4. Schur-condense to the outer two-variable system;
5. solve the connected `Rq=0, L=0` limit state;
6. run the same-state `KZ` audit;
7. report the new membrane-redistributed Case21 Pu and all intermediate coordinates/roots.

If that production calculation encounters a genuine structural/model error, report it directly. Do not reopen the exact-algebraic/Hermite backend automatically.

---

## 8. Gate verdict

```text
64_STATE_LOCAL_MATRIX_ERRATUM = ISSUED
CORRECT_LOCAL_MATRIX_OFFDIAGONALS = row_s: c1 ; row_qs: c1*Q
64_STATE_DIMENSION = RETAIN_64
64_STATE_SPARSITY_COUNT = RETAIN_159
DUAL_DENOMINATOR_GAUGE = PASS_EXACT_FOR_REGULAR_SIGNATURES
APPARENT_INTERIOR_POLE_x = 21/260
PHYSICAL_ATOM_REGULAR_AT_x = PASS
RATIONALIZED_BASIS_GLOBAL_REGULARITY = FAIL
EXACT_ALGEBRAIC_HOLONOMIC_PRODUCTION = PAUSED
N48_C1_MM_GENERAL_D15_PRODUCTION = REACTIVATED
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
FORMAL_THICKNESS_QUADRATURE = 0
NEW_Pu = NOT_RUN_IN_THIS_GATE
NEXT_GATE = UNIFIED_V1_CASE21_MEMBRANE_REDISTRIBUTED_N48_PRODUCTION_GATE
```
