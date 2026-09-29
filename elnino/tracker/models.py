from django.db import models

# Create your models here.
class Nino34Reading(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    anomaly = models.FloatField()

    class Meta:
        unique_together = ("year", "month")
        ordering = ["year", "month"]

    def __str__(self):
        return f"{self.year}-{self.month:02d}: {self.anomaly}"