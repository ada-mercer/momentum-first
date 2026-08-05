#!/usr/bin/env Rscript

options(repos = c(CRAN = "https://cloud.r-project.org"), Ncpus = 2L)
Sys.setenv(MAKEFLAGS = "-j2")

dir.create(Sys.getenv("R_LIBS_USER"), recursive = TRUE, showWarnings = FALSE)
.libPaths(c(Sys.getenv("R_LIBS_USER"), .libPaths()))

if (!requireNamespace("remotes", quietly = TRUE) ||
    as.character(utils::packageVersion("remotes")) != "2.5.0") {
  utils::install.packages("remotes")
}

required <- c(
  knitr = "1.51",
  rmarkdown = "2.31",
  ggplot2 = "4.0.2",
  svglite = "2.2.2",
  ragg = "1.5.2"
)

for (package in names(required)) {
  version <- required[[package]]
  installed <- requireNamespace(package, quietly = TRUE) &&
    as.character(utils::packageVersion(package)) == version
  if (!installed) {
    remotes::install_version(
      package,
      version = version,
      dependencies = NA,
      upgrade = "never"
    )
  }
}

actual <- vapply(names(required), function(package) {
  as.character(utils::packageVersion(package))
}, character(1))

if (!identical(unname(actual), unname(required))) {
  stop(sprintf(
    "R package version mismatch: expected %s; got %s",
    paste(sprintf("%s=%s", names(required), required), collapse = ", "),
    paste(sprintf("%s=%s", names(actual), actual), collapse = ", ")
  ))
}

writeLines(paste(sprintf("%s=%s", names(actual), actual), collapse = "\n"))
