PRE-COMPUTATION BACKUP
Project: UCFT / nonlinear membrane condensation / M8
Timestamp: 2026-09-30 20:55 +08:00
Source: latest recovered Library state before continuing M8 implementation.

Recovered verdict:
- M0–M7: PASS
- M8_INPUT_FREEZE: PASS
- M8_PATH_SOLVER: PARTIAL
- Remaining implementation gap: finite-trigonometric UHPC active interval analytic/rational Y integration after M3 C/S/B enrichment.
- Required NEXT_ACTION: implement t=tan(Y/2) rational primitive, prove baseline C1 degeneration to M4 analytic-Y, retain analytic thickness + analytic/rational Y + one deterministic X integral; then start BH005 perfect-local (N,m) identification -> restore A0 -> imperfect connected q-path.

Locked production inputs:
- Ec=43400 MPa; UHPC tensile peak ft=7.2 MPa production surrogate as frozen in Library.
- Steel Es=206000 MPa, fy=355 MPa, nu_s=0.30; ideal elastic-perfectly-plastic equivalent law.
- b = 250,500,1000,1600,2500,3000,3500,4250,5000 mm; a_h=2b; tc=42 mm; ts=4 mm; q0=0.0025; Aw=1332 mm^2.
- A0^±=0.225b/1600; local mode pair selected mechanically from perfect-local condensed tangent, initial integer search 1..12 and expand if boundary winner.

No FEM/test Pu is used for parameter fitting in M8.
