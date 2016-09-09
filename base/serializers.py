from rest_framework import serializers
from base.models import Host, Spanin, Phage

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('id', 'name')

class SpaninSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spanin
        fields = ('id', 'sequence', 'accession')

class PhageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phage
        fields = ('id', 'host', 'name', 'accession', 'spanin_type', 'i_spanin', 'o_spanin', 'u_spanin')
