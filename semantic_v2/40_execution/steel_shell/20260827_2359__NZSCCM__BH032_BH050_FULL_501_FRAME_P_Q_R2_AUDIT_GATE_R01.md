# NZ-SCCM — BH032 / equal-contract BH050 full 501-frame P-q-R2 audit gate R01

**Date:** 2026-08-27  
**Parent diagnostic result:** `46502aafc90421e5ee41507d34d1d088b67bce2c`  
**Executor:** `20260827_2358__NZSCCM__BH_FEM_FULL_PATH_P_Q_R2_AUDIT_R03.py`  
**Status:** `PEAK RESULT REINTERPRETED / FULL-PATH EXTRACTOR FROZEN / LOCAL ODB EXECUTION REQUIRED / THEORY UNCHANGED`

## 1. Why this gate is required

The direct peak-frame U2 projections are valid, but one sentence in the first interpretation is corrected before any promotion to `main`:

```text
BH032 q_FE/q_Airy(P_FE) = 2.179456  -> +117.95%
BH050 q_FE/q_Airy(P_FE) = 1.166243  -> +16.62%
```

Both cases therefore have the **same sign** of path discrepancy:

\[
q_{FE}>q_{Airy}(P_{FE}).
\]

The discrepancy is not a common proportional bias; its magnitude is strongly case-dependent. The correct description is:

```text
SAME_DIRECTION = YES
COMMON_MAGNITUDE = NO
FROZEN_AIRY_PATH_STIFFNESS = SUSPECT
```

No theory term is changed at this node.

## 2. Direct peak residual in P(q) form

The frozen Airy path remains

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0).
\]

Using the measured peak modal amplitudes without fitting:

### BH032

\[
q_{FE}=0.003026484533,
\]

\[
P_{Airy}(q_{FE})=16.9289847512\;\mathrm{MN},
\]

versus

\[
P_{FE}=10.990480\;\mathrm{MN}.
\]

Thus the frozen Airy path requires about **54.03% more load** to reach the same projected dominant-mode amplitude at the FEM peak.

### BH050 equal-contract

\[
q_{FE}=0.004802111224,
\]

\[
P_{Airy}(q_{FE})=13.3880061552\;\mathrm{MN},
\]

versus

\[
P_{FE}=12.591227\;\mathrm{MN}.
\]

The same-q load bias is about **+6.33%**, close in magnitude to the current terminal theory-over-FEM Pu difference (~+6.08%). This is strong motivation to audit the entire P-q path before assigning the remaining BH050 Pu gap primarily to terminal capacity.

For BH032, terminal Pu agreement cannot by itself validate the internal path because the peak modal amplitude is more than twice the frozen terminal q. Error compensation remains a live hypothesis.

## 3. Unique next audit

Run every field frame, not only the peak:

\[
\boxed{P_{FE}(t),\;q_{FE}(t),\;R^2(t),\;NRMS(t)}
\]

and compare to the unchanged Airy path in both equivalent forms:

\[
q_{Airy}(P_{FE})
\]

and

\[
P_{Airy}(q_{FE}).
\]

Define

\[
e_P=\frac{P_{Airy}(q_{FE})}{P_{FE}}-1,
\qquad
e_q=\frac{q_{FE}}{q_{Airy}(P_{FE})}-1.
\]

A positive `e_P` means the frozen Airy relation is stiffer than the FEM dominant-mode path at that state.

## 4. R03 extraction contract

`20260827_2358__NZSCCM__BH_FEM_FULL_PATH_P_Q_R2_AUDIT_R03.py` inherits the accepted R02 mode projection exactly:

- FE X -> theory x;
- FE Z -> theory/loading y;
- FE Y -> out-of-plane;
- incremental mode field = U2;
- shell instance = `C-S-SHELL-1`;
- initial imperfection fixes modal sign;
- rigid terms `[1,X,Z]` are removed;
- top/bottom horizontal face nodes are paired and area weighted;
- ODB is opened `readOnly=True`.

It adds only two diagnostic operations:

1. project all available field frames;
2. recover a canonical axial reaction node-set automatically at the frozen peak frame by requiring its `|sum RF3|` to match the already accepted FEM peak load within 1% (default), then use that same node-set for all frames.

The selected reaction set and top 20 candidate sets are written to the summary for audit. If no node set passes the peak-reaction identity gate, the script stops rather than inventing a load path.

## 5. Onset reporting — no hidden single threshold

Because the exact mathematical instant of 'divergence' depends on numerical tolerance, R03 does not silently declare one arbitrary acceptance boundary. It reports a family of explicit sustained-onset markers over the pre-peak path:

- first positive `e_P` sustained for 10 frames after 5% of peak load;
- first `e_P >= 2%, 5%, 10%, 20%, 50%` sustained for 5 frames;
- first `e_q >= 2%, 5%, 10%, 20%, 50%` sustained for 5 frames;
- first `R2 <= 0.95, 0.90, 0.80, 0.70, 0.60` sustained for 5 frames;
- first `NRMS >= 0.05, 0.10, 0.20, 0.30` sustained for 5 frames.

These are **diagnostic markers**, not theory acceptance criteria or fit parameters.

This makes it possible to decide whether Airy-path stiffening precedes, coincides with, or follows loss of single-mode completeness.

## 6. Canonical local commands

BH032:

```bat
abaqus python 20260827_2358__NZSCCM__BH_FEM_FULL_PATH_P_Q_R2_AUDIT_R03.py ^
  "C:\03SCI\abaqus-UCFT test\UCFT_PARAMETRIC_CANONICAL_V1\artifacts\manual_review\BH_LT50_EXPLICIT_R02_GRID_PENALTY\BH_LT50_EXPLICIT_R02_GRID_PENALTY_DT2E6\BH032_EXPLICIT_R02_GRID_B400.odb" ^
  "BH032_FULL_PATH_AUDIT" ^
  1600 3200 2 0.0025 30.6035224490574 6977.19391202655 262 10.990480 ^
  --step EXPLICIT_LOADING --instance C-S-SHELL-1 --peak-time 2.6200008392334
```

BH050 equal-contract:

```bat
abaqus python 20260827_2358__NZSCCM__BH_FEM_FULL_PATH_P_Q_R2_AUDIT_R03.py ^
  "C:\03SCI\abaqus-UCFT test\UCFT_PARAMETRIC_CANONICAL_V1\artifacts\manual_review\BH050_EQUAL_CONTRACT_R02_GRID_PENALTY_DT2E6\BH050\BH050_EQUAL_CONTRACT_R02_GRID_B400.odb" ^
  "BH050_EQUAL_FULL_PATH_AUDIT" ^
  2500 5000 2 0.0025 19.5818772367311 10841.3718065234 212 12.591227 ^
  --step EXPLICIT_LOADING --instance C-S-SHELL-1 --peak-time 2.1200006
```

Each case writes:

```text
FEM_FULL_PATH_P_Q_R2.csv
FEM_FULL_PATH_P_Q_R2_SUMMARY.json
```

## 7. Required interpretation after local execution

The next decision must be based on the full pre-peak path:

1. At what load/frame does positive Airy same-q load bias become sustained?
2. At what load/frame does the single-mode `R2` begin to deteriorate materially?
3. Which event occurs first for BH032 and BH050?
4. Are the two cases qualitatively the same but quantitatively different, or do their mechanisms bifurcate?
5. Is the BH050 ~6% Pu gap already generated by P-q path stiffness before terminal contact?
6. Is the near-exact BH032 Pu instead an error compensation between an overly stiff P-q path and an early terminal contact?

Do not change Airy, R06, q0, Pcr, C, material parameters, terminal capacity coordinates, or root selection before those six questions are answered.

```text
MAIN_PROMOTION = HOLD
FULL_PATH_AUDIT = NEXT_ONLY
THEORY_CHANGE = NO
TERMINAL_CHANGE = NO
FEM_CALIBRATION = NO
```
