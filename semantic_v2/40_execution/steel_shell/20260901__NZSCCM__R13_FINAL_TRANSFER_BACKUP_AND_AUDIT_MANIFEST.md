# NZ-SCCM — R13 FINAL TRANSFER BACKUP AND AUDIT MANIFEST

**Date:** 2026-09-01  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged

## 1. Current standalone theory ledger

Path:

`semantic_v2/20_theory/20260901__NZSCCM__STEEL_SHELL_UHPC_CENTRAL_TECHNICAL_LEDGER_R13_FINAL_TRANSFER_AUDITED.md`

Current blob SHA:

`f49de1d66b3922950e23a5b444925824f5c79343`

Identity:

`STEEL_SHELL_UHPC_R13_FINAL_TRANSFER_AUDITED`

R13 changes no R12 mechanical equation. It is the final notation/definition/standalone-transfer hardening of the R12 capacity-contact theory.

## 2. Current audited parameter-driven workbook

Original binary filename:

`NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx`

Binary size:

`35526 bytes`

Expected SHA-256:

`fbad8ecdafc4f73f98a5b50a4120a58e3228fbca73f2bf92a9b637e558f59255`

Because the current GitHub connector writes UTF-8 text rather than arbitrary binary contents, the `.xlsx` is backed up **losslessly** as four Base64 text parts:

1. `semantic_v2/40_execution/steel_shell/backups/NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part01`
2. `semantic_v2/40_execution/steel_shell/backups/NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part02`
3. `semantic_v2/40_execution/steel_shell/backups/NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part03`
4. `semantic_v2/40_execution/steel_shell/backups/NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part04`

The Base64 parts are transport encoding only. They do not alter workbook contents.

### Linux/macOS reconstruction

Concatenate the four parts in numerical order, remove whitespace, decode Base64, then verify SHA-256:

```bash
cat \
  NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part01 \
  NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part02 \
  NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part03 \
  NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part04 \
| tr -d '\n\r\t ' \
| base64 -d \
> NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx

sha256sum NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx
```

The resulting hash must equal:

`fbad8ecdafc4f73f98a5b50a4120a58e3228fbca73f2bf92a9b637e558f59255`

### PowerShell reconstruction

```powershell
$parts = @(
  'NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part01',
  'NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part02',
  'NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part03',
  'NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx.b64.part04'
)
$b64 = (($parts | ForEach-Object { Get-Content $_ -Raw }) -join '') -replace '\s',''
[IO.File]::WriteAllBytes(
  'NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx',
  [Convert]::FromBase64String($b64)
)
Get-FileHash 'NZSCCM_钢壳UHPC_R13_最终转移审计_通用参数化_无试件预存_20260901.xlsx' -Algorithm SHA256
```

## 3. Workbook logical structure

The audited workbook contains:

```text
00_README
01_INPUT
02_GLOBAL
03_ENGINE
04_CONSTITUENTS
05_CLOSURE
06_OUTPUT
07_DEPENDENCY_AUDIT
08_R12_MATERIAL
09_INPUT_SCHEMA
10_TRANSFER_CONTRACT
11_FINAL_AUDIT
```

The workbook keeps the mechanical engine identity `R12` where appropriate because R13 changes documentation/notation/transfer definitions only, not the R12 mechanical equations.

## 4. Final no-lookup audit

The final workbook was scanned before backup:

```text
historical specimen names BH005/BH010/BH020/BH032/BH050/T360 = 0 matches
reference specimen parameter database = NONE
reference Pu table = NONE
specimen_id read by engine = NO
formula error scan (#REF/#DIV0/#VALUE/#NAME/#N/A) = 0 matches
one active physical input set = YES
```

The embedded calculation engine reads the current input/material/global cells, not a historical specimen/result table.

## 5. Final standalone-ledger audit

R13 was reviewed specifically for transfer to an unfamiliar AI. The following formerly plausible ambiguities are explicitly closed:

```text
units and resultant dimensions
coordinate and tension/compression signs
curvature sign and upper/lower face identities
meaning of global q and q0
meaning of integer longitudinal mode m
exact integer-mode selection without a fixed cutoff
complete input dictionary and gates
Aw and rho_w physical meaning
distinction between initial A/D and nonlinear current section operators
explicit upper/lower steel-face centroid strains
independent generalized kappa_x,kappa_y versus separate not-frozen geometric q-curvature research
R02 tension-positive sign conversion
R02 cubic active-set/root-selection rule
local harmonic indices separated from global q
local Airy coefficients separated from global A11/A12 notation
complete generic 2D R06 local stress field
interior/edge/corner Mises candidate definition
R04/R06 mechanical gate
R06 radial projection notation and historical eta mapping
UHPC sixth-degree compression definition and primitives
Hiew cubic-Hermite tension generation and primitives
explicit scalar-by-direction UHPC current-operator identity
explicit statement that nu_c is used in initial A/D, not reinserted as nonlinear Poisson coupling
exact continuous-thickness UHPC resultants
exact web yield-crossing integration
total N/M assembly
axial compression-contact orientation and elimination
admissibility and smallest-positive-q selection
failure/out-of-scope terminal statuses
formal all-root theory versus practical numerical evaluator distinction
required implementation/audit outputs
```

Conclusion at the **formula/parameter-definition level**:

`STANDALONE_TRANSFER_DOCUMENTATION_GATE = PASS`

A new AI given only the R13 ledger and one complete parameter set has enough information to implement the current theory step by step without consulting historical markdown files.

## 6. Remaining theory/execution boundaries — not documentation gaps

The following must remain visible and must not be misrepresented as solved by documentation:

1. The current production terminal closes the first admissible **axial y-direction UHPC compression contact**. If UHPC tensile limit or a non-axial compression terminal controls first, R13 returns an explicit failure/out-of-scope status rather than inventing another terminal.
2. The nonlinear UHPC section operator is **scalar by direction**. R13 does not claim a frozen full nonlinear 2D/multiaxial UHPC constitutive surface.
3. The formal R06 definition is exhaustive finite algebraic interior/edge/corner enumeration. The current Excel is a practical numerical evaluator of the exact equations; its generic interior stationary equations and final section closure use numerical root solvers. This is not a stress/Pu surrogate and does not change the formal theory, but it is not itself a theorem-level proof that deterministic numerical starts exhaust every pathological parameter set.
4. Therefore, if an unfamiliar AI is asked for theorem-level exhaustive formal implementation, it must follow the R13 resultant/all-root definitions rather than copy the practical numerical-start strategy as the mathematical definition.

## 7. Current lock

```text
CURRENT_TRANSFER_LEDGER = R13_FINAL_TRANSFER_AUDITED
CURRENT_EXECUTABLE_REFERENCE = R13-audited R12 parametric workbook
HISTORICAL_MARKDOWN_RUNTIME_DEPENDENCY = NONE
REFERENCE_SPECIMEN_OR_PU_LOOKUP = NONE
PRODUCTION_MAIN_MODIFIED = NO
```
