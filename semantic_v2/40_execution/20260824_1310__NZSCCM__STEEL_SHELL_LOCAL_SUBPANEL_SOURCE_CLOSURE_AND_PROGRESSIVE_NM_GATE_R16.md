# NZ-SCCM — steel-shell local-subpanel source closure and progressive `Ny-My` gate R16

**Time:** 2026-08-24 13:10 +08:00  
**Status:** `EXECUTED / Z_LOCAL_GEOMETRY_SOURCE_CLOSED / YUN_ELASTIC_PREYIELD_GATE_SOLVED / T_BH_GEOMETRY_PARTIAL / PROGRESSIVE_RESULTANT_KERNEL_CANDIDATE_ONLY / R07_R14_UNCHANGED`

## 0. Scope and architecture guard

This gate executes the R15 next task:

\[
\boxed{
\text{local steel-shell subpanel geometry}
\rightarrow
\text{progressive local-postbuckling steel effectiveness}
\rightarrow
N_y-M_y.
}
\]

It does **not** reopen concrete `TC/CC/TT` material-state classification and does not modify the Marguerre--Airy structural front.

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
POINTWISE_MATERIAL_OPERATOR = DO_NOT_REOPEN
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
```

The only admissible object to be changed later is the finite steel contribution to the same resultant capacity envelope.

---

## 1. Source hierarchy used in this gate

### 1.1 Z0--Z6 family — primary-source geometry closed

Primary source: Zhou Siming, *Stability Performance of Multi-cell Concrete-filled Steel Tubular Composite Walls under Complex Boundary Conditions*, Zhejiang University doctoral dissertation, 2022.

Zhou Table 5.3 gives the steel-tube chamber geometry used in the four-edge simply-supported family:

\[
\boxed{l_s=200\ \mathrm{mm}},\qquad
\boxed{t_s=4\ \mathrm{mm}},\qquad
\boxed{f_y=355\ \mathrm{MPa}}.
\]

For example, `n_s=30` gives `b=6000 mm` and `n_s=40` gives `b=8000 mm`. Thus `b=n_s l_s` directly identifies the repeated local chamber width. The local steel-face subpanel width is therefore

\[
\boxed{B_s^{Z}=200\ \mathrm{mm}},
\qquad
\boxed{B_s^{Z}/t_s=50}.
\]

This is distinct from the gross Marguerre--Airy wall width, which ranges to 12000 mm in Z6.

```text
Z_LOCAL_SUBPANEL_WIDTH = 200 mm
Z_LOCAL_GEOMETRY_PROVENANCE = PRIMARY_SOURCE_CLOSED
GROSS_MA_WIDTH_AS_LOCAL_WIDTH = PROHIBITED
```

### 1.2 T120 / T360 — current project geometry retained, causal provenance still partial

The current steel-shell UHPC calculation contract uses:

```text
T120 local steel-face width  = 120 mm
T360 local steel-face width  = 360 mm
steel thickness              = 4 mm
```

The historical T360 Yun branch was built with `B_s=360 mm` and the associated local amplitude/backbone parameters.

However, the independent native-CAE audits establish the common 1600 x 50 x 3000 mm gross steel-shell geometry and a T120/T360 topology difference associated with `Remove faces-1`, while the original feature-selection causality has not been fully reconstructed. The raw CAE audit therefore does **not yet independently prove** the 120/360-mm local widths from first principles.

```text
T120_Bs_120 = CURRENT_PROJECT_GEOMETRY_CONTRACT
T360_Bs_360 = CURRENT_PROJECT_GEOMETRY_CONTRACT
T120_T360_LOCAL_WIDTH_PRIMARY_GEOMETRY_CAUSAL_PROVENANCE = PARTIAL
```

### 1.3 BH005--BH050 — working local-width contract, source closure open

The current project working geometry uses

\[
\boxed{B_s=0.225B},
\]

with

```text
BH005  B_s =  56.25 mm
BH010  B_s = 112.50 mm
BH020  B_s = 225.00 mm
BH032  B_s = 360.00 mm
BH050  B_s = 562.50 mm
```

This is sufficient for a deterministic **conditional mechanism screen**, but the current archive itself asks for independent geometry verification. It is therefore not promoted here to a primary-source-closed geometry identity.

```text
BH_Bs_0P225B = CURRENT_WORKING_GEOMETRY
BH_LOCAL_WIDTH_PRIMARY_SOURCE_PROVENANCE = OPEN
```

No old 32-mm web-height identity is reintroduced by this gate.

---

## 2. Source-independent lower bound for the Yun elastic local-buckling gate

For the one-side-constrained Yun-type elastic local plate, the current analytical family has the minimum elastic local-buckling coefficient

\[
\boxed{k_{cr,\min}=\frac{32}{3}}.
\]

Therefore, irrespective of the longitudinal aspect-ratio choice inside this family,

\[
\boxed{
\sigma_{cr,\min}
=
\frac{32}{3}
\frac{\pi^2E_s}{12(1-\nu_s^2)}
\left(\frac{t_s}{B_s}\right)^2.
}
\]

Using the frozen steel constants

\[
E_s=206000\ \mathrm{MPa},\qquad
\nu_s=0.30,\qquad
f_y=355\ \mathrm{MPa},
\]

the unique slenderness at which this lower bound first equals yield is

\[
\boxed{
\left(\frac{B_s}{t_s}\right)_{\sigma_{cr,\min}=f_y}
=74.79496253.
}
\]

Hence the following is a rigorous necessary-condition gate for **elastic local buckling before steel yield**:

\[
\boxed{
B_s/t_s<74.79496253
\Longrightarrow
\sigma_{cr}>f_y
\quad\text{for every aspect ratio in this Yun elastic family}.
}
\]

This is stronger than testing one assumed longitudinal local length because it uses the global minimum of the elastic coefficient.

---

## 3. Deterministic cross-family screen

|Family/case|`B_s` mm|`B_s/t_s`|`sigma_cr,min` MPa|`sigma_cr,min/f_y`|Yun elastic local buckling before yield? | Geometry identity |
|---|---:|---:|---:|---:|---|---|
|Z0--Z6|200.00|50.000|794.389|2.2377|**NO**|primary-source closed|
|T120|120.00|30.000|2206.635|6.2159|**NO**|current project contract / provenance partial|
|T360|360.00|90.000|245.182|0.6907|**POSSIBLE**|current project contract / provenance partial|
|BH005|56.25|14.0625|10042.642|28.2891|**NO**|working geometry only|
|BH010|112.50|28.125|2510.660|7.0723|**NO**|working geometry only|
|BH020|225.00|56.250|627.665|1.7681|**NO**|working geometry only|
|BH032|360.00|90.000|245.182|0.6907|**POSSIBLE**|working geometry only|
|BH050|562.50|140.625|100.426|0.2829|**POSSIBLE**|working geometry only|

`POSSIBLE` means only that elastic local buckling can precede yield for some admissible local aspect ratio. It does not yet authorize a production progressive law; the actual local longitudinal length/restraint must still be source-closed.

---

## 4. Major correction to the R15 cross-family interpretation

R15 retained a tentative common signal between Z6 and BH050: both are deep in the gross Marguerre--Airy postbuckling range and both retain positive validation residuals.

R16 now separates the mechanisms.

For Z0--Z6, Zhou's primary-source local chamber width is only `200 mm`, so

\[
B_s/t_s=50<74.795,
\]

and even the **minimum possible** Yun elastic local-buckling stress is

\[
\boxed{794.389\ \mathrm{MPa}>355\ \mathrm{MPa}}.
\]

Therefore:

\[
\boxed{
\text{the pre-yield Yun elastic progressive local-subpanel mechanism is inactive for the Z family.}
}
\]

This means the Z6 `+13.93%` R07 residual cannot be assigned to the same pre-yield elastic local-subpanel mechanism that remains possible for T360/BH032/BH050.

It does **not** prove that Z6 has no local steel instability. It means any Z6 local mechanism relevant after this gate must involve, for example, elastoplastic/yield-interaction local buckling or a different global/sectional resultant mechanism. Those alternatives are not selected here.

```text
Z6_YUN_ELASTIC_PROGRESSIVE_LOCAL_AREA_EXPLANATION = REJECT
Z6_LOCAL_INSTABILITY_IN_GENERAL = NOT_REJECTED
Z6_NEXT_MECHANISM_IDENTITY = OPEN
```

---

## 5. What remains physically admissible for T360 / BH032 / BH050

For the current local widths, the lower-bound screen allows elastic local buckling before yield for:

\[
T360,\quad BH032,\quad BH050.
\]

The Yun large-deflection formulation provides an amplitude-dependent average compressive stress rather than a single static cap. In the notation already used in the project,

\[
\widehat\sigma_Y(A)=
\left[
 k_{crx}\frac{A}{A+A_0}
 +
 k_p(1-\nu_s^2)
 \frac{2A_0A+A^2}{t_s^2}
\right]
\frac{\pi^2E_st_s^2}
{12(1-\nu_s^2)B_s^2}.
\]

This is exactly the type of source-supported object that can distinguish progressive local-postbuckling response from a constant ultimate cap.

A crucial interpretation is retained:

> progressive effectiveness need not mean that the absolute average steel force decreases monotonically. Yun membrane action can increase the average postbuckling stress. The missing physics is that the actual average resultant evolves differently from the gross-width elastic/plastic reference response.

---

## 6. Candidate algebraic elimination into a resultant law — formulated, not yet production

The project formula-mapping register also contains the local mean-strain/amplitude relation

\[
\widehat\varepsilon_{\ell}(A,A_0)
=
\frac{\widehat\sigma_Y(A)}{E_s}
+
C_\varepsilon(2A_0A+A^2),
\]

\[
C_\varepsilon=
\frac{3m^2\pi^2}{2a_\ell^2}.
\]

This provides a possible **algebraic elimination**, not a tracked material state:

\[
\boxed{
\widehat\varepsilon_{\ell}(A)=\varepsilon_f
\quad\Longrightarrow\quad
A=A(\varepsilon_f),
}
\]

then

\[
\boxed{
\bar\sigma_f(\varepsilon_f)
=
\widehat\sigma_Y[A(\varepsilon_f)]
}
\]

up to the source-supported steel strength terminal.

For a monotone unique branch, `A` is therefore only a finite **current algebraic internal coordinate** used while constructing the steel resultant envelope. It need not become a new global Ritz degree of freedom and need not create a history-state machine.

The corresponding resultant concept is

\[
N_{s,f}=\sum_i B_{s,i}t_s\,\bar\sigma_{f,i},
\qquad
M_{s,f}=\sum_i z_{f,i}B_{s,i}t_s\,\bar\sigma_{f,i}.
\]

This is compatible in principle with

```text
MATERIAL_POINTS = 0
SPATIAL_QUADRATURE = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
FINITE_RESULTANT_INTERNAL_COORDINATES = YES
```

but is **not frozen for production in R16** for three reasons:

1. the T/BH local longitudinal lengths and restraint identities are not all source-closed;
2. the BH `B_s=0.225B` geometry remains working-contract rather than primary-source-closed;
3. the current R14 external faces are integrated exactly through their 4-mm thickness. Replacing that with a centroidal thin-face average law, or multiplying every through-thickness compressive fibre by one width-effectiveness factor, would be an additional modeling assumption not yet source-authorized.

Therefore no new `Ny-My` production envelope is generated in this gate.

---

## 7. No-double-counting rule with Marguerre--Airy

The gross Marguerre--Airy mode and the local steel subpanel mode are distinct scales only when the local geometry and restraint pattern are independently identified.

For Z this separation is source-clear:

```text
GROSS MA WIDTH = n_s * 200 mm
LOCAL CHAMBER WIDTH = 200 mm
```

For T/BH, the same proof is not yet complete from primary geometry provenance.

Consequently:

```text
USE_GROSS_MA_q_AS_LOCAL_YUN_A = PROHIBITED
USE_GROSS_MA_b_AS_LOCAL_Bs = PROHIBITED
LOCAL_A = ALGEBRAIC_LOCAL_COORDINATE_ONLY
LOCAL_GLOBAL_DOUBLE_COUNTING_GATE = OPEN_FOR_T_BH
```

---

## 8. Production consequences

No comparator enters any gate above. No `P_u` is refit or rerun.

```text
R07_Z0_Z6_Pu = RETAIN_UNCHANGED
R14_T_BH_Pu = RETAIN_UNCHANGED
NEW_FITTED_FACTOR = NO
PRODUCTION_Pu_CHANGED_IN_R16 = NO
```

The R15 static-cap equivalence result also remains valid. R16 only determines when a genuinely progressive **elastic local-subpanel** law is even physically eligible.

---

## 9. R16 decision

```text
R16_EXECUTION = COMPLETE

MARGUERRE_AIRY = RETAIN
Ny_My_RESULTANT_TERMINAL = RETAIN
TC_CC_TT_ROUTE = OFF_MAINLINE

Z_LOCAL_Bs = 200 mm
Z_LOCAL_Bs_OVER_ts = 50
Z_LOCAL_GEOMETRY_PROVENANCE = PRIMARY_SOURCE_CLOSED
Z_YUN_ELASTIC_PREYIELD_LOCAL_GATE = FAIL / INACTIVE
Z6_COMMON_YUN_ELASTIC_MECHANISM_WITH_BH050 = REJECT

T120_Bs_120 = CURRENT_PROJECT_CONTRACT / PROVENANCE_PARTIAL
T120_YUN_ELASTIC_PREYIELD_LOCAL_GATE = INACTIVE_ROBUSTLY
T360_Bs_360 = CURRENT_PROJECT_CONTRACT / PROVENANCE_PARTIAL
T360_YUN_ELASTIC_PREYIELD_LOCAL_GATE = POSSIBLE

BH_Bs_0P225B = CURRENT_WORKING_GEOMETRY / PRIMARY_PROVENANCE_OPEN
BH005_YUN_ELASTIC_PREYIELD_LOCAL_GATE = INACTIVE_CONDITIONAL
BH010_YUN_ELASTIC_PREYIELD_LOCAL_GATE = INACTIVE_CONDITIONAL
BH020_YUN_ELASTIC_PREYIELD_LOCAL_GATE = INACTIVE_CONDITIONAL
BH032_YUN_ELASTIC_PREYIELD_LOCAL_GATE = POSSIBLE_CONDITIONAL
BH050_YUN_ELASTIC_PREYIELD_LOCAL_GATE = POSSIBLE_CONDITIONAL

YUN_AMPLITUDE_TO_CURRENT_RESULTANT_ALGEBRAIC_ELIMINATION = FORMULATED_CANDIDATE
YUN_PROGRESSIVE_NM_PRODUCTION_LAW = NOT_YET_AUTHORIZED

R07_NC = RETAIN
R14_UHPC = RETAIN
PRODUCTION_Pu_CHANGED = NO
```

## 10. Next gate

The next non-redundant task is now bifurcated by mechanism rather than by comparator residual:

```text
TRACK_A_T_BH = close actual T360/BH032/BH050 local longitudinal lengths,
               restraint identities, and BH B_s provenance;
               then prove monotone/unique A(eps_f) elimination and
               construct the zero-quadrature steel Ny-My contribution.

TRACK_B_Z6  = do not use Yun elastic progressive area;
               diagnose whether source-supported elastoplastic local
               buckling/yield interaction or a different sectional/global
               resultant mechanism is the missing object.
```

Primary next task:

```text
NEXT_TASK = T360_BH032_BH050_LOCAL_GEOMETRY_PROVENANCE_AND_ALGEBRAIC_YUN_TO_NM_CLOSURE
Z6_ELASTIC_LOCAL_PROGRESSIVE_AREA_ROUTE = CLOSED_INACTIVE
USER_ACCEPTANCE = PENDING
```
