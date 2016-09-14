# from django.shortcuts import render
from haystack.query import SearchQuerySet
from rest_framework import viewsets
from base.serializers import HostSerializer, SpaninSerializer, PhageSerializer
from base.models import Host, Spanin, Phage

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class SpaninViewSet(viewsets.ModelViewSet):
    queryset = Spanin.objects.all()
    serializer_class = SpaninSerializer

class PhageViewSet(viewsets.ModelViewSet):
    serializer_class = PhageSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search[value]', None)
        if not search:
            queryset = Phage.objects.all()
        else:
            queryset = SearchQuerySet().autocomplete(text=search)
            queryset = [p.object for p in queryset]
        return queryset
