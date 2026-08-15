# NZ-SCCM Z6 H0 same-branch stability causal decomposition — Stage A execution report

**Timestamp:** 2026-08-15 14:36 +08:00  
**Status:** STAGE-A COMPLETE / FULL SAME-BRANCH KZ BLOCKED BY VALIDATED-DOMAIN GATE / NO FABRICATED KZ

## 0. Task

Execute the current Z6 causal task while preserving:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
A0=a/500
R10/N48-C1/MM/general-D15 unchanged
outer steel = current local progressive radial-cap diagnostic
H0 web phase = continuous homogenized longitudinal steel
formal structural sampling = 0
formal structural quadrature = 0
formal structural subdomains = 1
no Zhou/Winter calibration
```

The intended complete output is the connected H0 `Rq=0` branch with component resultants, full current tangents, `L` and Zhou/Navier `KZ`. Before forcing that continuation, Stage A tests the hypothesis that H0 is low because it fails to restore enough web-related elastic/current steel stability stiffness.

## 1. Exact elastic decomposition: the previous broad hypothesis is not supported

For `rho_w=ts/ls`, the Zhou loading-direction rigidity can be rearranged exactly as

\[
D_{y,Zhou}=E_s\frac{h^3-t_c^3}{12}+\rho_wE_s\frac{t_c^3}{12}+(1-\rho_w)E_c\frac{t_c^3}{12}.
\]

This is exactly the H0 elastic sum of outer faceplates, homogenized longitudinal web steel, and remaining concrete. Therefore

\[
\boxed{D_{y,H0}=D_{y,Zhou}}.
\]

For Z6:

```text
D_y,H0   = 11.986113713e9 N mm
D_y,Zhou = 11.986113713e9 N mm
```

The H0 diagnostic differences in the other stiffness terms are small:

```text
Dx deficit = 0.8582%
Dmu deficit = 6.0064%
Dxy deficit = 0.8996%
H deficit = 2.2073%
```

The resulting m=1 elastic critical loads are

```text
old reduced = 41.78842153 MN
H0 elastic diagnostic = 42.34444126 MN
Zhou full = 42.83147561 MN
```

Thus H0 is only `1.1371%` below the source-full elastic `Pcr`.

As a Z4 control, H0 is `1.4462%` below Zhou in elastic Pcr. Therefore the elastic stiffness omission is not selectively worse in Z6.

## 2. Lower-envelope consequence

Using H0's own elastic diagnostic Pcr and its exact full-section `Pyth=88.089888 MN`:

```text
lambda_H0 = 1.442330627
phi_lower(lambda_H0) = 0.563252309
P_lower_equiv,H0 = 49.61683284 MN
```

Zhou original full gives

```text
lambda_Zhou = 1.434106851
P_Zhou,lower = 49.67243594 MN
```

Difference:

```text
-0.11194%
```

Therefore if the H0 object were judged only by the same elastic slenderness + Zhou lower-envelope machinery, its predicted lower reference would be essentially identical to Zhou. The present ~10% fixed-state deficit is a nonlinear path issue, not a large elastic rigidity deficit.

## 3. Differentiate the existing H0 steel current maps — no structural points

The H0 old Z6 state is

```text
D = 0.705
q = 0.0058975999
q0 = 0.0015
Pc,eq = 13.05503043 MN
Pw = 7.26267911 MN
Psh = 24.18847467 MN
P = 44.50618420 MN
Rq = -1.65814501e9 N mm
```

This is not a new equilibrium state.

### 3.1 Web phase

The exact target uniaxial current map is

\[
\sigma_w=f_yu\alpha(r),\qquad u=E_s\varepsilon_y/f_y,\qquad r=u^2.
\]

For the analytic material compiler,

\[
\frac{E_{t,w}}{E_s}=\alpha+2r\alpha'.
\]

The persisted degree-24 `[0,4]`, 4001 material-coordinate-node compiler was differentiated. After composition with the continuous Nguyen polynomial field and exact D15 moments:

```text
Pw reproduced = 7.262679105 MN
volume-mean Et/Es = 0.998987
z^2-weighted Et/Es = 0.996436
```

The material-coordinate nodes are coefficient-generation nodes only. Structural x/y/z points remain zero.

### 3.2 Outer shells

For the local radial current map `sigma=alpha(r)sigma_E`, the loading-direction derivative is

\[
C_{t,yy}=\alpha C^E_{yy}+\sigma_y^E\alpha'(r)\frac{\partial r}{\partial\varepsilon_y}.
\]

With the same H0 fixed-state degree-24 `[0,4]` compiler, exact coefficient-space moments give:

```text
negative face z^2-weighted Ctyy/Ceyy = 0.977664
positive face z^2-weighted Ctyy/Ceyy = 1.000230
combined outer-shell = 0.988947
Psh reproduced = 24.18847466 MN
```

The ~2.3e-4 value above unity on the almost-elastic positive face is polynomial compiler ripple and is not treated as hardening.

Outer + web longitudinal steel bending contribution weighted together gives

```text
~0.989598 of elastic longitudinal steel tangent
```

at this old state.

Therefore the old `D=0.705` state is **not** characterized by a wholesale steel-tangent collapse. The earlier reduced-model mechanism-scale concern about ideal-EP tangent loss remains relevant in general, but it is not numerically active at large measure at this persisted state.

## 4. What the calculation now says about Z6

The causal hierarchy is narrowed:

```text
1. old omission of web-steel axial material = confirmed major partial cause
2. large missing H0 elastic web rigidity = rejected as dominant cause
3. immediate whole-steel tangent collapse at D=0.705 = not supported
4. deep finite-amplitude equilibrium relocation = confirmed
5. primary open cause = nonlinear current-tangent/geometric-stiffness balance on the NEW H0 equilibrium branch, especially concrete/current coupling as q is driven upward
6. discrete-web topology may still matter nonlinearly, but elastic stiffness does not prove that claim
```

A useful scale comparison is:

```text
old reduced -> H0 fixed-state load increase = +18.65%
old reduced -> H0 elastic Pcr increase      = +1.33%
```

This does not by itself define KZ, but it explains why adding web axial material can strongly move the generalized equilibrium without comparably moving the small-amplitude elastic stability threshold.

The persisted old local-cap branch already shows concrete force decreasing as finite amplitude grows while shell force increases:

```text
first-yield reference: Pc=14.2863 MN, Ps=23.0915 MN
D=0.705 peak area:     Pc=13.3215 MN, Ps=24.1880 MN
```

Thus the next H0 equilibrium, which requires larger q, must be audited for concrete tangent degradation and geometric stiffness rather than assuming missing elastic web stiffness.

## 5. Why full same-branch KZ is not released in this step

Two hard gates remain.

### Gate A — no valid new H0 equilibrium state yet

At `D=0.705`:

```text
q=0.005 -> Rq ~= -2.5164e9 N mm
q=0.006 -> Rq ~= -1.5459e9 N mm
```

The continuation toward `q=0.008` exits the currently validated concrete N48 material domain `[-1.15,0.23]`. Extrapolation was already rejected. Hence a connected H0 `Rq=0` state cannot yet be certified.

### Gate B — full KZ needs the directional tangent contraction

The structural theory defines

\[
K_{Z,sh}^{mat}=\int b_\varphi^T C_t b_\varphi\,dV,
\]

and the corresponding current-stress geometric term. The present Stage-A derivative computes a loading-direction tangent diagnostic, not the complete `b_phi^T C_t b_phi` contraction for the web + shell + concrete H0 branch.

No numerical `KZ=0` event is invented in the absence of a valid H0 branch state and full directional contraction.

## 6. Fail-fast result

```text
STAGE_A_ELASTIC_STIFFNESS_DECOMPOSITION = PASS
H0_Dy_EXACT_ZHOU_IDENTITY = PASS
H0_ELASTIC_PCR_CLOSE_TO_ZHOU = PASS
OLD_STATE_WEB_TANGENT_DIAGNOSTIC = PASS
OLD_STATE_OUTER_SHELL_DIRECTIONAL_TANGENT_DIAGNOSTIC = PASS
MISSING_ELASTIC_ORTHOTROPY_AS_DOMINANT_Z6_CAUSE = REJECTED
FULL_H0_Rq_BRANCH = BLOCKED_BY_VALIDATED_MATERIAL_DOMAIN
FULL_H0_KZ = NOT RELEASED
NO_SPATIAL_DISCRETIZATION = PASS
NO_CALIBRATION = PASS
```

## 7. Next task

```text
CURRENT_NEXT_TASK = Z6_H0_ANALYTIC_DOMAIN_AND_FULL_DIRECTIONAL_TANGENT_KZ_GATE
```

Execution order:

1. analytic material-domain bound for the larger-q H0 branch;
2. source-consistent same-R10 N48 compilation over that justified domain;
3. full directional derivative of web/shell current maps;
4. connected `Rq=0` branch continuation;
5. exact-D15 component `KZ` and `L` evaluation;
6. event ordering `first yield -> KZ=0 -> load maximum/fold`.

No empirical correction is authorized.
