# R05 direct iteration progress — zero spatial Gauss

Date: 2026-09-24

This execution uses the 10-scalar state
[q,Aplus,Aminus,epsx_bar,epsy_bar,ex_alpha,ey_beta,Fx,Fy,P]
and directly iterates the 10 residual equations. No x/y/z/ζ Gauss points are used.

The integration backend expands the constitutive integrands in scalar strain/invariant space, lifts the resulting polynomial into the exact Fourier-Laurent algebra of the retained Chen-Ji §8.8 trigonometric field, and evaluates area/thickness moments analytically. These scalar constitutive-expansion coefficients are not structural unknowns.

Successfully converged direct states obtained in the current execution:

BH005:
dbar=0.001000, Delta=0.500 mm, P=0.992219934 MN, q=1.294483901e-5, Aplus=0.001101041 mm, Aminus=0.000828774 mm.
dbar=0.003000, Delta=1.500 mm, P=1.534747678 MN, q=2.389911164e-5, Aplus=0.003464911 mm, Aminus=0.002582569 mm.
dbar=0.004500, Delta=2.250 mm, P=2.190217457 MN, q=3.733449856e-5, Aplus=0.005742624 mm, Aminus=0.004287067 mm.

BH010:
dbar=0.001000, Delta=1.000 mm, P=1.179494379 MN, q=3.396876381e-5, Aplus=0.008977542 mm, Aminus=0.006852533 mm.
dbar=0.004500, Delta=4.500 mm, P=4.023603992 MN, q=1.380468034e-4, Aplus=0.075387043 mm, Aminus=0.059471583 mm.

BH020:
dbar=0.001000, Delta=2.000 mm, P=2.078227527 MN, q=1.197508262e-4, Aplus=0.094456110 mm, Aminus=0.078928940 mm.
dbar=0.004200, Delta=8.400 mm, P=7.292489251 MN, q=5.212872172e-4, Aplus=-0.400861900 mm, Aminus=-0.246983090 mm.

BH032:
dbar=0.003600, Delta=11.520 mm, P=10.081991177 MN, q=1.647098553e-3, Aplus=-0.409391936 mm, Aminus=-0.228716909 mm.

The negative local-amplitude states above are mathematical roots of the current unconstrained Eq.(114)/(119) system. They are recorded, not silently discarded. If unilateral local-direction admissibility is imposed, those roots must be rejected or treated with an active-set/complementarity condition; that would be an explicit extension of the current ten equations.

BH050/BH060 direct solves at the attempted larger dbar states did not finish within the current execution window; no root is recorded for them in this file. Nothing is inferred from the timeout.

No quadrature-order or accuracy judgment is made here.
