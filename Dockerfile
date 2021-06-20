# FROM python:3.8
FROM registry.redhat.io/rhel8/python-39:latest

LABEL name="Simple blog example using FastAPI, Uvicorn, Orator and Graphene" \
    maintainer="Mitchell Murphy<mitch.murphy@gmail.com>" \
    documentation="https://gitlab.com/kaizo_pipe/flaskql" \
    license="GPL-2.0-only"

ARG APP_ROOT=/usr/src/app/

# set work directory
WORKDIR ${APP_ROOT}

USER root
# set environment variables
ARG YOUR_ENV

ENV APP_NAME=superfast-blog \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1

# System deps:
COPY pyproject.toml poetry.lock ${APP_ROOT}/

RUN pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false \
    && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi --no-dev \
    && chown -R 1001:0 ${APP_ROOT} \
    && chmod -R +w ${APP_ROOT}

USER 1001
COPY . ${APP_ROOT}

EXPOSE 8080

CMD ["python", "asgi.py"]