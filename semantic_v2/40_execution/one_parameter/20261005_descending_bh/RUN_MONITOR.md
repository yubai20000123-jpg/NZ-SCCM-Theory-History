# Run monitor

BH085-BH050 old results remain quarantined. BH032 and smaller remain paused.

## CRITICAL RETRACTION: BH100 UHPC path

The latest BH100 damage-activation and subsequent steel local-Mises runs are INVALID because the UHPC module was accidentally reverted from the locked PEAK-REBASED path to ABS/raw damage and ABS/raw plastic.

Locked UHPC identity to restore:
- eta_t = positive_part(eps1)
- eta_c = positive_part(-eps2)
- d_hat_t = 0 for eta_t <= eps_tp
- d_hat_c = 0 for eta_c <= eps_cp
- post-peak damage is rebased from the peak value
- Delta p_t = max[p_t(eta_t)-p_t,p,0]
- Delta p_c = max[p_c(eta_c)-p_c,p,0]
- plastic initial imperfection w_P is projected only from these peak-rebased plastic strains
- if neither peak is crossed: rho_A=1, rho_D=1, w_P=0

The previously introduced "plane-stress equivalent-uniaxial strain" driver is NOT part of this locked path.

## Retracted numerical outputs
Do not use:
- BH100 Pu = 15.61115 MN damage-activation trial
- BH100 rho_A=0.8533161, rho_D=0.7715349, w_P=31.59680 mm at w≈82.155 mm
- BH100 continuous-local-Mises branch Pu≈24.895 MN at w≈146.32 mm
- all load partitions derived from those wrong-UHPC runs

## Steel audit status
The qualitative diagnosis that the single-e whole-face Mises corrector can artificially collapse one face remains a useful independent steel audit. However, every quantitative steel force and total-load result must be recomputed after the correct peak-rebased UHPC state is restored.

## Decision
Do not resume BH085-BH005.

Next executable target:
BH100 only, with:
1. the locked PEAK-REBASED UHPC damage/plastic/w_P path restored exactly;
2. the continuous local steel Mises-cap operator retained as a candidate steel correction;
3. no FEM/test data in the solve;
4. continuous level-set / deterministic integral backend.

Detailed retraction:
RETRACTION_BH100_UHPC_PATH_REVERSION.md
