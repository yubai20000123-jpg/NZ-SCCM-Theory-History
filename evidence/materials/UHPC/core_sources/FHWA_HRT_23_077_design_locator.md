# FHWA-HRT-23-077 — UHPC design/material qualification locator

## Source identity

- file: `FHWA_HRT_23_077_UHPC_design.pdf`
- ChatGPT File Library ID: `file_000000002fac820ba9e9f5aed3ca142e`
- report: FHWA-HRT-23-077, *Structural Design with Ultra-High Performance Concrete*, October 2023.
- official locator: `https://highways.dot.gov/sites/fhwa.dot.gov/files/FHWA-HRT-23-077.pdf`
- evidence identity: `OFFICIAL_DESIGN_GUIDE / MATERIAL_PARAMETER_QUALIFICATION`

## Effective evidence retained

The guide treats UHPC tensile response using material parameters tied to direct tensile testing, including:

- modulus of elasticity `Ec`;
- effective cracking strength `ft,cr`;
- crack localisation strength `ft,loc`;
- crack localisation strain `epsilon_t,loc`.

It identifies crack localisation as the transition to tensile softening and notes that softening is associated with localisation into a principal crack and fibre pullout. It also gives typical material-property ranges and test methods. The guide permits Poisson's ratio to be determined experimentally and provides a default design assumption when not tested.

The guide's design tension models deliberately do not include post-localisation softening capacity in the strain-based structural design model. This is a **design simplification**, not evidence that the physical post-localisation material response does not exist.

## USED FOR

- official terminology and material-test/qualification boundary;
- checking plausible ranges for `Ec`, `ft,cr`, `ft,loc`, `epsilon_t,loc`, compressive strain and Poisson ratio;
- distinguishing qualification parameters from project historical parameter guesses;
- confirming the significance of crack localisation in UHPC tension.

## NOT USED FOR

- replacing Hiew direct-tension post-localisation constitutive evidence;
- replacing Liu/Lee/Leutbecher biaxial material tests;
- defining a full multiaxial material operator;
- calibrating material parameters from structural Pu.

## Current identity

`AUXILIARY_OFFICIAL_QUALIFICATION_SOURCE`
