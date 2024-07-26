import csv
from django.core.management.base import BaseCommand
from main.models import Pigment, Material

class Command(BaseCommand):
    help = 'Import pigments and materials from CSV'

    def handle(self, *args, **kwargs):
        # Import pigments from Pigment.csv
        with open('main/CSV/PIGMENTS.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                pigment, created = Pigment.objects.get_or_create(
                    id=row['ID'],
                    defaults={
                        'label_picture': row['LABLE PICTURE'],
                        'bottle_picture': row['BOTTLE PICTURE'],
                        'specific_name': row['SPECIFIC NAME'],
                        'description': row['DESCRIPTION'],
                        'color': row['COLOR'],
                        'shade': row['SHADE'],
                        'stopper': row['STOPPER'],
                        'geographical_origins': row['GEOGRAPHICAL ORGINS'],
                        'date_of_production': row['DATE OF PRODUCTION'],
                        'chemical_composition': row['CHEMICAL COMPOSITION'],
                        'physical_properties': row['PHISICAL PROPERTIES'],
                        'archive_description': row['DESCRIPTION FOR ARCHIVE SITE'],
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Pigment "{pigment.specific_name}" created'))
                else:
                    self.stdout.write(f'Pigment "{pigment.specific_name}" already exists')

        # Import materials from Material.csv
        with open('/main/CSV/MATERIALS.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                material, created = Material.objects.get_or_create(
                    id=row['ID'],
                    defaults={
                        'name': row['NAME'],
                        'm_pictures': row['M.PICTURES'],
                        'type_of_material': row['TYPE OF MATERIAL'],
                        'factory': row['FACTORY'],
                        'geographical_origins': row['GEOGRAFICAL ORIGINS'],
                        'physical_properties': row['PHISICAL PROPERTIES'],
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Material "{material.name}" created'))
                else:
                    self.stdout.write(f'Material "{material.name}" already exists')