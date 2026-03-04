#!/usr/bin/env bash
set -euo pipefail
set -x

# Recompile and install COPTER (run from this script regardless of CWD)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REAC_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# Allow overriding SUNDIALS install prefix via env var
SUNDIALS_PREFIX="${SUNDIALS_PREFIX:-/mnt/c/Users/annal/REACT/sundials-install}"

cd "$REAC_DIR"
echo "Cleaning and rebuilding COPTER in: $REAC_DIR"
echo "Using SUNDIALS prefix: $SUNDIALS_PREFIX"

echo "Running make distclean to force full rebuild..."
make distclean || true

echo "Reconfiguring after distclean..."
./configure --prefix="$REAC_DIR" \
  CPPFLAGS="-I${SUNDIALS_PREFIX}/include" \
  LDFLAGS="-L${SUNDIALS_PREFIX}/lib" \
  CFLAGS="-fPIC" \
  CXXFLAGS="-fPIC -O3 -fomit-frame-pointer -mtune=native -fstrict-aliasing -Wall"

echo "Running make (verbose)..."
make -j"$(nproc)" V=1

echo "Installing into $REAC_DIR"
make install

echo "Recompile/install finished." 
