from __future__ import unicode_literals

from django.db import models
import uuid

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

class Phage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.ForeignKey(Host)
    name = models.CharField(max_length=128)
    accession = models.CharField(max_length=64)
    spanin_type = models.IntegerField(choices=SPANIN_TYPES)
    i_spanin = models.ForeignKey(Spanin, related_name="i_spanin", null=True)
    o_spanin = models.ForeignKey(Spanin, related_name="o_spanin", null=True)
    u_spanin = models.ForeignKey(Spanin, related_name="u_spanin", null=True)
