# 20260924 Chen–Ji current Eq.(1)–(149) — nine BH execution R01

Status: **strict equation compilation complete; certified numerical stationary-root solve blocked by one unresolved signed-C1 tensile anchor (`f_t,2`)**.

This package does not replace the requested Eq.(1)–(149) by an earlier 6DOF/10DOF/41DOF theory.

Common recovered inputs:
- tc = 42 mm
- ts+ = ts- = 4 mm
- Aw = 1332 mm^2
- Es = 206000 MPa, nu_s=0.30, fy=355 MPa
- Ec = 43400 MPa, nu_c=0.20, fc=141.1 MPa, eps_cp=0.0035
- C1 compression anchors f_c,1/2=75.95 MPa, f_c,2=70.55 MPa
- q0 = 1/400 = 0.0025
- N+=N-=m+=m-=4
- A0+=A0-=0.225 b / 1600
- a_h=b, L=2b

Recovered compression C1:
a_c=3.92862873060871, b_c=7.51034038113236, c_c=-11.9389691117411, d_c=8.43379892117488.

Files:
- 01_PARAMETER_LEDGER.csv
- 02_C1_NUMERIC_GATE.md
- 03_ROOT_SUMMARY.csv
- 04_POST149_SPECTRAL_SOLVER_CONTRACT.md
- cases/*_EQ1_149_SUBSTITUTION.md

Important: the root table intentionally contains no fabricated Pu. The formal signed-C1 source still leaves `ft2 := 'ft2'`, and the BH032 field is known to enter the tensile effective-strain region.
