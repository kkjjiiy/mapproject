# Generated by Django 4.1.2 on 2022-11-08 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0003_car_delete_cars"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car", name="Latitude", field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name="car", name="Longitude", field=models.FloatField(max_length=100),
        ),
    ]