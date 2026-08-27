# CURRENT STATE ADDENDUM — direct FEM global out-of-plane mode projection

**Updated:** 2026-08-27 23:50 +08:00  
**Scope:** read-only projection of canonical BH032 and equal-contract BH050 ODB peak frames using locked projector R02.

```text
BH032_FEM_MODE_PROJECTION = COMPLETED
BH050_EQUAL_FEM_MODE_PROJECTION = COMPLETED
THEORY_MODIFIED = NO
ODB_MODIFIED = NO
```

## Frozen identity

BH032 uses `BH032_EXPLICIT_R02_GRID_B400.odb`, `EXPLICIT_LOADING`, `C-S-SHELL-1`, frame 262 at 2.62000083923 s. BH050 uses `BH050_EQUAL_CONTRACT_R02_GRID_B400.odb`, the same step/instance, frame 212 at 2.12000060081 s. Both use 1071 paired face nodes and recover the full FE spans (`1600×3200 mm` and `2500×5000 mm`, respectively).

## Direct U2 projection

Initial defects reproduce the frozen `q0=0.0025` to within `3.1e−6%` (BH032) and `1.9e−6%` (BH050), with initial modal `R2≈1` in both cases. At the FEM peaks:

```text
BH032: q_FE=0.003026484533, Wd_FE=4.842375253 mm,
       kappa_FE_geom=1.866887817e-5 1/mm, R2=0.536620, NRMS=0.332179
BH050: q_FE=0.004802111224, Wd_FE=12.005278061 mm,
       kappa_FE_geom=1.895797523e-5 1/mm, R2=0.784330, NRMS=0.187457
```

At the same FEM loads, frozen theory gives `q=0.001388642235` (BH032) and `q=0.004117589557` (BH050). The corresponding q differences are `+117.95%` and `+16.62%`; relative to the frozen terminal roots they are `+119.49%` and `+0.61%`. These are diagnostic comparisons only. No FEM displacement was used to change q, q0, Pcr, C, R06, UHPC/steel parameters, or root selection.

The loaded single-mode fit is incomplete, particularly for BH032. The result supports q as a meaningful global coordinate only **partially** and does not establish that the BH050 Pu difference is caused by q kinematics alone. Subsequent review, if requested, should keep the direct q observable separate from capacity-surface coordinates and examine the remaining demand–capacity/terminal and multi-component deformation effects.

