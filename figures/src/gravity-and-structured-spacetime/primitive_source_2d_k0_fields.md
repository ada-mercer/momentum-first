# Primitive 2D K0 source-field figure notes

This note documents the math used by `primitive_source_2d_k0_fields.R`.

## Source profile

The plotted source is pointlike in the transverse plane and exponentially distributed along the axial direction:

\[
J_k^+(r,z)=Q_+\,{\delta(r)\over 2\pi r}\,f(z),
\qquad
f(z)={e^{-|z|/r_0}\over 2r_0}.
\]

The balanced comparison uses the same total source amount split equally between the two channels:

\[
J_k^+=J_k^-={Q_+\over2}{\delta(r)\over2\pi r}f(z).
\]

## Why `K_0(r/r_0)` appears

At the midplane, the axial convolution of the 3D Green kernel gives

\[
\int_{-\infty}^{\infty}
{e^{-|z|/r_0}\over 2r_0\sqrt{r^2+z^2}}\,dz
=
{1\over r_0}K_0(r/r_0).
\]

So the plotted radial dependence uses `K_0(r/r_0)` rather than the strict 2D logarithm.

## Interpretation in the figure

- Single-channel case `(Q_+,0)`: scalar field `theta_0`, directional field `theta_1`, scalar package `G`, and shift package `A_1` are nonzero.
- Balanced pair `(Q_+/2,Q_+/2)`: scalar response remains matched by total source amount, but the odd/shift sector cancels, so `theta_1=A_1=0`.
- Dashed circle marks `r=r_0`, the axial profile scale.

The exact derivation is mirrored in `book/tiers/T1_foundations/GR_PRIMITIVE_SOURCE_AXIAL_K0_REDUCTION_V1.md`.
