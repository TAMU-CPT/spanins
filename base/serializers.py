from rest_framework import serializers
from base.models import Host, Spanin, Phage

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('id', 'name')

class BasicPhageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phage
        fields = ('name',)


class SpaninSerializer(serializers.HyperlinkedModelSerializer):
    phage_name=serializers.SerializerMethodField()
    class Meta:
        model = Spanin
        fields = ('id', 'sequence', 'gene_name', 'accession', 'type_code', 'score', 'phage_name')

    def get_phage_name(self, obj):
        if obj.i_spanin.all().count():
            return obj.i_spanin.all()[0].name
        elif obj.o_spanin.all().count():
            return obj.o_spanin.all()[0].name
        elif obj.u_spanin.all().count():
            return obj.u_spanin.all()[0].name

class PhageSerializer(serializers.HyperlinkedModelSerializer):
    host=HostSerializer(read_only=True, allow_null=True)
    i_spanin=SpaninSerializer(read_only=True, allow_null=True)
    o_spanin=SpaninSerializer(read_only=True, allow_null=True)
    u_spanin=SpaninSerializer(read_only=True, allow_null=True)
    spanin_type = serializers.SerializerMethodField()

    class Meta:
        model = Phage
        fields = ('id', 'host', 'name', 'accession', 'spanin_type', 'i_spanin', 'o_spanin', 'u_spanin')

    def get_spanin_type(self,obj):
        return obj.get_spanin_type_display()
