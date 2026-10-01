# Correction to the primitive axial-profile kernel

The finite normalized exponential profile and its integrated channel strength are retained. The old identification of its inverse-distance convolution with K0 was incorrect:

$$
\int_0^\infty\frac{e^{-az}}{\sqrt{z^2+b^2}}\,dz
=\int_0^\infty e^{-ab\sinh t}\,dt,
$$

not the cosh representation of K0(ab). The corrected finite-source kernel has an inverse-distance far tail. The current renderer evaluates the actual integral.

The current figure is a primitive **linear channel-contribution** diagram, not a standalone particle population. Its `(Qplus,0)` column therefore does not assert that a physical shell has one vanishing opposed reading. Full-source transport and conservation remain governed by the current source equations.

The rebuilt calculation, source normalization, distinction between component contributions and complete solutions, and render instructions are in [the current source note](../../src/gravity-and-structured-spacetime/primitive_source_2d_k0_fields.md). Earlier versions remain in Git history. The interim finite-cylinder beam model has been superseded rather than promoted into this diagram's meaning.
