FROM python:2.7-alpine
ADD requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip --no-cache-dir install -U pip && \
    pip --no-cache-dir install -r requirements.txt gunicorn && \
	addgroup -S django && \
	adduser -S -G django django
ADD . /app
RUN chown -R django /app
# Port to expose
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE=spanins.production \
	ALLOWED_HOSTS="*" \
	CORS_ORIGINS="cpt.tamu.edu"
USER django
ENTRYPOINT ["/app/docker-entrypoint.sh"]
