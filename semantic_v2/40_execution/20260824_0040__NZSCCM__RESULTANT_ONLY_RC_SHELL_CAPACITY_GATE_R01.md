# NZ-SCCM — Resultant-only RC shell capacity gate R01

**Time:** 2026-08-24 00:40 +08:00  
**Status:** `ARCHITECTURE_GATE = PASS_DIAGNOSTIC / RESULTANT_ONLY = YES / AIRY_UNCHANGED / SWARTZ8_ONLY / PRODUCTION_NOT_YET_FROZEN`

## 0. Decision

The terminal capacity layer is changed from a pointwise concrete material path to a finite internal-resultant feasibility problem. The structural front end is unchanged:

\[
q\to P_{pb}(q)\to (N_x^d,N_y^d,M_x^d,M_y^d).
\]

The terminal layer no longer evaluates concrete strain history, concrete point stress history, CC/TC/TT states, Cedolin–Mulas continuation, or thickness quadrature.

The literature basis is the ultimate-limit sandwich/limit-analysis family of Brøndum-Nielsen (1974) and Marti, not Shell-2000/MCFT. Shell-2000 remains useful background but is not selected because it still evaluates biaxial constitutive stress/strain states internally.

Primary source: T. Brøndum-Nielsen, *Optimum Design of Reinforced Concrete Shells and Slabs*, DTU Report R-044, 1974. The source explicitly treats arbitrary membrane forces plus bending/twisting moments, neglects tensile concrete, uses uniformly distributed concrete compression, and does not require a deformation hypothesis for its original limit analysis.

## 1. Swartz-compatible generalized sandwich variables

For one unit width of panel, retain only finite resultant variables:

\[
(c_t,c_b,C_x^t,C_x^b,C_y^t,C_y^b,S_{x,i},S_{y,i}).
\]

`c_t,c_b` are top/bottom concrete compression-block depths; `C` are concrete compression resultants; `S` are steel-layer resultants at the actual source layer ordinates `z_i`.

No fictitious outer reinforcement layer is introduced. Therefore both two-layer specimens (4,5,6,8,14) and mid-plane reinforcement specimens (9,21,23) use their actual `z_i`.

## 2. Pure resultant admissibility

Concrete tension is zero. With specimen cylinder strength `f_c` used as the specified concrete strength for this experimental-capacity diagnostic:

\[
c_t\ge0,\qquad c_b\ge0,\qquad c_t+c_b\le t,
\]

\[
-f_c c_t\le C_x^t,C_y^t\le0,
\qquad
-f_c c_b\le C_x^b,C_y^b\le0.
\]

Following the original Brøndum-Nielsen simplification, compression reinforcement is not credited in R01. For each actual reinforcement layer,

\[
0\le S_{x,i}\le A_{sx,i}f_y,
\qquad
0\le S_{y,i}\le A_{sy,i}f_y.
\]

The project-corrected Swartz mapping is retained:

\[
\rho_x=\rho_y=p/2,
\]

and the directional steel area is divided equally among the source reinforcement layers. `f_y=530 MPa` follows `E_s=200000 MPa` and source yield strain `0.00265`.

The source measured cylinder strength is used here rather than Nguyen's separate FE analysis reduction `0.85 f_c`; this choice is fixed before comparison with `P_f` and is not calibrated to the 8-panel results.

## 3. Resultant equilibrium only

Concrete block centroids are

\[
z_t=t/2-c_t/2,
\qquad
z_b=-t/2+c_b/2.
\]

Membrane equilibrium:

\[
N_x^u=C_x^t+C_x^b+\sum_i S_{x,i}=N_x^d(q),
\]

\[
N_y^u=C_y^t+C_y^b+\sum_i S_{y,i}=N_y^d(q).
\]

Internal bending resultants are

\[
M_x^u=z_tC_x^t+z_bC_x^b+\sum_i z_iS_{x,i},
\]

\[
M_y^u=z_tC_y^t+z_bC_y^b+\sum_i z_iS_{y,i}.
\]

The single frozen Airy bending mode has only one work-conjugate bending equation. With the Airy curvature unit direction

\[
\mathbf d=(d_x,d_y)^T,
\]

use

\[
M_\parallel^u=d_xM_x^u+d_yM_y^u
=d_xM_x^d+d_yM_y^d=M_\parallel^d.
\]

`M_perp` is not imposed as a second terminal equilibrium equation.

## 4. Ultimate-load definition

The terminal problem is a finite static admissibility problem. The ultimate modal amplitude is

\[
q_u=\max\{q>0:\exists\,(c_t,c_b,C,S)\ \text{satisfying all resultant equilibrium and strength bounds}\}.
\]

Then

\[
\boxed{P_u=P_{pb}(q_u)}.
\]

This is exactly a first-contact problem between the Airy resultant curve and an RC shell resultant-capacity domain. No material loading path is required.

## 5. Fixed common-8 diagnostic

Only

\[
\{4,5,6,8,9,14,21,23\}
\]

is calculated. Existing representative-halfwave inputs and the frozen Airy front end are retained. `P_f` is comparator-only and is not used in the feasibility problem.

R01 finite-resultant diagnostic:

|Case|q_u|P_u / kN|P_f / kN|error|
|---:|---:|---:|---:|---:|
|4|0.0018100950|556.0648|534.2314|+4.09%|
|5|0.0019840636|534.2292|623.6407|-14.34%|
|6|0.0026630008|595.0867|691.6985|-13.97%|
|8|0.0012805028|488.5841|455.0531|+7.37%|
|9|0.0013185374|567.9543|625.8648|-9.25%|
|14|0.0009565348|765.6598|716.1637|+6.91%|
|21|0.0050999355|304.5437|368.3127|-17.31%|
|23|0.0031512133|341.0334|346.9613|-1.71%|

Statistics:

```text
mean signed error = -4.7766 %
MAE               =  9.3683 %
RMSE              = 10.6519 %
```

These values are a first architecture diagnostic, not a production promotion. No test load enters the solver or root selection.

## 6. Interpretation

The important result is not only the error reduction. The terminal problem has become finite and mechanically transparent:

```text
LOCAL_CONCRETE_STRAIN = REMOVED_FROM_TERMINAL
LOCAL_CONCRETE_STRESS_PATH = REMOVED
CC_TC_TT_STATE_MACHINE = REMOVED
CEDOLIN_MULAS_FOR_Pu = NOT_REQUIRED
SHELL2000_MCFT = BACKGROUND_ONLY
RESULTANT_ONLY_BRONDUM_NIELSEN_FAMILY = SELECTED_DIAGNOSTIC
TERMINAL_UNKNOWN = FINITE_INTERNAL_FORCE_RESULTANTS
THICKNESS_QUADRATURE = NONE
MATERIAL_POINTS = NONE
Pu = FIRST_AIRY_RESULTANT_CONTACT_WITH_RC_CAPACITY_DOMAIN
SWARTZ_SET = ONLY_4_5_6_8_9_14_21_23
```

## 7. Remaining gate before production

R01 deliberately keeps the original Brøndum-Nielsen simplifications: tensile concrete neglected and compression reinforcement not credited. Before production promotion, only the following should be audited, without reopening pointwise constitutive mechanics:

1. derive the finite resultant feasibility conditions into an explicit/finite algebraic active-set form rather than relying on a generic optimizer;
2. prove root exhaustion / first-contact uniqueness for each of the 8 panels;
3. audit whether the source-faithful no-compression-reinforcement assumption should be retained or whether a separately sourced resultant-level extension is justified;
4. keep all local material strain/stress histories permanently outside the Pu terminal.
