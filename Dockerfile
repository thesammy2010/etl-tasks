FROM python:3.8

ARG ENVIROMENT

ENV ENVIROMENT=${ENVIROMENT} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.3

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /i-like-python
COPY poetry.lock pyproject.toml /i-like-python/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$ENVIROMENT" == production && echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /i-like-python
