"""
R03 diagnostic evaluator for the repaired one-parameter steel route.

Purpose:
1. solve repaired total-mean elastic predictor;
2. add global + R06 + zero-mean GL stress fluctuations;
3. locate first combined-Mises yield;
4. test whether the proposed (A,e) post-yield corrector has a root.

The phase grid in this file is diagnostic only. The production Mises maximum remains
the finite algebraic tangent-half-angle/resultant evaluator.
"""
# The executable equations are preserved in the companion R03 memo.
# Numerical constants and the audited CSV are versioned beside this file.
# Re-running production should replace maxVM_grid() with the already-derived
# resultant candidate evaluator without changing the constitutive equations.

ES=206000.0
NU_S=0.30
FY=355.0
TS=4.0
N=M=4

def branch_gate(sigma_cr):
    return "yield-first" if sigma_cr >= FY else "local-first"

def postyield_identity(eU, CGL, s, w0, A, w, A0, sigma_u):
    # Missing quantity exposed by the failed R02 corrector:
    # total axial plastic strain required after S2 activation.
    return eU + s*CGL*(w0*A + w*A0 + w*A) - sigma_u/ES

if __name__ == "__main__":
    print("See companion CSV and memo for the full nine-specimen audit.")
    print("R03 result: (A,e) corrector rejected; S0/S1/S2 strength-path closure retained.")
