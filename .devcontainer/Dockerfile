FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

ENV PYTHONUNBUFFERED 1

RUN pip install pip --upgrade
RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN echo "Config virtualenvs" && \
    poetry config virtualenvs.in-project true 

RUN apt-get update && apt-get install -y postgresql postgresql-contrib 

RUN apt-get install -y sqlite3 nodejs npm

# Instalar dependências do projeto
# RUN poetry install --no-root  --no-interaction --no-ansi

# RUN echo "Install dependencies and Clear Poetry Cache files" && \
#     poetry install --no-root --without dev && rm -rf $POETRY_CACHE_DIR

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>



