# C1 numerical material gate — Eq.(47)–(67)

Strict execution source: uploaded Eq.(1)–(149) contract.

Recovered locked compression-side signed-C1 values:

- Ec = 43400 MPa
- nu_c = 0.20
- fc = 141.1 MPa
- eps_cp = 0.0035
- f_c,1/2 = 75.95 MPa
- f_c,2 = 70.55 MPa

Therefore

- a_c = 3.9286287306087058
- b_c = 7.510340381132359
- c_c = -11.938969111741057
- d_c = 8.433798921174882

The compression denominator has no real pole for radial compression coordinate r>=0.

## Hard unresolved input

The formal signed-C1 tensile source still contains the literal symbolic assignment:

`ft2 := 'ft2'`

No later locked numerical assignment was recovered.

Older pre-C1 PCHIP tension data exist, but this execution does **not** silently substitute them because that would violate Eq.(47)–(67) model identity.

The recovered BH032 prototype explicitly reports an effective normal-strain range crossing into tension (positive values occur), so the tensile C1 branch cannot be bypassed under a “compression dominated” argument.

Hence a certified numeric root of Eq.(1)–(149) does not exist until the signed-C1 tensile anchor set, at minimum f_t,2, is numerically fixed.
