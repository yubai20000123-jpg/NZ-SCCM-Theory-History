# NZ-SCCM — FHWA UHPC compression design-model vs physical-terminal role gate R13

**Date:** 2026-08-24 11:51 +08:00  
**Status:** `SOURCE_ROLE_AUDIT_COMPLETE / FHWA_DESIGN_MODEL_RETAINED / PHYSICAL_PREDICTION_ROLE_REJECTED / ZHANG_PHYSICAL_REINSERTION_AUTHORIZED`

## 0. Scope and locked architecture

R13 does not reopen the structural theory. It audits only the role assigned to the FHWA `alpha_u=0.85` compression model used in R10–R12.

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
Nx_Mx_IN_STRUCTURAL_FIELD = YES
Nx_Mx_HARD_TERMINAL_ON_Y_CUT = NO
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
```

The question is not whether the FHWA model is valid. It is whether it should be treated as the **physical peak-response material terminal** when the project compares predictions against nonlinear Abaqus/test peak loads.

---

## 1. Official FHWA source identity

Primary source:

- FHWA-HRT-23-077, *Structural Design with Ultra-High Performance Concrete*, October 2023;
- official report: `https://highways.dot.gov/sites/fhwa.dot.gov/files/FHWA-HRT-23-077.pdf`.

The report explicitly presents a potential structural **design** framework. Appendix A Article 1.4 states that UHPC material properties and idealized stress–strain behaviors are for use in design.

For compression:

1. `f'_c` is the compressive strength **for use in design** and is established from physical cylinder tests.
2. `epsilon_cu` is the ultimate compressive strain **for use in design**; without physical test data the guide supplies a default rule.
3. `alpha_u` is explicitly defined as a reduction factor accounting for nonlinearity of the UHPC compressive stress–strain response and shall not exceed `0.85`.
4. The commentary states that the recommended `alpha_u` corresponds approximately to the stress at which the initial elastic response of the tested UHPC products has deviated by not more than about 10% from linearity.
5. Article 1.4.2.4.3 is explicitly titled **Compression Design Model**. The idealization is elastic to `alpha_u f'_c`, then sustains that reduced resistance until `epsilon_cu` so that compressive strain capacity can be used in design.
6. Appendix B then uses this idealized model for a strain-compatibility design example.

Thus `alpha_u=0.85` is source-faithful as a design reduction/idealization. It is not identified by FHWA as the actual measured peak stress of a specific UHPC mixture, nor is the elastic-to-plateau diagram presented as a full physical pre-/post-peak constitutive reconstruction of that mixture.

---

## 2. Consequence for the project role assignment

R10–R12 used

\[
\sigma_c^{FHWA}(\varepsilon)=
\operatorname{clip}(E_c\varepsilon,0,0.85 f_c)
\]

with

\[
\varepsilon_{cu}=0.0035.
\]

That is a correct implementation of the FHWA **design compression idealization** under the project strain-compatible section framework.

However, the current comparator target is not a factored design resistance. It is the peak structural response from nonlinear Abaqus/test-type physical comparison. Therefore the following role assignment is not justified:

```text
FHWA_085_DESIGN_IDEALIZATION == UNIQUE_PHYSICAL_UHPC_PEAK_CONSTITUTIVE_LAW
```

R11/R12 made that role too strong. Their low bias is consistent with introducing a deliberately reduced design plateau into a physical-response comparison.

This does **not** mean that the numerical agreement itself is used to reject the FHWA model. The role decision follows from the source identity; the R11/R12 comparator trend is only a consistency check after the source audit.

---

## 3. Zhang 2023 source role already available in the project

The project D16 source register and the 2026-08-22 material gate already retain the Zhang et al. 2023 active-confinement/full-process UHPC compression law.

At zero confinement, with

\[
x=\varepsilon_c/\varepsilon_{c0},
\qquad
f_c=141.1\ \mathrm{MPa},
\qquad
E_c=43.4\ \mathrm{GPa},
\qquad
\varepsilon_{c0}=0.0035,
\qquad
V_f=0.02,
\]

the ascending branch is

\[
\boxed{
 g_a(x)=\frac{r x}{r-1+x^r},
 \qquad
 r=\frac{E_c}{E_c-f_c/\varepsilon_{c0}},
 \qquad 0\le x\le1.
}
\]

It satisfies

\[
g_a(0)=0,
\qquad
\frac{d\sigma}{d\varepsilon}\bigg|_0=E_c,
\qquad
g_a(1)=1,
\qquad g_a'(1)=0.
\]

The source-retained descending branch is

\[
 g_d(x)=0.18+\frac{0.82}{1+\frac23(x-1)^2},
 \qquad x\ge1.
\]

The 2026-08-22 gate already proved that the ascending branch has finite hypergeometric endpoint primitives and the descending branch has elementary `atan/log` primitives, so zero thickness quadrature is preserved.

---

## 4. Mainline terminal interpretation for direct R14 comparison

The current mainline has

```text
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
```

Therefore R14 shall make the **minimum direct change** from R11/R12:

- same plane-section strain compatibility;
- same `Ny-My` terminal;
- same steel laws/caps;
- same finite control-location audit;
- replace only the FHWA compression-design plateau by the Zhang physical ascending backbone;
- anchor the extreme compression fibre at the Zhang uniaxial peak strain

\[
\boxed{\varepsilon_{top}=\varepsilon_{c0}=0.0035.}
\]

This is the first-attainment-of-material-peak terminal and is the direct physical analogue of the R11 `epsilon_cu=0.0035` terminal.

The Zhang post-peak branch is retained as source evidence, but it is **not** used to extend the mainline capacity beyond first peak in R14. Doing so would create a different post-peak continuation/fold problem and would require an explicit path/continuation governance decision. It must not be silently mixed into the no-load-path terminal.

---

## 5. R13 decision

```text
FHWA_HRT_23_077_SOURCE_IDENTITY = OFFICIAL_STRUCTURAL_DESIGN_GUIDE
FHWA_ALPHA_U_085 = SOURCE_SUPPORTED_DESIGN_NONLINEARITY_REDUCTION
FHWA_COMPRESSION_MODEL = SOURCE_FAITHFUL_DESIGN_IDEALIZATION
FHWA_R11_R12_AS_DESIGN_BASELINE = RETAIN
FHWA_R11_R12_AS_UNIQUE_PHYSICAL_PEAK_TERMINAL = REJECT

ZHANG_2023_UNIAXIAL_COMPRESSION_SOURCE = RETAIN
ZHANG_PEAK_ANCHORED_STRAIN_COMPATIBLE_Ny_My = AUTHORIZED_NEXT
ZHANG_POSTPEAK_CONTINUATION = SOURCE_RETAINED / OFF_MAINLINE_UNTIL_SEPARATE_GATE

STRUCTURAL_FRONT_REOPEN = NO
Ny_My_TERMINAL_REOPEN = NO
TC_SOFTENING_INSERT_NOW = NO
NEW_FITTED_FACTOR = NO

NEXT = R14_ZHANG_PEAK_ANCHORED_EXACT_STRAIN_COMPATIBLE_Ny_My
```

R13 therefore authorizes a direct R14 rerun. The result must be judged only after all roots are fixed; comparator loads remain excluded from parameter selection and root selection.
