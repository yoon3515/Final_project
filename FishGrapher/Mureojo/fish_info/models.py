from django.db import models
# from django.contrib.auth import get_user_model
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import User

# Create your models here.

class FishBook(models.Model):
    fish_name = models.CharField(max_length=50, blank=True, null=True)
    scientific_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    prohibition_size = models.CharField(max_length=50)
    habitat = models.CharField(max_length=100, blank=True, null=True)
    distribution = models.CharField(max_length=100, blank=True, null=True)
    limit_start = models.CharField(max_length=50)
    limit_end = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='fishBook_image/')

    objects = models.Manager()  # 'objects' 속성 정의

    class Meta:
        managed = True
        db_table = 'fish_book'


User = get_user_model()

class CaughtFishInfo(models.Model):
    member = models.ForeignKey(User, models.DO_NOTHING)
    fish_book = models.ForeignKey('FishBook', models.DO_NOTHING)
    caught_date = models.DateField()
    myfish_photo = models.ImageField(upload_to='caughtFish_image/')

    objects = models.Manager()  # 'objects' 속성 정의

    class Meta:
        managed = True
        db_table = 'caught_fish_info'
