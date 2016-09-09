# from django.shortcuts import render
from rest_framework import viewsets, filters
from base.serializers import HostSerializer, SpaninSerializer, PhageSerializer
from base.models import Host, Spanin, Phage

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class SpaninViewSet(viewsets.ModelViewSet):
    queryset = Spanin.objects.all()
    serializer_class = SpaninSerializer

class PhageViewSet(viewsets.ModelViewSet):
    queryset = Phage.objects.all()
    serializer_class = PhageSerializer
