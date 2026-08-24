# NZ-SCCM — Swartz8 minimum-of-source-length capacities R05

**Time:** 2026-08-24 08:27 +08:00  
**Status:** `MINIMUM_CAPACITY_ENVELOPE = SELECTED / AIRY_UNCHANGED / AXIAL_CUT_Ny_My_UNCHANGED / PF_COMPARATOR_ONLY`

## 0. Correction

For each specimen, when the source-supported longitudinal morphology supplies two physical partition lengths, both lengths are calculated with the same frozen Airy + axial-cut `Ny-My` terminal. The specimen prediction is then the smaller theoretical ultimate load:

\[
\boxed{P_u^{panel}=\min_i P_u(\ell_i)}.
\]

This is not a best-fit selection against the experiment. The experimental failure load `Pf` is not used to choose the controlling length. The rule is the structural lower-envelope rule: if either admissible physical halfwave/partition reaches its terminal capacity at a lower common axial load, that lower load controls the specimen.

For Case 14 only one length is retained. For Case 21 the two reported half-lengths are both 1220 mm and therefore give the same capacity.

## 1. Selected results

|Case|candidate Pu values / kN|selected minimum Pu / kN|Pf / kN|error|
|---:|---|---:|---:|---:|
|4|595.536, 679.190|595.536|534.231|+11.48%|
|5|650.215, 568.598|568.598|623.641|-8.83%|
|6|621.074, 717.181|621.074|691.698|-10.21%|
|8|521.237, 623.193|521.237|455.053|+14.54%|
|9|592.150, 650.922|592.150|625.865|-5.39%|
|14|766.430|766.430|716.164|+7.02%|
|21|408.081, 408.081|408.081|368.313|+10.80%|
|23|367.811, 482.939|367.811|346.961|+6.01%|

Statistics:

```text
mean signed error = +3.1777 %
MAE               =  9.2835 %
RMSE              =  9.7233 %
```

These statistics are numerically identical to the earlier R03 axial-cut table because, for this selected set, the previously retained length happened to be the minimum-capacity branch in every specimen (Case 21 is a tie). The conceptual identity is now different and explicit: the panel prediction is a lower envelope over the source-supported physical lengths, not an arbitrary single-wave assignment.

## 2. Gate

```text
PANEL_Pu_RULE = MIN_OVER_SOURCE_SUPPORTED_LENGTH_CAPACITIES
CHOOSE_LENGTH_BY_CLOSENESS_TO_Pf = PROHIBITED
Pf_IN_ROOT_SELECTION = NO
Pf_IN_LENGTH_CONTROL_SELECTION = NO
AIRY = UNCHANGED
TERMINAL = AXIAL_CUT_Ny_My
R04_TWO_LENGTH_CALCULATIONS = RETAINED
R05_MINIMUM_ENVELOPE = CURRENT_COMPARISON_RULE
```
