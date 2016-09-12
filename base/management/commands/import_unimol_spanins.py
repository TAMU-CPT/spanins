from django.core.management.base import BaseCommand
from base.models import Host, Spanin, Phage
import csv
from django.db import transaction

class Command(BaseCommand):
    help = 'parses unimolecular spanin csv and populates database'

    def add_arguments(self, parser):
        parser.add_argument('unimol_spanin_file', type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        with open(options['unimol_spanin_file'], 'rU') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for i, row in enumerate(csvreader):
                if i == 0:
                    continue

                host, created = Host.objects.get_or_create(
                    name=row[5],
                )

                u_spanin, created = Spanin.objects.get_or_create(
                    sequence=row[9],
                    accession=row[6],
                    sd_sequence=row[8]
                )

                phage, created = Phage.objects.get_or_create(
                    host=host,
                    name=row[0],
                    accession=row[2],
                    spanin_type=3,
                    u_spanin=u_spanin
                )
