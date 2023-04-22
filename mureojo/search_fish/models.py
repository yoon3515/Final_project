from django.db import models

# Create your models here.

#from djongo.models import MongoModel,fields

#
class Fishes(models.Model):
    #_id = models.CharField(max_length=50),
    fish_name =models.CharField(max_length=50),
    scientific_name = models.CharField(max_length=50),
    english_name=models.CharField(max_length=50),
    prohibition_size=models.CharField(max_length=50),
    habitat=models.CharField(max_length=50),
    distribution=models.CharField(max_length=50),
    limit_start=models.CharField(max_length=50),
    limit_end=models.CharField(max_length=50),
    description=models.CharField(max_length=50),
    image_url=models.CharField(max_length=50),

    def __str__(self):
        return self.fish_name

