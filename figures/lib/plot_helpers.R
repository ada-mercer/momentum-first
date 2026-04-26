options(bitmapType = "cairo")

figure_palette_m1 <- list(
  source = "#fbbf24",
  field = "#22d3ee",
  observer = "#a78bfa",
  text = "#e5f0ff",
  muted = "#94a3b8",
  bg = "#0b1020"
)

figure_theme_m1 <- function(base_size = 12, dark = FALSE) {
  if (dark) {
    ggplot2::theme_minimal(base_size = base_size) +
      ggplot2::theme(
        plot.background = ggplot2::element_rect(fill = figure_palette_m1$bg, colour = NA),
        panel.background = ggplot2::element_rect(fill = figure_palette_m1$bg, colour = NA),
        legend.background = ggplot2::element_rect(fill = figure_palette_m1$bg, colour = NA),
        legend.key = ggplot2::element_rect(fill = figure_palette_m1$bg, colour = NA),
        text = ggplot2::element_text(colour = figure_palette_m1$text),
        axis.text = ggplot2::element_text(colour = figure_palette_m1$text),
        axis.title = ggplot2::element_text(colour = figure_palette_m1$text),
        panel.grid.minor = ggplot2::element_blank()
      )
  } else {
    ggplot2::theme_minimal(base_size = base_size) +
      ggplot2::theme(
        panel.grid.minor = ggplot2::element_blank(),
        legend.position = "bottom"
      )
  }
}

ensure_figure_dir <- function(path) {
  dir.create(dirname(path), recursive = TRUE, showWarnings = FALSE)
  invisible(path)
}

save_figure_set <- function(plot, png_path, pdf_path = NULL, svg_path = NULL,
                            width = 8, height = 6, units = "in", dpi = 300) {
  ensure_figure_dir(png_path)
  ggplot2::ggsave(png_path, plot = plot, width = width, height = height, units = units, dpi = dpi, device = ragg::agg_png)
  if (!is.null(pdf_path)) {
    ensure_figure_dir(pdf_path)
    ggplot2::ggsave(pdf_path, plot = plot, width = width, height = height, units = units, device = cairo_pdf)
  }
  if (!is.null(svg_path)) {
    ensure_figure_dir(svg_path)
    ggplot2::ggsave(svg_path, plot = plot, width = width, height = height, units = units, device = svglite::svglite)
  }
}
