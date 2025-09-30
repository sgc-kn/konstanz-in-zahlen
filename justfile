all: check test test-cycle-all

ci: all

test:
  # run tests
  uv run pytest

check:
  # check .py formatting
  uv run ruff format --check
  # check .py style and redundancies
  uv run ruff check
  # check type hints
  uv run pyright

fix:
  # fix .py formatting
  uv run ruff format
  # fix .py style and redundancies, where possible
  uv run ruff check --fix

build-pydantic-models:
  uv run pytab create-pydantic-model data/*/[a-z]*.md

export-all:
  #!/usr/bin/env bash
  for d in data/* ; do
    if [ -d "$d" ]; then
      uv run pytab export $d || exit 1
    fi
  done

import-all:
  #!/usr/bin/env bash
  for d in data/* ; do
    if [ -d "$d" ]; then
      uv run pytab import $d || exit 1
    fi
  done

cycle-all: export-all import-all

# test: convert all datasets to excel and back; then check for changes to the csv files
test-cycle-all: cycle-all
  git diff --stat --exit-code data/*/*.csv
