# NZ-SCCM — Strict Hard Admissibility Audit for Swartz Case1/2 and Z6

**Time:** 2026-08-22 00:15 +08:00  
**Status:** `EXECUTED / STRICT_LITERAL_GATE_AUDIT / PREVIOUS_Z6_FINAL_STATUS_DOWNGRADED`

## 0. Why this audit exists

The previous UMCG executions used the frozen current material maps and section equilibrium, but did not consistently retain the Nguyen/Foster concrete failure-envelope inequalities as hard admissibility conditions at every current-map state.

This audit therefore executes the literal rule

\[
\boxed{\sigma=\mathcal M(\varepsilon),\qquad F_{CC}\le0,\ F_{TC}\le0,\ F_{TT}\le0,\ F_{VM}^{steel}\le0}
\]

without introducing any new projection/capping constitutive law and without using experiment/Zhou/Winter in the root solution.

A current-map equilibrium state is admissible only while all hard inequalities are satisfied. Under this literal interpretation, the first contact with a hard concrete envelope is the end of the admissible current-map branch **unless a separate source-grounded post-envelope branch is supplied**.

This is intentionally stricter than the earlier current-map section-fold calculation.

## 1. Concrete hard surfaces

The ordinary-concrete hard surfaces are taken from Nguyen Ch.3 / Appendix-B `stmoduc`, which uses a modified Kupfer/Foster envelope.

Let the ordered principal stresses be

\[
\sigma_1\ge\sigma_2,
\]

with tension positive and compression negative.

### 1.1 CC

For \(\sigma_1<0\), define

\[
\alpha=\frac{\sigma_1}{\sigma_2}>0.
\]

The compression-compression peak is

\[
\sigma_{2p}
=
- f_c\frac{1+3.65\alpha}{(1+\alpha)^2},
\qquad
\sigma_{1p}=\alpha\sigma_{2p}.
\]

Admissibility requires the current compression state not to exceed that envelope.

### 1.2 TC

For \(\sigma_1\ge0>\sigma_2\),

\[
\alpha=\frac{\sigma_1}{\sigma_2}<0.
\]

With \(f_c^s=-f_c\), Nguyen Appendix-B evaluates the tensile peak as

\[
\sigma_{1p}
=
\begin{cases}
\dfrac{f_c^s\alpha}{\alpha f_c^s/f_t+0.5},
&\alpha\le0.75f_t/f_c^s,\\[8pt]
\dfrac{3f_c^s\alpha}{\alpha f_c^s/f_t+3},
&\alpha>0.75f_t/f_c^s,
\end{cases}
\]

and the compressive peak as

\[
\sigma_{2p}
=
\begin{cases}
 f_c^s\dfrac{1-3.28\alpha}{(1-\alpha)^2},&\alpha>-0.2,\\[8pt]
0.5375f_c^s,&\alpha\le-0.2.
\end{cases}
\]

The literal hard conditions are

\[
\sigma_1\le\sigma_{1p},
\qquad
\sigma_2\ge\sigma_{2p}.
\]

### 1.3 TT

For \(\sigma_2\ge0\), the Appendix-B peak envelope returns

\[
\sigma_{1p}=\sigma_{2p}=f_t.
\]

### 1.4 Steel

Two-dimensional steel faces retain the existing plane-stress von-Mises radial-cap current law, so

\[
\sigma_{VM}\le f_y
\]

is already enforced by the current steel map. One-dimensional rebars/webs retain their source axial clip law.

## 2. Important identity: the earlier Case1/2 495.99/501.03 kN result was not this strict unified gate

An earlier diagnostic used the uniaxial N-M section state plus a separate TC-envelope contact condition and obtained approximately

\[
495.99\ \mathrm{kN},\qquad 501.03\ \mathrm{kN}.
\]

That calculation remains useful evidence that TC strength is selective, but it is **not** the same object as

\[
\boxed{\text{current-map phase equilibrium}+\text{hard envelope admissibility}}.
\]

The present audit therefore does not force reproduction of those values.

## 3. Swartz Case1 — strict literal gate

Frozen structural/material input:

\[
a_{phys}=2440\ \mathrm{mm},\quad b=1220\ \mathrm{mm},\quad t=25.40\ \mathrm{mm},
\]

\[
f_c=22.81\ \mathrm{MPa},\quad E_0=21730\ \mathrm{MPa},\quad \varepsilon_0=0.00210,\quad \nu=0.18,
\]

\[
\rho_x=\rho_y=0.002,
\]

single mid-plane layer, and the project common ordinary-concrete value

\[
f_t=0.1f_c=2.281\ \mathrm{MPa}.
\]

The current structural frontend gives \(m_*=2\). The literal hard-admissibility search over the finite control coordinate gives the first contact at

\[
\boxed{s=1}.
\]

The current-map equilibrium state first touches the TC tensile envelope at

\[
\boxed{q_{hard,1}=0.0033103796663},
\]

which corresponds to

\[
\boxed{P_{hard,1}=588.598156\ \mathrm{kN}}.
\]

The active through-thickness location is interior, approximately

\[
z\approx-4.110\ \mathrm{mm},
\]

where

\[
\sigma_1\approx+0.202906\ \mathrm{MPa},
\qquad
\sigma_2\approx-22.133646\ \mathrm{MPa},
\]

and the Nguyen TC tensile peak is exactly

\[
\sigma_{1p}\approx0.202906\ \mathrm{MPa}.
\]

Against the experimental failure load \(490.194\) kN, opened only after the theoretical event is fixed,

\[
\boxed{\text{error}=+20.075\%}.
\]

Thus the strict unified current-map gate **does not** reproduce the earlier near-zero-error 495.99 kN diagnostic.

## 4. Swartz Case2 — strict literal gate

Frozen input:

\[
t=25.40\ \mathrm{mm},\quad f_c=22.27\ \mathrm{MPa},\quad E_0=23194\ \mathrm{MPa},\quad \varepsilon_0=0.00192,
\]

with the same geometry, reinforcement interpretation and \(f_t=0.1f_c\) project material identity.

The first literal hard contact is again

\[
\boxed{s=1},
\]

at

\[
\boxed{q_{hard,2}=0.0028515509569},
\]

\[
\boxed{P_{hard,2}=584.544674\ \mathrm{kN}}.
\]

The active interior thickness location is approximately

\[
z\approx-3.314\ \mathrm{mm},
\]

with

\[
\sigma_1\approx+0.197988\ \mathrm{MPa},
\qquad
\sigma_2\approx-21.610039\ \mathrm{MPa},
\]

and \(\sigma_1=\sigma_{1p}\) on the TC envelope.

Post-solution comparison with \(P_f=506.652\) kN gives

\[
\boxed{\text{error}=+15.374\%}.
\]

## 5. What happened to Case1/2

Three distinct quantities must no longer be conflated:

|Object|Case1 kN|Case2 kN|Identity|
|---|---:|---:|---|
|corrected-reinforcement uniaxial N-M PRE-GATE|567.712|561.638|old explicit section candidate|
|earlier separate TC contact diagnostic|495.989|501.025|uniaxial-state TC sensitivity only|
|current-map UMCG section fold without hard envelope|604.450|597.732|audit-only current-map fold|
|**strict literal current-map + hard envelope**|**588.598**|**584.545**|this audit|

Therefore the earlier statement that “strict UMCG should naturally reduce Case1/2 to about the experiment” is **not supported** by the consistent calculation.

The earlier 495.99/501.03 result must be retained only as a mechanism diagnostic based on a different stress-recovery object.

## 6. Z6 — strict literal hard-admissibility search

The current structural backbone remains exactly that of the preceding Z6 audits:

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

with

\[
P_{cr}=39.2880147150\ \mathrm{MN},
\]

\[
C=86071.5974582\ \mathrm{MN},
\quad
G=7.4692093263\times10^6\ \mathrm{N/mm},
\quad
J=1.2419245217\times10^7\ \mathrm{N}.
\]

The concrete is the same frozen NC-M6 current map, the two steel faces retain plane-stress von-Mises radial caps, and the longitudinal web retains its y-only yield clip.

For each prescribed \(s\), the phase-compatible current-map section equilibrium was solved first, and then the minimum Nguyen/Foster hard-envelope margin through the concrete thickness was localized. No hard-envelope projection/capping law was added.

Representative first-contact results are:

|s|q_hard|P_hard / MN|
|---:|---:|---:|
|0.0|0.01186808424|49.67970|
|0.1|0.01162600083|48.87005|
|0.2|0.01142160014|48.19053|
|0.3|0.01123069674|47.55914|
|0.4|0.01113699417|47.25035|
|0.5|0.01113486926|47.24335|
|0.6|0.01122414437|47.53752|
|0.7|0.01141036694|48.15329|
|0.8|0.01170683150|49.13979|
|0.9|0.01214269650|50.60480|
|1.0|0.01275324835|52.68831|

Continuous minimization gives

\[
\boxed{s_{hard,Z6}\approx0.452284},
\]

\[
\boxed{q_{hard,Z6}=0.0111245993274},
\]

\[
\boxed{P_{hard,Z6}=47.20955472\ \mathrm{MN}}.
\]

The active point is the concrete-core face

\[
z=-61\ \mathrm{mm},
\]

in TC, with

\[
\sigma_1\approx+0.990248\ \mathrm{MPa},
\qquad
\sigma_2\approx-27.099174\ \mathrm{MPa},
\]

and

\[
\sigma_1=\sigma_{1p}\approx0.990248\ \mathrm{MPa}.
\]

The compressive TC inequality is still inactive there.

## 7. Z6 comparator check after the strict event is fixed

Historical/source comparators:

\[
P_{Zhou}=49.48676675\ \mathrm{MN},
\qquad
P_{Winter}=50.18585413\ \mathrm{MN}.
\]

The literal hard-event value is therefore

\[
\boxed{-4.602\%\ \text{vs Zhou}},
\]

\[
\boxed{-5.931\%\ \text{vs Winter}}.
\]

Hence the hoped-for bracket

\[
P_{Zhou}<P_{NZ-SCCM}<P_{Winter}
\]

**does not emerge from treating the first Nguyen TC-envelope contact as the final ultimate state.**

No parameter is changed to force that bracket.

## 8. The key theoretical finding

The literal hard-envelope calculation exposes a more fundamental issue:

\[
\boxed{\text{Nguyen/Foster envelope contact is a material state-transition surface, not automatically global collapse.}}
\]

In Nguyen's source model, reaching the envelope can initiate cracking/crushing-state evolution and the material can continue on cracked/post-peak branches. Therefore two extreme interpretations are both incomplete:

1. **ignore the hard envelope and continue only with the smooth NC-M6 current map** — this produced the earlier Case1/2 `604/598 kN` and Z6 `51.345 MN` current-map folds;
2. **terminate the whole member at first hard-envelope contact** — this audit gives Case1/2 `588.6/584.5 kN` and Z6 `47.21 MN`.

The physically consistent strict unified model requires

\[
\boxed{\text{current-map evolution} + \text{hard transition surfaces} + \text{source-grounded admissible post-envelope continuation}.}
\]

The hard surface must trigger the appropriate material continuation; it must not simply disappear, but it also must not automatically be equated with global ultimate capacity when the source material model explicitly permits post-cracking/post-peak redistribution.

## 9. Governance corrections

The following previous statuses are superseded:

```text
Z6_FINAL_UMCG_ROOT = RESOLVED              -> SUPERSEDED / TOO STRONG
Z6_51P345_MN = FINAL                       -> NO
SWARTZ24_604_598_AS_STRICT_UMCG            -> NO
CASE1_2_495_501_AS_UNIFIED_STRICT_RESULT   -> NO
```

Retained identities:

```text
Z6_51P345_MN = CURRENT_MAP_UMCG_FOLD_CANDIDATE
Z6_47P210_MN = LITERAL_FIRST_HARD_ENVELOPE_EVENT
CASE1_2_588P598_584P545 = LITERAL_FIRST_HARD_ENVELOPE_EVENT
CASE1_2_495P989_501P025 = SEPARATE_TC_SENSITIVITY_DIAGNOSTIC
FINAL_STRICT_POST_ENVELOPE_ULTIMATE = OPEN
```

## 10. Decision

```text
STRICT_HARD_SURFACE_OVERLAY = EXECUTED
CASE1_STRICT_LITERAL_EVENT = 588.598156 kN
CASE2_STRICT_LITERAL_EVENT = 584.544674 kN
Z6_STRICT_LITERAL_EVENT = 47.20955472 MN
Z6_STRICT_LITERAL_CONTROL_s = 0.452284
DESIRED_ZHOU_WINTER_BRACKET = NOT USED AS ROOT CONDITION
DESIRED_ZHOU_WINTER_BRACKET = NOT ACHIEVED BY FIRST-CONTACT TERMINATION
POST_ENVELOPE_SOURCE_CONTINUATION = REQUIRED FOR FINAL STRICT UMCG
STRUCTURAL_BACKBONE_MODIFIED = NO
MATERIAL_PARAMETER_BACKFIT = NO
```

The next theory task is therefore not another scalar correction. It is to decide and implement one transferable, source-grounded post-envelope continuation rule for NC, then provide the analogous UHPC material continuation under the same UMCG architecture.