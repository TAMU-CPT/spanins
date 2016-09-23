import django
import string
# import sys
import os

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'spanins.settings'
application = get_wsgi_application()

from base.models import Spanin
django.setup()


"""
AGGAGGT is the ideal Shine-Dalgarno sequence.
This is a crude frequency map of SD sequences among different spanin types.
    eis, eos: embedded i/o spanins
    ois, oos: overlapping i/o spanins
    sis, sos: separated i/o spanins
    us:       unimolecular spanins
"""

# predetermined sequences. Will add more later.
sds = ['AGGAGGT',
       'GGAGGT', 'AGGAGG',
       'GAGGT', 'GGAGG', 'AGGAG',
       'AGGT', 'GAGG', 'GGAG', 'AGGA',
       'GGT', 'AGG', 'GAG', 'GGA']

freq = {key:{'eis':0, 'eos':0, 'ois':0, 'oos':0, 'sis':0, 'sos':0, 'us':0} for key in sds}

spanins = Spanin.objects.all()
for spanin in spanins:
    sd = str(spanin.sd_sequence)
    sd = sd.translate(None, string.ascii_lowercase)
    if spanin.accession == '331028055' or len(sd) < 3:
        continue
    if sd in freq:
        freq[sd][spanin.type_code] += 1
    # else:
        # freq[sd] = {'eis':0, 'eos':0, 'ois':0, 'oos':0, 'sis':0, 'sos':0, 'us':0}

for sd in sds:
    print sd, freq[sd]
