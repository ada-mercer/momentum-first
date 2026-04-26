#!/usr/bin/env Rscript
# Source-side directional gravity densities from the realized split
# for a uniformly dense rotating body.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- if (length(file_arg)) sub("^--file=", "", file_arg[1]) else getwd()
script_dir <- dirname(normalizePath(script_path))
project_root <- normalizePath(file.path(script_dir, "..", "..", ".."))

figure_slug <- "source-side-density-maps"
figure_dir <- file.path(project_root, "figures", "build", "gravity-and-structured-spacetime")
png_path <- file.path(figure_dir, paste0(figure_slug, ".png"))
pdf_path <- file.path(figure_dir, paste0(figure_slug, ".pdf"))
svg_path <- file.path(figure_dir, paste0(figure_slug, ".svg"))
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)

n <- 321
x <- seq(-1.05, 1.05, length.out = n)
y <- seq(-1.05, 1.05, length.out = n)

compute_source_fields <- function() {
  xy <- expand.grid(x = x, y = y)
  R <- sqrt(xy$x^2 + xy$y^2)
  Theta <- atan2(xy$y, xy$x)
  inside <- R <= 1

  rho <- 1.0
  p_f <- 1.0
  eta <- 0.65

  p_mag <- ifelse(inside, eta * p_f * R, NA)
  p_k <- ifelse(inside, -p_mag * sin(Theta), NA)
  M <- ifelse(inside, sqrt(p_f^2 + p_mag^2), NA)
  Jplus <- ifelse(inside, rho * (M + 0.5 * p_k), NA)
  Jminus <- ifelse(inside, rho * (M - 0.5 * p_k), NA)
  Mk <- ifelse(inside, 0.5 * (Jplus + Jminus), NA)
  Pk <- ifelse(inside, Jplus - Jminus, NA)

  zmat <- function(v) matrix(v, nrow = n, ncol = n, byrow = FALSE)

  list(
    Jplus = Jplus,
    Jminus = Jminus,
    Mk = Mk,
    Pk = Pk,
    ZJp = zmat(Jplus),
    ZM = zmat(Mk),
    ZP = zmat(Pk)
  )
}

seq_cols <- colorRampPalette(c("#f7fbff", "#c6dbef", "#6baed6", "#2171b5", "#08306b"))(140)
div_cols <- colorRampPalette(c("#2166ac", "#67a9cf", "#d1e5f0", "#f7f7f7", "#fddbc7", "#ef8a62", "#b2182b"))(161)

body_outline <- function() {
  th <- seq(0, 2 * pi, length.out = 500)
  lines(cos(th), sin(th), lwd = 2.2, col = "#333333")
}

draw_arc_arrow <- function(r, start, end, col = "#b35900", lwd = 2) {
  th <- seq(start, end, length.out = 140)
  xs <- r * cos(th)
  ys <- r * sin(th)
  lines(xs, ys, lwd = lwd, col = col)
  n_pts <- length(xs)
  arrows(xs[n_pts - 8], ys[n_pts - 8], xs[n_pts], ys[n_pts], length = 0.08, lwd = lwd, col = col)
}

field_panel <- function(Z, title_expr, cols, zlim = NULL, add_zero_contour = FALSE, zero_col = "#444444", draw_contour = TRUE) {
  par(mar = c(2.2, 2.2, 4.0, 1.2), xaxs = "i", yaxs = "i")
  plot.new()
  plot.window(xlim = range(x), ylim = range(y), asp = 1)
  image(x, y, Z, col = cols, zlim = zlim, useRaster = TRUE, add = TRUE)
  if (draw_contour) {
    contour(x, y, Z, add = TRUE, drawlabels = FALSE, col = rgb(0, 0, 0, 0.16), lwd = 0.7, nlevels = 8)
  }
  if (add_zero_contour) {
    contour(x, y, Z, add = TRUE, levels = 0, drawlabels = FALSE, col = zero_col, lwd = 1.4)
  }
  body_outline()
  mtext(title_expr, side = 3, line = 1.0, cex = 0.98)
  box(col = "#bdbdbd")
}

draw_figure <- function(fields) {
  layout(matrix(c(1, 2, 3, 4, 5, 5), nrow = 3, byrow = TRUE), heights = c(1, 1, 0.12))
  par(oma = c(0, 0, 1.7, 0))

  par(mar = c(2.2, 2.2, 3.8, 1.2), xaxs = "i", yaxs = "i")
  plot.new()
  plot.window(xlim = c(-1.2, 1.2), ylim = c(-1.32, 1.2), asp = 1)

  symbols(0, 0, circles = 1, inches = FALSE, add = TRUE, bg = rgb(0.80, 0.90, 0.96, 0.35), fg = NA)
  for (r in c(0.3, 0.6, 0.85)) {
    th <- seq(0, 2 * pi, length.out = 400)
    lines(r * cos(th), r * sin(th), col = rgb(0.3, 0.3, 0.3, 0.20), lwd = 1)
  }
  body_outline()
  points(0, 0, pch = 16, cex = 0.7, col = "#333333")

  arc_col <- "#b35900"
  draw_arc_arrow(0.30, start = 0.28 * pi, end = 1.38 * pi, col = arc_col, lwd = 2.0)
  span <- 0.42 * pi
  centers <- c(0, 2 * pi / 3, 4 * pi / 3)
  for (ctr in centers) {
    draw_arc_arrow(0.60, start = ctr - span / 2, end = ctr + span / 2, col = arc_col, lwd = 1.5)
  }
  draw_arc_arrow(0.85, start = 0.18 * pi, end = 1.78 * pi, col = arc_col, lwd = 2.2)
  text(0.66, 0.96, labels = expression(omega), col = arc_col, cex = 0.95)

  mtext(expression("(a) " * "Rotating source model"), side = 3, line = 0.8, cex = 1.05)
  box(col = "#bdbdbd")

  field_panel(
    fields$ZJp,
    title_expr = expression("(b) " * scriptstyle(J)[k]^"+"),
    cols = seq_cols,
    zlim = range(c(fields$Jplus, fields$Jminus), na.rm = TRUE),
    draw_contour = TRUE
  )

  field_panel(
    fields$ZM,
    title_expr = expression("(c) " * scriptstyle(M)[k] == frac(scriptstyle(J)[k]^"+" + scriptstyle(J)[k]^"-", 2)),
    cols = seq_cols,
    zlim = range(fields$Mk, na.rm = TRUE),
    draw_contour = TRUE
  )

  pmax_abs <- max(abs(fields$Pk), na.rm = TRUE)
  field_panel(
    fields$ZP,
    title_expr = expression("(d) " * scriptstyle(P)[k] == scriptstyle(J)[k]^"+" - scriptstyle(J)[k]^"-"),
    cols = div_cols,
    zlim = c(-pmax_abs, pmax_abs),
    add_zero_contour = TRUE,
    draw_contour = TRUE
  )

  par(mar = c(0.2, 3.0, 0.2, 3.0), xaxs = "i", yaxs = "i")
  plot.new()
  plot.window(xlim = c(0, 1), ylim = c(0, 1))
  arrows(0.12, 0.42, 0.90, 0.42, length = 0.07, lwd = 2.0, col = "#444444")
  text(0.50, 0.64, labels = "k", cex = 1.0, col = "#333333")
  text(0.92, 0.54, labels = "k+", cex = 1.0, col = "#333333")

  mtext("Source-side directional gravity densities from the realized split for a uniformly dense rotating body", outer = TRUE, cex = 1.15, font = 2)
}

render_with_device <- function(device, path, width, height, res = NULL) {
  dir.create(dirname(path), recursive = TRUE, showWarnings = FALSE)
  if (identical(device, png)) {
    device(path, width = width, height = height, res = res)
  } else {
    device(path, width = width, height = height)
  }
  on.exit(dev.off(), add = TRUE)
  draw_figure(compute_source_fields())
}

render_with_device(grDevices::png, png_path, width = 2300, height = 1850, res = 220)
render_with_device(grDevices::cairo_pdf, pdf_path, width = 10.45, height = 8.41)
render_with_device(grDevices::svg, svg_path, width = 10.45, height = 8.41)

cat(png_path, "\n")
cat(pdf_path, "\n")
cat(svg_path, "\n")
