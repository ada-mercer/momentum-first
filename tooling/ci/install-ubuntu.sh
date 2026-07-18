#!/usr/bin/env bash
set -Eeuo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

export DEBIAN_FRONTEND=noninteractive
LOCAL_BIN="$HOME/.local/bin"
LOCAL_OPT="$HOME/.local/opt"
R_USER_LIB_DEFAULT="${HOME}/.local/share/R/%p-library/%v"
JULIA_VERSION="1.12.5"
JULIA_SERIES="1.12"
EDIT_PROFILE=1

log() {
  printf '\n==> %s\n' "$*"
}

warn() {
  printf '\n[warn] %s\n' "$*" >&2
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "[error] required command not found: $1" >&2
    exit 1
  }
}

cleanup_tmpdir() {
  if [[ -n "${TMP_DIR:-}" && -d "${TMP_DIR:-}" ]]; then
    rm -rf "$TMP_DIR"
  fi
}
trap cleanup_tmpdir EXIT

ensure_local_bin_on_path_now() {
  mkdir -p "$LOCAL_BIN" "$LOCAL_OPT"
  export PATH="$LOCAL_BIN:$PATH"
}

ensure_local_bin_on_path_future() {
  if [[ "$EDIT_PROFILE" -eq 0 ]]; then
    log "Skipping ~/.profile update (--ci/--no-profile-edit)"
    return 0
  fi
  if grep -Fqs 'export PATH="$HOME/.local/bin:$PATH"' "$HOME/.profile" 2>/dev/null; then
    return 0
  fi
  printf '\n# Added by momentum-first installer\nexport PATH="$HOME/.local/bin:$PATH"\n' >> "$HOME/.profile"
  warn "Added ~/.local/bin to ~/.profile. Open a new shell after install if commands are still missing."
}

apt_install() {
  log "Installing Ubuntu system packages"
  sudo apt-get update
  sudo apt-get install -y \
    build-essential \
    ca-certificates \
    curl \
    gfortran \
    git \
    gnupg \
    graphviz \
    inkscape \
    libcurl4-openssl-dev \
    libfontconfig1-dev \
    libfribidi-dev \
    libgit2-dev \
    libharfbuzz-dev \
    libjpeg-dev \
    libpng-dev \
    libssl-dev \
    libxml2-dev \
    librsvg2-bin \
    libtiff-dev \
    libuv1-dev \
    libx11-dev \
    libxt-dev \
    latexmk \
    biber \
    make \
    pandoc \
    python3 \
    python3-pip \
    python3-venv \
    r-base \
    software-properties-common \
    texlive \
    texlive-fonts-recommended \
    texlive-latex-extra \
    texlive-luatex \
    texlive-science \
    wget
}

fetch_latest_quarto_tag() {
  python3 - <<'PY'
import json, urllib.request
with urllib.request.urlopen('https://api.github.com/repos/quarto-dev/quarto-cli/releases/latest', timeout=30) as r:
    data = json.load(r)
print(data['tag_name'])
PY
}

install_quarto_local() {
  local tag version url extracted_dir
  tag="$(fetch_latest_quarto_tag)"
  version="${tag#v}"
  url="https://github.com/quarto-dev/quarto-cli/releases/download/${tag}/quarto-${version}-linux-amd64.tar.gz"

  log "Installing Quarto ${version} into ~/.local/opt"
  TMP_DIR="$(mktemp -d)"
  curl --fail --location --retry 5 --retry-delay 2 --retry-connrefused "$url" -o "$TMP_DIR/quarto.tar.gz"
  tar -xzf "$TMP_DIR/quarto.tar.gz" -C "$LOCAL_OPT"

  extracted_dir="$LOCAL_OPT/quarto-${version}"
  if [[ ! -x "$extracted_dir/bin/quarto" ]]; then
    echo "[error] Quarto install failed: expected binary missing at $extracted_dir/bin/quarto" >&2
    exit 1
  fi

  ln -sfn "$extracted_dir" "$LOCAL_OPT/quarto"
  ln -sfn "$LOCAL_OPT/quarto/bin/quarto" "$LOCAL_BIN/quarto"
}

install_julia_local() {
  local url extracted_dir
  url="https://julialang-s3.julialang.org/bin/linux/x64/${JULIA_SERIES}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz"

  log "Installing Julia ${JULIA_VERSION} into ~/.local/opt"
  TMP_DIR="$(mktemp -d)"
  curl --fail --location --retry 5 --retry-delay 2 --retry-connrefused "$url" -o "$TMP_DIR/julia.tar.gz"
  tar -xzf "$TMP_DIR/julia.tar.gz" -C "$LOCAL_OPT"

  extracted_dir="$LOCAL_OPT/julia-${JULIA_VERSION}"
  if [[ ! -x "$extracted_dir/bin/julia" ]]; then
    echo "[error] Julia install failed: expected binary missing at $extracted_dir/bin/julia" >&2
    exit 1
  fi

  ln -sfn "$extracted_dir" "$LOCAL_OPT/julia"
  ln -sfn "$LOCAL_OPT/julia/bin/julia" "$LOCAL_BIN/julia"
}

ensure_venv() {
  log "Creating/updating Python virtual environment"
  python3 -m venv .venv
  .venv/bin/pip install --upgrade pip
  .venv/bin/pip install -r tooling/ci/requirements.txt
}

ensure_repo_renviron() {
  if [[ ! -f "$ROOT_DIR/.Renviron" ]]; then
    printf 'R_LIBS_USER=%s\n' "$R_USER_LIB_DEFAULT" > "$ROOT_DIR/.Renviron"
  fi
}

ensure_r_packages() {
  log "Installing minimal R packages into user library"
  export R_LIBS_USER="${R_LIBS_USER:-$R_USER_LIB_DEFAULT}"
  Rscript -e 'dir.create(path.expand(Sys.getenv("R_LIBS_USER")), recursive=TRUE, showWarnings=FALSE); .libPaths(c(path.expand(Sys.getenv("R_LIBS_USER")), .libPaths())); pkgs <- c("knitr","rmarkdown"); miss <- pkgs[!vapply(pkgs, requireNamespace, logical(1), quietly=TRUE)]; if (length(miss)) install.packages(miss, repos="https://cloud.r-project.org"); miss <- pkgs[!vapply(pkgs, requireNamespace, logical(1), quietly=TRUE)]; if (length(miss)) stop(paste("R package install failed:", paste(miss, collapse=",")))'
}

summarize() {
  log "Installed tool versions"
  quarto --version
  python3 --version
  .venv/bin/python --version
  R --version | head -n 1 || true
  julia --version || true

  cat <<EOF

Install complete.

Useful next steps:
  cd "$ROOT_DIR"
  python3 tooling/scripts/check_dependencies.py
  .venv/bin/python -m pytest tooling/tests/test_dependencies.py

If a new shell still cannot find 'quarto' or 'julia', reload your shell or run:
  export PATH="$HOME/.local/bin:$PATH"
EOF
}

usage() {
  cat <<'EOF'
Usage: bash tooling/ci/install-ubuntu.sh [--ci] [--no-profile-edit]

Options:
  --ci               CI-friendly mode; do not edit ~/.profile.
  --no-profile-edit  Do not edit ~/.profile.
  -h, --help         Show this help.
EOF
}

parse_args() {
  for arg in "$@"; do
    case "$arg" in
      --ci|--no-profile-edit)
        EDIT_PROFILE=0
        ;;
      -h|--help)
        usage
        exit 0
        ;;
      *)
        echo "[error] unknown option: $arg" >&2
        usage >&2
        exit 2
        ;;
    esac
  done

  if [[ "${CI:-}" == "true" ]]; then
    EDIT_PROFILE=0
  fi
}

main() {
  parse_args "$@"

  if [[ -f /etc/os-release ]]; then
    . /etc/os-release
    if [[ "${ID:-}" != "ubuntu" && "${ID_LIKE:-}" != *debian* ]]; then
      warn "This installer is tuned for Ubuntu/Debian. Detected: ${PRETTY_NAME:-unknown}."
    fi
  fi

  require_command sudo
  require_command python3
  require_command curl
  ensure_local_bin_on_path_now
  apt_install
  ensure_local_bin_on_path_future

  if ! command -v quarto >/dev/null 2>&1; then
    install_quarto_local
  else
    log "Quarto already available at $(command -v quarto)"
  fi

  if ! command -v julia >/dev/null 2>&1; then
    install_julia_local
  else
    log "Julia already available at $(command -v julia)"
  fi

  ensure_repo_renviron
  ensure_venv
  ensure_r_packages
  summarize
}

main "$@"
