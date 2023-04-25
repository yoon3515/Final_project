from django.db import models

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
    image_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'fish_book'


class CaughtFishInfo(models.Model):
    member = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    fish_book = models.ForeignKey('FishBook', models.DO_NOTHING)
    caught_date = models.DateField()
    myfish_photo = models.CharField(db_column='myFish_photo', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caught_fish_info'
