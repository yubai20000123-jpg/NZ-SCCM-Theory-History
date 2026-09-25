# 05 Strict reductions and cross-material UHPC stability test

Date: 2026-09-25

## A. Strict Yun-Lu reduction of the elastic whole-face steel path

Map the present coordinates to Yun-Lu's single-side plate as:
- present transverse width b -> Yun-Lu b;
- present axial length a_h -> Yun-Lu a;
- set q=q0=0;
- set transverse wave count N=1;
- retain axial local half-wave count m;
- define r=a_h/b.

The explicit elastic reduced path becomes exactly

p_s^E =
[ k_crx A/(A+A0)
 + k_p (1-nu_s^2)(2A0 A+A^2)/t_s^2 ] pi^2 D_s/b^2,

D_s=E_s t_s^3/[12(1-nu_s^2)],

with

k_crx =
4(3m^4+2m^2 r^2+3r^4)/(3r^4),

and

k_p =
[272m^16+2856m^14r^2+11273m^12r^4+23146m^10r^6
 +31506m^8r^8+23146m^6r^10+11273m^4r^12
 +2856m^2r^14+272r^16]
/
[r^4(m^2+r^2)^2(m^2+4r^2)^2(4m^2+r^2)^2].

At the integer-aspect minimum r=m:
k_crx=32/3=10.6666666667,
k_p=1066/25=42.64.

These are exactly Yun-Lu Eq.(2-32)–(2-34) and the stated integer-aspect coefficients.

The exact edge compressive stress on y=0 reduces to

sigma_edge,c =
p_s^E/t_s
+ (E_s pi^2/(2b^2))(2A0A+A^2) h(r,m),

where

h(r,m)=
[224m^12+1592m^10r^2+3999m^8r^4+3230m^6r^6
 +1703m^4r^8+504m^2r^10+48r^12]
/
[(m^2+r^2)^2(m^2+4r^2)^2(4m^2+r^2)^2].

At r=m:
h=113/25=4.52.

First yield is sigma_edge,c=f_y. Substituting p_s^E and clearing the factor A+A0 gives a cubic polynomial in A, exactly the same algebraic identity as Yun-Lu Eq.(2-38). Yun-Lu stops at the first positive connected root A_u and evaluates p_xu from Eq.(2-39).

The reduced post-yield continuation
p_s^Y=t_s[f_y-(E_s pi^2/(2b^2))(2A0A+A^2)h(r,m)]
is therefore NOT Yun-Lu's original formula. It is a new ideal-plastic continuation that intersects the exact Yun-Lu elastic path at Yun-Lu's first-yield point.

## B. Strict Chen-Ji single-sine reduction

For a pure global sine plate, set A=A0=0 and project with the global sine g, not with the local whole-face phi. This distinction is mandatory.

Using Chen-Ji's notation:
rho = m_C b/a_h,
f = physical sine amplitude,

p_cr = (pi^2 D_s/b^2)(rho+1/rho)^2,

p_g^E(f)=
p_cr
+(pi^2 E_s t_s/(16b^2)) f^2 (rho^2+rho^-2).

This is Chen-Ji Eq.(8.65)–(8.67).

The edge redistribution from the same Airy particular is

Delta sigma_edge =
[2(p_g^E-p_cr)/t_s]/(rho^-4+1).

The reduced ideal-plastic consistency continuation is

p_g^Y(f)=t_s[f_y-Delta sigma_edge(f)].

At the first intersection p_g^E=p_g^Y,

f_y =
sigma_u
+2(sigma_u-sigma_cr)/(rho^-4+1),

which is exactly Chen-Ji Eq.(8.71).

For the minimum-wave choice rho=1:

sigma_u=(f_y+sigma_cr)/2,

exactly Chen-Ji Eq.(8.72).

Thus the reduced elastic->yield construction strictly recovers Chen-Ji's single-wave elastic path and edge-yield endpoint. The descending p_g^Y branch after that point remains a new reduced ideal-plastic continuation, not an equation from Chen-Ji.

## C. UHPC minimum-order cross-material test

Formal family tested:

x=epsilon/epsilon_c0,
n=E_c epsilon_c0/f_c,

sigma/f_c =
n x (1+a x^2) /
[1+(b1 x+b2 x^2+b3 x^3)^2].

This is the minimum 4-shape-parameter core of the previously proposed globally pole-free family. It has:
- ordinary epsilon only;
- no abs, sign branch, Heaviside, max/min;
- sigma(0)=0;
- sigma'(0)=E_c;
- denominator strictly positive;
- if a>=0, sign(sigma)=sign(epsilon);
- stress -> 0 as |epsilon|->infinity when b3 !=0.

Four parameters are fitted only to:
sigma(-epsilon_c0)=-f_c,
sigma'(-epsilon_c0)=0,
sigma(epsilon_t0)=f_t,
sigma'(epsilon_t0)=0.

### Test sets

1. UC141 project baseline:
fc=141.1 MPa, Ec=43.4 GPa, epsc0=0.0035, ft=7.3 MPa, epst0=0.0009722.

2. Hiew SL-1.0:
fc=124.3 MPa, Ec=40.7 GPa (28-day compression table);
ft_peak=9.2 MPa, epst_peak=0.00445 (Table 7).
Hiew does not report compressive peak strain in the retrieved table, so for mathematical stability only epsc0*=fc/Ec=0.003054 is used. This is not claimed to be measured epsc0.

3. Hiew SL-1.5:
fc=129.3 MPa, Ec=40.9 GPa;
ft_peak=11.3 MPa, epst_peak=0.00676;
epsc0*=fc/Ec=0.003161 for stability only.

4. Hiew SL-2.0:
fc=137.9 MPa, Ec=41.3 GPa;
ft_peak=11.7 MPa, epst_peak=0.00380;
epsc0*=fc/Ec=0.003339 for stability only.

5. Hiew HL-2.0:
fc=143.1 MPa, Ec=41.6 GPa;
ft_peak=11.1 MPa, epst_peak=0.00674;
epsc0*=fc/Ec=0.003440 for stability only.

6. FHWA idealized design material:
use the actual idealized compressive peak 18.7 ksi=128.93 MPa at epsc0=0.00270;
Ec=6933 ksi=47.80 GPa;
tensile plateau stress 1 ksi=6.895 MPa and first attainment strain 0.000144.
This is intentionally a plateau-type stress test, not a strain-hardening direct-tension material.

### Numerical results

| Set | n | r=ft/fc | tau=epst0/epsc0 | fit residual norm | result |
|---|---:|---:|---:|---:|---|
| UC141 | 1.077 | 0.0517 | 0.278 | 1.4e-16 | PASS; exactly two physical extrema (-1,tau) |
| Hiew SL-1.0 | 1.000 | 0.0740 | 1.457 | 4.7e-2 | FAIL; four peak constraints cannot be matched with a>=0 |
| Hiew SL-1.5 | 1.000 | 0.0874 | 2.138 | 5.3e-2 | FAIL |
| Hiew SL-2.0 | 1.000 | 0.0848 | 1.138 | 5.3e-2 | FAIL |
| Hiew HL-2.0 | 1.000 | 0.0776 | 1.959 | 4.8e-2 | FAIL |
| FHWA idealized | 1.001 | 0.0535 | 0.053 | 2.1e-3 | FAIL; extra stationary points appear |

UC141 coefficients:
a=43.0184, b1=12.6797, b2=15.2053, b3=9.3365.
It has only the intended compression and tension stationary points and gives
sigma(-2epsc0)/fc=-0.242,
sigma(2epst0)/fc=+0.0477.

Conclusion:
The 4-parameter minimum core is stable for UC141-like moderate tensile peak strain ratio tau~0.2-0.35, but it is not a cross-UHPC universal law. Direct-tension strain-hardening UHPC in Hiew has tau about 1.1-2.1 and requires additional tensile-shape information; plateau-type design laws with tau~0.05 are also outside this core.

This is consistent with Hiew's experimental classification, which uses additional tensile parameters (cracking, localization and tensile limit) beyond ft and eps_t,peak.

Therefore the current minimum-order result is negative:
{Ec,fc,epsc0,ft,epst0} alone are insufficient to define a robust universal full-range UHPC curve with the tested 4-shape-parameter architecture.

The next admissible UHPC family should retain a single ordinary-epsilon formula but include at least one independent tensile ductility/localization descriptor. No tension/compression branch switch is to be reintroduced.
