# Gate lock — Case21 N48 membrane connected continuation

**2026-08-16 22:34 +08:00**

The anti-loop N48 production pivot is retained. The following subgate is now closed:

```text
CASE21_N48_MEMBRANE_BASELINE_FINGERPRINT_AND_CONNECTED_START_GATE = PASS
```

Locked facts:

1. The current 18:02 N48-C1/MM coefficient-space evaluator reproduces the frozen r=0 Case21 load fingerprint to sub-micro-kN difference and the concrete generalized-work component to about 1e-6 relative scale.
2. Five-term membrane equilibrium must be introduced by continuation from the origin-connected branch; direct insertion at the old r=0 limit state is not an admissible start strategy.
3. The first accepted nonzero connected state is frozen at `q=1e-4`, `D=0.016046306`, with the five `r` values recorded in the paired JSON artifact.
4. At that state, `||Rm||2=6.9022384258e-6`, `Rq=1.9082556149e-6 kN mm`, and the continuous material eigenvalue enclosure lies safely inside `[-1.15,0.12]`.
5. N=20 may be used only as a continuation predictor acceleration after parity checks; N=28 remains the acceptance corrector identity. This does not alter the N48 material compiler order.
6. FFT may accelerate coefficient-index convolution only. Formal structural spatial sampling/quadrature remains zero.

The unique next gate is

```text
CASE21_N48_MEMBRANE_CONNECTED_BRANCH_CONTINUATION_AND_SCHUR_GATE
```

Execution rule:

```text
start from accepted q=1e-4 connected state
-> advance q monotonically with predictor/corrector
-> at every accepted point close all five Rm and total Rq
-> retain N28 corrector
-> store r, Rm, Rq, P, Krr/condition, compiler-domain certificate
-> build same-state Schur derivatives as limit region is approached
-> locate first connected limit candidate
-> run same-state KZ
-> only then release new membrane-redistributed Pu
```

Forbidden next actions:

```text
jump back to old r=0 limit and solve Rm there as an isolated root
select a disconnected root cloud by largest load
use experiment to initialize/select continuation
reopen exact-algebraic/holonomic integration backend
introduce spatial quadrature/collocation/material grids
release new Pu before Schur + KZ gates close
```
