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
        search = self.request.query_params.get('search', None)
        spanin_type = self.request.query_params.get('spanin_type', None)
        if not search:
            search = 'pppw'
            queryset = SearchQuerySet().autocomplete(text=search)
            # queryset = Phage.objects.all()
        else:
            search = search.replace('_', '')
            search = search.replace('.', '')
            if spanin_type:
                queryset = SearchQuerySet().autocomplete(text=search).filter(spanin_type=int(spanin_type))
            else:
                queryset = SearchQuerySet().autocomplete(text=search)
            queryset = [p.object for p in queryset]
        return queryset
