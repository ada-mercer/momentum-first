# Primitive single-channel response — finite axial profile

## Visual job and source identity

Compare the contribution of one directional source channel with a balanced pair at the same total channel amount. Retain the paired theta/phi maps, restore the finite axial source curves and the reference strength Qplus, and keep calculation details here rather than on the image. The historical figure ID and output basename are unchanged.

The upper curves display the transverse-integrated axial weights of the channel distributions. A pair above each graph labels its entire selected profiles: `(J1plus,0)` or `(J1plus/2,J1minus/2)`. The small amounts pair alongside gives their integrals, with plus/minus as directional superscripts on Q. The matched full-strength reference amounts are equal and positive; the balanced plot uses half of each. The lower panels show the midplane transverse response. There are no colorbars, direction-symbol legends, radius-calibration circles, explanatory footer or redundant panel numbers. Corresponding maps use identical scales internally. Their common outer outline is the plot window, not a source boundary.

## Primitive contribution, not a particle-population replacement

This is a **formal decomposition of the linear response into channel contributions**. It is not the previous steady-light-beam example. Write the temporal and directional source inputs as

$$
\mathcal M+\mathcal C^i{}_i
=\tfrac12\mathcal J_1^++\tfrac12\mathcal J_1^-+\mathcal C^i{}_i,
\qquad
\mathcal P_1=\mathcal J_1^+-\mathcal J_1^-.
$$

The figure displays the channel terms; the transport response is separate. Linearity permits individual terms of a complete source to be inspected even when one term is not an independently realizable source. The source dictionary and physical particle cone are unchanged. In particular, a nonzero `(Jplus,0)` is not being promoted to the shell of a particle or a self-contained conserved stationary body. Nor is aggregate transport inferred from these channels or physically set to zero.

The displayed channel-only maps need not satisfy the complete harmonic/gauge and conservation conditions independently. Those apply to the assembled source and solution. Here the operation is the stated linear Green response, followed by the first-order registered theta-to-phi map. This explanatory use is a manuscript candidate, not a new physical law or theory lock.

## Finite source amount and restored profile

Let $\mathcal J_1^+$ and $\mathcal J_1^-$ be **matched full-strength reference profiles** in the opposed directions. Their positive integrated amounts are

$$
Q^\pm=\int\mathcal J_1^\pm(\mathbf x)\,d^3\mathbf x,
\qquad Q^+=Q^->0.
$$

The superscripts identify direction, not a sign of the quantity. These reference amounts are distinct from the dilation trace charge Q. The second column uses half of each reference profile, so its actual selected amounts are `(Qplus/2,Qminus/2)`, not the full reference amounts themselves. With z along the first spatial axis,

$$
f(z)=\frac{e^{-|z|/r_0}}{2r_0},\qquad
\int_{-\infty}^{\infty}f(z)\,dz=1.
$$

The full-strength transverse line profiles are

$$
\mathcal J_1^\pm(\mathbf x_\perp,z)
=Q^\pm\delta^{(2)}(\mathbf x_\perp)f(z).
$$

The selected profile pairs are

$$
(\mathcal J_1^+,0),\qquad
\left(\tfrac{\mathcal J_1^+}{2},\tfrac{\mathcal J_1^-}{2}\right).
$$

Form the channel mean and difference from these selected pairs. Their means match; their difference is Qplus times the profile in the single-channel case and zero in the balanced case. The actual source curves and their numerical normalization are unchanged by this notation revision. The full distributions have finite integrated amounts even though their exponential tails extend beyond the drawing.

## Correct radial kernel

At the midplane, the inverse-distance response uses

$$
I(r)=\int_{-\infty}^{\infty}
\frac{f(z)}{\sqrt{r^2+z^2}}\,dz
=\frac1{r_0}\int_0^\infty
 e^{-(r/r_0)\sinh t}\,dt,\qquad r>0.
$$

The last expression follows from z=r sinh(t) on the positive half-axis. It is **not** K0(r/r0)/r0. The renderer evaluates this integral by Gauss–Legendre quadrature after a controlled exponentially small tail truncation. Independent direct quadrature checks it. At large r, r I(r) tends to one, as required for a normalized finite axial source.

The line axis is singular and is omitted from the field grid, marked by the central point. No finite core radius or clipped plateau is invented. The plotted weak response is evaluated off axis; the unresolved source axis is not a claimed weak-field material interior.

## Channel-to-map calculation

For calculation only, abbreviate U(r)=(G_N Qplus/c^3) I(r). Then the isolated channel contributions are

$$
\theta^0{}_0=U/2,\qquad
\theta^1{}_0=-\theta^0{}_1=-U\quad\hbox{or}\quad0,
$$

and, at the retained first order,

$$
\phi^0{}_0=1-U/2,\qquad
\phi^1{}_0=4\theta^1{}_0=-4U\quad\hbox{or}\quad0.
$$

Both directional panels now use upper 1, lower 0. This is a sign-correct representation change: the plotted theta10 array is the negative of the former theta01 array, not the former array with a new label. V4 makes the lowered reference array $\eta\theta$ symmetric; the mixed array is not ordinarily symmetric. Phi is also not ordinarily symmetric: in the selected coframe $\phi^0{}_1=0$ while $\phi^1{}_0$ need not vanish. These facts are established by V4 §3 and Derivation 3.4A, not new theory.

The identity background is counted once. When assembling several contributions, add the changes in phi, not several identity maps. The spatial map change due to the channel term is `(U/2) delta^i_j`; the additional resolved-transport contribution belongs to the full source map and is not plotted here. There is no independent G/A packaging or universal clock-rate claim.

The plots use r0=1 and matched Qplus=Qminus=1 as source units, with G_N Qplus/(c^3 r0)=0.001 and a transverse window r<=4 r0. They show first-order phi, not the exact nonlinear reconstruction of an isolated channel piece. No rho field or scalar-sector completion is selected by this partial external-map illustration; the zero-rho qualification of the superseded beam model does not apply to it.

## Reproduction and validation

The registered R entrypoint invokes the adjacent NumPy/Matplotlib renderer. Use FIGURES_PYTHON to select an interpreter with those packages. `--data` exports the exact arrays; `--layout-report` exports the measured text extents. The renderer preserves accessible SVG metadata, editable text and unique raster IDs.

The current checker verifies source-profile normalization, reference strengths, preserved channel mean and cancelled difference, the actual axial convolution, its far tail, V4 linear coefficients, exact plotted arrays, source/figure placement, unchanged protected files, SVG/PDF/PNG output and warning-free reading previews. It does not relabel the superseded beam-conservation review as acceptance of this primitive-contribution diagram.

## Principal sources

- Owner's clarified purpose: integrated Qplus and a primitive single-channel response, not a substitute beam population.
- Historical source note at Git HEAD and the archived source section: normalized exponential profile and the two reference-strength allocations; the false K0 identity is not retained.
- Current section 3 channel identities and section 4 weak source/map equations.
- Derivations 3.3A and 3.4A and the V4 notation reference: physical source constraints, transport independence and theta/phi reconstruction.
