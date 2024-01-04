FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY .. /code/

COPY poetry.lock pyproject.toml /
RUN curl -sSL https://install.python-poetry.org | python -
RUN PATH="$PATH:$HOME/.local/bin" && poetry config virtualenvs.create false
RUN PATH="$PATH:$HOME/.local/bin" && poetry install --no-root

EXPOSE 8008

COPY ./deploy/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]