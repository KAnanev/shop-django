# The base image we want to inherit from
FROM python:3.10-alpine

ARG DJANGO_ENV

ENV PATH="${PATH}:/root/.poetry/bin"

ENV DJANGO_ENV=${DJANGO_ENV} \

  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \

  # poetry:
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

# System deps:
RUN apk add --no-cache --virtual build-deps \
    curl `#  poetry` \
    make gcc g++ `# make` \
    libjpeg-turbo-dev zlib-dev libffi-dev cairo-dev libwebp-dev `# pillow`

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# set work directory
WORKDIR /code
COPY pyproject.toml poetry.lock /code/

# Install dependencies:
RUN apk add --no-cache \
    git `# dependencies` \
    libjpeg-turbo zlib libffi cairo libwebp `# pillow`

RUN source $HOME/.poetry/env
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi
RUN apk del --no-cache build-deps

# copy project
COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=settings.local"]