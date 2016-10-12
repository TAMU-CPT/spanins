from __future__ import unicode_literals

from django.db import models
import uuid
import string

SPANIN_TYPES = (
    (0, 'embedded'),
    (1, 'overlapping'),
    (2, 'separate'),
    (3, 'unimolecular'),
)

class Host(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)

class Spanin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sequence = models.TextField()
    accession = models.CharField(max_length=64)
    gene_name = models.CharField(max_length=64)
    type_code = models.CharField(max_length=8)
    score = models.IntegerField(default=0)
    sd_sequence = models.TextField(blank=True, null=True)

    def spanin_score(self):
        sds = { 'AGGAGGT':18,
               'GGAGGT':16,
               'AGGAGG':16,
               'GGGGGG':14,
               'GGAGG':14,
               'GGGGG':13,
               'GAGGT':13,
               'AGGAG':13,
               'GAGG':11,
               'GGAG':11,
               'AGGT':10,
               'AGGA':10,
               'GGGG':10,
               'GGT':8,
               'AGG':8,
               'GAG':8,
               'GGA':8,
               'GGG':7,
               '': 0 }
        sd = str(self.sd_sequence).strip()
        if '*' not in sd:
            sd = sd.translate(None, string.ascii_lowercase)
            return sds[sd]




class Phage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.ForeignKey(Host)
    name = models.CharField(max_length=128)
    accession = models.CharField(max_length=64)
    spanin_type = models.IntegerField(choices=SPANIN_TYPES)
    i_spanin = models.ForeignKey(Spanin, related_name="i_spanin", null=True)
    o_spanin = models.ForeignKey(Spanin, related_name="o_spanin", null=True)
    u_spanin = models.ForeignKey(Spanin, related_name="u_spanin", null=True)

    def accession_mod(self):
        a = self.accession.replace('_', '')
        a = a.replace('.', '')
        return a
