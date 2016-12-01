#!/bin/bash

python manage.py migrate
python /docker/create_admin.py

# Start Gunicorn processes
echo Starting Gunicorn.
gunicorn ${DJANGO_WSGI_MODULE}:application \
	--bind 0.0.0.0:8000 \
	--workers 2 \
	"$@"
