# https://github.com/TAMU-CPT/docker-recipes/blob/master/django/Dockerfile.inherit
FROM quay.io/tamu_cpt/django

# Add our project to the /app/ folder
ADD . /app/
# Install dependencies
RUN pip install -r /app/requirements.txt
# Set current working directory to /app
WORKDIR /app/

# Fix permissions on folder while still root, and collect static files for use
# if need be.
RUN chown -R django /app && \
	python manage.py collectstatic --noinput

ENV DJANGO_SETTINGS_MODULE=spanins.production \
	DJANGO_URL_PREFIX="spanindb/" \
	ALLOWED_HOSTS="*" \
	CORS_ORIGINS="cpt.tamu.edu"

RUN python manage.py update_index

# Drop permissions
USER django
