# BH032 / BH050 post-local-yield strain–curvature path diagnosis (R01)

**Status:** diagnosis-only; ODB read-only; no Abaqus rerun; no R06/theory/model change.

## 1. ODB extraction contract

| item | BH032 | BH050 |
|---|---|---|
| ODB | `...\\BH032_EXPLICIT_R02_GRID_B400.odb` | `...\\BH050_EXPLICIT_R17_ANALYTICBOW_B400_UNIFORMMS.odb` |
| absolute path | `C:\\03SCI\\abaqus-UCFT test\\UCFT_PARAMETRIC_CANONICAL_V1\\artifacts\\manual_review\\BH_LT50_EXPLICIT_R02_GRID_PENALTY\\BH_LT50_EXPLICIT_R02_GRID_PENALTY_DT2E6\\BH032_EXPLICIT_R02_GRID_B400.odb` | `C:\\03SCI\\abaqus-UCFT test\\UCFT_PARAMETRIC_CANONICAL_V1\\artifacts\\manual_review\\BH050_OPEN_SIDE_SS4_R01\\diagnostic_r16_allvd_0p1s\\BH050_EXPLICIT_R17_ANALYTICBOW_B400_UNIFORMMS.odb` |
| step | `EXPLICIT_LOADING` | `EXPLICIT_LOADING` |
| station | z = 800 mm | z = 1250 mm |
| width normalization | b = 1592 mm | b = 2500 mm |

The previous resultant selections were reused: `UHPC_ALL_CELLS`, `UCFT_OUTER_SHELL_FACES` (station horizontal faces split by centroid y sign), and `UCFT_PBL_WEB_FACES`.

Available strain fields were checked in both ODBs: `LE`, `PE`, `PEEQ` (and corresponding stress/displacement fields). `LE` was selected as the total logarithmic strain. Plastic strain/PEEQ was not used as total strain. For horizontal shell faces the longitudinal loading direction is global z and is local shell direction 2, hence `LE22`; for the UHPC solid it is global z, hence `LE33`. Section/integration-point values were averaged within each element and then area-weighted over the complete selected face/solid station. The reported steel strain is therefore a face-centroid/membrane-like mean, not an extreme outer section-point value.

With `z_f = 23 mm` and compression-negative sign convention:

\[
\varepsilon_{y0}=(\varepsilon_{upper}+\varepsilon_{lower})/2,
\qquad
\kappa_y=(\varepsilon_{upper}-\varepsilon_{lower})/(2z_f),
\qquad
\chi_y=z_f|\kappa_y|/|\varepsilon_{y0}|.
\]

The full frame-by-frame CSVs contain all frames from the first available post-LY frame to the FEM peak. No frame was created at the exact theoretical P_LY when the ODB did not contain one; the first available frames are 7.518816 MN (BH032) and 8.909772 MN (BH050). `lambda_theoryLY` in the CSV/JSON is `(P-P_LY,theory)/(P_peak-P_LY,theory)`; the first available frame is therefore about 0.025 and 0.023, respectively.

## 2. 11-point checkpoint tables

### BH032 (P_LY,theory = 7.43075 MN; P_peak = 10.99048 MN)

| λ | P | eps_upper | eps_lower | eps_y0 | kappa_y (10^-6) | chi | sigma_upper | sigma_lower | Ny_UHPC | Ny_steel |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|0.025|7.519|-0.001229|-0.001331|-0.001280|2.216|0.0398|-245.4|-279.1|-2501|-2109|
|0.100|7.786|-0.001272|-0.001380|-0.001326|2.351|0.0408|-253.8|-289.4|-2592|-2184|
|0.200|8.144|-0.001329|-0.001449|-0.001389|2.592|0.0429|-265.0|-303.3|-2714|-2285|
|0.300|8.498|-0.001386|-0.001516|-0.001451|2.821|0.0447|-276.1|-316.9|-2835|-2384|
|0.393|8.831|-0.001438|-0.001578|-0.001508|3.028|0.0462|-286.3|-329.4|-2953|-2475|
|0.501|9.214|-0.001486|-0.001650|-0.001568|3.564|0.0523|-294.7|-343.9|-3098|-2567|
|0.601|9.569|-0.001541|-0.001709|-0.001625|3.650|0.0517|-303.2|-328.1|-3300|-2538|
|0.702|9.931|-0.001678|-0.001765|-0.001721|1.891|0.0253|-313.0|-263.8|-3629|-2319|
|0.802|10.286|-0.001818|-0.001937|-0.001878|2.594|0.0318|-307.9|-232.8|-3923|-2174|
|0.900|10.636|-0.001982|-0.002089|-0.002036|2.314|0.0261|-305.3|-223.3|-4185|-2125|
|1.000|10.990|-0.002510|-0.002670|-0.002590|3.485|0.0310|-292.6|-198.1|-4532|-1973|

### BH050 (P_LY,theory = 8.83278 MN; P_peak = 12.21981 MN)

| λ | P | eps_upper | eps_lower | eps_y0 | kappa_y (10^-6) | chi | sigma_upper | sigma_lower | Ny_UHPC | Ny_steel |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|0.023|8.910|-0.000917|-0.000992|-0.000955|1.617|0.0390|-180.0|-193.3|-2085|-1498|
|0.101|9.176|-0.000942|-0.001019|-0.000981|1.669|0.0391|-188.1|-197.9|-2181|-1568|
|0.194|9.488|-0.000980|-0.001034|-0.001007|1.171|0.0267|-195.3|-201.2|-2291|-1631|
|0.287|9.806|-0.001009|-0.001083|-0.001046|1.594|0.0351|-200.0|-204.8|-2402|-1680|
|0.399|10.184|-0.001045|-0.001121|-0.001083|1.643|0.0349|-204.0|-205.1|-2491|-1721|
|0.500|10.526|-0.001096|-0.001126|-0.001111|0.642|0.0133|-216.3|-205.9|-2525|-1694|
|0.605|10.883|-0.001133|-0.001193|-0.001163|1.293|0.0256|-220.5|-214.5|-2609|-1745|
|0.697|11.194|-0.001164|-0.001254|-0.001209|1.954|0.0372|-226.3|-217.2|-2694|-1780|
|0.804|11.557|-0.001215|-0.001304|-0.001260|1.936|0.0353|-234.3|-222.2|-2780|-1832|
|0.899|11.878|-0.001275|-0.001408|-0.001341|2.897|0.0497|-241.9|-229.3|-2842|-1891|
|1.000|12.220|-0.001438|-0.001726|-0.001582|6.253|0.0909|-254.4|-231.6|-2905|-1950|

## 3. Endpoint and closure audit

| case | quantity | first available post-LY | FEM peak | change |
|---|---|---:|---:|---:|
|BH032|eps_upper|−0.00122885|−0.00250958|more compressive|
|BH032|eps_lower|−0.00133080|−0.00266991|more compressive|
|BH032|eps_y0|−0.00127982|−0.00258975|more compressive|
|BH032|kappa_y|2.216e−6|3.485e−6|+57.3%|
|BH032|chi_y|0.03983|0.03095|no growth; lower at peak|
|BH050|eps_upper|−0.00091739|−0.00143804|more compressive|
|BH050|eps_lower|−0.00099179|−0.00172567|more compressive|
|BH050|eps_y0|−0.00095459|−0.00158185|more compressive|
|BH050|kappa_y|1.617e−6|6.253e−6|3.87×|
|BH050|chi_y|0.03897|0.09092|2.33×, still far below theory terminal 0.700|

The inherited resultant closure check remains usable for trend diagnosis: maximum absolute closure error is approximately 3.15% for BH032 and 4.10% for BH050 (peak errors +1.28% and −3.16%).

As an auxiliary UHPC check, BH050 peak `eps_UHPC_mean = −0.002058` and station local minimum is `eps_UHPC_min = −0.002959`; the latter remains less compressive than the frozen theoretical terminal value −0.0035. This is a cross-check only and does not alter the terminal criterion.

BH050 has no upper-strain turning point: the most-compressive upper mean strain occurs at the peak. Its upper mean stress also moves from −180.0 to −254.4 MPa. Thus strain and stress have the same loading direction. The lower stress has a mild late-stage turning/relaxation, but this does not change the upper-face conclusion.

## 4. H1/H2/H3 diagnosis

**Primary diagnosis: H1 — structural/section strain–curvature path mismatch (HIGH confidence).**

The decisive observation is not merely a stress difference: in BH050 the measured upper-face total strain itself becomes more compressive from post-LY to peak, while the frozen R06 terminal state would require the upper strain to become less compressive (−0.000917 at the first available FEM frame versus theoretical terminal target −0.000641, with the theoretical path tending toward unloading). FEM peak curvature is only 6.253×10−6/mm and chi = 0.0909, versus frozen theoretical terminal curvature 6.498×10−5/mm and chi ≈ 0.700. Therefore R06 is receiving a different face-strain state; the first layer to audit is upstream: Marguerre–Airy demand → section N–M equilibrium → eps_y0/kappa_y path. This dataset does not isolate R06 as the primary error.

**H2 — steel current resultant/operator mismatch: rejected as the primary BH050 explanation.** For H2, strain would unload while stress continued to become more compressive. BH050 instead shows both `LE22` and mean stress becoming more compressive. A secondary steel constitutive/localization effect may still exist, but it cannot be assigned primary status from this path.

**H3 — mixed:** not required for the BH050 upper-face diagnosis. BH032 does show a separate stress/strain decoupling on the lower face (lower strain remains more compressive while lower stress unloads after approximately λ ≈ 0.5), so BH032 is not a proof that every local-yield path is operator-consistent. It is, however, not the BH050 upper-face H2 pattern.

## 5. BH032 control interpretation

BH032 upper and lower strains both become more compressive to peak, while `chi_y` stays small (about 0.03–0.05) and ends at 0.03095. The upper stress reaches its most compressive value around the later middle path and then slightly relaxes (−314 MPa near λ≈0.685 to −292.6 MPa at peak); the lower stress relaxes substantially after about λ≈0.5 (−349.5 MPa minimum to −198.1 MPa at peak). This is a low-curvature, mostly membrane-dominated path with steel/UHPC redistribution that does not develop the severe BH050 curvature amplification. That quantitative difference is consistent with BH032’s near-zero Pu error and BH050’s large overprediction, but it does not by itself prove the complete source of the BH032 success.

## 6. Direct answers

1. **BH050 upper steel strain:** `MORE_COMPRESSIVE`, −0.00091739 → −0.00143804 from first available post-LY frame to peak. It does not unload.
2. **BH050 FEM kinematics:** eps_y0 becomes more compressive (−0.00095459 → −0.00158185); kappa_y rises 1.617×10−6 → 6.253×10−6/mm; chi_y rises 0.03897 → 0.09092, but remains about 7.7 times below frozen theoretical terminal chi ≈ 0.700.
3. **First clear theory/FEM divergence:** `STRAIN/CURVATURE`, not first at stress/resultant. FEM upper strain and stress are directionally consistent loading; the frozen theory’s terminal upper-face state is unloading.
4. **Next layer to audit:** `MARGUERRE_AIRY / SECTION_EQUILIBRIUM` (structural demand and section N–M path), before assigning primary blame to the R02/R06 steel operator.
5. **Why BH032 does not show same final error:** its post-LY chi remains approximately 0.03–0.05 and does not grow toward a curvature-dominated state; BH050 grows to 0.0909 with a 3.87-fold curvature increase. BH032’s steel unloading therefore occurs on a materially different, low-curvature redistribution path and cannot be used to validate the BH050 theoretical curvature continuation.

## 7. Artifact provenance

Original local artifacts generated by Codex included:

- `BH032_post_LY_strain_curvature_path.csv` — all 79 post-LY frames.
- `BH050_post_LY_strain_curvature_path.csv` — all 44 post-LY frames.
- `post_LY_strain_curvature_summary.json` — endpoints, 11 checkpoints, turning points, method contract, H1/H2 diagnosis.
- this report.

This GitHub copy archives the report and key checkpoint evidence additively. No canonical theory file is modified.