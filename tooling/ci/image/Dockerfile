# syntax=docker/dockerfile:1.7

FROM ubuntu:24.04@sha256:019e8eb29a85e74d64925745884f2ec79aa27e3feab36353d24656f4d6b89467

ARG QUARTO_VERSION=1.9.36
ARG QUARTO_SHA256=8c47762e78fe58642246a94d18f67eb332c1778b711e5bef991ef3c15490d83a
ARG UV_VERSION=0.12.1
ARG UV_SHA256=90b2f223fb69d19db49e117da601f64978593417988530aa733d456141b4bcbb
ARG GH_VERSION=2.97.0
ARG GH_SHA256=a2c9b8497e1f85b1ad0dfcb78b5a622e098801b8e461e459e88e1ee12f018112

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC \
    UV_PYTHON_INSTALL_DIR=/opt/momentum-first/python \
    UV_PYTHON_PREFERENCE=only-managed \
    R_LIBS_USER=/opt/momentum-first/R/library \
    PATH=/opt/momentum-first/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt/lists,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
      bash \
      biber \
      build-essential \
      ca-certificates \
      curl \
      gfortran \
      git \
      latexmk \
      libcurl4-openssl-dev \
      libfontconfig1-dev \
      libfribidi-dev \
      libgit2-dev \
      libharfbuzz-dev \
      libjpeg-dev \
      libpng-dev \
      libssl-dev \
      libtiff-dev \
      libuv1-dev \
      libxml2-dev \
      make \
      pkg-config \
      poppler-utils \
      r-base \
      texlive \
      texlive-fonts-recommended \
      texlive-latex-extra \
      texlive-luatex \
      texlive-science

RUN curl --fail --location --retry 5 \
      "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.deb" \
      --output /tmp/quarto.deb \
    && printf '%s  %s\n' "${QUARTO_SHA256}" /tmp/quarto.deb | sha256sum --check --strict \
    && dpkg --install /tmp/quarto.deb \
    && rm /tmp/quarto.deb

RUN curl --fail --location --retry 5 \
      "https://github.com/astral-sh/uv/releases/download/${UV_VERSION}/uv-x86_64-unknown-linux-gnu.tar.gz" \
      --output /tmp/uv.tar.gz \
    && printf '%s  %s\n' "${UV_SHA256}" /tmp/uv.tar.gz | sha256sum --check --strict \
    && tar --extract --gzip --file /tmp/uv.tar.gz --directory /tmp \
    && install --mode 0755 /tmp/uv-x86_64-unknown-linux-gnu/uv /usr/local/bin/uv \
    && install --mode 0755 /tmp/uv-x86_64-unknown-linux-gnu/uvx /usr/local/bin/uvx \
    && rm -rf /tmp/uv.tar.gz /tmp/uv-x86_64-unknown-linux-gnu

RUN curl --fail --location --retry 5 \
      "https://github.com/cli/cli/releases/download/v${GH_VERSION}/gh_${GH_VERSION}_linux_amd64.tar.gz" \
      --output /tmp/gh.tar.gz \
    && printf '%s  %s\n' "${GH_SHA256}" /tmp/gh.tar.gz | sha256sum --check --strict \
    && tar --extract --gzip --file /tmp/gh.tar.gz --directory /tmp \
    && install --mode 0755 "/tmp/gh_${GH_VERSION}_linux_amd64/bin/gh" /usr/local/bin/gh \
    && rm -rf /tmp/gh.tar.gz "/tmp/gh_${GH_VERSION}_linux_amd64"

COPY tooling/ci/image/requirements.lock /tmp/requirements.lock
RUN uv python install 3.14.3 \
    && uv venv --python 3.14.3 /opt/momentum-first/venv \
    && uv pip sync --python /opt/momentum-first/venv/bin/python /tmp/requirements.lock \
    && rm /tmp/requirements.lock

COPY tooling/ci/image/install-r-packages.R /tmp/install-r-packages.R
RUN Rscript /tmp/install-r-packages.R \
    && rm /tmp/install-r-packages.R \
    && rm -rf /tmp/downloaded_packages /root/.cache

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt/lists,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean \
    && apt-get update \
    && apt-get install -y --no-install-recommends fonts-urw-base35

RUN quarto --version \
    && python --version \
    && R --version | head -n 1 \
    && latexmk -v | head -n 1 \
    && biber --version | head -n 1 \
    && gh --version | head -n 1

LABEL org.opencontainers.image.source="https://github.com/ada-mercer/momentum-first" \
      org.opencontainers.image.description="Pinned figure and PDF build environment for Momentum First" \
      org.opencontainers.image.licenses="MIT"

WORKDIR /github/workspace
