FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY .. /code/

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 8008

COPY ./deploy/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]