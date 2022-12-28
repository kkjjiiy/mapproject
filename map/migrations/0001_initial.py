# Generated by Django 4.1.2 on 2022-11-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("TimeStamp", models.CharField(max_length=100)),
                ("Latitude", models.CharField(max_length=100)),
                ("Longitude", models.CharField(max_length=100)),
            ],
        ),
    ]
