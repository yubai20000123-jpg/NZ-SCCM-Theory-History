# BH032 / BH050 UHPC through-thickness projection and observable-contract diagnosis

**Scope:** ODB read-only post-processing only. No Abaqus rerun, no theory/material/R06/R07 change, no calibration.

## 1. Extraction contract

Both existing ODBs were reopened in `EXPLICIT_LOADING` using the previous stations: BH032 global z=800 mm and BH050 global z=1250 mm. The same `UHPC_ALL_CELLS` selection and the same element cross-sectional area construction as the previous resultant extraction were reused. For every valid UHPC C3D8 integration value, the weight is the element `dx*dy` section area divided by the number of valid LE values; the integration-point y coordinate is reconstructed from the C3D8 shape functions. No element-count or integration-point-count averaging is used.

The loading direction is global z and the UHPC total strain is Abaqus logarithmic `LE33`. `PE` and `PEEQ` are not used as total strain. A full weighted 2×2 normal equation is solved for

`LE33(y) = eps0_UHPC_FEM + kappa_UHPC_FEM*(y-y_mid)`.

Actual ODB UHPC node bounds (not forced to ±21 mm) are:

| case | y_lower (mm) | y_upper (mm) | y_mid (mm) | actual half-thickness (mm) | weighted centroid offset (mm) | section area weight (mm²) |
|---|---:|---:|---:|---:|---:|---:|
| BH032 | −20.9686 | 24.9921 | 2.0117 | 22.9804 | +0.507 | 71,042.0 |
| BH050 | −21.0000 | 27.2377 | 3.1188 | 24.1188 | +0.771 | 115,343.1 |

The theoretical comparison values `eps(+21)` and `eps(−21)` are nevertheless retained at exactly ±21 mm, as requested; the direct face-band values use the actual ODB boundaries.

## 2. Endpoint comparison with frozen theory

| quantity | BH032 theory | BH032 UHPC fit at FEM peak | ratio | BH050 theory | BH050 UHPC fit at FEM peak | ratio |
|---|---:|---:|---:|---:|---:|---:|
| eps0 | −0.00249443 | −0.00332953 | 1.335 | −0.00213546 | −0.00207179 | 0.970 |
| kappa (1/mm) | 4.78844×10⁻⁵ | 1.93135×10⁻⁵ | 0.403 | 6.49782×10⁻⁵ | 1.83974×10⁻⁵ | 0.283 |
| chi_core (21 mm) | 0.403 | 0.1218 | 0.302 | 0.639 | 0.1865 | 0.292 |
| eps(+21) | −0.00148886 | −0.00292395 | — | −0.000770916 | −0.00168544 | — |
| eps(−21) | −0.00350000 | −0.00373512 | — | −0.00350000 | −0.00245814 | — |

The steel-derived curvature from the previous run is not used as a generalized-variable observable here.

## 3. Four checkpoint values

### BH032

| λ_theoryLY | P (MN) | eps0 | kappa (1/mm) | chi_core | R² | r_norm | fitted eps(+21) | fitted eps(−21) | face-band upper | face-band lower |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|0.025|7.519|−0.00129617|3.00070e−6|0.0486|0.5537|0.0254|−0.00123316|−0.00135919|−0.00122862|−0.00131830|
|0.501|9.214|−0.00161549|3.58594e−6|0.0466|0.4681|0.0290|−0.00154019|−0.00169080|−0.00153523|−0.00163291|
|0.802|10.286|−0.00221965|9.34944e−6|0.0885|0.5113|0.0504|−0.00202331|−0.00241598|−0.00201835|−0.00230062|
|1.000|10.990|−0.00332953|1.93135e−5|0.1218|0.3493|0.0969|−0.00292395|−0.00373512|−0.00293661|−0.00346217|

### BH050

| λ_theoryLY | P (MN) | eps0 | kappa (1/mm) | chi_core | R² | r_norm | fitted eps(+21) | fitted eps(−21) | face-band upper | face-band lower |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|0.023|8.910|−0.00104418|4.03939e−6|0.0812|0.7154|0.0302|−0.00095936|−0.00112901|−0.00093779|−0.00107075|
|0.500|10.526|−0.00131957|6.12619e−6|0.0975|0.6282|0.0442|−0.00119092|−0.00144822|−0.00115498|−0.00134137|
|0.804|11.557|−0.00154834|8.62689e−6|0.1170|0.5942|0.0569|−0.00136718|−0.00172951|−0.00131416|−0.00157094|
|1.000|12.220|−0.00207179|1.83974e−5|0.1865|0.5792|0.0936|−0.00168544|−0.00245814|−0.00158130|−0.00213570|

The complete frame paths contain 79 BH032 rows and 44 BH050 rows. The four profile keyframes are stored separately with 11 thickness bins each.

## 4. Linear-through-thickness residual audit

Using the requested thresholds based on normalized weighted RMS: both cases are `GOOD` at the first post-LY frame and `ACCEPTABLE` through the peak (`r_norm` 9.69% for BH032 and 9.36% for BH050 at peak; neither exceeds the suggested 15% POOR threshold). However, the weighted R² is only 0.349 for BH032 and 0.579 for BH050 at peak, and the profile bins show local/nonlinear departures, especially in the lower BH050 core band. Therefore the appropriate description is **approximately first-order but with measurable local/nonlinear localization at peak**, not an exact plane section.

The keyframe profiles are in `UHPC_thickness_profile_keyframes.csv`; no profile smoothing was applied.

## 5. Steel/core compatibility cross-check

The UHPC fit was extrapolated to ±23 mm and compared with the previous actual steel mean `LE22` values.

| case at FEM peak | steel upper actual | UHPC fit at +23 | Δ upper | relative | steel lower actual | UHPC fit at −23 | Δ lower | relative |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BH032 | −0.00250958 | −0.00287449 | +3.757e−4 | 15.0% | −0.00266991 | −0.00377972 | +1.104e−3 | 41.3% |
| BH050 | −0.00143804 | −0.00163692 | +2.106e−4 | 14.6% | −0.00172567 | −0.00249896 | +7.693e−4 | 44.6% |

The lower-face compatibility discrepancy is large in both cases and slightly larger for BH050. This means steel material `LE22` is not a clean generalized-section strain observable after local shell deformation; it cannot be used to validate or reject the generalized curvature without a separate shell kinematic mapping.

At the endpoints, converting LE to engineering strain by `exp(LE)-1` changes the maximum absolute value by only 0.224% (BH032) and 0.148% (BH050). This is **STRAIN_MEASURE_DIFFERENCE_NOT_CAUSAL**.

## 6. K1–K5 ranking

1. **K4 — GENERALIZED_VARIABLE_TO_FEM_OBSERVABLE_CONTRACT_NOT_VALIDATED (HIGH).** The BH032 gate does not pass: its UHPC-fit kappa/theory kappa ratio is only 0.403 despite the nearly exact Pu. BH050 is 0.283. Since both cases show the same direction of observable mismatch, the BH050 error cannot yet be assigned uniquely to Marguerre–Airy or section N–M demand.
2. **K3 — PHASE_COMPATIBILITY_OR_LOCAL_SHELL_KINEMATIC_DECOUPLING (MEDIUM-HIGH).** Steel/core extrapolation errors reach 41–45% on the lower side in both cases. BH050 is not uniquely separated from BH032, but the common-strain assumption is demonstrably imperfect.
3. **K2 — SECTION_WARPING_OR_LOCALIZATION_NOT_CAPTURED_BY_LINEAR_NM_KINEMATICS (MEDIUM).** The first-order fit is usable but not exact at peak (`r_norm` ≈ 9–10%, R² 0.35–0.58, nonzero face-band residuals). This is a secondary issue until the observable contract is resolved.
4. **K1 — MARGUERRE_AIRY_OR_SECTION_NM_PATH_MISMATCH (LOW/CONDITIONAL).** BH050 fitted kappa is far below its frozen theoretical value, but BH032 is also far below; the present data do not isolate an upstream demand error.
5. **K5 — MIXED (not a primary label).** The evidence is mixed in the broad sense, but K4/K3/K2 provide the ordered mechanisms; “mixed” alone is not an adequate diagnosis.

## 7. Direct answers

**Q1. BH032 UHPC LE33 linearity:** approximately first-order with measurable peak localization. Peak `R²=0.349`, `r_norm=9.69%`, fitted `eps0=-0.00332953`, `kappa=1.93135e-5/mm`, fitted `eps(-21)=-0.00373512`.

**Q2. BH050 UHPC LE33 linearity:** approximately first-order but with measurable peak nonlinearity/localization. Peak `R²=0.579`, `r_norm=9.36%`, fitted `eps0=-0.00207179`, `kappa=1.83974e-5/mm`, fitted `eps(-21)=-0.00245814`.

**Q3. BH032 theory kappa versus UHPC-fit kappa:** **NO** as a strict observable-contract gate; ratio ≈0.403.

**Q4. BH050 theory kappa versus UHPC-fit kappa:** **YES, significantly different**; the peak ratio is ≈0.283 (theory is about 3.53 times the UHPC-fit curvature). The difference is already present at the first post-LY frame and grows toward the peak; an exact first-divergence load cannot be isolated because the frozen theory continuation curve is not available, only its endpoint.

**Q5. Steel/core compatibility:** not exact in either case. Lower-face relative mismatch is about 41.3% for BH032 and 44.6% for BH050; BH050 is slightly worse, but not by enough to establish it as the sole source of the 9.3% Pu error.

**Q6. Best-supported classification:** K4 > K3 > K2 > K1; K5 is only a residual umbrella description.

**Q7. Next theory-review priority:** first clarify **C (linear-through-thickness section kinematics)** and **D (steel/UHPC phase compatibility)**; only after that return to **A/B (Marguerre–Airy and terminal section N–M)**. R02/R06 steel operator review is later, because steel `LE22` is not the generalized-strain observable required for that conclusion.

## 8. Artifacts and hashes

- `BH032_UHPC_thickness_linear_projection_path.csv`: 79 rows; SHA-256 `782095E0A5F045A44E8D9B54D56244865CB780558B8BC7459D3CF94C7B9396F3`.
- `BH050_UHPC_thickness_linear_projection_path.csv`: 44 rows; SHA-256 `5B1C055C7AAC945A6C64727DA5F8E76F2244E8182565FDF44A528BF6E84410A3`.
- `UHPC_projection_checkpoints.json`: SHA-256 `56EE114A0CB2D127AC54D5F60EF923B4802D22BA832AA300AA95A93D60EE3316`.
- `UHPC_thickness_profile_keyframes.csv`: 88 rows (4 keyframes × 11 bins × 2 cases); SHA-256 `8A97C05C190ABA46D426FA009914BCB782A83B0101A60072B7A02013F7EBC3BA`.

The CSV column names are preserved in the files; the main projection columns are `eps0_UHPC_FEM`, `kappa_UHPC_FEM_per_mm`, `chi_core_UHPC_FEM`, `R2_weighted`, `r_RMS`, `r_norm`, `max_abs_residual`, `p95_abs_residual`, `eps_core_plus21_fit`, `eps_core_minus21_fit`, `eps_UHPC_upper_face_band`, `eps_UHPC_lower_face_band`, `eps_upper_steel_actual`, `eps_lower_steel_actual`, `delta_upper_compat`, `delta_lower_compat`, `Ny_UHPC`, `Ny_steel`, and `Ny_web`.

## 9. GitHub status

One availability check was made and failed (`github.com:443` unreachable). No further network attempts were made. No local clone with the requested remote is present, so no GitHub write or commit was attempted and no theory/archive file was modified.

`GITHUB_ARCHIVE = NOT_AVAILABLE`  
`LOCAL_COMMIT = NOT_CREATED`  
`PUSH_STATUS = NOT_ATTEMPTED`
