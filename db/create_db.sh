#!/bin/bash
set -e

WORKING_DIR=$(dirname "$0")

# Build project database for documentation and test creation.
psql -U vscode -d webtesterdb -f ${WORKING_DIR}/project.sql
psql -U vscode -d webtesterdb -f ${WORKING_DIR}/document.sql
psql -U vscode -d webtesterdb -f ${WORKING_DIR}/section.sql
psql -U vscode -d webtesterdb -f ${WORKING_DIR}/case.sql
psql -U vscode -d webtesterdb -f ${WORKING_DIR}/step.sql

psql -U vscode -d webtesterdb -f ${WORKING_DIR}/status.sql
