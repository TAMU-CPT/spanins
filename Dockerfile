# https://github.com/TAMU-CPT/docker-recipes/blob/master/django/Dockerfile.inherit
FROM quay.io/tamu_cpt/django

# Add our project to the /app/ folder
ADD . /app/
# Install dependencies
RUN pip install -r /app/requirements.txt
# Set current working directory to /app
WORKDIR /app/


ENV DJANGO_SETTINGS_MODULE=spanins.production \
	DJANGO_URL_PREFIX="spanindb/" \
	ALLOWED_HOSTS="*" \
	CORS_ORIGINS="cpt.tamu.edu"

# Fix permissions on folder while still root, and collect static files for use
# if need be.
RUN chown -R django /app && \
	python manage.py collectstatic --noinput

RUN python manage.py update_index

# Drop permissions
USER django

ENTRYPOINT ["/app/.docker-entrypoint.sh"]
