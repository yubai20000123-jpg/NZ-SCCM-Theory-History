from math import pi


def kcr_yun(r: float) -> float:
    return 4.0 * (3.0*r**4 + 2.0*r**2 + 3.0) / (3.0*r**2)


def kp_yun(r: float) -> float:
    num = (
        272*r**16 + 2856*r**14 + 11273*r**12 + 23146*r**10
        + 31506*r**8 + 23146*r**6 + 11273*r**4 + 2856*r**2 + 272
    )
    den = r**2 * (r**2 + 1)**2 * (r**2 + 4)**2 * (4*r**2 + 1)**2
    return num / den


def sigma_cr_yun(Es: float, nu: float, t: float, b: float, ell: float) -> float:
    r = ell / b
    return (
        kcr_yun(r)
        * pi**2 * Es / (12.0 * (1.0 - nu**2))
        * (t / b)**2
    )


# Real-source local gate:
# Shi, Gao & Guo, JCSR 180 (2021) 106581, specimen family DSCST140-120.
# In their notation the 140 mm welding spacing is vertical/loading-direction,
# while 120 mm is horizontal. For the Yun local coordinates this means
# ell=140 mm and transverse width b=120 mm.
shi = {
    "ell": 140.0,
    "b": 120.0,
    "t": 1.5,
    "Es": 215000.0,
    "nu": 0.24,
    "fy": 379.6,
}

r = shi["ell"] / shi["b"]
kcr = kcr_yun(r)
kp = kp_yun(r)
sigma = sigma_cr_yun(shi["Es"], shi["nu"], shi["t"], shi["b"], shi["ell"])

print(f"r={r:.16g}")
print(f"kcr_Yun={kcr:.15f}")
print(f"kp_Yun={kp:.15f}")
print(f"sigma_cr_Yun_MPa={sigma:.15f}")
print(f"sigma_cr_over_fy={sigma / shi['fy']:.15f}")
print(f"fy_over_sigma_cr_minus_1={shi['fy'] / sigma - 1.0:.15f}")
print(f"DIRECT_YUN_GATE={'PASS' if sigma < shi['fy'] else 'FAIL'}")

# Expected output:
# r=1.166666666666667
# kcr_Yun=11.049886621315194
# kp_Yun=44.082600459365610
# sigma_cr_Yun_MPa=323.966071641846950
# sigma_cr_over_fy=0.853440652375782
# fy_over_sigma_cr_minus_1=0.171727638256076
# DIRECT_YUN_GATE=PASS
