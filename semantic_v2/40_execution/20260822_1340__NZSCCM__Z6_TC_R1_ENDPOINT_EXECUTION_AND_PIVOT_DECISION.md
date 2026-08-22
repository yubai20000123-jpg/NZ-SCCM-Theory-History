# NZ-SCCM — Z6 TC-R1 endpoint execution + general-s stop gate + constitutive pivot decision

**Date:** 2026-08-22 13:40 +08:00  
**Status:** `EXECUTED / S0_DIRECT_ROOT_RESOLVED / GENERAL_S_FINAL_CERTIFICATE_OPEN / NO_PREMATURE_MODEL_LOCK`

## 0. Scope

This execution follows:

`semantic_v2/20_theory/20260822_1338__NZSCCM__NC_TC_MEMORYLESS_REDUCTION_R1_AND_ALTERNATIVE_MODEL_AUDIT.md`

and uses the unchanged Marguerre–Airy structural backbone.

Formal endpoint calculation:

```text
spatial quadrature = 0
material points = 0
load steps = 0
history state machine = 0
comparator in root selection = 0
```

The only nonlinear solve is one finite algebraic root in the endpoint variables.

---

# 1. Z6 finite s=0 system

At \(s=0\):

\[
m=Jqs=0,
\]

so the compatible section is uniform through thickness. Use current NC material coordinates

\[
(\lambda_t,\lambda_c),
\]

with physical bonded strains

\[
\frac{\varepsilon_x}{\varepsilon_0}=\lambda_t-\nu_c\lambda_c,
\qquad
\frac{\varepsilon_y}{\varepsilon_0}=\lambda_c-\nu_c\lambda_t.
\]

The finite phase system consists of:

\[
N_x^{sec}(\lambda_t,\lambda_c)=K_xq(q+2q_0),
\]

\[
N_y^{sec}(\lambda_t,\lambda_c)
=-\left[\frac{P_{pb}(q)}b+Gq(q+2q_0)\right],
\]

plus the longitudinal web compression-yield boundary

\[
E_s\varepsilon_y+f_y=0.
\]

Concrete uses TC-R1, external steel uses plane-stress elastic trial + von-Mises radial cap, and the equivalent longitudinal web uses an elastic-perfectly-plastic y law.

Z6 frozen coefficients:

\[
P_{cr}=39.2880147150\ \mathrm{MN},
\qquad
C=86071.5974582\ \mathrm{MN},
\]

\[
G=7.4692093263\times10^6\ \mathrm{N/mm},
\qquad
K_x=6.876056916767441\times10^6\ \mathrm{N/mm}.
\]

---

# 2. Direct endpoint root

The reproducible solver is:

`semantic_v2/40_execution/steel_shell/20260822_1340__NZSCCM__Z6_TC_R1_DIRECT_ENDPOINT_SOLVER.py`

The finite root is

\[
\boxed{\lambda_t\approx0.7249185},
\]

\[
\boxed{\lambda_c\approx-0.7904509},
\]

\[
\boxed{q\approx0.01202893},
\]

\[
\boxed{P_{s=0}^{TC-R1}\approx50.22069\ \mathrm{MN}}.
\]

This value is **not yet certified as final Z6 Pu**; it is the exact current finite endpoint candidate.

The current MCFT/Nguyen compression-softening factor is

\[
\boxed{\gamma_c\approx0.95559147}.
\]

Recovered concrete stresses are approximately

\[
\boxed{\sigma_x^c=+0.91389033\ \mathrm{MPa}},
\]

\[
\boxed{\sigma_y^c=-28.33808579\ \mathrm{MPa}}.
\]

The external steel faces are on their plane-stress radial cap:

\[
\boxed{\sigma_x^s\approx+193.42012\ \mathrm{MPa}},
\]

\[
\boxed{\sigma_y^s\approx-216.28594\ \mathrm{MPa}},
\]

with elastic-trial von-Mises stress about \(459.42\) MPa and radial scale about \(0.77271\).

The equivalent web satisfies exactly

\[
\boxed{\varepsilon_y=-f_y/E_s=-0.0017233009708737864},
\]

\[
\boxed{\sigma_y^w=-355\ \mathrm{MPa}}.
\]

The section resultants are approximately

\[
N_x^{sec}=1656.626\ \mathrm{N/mm},
\]

\[
N_y^{sec}=-5984.589\ \mathrm{N/mm},
\]

and match the structural demands to numerical root precision.

---

# 3. Why this is a terminal s=0 complementarity kink

The equilibrium branch was differentiated on the two one-sided web states at the same root.

Elastic-web side:

\[
\det\left(\frac{\partial(R_x,R_y)}{\partial(\lambda_t,\lambda_c)}\right)
\approx+1.5930\times10^6,
\]

and the web-yield function

\[
h=E_s\varepsilon_y+f_y
\]

has

\[
\frac{dh}{dq}\approx-3.6871\times10^5<0.
\]

Thus increasing \(q\) on the elastic branch approaches/crosses the compression-yield surface.

Capped-web side:

\[
\det\left(\frac{\partial(R_x,R_y)}{\partial(\lambda_t,\lambda_c)}\right)
\approx-2.5831\times10^4,
\]

but

\[
\frac{dh}{dq}\approx+2.2738\times10^7>0.
\]

Hence an incremental continuation on the capped branch immediately points back into the elastic side and violates the assumed active set. The finite s=0 branch therefore ends at this nonsmooth complementarity event.

```text
Z6_TC_R1_S0_ENDPOINT_ROOT = RESOLVED
Z6_TC_R1_S0_TERMINAL_COMPLEMENTARITY = PASS
```

---

# 4. Comparator opened only after the root

Only after the material/section root was fixed:

- Zhou comparator: \(49.48676675\) MN;
- Winter comparator: \(50.18585413\) MN.

The endpoint candidate differs by approximately:

\[
+1.4831\%\quad\text{vs Zhou},
\]

\[
+0.0694\%\quad\text{vs Winter}.
\]

Relative to the current 1D Z6 value \(56.37942109\) MN, the endpoint reduction is

\[
\boxed{-10.9237\%}.
\]

None of these comparators entered the root solve.

---

# 5. Why 50.22069 MN is not frozen as final Pu

For \(s>0\), the section has nonzero bending

\[
m=Jqs,
\]

so the longitudinal strain varies through thickness. A preliminary **off-mainline diagnostic only** was used to test whether the old endpoint-control assumption is robust. That diagnostic used thickness numerical integration and is therefore explicitly non-formal.

Its only admissible conclusion is qualitative:

> the controlling location may move a small distance away from exactly \(s=0\), with a load very close to the endpoint candidate.

Because formal spatial/thickness quadrature remains prohibited, the diagnostic number itself is not promoted into the theory.

A formal general-s TC-R1 calculation would require finite analytic branch-front primitives for T5, softened Saenz, steel radial-cap, and web-yield fronts. Such a construction appears mathematically possible, but it is substantially larger than the current low-order explicit section theory.

```text
Z6_TC_R1_GENERAL_S_DIAGNOSTIC = OFF_MAINLINE_ONLY
Z6_TC_R1_GENERAL_S_FORMAL_CERTIFICATE = OPEN
Z6_FINAL_POSTCRACK_2D_PU = OPEN
```

---

# 6. Constitutive-model pivot test

The user explicitly authorized abandoning Nguyen if this reduction becomes a dead end. Therefore the present execution also screened alternative concrete laws rather than automatically expanding the Nguyen machinery.

## Cedolin–Mulas 1984

The literature explicitly describes it as a total, explicit biaxial stress–strain relation with an explicit plane-stress transverse-strain elimination and only three material parameters. This is the strongest alternative in terms of G4/G6 architecture.

However, the recovered source scope is monotonic biaxial loading **up to peak stress**. A source-closed post-transverse-crack TC continuation has not yet been recovered. It therefore cannot yet replace TC-R1 for the exact Z problem without introducing another project postcrack assumption.

## Bažant–Tsubaki 1980

The total-strain core is algebraic and includes peak, strain softening and dilatancy, which is attractive. But the source describes the plain-concrete model as applying to material free of continuous cracks. The current problem is specifically continuation after a transverse cracking marker; direct domain equivalence is therefore not established.

## Darwin–Pecknold / full softened membrane models

Darwin–Pecknold remains a strong biaxial oracle but its equivalent-uniaxial machinery does not reduce the section complexity. Full softened-membrane models close cracked RC behavior better but import more state/path/reinforcement machinery and are not a cleaner steel-shell concrete G6 operator.

---

# 7. Decision

The literal Nguyen state machine has failed the production G6 gate and is not being preserved merely for continuity.

The reduced TC-R1 map, however, has **not** failed material-level G6: it gives a direct bounded memoryless current law and a clean finite Z6 endpoint solution.

Therefore the current decision is:

```text
LITERAL_NGUYEN_POSTCRACK_TC = OFF_MAINLINE_ORACLE
TC_R1_MATERIAL_LEVEL = PASS_CANDIDATE
TC_R1_S0_Z6 = 50.22069 MN ENDPOINT CANDIDATE
TC_R1_GENERAL_S = OPEN
CEDOLIN_MULAS_1984 = FIRST_REPLACEMENT_CANDIDATE_IF_GENERAL_S_BECOMES_OPAQUE
BAZANT_TSUBAKI_1980 = POSTPEAK_TOTAL_STRAIN_ORACLE
Z6_FINAL_POSTCRACK_2D_PU = OPEN
```

No further investment in a large TC-R1 primitive/compiler layer is automatically authorized. The next formal step is a compactness test: if a finite general-s capacity reduction cannot be written with a small auditable primitive set, switch the NC production candidate rather than building a large special-function backend around Nguyen.
