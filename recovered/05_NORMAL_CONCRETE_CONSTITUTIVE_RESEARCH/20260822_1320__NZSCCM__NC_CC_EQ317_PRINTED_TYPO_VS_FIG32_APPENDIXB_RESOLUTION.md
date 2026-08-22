# NZ-SCCM — Nguyen NC-CC Eq.3.17 printed-text discrepancy resolution

**Date:** 2026-08-22 13:20 +09:00  
**Status:** `SOURCE_DISCREPANCY_RESOLVED / PRODUCTION_FORM_UNCHANGED`

## 0. Discrepancy

A high-resolution visual check of Nguyen Chapter 3 shows that the typeset text of Eq. (3.17) prints the denominator as

\[
1+\alpha^2.
\]

However, two independent objects in the **same thesis** use

\[
(1+\alpha)^2.
\]

They are:

1. Figure 3.2, the plotted Foster-Gilbert biaxial strength envelope, which annotates

\[
-\sigma_{2p}
=\left[\frac{1+3.65\alpha}{(1+\alpha)^2}\right]f_c;
\]

2. Appendix-B executable `stmoduc`, biaxial-compression route:

```fortran
sig2p=((1.0d0+3.65d0*alpha)/(1.0d0+alpha)**2.0d0)*fc
sig1p=alpha*sig2p
```

Thus the printed Eq. (3.17) denominator `1+alpha^2` is inconsistent with both the plotted source envelope and Nguyen's executable implementation.

## 1. Physical cross-check without structural calibration

At equal biaxial compression `alpha=1`:

- printed-text literal `1+alpha^2` would give

\[
\frac{1+3.65}{1+1}=2.325,
\]

which is incompatible with Nguyen Figure 3.2 / Kupfer-type biaxial enhancement;

- Figure 3.2 / Appendix-B `(1+alpha)^2` gives

\[
\frac{4.65}{4}=1.1625,
\]

which matches the plotted envelope scale.

No panel Pu, experiment load, Zhou/Winter or FEM comparator is used for this resolution.

## 2. Source-precedence decision

For NC CC capacity the project therefore uses the **Figure 3.2 + Appendix-B executable** form:

\[
\boxed{
K_{CC}^{NC}(a)=\frac{1+3.65a}{(1+a)^2}
}
\]

with

\[
0\le a=p_m/p_M\le1.
\]

The printed Eq. (3.17) `1+alpha^2` is recorded as a thesis typesetting inconsistency and is not used in production.

```text
NGUYEN_EQ317_PRINTED_DENOMINATOR = 1+alpha^2 / SOURCE_TYPO_INCONSISTENT
NGUYEN_FIG32_DENOMINATOR = (1+alpha)^2 / ACCEPTED
NGUYEN_APPENDIXB_DENOMINATOR = (1+alpha)^2 / ACCEPTED
NC_CC_PRODUCTION_FORM = (1+3.65a)/(1+a)^2
G6 = PASS
G7 = PASS
STRUCTURAL_PU_RERUN = NOT_PERFORMED
```

This addendum does not change the numerical/formula content of the 13:15 material certificate; it strengthens its source provenance.
