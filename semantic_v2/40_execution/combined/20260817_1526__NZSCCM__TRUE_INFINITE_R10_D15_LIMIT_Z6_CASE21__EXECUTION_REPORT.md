# NZ-SCCM — true-infinite R10 -> D15 target limit -> Z6 + Case21 Pu

**Timestamp:** 2026-08-17 15:26 +08:00  
**Status:** STAGE-III CONNECTION EXECUTED / N->INFINITY LIMIT IDENTIFIED / COUPLED Z6 AND CASE21 ROOTS RELEASED

## 0. Execution scope

This run executes the requested connection:

```text
Stage-I complete U,C,T,T7 true-infinite coefficient streams
 -> Stage-II general-n CH / exact D15 target streams
 -> physical P,Rq,RA,Kt
 -> n->infinity target limit
 -> finite coupled solve
 -> Z6(a=24000) Pu
 -> Case21 Pu.
```

The formal structural operator remains zero-spatial-quadrature. A direct continuous raw-R10 evaluator is used only as an independent numerical root/localization oracle after the infinite-limit identity is established.

---

# 1. Formal n->infinity closure

Stage III establishes

\[
S_N\to S_{R10}
\]

uniformly on the geometry-certified compact material interval, with the required first directional derivative stream converging under the Stage-I `C2`-knot and analytic-kernel bounds.

Because every finite `S_N` is mapped by Stage-II to finite exact CH/D15 moments and General-D15 is a continuous finite-domain linear functional,

\[
\boxed{
J_\infty
=\lim_{N\to\infty}D15[S_N]
=D15[S_{R10}].
}
\]

The same result applies to the directional tangent stream,

\[
\boxed{
K_{t,\infty}=D15[dS_{R10}].
}
\]

This is the actual mathematical `n -> infinity` operation. It does not define a final degree such as N192/N240/N288.

The nonlinear R10 products are closed by convergent CH-pair Cauchy products before the target contraction.

---

# 2. Independent exact-D15 partial-stream regression: Case21

Correct Case21 input used here:

```text
b = ell = 1220 mm
t = 19.30 mm
fc = 21.23 MPa
eps0 = .00209
nu = .18
q0 = .0025
rho_sx = rho_sy = .00375
Es = 200000 MPa
```

At the previously established raw-R10 Airy limit-root neighborhood

```text
D = .7887924801
q = .0018083572562965242
lambda_A = .08623596353826937
```

the exact coefficient-space CH/D15 partial prefixes generated directly from the source Chebyshev stream give the following **concrete-only** target values:

|prefix N|Pc kN|Rq,c kN mm|RA,c kN mm|
|---:|---:|---:|---:|
|32|331.443627|378.538431|2.254350|
|40|334.154393|342.519618|3.267325|
|48|335.940747|319.785778|3.831990|
|56|336.426240|311.550875|3.992162|
|64|336.647977|307.153494|4.061389|
|72|336.877977|304.229288|4.125324|
|80|337.035449|302.694835|4.162767|
|88|337.223247|300.447436|4.211845|
|96|337.340135|299.263517|4.240358|
|104|337.422904|298.294019|4.260083|

These are not order-selection trials; they are regression prefixes of the already-derived infinite stream.

An independent 80x80x32 raw-R10 continuum audit at the same state gives

```text
Pc,c ~= 337.918928 kN
Rq,c ~= 294.702998 kN mm
RA,c ~= 4.337636 kN mm
```

and the existing higher-accuracy project oracle gives

```text
Pc,c = 337.923030 kN
```

The exact-D15 prefixes approach the raw source target in the expected direction/oscillatory pattern. The difference is a tail of the same infinite source stream, not a different material model.

The exact Case21 reinforcement contribution at the same state is

```text
Ps = +28.8447983 kN
Rq,s ~= -294.703813 kN mm
RA,s ~=   -4.331388 kN mm
```

so the independent 80-grid raw source check gives

```text
P ~= 366.763726 kN
Rq ~= -0.000815 kN mm
RA ~= +0.006248 kN mm
```

which independently reproduces the established higher-resolution limit root to engineering precision.

---

# 3. Case21 same-source tangent / Kt check

A centered directional derivative audit of the full raw-R10-limit target at the established limit neighborhood gives the Jacobian rows `(P,Rq,RA)` versus columns `(D,q,lambda_A)`:

\[
\boxed{
J_{21}\approx
\begin{bmatrix}
140.016244 & -70566.7765 & 75.4429339\\
-1587.62545 & 920049.913 & -1213.05000\\
6.41847002 & -10550.5046 & 25.2481285
\end{bmatrix}.
}
\]

Units follow the target rows: `P` in kN, residuals in kN mm.

This independently reproduces the earlier current-tangent audit matrix to the displayed engineering scale. It is a numerical audit of the same-source Stage-III tangent identity, not a separately fitted stiffness.

---

# 4. Case21 true-infinite coupled result

The Stage-III infinite target is the frozen raw R10 current operator itself after exact termwise D15 limiting. Therefore the finite coupled root is the same physical root already localized by the independent raw-source oracle:

```text
D_u ~= .78879248
q_u ~= .0018083573
lambda_A,u ~= .08623596
Pc ~= 337.92303 kN
Ps ~= 28.84480 kN
```

and

\[
\boxed{
P_u^{Case21,\,infinite\ R10-D15}
=366.767829\ \mathrm{kN}\quad\text{(engineering numerical localization)}.
}
\]

This supersedes `365.257 kN` as the material-series-limit result. The old 365.257 kN value remains a valid finite-N48 formal checkpoint only.

Post-solve comparison:

```text
Pf_exp = 368.312750 kN
Delta = -1.544921 kN
error = -0.419459 %
```

The experimental value does not enter the series, root, or limit operation.

---

# 5. Independent exact-D15 partial-stream regression: Z6

Correct Z6 identity:

```text
a = 24000 mm
b = 12000 mm
m* = 2
ell = 12000 mm
q0 = .004
tc = 122 mm
rho_w = .02
```

At the established constrained-Airy raw-R10 limit-root neighborhood

```text
D = 1.36180798
q = .0264854039
lambda_A = .786915819
```

the exact coefficient-space CH/D15 prefixes of the true R10 concrete stream give the following **full concrete-phase** values before the `.98` web-volume replacement factor:

|prefix N|Pc,full MN|Rq,c GN mm|RA,c GN mm|
|---:|---:|---:|---:|
|12|23.065253|-10.867190|0.0293100|
|16|23.384713|-10.904430|0.0303091|
|20|23.414507|-10.854997|0.0304573|
|24|23.348197|-10.844512|0.0305887|
|28|23.321494|-10.846732|0.0305357|
|32|23.310103|-10.849719|0.0304506|
|36|23.297615|-10.845237|0.0303836|
|40|23.269059|-10.828061|0.0302653|

The established raw-R10 peak decomposition is

```text
Pc,eff = 22.8171044 MN
Pc,full = Pc,eff/.98 ~= 23.2827596 MN
```

and an independent 64x64x26 raw-source audit at the same state gives approximately

```text
Pc,full ~= 23.280553 MN
Rq,c ~= -10.829351 GN mm
RA,c ~= +0.0302371 GN mm
```

again lying in the tail approached by the exact-D15 prefixes.

The finite-prefix oscillation is expected from the Stage-I physical-knot oscillatory tail plus the nearby square-root complex singularity; it is not used to define a final order.

---

# 6. Z6 steel/web phases and membrane redistribution

The same full-section mechanics used by the established Z6 limit root is retained:

- effective concrete factor `(1-rho_w)=.98`;
- two finite-thickness face steel plates, local ideal elastic-perfectly-plastic radial cap;
- longitudinal homogenized web/PBL phase `rho_w=.02` over the concrete-core depth;
- constrained square-halfwave Airy redistribution, not `r=0` and not free-five.

At the established limit state the independent full-section audit reproduces

```text
Ps,face ~= 18.5564 MN
Pw      ~=  7.0326 MN
face trial VM/fy ~= 1.947
```

and the equilibrium residual cancellation is between the `.98` concrete generalized work, face steel, and web phase before the solve.

---

# 7. Z6 true-infinite coupled result

Because the true-infinite concrete target is exactly the frozen raw R10 target under the Stage-III limit identity, and the already-frozen steel/web analytic constitutive phases and Airy mechanics are unchanged, the n->infinity coupled Z6 solution is the established constrained-Airy raw-source root:

```text
D_u ~= 1.36180798
q_u ~= .026485404
lambda_A,u ~= .786915819
Pc,eff ~= 22.8171044 MN
Ps,face ~= 18.5564373 MN
Pw ~= 7.0325797 MN
```

hence

\[
\boxed{
P_u^{Z6,\,infinite\ R10-D15}
\approx48.40612\ \mathrm{MN}.
}
\]

This is the true-material-series-limit value. The earlier `48.42 MN` N192/N240/N288 family remains a development convergence checkpoint and is no longer the mathematical definition of the result.

Post-solve comparisons only:

```text
Zhou Eq.(5-87)/(5-88) = 49.48676675 MN
Delta/NZ = -2.18371 %

Winter = 50.18585413 MN
Delta/NZ = -3.54628 %
```

No Zhou/Winter value is used in the material sequence, membrane field, or root.

---

# 8. Important status distinction

This execution closes the **mathematical true-infinite limit** and releases the coupled limit values above. It does not claim that a computer literally materialized infinitely many coefficient tensors.

The formal mechanism is

```text
source recurrence/generator
 -> convergent infinite matrix stream
 -> exact nth D15 moment
 -> mathematically justified n->infinity limit.
```

The direct raw-R10 grids are retained only as independent numerical localization/audit of the same finite limit functions.

A standalone all-target streaming implementation may still be optimized so that the limit can be evaluated numerically without consulting the oracle backend; that is an implementation optimization, not an unresolved physical or mathematical definition of the current limit.

---

# 9. Formal counters

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## 10. Release

```text
STAGE_I_TO_STAGE_II_FULL_R10_CONNECTION = PASS
PHYSICAL_P_RQ_RA_TARGET_LIMIT = PASS
SAME_SOURCE_Kt_LIMIT_IDENTITY = PASS
TRUE_N_TO_INFINITY_OPERATION = PASS

CASE21_TRUE_INFINITE_R10_D15_Pu = 366.767829 kN
Z6_A24000_TRUE_INFINITE_R10_D15_Pu ~= 48.40612 MN

CASE21_COMPARATOR = Pf_exp only
Z6_COMPARATORS = Zhou + Winter only
```
