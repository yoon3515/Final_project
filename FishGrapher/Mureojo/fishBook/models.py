from django.db import models
from django.contrib.auth import get_user_model

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
    image = models.ImageField()

    objects = models.Manager()  # 'objects' 속성 정의

    class Meta:
        managed = False
        db_table = 'fish_book'



class CaughtFishInfo(models.Model):
    User = get_user_model()
    member = models.ForeignKey(User, models.DO_NOTHING, related_name='caught_fish_info_set')
    fish_book = models.ForeignKey('FishBook', models.DO_NOTHING, related_name='caught_fish_infos')
    caught_date = models.DateField()
    myfish_photo = models.ImageField(upload_to='caughtFish_image/')

    objects = models.Manager()  # 'objects' 속성 정의

    class Meta:
        managed = False
        db_table = 'caught_fish_info'



# class AccountsUser(models.Model):
#     username = models.CharField(max_length=255, blank=True, null=True)
#     email = models.CharField(unique=True, max_length=50)
#     password = models.CharField(max_length=50)
#
#     objects = models.Manager()  # 'objects' 속성 정의
#
#     class Meta:
#         managed = False
#         db_table = 'accounts_user'

