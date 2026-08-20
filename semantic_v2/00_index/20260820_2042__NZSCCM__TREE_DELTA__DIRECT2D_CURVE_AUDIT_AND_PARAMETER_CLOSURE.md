# TREE DELTA — direct2D curve audit and parameter closure

Time: 2026-08-20 20:42 +08:00

Current conclusions:

1. The generalized compression primitive `C_m(c)=m_c c/[1+(m_c-2)c+c^2]`, `m_c=E0 eps_c0/fc`, is algebraically identical to the Saenz compression relation used by Nguyen after normalization. Compression primitive source fidelity PASS.
2. Current T4 tension branch fails source-fidelity: with initial tangent fixed to E0, its peak occurs at about 0.152 eps_cr and T4(eps_cr)≈0.4489, whereas Nguyen/Foster remains linear to cracking and reaches the cracking stress at eps_cr before tension-stiffening decay. T4 must reopen.
3. Foster CC envelope Eq. (3.17) gives equal-biaxial peak factor 1.1625, so the current CC coefficient can be closed without structural calibration as `k_eta=0.1625`.
4. If the smooth TC reduction family `Gamma=1/(1+k_tc r^2)`, `r=eps_t/eps_c0`, is retained, a source-only material-area closure on r∈[0,1] yields the unique positive root `atan(sqrt(k))/sqrt(k)=10/17+(1/0.34)ln(1.14)` and `k_tc=0.0830721554223...`. No Case21 load enters.
5. The globally additive Poisson correction Pi passes only the zero-strain plane-stress tangent gate but fails finite-strain behavior: it grows linearly without bound and destroys compression/tension softening. In Case21 material scale, equal biaxial compression at c=1 already gives |sigma|/fc≈1.60164 versus Foster peak 1.1625, and the stress re-grows at larger strain. `ADDITIVE_POISSON_FINITE_STRAIN_GATE=FAIL`.
6. Therefore do not production-lock NC-M4-R12-direct2D and do not rerun Case21 yet. Next task is to reconstruct finite-strain Poisson coupling with zero new free parameters, exact plane-stress tangent at the origin, and bounded/softening-compatible behavior; concurrently replace T4 with a source-consistent tensile representation.

GitHub report commit: f466d010c19a984ddc489abfc4ab2276916d46f9
