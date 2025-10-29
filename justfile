# run all non-destructive tests
all: check test

# run all CI tests (potentially destructive)
ci: all test-reformat-all-models test-reformat-all-tables

# run Python-based tests
test:
  # run tests
  uv run pytest

# check Python formatting
check:
  # check .py formatting
  uv run ruff format --check
  # check .py style and redundancies
  uv run ruff check
  # check type hints
  uv run pyright

# attempt to fix Python formatting
fix:
  # fix .py formatting
  uv run ruff format
  # fix .py style and redundancies, where possible
  uv run ruff check --fix

# create the data/*/*.py files from the data/*/*.md schema
build-pydantic-models:
  uv run pytab create-pydantic-model data/*/[a-z]*.md

# export all datasets to excel
export-all:
  #!/usr/bin/env bash
  for d in data/* ; do
    if [ -d "$d" ]; then
      uv run pytab export $d || exit 1
    fi
  done

# import all datasets from excel (assumes export format)
import-all:
  #!/usr/bin/env bash
  for d in data/* ; do
    if [ -d "$d" ]; then
      uv run pytab import $d || exit 1
    fi
  done

# reformat all data/*/*.csv files (potentially destructive)
reformat-all-tables: export-all import-all

# test CSV formatting (potentially destructive)
test-reformat-all-tables: reformat-all-tables
  git diff --stat --exit-code data/*/*.csv

# reformat all data/*/*.md schema files (potentially destructive)
reformat-all-models:
  uv run pytab format-markdown data/*/[a-z]*.md

# test schema formatting (potentially destructive)
test-reformat-all-models: reformat-all-models
  git diff --stat --exit-code data/*/[a-z]*.md

# upgrade python dependencies
upgrade:
  uv lock --upgrade && uv sync