# NZ-SCCM — NC TC crack-trigger + tension-stiffening source audit R01

**Time:** 2026-08-22 20:04 +08:00  
**Status:** `EXECUTED / EXPLICIT_STRUCTURAL_PATH_UNCHANGED / MATERIAL_LAYER_REOPENED / NO_Pf_BACKFIT`

## 0. Governing boundary

The explicit source-waveform structural path is unchanged:

\[
P_\Phi(q)=P_{cr,\Phi}\frac{q}{q+q_0}+C_\Phi q(q+2q_0),
\]

with the same frozen source waveforms and full two-slope section interface

\[
\lambda_x=a_x+b_xz,\qquad \lambda_y=a_y+b_yz.
\]

No spatial quadrature, material-point mesh or experimental-load root selection is introduced.

```text
EXPLICIT_STRUCTURAL_PATH_CHANGED = FALSE
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
Pf_IN_ROOT_SELECTION = 0
MATERIAL_LAYER_REOPENED = TRUE
```

The purpose is to determine which material layer actually needs replacement after the 19:27 full-2D diagnostic.

---

## 1. Source correction 1 — the current Vecchio–Collins gamma onset is not the error

Nguyen Eq. (3.43), following Vecchio & Collins, gives the cracked-TC compressive peak factor

\[
\gamma_{VC}=\min\left[1,\frac{1}{0.8+0.34\,\varepsilon_t/|\varepsilon_0|}\right].
\]

Therefore compression softening begins only when

\[
\frac{\varepsilon_t}{|\varepsilon_0|}>\frac{0.2}{0.34}=\frac{10}{17}=0.588235\ldots
\]

The present `10/17` threshold is therefore source-faithful. The previous interpretation that the gamma law itself must start immediately after cracking is withdrawn.

```text
VC_GAMMA_10_OVER_17 = SOURCE_CORRECT
REPLACE_GAMMA_ONLY = NOT_JUSTIFIED
```

---

## 2. Source correction 2 — Nguyen's TC envelope is a cracking/state-transition surface, not a terminal Pu surface

For positive tensile/compressive magnitudes `(t,p)`, the Nguyen/Foster–Kupfer TC source envelope is

\[
\frac{p}{f_c}+\frac{t}{3f_t}=1
\]

on the compression-axis segment and

\[
\frac{p}{2f_c}+\frac{t}{f_t}=1
\]

on the tension-axis segment, joining at

\[
(p/f_c,t/f_t)=(0.8,0.6).
\]

In Nguyen's constitutive state machine, reaching this source tensile peak initiates the cracked TC state. It is not an ultimate structural failure criterion.

The current scalar reduction instead uses the uniaxial fixed crack front

\[
\varepsilon_{cr}=f_t/E_0
\]

independently of simultaneous compression. This is now identified as the more fundamental TC omission.

### 2.1 Direct source-waveform transition calculation

Using the unchanged source-wave structural demand, the unchanged precrack material branch, and the full two-slope section equilibrium, the first TC-envelope crossing occurs at approximately:

| Panel | `u` | `q_TC-crack` | `P_TC-crack` / kN | role |
|---:|---:|---:|---:|---|
| 1 | 0.63394 | 0.00071294 | **341.912** | first TC cracking/state transition |
| 14 | 0.56809 | 0.00050707 | **476.375** | first TC cracking/state transition |
| 21 | 0.35648 | 0.00088147 | **128.249** | first TC cracking/state transition |

These loads are deliberately **not** called `Pu`. Treating them as terminal capacities would underpredict the corresponding tests by roughly 30%, 33% and 65%, which proves that the source TC envelope must be used as a branch-transition surface rather than a structural failure surface.

```text
TC_ENVELOPE_AS_TERMINAL_Pu = REJECTED
TC_ENVELOPE_AS_CRACK_TRANSITION = REQUIRED
CURRENT_FIXED_UNIAXIAL_CRACK_FRONT_IN_TC = INCOMPLETE
```

---

## 3. Foster alpha2 source audit

Nguyen, following Foster (1992), states:

\[
\alpha_1=10,
\]

while

\[
\alpha_2\approx0.3\quad\text{for lightly reinforced concrete},
\qquad
\alpha_2\approx0.7\quad\text{for more heavily reinforced concrete}.
\]

A retrospective source also records that Foster used `alpha2=0.3` for his own tests and varied `alpha2` roughly from `0.2` to `0.8` when simulating other tests. No deterministic transferable relation

\[
\alpha_2=\alpha_2(\rho,\phi,\text{bond})
\]

has been recovered from the available source chain.

Therefore a project interpolation of `alpha2` versus Swartz reinforcement ratio would be an additional empirical assumption. It is not source-closed merely because it lies between 0.3 and 0.7.

```text
FOSTER_ALPHA2_REINFORCEMENT_DEPENDENCE = SOURCE_REAL
FOSTER_ALPHA2_DETERMINISTIC_RHO_RULE = NOT_RECOVERED
ALPHA2_LINEAR_INTERPOLATION_FROM_SWARTZ = NOT_PROMOTED
```

---

## 4. Finite candidate sensitivity through the unchanged explicit path

The following calculations modify only the postcrack tensile material law. The source-wave structural operator, full two-slope section interface and exact finite section primitives remain unchanged. `Pf` is inserted only after each theoretical event is fixed.

### 4.1 Foster alpha2 sensitivity

| Candidate | Panel 1 event / kN | Panel 1 post-check | Panel 14 first event / kN | Panel 21 connected fold / kN | Panel 21 post-check |
|---|---:|---:|---:|---:|---:|
| F03: `alpha2=0.3` | 589.082 | +20.17% | 770.548 steel-yield terminal | 192.691 | −47.68% |
| F05: `alpha2=0.5` | 607.944 | +24.02% | 770.548 steel-yield terminal | 324.104 | −12.00% |
| F07: `alpha2=0.7` | 637.314 | +30.01% | 770.548 steel-yield terminal | 333.509 | −9.45% |

The trend is decisive:

- increasing `alpha2` greatly delays the premature Panel21 transverse-tension fold;
- the same increase makes the lightly reinforced Panel1 overprediction worse;
- Panel14 is practically unchanged because the first event remains the lower y-rebar compression-yield active-set terminal.

This is mechanically consistent with Foster's statement that `alpha2` is reinforcement/bond dependent, but it does **not** provide a lawful unique `alpha2(rho)` calibration.

### 4.2 Belarbi–Hsu postcrack power-shape diagnostic

A second diagnostic replaces only the Foster finite residual plateau by the Belarbi–Hsu postcrack shape

\[
\sigma_t=f_{cr}\left(\frac{\varepsilon_{cr}}{\varepsilon_t}\right)^{0.4},
\]

while retaining the present project `ft` and the present initial elastic anchor so that the plane-stress origin is not changed. This is labelled `BH04-anchor`; it is a source-shape diagnostic, not yet a production material law.

The affine-through-thickness primitive remains exact because

\[
\int \varepsilon^{-0.4}d\varepsilon\propto\varepsilon^{0.6},
\qquad
\int z\,\varepsilon^{-0.4}dz
\]

is elementary after an affine substitution.

Results:

| Candidate | Panel 1 / kN | Panel 1 post-check | Panel 14 / kN | Panel 21 / kN | Panel 21 post-check |
|---|---:|---:|---:|---:|---:|
| BH04-anchor + bare EPP steel | **529.948** | +8.11% | 770.548 steel-yield terminal | **375.039** | +1.83% |

This simultaneously removes most of the Panel1 excess and the severe Panel21 premature fold. However, this result is **not** sufficient to promote the law because the calculation still uses the incomplete fixed uniaxial TC crack front identified in Section 2.

### 4.3 Belarbi–Hsu paired embedded-steel diagnostic

Belarbi–Hsu/Hsu–Zhang explicitly warn that average cracked-concrete tension plus a bare steel law can create an unwarranted increase in yield strength. A paired diagnostic was therefore also run using the source family for reinforcing steel stiffened by concrete,

\[
f_s=\frac{0.975E_s\varepsilon_s}{[1+(1.1E_s\varepsilon_s/f_y)^m]^{1/m}}+0.025E_s\varepsilon_s,
\]

\[
m=\min\left(\frac1{9B-0.2},25\right),
\qquad
B=\frac1\rho\left(\frac{f_{cr}}{f_y}\right)^{1.5},
\]

for tensile steel only; compressive steel remains the physical bare-bar branch.

With the current `ft` anchor this gives approximately `m=0.934` for Panel1 and `m=9.595` for Panel21. The diagnostic connected-fold results are:

| Candidate | Panel 1 / kN | Panel 1 post-check | Panel 21 / kN | Panel 21 post-check |
|---|---:|---:|---:|---:|
| BH04-anchor + embedded-steel tension law | **528.582** | +7.83% | **303.412** | −17.62% |

Thus the paired Hsu-family law does not by itself solve Panel21. This result is useful because it prevents selecting the apparently excellent `BH04 + bare steel` result merely by closeness to the test.

---

## 5. Main verdict

The source and numerical evidence now separate three distinct issues.

### A. Do not change the 10/17 Vecchio–Collins gamma onset merely to force earlier weakening

That threshold is the literal consequence of the source equation. The previous `gamma starts too late` diagnosis was too coarse.

### B. Do not treat the TC source envelope as an ultimate capacity gate

The direct transition loads around 342/476/128 kN show that it is a cracking/state-transition surface. It must trigger a new TC current branch and then the structure must continue to carry load.

### C. The minimum material layer that must now be rebuilt is the **2D TC crack-front/current-branch switch**

The current scalar rule

\[
\varepsilon_t=f_t/E_0
\]

must no longer be the unique cracking front in a TC state. The next material candidate must use the source biaxial TC peak as the current crack-front definition and then apply the postcrack tension/compression relations on the cracked side of that front.

A useful explicit memoryless source reduction is available directly from the two source TC lines. If `p_0` denotes the current undamaged compressive-stress magnitude, define

\[
f_{cr}^{TC}(p_0)=
\begin{cases}
f_t\left(1-\dfrac{p_0}{2f_c}\right),&0\le p_0/f_c\le0.8,\\[2mm]
3f_t\left(1-\dfrac{p_0}{f_c}\right),&0.8<p_0/f_c\le1.
\end{cases}
\]

Then

\[
\varepsilon_{cr}^{TC}=f_{cr}^{TC}/E_0.
\]

For a Foster-type finite postcrack branch,

\[
\sigma_t=f_{cr}^{TC}\left[1-\frac{(1-\alpha_2)(\varepsilon_t/\varepsilon_{cr}^{TC}-1)}{\alpha_1-1}\right]
\]

can be rewritten as

\[
\boxed{\sigma_t=\left(1+\frac{1-\alpha_2}{\alpha_1-1}\right)f_{cr}^{TC}-\frac{1-\alpha_2}{\alpha_1-1}E_0\varepsilon_t.}
\]

Because the current undamaged compression backbone is rational and both material coordinates are affine in `z`, this TC current branch remains a finite rational/affine function of `z`. Hence a zero-quadrature exact primitive is still possible. The explicit calculation path need not be abandoned.

What changes is the material map: it becomes a genuinely coupled 2D TC current map rather than two independent scalar tension/compression laws.

---

## 6. Next execution

```text
NEXT_NC_CANDIDATE = NC_M6_2D_TC_CRACK_FRONT
STRUCTURAL_PATH = UNCHANGED
TC_CRACK_TRIGGER = SOURCE_BIAXIAL_ENVELOPE
TC_ENVELOPE_ROLE = STATE_TRANSITION_NOT_TERMINAL
VC_GAMMA = RETAIN_SOURCE_FORM_FIRST
POSTCRACK_TENSION = TEST_FOSTER_SOURCE_RANGE_AND_BH04_SHAPE_WITHOUT_Pf_FIT
EXACT_SECTION_PRIMITIVE = REQUIRED
SAME_LAW_JACOBIAN = REQUIRED
```

The next calculation should build `NC-M6` at this layer and rerun Panels 1/14/21 before reopening CC or TT.