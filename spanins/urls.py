from django.conf.urls import url, include
import os

urlpatterns = [
    url(os.environ.get('DJANGO_URL_PREFIX', ''), include([
        url(r'', include('base.urls')),
    ])),
]
