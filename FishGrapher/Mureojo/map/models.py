from django.db import models

class FishingSpot(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name
