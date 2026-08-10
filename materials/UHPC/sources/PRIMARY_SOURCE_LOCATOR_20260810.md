# UHPC primary-source locator — 2026-08-10

This file records File Library originals that are authoritative source documents but are not yet byte-exact binaries in this GitHub repository.

Evidence rule: original PDF > extracted/search mirror > evidence note > project interpretation.

| source | File Library ID | pages / identity recovered | role in project | current GitHub binary status | public locator |
|---|---|---|---|---|---|
| Hiew et al. 2024, *A unified tensile constitutive model for mono/hybrid fibre-reinforced UHPC* | `file_0000000087e882079606fbbb13dd1e2d` | 24 pages; Cement and Concrete Composites 150 (2024) 105553 | `SOURCE_EXPLICIT_UNIAXIAL`: tensile elastic -> strain-hardening -> peak -> localization -> fibre-pullout softening; 2% SL/HL/hybrid anchors | FILE_LIBRARY_ONLY | DOI `10.1016/j.cemconcomp.2024.105553`; Monash OA copy `https://research.monash.edu/files/599317955/589510091_oa.pdf` |
| Liu et al. 2024, *Experimental study on the mechanical properties of non-reinforced UHPC element under biaxial stress states* | `file_0000000012988211ab7b3fbcacf060ab` | 37-page uploaded preprint; four PBET groups: CC, TT, sequential TC, proportional TC | `SOURCE_BIAXIAL_PEAK_QUALIFICATION` for CC/TT; `PATH_DEPENDENT_VALIDATION_ONLY` for proportional/sequential TC | FILE_LIBRARY_ONLY | DOI `10.1016/j.conbuildmat.2024.139265`; SSRN `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4926706` |
| Leutbecher 2020, *Structural behavior of UHP(FR)C compression struts subjected to transverse tension and cracking* | `file_00000000df84820bb12fe27517028963` | 14 pages; 31 relevant panel tests out of 46 total | `EXTERNAL_VALIDATION`: TC strength and stiffness; crack/transverse-strain dependence | FILE_LIBRARY_ONLY | DOI `10.1002/suco.201900451`; `https://onlinelibrary.wiley.com/doi/full/10.1002/suco.201900451` |
| Leutbecher 2020 Data S1, 31 biaxial tests | `file_00000000e4a4820baf5e0f5aad438601` | uploaded supplementary PDF; exact original retained in File Library | `EXTERNAL_VALIDATION_DATA`: panel-level TC test ledger supporting source identification | FILE_LIBRARY_ONLY | Wiley supporting information linked from DOI `10.1002/suco.201900451` |
| Lee et al. 2017, *Biaxial tension-compression strength behaviour of UHPFRC in-plane elements* | `file_00000000ae4c8211812e4a9f0c2e3373` | 17 pages; 30 panel specimens, five target transverse tensile strain levels per series | `EXTERNAL_VALIDATION`: TC softening magnitude/shape and fibre effect | FILE_LIBRARY_ONLY | DOI `10.1617/s11527-016-0918-1`; `https://link.springer.com/article/10.1617/s11527-016-0918-1` |
| Shen et al. 2020, equi-biaxial tensile UHPFRC inverse analysis | `file_000000008170820baafcc59cc6a730fd` | 15 pages | `EXTERNAL_VALIDATION`: TT strain/strength ratio evidence; material/fibre system differs from project UHPC | FILE_LIBRARY_ONLY | DOI/source page `https://link.springer.com/article/10.1617/s11527-020-01553-1` |
| Diab & Ferche 2026, UHPC compression-softening synthesis | `file_00000000438882118a44003e65279d5b` | uploaded OA article | `SOURCE_SYNTHESIS_ORACLE`: smooth TC interaction synthesis; not an original two-dimensional panel campaign | FILE_LIBRARY_ONLY | DOI `10.1002/suco.70191`; author OA PDF retained in source registry |
| FHWA-HRT-23-077, *Structural Design with Ultra-High Performance Concrete* | `file_000000002fac820ba9e9f5aed3ca142e` | uploaded official report | `DESIGN_BOUNDARY`: qualification/design limits, not substitute for biaxial test evidence | FILE_LIBRARY_ONLY | `https://highways.dot.gov/sites/fhwa.dot.gov/files/FHWA-HRT-23-077.pdf` |

## Recovered source-specific anchors

### Hiew 2024 — 2% fibre rows used historically

The uploaded original contains Table 6 with the complete tensile parameter family. Historical G12 extraction retained the following 2% fibre summaries:

```text
series,Vf_percent,Et_GPa,eps_cr_percent,f_cr_MPa,eps_peak_percent,f_peak_MPa,eps_loc_percent,f_loc_MPa,eps_lim_percent
SL-2.0,2.0,47.8,0.040,10.0,0.380,11.7,0.624,9.9,0.759
HL-2.0,2.0,49.0,0.042,10.3,0.674,11.1,0.872,10.8,1.000
SL-HL-2.0,2.0,48.3,0.042,10.1,0.380,11.0,0.690,10.7,0.741
```

These are source anchors, not a permanent project parameter freeze. Project governance later retained only the user-required `fc = 141.1 MPa` as mandatory UHPC strength input; other UHPC parameters remain source-revisable.

### Liu 2024 — experimental identity

The uploaded preprint explicitly contains four test groups:

- CC proportional loading;
- TT proportional loading;
- TC sequential loading (first tension, hold tension, then increase compression);
- TC proportional loading.

The source states that TC strength is strongly affected by loading path. Therefore sequential/proportional TC rows cannot be promoted to exact identity constraints for a path-independent current map without an explicit modelling decision.

### Leutbecher 2020

The paper reports 31 relevant panel tests divided into C, FRC, RC and MRC series. For the reinforced series, transverse tensile strain is a key variable and both compressive strength and stiffness reduction are reported. This source is retained as validation evidence and as a check against over-aggressive UHPC TC interaction laws.

### Lee 2017

The uploaded source tests 30 panel specimens under sequential tension-then-compression loading. It reports substantially less compression-softening for fibre-reinforced UHPFRC than for fibre-free UHPC at high transverse tensile loading. The project uses this as an independent magnitude/shape check, not as the sole constitutive law.

### Shen 2020

The uploaded source provides equi-biaxial tensile stress/strain evidence. Historical extracted averages include approximately 59 GPa equi-biaxial elastic modulus, 9.14 MPa elastic-limit stress, 1.27% strain at end of hardening and 14.08 MPa tensile strength for that UHPFRC system. Because the material system differs, these are validation ratios/trends rather than direct project UHPC parameter identities.

## Migration boundary

None of the above File-Library-only PDFs is claimed here as a GitHub byte-exact binary. Their exact File Library IDs are retained so future ChatGPT sessions can recover the original upload. If a proper binary Git push/upload channel becomes available, the PDF itself should be copied under `sources/UHPC/` and its SHA-256 recorded without overwriting this locator history.
