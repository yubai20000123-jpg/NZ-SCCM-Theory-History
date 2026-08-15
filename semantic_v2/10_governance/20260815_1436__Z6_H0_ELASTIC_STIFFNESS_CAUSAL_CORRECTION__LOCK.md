# Z6 H0 elastic-stiffness causal correction lock

**Timestamp:** 2026-08-15 14:36 +08:00  
**Identity:** CAUSAL-HYPOTHESIS CORRECTION / NO PARENT-THEORY CHANGE / ZERO STRUCTURAL DISCRETIZATION

## 1. Why this correction is required

The 14:30 state ranked `H0 longitudinal web material without full orthotropic/topological restraint` as the strongest current Z6 hypothesis. The next calculation shows that this wording is too broad: at the **elastic Zhou/Navier stiffness level**, the H0 longitudinal web phase recovers the governing loading-direction rigidity almost exactly.

Therefore the project must not attribute the remaining Z6 deficit to a large missing *elastic* web stiffness without further evidence.

## 2. Exact longitudinal rigidity identity

Let

\[
\rho_w=t_s/l_s,\qquad t_c=h-2t_s,\qquad n_sl_s=b.
\]

Zhou's loading-direction rigidity is

\[
D_y=D_{y,s}+D_{y,c},
\]

\[
D_{y,s}=\frac{E_s}{b}\left[\frac{bh^3}{12}-\frac{n_s(l_s-t_s)t_c^3}{12}\right],
\]

\[
D_{y,c}=\frac{E_c}{b}\frac{n_s(l_s-t_s)t_c^3}{12}.
\]

Because

\[
\frac{n_s(l_s-t_s)}{b}=1-\rho_w,
\]

we obtain

\[
D_{y,s}=E_s\frac{h^3-t_c^3}{12}+\rho_wE_s\frac{t_c^3}{12},
\]

\[
D_{y,c}=(1-\rho_w)E_c\frac{t_c^3}{12}.
\]

These are exactly the H0 components `outer faceplates + homogenized longitudinal web steel + remaining concrete`. Hence

\[
\boxed{D_{y,H0}^{elastic}=D_{y,Zhou}^{elastic}}.
\]

This identity is algebraic and contains no fitting.

## 3. Z6 numerical consequence

For Z6 (`a=9000, b=12000, h=130, ts=4, tc=122, ls=200, rho_w=0.02, Es=206000 MPa, Ec=32500 MPa`):

```text
D_outer_y = 6.543109333e9 N mm
D_web_y   = 0.623441147e9 N mm
D_conc_rem= 4.819563233e9 N mm
D_y,H0    = 11.986113713e9 N mm
D_y,Zhou  = 11.986113713e9 N mm
```

Using the same Zhou elastic stiffness bookkeeping as a diagnostic for the other directions/couplings, H0 differs only modestly:

```text
Dx,H0 / Dx,Zhou - 1   = -0.8582 %
H,H0  / H,Zhou  - 1   = -2.2073 %
Pcr,H0 / Pcr,Zhou - 1 = -1.1371 %
```

For m=1:

```text
Pcr,Zhou = 42.83147561 MN
Pcr,H0 elastic diagnostic = 42.34444126 MN
```

If Zhou Eqs.(5-87)-(5-88) are evaluated with the H0 elastic diagnostic `Pcr` but the exact H0/full-section `Pyth=88.089888 MN`, the lower-envelope value is

```text
lambda_H0 = 1.442330627
phi_H0,lower = 0.563252309
P_H0,lower_equiv = 49.61683284 MN
```

versus Zhou original full

```text
49.67243594 MN
```

only `-0.11194%` different.

Thus a large missing **elastic** orthotropic web rigidity cannot explain the roughly 10% H0 fixed-state shortfall below the Zhou lower envelope.

## 4. Current-state steel tangent diagnostic

At the persisted Z6 H0 old state

```text
D=0.705
q=0.0058975999
q0=0.0015
```

the existing H0 material-coordinate radial-cap compiler was differentiated analytically and composed with the continuous Nguyen field. Structural integration remains exact coefficient-space D15; there are zero structural x/y/z points.

For the uniaxial web map

\[
\sigma_w=f_yu\alpha(r),\quad r=u^2,
\]

\[
\frac{E_{t,w}}{E_s}=\alpha(r)+2r\alpha'(r).
\]

With the persisted H0 degree-24 `[0,4]` material compiler:

```text
web volume-mean Et/Es       = 0.998987
web z^2-weighted Et/Es      = 0.996436
```

For the outer-shell local radial current map, the loading-direction derivative is

\[
C_{t,yy}=\alpha C^E_{yy}+\sigma_y^E\alpha'(r)\,\partial r/\partial\varepsilon_y.
\]

Using the same degree-24 `[0,4]` H0 checkpoint compiler gives z^2-weighted retention:

```text
negative face = 0.977664
positive face = 1.000230
combined outer-shell = 0.988947
```

The slight value above unity on the almost-elastic face is compiler ripple of order 2e-4 and is not interpreted as hardening.

Combining outer steel plus the homogenized web steel by their elastic longitudinal bending contributions gives approximately

```text
combined longitudinal steel tangent retention = 0.989598
```

Therefore an immediate wholesale steel-tangent collapse at the old `D=0.705` state is also not supported.

## 5. Corrected causal hierarchy

```text
OLD OMITTED WEB-STEEL AXIAL MATERIAL = CONFIRMED MAJOR PARTIAL CAUSE
LARGE MISSING ELASTIC H0 WEB RIGIDITY = REJECTED AS DOMINANT Z6 CAUSE
IMMEDIATE WHOLE-STEEL TANGENT COLLAPSE AT D=0.705 = NOT SUPPORTED
DEEP FINITE-AMPLITUDE EQUILIBRIUM RELOCATION = CONFIRMED ACTIVE AXIS
CONCRETE/CURRENT-TANGENT + GEOMETRIC-STIFFNESS BALANCE ON NEW H0 BRANCH = PRIMARY OPEN CAUSAL TARGET
DISCRETE-WEB TOPOLOGY MAY STILL MATTER NONLINEARLY = OPEN, NOT PROVEN BY ELASTIC STIFFNESS
N48 H0 DOMAIN EXHAUSTION = REAL COMPUTATIONAL/REPRESENTATION GATE
```

The prior broad statement `H0 longitudinal web material without full orthotropic/topological restraint = strongest hypothesis` is therefore superseded by the narrower statement above.

## 6. Next executable gate

A full same-branch `KZ` result cannot yet be honestly released because the H0 `Rq=0` branch leaves the currently validated concrete N48 material domain before the new equilibrium state is recovered. In addition, the committed H0 implementation persists `P,Rq` but not yet the full directional differentiated H0 `KZ` operator along that new branch.

The next task is therefore

```text
CURRENT_NEXT_TASK = Z6_H0_ANALYTIC_DOMAIN_AND_FULL_DIRECTIONAL_TANGENT_KZ_GATE
```

It must:

1. determine the required concrete material-coordinate domain from analytic bounds, not structural sampling;
2. compile the same frozen R10 target over that justified domain without structural calibration;
3. differentiate the existing H0 web and shell current maps into their full directional tangents;
4. recover the connected H0 `Rq=0` branch;
5. persist `Pc,Pw,Psh,Rq_c,Rq_w,Rq_sh,KZ_c^mat,KZ_w^mat,KZ_sh^mat,KZ_geo,KZ,L`;
6. establish event ordering without Zhou/Winter loads entering root or mode selection.

No empirical Z6 factor and no spatial discretization are authorized.
