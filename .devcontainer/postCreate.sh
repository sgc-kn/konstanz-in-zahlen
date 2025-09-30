#!/usr/bin/env bash
set -e

# install uv (used for Python package management)
pipx install uv

# install just (for small maintenance scripts, defined in justfile)
pipx install rust-just

# create Python virtual environment .venv with all Python dependencies (used as default Python interpreter)
uv sync