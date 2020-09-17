# /bin/bash

source venv/bin/activate  # activate virtual environment
pip install pre-commit poetry # install base requirements
pip install isort mypy flake8
poetry install
