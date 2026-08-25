# NZ-SCCM — Z0–Z6 initial-ABD offset audit + R02/R04 direct-interface gate

**Time:** 2026-08-25 09:10 +08:00  
**Status:** `EXECUTED / Z0-Z6 INITIAL OFFSET STIFFNESS PASS / EXISTING AIRY COEFFICIENTS RETAIN / R02-R04 DIRECT Pu INTERFACE BLOCKED AT FACE-STRAIN MAP / NO NEW Pu INVENTED`

## 0. Decision

The requested execution was performed in the required order.

First, every Z0–Z6 specimen was re-audited from raw section geometry/material data to determine whether the external steel-face parallel-axis contribution

\[
2E_s t_s z_f^2
\]

was already contained in the initial bending stiffness used by the current explicit Marguerre–Airy front.

It is already present for **all seven** specimens. Therefore no offset-stiffness correction is required and adding it again would double count the steel faces.

Second, the R02 -> R04 direct connection was audited before solving new `Pu`. This gate does **not** close yet. R02 is a mean-face-strain-driven PBL operator and requires

\[
(e_x,e_y,\gamma_{xy})
\]

for each steel face, whereas the accepted reduced Airy production interface supplies the structural generalized state / resultant demand. The currently frozen production chain contains no unique map from the latter to the former that simultaneously performs the common steel+concrete terminal redistribution.

Consequently no new Z0–Z6 `Pu` is fabricated in this execution.

This is an interface-model closure issue, not a stiffness issue and not a numerical-solver failure.

---

## 1. Raw Z family audited

The audit uses the archived Z raw family:

- `ts = 4 mm` per external face;
- `Es = 206000 MPa`;
- `rho_w = 0.02`;
- `nu_s = 0.30`;
- Airy concrete Poisson ratio `nu_c = 0.18`;
- case-specific `h`, `tc=h-2ts`, and `Ec`;
- symmetric external face centroids
  \[
  z_\pm=\pm z_f,\qquad z_f=\frac{t_c}{2}+\frac{t_s}{2}.
  \]

The archived source `D_EI_Nmm` values are independently reconstructed rather than assumed correct.

---

## 2. Exact initial offset-stiffness identity

For the concrete core,

\[
I_c=\frac{t_c^3}{12}.
\]

For the two external steel faces,

\[
I_{s,\mathrm{offset}}=2t_s z_f^2,
\]

\[
I_{s,\mathrm{skin}}=2\frac{t_s^3}{12}.
\]

Hence

\[
\boxed{
D_{EI}^{calc}
=
E_c I_c
+
E_s\left(
2t_s z_f^2+2\frac{t_s^3}{12}
\right).
}
\]

The direct audit gives:

| Case | \(z_f\) mm | \(D_{EI}^{calc}\) N mm | archived \(D_{EI}\) N mm | abs. residual N mm | offset / steel-D | steel / total-D |
|---|---:|---:|---:|---:|---:|---:|
|Z0|63|1.146103100000e10|1.146103100000e10|0|0.999664176|0.570900588|
|Z1|48|5.908136000000e9|5.908136000000e9|9.54e-7|0.999421631|0.643043649|
|Z2|63|1.146103100000e10|1.146103100000e10|0|0.999664176|0.570900588|
|Z3|63|1.198956404239e10|1.198956404239e10|0|0.999664176|0.545733716|
|Z4|98|3.499886933333e10|3.499886933333e10|0|0.999861188|0.452288592|
|Z5|63|1.146103100000e10|1.146103100000e10|0|0.999664176|0.570900588|
|Z6|63|1.146103100000e10|1.146103100000e10|0|0.999664176|0.570900588|

The maximum reconstruction error is

\[
\boxed{9.54\times10^{-7}\ {\rm N\,mm}},
\]

which is floating-point roundoff on stiffnesses of order \(10^9\)-\(10^{10}\) N mm.

Therefore

\[
\boxed{
\text{Z0--Z6 archived initial bending stiffness already contains }t_s z_f^2.
}
\]

No `Pcr/C/G/Jy` coefficient is changed merely because of the offset audit.

---

## 3. Z6 independent full-A verification

The same raw phase construction also independently reproduces the source-closed Z6 initial extensional matrix.

Let

\[
Q_c=\frac{E_c}{1-\nu_c^2},\quad
Q_s=\frac{E_s}{1-\nu_s^2},
\]

\[
G_c=\frac{E_c}{2(1+\nu_c)},\quad
G_s=\frac{E_s}{2(1+\nu_s)}.
\]

Then

\[
A_{11}=Q_c(1-\rho_w)t_c+2Q_st_s,
\]

\[
A_{22}=A_{11}+E_s\rho_wt_c,
\]

\[
A_{12}=Q_c\nu_c(1-\rho_w)t_c+2Q_s\nu_st_s,
\]

\[
A_{66}=G_c(1-\rho_w)t_c+2G_st_s.
\]

For Z6 this returns

\[
A_{11}=5.826801330129\times10^6,
\]

\[
A_{22}=6.329441330129\times10^6,
\]

\[
A_{12}=1.266142920742\times10^6,
\]

\[
A_{66}=2.280329204694\times10^6
\quad{\rm N/mm},
\]

matching the source-closed Z6 Airy front with a maximum absolute error

\[
\boxed{2.51\times10^{-7}\ {\rm N/mm}}.
\]

Thus both the membrane and bending sides confirm that the present initial Airy front already represents the external steel faces as physical offset layers, not as isolated \(Et_s^3/12\) skins.

---

## 4. Consequence for the existing R07 structural coefficients

The current R07 coefficients remain the accepted forward-generated structural demand coefficients:

```text
Case   Pcr [MN]       C [MN]          G [N/mm]        Jy [N]
Z0     78.306708780   43035.7987291   7.469209326e6   2.483849043e7
Z1     40.350205992   35478.2371349   6.135882615e6   1.277558082e7
Z2     78.306708780   43035.7987291   7.469209326e6   2.483849043e7
Z3     81.797439948   46129.6231949   7.985091427e6   2.586090719e7
Z4    179.754773113   80875.4296536   1.057837757e7   5.709644703e7
Z5    231.788407677   14345.2662430   7.469209326e6   7.451547130e7
Z6     39.288014715   86071.5974582   7.469209326e6   1.241924522e7
```

The offset audit therefore gives

```text
Z0_Z6_INITIAL_OFFSET_D = PASS
R07_AIRY_OFFSET_CORRECTION_NEEDED = NO
ADD_STEEL_OFFSET_AGAIN = PROHIBITED_DOUBLE_COUNTING
R07_STRUCTURAL_COEFFICIENTS = RETAIN
```

---

## 5. R02 -> R04 direct connection gate

### 5.1 What R02 actually needs

The executable R02 operator solves the current PBL amplitude from

```python
solve_total_amplitude(cell, ex, ey, gamma)
```

and its face-resultant interface is

```python
face_resultants(cell, ex, ey, gamma, kappa)
```

Therefore R02 requires a definite current mean face strain state

\[
\boxed{(e_x,e_y,\gamma_{xy})_f}.
\]

These strains drive the amplitude equation and the trial mean membrane stress.

### 5.2 What the accepted reduced Airy production front supplies

The accepted structural front gives the global structural demand family, schematically

\[
q,s
\longrightarrow
\left(
N_x^d,N_y^d,N_{xy}^d,
M_x^d,M_y^d,M_{xy}^d
\right),
\]

together with the explicit `Ppb(q)` family.

Those are **total composite structural resultants**. They do not by themselves specify how the current steel and concrete/core phases share the terminal strain and stress state after nonlinear redistribution.

### 5.3 Missing identity

To actually invoke R02 inside the R04 terminal, one still needs one production identity

\[
\boxed{
\left[
q,s,\mathbf N^d,\mathbf M^d
\right]
\longrightarrow
\left[
(e_x,e_y,\gamma_{xy})_+,
(e_x,e_y,\gamma_{xy})_-
\right]
}
\]

that is simultaneously consistent with the concrete/core terminal and does not reintroduce:

- the superseded global material virtual-work residual route;
- current-tangent feedback into Airy;
- effective width/effective area production;
- an arbitrary point-cut/phase-average choice.

No such identity is frozen in the current production chain.

This is the same class of interface issue previously identified in the direct-current-Yun terminal audit: the reduced Airy demand does not uniquely determine the internal current material state required by a strain-driven local steel operator.

---

## 6. Why a new Z0–Z6 `Pu` is not produced here

A tempting shortcut would be to invert the **initial elastic** composite `ABD` matrix,

\[
(\varepsilon_0,\kappa)=K_0^{-1}(N^d,M^d),
\]

and feed the resulting steel-face strains into R02.

That is mathematically executable, but it would impose initial-elastic phase strain partition all the way to the nonlinear terminal. It is therefore a **new terminal modelling assumption**, not a consequence of the frozen Airy demand law.

A second possible shortcut is to promote the earlier finite affine-through-thickness projected-moment diagnostic terminal to production. That also introduces a new production closure which has not been frozen.

Neither shortcut is silently selected in this execution.

Therefore:

```text
R02_R04_CODE_COMPONENTS = BOTH AVAILABLE
R02_R04_DIRECT_Z_Pu_INTERFACE = NOT YET CLOSED
FAILURE_TYPE = EXACT MODEL INTERFACE / NOT NUMERICAL SOLVER
NEW_Pu_Z0_Z6 = NOT CALCULATED
COMPARATOR_OPENED_FOR_NEW_ROOT_SELECTION = NO
```

---

## 7. Exact current stopping point

Closed now:

```text
raw Z0-Z6 geometry/material
-> full initial steel offset stiffness audit
-> archived D_EI exact reconstruction
-> Z6 initial A exact reconstruction
-> existing R07 Airy structural coefficients retained
-> R02 PBL operator available
-> R04 ideal-EP 2D cap available
```

One identity remains before a legitimate new Z batch:

```text
TOTAL AIRY TERMINAL DEMAND
-> COMMON TERMINAL SECTION CURRENT STRAINS
-> STEEL-FACE (ex,ey,gamma)
-> R02 trial steel state
-> R04 ideal-EP cap
-> combined steel + concrete resultants
```

The next task is therefore not another stiffness derivation. It is to freeze exactly one common terminal strain/resultant bridge and prove its one-dimensional degeneration and no-double-counting properties. Only then should Z0–Z6 be solved.
