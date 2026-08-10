# Leutbecher 2020 Data S1 — individual panel numeric evidence locator

## Source identity

- file: `Leutbecher_2020_DataS1_31_biaxial_tests.pdf`
- ChatGPT File Library ID: `file_00000000e4a4820baf5e0f5aad438601`
- role: supplementary primary data for the 31 panel tests evaluated in Leutbecher 2020.
- parent paper DOI: `10.1002/suco.201900451`
- evidence identity: `PRIMARY_SUPPLEMENTARY_NUMERIC_DATA`

## Why the file is retained separately

The main paper provides interpretation/modeling; Data S1 preserves specimen-level values and stress-strain diagrams. It should be used when numerical material identification or independent reprocessing is required, rather than fitting to figures reproduced in later papers.

## Example source records confirming the data structure

### Panel RC1-1 — no fibres, uniaxial compression reference

- fibre content: none;
- applied tensile strain: none;
- maximum panel compressive stress `sigma_2,min = -131.1 MPa`;
- concrete compressive stress `sigma_c2,min = -125.7 MPa`;
- peak compressive strain `epsilon_2,min = -3.04 per mille`;
- accompanying cylinder mean `fc,cyl = 135.8 MPa`, `Ec,cyl = 42,246 MPa`.

### Panel MRC2-5 — fibre+bar TC example

- fibre content `rho_f = 1.0% by volume`;
- applied transverse tensile strain `epsilon_1,max = 2.54 per mille`;
- nominal maximum tensile stress `sigma_1,max = 11.40 MPa`;
- maximum panel compressive stress `sigma_2,min = -132.1 MPa`;
- concrete compressive stress `sigma_c2,min = -125.4 MPa`;
- peak compressive strain `epsilon_2,min = -3.85 per mille`;
- accompanying cylinder mean `fc,cyl = 163.4 MPa`, `Ec,cyl = 44,565 MPa`.

The complete 31-record supplementary file remains the authoritative numerical source. These examples are stored only to make the available variables and units immediately visible during future recovery.

## USED FOR

- specimen-level TC material identification;
- direct re-evaluation of transverse-strain versus compression-strength/stiffness reduction;
- separating fibre, bar and plain-UHPC series;
- future material-level regression/qualification where justified.

## NOT USED FOR

- replacing the complete Data S1 file with these two examples;
- structural Pu calibration;
- claiming all 31 tests have identical material/fibre configuration;
- general arbitrary-path closure without an explicit constitutive framework.

## Current identity

`PRIMARY_NUMERIC_DATA_LOCATOR / HIGH_PRIORITY_WHEN_PARAMETER_IDENTIFICATION_IS_REOPENED`
