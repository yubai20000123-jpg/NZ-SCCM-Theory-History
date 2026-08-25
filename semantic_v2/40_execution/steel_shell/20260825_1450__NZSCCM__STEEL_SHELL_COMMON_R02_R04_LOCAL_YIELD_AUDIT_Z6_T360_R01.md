# NZ-SCCM — Steel-shell common R02/R04 local-yield resultant audit: Z6 vs T360 R01

**Time:** 2026-08-25 14:50 +08:00  
**Parent:** `current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`  
**Scope:** common steel-shell submodule shared by SSNC and SSUHPC  
**Status:** `COMMON-MECHANISM AUDIT COMPLETE / NO PRODUCTION CHANGE`

---

# 0. Scope correction

The preceding SSUHPC-only diagnosis correctly identified a possible loss of R02 local postbuckling stress information before the R04 mean-stress cap, but its scope was too narrow.

R02 and R04 belong to the **steel-shell common layer** of the RC–SSNC milestone. SSUHPC inherits them unchanged. Therefore any defect in the R02 -> R04 interface must first be audited as

```text
STEEL-SHELL COMMON SUBMODULE
```

and cannot be repaired only inside SSUHPC.

This audit uses two deliberately contrasting current-theory states:

- **SSNC Z6 R05**: stockier local steel cell, R02 amplitude barely above the initial imperfection, and the current R05 prediction is already essentially coincident with the post-opened Zhou comparator;
- **SSUHPC T360 R01**: local elastic buckling precedes yield, R02 amplitude grows strongly, and the current blind result is materially above Abaqus.

No comparator is used to recompute either root. Both roots remain frozen.

---

# 1. Shared steel-shell operator being audited

Both SSNC and SSUHPC use the same steel-face sequence:

```text
common terminal face strain
-> R02 finite PBL/Yun amplitude condensation
-> R02 full-area mean membrane stress + finite local harmonic redistribution
-> R04 path-free ideal-EP radial Mises cap on the mean trial stress
-> full-area face resultant Nf = ts * sigma_mean_cap
-> centroidal moment Mf = zf * Nf
```

Thus the formal interface issue, if activated, is common to both materials.

The question is not whether R02 contains local buckling. It does. The question is whether the local stress redistribution is large enough that a **local-yield condition** separates materially from the current **mean-Mises cap**.

Two diagnostics are kept distinct:

1. **Yun-source axial check**: the uniaxial source defines ultimate when the maximum local axial compression reaches `fy`, then evaluates the corresponding mean stress/resultant;
2. **2D consistency diagnostic**: because current R04 is a 2D Mises cap, evaluate the finite R02 local membrane Mises field to determine how far local 2D yielding separates from mean-Mises yielding. This is a diagnostic extension of the already-existing R02 + R04 operators; it is not claimed to be a new Yun source equation.

---

# 2. Z6 R05 — stocky/yield-first control case

Current frozen Z6 R05 data:

```text
local cell = 200 x 200 x 4 mm
A0 = 0.125 mm
fy = 355 MPa
U = 0.12709868068795448 mm
Pu = 49.45439833719624 MN
```

The R02/Yun elastic local critical stress for this 200 x 200 x 4 cell is

\[
\boxed{\sigma_{cr,s}=794.3886717\ \mathrm{MPa}>f_y=355\ \mathrm{MPa}.}
\]

Therefore Z6 is not a `local-buckling-before-yield` steel-face case.

The normalized R02 amplitude is

\[
\boxed{U/A_0=1.0167894455.}
\]

Only about 1.68% growth above the R02 imperfection coefficient occurs at the current terminal state.

## 2.1 Mean R02/R04 state

Current physical trial mean stress:

\[
\boldsymbol\sigma^{tr}_{mean}
=(+286.3263780,-299.5390506,0)\ \mathrm{MPa}.
\]

Mean trial Mises:

\[
\boxed{\sigma_{VM,mean}^{tr}=507.41735195\ \mathrm{MPa}.}
\]

R04 therefore uses

\[
\boxed{\lambda_{R04}=0.699621324802}
\]

and returns

\[
(+200.3200399,-209.5639074,0)\ \mathrm{MPa},
\]

with mean Mises exactly 355 MPa.

## 2.2 Reinsert the finite R02 local membrane fluctuation

At the same fixed Z6 state, the continuous finite-harmonic membrane field gives

\[
\boxed{\max_{\Omega}\sigma_{VM,local}^{mem}\approx507.5050551\ \mathrm{MPa}.}
\]

Hence the local/mean amplification is only

\[
\boxed{
\chi_{loc}^{Z6}
=\frac{507.5050551}{507.4173520}
=1.00017284.
}
\]

As a consistency diagnostic only, if the current R04 scale were applied uniformly to the whole R02 membrane field, the maximum would be

\[
507.5050551\times0.6996213248
=\boxed{355.06136\ \mathrm{MPa}},
\]

which is essentially the same yield surface at this scale.

## 2.3 Yield-onset separation along the fixed Z6 strain ray

Proportionally scale the already-fixed terminal strain vector by `eta`, solving the same R02 cubic at every `eta`.

First local-Mises yield:

\[
\eta_{loc,VM}=0.69950131.
\]

First mean-Mises yield:

\[
\eta_{mean,VM}=0.69962132.
\]

Relative separation is only about

\[
\boxed{0.0172\%}.
\]

At first local-Mises yield the mean stress is approximately

\[
(+200.2854,-209.5283)\ \mathrm{MPa},
\]

almost identical to the current R04 capped mean stress.

For the stricter Yun-source axial criterion, the prescribed local axial compression does not reach 355 MPa until approximately

\[
\boxed{\eta_{axial}=1.18491>1.}
\]

so no Yun-type local-axial-yield truncation is active before the current Z6 terminal state.

### Z6 decision

```text
Z6_LOCAL_BUCKLING_BEFORE_YIELD = NO
Z6_U_OVER_A0 = 1.01679
Z6_LOCAL_VS_MEAN_MISES_SEPARATION = NEGLIGIBLE
Z6_YUN_LOCAL_AXIAL_YIELD_BEFORE_CURRENT_TERMINAL = NO
```

Therefore the existence of the common R02/R04 interface does **not** imply a material correction to the current Z6 R05 result. In Z6, R04 is primarily responding to the strong biaxial mean steel state, not to a severe local-buckling stress concentration.

This explains why the current Z6 R05 result can remain near the post-opened Zhou/Winter comparators without contradicting the common-interface diagnosis.

---

# 3. T360 — local-buckling-before-yield contrast case

Current frozen T360 data:

```text
local cell = 360 x 375 x 4 mm
A0 = 0.225 mm
fy = 355 MPa
U_top = 0.7752040465 mm
U_bottom = 2.8664799221 mm
Pu = 12.18255684307 MN
```

The local elastic critical stress is

\[
\boxed{\sigma_{cr,s}=245.7948984\ \mathrm{MPa}<355\ \mathrm{MPa}.}
\]

Thus local steel buckling definitely precedes material yield.

Normalized amplitudes:

\[
\boxed{U_+/A_0=3.44535132,}
\]

\[
\boxed{U_-/A_0=12.73991077.}
\]

This is qualitatively different from Z6.

## 3.1 Upper face

Current R02 mean trial:

\[
(+84.8810214,-297.3045428,0)\ \mathrm{MPa},
\]

with

\[
\sigma_{VM,mean}=347.6065192\ \mathrm{MPa}<355\ \mathrm{MPa}.
\]

Current R04 therefore does nothing:

\[
\lambda_+=1.
\]

But the finite R02 local membrane field gives

\[
\boxed{\max\sigma_{VM,local}^{mem}\approx374.5803401\ \mathrm{MPa}>355\ \mathrm{MPa}.}
\]

Thus the existing 2D R02+R04 operators themselves are inconsistent at this fixed state: the mean Mises says `elastic`, while the local R02 field contains a point beyond the Mises yield surface.

Local/mean amplification:

\[
\boxed{\chi_{loc,+}^{T360}=1.07759872.}
\]

Along the fixed upper-face strain ray:

\[
\eta_{loc,VM}=0.95163487,
\qquad
\eta_{mean,VM}=1.02169834.
\]

Hence local 2D yield precedes mean-Mises yield by about 6.9% in this proportional strain measure.

However, the original Yun **axial** source criterion does not yet trigger on the upper face at the frozen terminal state; its corresponding axial-yield scale is about

\[
\eta_{axial,+}=1.12281>1.
\]

Therefore the upper-face Mises observation is kept as a 2D consistency diagnostic, not mislabeled as a direct Yun-source axial gate.

## 3.2 Lower face

Current mean trial:

\[
(-87.5897967,-587.7395949,0)\ \mathrm{MPa},
\]

with

\[
\sigma_{VM,mean}^{tr}=549.2083505\ \mathrm{MPa}.
\]

Current R04 applies

\[
\lambda_-=0.6463849277,
\]

and retains the mean stress

\[
(-56.6167244,-379.9060156,0)\ \mathrm{MPa}
\]

with mean Mises exactly 355 MPa.

The same R02 local membrane field before mean homogenized capping has

\[
\boxed{\max\sigma_{VM,local}^{mem}\approx919.8894310\ \mathrm{MPa}.}
\]

Hence

\[
\boxed{\chi_{loc,-}^{T360}=1.67493708.}
\]

Even the purely hypothetical operation of multiplying the entire local field by the current mean R04 scale would leave

\[
919.8894310\times0.6463849277
=\boxed{594.603\ \mathrm{MPa}>355\ \mathrm{MPa}.}
\]

So the gap cannot be described as a tiny localization correction.

The Yun-source axial maximum at the source-controlled point is approximately

\[
|\sigma_y|\approx864.49\ \mathrm{MPa},
\]

far above `fy`.

Along the fixed lower-face strain ray:

\[
\boxed{\eta_{axial,-}\approx0.41317,}
\]

while the local-Mises diagnostic gives

\[
\eta_{loc,VM,-}=0.41923743,
\]

and the mean-Mises yield state is much later:

\[
\eta_{mean,VM,-}=0.62378118.
\]

At first local-Mises yield the R02 full-area mean stress is only approximately

\[
(-67.803,-276.148)\ \mathrm{MPa},
\]

with mean Mises about 249.26 MPa.

Thus, unlike Z6, T360 lower-face local yielding is unequivocally a **local-buckling-driven** event that appears far before the current mean-Mises terminal cap.

---

# 4. Direct common comparison

| metric | SSNC Z6 R05 | SSUHPC T360 upper | SSUHPC T360 lower |
|---|---:|---:|---:|
| local cell / mm | 200x200x4 | 360x375x4 | 360x375x4 |
| `sigma_cr` / MPa | 794.389 | 245.795 | 245.795 |
| `sigma_cr/fy` | 2.238 | 0.692 | 0.692 |
| `A0` / mm | 0.125 | 0.225 | 0.225 |
| current `U/A0` | **1.0168** | **3.4454** | **12.7399** |
| mean trial Mises / MPa | 507.417 | 347.607 | 549.208 |
| current R04 lambda | 0.69962 | 1.00000 | 0.64638 |
| max local membrane Mises / MPa | 507.505 | 374.580 | 919.889 |
| local/mean Mises amplification | **1.00017** | **1.07760** | **1.67494** |
| local Mises after hypothetical uniform R04 scaling / MPa | 355.061 | 374.580 | 594.603 |
| local-Mises yield scale `eta_loc` | 0.69950 | 0.95163 | 0.41924 |
| mean-Mises yield scale `eta_mean` | 0.69962 | 1.02170 | 0.62378 |
| Yun axial-yield scale | 1.18491 | 1.12281 | **0.41317** |

This table is the decisive common-module result.

The same R02/R04 architecture has two regimes:

```text
REGIME A — stocky/yield-first steel face
sigma_cr > fy, U/A0 ~ 1, local redistribution weak
=> local and mean yield checks nearly coincide
=> current R04 is not materially penalized by the homogenization issue

REGIME B — local-buckling-first steel face
sigma_cr < fy, U/A0 grows strongly, local redistribution large
=> local yield can occur far before mean-Mises yielding
=> current mean-only R04 can retain excessive full-area resultant
```

This is a **steel-shell regime distinction**, not an NC-versus-UHPC distinction.

---

# 5. Comparator post-check — evidence only, not a root criterion

The already-fixed outputs remain:

SSNC Z6 R05:

\[
P_u=49.45439834\ \mathrm{MN},
\]

post-opened comparator differences:

```text
vs Zhou   = -0.0654%
vs Winter = -1.4575%
```

SSUHPC T360:

\[
P_u=12.18255684\ \mathrm{MN},
\]

post-opened Abaqus difference:

```text
+11.0655%
```

These comparators are not used to establish the common mechanism. They are only consistent with the internal operator audit:

- Z6 has essentially no local-vs-mean separation;
- T360 has a large local-vs-mean separation.

No correction factor is fitted from these two values.

---

# 6. Common-module verdict

The audit answers the user's question explicitly:

\[
\boxed{
\text{YES: the formal R02 -> R04 interface is shared by SSNC and SSUHPC.}
}
\]

But it also resolves the apparent contradiction:

\[
\boxed{
\text{NO: the numerical severity is not the same in Z6 and T360.}
}
\]

Z6 is a stocky/yield-first local steel case. Its R02 local field remains almost homogeneous at the governing endpoint, so replacing a local-yield check by the mean R04 cap changes essentially nothing at the current state.

T360 is a local-buckling-first case. Its R02 local field becomes strongly nonuniform, especially on the lower face, so local yield and mean-Mises yield separate substantially.

Therefore the preceding interpretation

```text
SSUHPC-SPECIFIC R06
```

is superseded.

Any future correction must be

```text
STEEL-SHELL COMMON R06
```

and must be available identically to SSNC and SSUHPC. Whether it activates is determined by the local steel-face state, not by the core material label.

---

# 7. Governance boundary after this audit

This audit does **not** promote a new production law.

The current production values remain frozen:

```text
Z6 R05 Pu = 49.45439833719624 MN
T360 R01 Pu = 12.18255684307 MN
all current SSUHPC seven-case R01 values remain unchanged
```

The current milestone R02/R04 chain remains production until a common gate passes.

Future common gate requirements:

1. common steel-shell identity: same equations for SSNC and SSUHPC;
2. retain R02 source amplitude and local harmonic field;
3. no effective width/effective area;
4. finite analytic/algebraic local extremum evaluation, no formal spatial grid/quadrature/material points;
5. exact degeneration to existing R04 when local redistribution vanishes / stocky regime governs;
6. Z6 non-regression must be demonstrated blindly;
7. T360/BH032 local-buckling cases must be rerun blindly;
8. only after roots are fixed may Zhou/Winter/Abaqus comparators be reopened.

Current state:

```text
COMMON_R02_R04_INTERFACE_EXISTS = YES
COMMON_INTERFACE_DEFECT_CAN_ACTIVATE = YES
ACTIVATION_IS_CORE_MATERIAL_SPECIFIC = NO
Z6_ACTIVATION_SEVERITY = NEGLIGIBLE AT CURRENT R05 ENDPOINT
T360_ACTIVATION_SEVERITY = STRONG
SSUHPC_ONLY_R06 = REJECTED
NEXT_IF_AUTHORIZED = STEEL_SHELL_COMMON_R06
CURRENT_PRODUCTION_RESULTS = FROZEN
```
