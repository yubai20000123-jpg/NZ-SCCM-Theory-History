# NC material semantic branch

## Current material target

- R10 physical current material target remains **CURRENT_SUPPORT / FROZEN**.
- R10 material physics is not reopened.
- The previous Z6-wide single `N48-C1/MM` representation is **not valid for Z0–Z5 AR2 production** after the 2026-08-16 stocky-panel fidelity audit.

## Current Z0–Z5 material representation candidate

Source-only fidelity gate passed for:

`R10-MR-C1(256,1024,1280,512)`

with

```text
guard material interval = [-1.50,+0.35]
operational fidelity core = [-1.40,+0.30]
U degree=256
C degree=1024
T degree=1280
T7 degree=512
```

Each primitive remains one global finite Chebyshev polynomial. `MR` means different finite polynomial orders for different source primitives; it does **not** mean material zones, spatial cells, piecewise structural integration, or material-point states.

Exact R10 C1 anchors at `lambda=0` are retained. On the operational core, the unchanged R10 current master reconstructed from the multirate primitives has approximately

```text
max spectral stress-scalar error = 4.22e-4
max tangent error / source peak tangent = 2.82%
```

The rejected Z6-wide N48 representation on the same core was approximately

```text
max spectral stress-scalar error = .7185
max tangent error / source peak tangent = 81.5%
```

Current artifact:

- `20260816_1110__NZSCCM__NC_MATERIAL__R10_MULTIRATE_C1_SOURCE_FIDELITY__THEORY.md`

## Production-status boundary

```text
R10_MR_C1_SOURCE_FIDELITY = PASS
CAYLEY_HAMILTON_FORMAL_COMPATIBILITY = PASS
GENERAL_D15_FORMAL_COMPATIBILITY = PASS
VARIABLE_ORDER_STRUCTURAL_D15_BACKEND = NOT_YET_EXECUTED
NEW_Z0_Z5_Pu = NOT_CALCULATED
```

The existing structural execution code assumes N48-style fixed recurrence, so the new material compiler is **not yet a released Z0–Z5 production structural backend**.

Unique next compiler/structure gate:

`Z0_Z5_AR2_MULTIRATE_R10_TO_VARIABLE_ORDER_MOMENT_FIRST_D15_RECOMPILE_GATE`

The blind structural solution must also re-certify that the continuous reachable principal spectrum stays inside `[-1.40,+0.30]`; otherwise the material guard/core must be rebuilt before a Pu is accepted.

## Historical compiler-fidelity review

- `20260813_1719__NZSCCM__NC_MATERIAL__VALUE_TANGENT_BALANCED_MINIMAX_AND_REACHABLE_SPECTRUM__COMPILER_AUDIT.md`

That audit introduced a source-only balanced-minimax candidate and the non-calibrating reachable-spectrum self-consistency concept. It remains historical support for the present fidelity governance; it is not itself the current Z0–Z5 production compiler.

Older direct-N48, global-energy, rational/PF1 and other compiler routes remain semantic history/rejected branches and do not become current merely because files remain in the repository.