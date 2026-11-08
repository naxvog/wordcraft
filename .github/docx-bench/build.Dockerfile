# Build image of the docxide-pdf bench: what `wordcraft-cli` needs to compile. Same as the local wc-ci image
# without clippy, rustfmt and the wasm target; toolchain pinned to match.
FROM ubuntu:24.04
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl git build-essential pkg-config cmake python3 \
    libxkbcommon-dev libwayland-dev libx11-dev libxrandr-dev libxi-dev libxcursor-dev libxcb1-dev \
    libgl1-mesa-dev libvulkan-dev libgtk-3-dev libfontconfig1-dev libfreetype-dev libasound2-dev libssl-dev \
    fontconfig fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*
ENV RUSTUP_HOME=/opt/rustup CARGO_HOME=/opt/cargo PATH=/opt/cargo/bin:$PATH
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain 1.99.0 --profile minimal
RUN git config --global --add safe.directory '*'
WORKDIR /src
