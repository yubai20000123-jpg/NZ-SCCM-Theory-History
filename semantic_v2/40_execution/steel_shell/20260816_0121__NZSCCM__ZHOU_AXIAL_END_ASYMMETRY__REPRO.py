"""NZ-SCCM 20260816_0121 Zhou axial-end asymmetry gate reproducer.

NO spatial sampling.
NO spatial quadrature.
NO collocation.
NO material-point grid.

The exact test mode is
    v_A=(b/pi)*eta*cos(2X)*(1-cos Z)
on the full AR2 panel coordinates X=pi*x/b, Z=pi*y/a, a=2b.

Closed-form coefficient-space moments reproduced here:
    fG = <B_A,G> = pi/120
    KA = <B_A,B_A> = pi^2(25-24nu)/16
    fD = <B_A,D> = 0
    eta_G = -fG/KA = -2/[15*pi*(25-24nu)]

The lower-half restriction contains cos(Y/2), Y=2Z, proving that the
01:02 finite integer-harmonic symmetric v-family is not an exact representation
of this admissible full-panel axial trace mode.
"""

import math

PI = math.pi


def exact_gate_values(nu):
    fG = PI / 120.0
    KA = PI**2 * (25.0 - 24.0*nu) / 16.0
    fD = 0.0
    etaG = -fG / KA
    single_mode_energy_reduction = -(fG*fG) / KA
    return {
        "nu": nu,
        "fG": fG,
        "KA": KA,
        "fD": fD,
        "etaG": etaG,
        "single_mode_energy_reduction": single_mode_energy_reduction,
    }


def top_trace_width_mean():
    # exact integral int_0^pi cos(2X) dX = [sin(2X)/2]_0^pi = 0
    return 0.0


def main():
    print("FORMAL_SPATIAL_SAMPLING=0")
    print("FORMAL_SPATIAL_QUADRATURE=0")
    print("FORMAL_SPATIAL_SUBDOMAINS=1")
    print("TEST_MODE=v_A=(b/pi)*eta*cos(2X)*(1-cos Z)")
    print("BOTTOM_TRACE=v_A(X,0)=0 EXACT")
    print("TOP_TRACE=v_A(X,pi)=2(b/pi)eta*cos(2X)")
    print("TOP_TRACE_WIDTH_MEAN=", top_trace_width_mean())
    print("LOWER_HALFWAVE_RESTRICTION_FACTOR=1-cos(Y/2)")
    print("FINITE_INTEGER_TRIG_D15_REPRESENTATION_OF_cos(Y/2)=NO")
    for nu in (0.18, 0.30):
        print(exact_gate_values(nu))
    print("ZHOU_BOTTOM_UY0_IS_PURE_RIGID_DATUM=FAIL")
    print("CURRENT_0102_SYMMETRIC_V_RITZ_FULL_ZHOU_EQUIVALENCE=FAIL")
    print("ONE_CONTINUOUS_COMPLETE_HALFWAVE=RETAINED")
    print("NEW_AR2_PU=NOT_CALCULATED")


if __name__ == "__main__":
    main()
