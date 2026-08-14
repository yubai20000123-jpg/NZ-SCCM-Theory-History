# NZ-SCCM vs Zhou empirical formula — reduced-reference numerical comparison

**Timestamp:** 2026-08-14 21:41 +08:00  
**Object:** same reduced four-edge simply-supported concrete + two outer steel-faceplate object  
**Purpose:** numerical comparison requested by user; persist inputs, intermediate values and comparison for later audit.

## 1. Governance and identity

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
EXPERIMENTAL_LOAD_USED_FOR_TUNING = NO
```

NZ-SCCM parent chain remains:

```text
R10 ordinary-concrete current operator
-> N48-C1/MM
-> Cayley-Hamilton 2D lift
-> Nguyen second-order complete-halfwave kinematics
-> general D15 exact moments
-> P(D,q), Rq(D,q), L(D,q)
-> current-tangent Zhou/Navier audit
```

The steel-shell extension replaces the reinforcement term by two continuous finite-thickness faceplate shell contributions. No spatial Gauss/Simpson/material-point grid is introduced.

**Important result identity:** the only persisted NZ-SCCM numerical load for this exact reduced object is the historical diagnostic branch-peak-neighbourhood value `26.1085 MN` recorded in the 16:06 checkpoint. Its corresponding `D,q` and component tangents were not persisted; therefore this report does **not** relabel it as a newly certified production `Rq=0 + L=0` root.

## 2. Same-object input

```text
a = 6000 mm
b = 6000 mm
h = 130 mm
ts = 4 mm per faceplate
concrete core thickness = 122 mm
Ac = 6000*122 = 732000 mm2
As = 2*6000*4 = 48000 mm2
fy = 355 MPa
Es = 206000 MPa
fcu = 40 MPa
fc' = 0.76 fcu = 30.4 MPa
Ec = 32500 MPa
internal web steel bearing term = 0
```

Section strength reference:

\[
P_{s,0}=f_yA_s=17.0400\ \mathrm{MN},
\]

\[
P_{c,0}=f'_cA_c=22.2528\ \mathrm{MN},
\]

\[
P_{yth}=P_{s,0}+P_{c,0}=39.2928\ \mathrm{MN}.
\]

## 3. NZ-SCCM numerical result

The same-object persisted NZ-SCCM diagnostic result is

\[
\boxed{P_{NZ,diag}=26.1085\ \mathrm{MN}}.
\]

Normalized by the same reduced section strength:

\[
\frac{P_{NZ,diag}}{P_{yth}}
=0.664460155550.
\]

This is a genuine previously calculated NZ-SCCM branch value, but its formal identity remains `DIAGNOSTIC_BRANCH_PEAK_NEIGHBOURHOOD`, not `NEWLY_CERTIFIED_PRODUCTION_LIMIT_ROOT`.

## 4. Zhou empirical Eqs. (5-87)-(5-88)

For the same reduced-object diagnostic elastic rigidity,

\[
I_c=\frac{(h-2t_s)^3}{12}=151320.666666667\ \mathrm{mm^3},
\]

\[
I_s=\frac{h^3-(h-2t_s)^3}{12}=31762.666666667\ \mathrm{mm^3},
\]

\[
D_{EI}=E_cI_c+E_sI_s=1.146103100000\times10^{10}\ \mathrm{N\,mm}.
\]

Under the same square isotropic reduced diagnostic used in the existing checkpoint,

\[
P_{cr}=\frac{4\pi^2D_{EI}}{b}=75.4105613324\ \mathrm{MN}.
\]

Thus

\[
\lambda_n=\sqrt{\frac{P_{yth}}{P_{cr}}}
=0.721839098657.
\]

Because `lambda_n <= 1`, Zhou Eq. (5-88) gives

\[
\Phi_N=0.454+0.192\lambda_n+0.416\lambda_n^2
=0.809350607632.
\]

Because `lambda_n > 0.55`, Zhou Eq. (5-87) gives

\[
\phi_N=\frac{1}{\Phi_N+\sqrt{\Phi_N^2-\lambda_n^2}}
=0.850769692150.
\]

The Zhou empirical ultimate/stability resistance comparator is therefore

\[
\boxed{P_{u,Zhou,emp}=\phi_NP_{yth}=33.4291233597\ \mathrm{MN}}.
\]

## 5. Direct numerical comparison

| quantity | NZ-SCCM | Zhou empirical Eq. (5-87)-(5-88) |
|---|---:|---:|
| normalized resistance | 0.66446016 | 0.85076969 |
| load / MN | **26.1085** | **33.42912336** |

Difference using Zhou empirical value as denominator:

\[
\Delta P=P_{NZ}-P_{Zhou}=-7.3206233597\ \mathrm{MN},
\]

\[
\frac{P_{NZ}}{P_{Zhou}}=0.781010609194,
\]

\[
\boxed{\frac{P_{NZ}-P_{Zhou}}{P_{Zhou}}=-21.89893908\%}.
\]

So, under this same-object reduced diagnostic convention, **NZ-SCCM is 21.90% lower than Zhou's empirical formula**.

## 6. What this comparison does and does not prove

This numerical comparison is now fully explicit and reproducible, but it does **not** establish that the current NZ-SCCM production theory is accurate to 21.9% or inaccurate by exactly 21.9%, for two reasons:

1. `26.1085 MN` is the persisted NZ diagnostic branch-peak neighbourhood; the complete post-retraction connected `D-q` path with `Y_s^- / Y_s / Y_s^+`, `Pc, Ps, Rq, L, KZ` was not persisted with that old value.
2. Zhou's empirical curve here uses the same reduced square-isotropic diagnostic `Pcr=75.4105613324 MN`; the source-exact reduced-object orthotropic `H` has not been rederived and substituted.

Therefore the correct present conclusion is:

```text
NUMERICAL_COMPARISON = AVAILABLE
P_NZ_DIAGNOSTIC = 26.1085 MN
P_ZHOU_EMPIRICAL_DIAGNOSTIC = 33.4291233597 MN
NZ_MINUS_ZHOU = -7.3206233597 MN
NZ_RELATIVE_ERROR_VS_ZHOU = -21.89893908 percent
CURRENT_HIGH_ACCURACY_VALIDATION = NOT YET DEMONSTRATED
OBSERVED_DISCREPANCY = MATERIAL / REQUIRES FULL CONNECTED D-q CAUSAL RUN
```

No parameter was tuned to reduce this discrepancy.

## 7. Persisted companion files

- `semantic_v2/40_execution/steel_shell/20260814_2141__NZSCCM_VS_ZHOU_EMPIRICAL__REDUCED_REFERENCE__PARAMS.json`
- `semantic_v2/40_execution/steel_shell/20260814_2141__NZSCCM_VS_ZHOU_EMPIRICAL__REDUCED_REFERENCE__REPRO.py`
- `semantic_v2/50_results/steel_shell/20260814_2141__NZSCCM_VS_ZHOU_EMPIRICAL__REDUCED_REFERENCE__RESULT.csv`
- this report

The next formal calculation should replace the diagnostic `P_NZ=26.1085 MN` with a newly persisted connected-branch `Rq=0 + L=0` result and retain `D,q,Pc,Ps,P,Rq,L,KZ_c^mat,KZ_s^mat,KZ^geo,KZ` around steel yield. That replacement must be performed without altering the frozen R10/N48/D15 mother theory and without calibrating against Zhou's empirical value.
