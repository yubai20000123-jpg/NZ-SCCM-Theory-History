# CURRENT ADDENDUM — SSUHPC terminal capacity-contact identity recovery

**Updated:** 2026-08-27 16:52 +08:00  
**Parent current state:** `current/SSUHPC_CURRENT_STATE_20260825.md`  
**Detailed audit:** `semantic_v2/40_execution/steel_shell/20260827_1648__NZSCCM__BH050_ORIGINAL_EXPLICIT_CAPACITY_CONTACT_RECOVERY_R01.md`  
**Status:** `RESTORE_20260825_CAPACITY_CONTACT / RETRACT_RECENT_COMMON_KAPPA_AND_CURRENT_MOMENT_DETOURS`

## Current authoritative interpretation

The 20260825 milestone architecture remains the parent:

```text
initial full-composite Airy/Galerkin resultant demand
-> common terminal capacity-state parameterization
-> UHPC exact N-M + R02/R06 steel faces + web
-> Nx/Mx/Ny/My demand-capacity contact
-> Pu
```

The terminal affine parameters `(A_x,B_x,A_y,B_y)` parameterize the terminal N-M capacity state. They are not required to equal the actual global q-derived deformation/curvature field.

Therefore the following recent interpretations are retracted from the current route:

```text
terminal Bx = global pi^2 q/b                 RETRACTED
terminal By = global pi^2 q/b                 RETRACTED
remove Mx/My contact equations                RETRACTED
current antinode moment -> global harmonic    RETRACTED
current-moment feedback into Airy P(q)        RETRACTED
R02 U=0 active-set extension as BH050 need    RETRACTED/NOT NEEDED
```

The global Airy equations remain unchanged, exactly as required by the 20260825 milestone:

```text
CURRENT_MATERIAL_IN_AIRY_COMPATIBILITY = NO
NONLINEAR_CURRENT_MATERIAL_GLOBAL_WORK_CLOSURE = RETRACTED
```

## BH050 status

Formal frozen qU-off common-R06 regression remains:

```text
Pu = 13.3563763545430 MN
q  = 0.004772819645833164
```

Restoring the exact qU GL terms inside the steel-face R02/R06 capacity operator while keeping the original five-equation terminal contact gives the current pre-certified blind root:

```text
q  = 0.004715120492577262
Pu = 13.29348446718 MN
```

The qU change is `-0.47088%` relative to the frozen common-R06 root.

The qU-on result is not yet promoted over the formal frozen R06 result solely because the combined GL+LL local-Mises maximum still needs its finite-algebraic candidate certificate. No spatial or thickness numerical quadrature is required.

## Comparator discipline

The accepted equal-contract BH050 FE peak `12.591227 MN` is post-check only. The pre-certified qU-on root is `+5.5774%` high. No coefficient or root was altered after this comparison.

Terminal `A/B/U/face mean stress` variables must not be compared to FE actual deformation/stress fields as if they were predictions of the same local physical state. The production claim of this reduced theory is resultant-capacity contact and Pu.

## Current flags

```text
AIRY_RESULTANT_DEMAND = RETAIN
TERMINAL_NM_CAPACITY_CONTACT = RETAIN
UHPC_EXACT_NM = RETAIN
WEB_EXACT = RETAIN
COMMON_R06 = RETAIN
qU_GL_LOCAL_STEEL = RETAIN_PRECERTIFIED
q_TO_TERMINAL_COMMON_KAPPA = NO
CURRENT_MOMENT_GLOBAL_FEEDBACK = NO
FULL_HALFWAVE_CURRENT_INTEGRAL = NO
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
CURRENT_FORMAL_BH050 = 13.3563763545430 MN
CURRENT_PRECERTIFIED_qU_BH050 = 13.29348446718 MN
NEXT_ONLY = GL+LL R06 finite-algebraic maximum certificate
```
