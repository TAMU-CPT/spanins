# from django.shortcuts import render
from haystack.query import SearchQuerySet
from rest_framework import viewsets
import string
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from base.models import Host, Spanin, Phage
from base.serializers import HostSerializer, SpaninSerializer, PhageSerializer
import os

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
            if spanin_type:
                queryset = SearchQuerySet().filter(spanin_type=int(spanin_type)).order_by('name')
                queryset = [p.object for p in queryset]
            else:
                queryset = Phage.objects.all().order_by('name')
        else:
            search = search.replace('_', '')
            search = search.replace('.', '')
            if spanin_type:
                queryset = SearchQuerySet().autocomplete(text=search).filter(spanin_type=int(spanin_type)).order_by('name')
            else:
                queryset = SearchQuerySet().autocomplete(text=search).order_by('name')
            queryset = [p.object for p in queryset]
        return queryset

def phage_name(obj):
    if obj.i_spanin.all().count():
        return obj.i_spanin.all()[0].name
    elif obj.o_spanin.all().count():
        return obj.o_spanin.all()[0].name
    elif obj.u_spanin.all().count():
        return obj.u_spanin.all()[0].name

keep = []
with open(os.path.realpath('spanin_names.txt'), 'r') as handle:
    keep = [h.strip() for h in handle.read().split('\n') if h.strip()]

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def spanin_freq(request):
    """
    AGGAGGT is the ideal Shine-Dalgarno sequence.
    This is a crude frequency map of SD sequences among different spanin types.
        eis, eos: embedded i/o spanins
        ois, oos: overlapping i/o spanins
        sis, sos: separated i/o spanins
        us:       unimolecular spanins
    """

    # predetermined sequences.
    sds = ['AGGAGGT', #18
           'GGAGGT',  #16
           'AGGAGG',  #16
           'GGGGGG',  #14
           'GGAGG',   #14
           'GGGGG',   #13
           'GAGGT',   #13
           'AGGAG',   #13
           'GAGG',    #11
           'GGAG',    #11
           'AGGT',    #10
           'AGGA',    #10
           'GGGG',    #10
           'GGT',     #8
           'AGG',     #8
           'GAG',     #8
           'GGA',     #8
           'GGG',     #7
           ''
           ]

    freq = {key:{'eis':0, 'eos':0, 'ois':0, 'oos':0, 'sis':0, 'sos':0, 'us':0} for key in sds}

    count = 0
    spanins = Spanin.objects.all()
    for spanin in spanins:
        sd = str(spanin.sd_sequence).strip()
        # flag for ignoring spanin
        if '*' in sd:
            # count += 1
            continue
        if phage_name(spanin) in keep:
            sd = sd.translate(None, string.ascii_lowercase)
            if sd in freq:
                count += 1
                freq[sd][spanin.type_code] += 1
        # else:
            # count += 1
            # freq[sd] = {'eis':0, 'eos':0, 'ois':0, 'oos':0, 'sis':0, 'sos':0, 'us':0}
            # freq[sd][spanin.type_code] += 1

    print "*******"
    print count
    print "*******"
    return Response(freq)

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def spanin_score(request):
    sds = {
        18: ['AGGAGGT'],
        16: ['GGAGGT', 'AGGAGG'],
        14: ['GGGGGG', 'GGAGG'],
        13: ['GGGGG', 'GAGGT', 'AGGAG'],
        11: ['GAGG', 'GGAG'],
        10: ['AGGT', 'AGGA', 'GGGG'],
        8: ['GGT', 'AGG', 'GAG', 'GGA'],
        7: ['GGG'],
        0: [''],
    }

    freq = {key:{'eis':0, 'eos':0, 'ois':0, 'oos':0, 'sis':0, 'sos':0, 'us':0} for key in sds}

    count = 0
    spanins = Spanin.objects.all()
    for spanin in spanins:
        sd = str(spanin.sd_sequence).strip()
        # flag for ignoring spanin
        if '*' in sd:
            # count += 1
            continue
        if phage_name(spanin) in keep:
            sd = sd.translate(None, string.ascii_lowercase)
            for key in sds:
                if sd in sds[key]:
                    count += 1
                    freq[key][spanin.type_code] += 1

    print "*******"
    print count
    print "*******"
    return Response(freq)

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def chord_plot(request):
    scores = {}
    phages = Phage.objects.all()
    for phage in phages:
        if phage.name in keep:
            if phage.spanin_type == int(request.query_params['type']):
                sc = str((phage.i_spanin.spanin_score(), phage.o_spanin.spanin_score()))
                if sc in scores:
                    scores[sc] += 1
                else:
                    scores[sc] = 1

    return Response(scores)
