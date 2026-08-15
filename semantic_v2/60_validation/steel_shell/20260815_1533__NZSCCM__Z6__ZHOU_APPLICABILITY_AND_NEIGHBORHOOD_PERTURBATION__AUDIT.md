# NZ-SCCM Z6 — Zhou applicability and neighborhood perturbation audit

**Timestamp:** 2026-08-15 15:33 +08:00  
**Status:** SOURCE APPLICABILITY AUDITED / ORIGINAL NZ METHOD NOT REJECTED / NEIGHBORHOOD DISCRIMINATOR DEFINED

## 0. Reason for reopening the diagnosis

The previous execution encountered a deep-q coefficient-composition conditioning problem in the outer-shell radial-cap analytic compiler. That is a real representation gate, but it is **not evidence that the original NZ-SCCM physical calculation method is the cause of the Z6 discrepancy**.

This audit therefore resets the causal order:

```text
DO_NOT_INFER: original NZ-SCCM method is wrong because deep-q compiler fails
FIRST QUESTION: what is special about Z6 relative to Zhou's own source parameter space?
SECOND QUESTION: is the Zhou comparator a raw FE/case value or a fitted envelope value?
THIRD QUESTION: do small perturbations around Z6 change the Zhou prediction smoothly or singularly?
FOURTH QUESTION: run the unchanged NZ method on the same neighborhood before modifying theory.
```

No R10/N48/material/imperfection/calibration change is made here.

## 1. Source applicability: Z6 is nominally inside Zhou Chapter-5 axial parameter space

Zhou, Chapter 5, Table 5.1 gives the four-edge simply-supported axial-compression parameter design. Group 4 is:

```text
ns = 10–60
ls = 200 mm
h = 100–130 mm
ts = 4 mm
fy = 355 MPa
fcu = 40 MPa
a = 3000–9000 mm
b = 2000–12000 mm
```

Current Z6 is:

```text
ns = 60
ls = 200 mm
h = 130 mm
ts = 4 mm
fy = 355 MPa
fcu = 40 MPa
a = 9000 mm
b = 12000 mm
```

Therefore Z6 is not outside the nominal Table-5.1 source range. It sits at the **extreme corner** of Group 4: maximum ns, h, a and b of that row.

Decision:

```text
Z6_OUTSIDE_ZHOU_NOMINAL_PARAMETER_RANGE = NO
Z6_AT_EXTREME_PARAMETER_CORNER = YES
```

Important qualification: the project labels Z0–Z6 as representative parameter combinations constructed from Zhou's parameter design; unless a literal source FE row is recovered, they must not be relabelled as original FE specimen IDs.

## 2. Z6 is mechanically different from Z0–Z5 even before any NZ-specific issue

For Z6:

\[
a/h = 9000/130 = 69.2308,
\qquad
b/h = 12000/130 = 92.3077.
\]

Zhou's Chapter-5 conclusion states that four-edge axial stability depends jointly on `Dy`, `Dx` and `H`, and is strongly related to `a/h` and `b/h`. The reported elastic transition values are approximately

\[
a/h=36,\qquad b/h=60,
\]

while the elastoplastic width transition is approximately

\[
b/h=40,
\]

with the corresponding elastoplastic critical `a/h` below 20.

Thus Z6 is not a near-transition case; it is deep in the stability-controlled region.

The current representative normalized slenderness values are:

```text
Z0  0.749978
Z1  0.866840
Z2  0.804027
Z3  0.819614
Z4  0.635754
Z5  0.240871
Z6  1.434107
```

Z6 is the only representative case with

\[
\boxed{\lambda_n>1}.
\]

Therefore it alone enters the second branch of Zhou Eq. (5-88). This is the cleanest source-side distinction between Z6 and the six better-predicted cases.

The Z4–Z6 pair is especially informative:

```text
same fy = 355 MPa
same fcu = 40 MPa
same ts = 4 mm
same ls/ts = 50
same a/b = 0.75

Z4: a/h=30.0,   b/h=40.0
Z6: a/h=69.23,  b/h=92.31
```

Hence local `ls/ts` is not a unique Z6 cause; the principal changed axis is global slenderness.

## 3. Comparator identity correction: 49.6724 MN is not a literal raw FE Z6 capacity

Zhou Chapter 5 states:

- the Winter curve lies above the FE points and, for `lambda_n >= 1.0`, is almost their upper envelope;
- Eqs. (5-87)/(5-88) are obtained by fitting a Perry-Robertson lower-envelope curve;
- the fitted curve envelopes the FE points and is proposed for four-edge axial stability design.

Therefore the current value

\[
P_{Zhou,lower}(Z6)=49.6724\;\text{MN}
\]

has the identity

```text
ZHOU_LOWER_ENVELOPE_DESIGN_VALUE
```

and not

```text
RAW_FE_CAPACITY_OF_A_LITERAL_SPECIMEN_NAMED_Z6.
```

For the same Z6 parameters the Winter upper reference is

\[
P_{Winter}=52.0020\;\text{MN}.
\]

This does not make the NZ value `37.5094 MN` acceptable by itself, but it changes the validation question: the current 24.5% gap is a gap to a **source lower-envelope design curve evaluated at a representative extreme-corner parameter combination**, not a direct experimental/FE error for a literal source specimen.

## 4. Zhou-side neighborhood perturbation — smooth, not singular

All calculations below use the original Zhou full-topology formulas with unchanged

```text
ls=200 mm
ts=4 mm
fy=355 MPa
fcu=40 MPa
```

and `ns=b/ls` for changed-width cases. No NZ result is used.

|case|a/h|b/h|Pyth MN|Pcr MN|m|lambda_n|phi_lower|Zhou lower MN|Winter MN|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|Z6 base|69.2308|92.3077|88.089888|42.831476|1|1.434107|0.563884|49.672436|52.001988|
|a -5%: 8550|65.7692|92.3077|88.089888|44.207855|1|1.411605|0.566069|49.864952|52.678318|
|a = 8000|61.5385|92.3077|88.089888|46.373899|1|1.378244|0.570442|50.250137|53.712307|
|b -5%: 11400, ns=57|69.2308|87.6923|83.685394|43.882545|1|1.380953|0.570039|47.703942|50.945577|
|b = 10000, ns=50|69.2308|76.9231|73.408240|47.738826|1|1.240042|0.601165|44.130467|48.695627|
|a,b -5%|65.7692|87.6923|83.685394|45.078257|1|1.362515|0.572938|47.946569|51.502582|
|a=8000,b=10000|61.5385|76.9231|73.408240|49.695235|1|1.215388|0.608714|44.684656|49.466053|
|h +5%: 136.5|65.9341|87.9121|90.967464|48.535922|1|1.369025|0.571872|52.021775|55.768991|
|h = 150|60.0000|80.0000|96.943968|61.884205|1|1.251614|0.597842|57.957129|63.840626|

The normalized stability factor varies smoothly:

```text
Z6 base       phi = 0.5639
a -5%         phi = 0.5661
a = 8000      phi = 0.5704
b -5%         phi = 0.5700
b = 10000     phi = 0.6012
a,b -5%       phi = 0.5729
a=8000,b=10000 phi = 0.6087
h +5%         phi = 0.5719
```

There is no source-formula discontinuity at Z6. A 5% height reduction changes Zhou lower capacity by only about +0.39% because section strength is unchanged and only stability improves. Width reduction improves normalized stability but reduces absolute section strength, so absolute Pu can fall even while `phi` rises.

Decision:

```text
ZHOU_Z6_LOCAL_PARAMETER_SINGULARITY = NOT SUPPORTED
ZHOU_Z6_HIGH_SLENDERNESS_TAIL = CONFIRMED
```

## 5. What this says about the original NZ method

The current evidence is insufficient to reject the original NZ-SCCM method. The six-case pattern instead suggests a targeted discriminator:

- If the **unchanged** NZ method suddenly returns close agreement when moving only slightly away from Z6 (for example `a=8000,b=12000` or `a=9000,b=10000`), then the priority suspect is a branch/mode/one-halfwave representation issue localized near the extreme slender corner.
- If the unchanged NZ underprediction remains smooth and large across those neighboring cases, then the likely missing mechanism is a high-slenderness finite-amplitude reserve (postbuckling/membrane/multimode/topology effect), rather than a one-off numerical bug.

This test must be done before modifying R10, N48, the shell constitutive law, imperfection, or adding an empirical Z6 factor.

## 6. Revised next task

```text
CURRENT_NEXT_TASK = Z6_UNCHANGED_NZ_METHOD_NEIGHBORHOOD_SWEEP
```

Minimum set:

```text
S0: a=9000, b=12000, h=130, ns=60  # Z6
S1: a=8000, b=12000, h=130, ns=60
S2: a=9000, b=10000, h=130, ns=50
S3: a=8000, b=10000, h=130, ns=50
S4: a=8550, b=11400, h=130, ns=57  # smooth -5% diagnostic
```

Frozen NZ identity for the sweep:

```text
R10 = unchanged
N48-C1/MM = unchanged
Cayley-Hamilton = unchanged
General D15 = unchanged
Nguyen second-order kinematics = unchanged
local progressive radial-cap shell map = unchanged
A0 = a/500
formal structural spatial sampling = 0
formal structural quadrature = 0
Zhou/Winter loads do not enter root selection
```

Only after this sweep should the project decide whether the deep-q shell-compiler stabilization is a production necessity or merely a secondary implementation gate reached by an H0 branch that is not the correct causal path.

## 7. Governance conclusion

```text
ORIGINAL_NZ_METHOD_AS_ROOT_CAUSE = NOT ESTABLISHED
Z6_OUTSIDE_ZHOU_RANGE = NO
Z6_EXTREME_CORNER = YES
Z6_ONLY_CASE_WITH_LAMBDA_GT_1 = YES
ZHOU_49P672_IDENTITY = LOWER_ENVELOPE_DESIGN_VALUE
ZHOU_NEIGHBORHOOD_RESPONSE = SMOOTH
H0_SHELL_COMPILER_FAILURE_AS_Z6_PHYSICAL_CAUSE = REJECTED
NEXT = UNCHANGED_NZ_NEIGHBORHOOD_SWEEP
```
