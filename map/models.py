from django.db import models

# Create your models here.
class Car(models.Model):
    TimeStamp = models.CharField(max_length=100)
    Latitude = models.CharField(max_length=100)
    Longitude = models.CharField(max_length=100)
    CarName = models.CharField(max_length=100)
    CarSpeed = models.CharField(max_length=100)
    Heading = models.CharField(max_length=100)
    def __str__(self):
        """String for representing the Model object."""
        return self.CarName
    class Meta:
        ordering = ['CarName']

