from django.core.management.base import BaseCommand
from base.models import Host, Spanin, Phage
import csv
from django.db import transaction

class Command(BaseCommand):
    help = 'parses biomolecular spanin csv and populates database'

    def add_arguments(self, parser):
        parser.add_argument('biomol_spanin_file', type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        spanin_type = {
            'e': 0,
            'o': 1,
            's': 2
        }

        with open(options['biomol_spanin_file'], 'rU') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for i, row in enumerate(csvreader):
                if i == 0 or not row[0]:
                    print 'empty or header'
                    continue

                host, created = Host.objects.get_or_create(
                    name=row[8],
                )

                i_spanin, created = Spanin.objects.get_or_create(
                    sequence=row[12],
                    accession=row[9],
                    sd_sequence=row[11]
                )

                o_spanin, created = Spanin.objects.get_or_create(
                    sequence=row[23],
                    accession=row[20],
                    sd_sequence=row[22]
                )

                phage, created = Phage.objects.get_or_create(
                    host=host,
                    name=row[0],
                    accession=row[2],
                    spanin_type=spanin_type[str.lower(row[4][0])],
                    i_spanin=i_spanin,
                    o_spanin=o_spanin
                )
