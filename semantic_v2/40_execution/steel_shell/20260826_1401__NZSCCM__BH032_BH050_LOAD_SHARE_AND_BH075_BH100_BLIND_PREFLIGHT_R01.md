# NZ-SCCM — BH032/BH050 load-share + BH075/BH100 blind preflight R01

**Date:** 2026-08-26  
**Scope:** additive execution evidence only; no theory change; no FEM/comparator in root selection.

## 1. Load-share check

The user/Codex equal-contract section extraction gives, at FEM peak:

| Case/source | UHPC | steel total | web |
|---|---:|---:|---:|
| BH032 FEM | 66.49% | 28.95% | 4.56% |
| BH032 R06 theory | 64.24% | 31.45% | 4.31% |
| BH050 equal-contract FEM | 55.80% | 40.61% | 3.58% |
| BH050 R06 theory | 73.49% | 23.19% | 3.33% |

Absolute BH050 equal-contract FEM section resultants are approximately:

```text
Ny_UHPC  = -2947.266 N/mm
Ny_steel = -2144.846 N/mm
Ny_web   =  -189.296 N/mm
Ny_total = -5281.408 N/mm
```

Frozen BH050 R06 theory:

```text
Ny_UHPC  = -3775.209 N/mm
Ny_steel = -1191.196 N/mm
Ny_web   =  -170.905 N/mm
Ny_total = -5137.309 N/mm
```

Interpretation remains limited: BH032 internal sharing is close; BH050 equal-contract has substantially more steel share and less UHPC share than theory, while web share is close. This observation does not reopen R06 or create a new mechanism.

## 2. Geometry-label correction before BH075/BH100 theory

The historical parameter registry uses `H=50 mm` as total sandwich depth. The current frozen BH theory uses:

```text
H_total = 50 mm
ts = 4 mm per external face
tc = 42 mm UHPC core
web net height = 37 mm
Aw = 9*4*37 = 1332 mm^2
```

Therefore the recent preparation table entry `tc=50 mm` is treated as a label error for `H=50 mm`; current theory must retain `tc=42 mm` unless a new geometry contract is explicitly authorized.

## 3. Canonical theory source recovered

The GitHub repository contains the current common R06 operator and exact control executions, so the previous local-workspace status `BLOCKED_BY_MISSING_R06_RUNNER` is not a theory-data absence.

Canonical sources:

```text
semantic_v2/40_execution/steel_shell/20260825_1535__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE.py
semantic_v2/40_execution/steel_shell/20260825_1550__NZSCCM__STEEL_SHELL_COMMON_R06_Z6_NONREGRESSION_T360_BH032_BLIND_EXECUTION_R01.md
semantic_v2/40_execution/steel_shell/20260825_1622__NZSCCM__STEEL_SHELL_COMMON_R06_SSUHPC_7CASE_BH050_FULL_EXECUTION_R01.md
```

The reconstructed blind evaluator reproduces the frozen BH050 R06 root before higher-case use.

## 4. Higher-slenderness blind structural/local preflight

Using the unchanged BH family geometry rules `a=2b`, `Lx=0.225b`, `Ly=a/9`, `A0=Lx/1600`, `tc=42`, `ts=4`, `Aw=1332`:

| Case | b mm | a mm | Lx mm | Ly mm | Lx/ts | m* | Pcr MN | sigma_cr,s MPa | sigma_cr/fy | R06 branch |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| BH075 | 3750 | 7500 | 843.75 | 833.3333 | 210.9375 | 2 | 13.05285559 | 44.64429666 | 0.1257586 | LOCAL_BUCKLING_FIRST |
| BH100 | 5000 | 10000 | 1125.0 | 1111.1111 | 281.25 | 2 | 9.78899323 | 25.11241687 | 0.0707392 | LOCAL_BUCKLING_FIRST |

## 5. Blind terminal-root status

The unchanged current five-equation SSUHPC terminal family was checked without reading any BH075/BH100 FEM peak. The four candidate first-UHPC-compression-face contacts (`x+`, `x-`, `y+`, `y-`) were tested. No admissible exact terminal root was found for BH075 or BH100 within the frozen rising-compression material domain.

The BH050-connected `eps_y(-tc/2)=-0.0035` branch continues exactly through intermediate widths but ceases to close by BH075. Representative continuation values are:

```text
b=2500: Pu=13.35637635 MN  (BH050 exact root)
b=3000: Pu=13.94315679 MN
b=3500: Pu=14.76496126 MN
b=3600: Pu=14.69798452 MN
b=3700: Pu=14.52535518 MN
b=3725: Pu=14.49089100 MN
b=3750: no exact admissible root on this branch
```

This is not promoted to a new instability criterion and is not `det Jsec=0`.

Frozen blind status:

```text
BH075_BLIND_THEORY = NO_ADMISSIBLE_TERMINAL_ROOT_IN_CURRENT_FROZEN_COMPRESSION_CONTACT_FAMILY
BH100_BLIND_THEORY = NO_ADMISSIBLE_TERMINAL_ROOT_IN_CURRENT_FROZEN_COMPRESSION_CONTACT_FAMILY
Pu_theory = NOT_INVENTED
R06_CHANGED = NO
MARGUERRE_AIRY_CHANGED = NO
COMPARATOR_IN_ROOT_SELECTION = 0
```

## 6. Execution consequence

If higher-slenderness validation is continued, the no-root status itself is the blind theory result. Equal-contract BH075/BH100 FEM models may then be prepared without using FEM to select or create a theoretical root. Their FEM peaks would test the scope boundary of the current frozen terminal theory, not calibrate it.
