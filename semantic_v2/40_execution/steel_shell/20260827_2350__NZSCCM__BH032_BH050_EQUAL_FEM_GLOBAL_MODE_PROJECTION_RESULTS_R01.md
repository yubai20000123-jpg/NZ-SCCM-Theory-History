# NZ-SCCM — BH032 / equal-contract BH050 FEM global out-of-plane mode projection

**Execution:** 2026-08-27 (read-only ODB post-processing)  
**Git start HEAD:** `8980f8690012c8e327f53d17ab91a5dec9aa0fc5`  
**Scope:** direct U2 displacement projection only; no Abaqus rerun, no theory or model modification.

## 1. Contract and identity gate

The locked R02 projector was used:

`semantic_v2/40_execution/steel_shell/20260827_2238__NZSCCM__BH_FEM_OUT_OF_PLANE_MODE_PROJECTOR_R02.py`

Both ODBs were opened with `openOdb(..., readOnly=True)`. The projector verified `EXPLICIT_LOADING`, instance `C-S-SHELL-1`, the requested peak frame/time, and `U.getSubset(region=instance)`. The displacement contract is FE global X → theory x, FE global Z → theory/loading y, FE global Y → out-of-plane, with incremental displacement `U2`. No ODB was written.

| Case | ODB | Size (bytes) | Step | Peak frame | Peak time (s) | Peak P (MN) | Paired nodes | Identity |
|---|---|---:|---|---:|---:|---:|---:|---|
| BH032 | `C:\03SCI\abaqus-UCFT test\UCFT_PARAMETRIC_CANONICAL_V1\artifacts\manual_review\BH_LT50_EXPLICIT_R02_GRID_PENALTY\BH_LT50_EXPLICIT_R02_GRID_PENALTY_DT2E6\BH032_EXPLICIT_R02_GRID_B400.odb` | 3496526140 | EXPLICIT_LOADING | 262 | 2.62000083923 | 10.990480 | 1071 | PASS |
| BH050 equal-contract | `C:\03SCI\abaqus-UCFT test\UCFT_PARAMETRIC_CANONICAL_V1\artifacts\manual_review\BH050_EQUAL_CONTRACT_R02_GRID_PENALTY_DT2E6\BH050\BH050_EQUAL_CONTRACT_R02_GRID_B400.odb` | 3496526132 | EXPLICIT_LOADING | 212 | 2.12000060081 | 12.591227 | 1071 | PASS |

The actual FE spans were recovered from the paired face nodes: BH032 `Lx_FE=1600 mm`, `Lz_FE=3200 mm`; BH050 `Lx_FE=2500 mm`, `Lz_FE=5000 mm`. The paired-face baseline is the initial shell-face mid-surface. The mode is `sin(pi*xi)*sin(2*pi*eta)`, with constant, X-tilt and Z-tilt removed. Its sign is fixed by the initial imperfection projection.

## 2. Results

### BH032

- Initial: `W0_FE=3.999999876 mm`, `q0_FE=0.002499999923`; error from frozen `q0=0.0025`: **−0.00000309%**.
- Initial fit: `R2=0.9999999999999`, `NRMS=1.3213e−7`, `RMS=5.2850e−7 mm`.
- Peak: `Wd_FE=4.842375253 mm`, `q_FE=0.003026484533`, `kappa_FE_geom=1.866887817e−5 mm⁻¹`.
- Peak fit: `R2=0.536620494`, `NRMS=0.332179345`, `RMS=1.608537038 mm`.
- Same-load theory target: `q_theory(P_FE)=0.001388642235`, `Wd_theory=2.221827576 mm`, `kappa_theory=8.565843445e−6 mm⁻¹`.
- Same-load ratios/errors: `q_FE/q_theory=2.179456` (**+117.9456%**); same ratios apply to Wd and kappa because the frozen mode geometry is identical.
- Terminal reference: `q_u=0.001378899616`; `q_FE/q_u=2.194855` (**+119.4855%**).

### BH050 equal-contract

- Initial: `W0_FE=6.250000119 mm`, `q0_FE=0.002500000048`; error from frozen `q0=0.0025`: **+0.00000191%**.
- Initial fit: `R2=0.9999999999999`, `NRMS=8.9278e−8`, `RMS=5.5799e−7 mm`.
- Peak: `Wd_FE=12.005278061 mm`, `q_FE=0.004802111224`, `kappa_FE_geom=1.895797523e−5 mm⁻¹`.
- Peak fit: `R2=0.784329538`, `NRMS=0.187456901`, `RMS=2.250472217 mm`.
- Same-load theory target: `q_theory(P_FE)=0.004117589557`, `Wd_theory=10.293973894 mm`, `kappa_theory=1.625559201e−5 mm⁻¹`.
- Same-load ratios/errors: `q_FE/q_theory=1.166243` (**+16.6243%**); same ratios apply to Wd and kappa.
- Terminal reference: `q_u=0.004772819646`, `Wd_u=11.932049115 mm`; `q_FE/q_u=1.006137` (**+0.6137%**).

## 3. Cross-case diagnosis

The initial imperfection amplitude is reproduced essentially exactly in both ODBs, so the initial mode-sign and amplitude contract passes. At the loaded peak, the single frozen global mode is only a partial representation: BH032 has `R2≈0.537` and `NRMS≈33.2%`; BH050 is better but still not exact (`R2≈0.784`, `NRMS≈18.7%`). These residuals are evidence of additional/global-local deformation components, not permission to fit a new mode or alter theory.

The displacement-projected `q_FE` bias is not a common-direction systematic error: BH032 is far above its same-load theory target, while BH050 is moderately above its same-load target and is very close to its terminal reference. Therefore the projection does **not** support a claim that the BH050 load discrepancy is explained solely by the q coordinate. It does show that BH050's peak global amplitude is near the frozen terminal amplitude, whereas its single-mode representation remains imperfect.

`q` here is the direct U2-projected global mode amplitude. It is not a substitute for capacity-surface coordinates, FEM through-thickness curvature, or steel apparent curvature. No FEM value entered root selection, parameter calibration, or any theory update.

## 4. Required answers

1. **Can theory q be interpreted as the dominant FEM global out-of-plane modal amplitude?** Partially. The initial field is an exact match; at peak, BH050 has a dominant but incomplete single-mode representation (`R2=0.784`), while BH032 is substantially multi-component (`R2=0.537`).
2. **Same-direction systematic bias?** No. The peak q error is +117.95% for BH032 versus +16.62% for equal-contract BH050 at the same FEM load.
3. **Is BH050's overprediction localized to q kinematics itself?** Not established. The direct projection gives a +16.62% same-load q difference, but the modal residual is material and q_FE is nearly equal to the terminal q_u; this cannot by itself allocate the Pu difference to the q operator.
4. **More likely next layer?** With q now directly observable, the remaining BH050 discrepancy should be examined in demand–capacity/terminal closure and the non-single-mode component, not by replacing q with a capacity curvature coordinate.
5. **Is there single-mode deficiency?** Yes, quantitatively: BH032 `R2=0.5366`, `NRMS=0.3322`; BH050 `R2=0.7843`, `NRMS=0.1875`.

## 5. Reproducibility and boundaries

Output files are the two projector summaries and paired-node CSVs in the adjacent case directories. This report and the machine-readable summary are additive execution evidence. The canonical ODB binaries are not committed. The projector did not modify the ODB, CAE, INP, materials, boundary conditions, R06, q0, Pcr, C, or root selection.

`BH032_FEM_MODE_PROJECTION = COMPLETED`  
`BH050_EQUAL_FEM_MODE_PROJECTION = COMPLETED`

