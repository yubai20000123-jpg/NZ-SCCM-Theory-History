# NZ-SCCM Z6 boundary-warp sparse static-condensation execution checkpoint

**Timestamp:** 2026-08-15 18:44 +08:00  
**Status:** FIRST FULL Rq=0 + Rc=0 CURRENT-OPERATOR CHECKPOINT FOUND AT D=0.5; NOT Pu

## 1. Frozen theory

Unchanged:
- ONE_CONTINUOUS_COMPLETE_HALFWAVE
- Nguyen second-order kinematics
- R10 / N48-C1-MM / Cayley-Hamilton
- D15 exact structural moments
- A0=a/500
- formal structural spatial sampling = 0
- formal structural quadrature = 0
- outer-shell current local radial-cap diagnostic
- no Zhou/Winter load used to select q or c.

Only new generalized in-plane amplitude:
`c`, using the N=1 boundary-admissible warp field from the 18:13 preflight.

## 2. Exact current residuals

At fixed D, solve:
`Rq(D,q,c)=0`
`Rc(D,q,c)=0`

where
`Rc = ∫ sigma : epsilon_,c dV`.

All spatial contractions are analytic coefficient moments. The material compiler remains N48; shell radial-cap coefficient degree is checked through 8,12,20,24 and degree24 is used for the released checkpoint.

Compiler interval used for this checkpoint:
`lambda in [-1.75, 0.45]`.

## 3. D=0.5 old free-Poisson equilibrium

With old field and degree24 shell cap:
- D = 0.500000000
- q = 0.003706299953
- P = 35.928871761 MN
- Rq = +0.001276 MN mm
- Pc = 18.078808678 MN
- Ps = 17.850063082 MN

This is a one-residual Rq equilibrium checkpoint for the old field.

## 4. D=0.5 boundary-admissible coupled equilibrium

N=1 admissible warp, degree24:
- D = 0.500000000
- q = 0.007244278905
- c = -0.0154563484942
- P = 37.345137133 MN
- Rq = +0.000722 MN mm
- Rc = +0.000173 MN mm
- Pc = 21.070046455 MN
- Ps = 16.275090678 MN

Residual decomposition:
- Rq,c = -2648.321974 MN mm
- Rq,s = +2648.322697 MN mm
- Rc,c = -28.69208393 MN mm
- Rc,s = +28.69225680 MN mm

Thus both generalized virtual-work balances close by independent concrete/steel cancellation, rather than by residual suppression.

At the same D, the boundary-admissible equilibrium load is:
`+3.9419%`
relative to the old free-Poisson equilibrium.

## 5. Shell cap degree check at near-root state

At D=0.5, q≈0.00724, c≈-0.01545:
- degree 8: P≈37.36088 MN
- degree 12: P≈37.36055 MN
- degree 20: P≈37.36216 MN
- degree 24: P≈37.36174 MN before final q,c correction

Therefore the shell radial-cap degree is not the controlling uncertainty at this checkpoint. Production identity remains degree24; lower degrees are diagnostics only.

## 6. Meaning of c<0

The elastic q=0 condensation gave c>0. At finite q≈0.00724, nonlinear geometric membrane strain from w_,x^2 and w_,y^2 is already substantial. The condensed c changes sign to oppose part of that nonlinear transverse membrane strain while satisfying loaded-edge ux=0. This sign change is not itself an illegality; only Rq/Rc equilibrium and admissibility decide the state.

## 7. What this does and does not establish

Established:
- Full current-map boundary warp is not merely theoretical; a coupled Rq/Rc equilibrium can be found with zero structural quadrature.
- At D=0.5, fixing the loaded-edge in-plane admissibility raises P only about 3.94%, despite a large q shift.

Not established:
- Z6 corrected Pu.
- Peak location in D.
- The boundary mismatch explains the original ~24.5% gap.
- Z4 response under the same coupled warp.

## 8. Next execution

Continue the connected coupled branch in D from the certified D=0.5 checkpoint using predictor/corrector in (q,c), with fixed N=1 and degree24. Record every accepted D,q,c,P,Rq,Rc and stop at first connected P peak or representation/domain gate. Then run Z4 under the same formulation as control.
