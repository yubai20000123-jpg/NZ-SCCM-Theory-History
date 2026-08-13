# NZ-SCCM Swartz24 current checkpoint recovery — Case21 regression fail-fast record

**Timestamp:** 2026-08-13 12:21 +08:00  
**Identity:** CURRENT EXECUTION FAILURE RECORD / NO ALTERNATIVE BRANCH

## 0. Authorized task

Recover the missing current resumable checkpoints for Swartz Cases 1–18 while simultaneously repairing the execution-backup gap. The governing production chain remains:

`R10 -> N48-C1/MM -> Cayley-Hamilton -> Nguyen second-order complete halfwave -> general-D15 exact moments -> P(D,q), Rq(D,q), L(D,q)`.

User execution rule for this run: if the requested calculation fails, stop immediately and do not open an alternative theoretical/computational branch.

## 1. What was successfully recovered before the structural regression

The current R10 material formulas and N48-C1 constraints were reimplemented directly from the governing contracts.

For Case21, the following material quantities were reproduced:

- kappa = 2.0005129533678754
- xcr = 0.04998717945397425
- eta = 0.0024993589726987125
- Wsrc = 0.031741235181249175
- h = 0.09799750427197018

The Case21 U/C/T7 N48-C1 coefficient arrays reproduced the saved current coefficient file to numerical precision. The T constrained-minimax solve on the final Case21 compiler interval [-1.15, 0.12] also converged to the saved current T-MM coefficient set within small LP/tie-breaking numerical differences.

Thus the recovery reached the structural current-map / exact-moment backend with the current material compiler identified consistently.

## 2. Required first regression and failure

Before running Cases1–18, the recovered structural backend was required to reproduce the frozen current Case21 state at

- D = 0.7822850963110681
- q = 0.0017707520964949533
- expected Pc = 336.968777333 kN
- expected Ps = 28.611650232 kN
- expected Pu = 365.580427565 kN
- expected Rq approximately zero within the frozen engineering residual gate.

The attempted coefficient-space implementation used the same finite Cayley-Hamilton recurrence and analytic invariant-ring moments, with no physical-space Gauss/Simpson/collocation/material-point grid. However, the floating dense polynomial-convolution realization suffered catastrophic coefficient cancellation/conditioning in the high-order structural composition. At the frozen Case21 point it returned an absurd concrete force of order -1.86e16 kN and generalized residual of order 8.97e17 kN mm instead of the frozen Case21 values.

Therefore the recovered implementation does **not** pass the mandatory Case21 production regression and is not a valid current executable.

## 3. Fail-fast disposition

```text
CASE21_MATERIAL_COMPILER_RECOVERY = PASS
CASE21_STRUCTURAL_PRODUCTION_REGRESSION = FAIL
FAILURE_LAYER = CURRENT_MAP / HIGH_ORDER_COEFFICIENT_CONVOLUTION NUMERICAL CONDITIONING
CASES1_18_CURRENT_ROOT_REGENERATION = NOT RUN
CASES1_18_CHECKPOINTS = NOT FABRICATED
SWARTZ24_CURRENT_RESUMABLE_CHECKPOINT = STILL INCOMPLETE
ALTERNATIVE_BRANCH_STARTED = NO
THEORY_CHANGED = NO
R10_CHANGED = NO
N48_ORDER_CHANGED = NO
SPATIAL_QUADRATURE_INTRODUCED = NO
STRUCTURAL_CALIBRATION = NO
```

This run stops here in accordance with the user fail-fast instruction. No old direct-N48 roots are substituted, no experimental Pu/Pf is used to reconstruct roots, and no alternative solver/backend is attempted in this execution.

## 4. Backup consequence

The existing checkpoint-governance file remains valid: a future successful recovery must first pass the frozen Case21 regression and then persist the production executable/version/hash together with each panel's `(D_u,q_u,A_u)`, `Pc/Ps/Pu`, equilibrium residuals, `P_D,P_q,Rq_D,Rq_q,L,L_norm`, material-domain/steel certificates and execution identity before any panel is marked calculation-complete.
