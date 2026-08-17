# NZ-SCCM — Z1/Z4 phase assembly + nonuniform steel-yield tangent audit

**Timestamp:** 2026-08-17 22:04 +08:00  
**Identity:** CURRENT HARD-GATE AUDIT / NO NEW Pu CLAIM / ZERO-SPATIAL PRODUCTION GOVERNANCE RETAINED

## 0. Audit questions

This execution addresses exactly two hard questions:

1. Does the current evaluator demonstrably satisfy, at the same `(D,q,alpha)`,

\[
R_q^{tot}=R_q^c+R_q^{face}+R_q^w,
\]

\[
R_A^{\Delta,tot}=R_A^{\Delta,c}+R_A^{\Delta,face}+R_A^{\Delta,w},
\]

and

\[
\mathbf J^{tot}=\mathbf J^c+\mathbf J^{face}+\mathbf J^w?
\]

2. Does local steel yielding retain the correct local/full directional consistent tangent, rather than turning `max sigma_vm > fy` into a whole-shell tangent deletion?

No Zhou/Winter load is used in either audit.

---

## 1. Governing evidence recovered before calculation

The current unified workflow requires every phase to return analytic `P`, `Rq`, and consistent derivatives before the coupled solve; tangent/stability must use the same current state. The 2026-08-17 canonical end-to-end lock additionally requires the full directional consistent tangent from the same material operator.

A particularly important historical file was re-opened:

`20260815_0126__NZSCCM__Z6__LOCAL_IDEAL_EP_PROGRESSIVE_YIELD__PREFLIGHT_AUDIT.md`.

It explicitly documented the old reduced whole-shell rule

\[
\alpha_g=\min\left(1,\frac{f_y}{\max_{\Omega_s}\sigma_{VM}^E}\right),
\qquad
\sigma_s^{red}=\alpha_g\sigma_s^E,
\]

and rejected it as a physical progressive-yield operator because first local yield caused a global derivative/resultant change.

That same file prescribed the zero-spatial replacement architecture:

```text
finite analytic elastic invariant field
-> local ideal-EP projection compiler
-> finite analytic coefficient composition
-> General-D15 exact moments
```

with no structural point grid.

Later Z6 files describe `steel-cap coefficient nodes` as material-coordinate coefficient-generation objects and, by 2026-08-17, describe the steel phase as an `ideal elastic-perfectly-plastic local radial cap`. Therefore the stress-level intent has clearly moved away from the old specimen-wide multiplier.

However, the latest Z1/Z4 execution reports persist only total `Rq`, total `RA_delta`, phase loads and `max trial VM/fy`; they do not persist phase residuals or phase Jacobian blocks. They also do not persist the exact shell tangent target stream used in D15.

---

## 2. Frozen Z1/Z4 states used for this audit

No new root is selected. The currently frozen states are audited as-is.

| state | D | q | alpha | b mm | tc mm | ts mm | fy MPa | report max trial VM/fy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Z1 OFF | 0.5939452076 | 0.003204740061 | 0 | 6000 | 92 | 4 | 235 | 1.17963 |
| Z1 ON | 0.5820414604 | 0.004873166767 | 0.1317481353 | 6000 | 92 | 4 | 235 | 1.19533 |
| Z4 OFF | 0.9065170837 | 0.001300622089 | 0 | 8000 | 192 | 4 | 355 | 1.04911 |
| Z4 ON | 0.9177226716 | 0.001403182997 | 0.004739862166 | 8000 | 192 | 4 | 355 | 1.06578 |

Common steel constants in the execution reports:

```text
Es = 206000 MPa
nu_s = 0.30
```

Reference kinematic constants:

```text
eps0 = 0.0018712490394580678
nu_ref = 0.18
ell = b for the representative halfwave
```

---

## 3. Closed-form local point audit — no spatial integration

To test the constitutive/tangent identity without introducing any structural quadrature, evaluate the existing analytic field at one mechanics-defined point only:

\[
X=Y=\pi/2
\]

and at the centroid of the more highly compressed faceplate,

\[
z=-(t_c/2+t_s/2).
\]

This is a local current-map evaluation, **not** a numerical integration rule and not a production load calculation.

At the halfwave center,

\[
B_A^x=(1-2\nu_{ref})/4,
\qquad
B_A^y=(2-\nu_{ref})/4,
\]

and the square-halfwave bending contribution is

\[
z\pi^2 A/b^2=z\pi^2 q/b.
\]

The steel trial stress uses the exact plane-stress elastic matrix

\[
\mathbf C_e=\frac{E_s}{1-\nu_s^2}
\begin{bmatrix}
1&\nu_s&0\\
\nu_s&1&0\\
0&0&(1-\nu_s)/2
\end{bmatrix}.
\]

The local radial projection and its analytic tangent are those locked in

`20260817_2204__NZSCCM__LOCAL_RADIAL_CAP_FULL_DIRECTIONAL_TANGENT_AND_PHASE_ASSEMBLY__CORRECTION_LOCK.md`.

### 3.1 Reconstructed local states

| state | z mm | eps_x | eps_y | trial sx MPa | trial sy MPa | trial VM MPa | VM/fy | lambda_loc | returned sx MPa | returned sy MPa | Ct rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Z1 OFF | -48 | -5.2980641e-5 | -1.3644555e-3 | -104.65644 | -312.47477 | 275.48313 | 1.172269 | 0.8530468 | -89.27684 | -266.55560 | 2 |
| Z1 ON | -48 | -1.4927844e-4 | -1.3617416e-3 | -126.27142 | -318.40019 | 277.70183 | 1.181710 | 0.8462314 | -106.85483 | -269.44022 | 2 |
| Z4 OFF | -98 | 1.4808880e-4 | -1.8535679e-3 | -92.35627 | -409.54186 | 372.06244 | 1.048063 | 0.9541409 | -88.12089 | -390.76065 | 2 |
| Z4 ON | -98 | 1.4088235e-4 | -1.8829006e-3 | -95.97966 | -416.67143 | 377.93543 | 1.064607 | 0.9393139 | -90.15503 | -391.38526 | 2 |

These local center values are not asserted to be the exact spatial maxima; they are intentionally a closed-form mechanics point. Their `VM/fy` values are nevertheless close to the separately reported global maxima and independently confirm that the compressed face is in the active cap regime at all four audited limit states.

### 3.2 Full directional tangent is not zero

Singular values of the exact active-cap `3x3` tangent at the same point are:

```text
Z1 OFF: [1.89825160e5, 6.75875528e4, 6.94e-12] MPa
Z1 ON : [1.80421142e5, 6.70475616e4, 2.61e-12] MPa
Z4 OFF: [2.27328393e5, 7.55973189e4, 2.62e-11] MPa
Z4 ON : [2.23174502e5, 7.44225624e4, 5.01e-11] MPa
```

Thus every active local tangent has numerical rank two: one radial loading direction loses tangent, while two independent directional stiffnesses remain finite.

This directly rejects the interpretation

```text
local yield anywhere -> C_t^steel = zero matrix everywhere
```

for the stated local radial-cap current map.

A material-local centered finite-difference derivative check of the returned-stress map, used only as an independent derivative oracle, gives relative matrix errors of approximately `2.2e-11` to `2.5e-11` for the four states. The production tangent remains the analytic derivative; the finite difference is not used in any structural integral or root.

---

## 4. Nonuniform-yield diagnosis

The current reports already give `max trial VM/fy > 1` for all four states. The closed-form center audit proves that one faceplate is actively capped while the opposite faceplate center remains elastic:

```text
Z1 OFF opposite-face center VM/fy ~= 0.8068
Z1 ON  opposite-face center VM/fy ~= 0.7083
Z4 OFF opposite-face center VM/fy ~= 0.8932
Z4 ON  opposite-face center VM/fy ~= 0.8980
```

Therefore, without any spatial numerical integration, the analytic field itself already proves

\[
\boxed{\text{steel yielding is nonuniform through the two faceplates}.}
\]

The earlier conversation-level dense-field scan estimated wider trial-over-yield area fractions. Those percentages are retained only as `AUDIT_ONLY_SPATIAL_ORACLE` evidence and are **not** used in this formal audit, root selection, phase resultant or D15 target:

```text
Z1 OFF total two-face trial-over-yield ~32.35%
Z1 ON  total two-face trial-over-yield ~38.03%
Z4 OFF total two-face trial-over-yield ~17.84%
Z4 ON  total two-face trial-over-yield ~26.16%
```

The production theory does not adopt these area percentages and does not create elastic/plastic cells from them.

---

## 5. Gate 1 — phase assembly result

### 5.1 Formal/theory level

PASS.

At a common state, exact continuum integration and differentiation are linear over material phases, so

\[
R_q^{tot}=R_q^c+R_q^{face}+R_q^w,
\]

\[
R_A^{\Delta,tot}=R_A^{\Delta,c}+R_A^{\Delta,face}+R_A^{\Delta,w},
\]

\[
\mathbf J^{tot}=\mathbf J^c+\mathbf J^{face}+\mathbf J^w
\]

are mandatory identities of the current theory.

### 5.2 Existing persisted Z1/Z4 execution evidence

INCOMPLETE.

The latest Z1/Z4 reports state that all phases enter before solve and persist phase loads, but they do **not** persist:

```text
Rq_c, Rq_face, Rq_w
RA_c, RA_face, RA_w
J_c, J_face, J_w
```

at the final states.

During this audit, no persisted production evaluator source or exact per-phase D15 target dump sufficient to reconstruct those missing quantities was found in the opened current GitHub artifacts. Therefore a numerical phase-assembly certificate cannot be fabricated from the existing reports.

Verdict:

```text
PHASE_ASSEMBLY_THEORY = PASS
PHASE_ASSEMBLY_REPORT_CLAIM = PRESENT
PHASE_ASSEMBLY_MACHINE_NUMERIC_CERTIFICATE = BLOCKED_BY_MISSING_PERSISTED_PHASE_TARGETS
```

---

## 6. Gate 2 — local yield / same-source consistent tangent result

### 6.1 Stress-map locality

PASS at the governing-formulation level.

The 2026-08-15 preflight explicitly rejected the earlier whole-shell cap and required local progressive yielding. Later files use local steel-cap coefficient generation / local radial cap language.

### 6.2 Analytic local tangent

PASS.

For the stated local radial-cap map, the exact derivative is now closed and independently checked. Active local points have rank-two directional tangents, not a zero matrix.

### 6.3 Exact-D15 structural tangent/resultant certificate

PENDING.

The currently opened Z1/Z4 reports do not persist enough coefficient-space data to give auditable numerical values for

\[
K_{Z,s}^{mat},\quad R_{q,s},\quad R_{A,s}^{\Delta},\quad \mathbf J_s
\]

from the same local stress/tangent analytic series.

No Gauss, Simpson, adaptive quadrature or structural material-point integration is introduced to fill this gap.

Verdict:

```text
LOCAL_NONUNIFORM_YIELD = CONFIRMED
WHOLE_PHASE_ZERO_TANGENT = REJECTED
LOCAL_RADIAL_CAP_ANALYTIC_TANGENT = PASS
EXACT_D15_STEEL_TANGENT_TARGETS_Z1_Z4 = NOT YET PERSISTED / PENDING
```

---

## 7. Required next executable action

Do **not** rerun the whole Z0-Z5 batch and do not change material parameters.

Recover or rebuild the same current exact-moment evaluator under the canonical chain, adding only a phase-return/audit interface. For each of Z1 OFF, Z1 ON, Z4 OFF and Z4 ON, evaluate from its own frozen/raw state and persist:

```text
P_c, P_face, P_w
Rq_c, Rq_face, Rq_w
RADelta_c, RADelta_face, RADelta_w
J_c, J_face, J_w
KZmat_c, KZmat_face, KZmat_w
KZgeo_c, KZgeo_face, KZgeo_w
steel stress-series convergence record
steel tangent-series convergence record
```

The formal steel path must remain:

```text
local finite current cap
-> analytic material-coordinate series
-> exact continuous halfwave composition
-> General-D15 exact moments
-> phase targets
```

No spatial quadrature/cells may be substituted merely to obtain the missing numbers.

Only after the exact phase/tangent certificate passes should Z1 and Z4 be independently re-solved from the origin and their current membrane increments reinterpreted.

---

## 8. Current project decision from this audit

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0

GATE1_PHASE_ASSEMBLY_THEORY = PASS
GATE1_MACHINE_CERTIFICATE = BLOCKED/PENDING
GATE2_LOCAL_YIELD = PASS
GATE2_FULL_DIRECTIONAL_LOCAL_TANGENT = PASS FOR CURRENT RADIAL-CAP MAP
GATE2_EXACT_D15_STRUCTURAL_TANGENT_CERTIFICATE = PENDING
Z1_Z4_CURRENT_Pu_STATUS = DIAGNOSTIC / NOT YET PRODUCTION-CERTIFIED
NEW_Pu_CLAIM = NONE
CALIBRATION = NONE
```
