# NZ-SCCM — Swartz24 UMCG Batch Audit Localizer

**Time:** 2026-08-21 23:55 +08:00  
**Status:** `EXECUTED / AUDIT_ONLY_UMCG_LOCALIZER / NOT YET FORMAL PRODUCTION`

## 0. Purpose and strict identity

This batch applies the same phase-compatible UMCG architecture used for the resolved Z6 calculation to all 24 Swartz RC panels, without modifying the Marguerre–Airy structural backbone and without using experimental failure loads in root solution.

Mandatory source correction is active:

\[
\rho_x=\rho_y=p_{table},
\]

with the table ratio distributed only among reinforcement layers.

The ordinary-concrete phase uses the frozen NC-M6 current material identity with the project baseline

\[
f_t=0.10f_c.
\]

This `0.10fc` identity is not a specimen-specific Swartz measured tensile strength. Consequently the present batch is a common-material UMCG diagnostic, not a claim of specimen-specific source-closed tensile calibration.

For decimal localization of the section fold, continuous through-thickness evaluation was performed numerically as an audit oracle. This does not change the formal project rule

```text
FORMAL_SPATIAL_QUADRATURE = 0
```

but the 24 numerical values below are not promoted to formal production until the finite branchwise thickness primitives / endpoint reductions are instantiated for the RC UMCG section.

## 1. Common RC UMCG section

For each structural candidate \((q,s)\), compatible section strains are recovered as

\[
\varepsilon_x(z)=\varepsilon_0X,
\]

\[
\varepsilon_y(z)=\varepsilon_0\left(Y+K\frac{z}{h}\right),
\qquad h=t/2,
\]

\[
\gamma_{xy}=0.
\]

The phase resultants satisfy

\[
N_x^{sec}=N_x^d(q),
\]

\[
N_y^{sec}=-n_y(s;q),
\]

\[
M_y^{sec}=m_y(s;q).
\]

Concrete gross section response is reduced by the actual x+y reinforcement area at each reinforcement layer. x-direction reinforcement contributes to \(N_x\); y-direction reinforcement contributes to \(N_y,M_y\). Reinforcement follows the source axial elastic-perfectly-plastic law.

The capacity localizer solves section equilibrium together with local loss of rank of the compatible section resultant map. No failure load is present in this solve.

## 2. Control-location result

Representative finite s checks show the resolved UMCG capacity increases away from the transverse anti-node toward smaller s for the RC panels. The controlling location remains

\[
\boxed{s_u=1}
\]

for the 24-panel batch.

This differs from Z6, where UMCG moved control to \(s=0\). The contrast is physical: Z6 is governed by large transverse membrane demand competing with multiaxial steel capacity, whereas the Swartz RC panels remain dominated by the bending/compression anti-node.

## 3. Batch results

`Pu_pre` is the corrected-reinforcement uniaxial N-M candidate from the current explicit theory. `Pu_UMCG` is the present common NC-M6 section-fold audit localizer.

|Case|Pu_pre kN|Pu_UMCG kN|gate change|Pf kN|UMCG error|
|---:|---:|---:|---:|---:|---:|
|1|567.712|604.450|+6.47%|490.194|+23.31%|
|2|561.638|597.732|+6.43%|506.652|+17.98%|
|3|502.555|540.349|+7.52%|444.377|+21.60%|
|4|539.885|577.512|+6.97%|534.231|+8.10%|
|5|535.241|581.423|+8.63%|623.641|-6.77%|
|6|596.560|642.258|+7.66%|691.698|-7.15%|
|7|598.218|656.351|+9.72%|640.099|+2.54%|
|8|513.907|567.382|+10.41%|455.053|+24.68%|
|9|515.424|546.510|+6.03%|625.865|-12.68%|
|10|534.711|564.953|+5.66%|696.147|-18.85%|
|11|532.402|566.266|+6.36%|636.541|-11.04%|
|12|562.325|597.293|+6.22%|639.654|-6.62%|
|13|584.604|635.127|+8.64%|511.990|+24.05%|
|14|657.813|708.947|+7.77%|716.164|-1.01%|
|15|696.149|761.971|+9.46%|766.429|-0.58%|
|16|615.623|677.548|+10.06%|721.946|-6.15%|
|17|316.788|325.963|+2.90%|429.253|-24.06%|
|18|339.837|355.419|+4.59%|396.337|-10.32%|
|19|339.177|353.147|+4.12%|377.654|-6.49%|
|20|335.013|340.518|+1.64%|372.761|-8.65%|
|21|350.460|352.276|+0.52%|368.313|-4.35%|
|22|351.679|359.212|+2.14%|355.858|+0.94%|
|23|356.875|382.330|+7.13%|346.961|+10.19%|
|24|414.499|438.574|+5.81%|400.340|+9.55%|

## 4. Statistics

All 24:

\[
\boxed{\text{mean signed error}=+0.759\%}
\]

\[
\boxed{\text{MAE}=11.153\%,\qquad RMSE=13.583\%}
\]

By the three historical thickness groups:

- Cases 1–8: mean signed `+10.536%`, MAE `14.016%`, RMSE `16.245%`;
- Cases 9–16: mean signed `-4.110%`, MAE `10.122%`, RMSE `12.744%`;
- Cases 17–24: mean signed `-4.149%`, MAE `9.321%`, RMSE `11.278%`.

Compared with the corrected-reinforcement PRE-GATE batch (mean signed about `-5.34%`, MAE about `11.54%`), the common UMCG/NC-M6 section response removes much of the overall negative bias but does not materially collapse pointwise scatter. MAE improves only modestly.

## 5. Trusted-pair view

The trusted/repeat-pair logic remains more informative than fitting all 24 points.

### Case1/2

Experimental pair difference:

\[
+3.36\%.
\]

UMCG theory pair difference:

\[
-1.11\%.
\]

Both still predict nearly the same capacity within the pair, but the pair mean error becomes

\[
\boxed{+20.64\%}.
\]

Therefore the present common NC-M6 section-fold gate does **not** reproduce the earlier separate hard-TC diagnostic reduction for Case1/2. That earlier result must not be conflated with the present unified current-material gate.

### Case9/10

Experimental pair difference:

\[
+11.23\%.
\]

UMCG theory pair difference:

\[
+3.37\%.
\]

Direction remains correct. Pair mean error improves from the PRE-GATE level near `-20.6%` to

\[
\boxed{-15.76\%}.
\]

### Case19/20

Experimental pair difference:

\[
-1.30\%.
\]

UMCG theory pair difference:

\[
-3.58\%.
\]

Pair mean error becomes

\[
\boxed{-7.57\%},
\]

an improvement over the PRE-GATE level near `-10.2%`.

### Case21/22

Experimental pair difference:

\[
-3.38\%.
\]

UMCG theory pair difference:

\[
+1.97\%.
\]

Pair mean error remains small:

\[
\boxed{-1.71\%}.
\]

## 6. Main interpretation

The batch does not support a new Swartz-specific correction factor.

The common UMCG/NC-M6 section response produces three useful observations:

1. it raises all 24 PRE-GATE RC capacities by roughly `0.5–10.4%`;
2. this reduces the systematic low bias of Cases9/10 and Cases19/20 and preserves the good Case21/22 scale;
3. it worsens the already-high Case1/2 design point, showing that the unresolved Case1/2 mechanism is not solved merely by replacing the uniaxial N-M gate with the present NC-M6 section fold.

This is consistent with the current project principle: residual material/specimen mismatch is acceptable if identified explicitly; it is not legitimate to introduce a Case1/2-specific weakening factor.

The contrast between the earlier separate TC-envelope diagnostic and the present UMCG result is itself diagnostic. The former imposed a source-envelope boundary with an assumed `ft`; the latter uses the unified current material response and compatible section capacity. Because Swartz did not report specimen-specific tensile strength, the project currently lacks evidence to force the unified NC material identity to reproduce the earlier `~496/501 kN` Case1/2 numbers.

## 7. Decision

```text
SWARTZ24_UMCG_AUDIT_BATCH = 24/24 RESOLVED
SWARTZ24_CONTROL_s = 1 FOR CURRENT BATCH
SWARTZ24_MEAN_SIGNED_ERROR = +0.759 percent
SWARTZ24_MAE = 11.153 percent
SWARTZ24_RMSE = 13.583 percent
TRUSTED_PAIR_1_2 = STILL SYSTEMATICALLY HIGH
TRUSTED_PAIR_9_10 = LOW BIAS REDUCED BUT REMAINS
TRUSTED_PAIR_19_20 = LOW BIAS REDUCED
TRUSTED_PAIR_21_22 = CLOSE
SWARTZ_SPECIFIC_CORRECTION = NOT AUTHORIZED
FORMAL_RC_UMCG_THICKNESS_PRIMITIVE = NOT YET INSTANTIATED
SPECIMEN_SPECIFIC_FT = SOURCE OPEN
```

This batch is retained as a unified-mechanics diagnostic, not as a new calibrated Swartz production curve.