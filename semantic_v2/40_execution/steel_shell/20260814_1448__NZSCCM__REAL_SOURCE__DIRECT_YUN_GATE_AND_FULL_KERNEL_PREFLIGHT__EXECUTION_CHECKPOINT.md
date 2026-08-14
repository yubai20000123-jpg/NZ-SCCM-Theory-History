# Execution checkpoint — direct real-source Yun gate and full-kernel preflight

Date: 2026-08-14 14:48 Asia/Tokyo

## Requested operation

1. Retire `b_s/t_s >= 56` as the final screen.
2. Search real concrete-constrained steel faceplates directly with the actual compiled Yun gate

\[
\sigma_{cr,Yun}<f_y.
\]

3. Once a source point passes, attempt to enter the unchanged frozen `R10 + N48-C1/MM + Cayley-Hamilton + general-D15 + double steel-shell + Yun` branch and track

\[
B_s\to S1_{Yun}\to Y_s\to K_Z/L.
\]

4. Correct the Zhou ultimate-capacity comparator: use Zhou's proposed stability/ultimate curve rather than raw cross-section strength `Pyth`.

No experimental root selection, no synthetic geometry, no source-free material parameter, no structural calibration.

## Final screening identity

```text
FINAL_LOCAL_GATE = sigma_cr_Yun < fy
BT_THRESHOLD_56_AS_FINAL_GATE = RETIRED
BT_THRESHOLD_56 = HISTORICAL_PRELIMINARY_SSSS_SCREEN_ONLY
```

The already-compiled Yun expressions are used unchanged:

\[
k_{crx}(r)=\frac{4(3r^4+2r^2+3)}{3r^2},\qquad r=\ell/b,
\]

\[
\sigma_{cr,Yun}=k_{crx}(r)\frac{\pi^2E_s}{12(1-\nu_s^2)}\left(\frac{t_s}{b}\right)^2.
\]

## Real-source search result A — Sun Lipeng Chapter 4 family

Sun's real PBL-stiffened ordinary-concrete parameter family was re-screened source-first. The one-factor table reaches `s_l/t=63`, but the high-yield-strength rows and the large-`s_l/t` rows are separate source points and must not be combined into a synthetic case.

No real Sun Chapter-4 row was found that simultaneously closes a clean compiled-Yun `sigma_cr_Yun < fy` condition and the frozen ordinary-concrete material inputs required by the current global R10 operator.

```text
SUN_REAL_SOURCE_SCREEN = NO CLEAN FULL-KERNEL CASE
SYNTHETIC_COMBINATION_OF_ONE_FACTOR_ROWS = PROHIBITED
```

## Real-source search result B — Shi, Gao & Guo 2021

Source: *Compressive behaviour of double skin composite shear walls stiffened with steel-bars trusses*, JCSR 180 (2021) 106581.

The source contains the real specimen family `DSCST140-120`. For the steel faceplate:

```text
vertical/loading-direction weld spacing ell = 140 mm
horizontal spacing / Yun transverse width b = 120 mm
r = ell/b = 7/6
steel plate thickness t = 1.5 mm
Es = 215000 MPa
nu = 0.24
fy = 379.6 MPa
```

Exact compiled-Yun evaluation:

```text
kcr_Yun = 11.049886621315194
kp_Yun  = 44.08260045936561
sigma_cr_Yun = 323.96607164184695 MPa
sigma_cr_Yun/fy = 0.8534406523757823
fy/sigma_cr_Yun - 1 = 0.17172763825607595
```

Therefore the local mechanism gate is a strict PASS:

\[
\boxed{323.9661<379.6\;\mathrm{MPa}}
\]

and the current local steel-shell event ordering is admissible as

\[
\boxed{B_s\to S1_{Yun}\to Y_s}.
\]

The 17.17% number above is only the stress interval between the elastic Yun buckling threshold and first steel yield; it is **not** a global `Pu` reserve.

### Full frozen-kernel preflight for Shi specimen

The calculation was stopped before a false global root was generated because the real specimen is not the same structural object as the frozen reduced two-faceplate model:

- its steel-bar trusses are explicitly load-resisting members as well as local-buckling restraints;
- it has edge CFST boundary members;
- deleting those source members and comparing against the actual specimen maximum load would change the structural object;
- the frozen R10 operator requires ordinary-concrete `eps0` as an explicit material input, and a source-frozen value for this exact specimen has not been recovered.

Therefore:

```text
SHI_DSCST140_120_DIRECT_YUN_GATE = PASS
SHI_LOCAL_ORDERING_BS_S1_YS = ADMISSIBLE
SHI_FULL_R10_D15_YUN_ROOT = BLOCKED_PRE_SOLVE
BLOCK_1 = SOURCE_TOPOLOGY_MISMATCH_LOAD_RESISTING_TRUSS_AND_EDGE_CFST
BLOCK_2 = R10_EPS0_NOT_SOURCE_FROZEN
NO_FAKE_Du_qu_Pu = PASS
```

This is a successful direct local-Yun source gate, but not yet the first clean full-system Pu benchmark.

## Real-source search result C — Yang, Liu & Fan 2016

Source: *Buckling behavior of double-skin composite walls: An experimental and modeling study*, JCSR 121 (2016) 126-135.

This source is topologically closer to the frozen target: two flat steel faceplates + ordinary infill concrete + discrete headed studs/tie restraints, without the Shi steel-bar-truss load-resisting subsystem.

A published review database reproduces the Yang test rows, including:

```text
DSC4-300 (square studs)
fcu = 39.6 MPa
fy = 409.5 MPa
t = 4 mm
B/t = 75
Pu,test = 11610 kN
reported failure/local-buckling class = ELASTIC LOCAL BUCKLING
```

The primary Yang paper itself states that large `B/t` specimens were deliberately used to investigate elastic local buckling and that local buckling reduced strength/ductility.

This specimen is therefore the current highest-priority **full-topology** candidate.

However, the exact source steel `Es, nu` pair needed to replay the **Yun** formula, and the ordinary-concrete `eps0` input needed by frozen R10, have not yet been source-closed. They are not replaced by generic textbook values.

```text
YANG_DSC4_300_FULL_TOPOLOGY_PRIORITY = YES
YANG_SOURCE_CLASSIFICATION = ELASTIC_LOCAL_BUCKLING
YANG_DIRECT_YUN_NUMERIC_GATE = PENDING_SOURCE_EXACT_Es_nu
YANG_FULL_R10_D15_YUN_ROOT = PENDING_SOURCE_R10_eps0
NO_GENERIC_Es_nu_OR_INVENTED_eps0 = PASS
```

## Zhou ultimate-comparator correction

The preceding comparison against raw `Pyth` is demoted. Zhou's own axial ultimate identity is

\[
\boxed{P_u=\varphi_N P_{yth}}.
\]

For four-edge simply-supported axial compression, Zhou's proposed stability factor is Eq. (5-87)-(5-88):

\[
\varphi_N=1\quad(\lambda_n\le0.55),
\]

\[
\varphi_N=\frac{1}{\Phi+\sqrt{\Phi^2-\lambda_n^2}}\quad(\lambda_n>0.55),
\]

with

\[
\Phi=0.454+0.192\lambda_n+0.416\lambda_n^2\quad(\lambda_n\le1.0),
\]

\[
\Phi=-0.140+1.387\lambda_n-0.186\lambda_n^2\quad(\lambda_n>1.0).
\]

Hence the correct ultimate comparison is

\[
\boxed{P_{u,NZ}\;\text{vs}\;P_{u,Zhou,emp}=\varphi_N(\lambda_n)P_{yth}}.
\]

The existing `Pyth_reduced=39.2928 MN` is retained only as the same-object **section-strength baseline**, not as Zhou's ultimate prediction.

The source-exact definition of `lambda_n` must be recovered before releasing a numerical `phi_N` or `Pu_Zhou,emp` for the reduced object. No assumed `lambda_n=sqrt(Pyth/Pcr)` value is inserted without the source equation being explicitly recovered.

```text
ZHOU_RAW_PYTH_AS_ULTIMATE_COMPARATOR = RETIRED
ZHOU_PYTH_REDUCED_39_2928_MN = SECTION_STRENGTH_BASELINE_ONLY
ZHOU_ULTIMATE_COMPARATOR = phi_N(lambda_n) * Pyth
ZHOU_EQ5_87_5_88 = ACTIVE
ZHOU_NUMERIC_EMPIRICAL_PU_REDUCED = PENDING_SOURCE_EXACT_lambda_n_DEFINITION
```

## Current gate

```text
REAL_SOURCE_DIRECT_YUN_SEARCH = PASS
FIRST_EXACT_sigma_cr_Yun_LT_fy_REAL_POINT = SHI_DSCST140_120
FIRST_EXACT_LOCAL_BS_S1_YS_GATE = PASS
FIRST_FULL_R10_D15_YUN_PU = NOT RELEASED
PRIMARY_FULL_TOPOLOGY_NEXT_CASE = YANG_DSC4_300
FULL_ROOT_RELEASE_REQUIRES = source-exact Es,nu + source-constrained R10 eps0 + unchanged topology
```
