#!/bin/bash

python3 checkers_parser/manage.py makemigrations
python3 checkers_parser/manage.py migrate
python3 checkers_parser/manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8008