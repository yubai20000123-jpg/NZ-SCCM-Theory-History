# Leutbecher 2020 — TC compressive strength and stiffness evidence

## Source identity

- file: `Leutbecher_2020_UHPFRC_TC.pdf`
- ChatGPT File Library ID: `file_00000000df84820bb12fe27517028963`
- supplementary data file registered separately: `Leutbecher_2020_DataS1_31_biaxial_tests.pdf`, File Library ID `file_00000000e4a4820baf5e0f5aad438601`
- paper: Torsten Leutbecher, *Structural behavior of ultra-high performance (fiber-reinforced) concrete compression struts subjected to transverse tension and cracking*, Structural Concrete 21 (2020) 2154–2167.
- DOI: `10.1002/suco.201900451`
- evidence identity: `PRIMARY_SOURCE / TC_STRENGTH_STIFFNESS_MODEL_EVIDENCE`

## Effective evidence retained

The paper re-evaluates biaxial UHP(FR)C panel tests to quantify not only compressive-strength reduction under transverse tension/cracking, but also reduction of compressive stiffness. This distinction is important because a constitutive operator needs more than a peak-strength envelope.

The reported program contains 46 total panel tests, of which 31 are treated as relevant for compression-strut strength/stiffness evaluation. The relevant specimens include plain UHPC, fibre-only UHPFRC, bar-reinforced UHPC, and combined bar+fibre UHPFRC series.

For the fibre-containing series reported in the article, the steel fibres are smooth straight fibres with approximately:

- length `17 mm`;
- diameter `0.15 mm`;
- tensile strength about `2500 MPa`;
- fibre volume fraction `1.0%`.

The source conclusions/evidence emphasize:

- transverse tension and cracks parallel to compression reduce compressive strength;
- a pronounced reduction is already visible at small transverse tensile strain/crack width;
- the reduction tends to stabilize at larger tensile strain;
- compressive stiffness also decreases;
- UHPFRC generally shows less reduction in strength and stiffness than plain UHPC;
- a stress–strain modeling proposal is developed from the evaluated panel data.

## USED FOR

- TC compression-strength reduction evidence;
- TC compressive-stiffness/tangent qualification;
- material-level comparison between fibre and non-fibre UHPC;
- identifying whether a future compact TC law captures the early reduction and later stabilization trend;
- Data S1 as a high-value source of individual panel data when numerical identification is needed.

## NOT USED FOR

- direct parameter transfer to 2%-fibre UHPC without material qualification;
- full tensile-direction stress, crack-shear, unloading/reloading or general path closure;
- complete CC/TT/C3 law;
- structural Pu calibration.

## Current identity

`SOURCE_ONLY / HIGH_PRIORITY_TC_STRENGTH_AND_STIFFNESS`

This source is more informative than a strength envelope alone because it constrains both strength and stiffness, but it still does not by itself close the full two-dimensional material state/update problem.
