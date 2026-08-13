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

The extension removes the reinforcement contribution and replaces it by continuous steel-shell contributions. The parent concrete theory is unchanged.

## Preliminary zero-quadrature structural validation — PASS

Validation report:

- `semantic_v2/60_validation/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__ZERO_QUADRATURE_SSSS_NAVIER_ZHOU_ABAQUS__VALIDATION.md`

Execution test:

- `semantic_v2/40_execution/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__ZERO_QUADRATURE_SSSS_EXACT_MOMENT_TEST.py`

Result table:

- `semantic_v2/50_results/steel_shell/20260813_1854__NZSCCM__STEEL_SHELL__SSSS_EXACT_VS_ABAQUS__RESULT_TABLE.csv`

The finite-thickness shell exact-moment operator reduces to the classical four-edge simply-supported elastic Navier plate and reproduces the official Abaqus benchmark analytical value at machine roundoff:

```text
Ncr exact-moment = 90.38099268396850
Ncr classical     = 90.38099268396849

FINITE_THICKNESS_SHELL_EXACT_MOMENTS = PASS
ZERO_SPATIAL_QUADRATURE = PASS
ZERO_THICKNESS_QUADRATURE = PASS
SSSS_NAVIER_ELASTIC_DEGENERATION = PASS
```

Zhou's four-edge simply-supported Navier/orthotropic architecture is compatible with this degeneration. Literal reproduction of Zhou's own numerical FE table remains pending recovery of the primary numerical table; no value is invented.

## Yun Lu Chapter 2 exact general-D15 compilation — PASS

Current primary local-shell audit:

- `20260813_1919__NZSCCM__YUN_LU__CH2_GENERAL_D15_EXACT_COMPILATION_AND_DQ_COUPLING__THEORY_AUDIT.md`

Reproducible exact-symbolic audit:

- `semantic_v2/40_execution/steel_shell/20260813_1919__NZSCCM__YUN_LU__CH2_D15_EXACT_SYMBOLIC_AUDIT.py`

The Yun Lu Chapter 2 source chain has now been compiled directly:

```text
Eq.2-19 / 2-20 deflection + imperfection
-> Eq.2-23 Karman compatibility
-> Table 2-1 Airy coefficients
-> Eq.2-28~2-31 Galerkin
-> Eq.2-32 closed postbuckling path
-> Eq.2-35~2-37 axial stress field / first-yield event
```

Exact gates:

```text
YUN_LU_CH2_GENERAL_D15_EXACT = PASS
ONE_COMPLETE_HALFWAVE_REDUCTION = EXACT PASS
TABLE_2_1_FROM_D15 = EXACT PASS
KCRX_FROM_D15 = EXACT PASS
KP_FROM_D15 = EXACT PASS
EQ_2_32_FROM_D15 = EXACT PASS
EQ_2_37_FROM_TABLE_2_1 = EXACT PASS
MINIMUM_LOCAL_HALFWAVE_r=1 = EXACT PASS
FORMAL_SPATIAL_QUADRATURE = 0
```

With `r=ell/b=(a/b)/m`, the exact D15 reduction gives

\[
k_{crx}(r)=\frac{4(3r^4+2r^2+3)}{3r^2},
\]

and

\[
k_p(r)=\frac{272r^{16}+2856r^{14}+11273r^{12}+23146r^{10}+31506r^8+23146r^6+11273r^4+2856r^2+272}{r^2(r^2+1)^2(r^2+4)^2(4r^2+1)^2}.
\]

At `r=1`:

```text
k_crx = 32/3 = 10.666666...
k_p   = 1066/25 = 42.64
k_crx'(1)=0, k_crx''(1)=32>0
k_p'(1)=0,   k_p''(1)=75064/625>0
```

This independently recovers Yun Lu's minimum-wave statement and is fully consistent with the parent energy-minimum-halfwave governance.

### Source-internal Eq.2-36 qualification

The printed last cross-harmonic term of Yun Lu Eq.2-36 is not algebraically consistent with Table 2-1 + Eq.2-27. The unique field generated from Table 2-1 contains a `cos(2m*pi*x/a) cos(4*pi*y/b)` cross harmonic with denominator `(4a^2+b^2m^2)^2`. Yun Lu Eq.2-37 at the maximum-compression point agrees with this Table-2-1-derived form.

Therefore:

```text
TABLE_2_1 + EQ_2_27 + EQ_2_37 = internally consistent
EQ_2_36_LAST_CROSS_TERM_AS_PRINTED = SOURCE INTERNAL TYPO / INCONSISTENCY
PRODUCTION_COMPILATION = generated from Table 2-1 and cross-checked by Eq.2-37
```

The source discrepancy is documented rather than silently overwritten.

## Steel material rule for the Yun-Lu branch

Per current user instruction and Yun Lu's own Chapter 2 ultimate definition:

```text
STEEL = IDEAL ELASTIC-PERFECTLY-PLASTIC
YUN_LU_ELASTIC_LARGE_DEFLECTION_PATH = retained to first local yield
ULTIMATE/YIELD EVENT = first maximum axial compressive stress reaches fy
STRAIN_HARDENING = 0
```

The earlier J2 deformation-theory current-map remains a retained candidate/history item, but it is not required for the first Yun-Lu production branch.

No post-first-yield expanding plastic-zone theory is silently invented. If such continuation is opened later, it will require a separate analytic yield-boundary derivation.

## Global D-q analytic interface — CLOSED

A displacement-control compatibility relation has been derived from Yun Lu's same Karman field and Airy stress field, using exact D15 averaging:

\[
\varepsilon_{c,s}=\frac{p_x}{E_st_s}+\frac{3\pi^2}{\ell^2}\left(A_0A+\frac12A^2\right).
\]

For a shell longitudinal direction sharing the global axial shortening `eps0*D`:

\[
p_x^{comp}(D,A)=E_st_s\left[\varepsilon_0D-\frac{3\pi^2}{\ell^2}\left(A_0A+\frac12A^2\right)\right].
\]

The Yun-Lu Galerkin residual can be written exactly as

\[
\mathcal G_Y=\frac{3\pi^2b}{t_s\ell}(A+A_0)[p_x^Y(A)-p_x].
\]

For an analytically prescribed design-side amplitude map `A=A(q)`, the physical shell contribution becomes

\[
R_{q,sh}=\frac{3\pi^2b}{\ell}A_{,q}(A+A_0)[p_x^Y(A)-p_x^{comp}(D,A)].
\]

For multiple local shell subpanels, sum this finite analytic contribution over the subpanels. The shell axial load is

\[
P_{sh}(D,q)=\sum_i b_i p_{x,i}^{comp}(D,A_i(q)).
\]

Hence the locked two-variable global structure is preserved:

\[
P=P_c+P_{sh},\qquad R_q=R_{q,c}+R_{q,sh},
\]

\[
L=P_DR_{q,q}-P_qR_{q,D}.
\]

All derivatives are analytic; no new spatial quadrature, material-point grid, or load-history stepping is introduced.

Current status:

```text
YUN_LU_LOCAL_AMPLITUDE_COUPLING = ANALYTIC INTERFACE CLOSED
GLOBAL_GENERALIZED_COORDINATES = D,q RETAINED
IDEAL_EP_FIRST_YIELD_CAP = ACCEPTED
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = one representative complete halfwave per analytic local panel contribution
```

## Next execution gate

The next task is no longer a theoretical feasibility question. It is the first blind nonlinear `concrete + Yun-Lu steel-shell` benchmark:

```text
1. freeze the benchmark's design geometry / local PBL-bounded shell widths and initial local imperfections;
2. generate each local r, k_crx, k_p and A_i(q) mapping from design-side data only;
3. assemble Psh and Rq,sh analytically with the frozen concrete Pc and Rq,c;
4. solve Rq=0 and L=0 directly on the primary branch;
5. on that same branch compare first L=0, first KZ=0 and first local Yun-Lu yield Y_s,i=0;
6. only after theory freeze compare with an experimental or FE benchmark.
```

No reopening of the locked concrete theory is authorized by this benchmark.
