from django.conf.urls import url, include
from rest_framework import routers
from base import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'hosts', views.HostViewSet)
router.register(r'spanins', views.SpaninViewSet)
router.register(r'phages', views.PhageViewSet, 'phages')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
