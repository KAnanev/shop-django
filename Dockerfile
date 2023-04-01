FROM python:3.11-slim
WORKDIR /opt/app
ARG DJANGO_ENV

ENV DJANGO_SETTINGS_MODULE 'config.settings'
# python:
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
# poetry:
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=false
ENV PATH="$POETRY_HOME/bin:$PATH"

COPY install-poetry.py install-poetry.py
RUN python3 -m pip install poetry

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry install --no-interaction --no-ansi

COPY . .

ENTRYPOINT ["poetry", "run", "gunicorn", "config.wsgi"]