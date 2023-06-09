#!/usr/bin/env sh

set -o errexit
set -o nounset

pyclean () {
  find . | grep -E '(__pycache__|\.py[cod]$)' | xargs rm -rf
}

run_linter () {
  echo ruff...
  ruff check .

  echo flake8...
  flake8 .
}

# Removing cache:
pyclean

# Cleaning:
trap pyclean EXIT INT TERM

# Running linter:
run_linter
