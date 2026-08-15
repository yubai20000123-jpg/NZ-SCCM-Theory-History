# Zhou four-edge axial comparator — source evidence note

**Timestamp:** 2026-08-15 14:07 +08:00

## Primary dissertation evidence

The source search recovered the exact §5.3.4 passage around Eqs. (5-87)-(5-88). Zhou first notes that the existing two-edge, three-edge, Winter, and CECS curves do not fit the four-edge axial FE points. The dissertation then states, in concise source wording, that the Perry-Robertson form is used to fit the **“曲线的下包络线”**. After Eqs. (5-87)-(5-88), the text states that the fitted formula **“能很好地包络所有有限元点”** and is suitable for four-edge axial stability design.

This establishes the source role directly:

```text
Eq.5-87 / Eq.5-88 = lower-envelope fit to FE point cloud for design
Eq.5-87 / Eq.5-88 != individual FE point
```

Figure 5.8 is identified in the dissertation figure list as the fitted four-edge axial stability curve.

## Independent journal evidence

The 2021 Thin-Walled Structures article `10.1016/j.tws.2021.107966` independently states that the design curve is based on numerous FE models with imperfection amplitude `w0=a/500` and conservatively predicts ultimate axial resistance.

## Data-recovery consequence

The raw FE point cloud is therefore a separate validation dataset. No source table or public supplementary file was recovered that maps every nonlinear FE model's full parameter tuple to its ultimate axial resistance. Z0-Z6 cannot be assigned to visually nearby Figure-5.8 points without an unambiguous series/model mapping.

```text
RAW_FE_NUMERIC_MAPPING = OPEN
UNLABELED_NEAREST_POINT_DIGITIZATION = PROHIBITED
```
