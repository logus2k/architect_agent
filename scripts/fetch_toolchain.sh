#!/usr/bin/env bash
# Fetch the SysML v2 Pilot Implementation into data/sysml-toolchain/.
#
# Run once at provisioning time. The Architect Agent itself never reaches the
# network — this is the only step that does, and it is deliberately separate so
# the runtime stays air-gapped.
set -euo pipefail

VERSION="${SYSML_KERNEL_VERSION:-0.60.1}"
RELEASE="${SYSML_KERNEL_RELEASE:-2026-05}"
URL="https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/releases/download/${RELEASE}/jupyter-sysml-kernel-${VERSION}.zip"

DEST="$(cd "$(dirname "$0")/.." && pwd)/data/sysml-toolchain"
mkdir -p "$DEST"

if [ -f "$DEST/jupyter-sysml-kernel-${VERSION}-all.jar" ]; then
    echo "toolchain already present at $DEST"
else
    tmp="$(mktemp -d)"
    trap 'rm -rf "$tmp"' EXIT
    echo "downloading $URL ..."
    curl -fsSL -o "$tmp/kernel.zip" "$URL"
    unzip -q "$tmp/kernel.zip" -d "$tmp/unpacked"
    cp "$tmp/unpacked/sysml/jupyter-sysml-kernel-${VERSION}-all.jar" "$DEST/"
    cp -r "$tmp/unpacked/sysml/sysml.library" "$DEST/"
    echo "installed jar + standard library"
fi

echo "compiling ArchitectTool ..."
mkdir -p "$DEST/classes"
javac -cp "$DEST/jupyter-sysml-kernel-${VERSION}-all.jar" \
      -d "$DEST/classes" "$(dirname "$0")/../java/ArchitectTool.java"
echo "toolchain ready"
