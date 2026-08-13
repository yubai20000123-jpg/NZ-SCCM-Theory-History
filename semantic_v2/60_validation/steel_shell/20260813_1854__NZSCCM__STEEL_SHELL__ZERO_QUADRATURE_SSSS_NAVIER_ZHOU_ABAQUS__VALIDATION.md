# NZ-SCCM steel shell — zero-quadrature SSSS Navier / Zhou architecture / Abaqus benchmark validation

**Timestamp:** 2026-08-13 18:54 +08:00  
**Identity:** PRELIMINARY STRUCTURAL VALIDATION / ELASTIC-TANGENT DEGENERATION  
**Parent theory:** `20260813_1834__NZSCCM__NC_PANEL__ENERGY_MINIMUM_HALFWAVE_R10_N48C1MM_D15_DIRECT_LIMIT__LOCKED_BASELINE.md`  
**Steel-shell extension:** `20260813_1834__NZSCCM__NC_STEEL_SHELL_PANEL__REBAR_REPLACEMENT_GENERAL_D15__THEORY_EXTENSION_CONTRACT.md`  
**Structural calibration:** NO  
**Formal spatial quadrature:** ZERO

---

## 0. Question and scope

This gate asks only the first implementation question:

> Can the reinforcement contribution be replaced by a bonded finite-thickness continuous steel shell while retaining a complete-halfwave analytical calculation with zero numerical spatial integration, and does the resulting shell stability operator actually calculate through to a known benchmark?

This gate does **not** yet claim a nonlinear steel-shell ultimate-load production solution. It isolates the steel-shell geometry/integration/stability layer using an exactly known elastic plane-stress degeneration.

---

## 1. Zhou four-edge simply-supported architecture

The project source/equation register identifies Zhou Siming's four-edge simply-supported Navier framework in Chapter 5, with orthotropic directional stiffnesses and candidate `(m,n)` Navier modes. Zhou's published work on multi-celled CFST walls likewise uses a four-edge simply-supported global-buckling model, an orthotropic plate analytical formulation and refined FE eigenvalue calculations for comparison.

The Zhou source architecture therefore supplies the correct benchmark **type**:

```text
four-edge simply supported
+ Navier sine halfwaves
+ directional plate stiffness
+ eigenvalue/critical-load comparison
```

However, the exact primary Zhou dissertation numerical FE benchmark table is not presently recovered in the repository. Therefore no Zhou numerical value is invented here. Literal reproduction of Zhou's own FE table remains pending primary-table recovery.

For a numerical comparison in this gate, the official Abaqus/Standard verification problem `Buckling of a simply supported square plate` is used because it gives the exact same clean four-edge simply-supported elastic plate degeneration and publishes both the analytical critical load and multiple FE element results.

---

## 2. Finite-thickness steel shell without thickness points

Take one steel shell layer of thickness `t`, with local thickness coordinate

\[
z=\frac{t}{2}\eta,\qquad \eta\in[-1,1].
\]

For one complete simply-supported Navier halfwave

\[
\varphi=\sin X\sin Y,
\qquad
X=\frac{\pi x}{b},
\qquad
Y=\frac{\pi y}{\ell},
\]

and

\[
\alpha=\frac{\pi}{b},\qquad
\beta=\frac{\pi}{\ell}.
\]

The shell bending perturbation strain operator is

\[
\mathbf b_\varphi=-z
\begin{bmatrix}
\varphi_{,xx}\\
\varphi_{,yy}\\
2\varphi_{,xy}
\end{bmatrix}.
\]

For isotropic elastic plane-stress steel,

\[
\mathbf C_s=
\frac{E_s}{1-\nu_s^2}
\begin{bmatrix}
1&\nu_s&0\\
\nu_s&1&0\\
0&0&(1-\nu_s)/2
\end{bmatrix}.
\]

All integrands are finite products of `sin`, `cos` and `eta^2`. No spatial or thickness quadrature is required.

The only moments needed for this degeneration are

\[
\int_0^\pi\sin^2X\,dX=\frac\pi2,
\qquad
\int_0^\pi\cos^2X\,dX=\frac\pi2,
\qquad
\int_{-1}^{1}\eta^2\,d\eta=\frac23.
\]

These are a direct subset of `general-D15` exact moments.

---

## 3. Exact material and geometric stability terms

Define the classical steel plate bending rigidity

\[
\boxed{D_s=\frac{E_st^3}{12(1-\nu_s^2)}}.
\]

Exact integration gives

\[
\boxed{
K_{Z,sh}^{mat}
=\frac{D_sb\ell}{4}(\alpha^2+\beta^2)^2
}.
\]

For a uniform compressive membrane force `N_y>0` in the loading direction,

\[
\boxed{
K_{Z,sh}^{geo}
=-\frac{N_yb\ell}{4}\beta^2
}.
\]

Therefore

\[
K_Z=K_{Z,sh}^{mat}+K_{Z,sh}^{geo}=0
\]

gives

\[
\boxed{
N_{y,cr}
=D_s\frac{(\alpha^2+\beta^2)^2}{\beta^2}
}.
\]

Equivalently,

\[
\boxed{
N_{y,cr}
=\frac{\pi^2D_s}{b^2}
\left(\frac{\ell}{b}+\frac{b}{\ell}\right)^2
}.
\]

For the square complete halfwave `ell=b`,

\[
\boxed{N_{cr}=\frac{4\pi^2D_s}{b^2}},
\]

which is exactly the classical four-edge simply-supported square-plate result.

This establishes an algebraic degeneration from the finite-thickness shell `K_Z` operator back to the classical Navier plate without introducing any structural integration points.

---

## 4. Official Abaqus simply-supported square-plate benchmark

Official benchmark inputs:

```text
b = ell = 2
thickness t = 0.01
E = 1.0e8
nu = 0.3
four edges simply supported
uniform in-plane compression
```

The exact rigidity is

\[
D_s=9.157509157509159.
\]

The exact critical membrane force is

\[
\boxed{N_{cr}^{exact}=90.38099268396849}.
\]

The present exact-moment shell evaluator gives

```text
Kmat = +223.00616079213015
Kgeo/N = -2.4674011002723395
KZ=0 -> Ncr = 90.38099268396850
```

Difference from the classical closed form is at machine roundoff.

The published Abaqus FE results are:

| element/mesh | FE critical load | error vs exact |
|---|---:|---:|
| S8R5, 2x2 | 90.52 | +0.154% |
| S8R, 2x2 | 95.32 | +5.465% |
| S9R5, 2x2 | 90.52 | +0.154% |
| STRI65, 2x2 | 89.64 | -0.820% |
| STRI3, 4x4 | 90.47 | +0.098% |
| S3R, 4x4 | 115.92 | +28.257% |
| S4R, 4x4 | 92.80 | +2.676% |
| S4R5, 4x4 | 92.76 | +2.632% |
| S4, 4x4 | 92.35 | +2.179% |

The zero-quadrature shell result is not merely close to the FE values: it reproduces the analytical benchmark exactly, while the FE deviations are the expected discretization/element effects. Abaqus itself notes that the S3R result is excessively stiff in this example.

---

## 5. Halfwave-energy/minimum check

For the same plate, let `r=ell/b`. Then

\[
k(r)=\left(r+\frac1r\right)^2.
\]

Selected values are:

| ell/b | k | Ncr |
|---:|---:|---:|
| 0.50 | 6.250000 | 141.220301 |
| 0.75 | 4.340278 | 98.069654 |
| 1.00 | 4.000000 | 90.380993 |
| 1.25 | 4.202500 | 94.956530 |
| 1.50 | 4.694444 | 106.072137 |
| 2.00 | 6.250000 | 141.220301 |

Thus the square complete halfwave is the minimum for this classical SSSS plate. This is consistent with the locked project rule that the production halfwave is selected from the theoretical energy/minimum family, not from a later observed experimental bulge.

---

## 6. What this proves for rebar -> steel-shell replacement

The reinforcement module was lower-dimensional in thickness. Replacing it by a finite-thickness shell adds the shell thickness coordinate `eta`, but **does not force numerical integration**. The added coordinate is integrated analytically by the same moment operator.

At the structural/operator level, the following chain is now demonstrated to calculate through:

```text
finite-thickness shell
-> same complete-halfwave trigonometric field
-> plane-stress stress/tangent
-> exact thickness + x + y moments
-> KZ,sh^mat + KZ,sh^geo
-> exact critical root
```

The same closure applies to `P_sh` and `R_q,sh` whenever the steel current map has been compiled into a finite analytic basis, because their integrands have the same finite trigonometric-thickness algebraic form.

---

## 7. Gate verdict

```text
FINITE_THICKNESS_STEEL_SHELL_EXACT_MOMENTS = PASS
ZERO_NUMERICAL_SPATIAL_QUADRATURE = PASS
ZERO_NUMERICAL_THICKNESS_QUADRATURE = PASS
SSSS_NAVIER_ELASTIC_DEGENERATION = PASS
OFFICIAL_ABAQUS_BENCHMARK = PASS
ZHOU_FOUR_EDGE_SSSS_ARCHITECTURE_COMPATIBILITY = PASS
ZHOU_LITERAL_NUMERICAL_FE_TABLE_REPRODUCTION = PENDING_PRIMARY_TABLE_RECOVERY
FULL_NONLINEAR_STEEL_CURRENT_MAP_COMPILER = PENDING
FULL_CONCRETE_PLUS_STEEL_SHELL_Pu = NOT_YET_PRODUCTION
```

The important first question is therefore answered positively: **steel shell itself does not break the zero-spatial-quadrature analytical architecture.** The remaining nonlinear production gate is material compilation/current-map closure, not spatial integration.
