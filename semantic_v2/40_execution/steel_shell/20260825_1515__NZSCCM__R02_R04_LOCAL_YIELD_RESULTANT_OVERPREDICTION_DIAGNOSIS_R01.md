# NZ-SCCM — R02/R04 severe-local-buckling steel-face resultant overprediction diagnosis R01

**Time:** 2026-08-25 15:15 +08:00  
**Parent:** `current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`  
**Applied state:** `current/SSUHPC_CURRENT_STATE_20260825.md`  
**Status:** `ROOT CAUSE IDENTIFIED / NO PRODUCTION REPAIR YET`

---

# 0. Question

After the milestone-derived SSUHPC seven-case blind calculation, the positive error rises strongly in the cases whose steel face locally buckles before yield. This audit asks only:

> Why can the current R02 -> R04 chain still overestimate the complete steel-face terminal resultants after severe local buckling, while retaining R02 source identity and prohibiting effective width/area?

This audit does **not** modify Marguerre–Airy, UHPC N-M, web mechanics, R03 status, or any comparator-independent root already fixed.

---

# 1. Yun source role: mean postbuckling path is not the ultimate criterion

Yun's Eq. (2-32) gives the postbuckling **average applied pressure / mean axial stress path** as a function of local buckling amplitude. It is the mean resultant path, not a statement that the full-area mean stress may rise to `fy`.

Yun then reconstructs the nonuniform in-plane axial stress field from the Airy stress function, locates the maximum axial compression, and defines the plate ultimate when that **local maximum axial stress** first reaches `fy`. The corresponding ultimate mean stress is Eq. (2-40), i.e. the full-section average stress evaluated at that local-yield amplitude.

Therefore the source sequence is

```text
postbuckling amplitude
-> nonuniform local membrane stress field
-> first local maximum stress reaches fy
-> mean/resultant capacity at that same amplitude
```

not

```text
postbuckling amplitude
-> full-area mean stress
-> mean stress itself reaches fy
```

Yun also reports that the ultimate-stress discrepancy changes strongly with `b/t`, reaching 28.6% at large `b/t`, and that material plasticity changes ultimate strength mainly for `b/t < 70`; for `b/t > 70` the elastic and elastoplastic FEM ultimate stresses are essentially unchanged. This is directly relevant to T360 (`b/t=90`), BH032 (`b/t=80`) and BH050 (`b/t=125`).

---

# 2. Current R02 already contains both quantities, but the terminal uses the wrong one for yielding

The current R02 implementation is internally richer than the terminal chain currently uses.

It contains:

1. `mean_compression_stress(...)`: full-area mean postbuckling membrane stress;
2. `airy_fluctuation_tension(...)`: exact finite-harmonic local membrane-stress fluctuation;
3. `local_mises(...)`: pointwise diagnostic assembled from mean + local fluctuation (+ optional local bending diagnostic).

However, `face_resultants(...)` returns

\[
\mathbf N_f=t_s\,\bar{\boldsymbol\sigma}_{R02},
\]

using only the **mean** R02 stress. R04 is then applied to that mean stress vector:

\[
\lambda_p=\min\left(1,\frac{f_y}{\sigma_{VM}(\bar{\boldsymbol\sigma}_{R02})}\right).
\]

Thus the current terminal strength check is effectively

\[
\boxed{\sigma_{VM}(\text{mean stress})=f_y}
\]

while the source-local postbuckling mechanism says local stress peaks arise before the mean reaches that level.

This is the semantic loss:

\[
\boxed{
\text{R02 retains local stress redistribution, but R04 discards it before the yield/capacity check.}
}
\]

---

# 3. T360 direct diagnostic at the already-fixed current root

Canonical current T360 terminal state:

```text
Bs = 360 mm
ts = 4 mm
local Ly = 375 mm
A0 = 0.225 mm
fy = 355 MPa
U_top = 0.775204046541 mm
U_bottom = 2.866479922145 mm
```

Current R02 mean trial stresses:

upper face:

\[
(\bar\sigma_x,\bar\sigma_y)^{tr}_+
=(+84.8810,-297.3045)\ \mathrm{MPa},
\]

with mean Mises

\[
\sigma_{VM}^{mean,+}=347.6065\ \mathrm{MPa}<355\ \mathrm{MPa}.
\]

Therefore current R04 leaves the upper face unscaled.

lower face:

\[
(\bar\sigma_x,\bar\sigma_y)^{tr}_-
=(-87.5898,-587.7396)\ \mathrm{MPa},
\]

current R04 gives

\[
\lambda_-=0.64638493,
\]

and final mean stress

\[
(\bar\sigma_x,\bar\sigma_y)_-
=(-56.6167,-379.9060)\ \mathrm{MPa},
\]

whose **mean** Mises is exactly 355 MPa.

## 3.1 Reinsert the R02 finite-harmonic local membrane fluctuation

Using the R02 local membrane field that is already present in the source-derived operator, the same fixed terminal state gives approximately:

upper face:

\[
\boxed{\max_{\Omega}\sigma_{VM}^{local,mem}\approx374.58\ \mathrm{MPa}>355\ \mathrm{MPa}}
\]

even though the mean Mises is only 347.61 MPa.

lower face:

\[
\boxed{\max_{\Omega}\sigma_{VM}^{local,mem}\approx919.89\ \mathrm{MPa}}
\]

before R04 mean-stress scaling.

The maximum local axial compression on the lower face is about

\[
|\sigma_y|_{max}\approx865\ \mathrm{MPa}.
\]

Therefore the current T360 root is already far beyond first local yielding according to the very same R02 postbuckling stress field.

This is not a new material model and not an effective-width argument. It is a direct consistency audit between two existing outputs of R02.

---

# 4. Proportional-strain diagnostic: how early does local yielding begin?

As a **diagnostic only**, scale each fixed terminal face strain vector proportionally from the origin and, at every scale, solve the same R02 cubic. Then identify the first scale at which the R02 local membrane Mises reaches 355 MPa.

This proportional continuation is not promoted to production root selection; it is used only to quantify the semantic gap.

Upper T360 face:

\[
\eta_{y,+}\approx0.951635,
\qquad U\approx0.733832\ \mathrm{mm},
\]

with mean R02 stress at first local yield approximately

\[
(\bar\sigma_x,\bar\sigma_y)
\approx(+79.59,-284.06)\ \mathrm{MPa}.
\]

Lower T360 face:

\[
\eta_{y,-}\approx0.419237,
\qquad U\approx1.59139\ \mathrm{mm},
\]

with mean R02 stress at first local yield approximately

\[
(\bar\sigma_x,\bar\sigma_y)
\approx(-67.80,-276.15)\ \mathrm{MPa}.
\]

Hence the lower face enters local yielding at only about 42% of the current terminal face-strain magnitude, long before the current R04 mean-Mises cap is reached.

---

# 5. Independent Yun scalar check for the T360 local cell

For the T360 local cell (`b=360 mm`, local axial halfwave length `375 mm`, `A0=0.225 mm`), Yun/R02 source coefficients are

\[
k_{cr}=10.69334444,
\qquad k_p=42.74014833.
\]

Using Yun's own sequence — postbuckling mean path plus first local maximum axial stress reaching `fy` — the scalar uniaxial source calculation gives approximately

\[
\boxed{\bar\sigma_{u,Yun}\approx297.87\ \mathrm{MPa}.}
\]

This is consistent with the historical T360 Yun-source value near 302 MPa.

By contrast the current lower-face R04 terminal retains an axial mean magnitude

\[
|\bar\sigma_y|=379.91\ \mathrm{MPa}.
\]

Thus the current mean-stress terminal is roughly 27.5% higher than the source-local-yield average scale for this slender local panel.

This does not by itself define the corrected composite-member Pu, because the full terminal is biaxial and other phases can redistribute. It does identify the direction and size of the steel-face overcapacity.

---

# 6. Seven-case correlation after the milestone-derived blind run

Use local steel critical stress only as an independent stability severity indicator; no comparator entered the blind solution.

Current post-check errors:

```text
T120   +1.0393%   sigma_cr = 2206.635 MPa
T360  +11.0655%   sigma_cr =  245.795 MPa
BH005  +4.5221%   sigma_cr =10044.967 MPa
BH010  +6.4836%   sigma_cr = 2511.242 MPa
BH020  +6.8732%   sigma_cr =  627.810 MPa
BH032 +12.3959%   sigma_cr =  245.238 MPa
BH050 +28.4602%   sigma_cr =  100.450 MPa  [lower-confidence comparator]
```

Diagnostic correlations:

\[
\mathrm{corr}(b/t,\,error)\approx0.897
\]

for all seven, and about 0.840 for the primary six.

More directly,

\[
\mathrm{corr}(1/\sigma_{cr},\,error)\approx0.976
\]

for all seven, and about 0.893 for the primary six.

These correlations are not a calibration law. They are only evidence that the remaining bias follows local-shell severity much more strongly than the UHPC material replacement.

---

# 7. Root-cause verdict

The primary current defect is now specific:

\[
\boxed{
R02\ \text{postbuckling redistribution is source-consistent at the elastic field level,}
}
\]

but

\[
\boxed{
R04\ \text{is applied to the R02 full-area mean stress after the local stress field has been homogenized.}
}
\]

Therefore current `R02 -> R04` can permit the face to keep increasing its full-area resultants even after the R02 local stress field has already crossed first yield by a large margin.

This is exactly the mechanism expected to become more severe as local `b/t` increases.

The issue is **not** that local buckling is absent from R02. The issue is that local buckling-induced stress concentration is not retained in the terminal plastic/resultant cap.

---

# 8. Source-consistent next operator concept — R06, not yet production

The next operator should keep all of R02 and avoid effective width.

For a steel face define local harmonic coordinates

\[
u=\cos(k_xx),\qquad v=\cos(k_yy).
\]

Because the R02 membrane fluctuation contains only the finite harmonics `(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)`, the normal stresses are finite polynomials in `(u,v)`. The shear fluctuation has the form

\[
\tau=\sqrt{1-u^2}\sqrt{1-v^2}\,P_\tau(u,v),
\]

so

\[
\Phi(u,v)=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau^2
\]

is a finite polynomial on

\[
(u,v)\in[-1,1]^2.
\]

Thus

\[
\max_\Omega \sigma_{VM}
=\sqrt{\max_{[-1,1]^2}\Phi(u,v)}
\]

can be obtained from a finite algebraic candidate set:

1. interior roots `dPhi/du = dPhi/dv = 0`;
2. four edge stationary-root families;
3. four corners.

Therefore the local-yield check can be formalized with

```text
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
```

and without an effective width.

Candidate R06 face rule:

```text
R02 amplitude and finite harmonic local field
-> exact finite local-yield admissibility max(Phi) <= fy^2
-> face full-area mean resultant evaluated at the admissible local-yield boundary
-> only then any source-justified plastic reserve rule
```

For slender panels where Yun shows negligible plastic reserve (`b/t > 70`), the first-local-yield resultant is a source-supported terminal candidate. For stockier/yield-first panels, the current R04/other material-plastic branch must not be replaced blindly.

---

# 9. Current decision boundary

This audit does **not** yet replace R04 in production and does not change the seven blind Pu values. Before promotion, R06 must pass:

1. finite algebraic extrema implementation with no spatial grid;
2. x<->y symmetry;
3. zero-buckling degeneration to the current R04 uniaxial/2D material limit;
4. T360 and BH032 blind rerun without comparator use;
5. stocky T120/BH005/BH010/BH020 non-regression;
6. only then reopen Abaqus comparisons.

Current status:

```text
R02_SOURCE_IDENTITY = RETAIN
EFFECTIVE_WIDTH = PROHIBITED
PRIMARY_OVERPREDICTION_CAUSE = MEAN-STRESS PLASTIC CAP AFTER LOCAL-FIELD HOMOGENIZATION
T360_DIRECT_EVIDENCE = PASS
R06_LOCAL_YIELD_RESULTANT_GATE = CONCEPT_CLOSED / PRODUCTION_NOT_YET_PROMOTED
CURRENT_SEVEN_CASE_Pu = UNCHANGED_PENDING_R06_GATE
```
