# NZ-SCCM R13 — Case21 / Z6 unbuckled-branch overprediction diagnosis

**Date:** 2026-08-19  
**Formal discretization:** NONE  
**Purpose:** identify why the previous Case21 `q=0, alpha=0` smoke-test load is much higher than the real plate limit, then run the identical zero-discretization unbuckled-branch calculation for Z6.

## 1. Diagnosis: the 538.273 kN Case21 value is not a plate Pu

The previous trial solved only the trivial uniform branch

\[
q=0,\qquad \alpha=0,
\]

and then imposed

\[
\frac{dP(D,0,0)}{dD}=0.
\]

That is a material/section stationary point. It is **not** the governing structural limit condition

\[
R_q=0,\qquad R_\alpha=0,\qquad \det J_{\lim}=0.
\]

On the trivial branch, the initial imperfection only enters the Nguyen membrane scale through `q0*q`; therefore at `q=0`,

\[
M=0,\qquad B=0,
\]

and the imperfection does not activate the nonuniform postbuckling strain redistribution. Hence this branch suppresses the mechanism whose purpose is to reduce/redistribute the load before the material section peak.

For Case21:

```text
unbuckled stationary P* = 538.273498279198 kN
exact elastic Navier Pcr = 407.136279059126 kN
D at Pcr on the uniform branch = 0.478843845165660
D at uniform-branch stationary point = 1.083794870106547
released coupled Pu = 366.767828685212 kN
experimental comparator = 368.312749743569 kN
```

Thus the uniform branch exceeds experiment by

\[
+46.1458\%.
\]

The reason is not the R13 spline identity; it is that `dP(D,0,0)/dD=0` is the wrong structural limit problem.

## 2. Z6 inputs and exact uniform branch

Use the frozen Z6 section/material identity:

```text
b = 12000 mm
core tc = 122 mm
face steel ts = 4 mm each
rho_w = 0.02
fc = 30.4 MPa
eps0 = 0.0018712490394580678
nu_c = 0.18
Es = 206000 MPa
fy = 355 MPa
nu_s = 0.30
```

Areas:

\[
A_{c,eff}=0.98\,b t_c=1,434,720\ \mathrm{mm^2},
\]

\[
A_{face}=2bt_s=96,000\ \mathrm{mm^2},
\]

\[
A_w=\rho_wbt_c=29,280\ \mathrm{mm^2}.
\]

Set again

\[
q=0,\qquad \alpha=0.
\]

The concrete field is uniform and uses the same exact finite R10 scalar compression response

\[
S_{yy}(D)
=-\kappa D-C(D)+\kappa c(D)+u_R(t(D)/x_{cr})-\kappa t(D).
\]

Therefore

\[
P_c(D)=-A_{c,eff} f_c S_{yy}(D).
\]

## 3. Z6 face steel on the same uniform branch

Physical uniform strains are

\[
\varepsilon_x=\nu_c D\varepsilon_0,\qquad
\varepsilon_y=-D\varepsilon_0,\qquad
\gamma=0.
\]

The plane-stress elastic trial stresses are exactly linear in `D`:

\[
\sigma_x^{tr}=-50.8321717092345\,D\ \mathrm{MPa},
\]

\[
\sigma_y^{tr}=-400.726953641132\,D\ \mathrm{MPa},
\]

and the von-Mises trial magnitude is

\[
v=377.883817778924\,D\ \mathrm{MPa}.
\]

Hence the face radial-cap activates at

\[
D_{y,f}=\frac{355}{377.883817778924}
=0.939442186454484.
\]

After cap activation, the stress direction is unchanged and the stress vector is constant:

\[
\sigma_{x,f}=-47.7538865327531\ \mathrm{MPa},
\]

\[
\sigma_{y,f}=-376.459805499870\ \mathrm{MPa},
\]

with exact von-Mises magnitude `355 MPa`.

Thus both faces contribute, after the cap,

\[
P_{face}=36.1401413279875\ \mathrm{MN}.
\]

## 4. Z6 web steel

The web strain is simply

\[
\varepsilon_y^w=-D\varepsilon_0.
\]

The ideal-EP web reaches yield at

\[
D_{y,w}=\frac{355}{206000\times0.0018712490394580678}
=0.920936195308814.
\]

Thereafter

\[
\sigma_y^w=-355\ \mathrm{MPa},
\]

so

\[
P_w=A_w f_y=10.3944000000000\ \mathrm{MN}.
\]

## 5. Z6 exact unbuckled stationary point

Both steel phases have already plateaued before the concrete compression maximum. Therefore the total branch stationary point is the exact R10 concrete stationary point

\[
\frac{dS_{yy}}{dD}=0,
\]

which gives

\[
\boxed{D_*=0.999995310340506}.
\]

At this state

\[
S_{yy}=-1.000009372542488.
\]

Hence

\[
\boxed{P_{c,eff}=43.6158967880144\ \mathrm{MN}},
\]

\[
\boxed{P_{face}=36.1401413279875\ \mathrm{MN}},
\]

\[
\boxed{P_w=10.3944000000000\ \mathrm{MN}},
\]

and

\[
\boxed{P_*^{Z6}=90.1504381160020\ \mathrm{MN}}.
\]

No spatial quadrature, grid, material point, finite prefix, or discrete oracle is used.

## 6. Compare with structural instability scale

The frozen exact Navier controlling mode for Z6 is

\[
\boxed{P_{cr}=39.2880147150278\ \mathrm{MN}}.
\]

On the exact uniform branch this load is reached already at

\[
\boxed{D(P_{cr})=0.303002225781078},
\]

far before web yield (`0.92094`), face yield (`0.93944`) and the material stationary point (`~1.00000`).

The previously released full coupled Z6 result is

\[
P_u=48.4061215\ \mathrm{MN},
\]

with Zhou comparator

\[
49.4867667519\ \mathrm{MN}
\]

and Winter comparator

\[
50.1858541295\ \mathrm{MN}.
\]

Post-solve comparison of the **uniform material branch** gives:

```text
vs released coupled Pu: +86.2377 %
vs Zhou comparator:      +82.1708 %
vs Winter comparator:    +79.6332 %
```

Therefore the severe overprediction is not a Case21-specific accident. It is a systematic property of using the uniform material/section stationary point as a substitute for the coupled plate limit.

## 7. Mechanistic conclusion

The error source is now isolated:

1. `q=alpha=0` suppresses the nonuniform buckling/postbuckling branch;
2. `q0` cannot act by itself because the Nguyen membrane coupling contains `q0*q` and vanishes when `q=0`;
3. the calculation uses `dP(D,0,0)/dD=0`, whereas the formal plate limit is `Rq=0, Ralpha=0, det(Jlim)=0`;
4. the discrepancy grows strongly when the structural instability scale lies far below the material section capacity. Z6 is the clearer example: `Pcr/P*_uniform = 43.58%`, compared with `75.64%` for Case21.

Hence:

```text
R13 finite material constructor overprediction = NOT ESTABLISHED
UNBUCKLED-BRANCH-AS-Pu = REJECTED
FULL COUPLED (D,q,alpha) LIMIT SYSTEM = REQUIRED
```

The correct next execution is not another uniform-branch specimen. It is the full zero-discretization coupled `P,Rq,Ralpha,Jlim` solve using the same R13 finite material constructor.
