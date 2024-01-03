FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY .. /code/

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 8008

RUN python3 checkers_parser/manage.py makemigrations
RUN python3 checkers_parser/manage.py migrate
RUN python3 checkers_parser/manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8008"]
