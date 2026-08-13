# NZ-SCCM Aug11–13 execution-history recovery audit

**Timestamp:** 2026-08-13 12:49 +08:00  
**Identity:** HISTORY RECOVERY / EXECUTION ARTIFACT LOCATOR / NO THEORY CHANGE

## 0. Correction of the previous audit statement

The earlier statement that the Cases1–18 “calculation process is missing” was too broad and is corrected here.

The correct distinction is:

```text
ACTIVE_CURRENT_RESUMABLE_EXECUTION_ARTIFACT = INCOMPLETE
HISTORICAL_CALCULATION_PROCESS = PRESENT
HISTORICAL_BACKEND_STRATEGY = PRESENT
EXACT_FINAL_AUG12_13_TRANSIENT_TOOL_SOURCE = NOT YET LOCATED
CURRENT_CORRECTED_CASES1_18_ROOT_COORDINATES = NOT YET LOCATED
```

Thus “not retained in the active current package” must not be interpreted as “the historical process did not exist” or “all implementation evidence was lost.”

## 1. Git pre-clean recovery

The repository itself preserves `history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md`, which states that migration-era full-text mirrors, checkpoints, snapshots and migration metadata were intentionally removed from active `main` but remain recoverable from Git history.

Authoritative recovery commits:

- `5c83f82da95d42efa33cbf2192c95545ab009017` — last useful migration-era working tree before cleanup; includes old `sources_text/`, `checkpoints/`, `snapshots/` and pre-clean layout.
- `41fc94aea846f05ed98d7099703ec49c9356cf9e` — staging tree immediately before atomic reorganization.

The pre-clean tree contains historical executable artifacts such as old Case21 direct-analytic Python/Sage scripts. These are history evidence only and are not promoted to the current C1/MM + general-D15 production identity.

## 2. Current N48-C1/MM calculation process is explicitly archived

Git commit:

`1e459fb91abb187ffa78156c6412d6ef6aacdd84`

message:

`Add complete fresh Case21 N48-C1/MM calculation process`

The archived process file is:

`current/results/NZ_SCCM_CASE21_N48C1MM_D15_FRESH_FULL_CALCULATION_20260812.md`

It explicitly records the implementation strategy used in the successful fresh calculation:

1. finite analytic coefficient algebra;
2. FFT convolution may accelerate coefficient-sequence convolution but does not sample physical space;
3. floating coefficient convolution applies a `1e-5` noise-cleanup threshold solely to remove floating FFT noise;
4. finite power coefficients are formed in `u=sin X`, `v=sin Y`, `zeta` and then converted to the finite Chebyshev basis;
5. final spatial contraction is D15 exact analytic moments;
6. the same coefficient expression carries directional/forward automatic differentiation for `P_D`, `P_q`, `Rq_D`, `Rq_q`.

Therefore the backend implementation concept is not missing.

## 3. Recovered executable ancestor / backend lineage

File Library retains:

`global_one_halfwave_cheb_algebraic.py`

This Aug-09 executable ancestor contains:

- `from scipy.signal import fftconvolve`;
- a global multivariate coefficient object (`C3`);
- Laurent/Chebyshev convolution for coefficient multiplication;
- no spatial cells, no adaptive subdivision, no spatial collocation and no DCT;
- exact analytic moment integration;
- coefficient-space construction of concrete `Pc` and `Rq`.

Its own header correctly labels it only as a convergence-study candidate, so it is **not** the final Aug12/13 production executable. It is retained as source-code lineage explaining the successful coefficient-space/FFT architecture.

## 4. General-D15 correction chronology

Commit:

`e1828b2c193a0f08c6467177f979c2641d209c84`

records the Case21 tangent/general-D15 consistency audit. It shows that an earlier fresh branch had an incorrect `Qq` realization under the governing general-D15 definition, while the coefficient-space tangent implementation reproduced the exact unloaded tangent target. The later current Case21 result superseded that earlier fresh candidate.

Final current Case21 is frozen in `current/CURRENT_STATE.md` with:

- `D_u = 0.7822850963110681`
- `q_u = 0.0017707520964949533`
- `A_u = 2.160317557723843 mm`
- `Pc = 336.968777333 kN`
- `Ps = 28.611650232 kN`
- `Pu = 365.580427565 kN`
- `R_norm = 1.5607568553e-6`
- `|L_norm| = 4.0119433896e-6`
- Case21 same-branch KZ audit complete.

## 5. Swartz24 final execution evidence and retained current roots

The final current execution freeze explicitly states that Cases19,20,22,23,24 were continued through fresh `R10 -> N48-C1/MM -> current-map -> general-D15` equilibrium-limit calculations, with Case21 using the already frozen current closure.

Retained current root coordinates:

|Case|D_u|q_u|Pu / kN|
|---:|---:|---:|---:|
|19|0.895498262463|0.001490667301|356.402209|
|20|0.841997608509|0.001686144683|347.898637|
|21|0.782285096311|0.001770752096|365.580428|
|22|0.829956917853|0.001656490263|367.553168|
|23|0.925495201721|0.001295223916|375.917916|
|24|0.922369098591|0.001430121260|441.642463|

The same freeze contains 24/24 final current Pu values, including Cases1–18, but does not print current corrected `(D_u,q_u)` for Cases1–18.

## 6. Search for Cases1–18 current corrected roots

The following locations were searched:

- active Git `current/`, `governance/`, `history/`, `recovery/`;
- pre-clean recovery tree;
- Aug11–13 File Library files by exact final Pu values, final Case21 root, current 19–24 roots, `run_id`, `/mnt/data`, `fftconvolve`, `directional automatic differentiation`, `general-D15`, `N48-C1` and related terms;
- available personal prior-conversation retrieval for exact Aug12–13 tool execution.

Result:

```text
CASES1_18_CURRENT_Pu = PRESENT 18/18
CASES1_18_OLD_DIRECT_N48_ROOTS = PRESENT 18/18 (HISTORICAL ONLY)
CASES1_18_CURRENT_CORRECTED_Du_qu = NOT YET LOCATED
FINAL_AUG12_13_PYTHON_RUN_ID = NOT YET LOCATED
FINAL_AUG12_13_TRANSIENT_TOOL_CODE = NOT YET LOCATED
```

No old direct-N48 root is substituted for a current C1/MM + general-D15 root.

## 7. Why exact final tool code is not in the visible Git chronology

Comparison of the Git history across the final Case21 closure to the 24-panel Pu freeze shows reports/contracts/results being committed, but no corresponding final batch executable was committed in that interval. This is consistent with the final 24-panel computation having been executed in transient chat/Python runtime and only the results/report being committed.

This is an execution-archive failure, not evidence that the computation did not happen.

## 8. Original Conversation JSON status

File Library contains raw Conversation JSON exports from the earlier project history. These exports demonstrably preserve tool messages with fields such as:

- `author.role = tool`
- Python `execution_output`
- `aggregate_result.code`
- `run_id`
- exact final expression output.

However, the currently located raw exports terminate before the final Aug12–13 C1/MM + general-D15 Swartz24 continuation. No raw Aug12–13 conversation export containing the final batch tool call has yet been located in the accessible File Library.

Therefore the raw-JSON route is proven capable of recovering exact code, but the specific final execution export has not yet been found.

## 9. Current recovery verdict

```text
PRE_CLEAN_HISTORY_RECOVERY = PASS
HISTORICAL_N48C1MM_CALCULATION_PROCESS = RECOVERED
BACKEND_ALGORITHM_IDENTITY = RECOVERED
BACKEND_EXECUTABLE_LINEAGE = RECOVERED
FINAL_AUG12_13_EXACT_TRANSIENT_BACKEND_SOURCE = NOT_YET_LOCATED
CASES19_24_CURRENT_ROOTS = RECOVERED 6/6
CASES1_18_CURRENT_Pu = RECOVERED 18/18
CASES1_18_CURRENT_CORRECTED_ROOTS = NOT_YET_LOCATED
OLD_DIRECT_N48_ROOT_SUBSTITUTION = PROHIBITED / NOT USED
THEORY_CHANGED = NO
RECALCULATION_PERFORMED = NO
```

The next recovery target is not “invent a new solver”; it is exclusively to locate the final Aug12–13 transient execution record or an equivalent exact artifact carrying the current Cases1–18 `(D_u,q_u)` and the exact production source used to generate them.
