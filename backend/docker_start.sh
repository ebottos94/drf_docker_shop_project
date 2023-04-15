#!/bin/sh
python /code/manage.py migrate

while true; do
    echo "Re-starting Django"
    python /code/manage.py runserver 0.0.0.0:8000
    sleep 2
done