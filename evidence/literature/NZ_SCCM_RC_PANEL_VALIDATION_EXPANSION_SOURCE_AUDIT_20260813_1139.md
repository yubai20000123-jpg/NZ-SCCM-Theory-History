# NZ-SCCM ordinary-RC panel validation expansion — source audit

**Timestamp:** 2026-08-13 11:39 +08:00  
**Identity:** LITERATURE/RAW-DATA ACQUISITION AUDIT / NO CALIBRATION

## 0. Screening contract

Strict current structural compatibility is screened against the present NC+Rebar production model:

```text
ordinary reinforced concrete solid rectangular wall/panel
one continuous representative halfwave compatible
uniform in-plane uniaxial compression
central/concentric loading preferred: e = 0
all four edges simply supported or a documented close experimental realization
no opening
orthogonal reinforcement compatible with current x/y rebar mapping
physical failure/ultimate load available
raw geometry/material/rebar/imperfection data sufficient for blind solve
```

Failure load must never be used to infer a missing material, reinforcement or imperfection parameter.

## 1. Shahin, Mahmoud, El-Gohary & Taha — 2011

Primary paper identified:

`Evaluation of Experimental Results of Normal Strength Reinforced Concrete Walls in One and Two-way Action under Centric and Eccentric In-Plane Forces`, Journal of Al-Azhar University Engineering Sector, 33(2), April 2011.

The paper reports 12 normal-strength RC wall specimens: five one-way panels and seven four-side-supported two-way panels. Both centric and eccentric in-plane compression were tested to failure.

The four strict current-structure candidates are the centric two-way specimens:

|specimen|H×L×t (cm)|H/t|H/L|test Fcu (kg/cm²)|vertical steel|horizontal steel|eccentricity|failure load|
|---|---:|---:|---:|---:|---|---|---:|---:|
|TW8|160×120×8|20|1.33|244.5|6φ6/m/side|5φ6/m/side|0|112.11 ton|
|TW10|160×120×10|16|1.33|322.2|7φ6/m/side|6φ6/m/side|0|191.91 ton|
|TW12|160×120×12|13.3|1.33|282.2|5φ8/m/side|7φ6/m/side|0|215.74 ton|
|TA10|160×100×10|16|1.60|256.0|7φ6/m/side|6φ6/m/side|0|168.07 ton|

The paper states that the walls used double meshes of 6 mm and 8 mm plain steel bars, grade 24/35. Test-time cube strengths were reported. The setup was intended to provide hinged top/bottom edges and simply supported side edges for two-way action.

### Current admission status

```text
STRUCTURAL_MATCH = STRONG
PRIMARY_FULLTEXT = AVAILABLE
EXPERIMENTAL_Pf = AVAILABLE
CURRENT_BLIND_CALCULABILITY = NOT YET COMPLETE
```

Missing or unresolved for the current R10 contract: specimen-specific `E0`, `epsilon0`, `nu`, stress-free initial imperfection `q0/A0`, steel coupon `Es/fy` identity, and the admissible mapping from reported cube strength `Fcu` to the current R10 `fc` input. None may be inferred from the reported failure load.

## 2. Waddick & Swifte — 1991

Original source identified through later literature:

`M. Waddick and B. Swifte, Buckling of Thin-Walled Concrete Structure, Fourth Year Project Report, Department of Civil Engineering, Monash University, 1991.`

Doh's 2002 thesis records three panels:

```text
H = 2.0 m
L = 1.0 m
t = 25 mm
H/t = 80
L/t = 40
all four sides simply supported
concentric axial loading
normal concrete strengths = 37.9–42.6 MPa
central 2.5 mm wire mesh @ 25 mm
rho_v = 0.00245
rho_h = 0.00315
failure loads = 357–450 kN
failure = brittle double-curvature pattern
```

### Current admission status

```text
STRUCTURAL_MATCH = STRONG
SECONDARY_DATA = SUBSTANTIAL
PRIMARY_REPORT = NOT YET ACQUIRED
CURRENT_BLIND_CALCULABILITY = INPUT_INCOMPLETE
```

Need the original report or another specimen-level primary table for individual strength/failure mapping, elastic modulus/reference strain, imperfection, and steel coupons.

## 3. Roongsang — 1994

Original source identified through later literature:

`D. Roongsang, Buckling of Reinforced Concrete Walls with Simply Supported Side Edges, Structural Engineering Report, Monash University, 1994.`

Doh's 2002 thesis records three 2 m × 1 m × 50 mm panels. Two were four-side-supported; one of these was concentrically loaded and one used e=t/6. For the strict-match centric two-way specimen:

```text
H = 2.0 m
L = 1.0 m
t = 50 mm
H/t = 40
L/t = 20
four-side-supported two-way action
concentric load e = 0
average concrete strength ≈ 45 MPa
central 6.1 mm micro-deformed bars @ 100 mm
rho_v = rho_h = 0.0058
failure load = 1854 kN
failure = brittle double-curvature pattern
```

### Current admission status

```text
STRUCTURAL_MATCH = STRONG
SECONDARY_DATA = SUBSTANTIAL
PRIMARY_REPORT = NOT YET ACQUIRED
CURRENT_BLIND_CALCULABILITY = INPUT_INCOMPLETE
```

## 4. Ernst — 1952 / Ernst-Hromadik-Riveland — 1953

Primary ACI record:

`George C. Ernst, Stability of Thin-Shelled Structures, ACI Journal Proceedings, Vol.49, pp.277–291, 1952, DOI 10.14359/11818.`

ACI's abstract states that the work presents a series of new tests illustrating thin-shell stability and examining empirical/tangent-modulus concepts.

The later Doh thesis describes about 10 small-scale rectangular reinforced concrete panels, simply supported on all four edges under uniformly distributed compression, with approximately:

```text
H/t = 13–80
H/L = 0.5–1.0
L/t = 26.67–80
t = 12–38 mm
single symmetric reinforcement layer
```

A broader 1953 source is independently catalogued:

`G.C. Ernst, J.J. Hromadik, A.R. Riveland, Inelastic Buckling of Plain and Reinforced Concrete Columns, Plates, and Shells, Engineering Experiment Station Bulletin 3, University of Nebraska, 1953.`

The located library catalogue has no electronic copy.

### Current admission status

```text
STRUCTURAL_MATCH = LIKELY_STRONG
PRIMARY_METADATA = CONFIRMED
SPECIMEN_LEVEL_INPUT = INCOMPLETE
ARCHIVAL_ACQUISITION_PRIORITY = HIGH
```

## 5. Explicit exclusions from strict current validation

- Saheb & Desayi (1990): 24 four-side-supported two-way RC panels, but the primary ASCE record explicitly states eccentric vertical loading to represent accidental eccentricity. `OUT_OF_CURRENT_CENTRIC_SCOPE`.
- Fragomeni, Doh & Lee (2012): 47 RC wall panels with openings, one/two-way, uniformly distributed load at `e=t/6`. `OUT_OF_CURRENT_SCOPE = OPENING + ECCENTRICITY`.
- Three-side-restrained RC walls (2018 and related): modern and important but boundary topology differs. `FUTURE_BOUNDARY_EXTENSION`, not strict current validation.
- RPC/geopolymer/precast/AAC/sandwich wall panels: demonstrate modern activity but use different material/section systems. `FUTURE_MATERIAL/STRUCTURAL_EXTENSION`.

## 6. Immediate acquisition ranking

```text
P0 = Shahin 2011: primary full text already available; close remaining material/imperfection inputs
P1 = Waddick & Swifte 1991: acquire original Monash report
P1 = Roongsang 1994: acquire original Monash report
P1 = Ernst 1952 full article + 1953 Nebraska Bulletin: recover specimen-level tables
P2 = modern adjacent datasets: retain for future eccentric/opening/3-side/material-extension branches
```

Current candidate ledger is stored in:

`evidence/literature/NZ_SCCM_RC_PANEL_CANDIDATE_RAW_DATA_20260813_1139.csv`

No candidate is promoted to production blind calculation until its current-contract inputs are explicitly closed.