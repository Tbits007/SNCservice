FROM python

WORKDIR /usr/src/auth

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/src

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY app app/

WORKDIR /usr/src/auth/app