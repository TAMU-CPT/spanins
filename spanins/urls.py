from django.conf.urls import url, include

urlpatterns = [
    url(os.environ.get('DJANGO_URL_PREFIX', ''), include([
        url(r'', include('base.urls')),
    ])),
]
