from django.db import models

# Create your models here.

class PictureSave(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fish_images')

    def __str__(self):
        return self.name
