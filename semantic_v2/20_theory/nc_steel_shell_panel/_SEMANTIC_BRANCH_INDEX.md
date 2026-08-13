# Concrete + steel-shell semantic branch

## Parent theory

Locked parent governance:

- `semantic_v2/10_governance/20260813_1834__NZSCCM__NC_PANEL__ENERGY_MINIMUM_HALFWAVE_R10_N48C1MM_D15_DIRECT_LIMIT__LOCKED_BASELINE.md`

The parent locks:

```text
one theoretical energy-minimum complete halfwave
D,q Nguyen second-order kinematics with membrane terms included
energy-fitted R10 concrete target
current N48-C1/MM compiler with specimen/design-dependent material interval
Cayley-Hamilton 2D lift
full directional current tangent
general-D15 exact multiple integrals
zero formal spatial quadrature
direct Rq=0,L=0 first +->- limit solve
same-branch Zhou/Navier stability check
```

## Active structural extension

- `20260813_1834__NZSCCM__NC_STEEL_SHELL_PANEL__REBAR_REPLACEMENT_GENERAL_D15__THEORY_EXTENSION_CONTRACT.md`

The extension removes the reinforcement contribution and replaces it by one or more bonded finite-thickness continuous steel-shell layers.

Structurally closed identities:

```text
P = Pc + Psh
Rq = Rq,c + Rq,sh
L = P_D Rq,q - P_q Rq,D
KZ = KZ,c + KZ,sh
```

Each steel-shell layer is integrated exactly through its own thickness coordinate; no shell Gauss points or material-point grid are introduced.

## Preliminary zero-quadrature structural validation — PASS

Validation report:

- `semantic_v2/60_validation/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__ZERO_QUADRATURE_SSSS_NAVIER_ZHOU_ABAQUS__VALIDATION.md`

Execution test:

- `semantic_v2/40_execution/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__ZERO_QUADRATURE_SSSS_EXACT_MOMENT_TEST.py`

Result table:

- `semantic_v2/50_results/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__SSSS_EXACT_VS_ABAQUS__RESULT_TABLE.csv`

The finite-thickness shell exact-moment operator was reduced to the classical four-edge simply-supported elastic Navier plate and reproduces the official Abaqus benchmark analytical value at machine roundoff:

```text
Ncr exact-moment = 90.38099268396850
Ncr classical     = 90.38099268396849
```

Therefore:

```text
FINITE_THICKNESS_SHELL_EXACT_MOMENTS = PASS
ZERO_SPATIAL_QUADRATURE = PASS
ZERO_THICKNESS_QUADRATURE = PASS
SSSS_NAVIER_ELASTIC_DEGENERATION = PASS
```

Zhou's four-edge simply-supported Navier/orthotropic architecture is compatible with this degeneration. Literal reproduction of Zhou's own numerical FE table remains pending recovery of the primary numerical table; no value is invented.

## Active steel-material derivation

- `20260813_1834__NZSCCM__STEEL_SHELL__J2_DEFORMATION_THEORY_SOURCE_CURVE_PLANE_STRESS__MATERIAL_OPERATOR_DERIVATION.md`

This derives a path-independent full 2D plane-stress current operator by lifting an approved uniaxial steel source curve through J2 deformation theory. The map reduces the multiaxial update to one scalar equivalent-stress constitutive equation, exactly recovers the uniaxial source curve, exactly degenerates to standard elastic plane stress, and provides an analytic consistent tangent by implicit differentiation.

The structural test set is not used in this derivation.

This operator remains a candidate rather than a production-frozen steel law; the zero-quadrature structural PASS above does not depend on accepting the nonlinear J2 candidate.

## Yun Lu replacement feasibility — PASS WITH BOUNDARY

Source-grounded audit:

- `20260813_1854__NZSCCM__STEEL_SHELL__YUN_LU_REPLACEMENT_ZERO_QUADRATURE__FEASIBILITY_AUDIT.md`

Current verdict:

```text
YUN_LU_ANALYTIC_ZERO_QUADRATURE = PASS
YUN_LU_AS_LOCAL_SINGLE_SIDE_SHELL_MODEL = HIGH_COMPATIBILITY
YUN_LU_AS_GLOBAL_ZHOU_SSSS_REPLACEMENT = NO
YUN_LU_AS_CONCRETE_MOTHER_THEORY_REPLACEMENT = NO
YUN_LU_AS_STEEL_MATERIAL_CONSTITUTIVE_LAW = NO
YUN_LU_LOCAL_AMPLITUDE_COUPLING = OPEN
STEEL_PLASTICITY_COMPLETION = OPEN
EXPERIMENTAL_EFFECTIVE_WIDTH_FIT = EXCLUDED
```

Yun Lu's finite cosine deflection/stress-function/Galerkin structure is intrinsically compatible with exact trigonometric moments and therefore with zero numerical spatial quadrature. Its natural role is a local PBL/design-bounded, single-side-constrained steel-wall buckling/postbuckling module. It does not replace the locked global `D,q` mother theory or the global Zhou/Navier simply-supported stability layer.

## Remaining production gates

The next production questions are now narrower:

```text
1. derive/freeze coupling of local Yun-Lu shell amplitude A_s to global D,q;
2. preserve exact finite-dimensional elimination/coupling with zero spatial quadrature;
3. close steel inelasticity beyond Yun Lu's elastic analytical source range;
4. compile the accepted steel/local-shell operator into the exact moment basis;
5. only then calculate the first concrete + steel-shell nonlinear Pu benchmark.
```

No reopening of the locked concrete theory is authorized by these steps.
