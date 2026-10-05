# RETRACTION: BH100 UHPC path reversion error

Date: 2026-10-05
Status: REQUIRED CORRECTION / NUMERICAL RESULTS INVALID

## What went wrong

The BH100 damage-activation trial and every subsequent steel-shell recomputation inherited the wrong UHPC material path.

The locked UHPC route in the current analytic ledger is PEAK-REBASED, not ABS/raw:

1. Damage:
   - d_hat_t = 0 for eta_t <= eps_tp
   - d_hat_c = 0 for eta_c <= eps_cp
   - after peak:
     d_hat_t = (d_t^ABAQUS - d_t,p)/(1-d_t,p)
     d_hat_c = (d_c^ABAQUS - d_c,p)/(1-d_c,p)
   - local damage = max(d_hat_t,d_hat_c)

2. Plastic strain / plastic initial imperfection:
   - Delta p_t = max[p_t(eta_t)-p_t,p, 0]
   - Delta p_c = max[p_c(eta_c)-p_c,p, 0]
   - rotate these rebased principal plastic strains to x-y
   - obtain kappa_x,p and kappa_y,p from the top/bottom surface difference
   - project those curvatures to w_P

3. If both tensile and compressive measures remain below their peak markers, the locked state is strictly:
   rho_A = 1, rho_D = 1, w_P = 0.

## The incorrect reversion

The file BH100_DAMAGE_ACTIVATION_CORRECTION_SPEC.md explicitly says:
"Keep exactly the same ABS/raw UC141 functions..."

That sentence is wrong and violates the previously frozen UHPC ledger.

The subsequent result BH100_DAMAGE_ACTIVATION_CORRECTION_RESULT.md therefore used:
- ABS/raw damage,
- ABS/raw plastic,
- plus a newly introduced plane-stress equivalent-uniaxial strain driver.

This changed the UHPC model identity twice at once.

The later BH100_STEEL_LOCAL_MISES_REPAIR_RESULT.md froze and propagated that same wrong UHPC state, so its:
- rho_A,
- rho_D,
- w_P,
- P_UHPC,
- total P-w path,
- and reported Pu
are INVALID for the intended current theory.

## Why the "Poisson false-cracking correction" was a false diagnosis of the locked model

The alleged false cracking came from feeding positive Poisson strain into the ABS/raw tensile damage table.

But the locked peak-rebased model has:
d_hat_t = 0 until eta_t exceeds eps_tp.

Therefore a pure Poisson lateral expansion below the tensile peak cannot create tensile damage in the locked model.

The earlier audit diagnosed a pathology created by the accidental ABS/raw path, then "fixed" that accidental path by changing the multiaxial driver. It did not identify a defect in the frozen peak-rebased UHPC model.

## Consequences

The following BH100 numerical outputs are retracted:
- 15.61115 MN corrected-damage trial;
- rho_A = 0.8533161, rho_D = 0.7715349, w_P = 31.59680 mm at w ≈ 82.155 mm;
- the continuous-local-Mises steel branch peaking near 24.895 MN at w ≈ 146.32 mm;
- all load partitions on that branch.

The steel single-e whole-face corrector criticism remains a useful independent mechanical audit, but it must be recomputed with the correct UHPC state before any quantitative BH100 result is retained.

## Correct next computation

Return to the previously locked PEAK-REBASED UHPC path exactly as written in the analytic ledger:
- principal trial strains eta_t=max(eps1,0), eta_c=max(-eps2,0);
- peak-rebased damage;
- peak-rebased plastic strain;
- peak-rebased plastic reference imperfection w_P;
- continuous level-set/integral evaluation.

Then, and only then, combine that UHPC state with the continuous local steel Mises-cap operator and recompute BH100.

No BH085-BH005 run may resume before BH100 is re-established on this corrected combined path.
