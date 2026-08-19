# NZ-SCCM — Engineering operator R02 low-degree tension amendment

**Date:** 2026-08-19 23:46 +08  
**Status:** supersedes only the provisional `T~` formula in checkpoints `5dc2d5...` / `d340ae...`; all history retained.

Before D15 compilation, the degree-6 provisional tensile utilization is reduced to a degree-4 source polynomial to prevent unnecessary TT degree growth while preserving the conservative scalar envelope.

Final R02 tensile utilization:

\[
\boxed{
\widetilde T(\lambda)=5\rho\,\lambda^2(\lambda+1)^2.
}
\]

For `rho=0.1`, the coefficient is `5rho=0.5`.

Properties on the certified engineering domain `-1<=lambda<=lambda_t=10xcr`:

- `T~>=0`;
- `T~(-1)=T~(0)=0`;
- on `0<=lambda<=lambda_t`, `T~` remains below the frozen R13 tensile utilization for the current R10 constants;
- maximum compression-side leakage on `[-1,0]` is `0.03125` at `lambda=-1/2` and is retained explicitly in the multiaxial audit rather than hidden by a state classifier.

The final uniaxial master is therefore

\[
\boxed{
\widetilde U(\lambda)=
\frac25\kappa\lambda
\left[
\frac{(\lambda+1)(\lambda_t-\lambda)}{\lambda_t}
\right]^3
-\widetilde C(\lambda)
+\rho\widetilde T(\lambda).
}
\]

The compression chain remains

\[
\boxed{
\widetilde C(\lambda)=
(2\lambda+\lambda^2)^2
\left[
1-\left(\frac{\lambda+1}{\lambda_t+1}\right)^2
\right]^4.
}
\]

Case21 scalar audit after this amendment:

```text
compression stress envelope: conservative on [-1,0]
tension stress envelope:     conservative on [0,lambda_t]
compression work ratio:      ~0.9147
tension work ratio:          ~0.6100
initial tangent ratio:       0.4
```

Polynomial degrees now are

```text
deg C~ = 12
deg T~ = 4
deg U~ = 12
```

and the highest scalar interaction degree from `T1*T2^8` is `36`, matching the `C^3` degree ceiling instead of creating an unnecessary degree-54 branch.

**Unique resume point:** compile R02 (`C~12,T~4,U~12`) through CH and exact D15.