# Liu et al. 2024 — complete planar biaxial strength and path evidence

## Source identity

- file: `Liu_2024_UHPC_biaxial_full.pdf`
- ChatGPT File Library ID: `file_0000000012988211ab7b3fbcacf060ab`
- title: *Experimental study on the mechanical properties of non-reinforced UHPC element under biaxial stress states*
- formal article identity recorded by the project: Construction and Building Materials 456 (2024) 139265; DOI `10.1016/j.conbuildmat.2024.139265`.
- SSRN preprint locator: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4926706`
- evidence identity: `PRIMARY_SOURCE / PLANAR_BIAXIAL_STRENGTH_AND_PATH`

## Effective evidence retained

The PBET program contains four categories of unreinforced UHPC planar tests:

1. biaxial compression (CC);
2. biaxial tension (TT);
3. tension-compression with sequential loading (TC-SL);
4. tension-compression with proportional loading (TC-PL).

The preprint test matrix includes three CC specimens, two TT specimens, five sequential-TC specimens and four proportional-TC specimens used in the reported conclusions.

### CC

The paper reports biaxial compression strengthening relative to uniaxial compression. The improvement is limited near the equal-compression ratio and more pronounced for unequal compression ratios. A conservative piecewise CC strength envelope combines elliptic and parabolic forms.

### TT

The measured biaxial tensile peak stress is close to the uniaxial tensile strength. Unequal biaxial tension can show apparent strengthening, but the proposed design/strength envelope conservatively takes biaxial tensile strength as the uniaxial tensile strength.

### TC and loading path

The sequential path first establishes tensile stress and associated tensile stress/strain redistribution, holds the tension, and then applies compression to failure. The proportional path develops tension and compression together. The paper reports a significant loading-path effect: the sequential path generally produces a larger loss of compression capacity and is used as the conservative controlling path for the proposed TC envelope.

The proposed TC strength envelope is piecewise: a low-compression segment controlled by tensile capacity and a descending segment toward the uniaxial compression point. The source therefore contains both **strength-interaction information** and explicit evidence that the same nominal biaxial stress quadrant cannot generally be represented without regard to loading path.

## USED FOR

- CC/TT/TC material-level strength-envelope qualification;
- testing the sign and magnitude trend of a future two-dimensional interaction kernel;
- explicit evidence that TC response/strength can be loading-path sensitive;
- independent material-level check of any current-state approximation.

## NOT USED FOR

- direct identification of a unique arbitrary-path stress-strain operator;
- replacing Hiew's direct-tension constitutive law;
- supplying crack shear transfer, unloading/reloading, or crack closure;
- multiplying the strength envelope directly into the current stress tensor without a declared constitutive derivation;
- structural Pu calibration.

## Current identity

`SOURCE_ONLY_FOR_BIAXIAL_STRENGTH_AND_PATH_QUALIFICATION / HIGH_PRIORITY`

The complete biaxial strength envelope is a failure/strength boundary. It is not by itself a complete constitutive mapping `sigma = M(epsilon,state)`.
