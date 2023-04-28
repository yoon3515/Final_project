# Generated by Django 4.1.6 on 2023-04-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fishBook", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CaughtFishInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("caught_date", models.DateField()),
                (
                    "myfish_photo",
                    models.CharField(db_column="myFish_photo", max_length=200),
                ),
            ],
            options={
                "db_table": "caught_fish_info",
                "managed": False,
            },
        ),
    ]