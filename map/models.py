from django.db import models

# Create your models here.
class Car(models.Model):
    TimeStamp = models.CharField(max_length=100)
    Latitude = models.CharField(max_length=100)
    Longitude = models.CharField(max_length=100)