# Generated by Django 3.2 on 2023-05-09 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FishBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish_name', models.CharField(blank=True, max_length=50, null=True)),
                ('scientific_name', models.CharField(max_length=100)),
                ('english_name', models.CharField(max_length=100)),
                ('prohibition_size', models.CharField(max_length=50)),
                ('habitat', models.CharField(blank=True, max_length=100, null=True)),
                ('distribution', models.CharField(blank=True, max_length=100, null=True)),
                ('limit_start', models.CharField(max_length=50)),
                ('limit_end', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='fishBook_image/')),
            ],
            options={
                'db_table': 'fish_book',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CaughtFishInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caught_date', models.DateField()),
                ('myfish_photo', models.ImageField(upload_to='caughtFish_image/')),
                ('fish_book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fish_info.fishbook')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'caught_fish_info',
                'managed': True,
            },
        ),
    ]
