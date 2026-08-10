# NZ-SCCM R04 NAMED KERNEL AND MATRIX-FUNCTION EVIDENCE — 2026-08-10

## 1. Purpose

Support the R04 classification of which mature special-function families are genuinely relevant to the existing G18/G20/G27 + D15 mainline.

This note does not authorize a route switch and does not grant a named special function production status unless the actual reduced NZ-SCCM kernel matches its algebraic class.

## 2. Appell F1

NIST DLMF §16.15 gives the Euler integral representation of the Appell F1 two-variable hypergeometric function. This supports the previously verified master kernel for denominators reducible to a bilinear `sin^2` form such as

```text
1/(a+b sin^2 X+c sin^2 Y+d sin^2 X sin^2 Y).
```

R03 already numerically cross-checked one representative Appell F1 master value to approximately machine precision with an independent audit-only quadrature.

R04 restriction: the exact `Pi_eta + H1 + H10` source-shaped tensile tower does not generically reduce to this Appell class.

## 3. Carlson symmetric elliptic integrals

NIST DLMF Chapter 19, especially §19.36, describes stable computation of Carlson symmetric elliptic integrals and the duplication method. Repeated duplication reduces variable differences by factors of four before evaluation of a fixed polynomial expansion.

This makes `RF`, `RD`, `RJ` attractive as stable numerical backends for **named exact genus-1 kernels**.

R04 restriction: they do not provide a generic wrapper for nested radical towers of algebraic degree far above one cubic/quartic square-root extension.

## 4. 2x2 matrix functions

Higham and Al-Mohy, *Computing Matrix Functions*, Acta Numerica 19 (2010), provides the general matrix-function framework and numerical theory relevant to stable evaluation and Frechet derivatives.

For the present 2x2 symmetric tensor, the project uses the coalescence-safe form

```text
X = mu I + Y,   Y^2 = r_s^2 I
f(X)=f_e I+f_o Y
f_e=[f(mu+r_s)+f(mu-r_s)]/2
f_o=[f(mu+r_s)-f(mu-r_s)]/(2 r_s) -> f'(mu)
```

This is a spectral reconstruction device. It prevents artificial singularity when principal values coalesce, but it does not by itself perform the whole-halfwave structural integration.

## 5. R04 evidence conclusion

```text
Appell F1 = DIRECT KERNEL ONLY WHEN ACTUAL DENOMINATOR MATCHES
Carlson RF/RD/RJ = DIRECT KERNEL ONLY FOR ELLIPTIC/GENUS-1 REDUCTIONS
2x2 matrix functions = STABLE SPECTRAL RECONSTRUCTION SUPPORT
FULL SOURCE PI+H1+H10 TOWER = NO GENERIC SMALL NAMED-KERNEL CLOSURE FOUND
```

Therefore R04 returns the main difficulty to one-dimensional material scalar design on the material-native domain instead of expanding the spatial integration machinery.
