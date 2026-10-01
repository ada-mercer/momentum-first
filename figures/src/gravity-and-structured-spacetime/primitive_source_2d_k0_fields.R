#!/usr/bin/env Rscript
# Stable registry entrypoint. The legacy output slug is retained in place.
# Exact panel labels and reproducible weak-field arrays are rendered by Python.
args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep('^--file=', args, value = TRUE)
if (!length(file_arg)) stop('Run this entrypoint with Rscript')
script_path <- normalizePath(sub('^--file=', '', file_arg[1]))
script_dir <- dirname(script_path)
project_root <- normalizePath(file.path(script_dir, '..', '..', '..'))
python <- Sys.getenv('FIGURES_PYTHON', '')
if (!nzchar(python)) {
  local_python <- file.path(project_root, '.venv', 'bin', 'python')
  python <- if (file.exists(local_python)) local_python else Sys.which('python3')
}
if (!nzchar(python)) stop('Set FIGURES_PYTHON to Python with numpy and matplotlib')
renderer <- file.path(script_dir, 'primitive_source_2d_k0_fields.py')
status <- system2(python, c(shQuote(renderer), vapply(commandArgs(trailingOnly = TRUE), shQuote, '')))
if (status != 0) quit(status = status)
