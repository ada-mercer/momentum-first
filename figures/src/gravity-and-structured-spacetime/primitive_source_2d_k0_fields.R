#!/usr/bin/env Rscript
# Primitive 2D source fields from an exponential axial profile.
# Horizontal grouped 2x2 layout with square-in-pixels panel regions.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep('^--file=', args, value = TRUE)
script_path <- if (length(file_arg)) sub('^--file=', '', file_arg[1]) else getwd()
script_dir <- dirname(normalizePath(script_path))
project_root <- normalizePath(file.path(script_dir, '..', '..', '..'))

figure_slug <- 'primitive-source-2d-k0-fields'
figure_dir <- file.path(project_root, 'figures', 'build', 'gravity-and-structured-spacetime')
png_path <- file.path(figure_dir, paste0(figure_slug, '.png'))
pdf_path <- file.path(figure_dir, paste0(figure_slug, '.pdf'))
svg_path <- file.path(figure_dir, paste0(figure_slug, '.svg'))
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)

W <- 1900
H <- 1350

n <- 361
x <- seq(-1.05, 1.05, length.out = n)
y <- seq(-1.05, 1.05, length.out = n)
xy <- expand.grid(x = x, y = y)
R <- sqrt(xy$x^2 + xy$y^2)
inside <- R <= 1
r_eps <- 0.03
r0 <- 0.42

a_single <- 0.12
b_single <- 0.18
a_bal <- 0.12
b_bal <- 0.00
k0_term <- besselK(pmax(R, r_eps) / r0, nu = 0)

th0_single_v <- ifelse(inside, a_single * k0_term, NA)
th1_single_v <- ifelse(inside, -b_single * k0_term, NA)
th0_bal_v <- ifelse(inside, a_bal * k0_term, NA)
th1_bal_v <- ifelse(inside, -b_bal * k0_term, NA)
G_single_v <- ifelse(inside, sqrt(pmax(1 - 2 * th0_single_v, 1e-6)), NA)
A1_single_v <- ifelse(inside, -th1_single_v, NA)
G_bal_v <- ifelse(inside, sqrt(pmax(1 - 2 * th0_bal_v, 1e-6)), NA)
A1_bal_v <- ifelse(inside, -th1_bal_v, NA)

zmat <- function(v) matrix(v, nrow = n, ncol = n, byrow = FALSE)
TH0s <- zmat(th0_single_v); TH1s <- zmat(th1_single_v); Gs <- zmat(G_single_v); A1s <- zmat(A1_single_v)
TH0b <- zmat(th0_bal_v); TH1b <- zmat(th1_bal_v); Gb <- zmat(G_bal_v); A1b <- zmat(A1_bal_v)

seq_cols <- colorRampPalette(c('#f7fbff', '#c6dbef', '#6baed6', '#2171b5', '#08306b'))(140)
seq_cols_G <- colorRampPalette(c('#eff6ff', '#bfdbfe', '#60a5fa', '#1d4ed8', '#1e3a8a'))(140)
div_cols <- colorRampPalette(c('#2166ac', '#67a9cf', '#d1e5f0', '#f7f7f7', '#fddbc7', '#ef8a62', '#b2182b'))(161)
zero_cols <- colorRampPalette(c('#ffffff', '#fafafa', '#f3f3f3'))(40)
th0_lim <- range(c(th0_single_v, th0_bal_v), na.rm = TRUE)
thi_abs <- max(abs(range(c(th1_single_v, th1_bal_v), na.rm = TRUE)), na.rm = TRUE)
G_lim <- range(c(G_single_v, G_bal_v), na.rm = TRUE)
Ai_abs <- max(abs(range(c(A1_single_v, A1_bal_v), na.rm = TRUE)), na.rm = TRUE)

body_outline <- function(scale = 0.98) {
  th <- seq(0, 2*pi, length.out = 500)
  lines(scale * cos(th), scale * sin(th), lwd = 2.0, col = '#333333')
}
r0_circle <- function(scale = 0.98) {
  th <- seq(0, 2*pi, length.out = 400)
  lines(scale * r0 * cos(th), scale * r0 * sin(th), lwd = 1.4, col = '#d4a017', lty = 2)
}

# fig rectangle from pixel coordinates: x,y are bottom-left in pixels.
fig_px <- function(x, y, w, h) c(x / W, (x + w) / W, y / H, (y + h) / H)

with_panel <- function(fig, expr) {
  par(fig = fig, new = TRUE, mar = c(0, 0, 0, 0), xaxs = 'i', yaxs = 'i')
  force(expr)
}

draw_field <- function(fig, Z, title_expr, cols, zlim = NULL, zero_panel = FALSE) {
  with_panel(fig, {
    plot.new(); plot.window(xlim = c(-1.03, 1.03), ylim = c(-1.18, 1.12), asp = 1)
    if (zero_panel) {
      rect(-1.03, -1.03, 1.03, 1.03, col = 'white', border = NA)
    } else {
      image(x, y, Z, col = cols, zlim = zlim, useRaster = TRUE, add = TRUE)
      contour(x, y, Z, add = TRUE, drawlabels = FALSE, col = rgb(0, 0, 0, 0.16), lwd = 0.7, nlevels = 8)
    }
    body_outline(); r0_circle(); points(0, 0, pch = 16, cex = 0.68, col = '#333333')
    mtext(title_expr, side = 3, line = -0.25, cex = 0.95)
  })
}

draw_geometry <- function(fig, title, channel_label) {
  with_panel(fig, {
    plot.new(); plot.window(xlim = c(-1.04, 1.04), ylim = c(-1.16, 1.10), asp = 1)
    th <- seq(0, 2*pi, length.out = 500); rad <- 0.96
    polygon(rad * cos(th), rad * sin(th), col = rgb(0.80, 0.90, 0.96, 0.22), border = NA)
    for (rr in c(0.33, 0.62, 0.88)) lines(rr * rad * cos(th), rr * rad * sin(th), col = rgb(0.3, 0.3, 0.3, 0.20), lwd = 1)
    lines(rad * cos(th), rad * sin(th), lwd = 2.0, col = '#333333')
    lines((r0 * rad) * cos(th), (r0 * rad) * sin(th), lwd = 1.5, col = '#d4a017', lty = 2)
    points(0, 0, pch = 16, cex = 0.9, col = '#333333')
    text(0.34 * rad, 0.08 * rad, labels = expression(r[0]), cex = 0.98, col = '#b8860b', pos = 4)
    text(0.04 * rad, 0.07 * rad, labels = 'source', cex = 0.82, col = '#333333', pos = 4)
    mtext(title, side = 3, line = -0.25, cex = 0.95)
    text(0, -1.05, labels = channel_label, cex = 0.9, font = 2)
  })
}

draw_figure <- function() {
  par(oma = c(0, 0, 0, 0), mar = c(0, 0, 0, 0), bg = 'white', xaxs = 'i', yaxs = 'i')
  plot.new(); plot.window(xlim = c(0, 1), ylim = c(0, 1))

# Square panel sizes in pixels. Critical fix: w == h in device pixels.
p <- 390
g <- 22
group_gap <- 80
group_w <- 2 * p + g
left1 <- (W - (2 * group_w + group_gap)) / 2
left2 <- left1 + group_w + group_gap

# y positions, cropped tightly around the plotted content.
bot_y <- 35
mid_y <- bot_y + p + 35
geo_y <- mid_y + p + 60

# helper for group panel positions
cell <- function(group_left, col, row_y) fig_px(group_left + (col - 1) * (p + g), row_y, p, p)
geom_fig <- function(group_left) fig_px(group_left + (group_w - p) / 2, geo_y, p, p)

# Lightweight group guide. Grouped subpanel labels are used because this is a two-case comparison.
par(fig = c(0, 1, 0, 1), new = TRUE, mar = c(0, 0, 0, 0), xaxs = 'i', yaxs = 'i')
plot.new(); plot.window(xlim = c(0, W), ylim = c(0, H))
segments(W/2, 35, W/2, H - 30, col = '#bdbdbd', lwd = 1.2)

# Geometry above each group's 2x2 fields.
draw_geometry(geom_fig(left1), expression('(a0) single-channel geometry'), expression((Q['+'] * ',' ~~ 0)))
draw_geometry(geom_fig(left2), expression('(b0) balanced-pair geometry'), expression((Q['+']/2 * ',' ~~ Q['+']/2)))

# Single-channel group, left.
draw_field(cell(left1, 1, mid_y), TH0s, expression('(a1) ' * theta[0]), seq_cols, th0_lim)
draw_field(cell(left1, 2, mid_y), TH1s, expression('(a2) ' * theta[1]), div_cols, c(-thi_abs, thi_abs))
draw_field(cell(left1, 1, bot_y), Gs, expression('(a3) ' * G), seq_cols_G, G_lim)
draw_field(cell(left1, 2, bot_y), A1s, expression('(a4) ' * A[1]), div_cols, c(-Ai_abs, Ai_abs))

# Balanced group, right.
draw_field(cell(left2, 1, mid_y), TH0b, expression('(b1) ' * theta[0]), seq_cols, th0_lim)
draw_field(cell(left2, 2, mid_y), TH1b, expression('(b2) ' * theta[1] == 0), zero_cols, c(0, 1), zero_panel = TRUE)
draw_field(cell(left2, 1, bot_y), Gb, expression('(b3) ' * G), seq_cols_G, G_lim)
draw_field(cell(left2, 2, bot_y), A1b, expression('(b4) ' * A[1] == 0), zero_cols, c(0, 1), zero_panel = TRUE)


}

render_with_device <- function(device, path, width, height, res = NULL) {
  dir.create(dirname(path), recursive = TRUE, showWarnings = FALSE)
  if (identical(device, grDevices::png)) {
    device(path, width = width, height = height, res = res)
  } else {
    device(path, width = width, height = height)
  }
  on.exit(dev.off(), add = TRUE)
  draw_figure()
}

render_with_device(grDevices::png, png_path, width = W, height = H, res = 220)
render_with_device(grDevices::cairo_pdf, pdf_path, width = W / 220, height = H / 220)
render_with_device(grDevices::svg, svg_path, width = W / 220, height = H / 220)

cat(png_path, '\n')
cat(pdf_path, '\n')
cat(svg_path, '\n')
