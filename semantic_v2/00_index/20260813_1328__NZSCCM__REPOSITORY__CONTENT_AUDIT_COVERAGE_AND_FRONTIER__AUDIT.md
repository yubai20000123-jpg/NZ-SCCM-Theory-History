# NZ-SCCM repository content-audit coverage and frontier

**Timestamp:** 2026-08-13 13:28 +08:00  
**Purpose:** make the semantic reconstruction auditable; distinguish direct body-reading from registry/ledger classification and unresolved leaf content.

## 1. High-risk branches already direct-audited

The highest-risk ambiguity was not the literature/source archive; it was the legacy active workspace, because files under `current/` and files whose names contain `FRESH`, `CURRENT`, `PASS`, `PRODUCTION`, `CLOSURE`, `Rxx`, or `Vxx` could be mistaken for current production.

The following high-risk families have been body-read at file level for their governing/ambiguous artifacts:

```text
current/CURRENT_STATE.md
current/results/              primary/current vs old direct-N48 tables and candidate Case21 results
current/case21/               current inputs/coefficients vs old Aug-09 handoff/tail files
current/workflows/            current Case21 execution contract vs direct-N48/reproduction contracts
current/diagnostics/          Swartz24 source/mechanism diagnostic
current/audits/               compiler repair, general-D15 correction, reproduction, recovery, checkpoint/KZ audits
current/governance/           timestamp naming, root/closure/checkpoint governance
current/theory/               current production/theory chain plus principal obsolete analytical routes
root governance/              source/recovery/sync + major material/compiler/route decisions and revocations
```

Directly audited root-governance chronology includes at least:

- source-of-truth, recovery and sync protocols;
- effective source excerpt policy;
- explicit execution evidence rule;
- full-startup recovery/architecture checkpoint;
- material-native domain rules;
- energy-potential proposal and its later revocation/stop evidence;
- R07R explicit-surface route;
- root-cause pause;
- PF1 invariant/relevance/complexity controls;
- R09A/R09C;
- R10 material smoothing and intent audit;
- R10B representation/refreeze/direct-N48 decisions;
- N48 tangent failure -> C1 -> T constrained-minimax chronology;
- direct-N48 Case21 closure -> C1/MM candidate -> general-D15 correction -> final Case21 closure.

These are `A_DIRECT_CONTENT_AUDIT` and may be assigned semantic identities based on their bodies + later supersession.

## 2. Important content corrections found by direct reading

### 2.1 `current/` is not semantically current

Examples:

- `current/results/NZ_SCCM_SWARTZ24_FRESH_BLIND_THEORY_RESULTS_20260811.csv` = old direct-N48 24-panel roots/results, not current C1/MM + general-D15 roots.
- `current/case21/NEXTSTEP_EXECUTION_REPORT.md` = old Aug-09 tail/Chebyshev route.
- `current/theory/NZ_SCCM_EXPLICIT_SURFACE_SIMPLIFICATION_AND_CAPACITY_CHAIN_R07R_20260810.md` = panel/global D-q surrogate route now prohibited for production.

### 2.2 whole-file CURRENT/HISTORICAL labels are insufficient

`current/results/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_FULL_CLOSURE_20260812_1802.md` contains current root/KZ data **and** an obsolete experiment-identity comparison to 336 kN. It therefore requires section-level partial supersession.

### 2.3 older `CURRENT GOVERNANCE` can become historical

Examples:

- PF1 route locks self-declared CURRENT while PF1 was active, but current R10/N48-C1/MM production no longer uses PF1 as the production route.
- the energy-potential-first rule was later explicitly revoked as the wrong governing blocker/route test.
- the material-native Lambda_M/Lambda_R concept remains useful governance metadata but a later 22:31 correction explicitly revokes promoting it into an extra current runtime/root blocker.

Thus self-declared identity at creation time must be followed by later chronology.

## 3. B-level source/evidence coverage

The following content-derived indices were directly read:

- `evidence/catalog/SOURCE_REGISTRY.md`
- `evidence/catalog/MASTER_SOURCE_INVENTORY.csv`
- `history/ledgers/HISTORICAL_COMPONENT_LEDGER.md`
- `history/README.md`
- `history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md`

Therefore source/history leaf files can be placed in the semantic tree at `B_CONTENT_DERIVED_REGISTRY_OR_LEDGER` when the only claim is their stable repository role (source excerpt, source map, raw archive, historical artifact, recovery locator).

This **does not** authorize extracting a technical formula/number from a B-level leaf without opening the leaf/original source.

## 4. C-level direct-audit frontier

The remaining `C_NOT_YET_DIRECT_CONTENT_AUDITED` population is mainly low-risk companion material rather than ambiguous production identity:

### 4.1 companion result JSONs / coefficient JSONs

Examples:

```text
current/theory/*_results.json
current/theory/NZ_SCCM_R07R_EXPLICIT_GLOBAL_P_RQ_COEFFICIENTS.json
```

Their parent route/report has been body-read, so the route status is known. The companion numerical payload itself should still be opened before citing a number from it.

### 4.2 historical helper scripts whose parent route is already direct-audited

Examples include remaining `nz_sccm_m1*`, `nz_sccm_m1r*`, `nz_sccm_pf1*`, `nz_sccm_tensile*` helper scripts. Several representative helpers were directly opened; the rest remain C-level until code contents are individually inspected.

### 4.3 prompt-only workflow companions

Prompt files for old blind/recovery audits may remain C-level if their paired input/contract/audit body is already direct-read. They cannot acquire production status from their filenames.

### 4.4 source/history leaves

Most are B rather than C because their source/archive roles are established by registries/ledgers. They become A when a technical claim requires leaf-level inspection.

## 5. Physical migration frontier

A canonical semantic tree, naming policy, rename map, supersession map and primary locators now exist under `semantic_v2/`.

Physical moving/renaming of legacy source files is intentionally not yet performed because:

1. old internal links would break;
2. raw/historical provenance could be damaged;
3. a file may contain both retained and superseded sections;
4. Git history already provides chronology, so a clean canonical locator can be introduced first without destructive rewrite.

The next migration stage, if desired, is:

```text
A/B semantic classification sufficiently complete
-> create canonical locator for every important artifact
-> patch internal links to canonical IDs/locators
-> move stable legacy files in controlled batches
-> leave old-path locator stubs or preserve an unambiguous rename map
-> verify START_HERE + semantic manifests + source locators after every batch
```

No file should be moved merely because its old name contains `current`, `fresh`, `pass`, `production`, `Rxx`, or a date.

## 6. Current semantic-reconstruction status

```text
SEMANTIC_V2_TREE = ESTABLISHED
CANONICAL_NAMING_SYSTEM = ESTABLISHED
LEGACY_TO_CANONICAL_RENAME_MAP = ESTABLISHED
SUPERSESSION_MAP = ESTABLISHED
PRIMARY_CURRENT_LOCATORS = ESTABLISHED
HIGH_RISK_CURRENT_WORKSPACE_CONTENT_AUDIT = SUBSTANTIAL / ACTIVE
SOURCE_HISTORY_ROLE_COVERAGE = B_LEVEL_REGISTRY_LEDGER
DESTRUCTIVE_PHYSICAL_RENAME = NOT_STARTED
THEORY_CHANGED = NO
RESULT_CHANGED = NO
```

The remaining work is content completion and controlled migration, not another filename-based reorganization.
