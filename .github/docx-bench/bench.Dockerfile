# Scoring image of the docxide-pdf bench (docxide's own Dockerfile without the dev user, Node and Claude Code):
# mutool, Python and the fonts the scores depend on. Same as the local wc-bench image; toolchain pinned to match.
# Microsoft's core fonts are installed at build time under their EULA: never push this image to a public registry.
FROM ubuntu:24.04


# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    ca-certificates \
    build-essential \
    pkg-config \
    libssl-dev \
    mupdf-tools \
    python3 \
    python3-pip \
    python3-venv \
    fontconfig \
    fonts-liberation \
    fonts-dejavu \
    fonts-noto-core \
    fonts-freefont-ttf \
    fonts-crosextra-caladea \
    fonts-crosextra-carlito \
    fonts-croscore \
    fonts-open-sans \
    fonts-urw-base35 \
    fonts-noto-cjk \
    fonts-ipafont-gothic \
    fonts-ipafont-mincho \
    fonts-wqy-zenhei \
    fonts-wqy-microhei \
    fonts-nanum \
    fonts-lato \
    fonts-stix \
    bubblewrap \
    socat \
    && rm -rf /var/lib/apt/lists/*

# Microsoft core fonts: Arial, Verdana, Times New Roman, Courier New, Georgia,
# Comic Sans, Impact, Trebuchet MS, Webdings, Andale Mono (requires EULA acceptance)
# Use ports.ubuntu.com for arm64, archive.ubuntu.com for amd64
RUN ARCH=$(dpkg --print-architecture) \
    && if [ "$ARCH" = "amd64" ] || [ "$ARCH" = "i386" ]; then \
         REPO="http://archive.ubuntu.com/ubuntu"; \
       else \
         REPO="http://ports.ubuntu.com/ubuntu-ports"; \
       fi \
    && echo "deb ${REPO} noble multiverse" \
        > /etc/apt/sources.list.d/multiverse.list \
    && apt-get update \
    && echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" \
        | debconf-set-selections \
    && apt-get install -y --no-install-recommends ttf-mscorefonts-installer \
    && rm -rf /var/lib/apt/lists/*


# Fontconfig aliases: map common Microsoft font names to metrically-identical free substitutes.
# Carlito = Calibri (identical metrics), Caladea = Cambria, Liberation = Arial/TNR/Courier New.
# This ensures correct text layout even without the proprietary originals.
RUN mkdir -p /etc/fonts/conf.d \
    && cat > /etc/fonts/conf.d/99-ms-font-aliases.conf << 'EOF'
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <!-- Fonts NOT provided by ttf-mscorefonts-installer: alias to metrically-compatible substitutes -->
  <!-- Carlito = Calibri (identical metrics); Caladea = Cambria (identical metrics) -->
  <alias><family>Calibri</family><prefer><family>Carlito</family></prefer></alias>
  <alias><family>Calibri Light</family><prefer><family>Carlito</family></prefer></alias>
  <alias><family>Cambria</family><prefer><family>Caladea</family></prefer></alias>
  <alias><family>Cambria Math</family><prefer><family>Caladea</family></prefer></alias>
  <alias><family>Segoe UI</family><prefer><family>DejaVu Sans</family></prefer></alias>
  <alias><family>Tahoma</family><prefer><family>DejaVu Sans</family></prefer></alias>
  <alias><family>Consolas</family><prefer><family>Liberation Mono</family></prefer></alias>
  <alias><family>Century Gothic</family><prefer><family>Carlito</family></prefer></alias>
  <alias><family>Palatino Linotype</family><prefer><family>DejaVu Serif</family></prefer></alias>
  <alias><family>Arial Narrow</family><prefer><family>Liberation Sans Narrow</family></prefer></alias>
  <!-- CJK Microsoft font names → IPA equivalents -->
  <alias><family>MS Gothic</family><prefer><family>IPAGothic</family></prefer></alias>
  <alias><family>MS Mincho</family><prefer><family>IPAMincho</family></prefer></alias>
  <alias><family>MS PGothic</family><prefer><family>IPAPGothic</family></prefer></alias>
  <alias><family>MS PMincho</family><prefer><family>IPAPMincho</family></prefer></alias>
  <alias><family>ＭＳ ゴシック</family><prefer><family>IPAGothic</family></prefer></alias>
  <alias><family>ＭＳ 明朝</family><prefer><family>IPAMincho</family></prefer></alias>
  <!-- Aptos (Office 365 default) — not yet publicly available; use Carlito as stand-in -->
  <alias><family>Aptos</family><prefer><family>Carlito</family></prefer></alias>
  <alias><family>Aptos Display</family><prefer><family>Carlito</family></prefer></alias>
  <alias><family>Aptos Narrow</family><prefer><family>Carlito</family></prefer></alias>
  <alias><family>Aptos Serif</family><prefer><family>Caladea</family></prefer></alias>
  <alias><family>Aptos Mono</family><prefer><family>Liberation Mono</family></prefer></alias>
</fontconfig>
EOF

RUN fc-cache -f
RUN apt-get update && apt-get install -y --no-install-recommends time && rm -rf /var/lib/apt/lists/*
ENV RUSTUP_HOME=/opt/rustup CARGO_HOME=/opt/cargo PATH=/opt/cargo/bin:$PATH
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain 1.99.0 --profile minimal
WORKDIR /work
