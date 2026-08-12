# Case21 experimental comparison source — experiment only

**Date:** 2026-08-12  
**Identity:** EXPERIMENT-ONLY EVIDENCE / READ ONLY AFTER FRESH THEORY RESULT WAS FROZEN

## Isolation rule

This file was created only after the fresh NC-R1 theory calculation had already frozen its theoretical root and theoretical load. It contains no historical NZ-SCCM calculation, no FE prediction, no prior Case21 root, and no analytical prediction from Swartz/Attard/Nguyen.

```text
THEORY_RESULT_FROZEN_BEFORE_EXPERIMENT_READ = YES
HISTORICAL_CASE21_THEORY_RESULT_IMPORTED = NO
HISTORICAL_FE_GAUSS_RESULT_IMPORTED = NO
EXPERIMENT_USED_FOR_ROOT_SELECTION = NO
EXPERIMENT_USED_FOR_PARAMETER_TUNING = NO
```

## Primary source location

Source read directly from the uploaded Nguyen thesis PDF (`Nguyen-011325526.pdf`), Chapter 5, Section 5.2, printed page 143, table titled **“Experimental and FE Buckling Loads”**.

Only the experimental entry required for the final blind comparison is transcribed here.

For **Case 21**:

\[
\boxed{P_{u,\mathrm{exp}}=336\ \mathrm{kN}}
\]

The same row identifies the panel slenderness ratio approximately as

\[
b/t=63.2.
\]

No FE value and no historical analytical prediction from that table is imported into the current calculation record.