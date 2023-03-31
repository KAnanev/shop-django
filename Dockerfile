FROM python:3.11-slim
WORKDIR /opt/app
ARG DJANGO_ENV

ENV DJANGO_SETTINGS_MODULE 'config.settings'
# python:
ENV  PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
# poetry:
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=false
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN export POETRY_HOME=/opt/poetry
RUN python -m pip install --upgrade pip
RUN pip install poetry



COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "gunicorn", "config.wsgi"]

