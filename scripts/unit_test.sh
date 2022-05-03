#!/bin/sh

# designed to be run from project-root

PYTHONPATH=src python -m pytest \
    -v \
    --cov-branch \
    --cov-report=term \
    --cov=src \
    tests $@

