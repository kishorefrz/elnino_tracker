import os
from django.core.management.base import BaseCommand
from tracker.models import Nino34Reading

class Command(BaseCommand):
    help = "Load Nino 3.4 monthly data from nino34.txt"

    def handle(self, *args, **options):
        # nino34.txt is one level up, in elnino_tracker/
        file_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "nino34.txt")
        file_path = os.path.abspath(file_path)

        count = 0
        with open(file_path) as f:
            for line in f:
                parts = line.split()
                if len(parts) == 13 and parts[0].isdigit():
                    year = int(parts[0])
                    for month, val in enumerate(parts[1:], start=1):
                        v = float(val)
                        if v > -90:
                            Nino34Reading.objects.update_or_create(
                                year=year, month=month,
                                defaults={"anomaly": v}
                            )
                            count += 1

        self.stdout.write(self.style.SUCCESS(f"Loaded {count} readings"))