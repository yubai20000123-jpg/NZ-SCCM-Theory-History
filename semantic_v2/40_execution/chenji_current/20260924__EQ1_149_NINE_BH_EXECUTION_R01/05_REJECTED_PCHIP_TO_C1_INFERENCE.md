# Why the old PCHIP tensile curve cannot be silently converted into the missing signed-C1 anchor

This is a diagnostic only; it is **not** used in the strict root solve.

From the older pre-C1 PCHIP tension curve one can read candidate values

- f_t = 10.734818 MPa at eps_tp = 0.0038
- f_t,1/2 = 10.51566981000485 MPa at eps = 0.0019
- old curve reaches zero at approximately 0.00759, so a tempting but **unlocked** guess would be f_t,2 = 0 at 2 eps_tp = 0.0076

Substituting that guess into the signed-C1 rational coefficient equations gives

- a_t = -7.681546161285641
- b_t = 12.323600003789068
- c_t = -4.602561523721217
- d_t = -1.0394923187822118

The tensile denominator then has real roots in r/eps_tp at approximately

- -6.28859739
- **+1.93975973**
- -0.07886367

Therefore the guessed f_t,2=0 creates a positive real pole before 2 eps_tp. It cannot be treated as a harmless recovery of the locked signed-C1 tensile branch.

Conclusion: R01 does not use the old PCHIP-to-C1 inferred anchor set.
