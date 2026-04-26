#!/usr/bin/env Rscript

options(bitmapType = "cairo")

suppressPackageStartupMessages({
  library(ggplot2)
})

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- if (length(file_arg)) sub("^--file=", "", file_arg[1]) else getwd()
script_dir <- dirname(normalizePath(script_path))
project_root <- normalizePath(file.path(script_dir, "..", "..", ".."))

figure_slug <- "momentum-triangle"
figure_dir <- file.path(project_root, "figures", "build", "foundations")
png_path <- file.path(figure_dir, paste0(figure_slug, ".png"))
pdf_path <- file.path(figure_dir, paste0(figure_slug, ".pdf"))
svg_path <- file.path(figure_dir, paste0(figure_slug, ".svg"))
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)

pf_seg <- data.frame(x = 0.00, y = 0.00, xend = 1.42, yend = 0.00)
p_seg <- data.frame(x = 0.00, y = 0.00, xend = 0.00, yend = 0.76)
M_seg <- data.frame(x = 0.00, y = 0.76, xend = 1.42, yend = 0.00)

triangle_fill <- data.frame(
  x = c(0.00, 1.42, 0.00),
  y = c(0.00, 0.00, 0.76)
)

right_angle <- data.frame(
  x = c(0.08, 0.08),
  y = c(0.00, 0.08),
  xend = c(0.08, 0.00),
  yend = c(0.08, 0.08)
)

p <- ggplot() +
  geom_polygon(
    data = triangle_fill,
    aes(x = x, y = y),
    fill = "#f8fafc",
    color = NA
  ) +
  geom_segment(
    data = pf_seg,
    aes(x = x, y = y, xend = xend, yend = yend),
    linewidth = 1.05,
    color = "#475569",
    lineend = "round"
  ) +
  geom_segment(
    data = p_seg,
    aes(x = x, y = y, xend = xend, yend = yend),
    linewidth = 1.05,
    color = "#475569",
    lineend = "round"
  ) +
  geom_segment(
    data = M_seg,
    aes(x = x, y = y, xend = xend, yend = yend),
    linewidth = 1.15,
    color = "#111827",
    lineend = "round"
  ) +
  geom_segment(
    data = right_angle,
    aes(x = x, y = y, xend = xend, yend = yend),
    linewidth = 0.38,
    color = "#64748b"
  ) +
  annotate(
    "text",
    x = 0.71,
    y = -0.08,
    label = "p[f]",
    parse = TRUE,
    family = "serif",
    size = 7.0 / .pt,
    color = "#334155"
  ) +
  annotate(
    "text",
    x = -0.09,
    y = 0.38,
    label = "p",
    parse = TRUE,
    family = "serif",
    size = 7.0 / .pt,
    color = "#334155"
  ) +
  annotate(
    "text",
    x = 0.74,
    y = 0.43,
    label = "M",
    parse = TRUE,
    family = "serif",
    size = 7.2 / .pt,
    angle = -24,
    color = "#111827"
  ) +
  coord_equal(xlim = c(-0.14, 1.52), ylim = c(-0.10, 0.86), expand = FALSE) +
  theme_void() +
  theme(
    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "white", color = NA)
  )

if (requireNamespace("ragg", quietly = TRUE)) {
  ggsave(
    filename = png_path,
    plot = p,
    width = 4.4,
    height = 2.9,
    units = "in",
    dpi = 300,
    device = ragg::agg_png,
    bg = "white"
  )
} else {
  ggsave(
    filename = png_path,
    plot = p,
    width = 4.4,
    height = 2.9,
    units = "in",
    dpi = 300,
    bg = "white"
  )
}

ggsave(
  filename = pdf_path,
  plot = p,
  width = 4.4,
  height = 2.9,
  units = "in",
  device = cairo_pdf,
  bg = "white"
)

ggsave(
  filename = svg_path,
  plot = p,
  width = 4.4,
  height = 2.9,
  units = "in",
  device = svglite::svglite,
  bg = "white"
)

cat(png_path, "\n")
cat(pdf_path, "\n")
cat(svg_path, "\n")
